#!/usr/bin/env python3
"""Simulador Monte Carlo de la Prueba 1 de Día 30 (expedición mínima).

Port de las reglas del JavaScript de fuentes/prueba_1_simulador.html (la
implementación jugable exacta del kit de prueba 1) más jugadores automáticos.
Solo librería estándar.

Uso:
  python3 herramientas/simular_prueba1.py                 # matriz completa, 10.000 partidas por configuración
  python3 herramientas/simular_prueba1.py -n 2000         # menos partidas
  python3 herramientas/simular_prueba1.py --estilo mixto --armas CB --entrada puerta -n 20000
  python3 herramientas/simular_prueba1.py --regla horda=6 --regla pistola_ruido=3   # variantes de reglas
  python3 herramientas/simular_prueba1.py --variantes     # batería de ajustes propuestos en diseno/balance.md

Estilos automáticos:
  sigiloso: Sigilo (2 PA) siempre que se pueda; con 1 PA suelto, Caminar. Cuchillo primero.
  ruidoso : Correr + Caminar (4 zonas por turno). Pistola primero, y dispara a zombies
            alerta a 2 zonas antes de que lleguen. Bate antes que cuchillo.
  mixto   : por cada paso elige el movimiento más rápido cuyo ruido no oye ningún zombie
            (Correr > Caminar > Sigilo). Arma cuerpo a cuerpo; pistola solo con 2+ zombies
            en la zona o con 3 de sangre o menos.
Entradas: puerta (principal, D2-E2), vidriera (E1-E2), trasera (F3-F2, forzar).
Armas: CB = cuchillo+bate, CP = cuchillo+pistola, BP = bate+pistola.
"""
import argparse
import random
import sys
from collections import Counter, deque
from multiprocessing import Pool

# ---------------------------------------------------------------------------
# Reglas (valores del kit de prueba 1). Las variantes se cambian con --regla.
# ---------------------------------------------------------------------------
REGLAS_BASE = {
    "horda": 5,              # fichas para que llegue la horda
    "horda_zombies": 3,      # caminantes que trae la horda
    "pistola_ruido": 4,      # nivel de ruido de la pistola (4 = Máximo)
    "bate_ruido": 2,         # nivel de ruido del bate (2 = Medio; las cartas dicen 1 = Bajo)
    "balas": 6,
    "zombi_ataque": 2,       # bonificador del ataque zombie (d20 + 2)
    "defensa": 11,           # Defensa del superviviente
    "zombi_def": 8,
    "zombi_vida": 5,
    "sangre": 6,
    "sigilo_pa": 2,
    "aparicion_dia": 1,      # d6 <= este valor: aparece un errante (de día)
    "aparicion_noche": 2,
    "noche": 9,              # turno en que anochece
    "turnos": 12,
    "botin_mod": 0,          # suma fija a las tiradas de registro de la farmacia
    "disipacion": 1,
    "correr_ruido": 2,       # nivel de ruido de Correr
    "correr_fichas": 1,      # fichas de ruido que deja Correr
    "kit_deposito": 5,       # resultado mínimo (d6 + mod) para el kit en el depósito
    "kit_salon": 6,          # ídem en el salón
    "bate_dano": 6,
    "cuchillo_dano": 4,
    "pistola_dano": 10,
    "pistola_mod_dano": 0,
    "efectos_js": 0,         # 1 = efectos de zona permanentes, como el JS
    "derribar_js": 0,        # 1 = los zombies también derriban vidriera y puerta con llave, como el JS
    "mod_fue": 1,            # modificador de Fuerza (ataque y daño cuerpo a cuerpo)
    "mod_des": 1,            # modificador de Destreza (ataque con pistola)
    "hab_vendar1": 0,        # Marta: primeros auxilios por 1 PA
    "hab_forzar": 0,         # Sofía: forzar por 1 PA y un nivel menos de ruido
    "hab_ventaja_fuego": 0,  # Raúl: ventaja en el primer disparo de la expedición
}

# Supervivientes de mesa_online.html: (F, D, C, P) y habilidad aplicable a la prueba 1
SUPERVIVIENTES = {
    'Neutro (kit)': ((3, 3, 3, 3), {}),
    'Marta (enfermera)': ((2, 3, 3, 4), {'hab_vendar1': 1}),
    'Raúl (ex policía)': ((4, 3, 3, 2), {'hab_ventaja_fuego': 1}),
    'Sofía (mecánica)': ((3, 4, 3, 2), {'hab_forzar': 1}),
    'Tomás (cocinero)': ((4, 2, 4, 2), {}),
    'Nico (estudiante)': ((1, 5, 2, 4), {}),
    'Aurelio (cazador)': ((3, 3, 2, 4), {}),
    'Elena (maestra)': ((2, 2, 3, 5), {}),
}
def reglas_superviviente(nombre, R):
    (F, D, Co, P), hab = SUPERVIVIENTES[nombre]
    R = dict(R)
    R['mod_fue'] = F - 2
    R['mod_des'] = D - 2
    R['defensa'] = 10 + D - 2
    R.update(hab)
    return R

C, N = 6, 18
LET = "ABCDEF"
TYPE = ['calle'] * 6 + ['patio', 'casa', 'casa', 'calle', 'farm', 'farm', 'base', 'calle', 'calle', 'calle', 'calle', 'estac']
def BLD(i):
    t = TYPE[i]
    return 'casa' if t == 'casa' else 'farm' if t == 'farm' else None
def ek(a, b):
    return (a, b) if a < b else (b, a)
OPEN = {(7, 13): 'door', (9, 10): 'door', (4, 10): 'window', (11, 17): 'locked'}
PASS = {'open', 'opened', 'broken'}
SOUND = {'wall', 'door', 'locked', 'window'}
SIGHT = {'wall', 'door', 'locked'}
FICHAS = [0, 1, 1, 2, 3]
RANGE = [0, 1, 2, 3, 99]
BORDER = [0, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17]
SIZE = {'cuchillo': 1, 'bate': 2, 'pistola': 1, 'venda': 1, 'kit': 1, 'analgesico': 1, 'comida': 1}
PUNTOS = {'kit': 3, 'analgesico': 2, 'venda': 1, 'comida': 1}
ZONES = {1: 'Cabeza', 2: 'Torso', 3: 'Torso', 4: 'BrazoI', 5: 'BrazoD', 6: 'Piernas'}

def nb(i):
    c, r = i % C, i // C
    o = []
    if c > 0: o.append(i - 1)
    if c < C - 1: o.append(i + 1)
    if r > 0: o.append(i - C)
    if r < 2: o.append(i + C)
    return o
NB = [nb(i) for i in range(N)]
GROUPS = [[7, 8], [10, 11]] + [[i] for i in range(N) if not BLD(i)]
def manh(a, b):
    return abs(a % C - b % C) + abs(a // C - b // C)
HORDE_CELL = {}
for g in GROUPS:
    HORDE_CELL[g[0]] = sorted(BORDER, key=lambda x: manh(x, g[0]))[0]


class Fin(Exception):
    pass


class Juego:
    def __init__(self, rng, armas, R):
        self.rng = rng
        self.R = R
        self.edges = {}
        for i in range(N):
            for j in NB[i]:
                if j > i:
                    k = (i, j)
                    self.edges[k] = OPEN.get(k) or ('wall' if BLD(i) != BLD(j) else 'open')
        self.armas = armas
        self.inv = list(armas) + ['venda', 'venda']
        self.found = []
        self.W = {
            'cuchillo': (R['cuchillo_dano'], R['mod_fue'], 0, True),
            'bate': (R['bate_dano'], R['mod_fue'], R['bate_ruido'], True),
            'pistola': (R['pistola_dano'], R['pistola_mod_dano'], R['pistola_ruido'], False),
        }
        self.turno = 1
        self.pa = 3
        self.sangre = R['sangre']
        self.pos = 12
        self.hidden = False
        self.stunned = False
        self.ran = False
        self.ammo = R['balas']
        self.jam = False
        self.wounds = []  # [zona, tipo, vendada]
        self.head = 0
        self.bites = 0
        self.zombies = [[2, 0, False], [5, 0, False], [15, 0, False]]  # [celda, daño, alerta]
        self.tokens = [0] * N
        self.events = []
        self.farm = False
        self.farm_mod = 0
        self.casa = False
        self.searches = [0] * N
        self.hordas = 0
        self.over = False
        self.win = False
        self.razon = ''
        self.uso = Counter()
        self.kills = Counter()
        self.ataques_recibidos = 0
        self.heridas = 0
        self.turno_kit = None
        self.disparos = 0

    def d(self, n):
        return self.rng.randint(1, n)

    # --- utilidades ---
    def night(self):
        return self.turno >= self.R['noche']
    def effect(self, z):
        # Kit: el efecto dura mientras haya ahí una herida que no sea rasguño.
        # Una laceración vendada deja de contar; fractura y mordedura duran toda la expedición.
        # (El JS los deja permanentes para cualquier tipo: R['efectos_js'] = 1 reproduce eso.)
        if self.R['efectos_js']:
            return any(w[0] == z and w[1] != 'Rasguño' for w in self.wounds)
        return any(w[0] == z and w[1] != 'Rasguño' and not (w[1] == 'Laceración' and w[2]) for w in self.wounds)
    def cap(self):
        return 6 - (1 if self.effect('BrazoI') else 0)
    def load(self):
        return sum(SIZE[k] for k in self.inv)
    def has(self, k):
        return k in self.inv
    def zhere(self, c):
        return [z for z in self.zombies if z[0] == c]
    def edge(self, a, b):
        return self.edges[ek(a, b)]

    # --- ruido ---
    def noise(self, cell, lv, fichas=None):
        if lv <= 0:
            return
        self.tokens[cell] += FICHAS[lv] if fichas is None else fichas
        self.events.append((cell, lv))

    def hear(self, src, lv, tgt):
        best = [None] * N
        best[src] = (lv, 0)
        q = deque([src])
        while q:
            a = q.popleft()
            bl, bd = best[a]
            for j in NB[a]:
                nl = bl - (1 if self.edges[ek(a, j)] in SOUND else 0)
                nd = bd + 1
                if nl <= 0 or nd > RANGE[nl]:
                    continue
                o = best[j]
                if o is None or nl > o[0] or (nl == o[0] and nd < o[1]):
                    best[j] = (nl, nd)
                    q.append(j)
        return best[tgt]

    def reach(self, frm, steps):
        dist = [-1] * N
        dist[frm] = 0
        q = deque([frm])
        while q:
            a = q.popleft()
            if dist[a] >= steps:
                continue
            for j in NB[a]:
                if dist[j] < 0 and self.edges[ek(a, j)] in PASS:
                    dist[j] = dist[a] + 1
                    q.append(j)
        return dist

    def step_toward(self, a, t):
        if a == t:
            return -1
        INF = float('inf')
        dist = [INF] * N
        prev = [-1] * N
        done = [False] * N
        dist[a] = 0
        while True:
            u = -1
            for i in range(N):
                if not done[i] and dist[i] < INF and (u < 0 or dist[i] < dist[u]):
                    u = i
            if u < 0 or u == t:
                break
            done[u] = True
            for j in NB[u]:
                e = self.edges[ek(u, j)]
                if e in PASS:
                    w = 1
                elif e == 'door' or (self.R['derribar_js'] and e != 'wall'):
                    w = 4
                else:
                    w = INF  # kit: solo derriban puertas cerradas sin llave; vidriera y puerta con llave son pared para ellos
                if dist[u] + w < dist[j]:
                    dist[j] = dist[u] + w
                    prev[j] = u
        if dist[t] == INF:
            return -1
        s = t
        while prev[s] != a:
            s = prev[s]
        return s

    def sees(self, z):
        if z[0] == self.pos:
            return True
        if self.hidden or self.night():
            return False
        return self.pos in NB[z[0]] and self.edges[ek(z[0], self.pos)] not in SIGHT

    # --- heridas y fin ---
    def finish(self, win, razon):
        self.over = True
        self.win = win
        self.razon = razon
        raise Fin()

    def wound(self):
        zr, tr = self.d(6), self.d(6)
        zone = ZONES[zr]
        typ = 'Rasguño' if tr <= 2 else 'Laceración' if tr <= 4 else 'Fractura' if tr == 5 else 'Mordedura'
        self.wounds.append([zone, typ, False])
        self.heridas += 1
        self.sangre -= 1
        if zone == 'Torso' and typ != 'Rasguño':
            self.sangre -= 1
        if zone == 'Cabeza':
            self.head += 1
            if typ != 'Rasguño':
                self.stunned = True
        if typ == 'Mordedura':
            self.bites += 1
        if self.head >= 2:
            self.finish(False, 'cabeza')
        if self.sangre <= 0:
            self.finish(False, 'desangrado')
        self.fix_bag()

    # --- edificios y botín ---
    def reveal_farm(self):
        if self.farm:
            return
        self.farm = True
        r = self.d(6)
        put = {1: [], 2: [10], 3: [11], 4: [10, 11], 5: [11], 6: [10, 10, 11]}[r]
        self.farm_mod = -1 if r == 1 else 1 if r >= 5 else 0
        for c in put:
            self.zombies.append([c, 0, False])

    def reveal_casa(self):
        if self.casa:
            return
        self.casa = True
        if self.d(6) <= 2:
            self.zombies.append([7, 0, False])

    def loot(self, cell):
        r = self.d(6)
        if TYPE[cell] == 'casa':
            return (None if r <= 3 else 'venda' if r <= 5 else 'comida'), False
        t = r + self.farm_mod + self.R['botin_mod']
        if cell == 10:
            return (None if t <= 1 else 'kit' if t >= self.R['kit_salon'] else 'venda' if t <= 3 else 'analgesico'), False
        return (None if t <= 1 else 'kit' if t >= self.R['kit_deposito'] else 'venda' if t == 2 else 'comida'), t <= 1

    # mochila: el jugador automático guarda siempre 1 espacio para el kit
    VALOR = {'kit': 100, 'pistola': 8, 'cuchillo': 7, 'bate': 6, 'venda': 4, 'analgesico': 5, 'comida': 1}
    def add_item(self, k):
        reserva = 0 if (k == 'kit' or self.has('kit')) else 1
        if self.load() + SIZE[k] + reserva <= self.cap():
            self.inv.append(k)
            self.found.append(k)
            if k == 'kit':
                self.turno_kit = self.turno
            return
        if k == 'kit':
            # suelta lo de menor valor hasta que entre
            while self.load() + 1 > self.cap():
                self.drop_worst()
            self.inv.append(k)
            self.found.append(k)
            self.turno_kit = self.turno
        # otros objetos sin espacio se dejan

    def drop_worst(self):
        v = min(self.inv, key=lambda k: self.VALOR[k] if k != 'venda' or self.inv.count('venda') > 1 else 3)
        self.inv.remove(v)
        if v in self.found:
            self.found.remove(v)

    def fix_bag(self):
        while self.load() > self.cap():
            self.drop_worst()

    # --- acciones ---
    def use(self, nombre, pa):
        self.pa -= pa
        self.uso[nombre] += 1

    def move(self, cell, how):
        if how == 'sigilo':
            self.use('Sigilo', self.R['sigilo_pa'])
        elif how == 'caminar':
            self.use('Caminar', 1)
            self.noise(cell, 1)
        else:
            self.use('Correr', 1)
            self.ran = True
            self.noise(cell, self.R['correr_ruido'], self.R['correr_fichas'])
        self.pos = cell
        if cell == 12 and self.has('kit'):
            self.finish(True, 'victoria')

    def open_edge(self, cell, kind):
        here = self.pos
        k = ek(here, cell)
        if kind == 'abrir':
            self.use('Abrir', 1); self.edges[k] = 'opened'; self.noise(here, 1)
        elif kind == 'forzar':
            h = self.R['hab_forzar']
            self.use('Forzar', 1 if h else 2); self.edges[k] = 'opened'; self.noise(here, 1 if h else 2)
        else:
            self.use('Romper', 1); self.edges[k] = 'broken'; self.noise(here, 3)
        if k == (7, 13) and kind == 'abrir':
            self.reveal_casa()
        if BLD(cell) == 'farm' or BLD(here) == 'farm':
            self.reveal_farm()

    def search(self):
        here = self.pos
        self.use('Registrar', 2)
        self.searches[here] += 1
        self.noise(here, 1)
        item, drop = self.loot(here)
        if drop:
            self.tokens[here] += 1
        if item:
            self.add_item(item)

    def bandage(self):
        self.use('Vendar', 1 if self.R['hab_vendar1'] else 2)
        for w in self.wounds:
            if w[1] == 'Laceración' and not w[2]:
                w[2] = True
                break
        self.inv.remove('venda')
        self.noise(self.pos, 1)

    def painkiller(self):
        self.use('Analgésico', 1)
        self.inv.remove('analgesico')
        self.sangre = min(self.R['sangre'], self.sangre + 1)

    def attack(self, w, cell):
        die, mod, ru, melee = self.W[w]
        zs = sorted(self.zhere(cell), key=lambda z: -z[1])
        z = zs[0]
        self.use('Atacar ' + w, 1)
        if w == 'pistola':
            self.ammo -= 1
        adv = not z[2]
        if w == 'pistola':
            self.disparos += 1
            if self.disparos == 1 and self.R['hab_ventaja_fuego']:
                adv = True
        dis = self.effect('BrazoD') or (w == 'pistola' and self.night())
        r1, r2 = self.d(20), self.d(20)
        nat = r1
        if adv and not dis:
            nat = max(r1, r2)
        elif dis and not adv:
            nat = min(r1, r2)
        tot = nat + (self.R['mod_fue'] if melee else self.R['mod_des'])
        self.noise(self.pos, ru)
        if nat == 1:
            self.tokens[self.pos] += 1
            if w == 'pistola':
                self.jam = True
            z[2] = True
            return
        if nat == 20 or tot >= self.R['zombi_def']:
            dmg = die + mod if nat == 20 else self.d(die) + mod
            z[1] += dmg
            if z[1] >= self.R['zombi_vida']:
                self.zombies.remove(z)
                self.kills[w] += 1
            else:
                z[2] = True
        else:
            z[2] = True

    # --- fase de zombies, horda, disipación, reloj ---
    def end_turn(self):
        for z in list(self.zombies):
            if z not in self.zombies:
                continue
            if z[0] == self.pos:
                z[2] = True
                self.ataques_recibidos += 1
                if self.d(20) + self.R['zombi_ataque'] >= self.R['defensa']:
                    self.wound()
                continue
            tgt = -1
            best = None
            for (cell, lv) in self.events:
                h = self.hear(cell, lv, z[0])
                if h and (best is None or h[0] > best[1][0] or (h[0] == best[1][0] and h[1] < best[1][1])):
                    best = (cell, h)
            if best:
                tgt = best[0]
            elif self.sees(z):
                tgt = self.pos
            if tgt < 0 or tgt == z[0]:
                z[2] = tgt >= 0
                continue
            z[2] = True
            s = self.step_toward(z[0], tgt)
            if s < 0:
                continue
            k = ek(z[0], s)
            if self.edges[k] in PASS:
                z[0] = s
            elif self.d(6) == 6:
                self.edges[k] = 'broken'
                # corrección del error del JS: al caer la abertura se revela el edificio
                if k == (7, 13):
                    self.reveal_casa()
                if BLD(k[0]) == 'farm' or BLD(k[1]) == 'farm':
                    self.reveal_farm()
        # horda
        for g in GROUPS:
            tot = sum(self.tokens[i] for i in g)
            if tot >= self.R['horda']:
                b = HORDE_CELL[g[0]]
                for _ in range(self.R['horda_zombies']):
                    self.zombies.append([b, 0, False])
                for i in g:
                    self.tokens[i] = 0
                self.hordas += 1
        # disipación
        dis = self.R['disipacion']
        self.tokens = [max(0, t - dis) for t in self.tokens]
        # sangrado
        lac = sum(1 for w in self.wounds if w[1] == 'Laceración' and not w[2])
        if lac:
            self.sangre -= lac
            if self.sangre <= 0:
                self.finish(False, 'desangrado')
        if self.turno >= self.R['turnos']:
            self.finish(False, 'tiempo')
        self.turno += 1
        sp = self.d(6)
        lim = self.R['aparicion_noche'] if self.night() else self.R['aparicion_dia']
        if sp <= lim:
            r = self.d(6)
            if r <= 2:
                c = self.d(6) - 1
            elif r <= 4:
                c = 5 if self.d(2) == 1 else 17
            else:
                c = 12 + self.d(5)
            self.zombies.append([c, 0, False])
        self.pa = 2 if self.stunned else 3
        self.stunned = False
        self.hidden = False
        self.ran = False
        self.events = []


# ---------------------------------------------------------------------------
# Jugadores automáticos
# ---------------------------------------------------------------------------
ENTRADAS = {
    'puerta': (9, 10, 'abrir'),
    'vidriera': (4, 10, 'romper'),
    'trasera': (17, 11, 'forzar'),
}


class Jugador:
    def __init__(self, g, estilo, entrada):
        self.g = g
        self.estilo = estilo
        self.entrada = entrada

    # Dijkstra sobre aberturas pasables, con castigo por zombies en el camino
    def path(self, target, castigo=2):
        g = self.g
        INF = 10 ** 9
        dist = [INF] * N
        prev = [-1] * N
        dist[g.pos] = 0
        done = [False] * N
        zc = Counter(z[0] for z in g.zombies)
        while True:
            u = -1
            for i in range(N):
                if not done[i] and dist[i] < INF and (u < 0 or dist[i] < dist[u]):
                    u = i
            if u < 0 or u == target:
                break
            done[u] = True
            for j in NB[u]:
                if g.edges[ek(u, j)] not in PASS:
                    continue
                w = 1 + (castigo * zc[j] if j != target else 0)
                if dist[u] + w < dist[j]:
                    dist[j] = dist[u] + w
                    prev[j] = u
        if dist[target] >= INF:
            return None
        p = [target]
        while p[-1] != g.pos:
            p.append(prev[p[-1]])
        p.reverse()
        return p[1:]

    def heard_by_calm(self, cell, lv):
        """¿Algún zombie que todavía no viene hacia mí oiría este ruido?"""
        g = self.g
        if lv <= 0:
            return False
        for z in g.zombies:
            if z[2] and manh(z[0], cell) <= 1:
                continue  # ya está encima: el ruido no cambia nada
            if g.hear(cell, lv, z[0]):
                return True
        return False

    def pick_move(self, p):
        """Devuelve (celda, modo) para avanzar por el camino p."""
        g = self.g
        here_z = bool(g.zhere(g.pos))
        sig_ok = (not here_z) and g.pa >= g.R['sigilo_pa']
        run_ok = (not g.ran) and (not g.effect('Piernas')) and len(p) >= 2
        if self.estilo == 'sigiloso':
            if sig_ok:
                return p[0], 'sigilo'
            return p[0], 'caminar'
        if self.estilo == 'ruidoso':
            if run_ok:
                return p[1], 'correr'
            return p[0], 'caminar'
        # mixto: lo más rápido que nadie oiga
        if run_ok and not self.heard_by_calm(p[1], g.R['correr_ruido']):
            return p[1], 'correr'
        if not self.heard_by_calm(p[0], 1):
            return p[0], 'caminar'
        if sig_ok:
            return p[0], 'sigilo'
        return p[0], 'caminar'

    def weapon_for_melee(self, nz):
        g = self.g
        pistol_ok = g.has('pistola') and g.ammo > 0 and not g.jam
        if self.estilo == 'ruidoso':
            order = ['pistola', 'bate', 'cuchillo']
        elif self.estilo == 'sigiloso':
            order = ['cuchillo', 'bate', 'pistola']
        else:
            if pistol_ok and (nz >= 2 or g.sangre <= 3):
                order = ['pistola', 'bate', 'cuchillo']
            else:
                order = ['bate', 'cuchillo', 'pistola']
        for w in order:
            if not g.has(w):
                continue
            if w == 'pistola' and not pistol_ok:
                continue
            return w
        return None

    def objetivo(self):
        g = self.g
        if g.has('kit'):
            return ('volver', 12)
        bx, inside, kind = ENTRADAS[self.entrada]
        entered = g.pos in (10, 11)
        if not entered:
            # ¿hay ya un camino abierto a la farmacia?
            if self.path(11, 0) is None and self.path(10, 0) is None:
                if g.pos == bx:
                    return ('abrir', inside, kind)
                return ('ir', bx)
        for c in (11, 10):
            if g.searches[c] < 3:
                if g.pos == c:
                    return ('registrar', c)
                return ('ir', c)
        return ('rendirse', 12)

    def turno(self):
        g = self.g
        while g.pa > 0 and not g.over:
            if not self.accion():
                break
        if not g.over:
            g.end_turn()

    def accion(self):
        g = self.g
        here = g.zhere(g.pos)
        # 1. destrabar si la pistola es el arma principal y hay peligro cerca
        if g.jam and g.has('pistola') and g.ammo > 0 and self.estilo != 'sigiloso':
            if here or any(manh(z[0], g.pos) <= 2 for z in g.zombies):
                if not (here and self.weapon_for_melee(len(here))):
                    g.use('Destrabar', 1); g.jam = False
                    return True
        # 2. zombie en mi zona: pelear
        if here:
            w = self.weapon_for_melee(len(here))
            if w:
                g.attack(w, g.pos)
                return True
            # sin armas utilizables: alejarse caminando
            p = self.path(self.objetivo()[1], 0) or []
            if p:
                g.move(p[0], 'caminar')
                return True
            return False
        # 3. vendar laceraciones (2 PA)
        if g.pa >= (1 if g.R['hab_vendar1'] else 2) and g.has('venda') and any(w[1] == 'Laceración' and not w[2] for w in g.wounds):
            g.bandage()
            return True
        # 4. analgésico
        if g.has('analgesico') and g.sangre <= 3:
            g.painkiller()
            return True
        # 5. el ruidoso dispara a zombies alerta a 1-2 zonas
        if self.estilo == 'ruidoso' and g.has('pistola') and g.ammo > 0 and not g.jam:
            dist = g.reach(g.pos, 2)
            tg = [i for i in range(N) if dist[i] > 0 and any(z[2] for z in g.zhere(i))]
            if tg:
                tg.sort(key=lambda i: dist[i])
                g.attack('pistola', tg[0])
                return True
        # 6. objetivo
        ob = self.objetivo()
        if ob[0] == 'abrir':
            cost = 2 if ob[2] == 'forzar' and not g.R['hab_forzar'] else 1
            if g.pa < cost:
                return False
            g.open_edge(ob[1], ob[2])
            return True
        if ob[0] == 'registrar':
            if g.pa < 2:
                return False
            g.search()
            return True
        if ob[0] == 'rendirse':
            # sin kit posible: la partida se pierde igual; se cuenta como "farmacia vacía"
            g.finish(False, 'sin kit')
        p = self.path(ob[1])
        if not p:
            return False
        cell, how = self.pick_move(p)
        if how == 'sigilo' and g.pa < g.R['sigilo_pa']:
            how = 'caminar'
        if how == 'caminar' and self.estilo == 'sigiloso' and g.pa == 1 and ob[0] != 'volver':
            # con 1 PA el sigiloso camina solo si nadie lo oye; si no, se queda quieto
            if self.heard_by_calm(cell, 1):
                return False
        g.move(cell, how)
        return True


def jugar(seed, estilo, armas, entrada, R):
    rng = random.Random(seed)
    g = Juego(rng, armas, R)
    j = Jugador(g, estilo, entrada)
    try:
        while True:
            j.turno()
    except Fin:
        pass
    puntos = sum(PUNTOS.get(k, 0) for k in g.found) if g.win else 0
    return {
        'win': g.win, 'razon': g.razon, 'turno': g.turno, 'hordas': g.hordas,
        'mordido': g.bites > 0, 'sangre': max(0, g.sangre), 'heridas': g.heridas,
        'ataques': g.ataques_recibidos, 'uso': g.uso, 'kills': g.kills,
        'turno_kit': g.turno_kit, 'puntos': puntos, 'balas': g.R['balas'] - g.ammo,
    }


ARMAS = {'CB': ('cuchillo', 'bate'), 'CP': ('cuchillo', 'pistola'), 'BP': ('bate', 'pistola')}


def correr_config(args):
    estilo, armas, entrada, n, seed0, R = args
    res = Counter()
    turnos_win = 0
    hordas = 0
    usos = Counter()
    kills = Counter()
    heridas = 0
    tkit = []
    for i in range(n):
        r = jugar(seed0 + i, estilo, ARMAS[armas], entrada, R)
        if r['win']:
            res['win'] += 1
            turnos_win += r['turno']
            if r['mordido']:
                res['win_mordido'] += 1
        else:
            res[r['razon']] += 1
        hordas += r['hordas']
        if r['hordas']:
            res['con_horda'] += 1
        heridas += r['heridas']
        usos.update(r['uso'])
        kills.update(r['kills'])
        if r['turno_kit']:
            tkit.append(r['turno_kit'])
    return {
        'estilo': estilo, 'armas': armas, 'entrada': entrada, 'n': n,
        'win': res['win'] / n, 'win_limpia': (res['win'] - res['win_mordido']) / n,
        'turnos_win': turnos_win / max(1, res['win']),
        'hordas': hordas / n, 'p_horda': res['con_horda'] / n,
        'desangrado': res['desangrado'] / n, 'cabeza': res['cabeza'] / n,
        'tiempo': res['tiempo'] / n, 'sin_kit': res['sin kit'] / n,
        'heridas': heridas / n, 'usos': {k: v / n for k, v in usos.items()},
        'kills': {k: v / n for k, v in kills.items()},
        'turno_kit': sum(tkit) / max(1, len(tkit)), 'p_kit': len(tkit) / n,
    }


def fmt_row(r):
    return ("| {estilo} | {armas} | {entrada} | {w:.1f} | {wl:.1f} | {t:.1f} | {h:.2f} | {ph:.0f} | {de:.1f} | {ca:.1f} | {ti:.1f} | {sk:.1f} |".format(
        estilo=r['estilo'], armas=r['armas'], entrada=r['entrada'], w=100 * r['win'], wl=100 * r['win_limpia'],
        t=r['turnos_win'], h=r['hordas'], ph=100 * r['p_horda'], de=100 * r['desangrado'], ca=100 * r['cabeza'],
        ti=100 * r['tiempo'], sk=100 * r['sin_kit']))


HEADER = ("| Estilo | Armas | Entrada | % victoria | % victoria sin mordida | Turnos (victorias) | Hordas/partida | % con horda | % desangrado | % 2.ª herida cabeza | % se acaba el tiempo | % farmacia sin kit |\n"
          "|---|---|---|---|---|---|---|---|---|---|---|---|")


def matriz(n, R, estilos, armas_l, entradas, procs, seed=12345):
    jobs = []
    k = 0
    for e in estilos:
        for a in armas_l:
            for en in entradas:
                jobs.append((e, a, en, n, seed + 1000003 * k, R))
                k += 1
    with Pool(procs) as p:
        return p.map(correr_config, jobs)


VARIANTES = [
    ('Reglas actuales', {}),
    ('Correr deja 2 fichas', {'correr_fichas': 2}),
    ('Correr ruido Alto (3, 2 fichas)', {'correr_ruido': 3}),
    ('Kit en depósito con 4+ y salón 5+', {'kit_deposito': 4, 'kit_salon': 5}),
    ('Pistola: ruido Alto (3) en vez de Máximo', {'pistola_ruido': 3}),
    ('Pistola: 4 balas en vez de 6', {'balas': 4}),
    ('Horda: umbral 6 fichas', {'horda': 6}),
    ('Horda: umbral 4 fichas', {'horda': 4}),
    ('Ataque zombie d20+1 (55 %)', {'zombi_ataque': 1}),
    ('Bate ruido Bajo (como la carta)', {'bate_ruido': 1}),
    ('Correr ruido Bajo', {'correr_ruido': 1}),
    ('Botín farmacia +1', {'botin_mod': 1}),
    ('Expedición de 14 turnos', {'turnos': 14}),
    ('Sangre 7', {'sangre': 7}),
    ('Paquete propuesto', {'zombi_ataque': 1, 'botin_mod': 1, 'balas': 4}),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('-n', type=int, default=10000, help='partidas por configuración')
    ap.add_argument('--estilo', choices=['sigiloso', 'ruidoso', 'mixto'], action='append')
    ap.add_argument('--armas', choices=list(ARMAS), action='append')
    ap.add_argument('--entrada', choices=list(ENTRADAS), action='append')
    ap.add_argument('--regla', action='append', default=[], help='clave=valor, p. ej. horda=6')
    ap.add_argument('--variantes', action='store_true', help='corre la batería de ajustes')
    ap.add_argument('--supervivientes', action='store_true', help='compara los 7 supervivientes (estilo mixto)')
    ap.add_argument('--procs', type=int, default=None)
    ap.add_argument('--seed', type=int, default=12345)
    a = ap.parse_args()
    R = dict(REGLAS_BASE)
    for kv in a.regla:
        k, v = kv.split('=')
        if k not in R:
            sys.exit('regla desconocida: ' + k)
        R[k] = int(v)
    estilos = a.estilo or ['sigiloso', 'ruidoso', 'mixto']
    armas_l = a.armas or list(ARMAS)
    entradas = a.entrada or list(ENTRADAS)
    if a.supervivientes:
        armas_s = a.armas or ['CB', 'CP']
        ents = a.entrada or ['puerta', 'trasera']
        cols = [(w, e) for w in armas_s for e in ents]
        print('| Superviviente | F/D/C/P | ' + ' | '.join(f'mixto {w} {e}' for w, e in cols) + ' | Media |')
        print('|---|---|' + '---|' * (len(cols) + 1))
        for nombre in SUPERVIVIENTES:
            RV = reglas_superviviente(nombre, R)
            rs = matriz(a.n, RV, ['mixto'], armas_s, ents, a.procs, a.seed)
            ws = [100 * r['win'] for r in rs]
            at = '/'.join(map(str, SUPERVIVIENTES[nombre][0]))
            print(f'| {nombre} | {at} | ' + ' | '.join(f'{w:.1f}' for w in ws) + f' | {sum(ws) / len(ws):.1f} |', flush=True)
        return
    if a.variantes:
        print('| Variante | ' + ' | '.join(f'{e[:3]} {w}' for e in estilos for w in armas_l) + ' | mejor − peor |')
        print('|---|' + '---|' * (len(estilos) * len(armas_l) + 1))
        for nombre, cambios in VARIANTES:
            RV = dict(R); RV.update(cambios)
            rs = matriz(a.n, RV, estilos, armas_l, ['puerta'], a.procs, a.seed)
            ws = [100 * r['win'] for r in rs]
            print(f'| {nombre} | ' + ' | '.join(f'{w:.1f}' for w in ws) + f' | {max(ws) - min(ws):.1f} |', flush=True)
        return
    rs = matriz(a.n, R, estilos, armas_l, entradas, a.procs, a.seed)
    print(f'Partidas por configuración: {a.n}. Reglas cambiadas: {a.regla or "ninguna"}')
    print(HEADER)
    for r in rs:
        print(fmt_row(r))
    print()
    print('| Estilo | Armas | Entrada | Heridas/partida | Turno del kit | % consigue kit | Acciones por partida (top) | Zombies muertos por arma |')
    print('|---|---|---|---|---|---|---|---|')
    for r in rs:
        top = ', '.join(f'{k} {v:.1f}' for k, v in sorted(r['usos'].items(), key=lambda x: -x[1])[:6])
        kl = ', '.join(f'{k} {v:.2f}' for k, v in sorted(r['kills'].items()))
        print(f"| {r['estilo']} | {r['armas']} | {r['entrada']} | {r['heridas']:.2f} | {r['turno_kit']:.1f} | {100 * r['p_kit']:.0f} | {top} | {kl} |")


if __name__ == '__main__':
    main()
