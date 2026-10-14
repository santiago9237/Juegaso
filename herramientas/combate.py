#!/usr/bin/env python3
"""Probabilidades exactas de combate de Día 30 (reglas del kit de prueba 1).

Uso: python3 herramientas/combate.py   (imprime tablas en Markdown)
Solo librería estándar. Todo se calcula exacto (enumeración), sin azar.
"""
from fractions import Fraction as Fr
from functools import lru_cache

# ---------------------------------------------------------------- tiradas d20
def p_nat(mode):
    """Distribución del d20 natural: normal, ventaja o desventaja."""
    d = {}
    for k in range(1, 21):
        if mode == 'n':
            d[k] = Fr(1, 20)
        elif mode == 'v':
            d[k] = Fr(2 * k - 1, 400)
        else:
            d[k] = Fr(41 - 2 * k, 400)
    return d

def p_hit(bonus, defensa, mode='n'):
    """Acierta con 20 natural o d20+bonus >= defensa; el 1 natural siempre falla."""
    return sum(p for k, p in p_nat(mode).items() if k == 20 or (k > 1 and k + bonus >= defensa))

# ---------------------------------------------------------------- armas
# nombre: (dados, caras, suma Fuerza, ruido, es de fuego)
ARMAS = {
    'Cuchillo d4+F': (1, 4, True, 'Silencio', False),
    'Bate d6+F': (1, 6, True, 'Medio (kit) / Bajo (carta)', False),
    'Hacha d8+F': (1, 8, True, 'Medio', False),
    'Pistola d10': (1, 10, False, 'Máximo', True),
    'Escopeta d12': (1, 12, False, 'Máximo', True),
    'Motosierra 2d8+F': (2, 8, True, 'Máximo', False),
}

def dmg_dist(n, f, mod):
    dist = {0: Fr(1)}
    for _ in range(n):
        nd = {}
        for a, p in dist.items():
            for k in range(1, f + 1):
                nd[a + k] = nd.get(a + k, 0) + p * Fr(1, f)
        dist = nd
    return {a + mod: p for a, p in dist.items()}

def outcome(weapon, bonus, fue, defensa, mode):
    """Distribución del daño de un ataque (0 = falla). Crítico = daño máximo."""
    n, f, usaF, _, fuego = ARMAS[weapon]
    mod = fue if usaF else 0
    out = {}
    for k, p in p_nat(mode).items():
        if k == 1:
            out['pifia'] = out.get('pifia', 0) + p
        elif k == 20:
            out[n * f + mod] = out.get(n * f + mod, 0) + p
        elif k + bonus >= defensa:
            for dmg, q in dmg_dist(n, f, mod).items():
                out[dmg] = out.get(dmg, 0) + p * q
        else:
            out[0] = out.get(0, 0) + p
    return out

def exp_dmg(weapon, bonus, fue, defensa, mode='n'):
    return sum((0 if k == 'pifia' else k) * p for k, p in outcome(weapon, bonus, fue, defensa, mode).items())

def pa_to_kill(weapon, bonus, fue, defensa, vida, primero_tranquilo=True):
    """PA esperados para matar: 1.er ataque con ventaja si el zombie está tranquilo; luego normal.
    La pistola encasquillada por pifia cuesta 1 PA extra. Devuelve (PA esperados, P(muere en <=1,2,3 PA))."""
    fuego = ARMAS[weapon][4]
    o_v = outcome(weapon, bonus, fue, defensa, 'v')
    o_n = outcome(weapon, bonus, fue, defensa, 'n')

    @lru_cache(None)
    def E(d, alerta):
        if d >= vida:
            return Fr(0)
        o = o_n if alerta else o_v
        # E = 1 + sum p * E(next); la autotransición (falla estando alerta) se despeja
        self_p = Fr(0)
        acc = Fr(1)
        for k, p in o.items():
            if k == 'pifia':
                cost = 1 if fuego else 0
                if alerta:
                    self_p += p
                    acc += p * cost
                else:
                    acc += p * (cost + E(d, True))
            elif k == 0:
                if alerta:
                    self_p += p
                else:
                    acc += p * E(d, True)
            else:
                acc += p * E(d + k, True)
        return acc / (1 - self_p)

    # probabilidad de matar con a lo sumo m PA (sin contar destrabar como éxito)
    def P(m):
        @lru_cache(None)
        def G(d, alerta, pa):
            if d >= vida:
                return Fr(1)
            if pa <= 0:
                return Fr(0)
            o = o_n if alerta else o_v
            s = Fr(0)
            for k, p in o.items():
                if k == 'pifia':
                    s += p * G(d, True, pa - 1 - (1 if fuego else 0))
                elif k == 0:
                    s += p * G(d, True, pa - 1)
                else:
                    s += p * G(d + k, True, pa - 1)
            return s
        return G(0, not primero_tranquilo, m)

    return E(0, not primero_tranquilo), [P(m) for m in (1, 2, 3)]

# ---------------------------------------------------------------- heridas
def heridas_hasta_morir(sangre=6):
    """P(muerto) tras k golpes zombie (sin contar sangrado de laceraciones)."""
    # estado: (sangre, heridas en cabeza) -> prob
    st = {(sangre, 0): Fr(1)}
    dead = Fr(0)
    res = []
    for k in range(1, 9):
        ns = {}
        for (s, h), p in st.items():
            for z in range(1, 7):
                for t in range(1, 7):
                    q = p * Fr(1, 36)
                    rasg = t <= 2
                    s2 = s - 1 - (1 if z in (2, 3) and not rasg else 0)
                    h2 = h + (1 if z == 1 else 0)
                    if s2 <= 0 or h2 >= 2:
                        dead += q
                    else:
                        ns[(s2, h2)] = ns.get((s2, h2), 0) + q
        st = ns
        res.append(dead)
    return res

def pct(x):
    return f'{100 * float(x):.1f}'

def main():
    print('## Tirada de ataque: % de acertar según el número natural mínimo\n')
    print('| Necesitas en el d20 | Normal | Ventaja | Desventaja |')
    print('|---|---|---|---|')
    for need in range(2, 21):
        b, D = 0, need
        print(f'| {need}+ | {pct(p_hit(b, D))} | {pct(p_hit(b, D, "v"))} | {pct(p_hit(b, D, "d"))} |')

    zombies = [('Caminante', 8), ('Chillón', 8), ('Infectado ácido', 9), ('Bruto', 10), ('Corredor', 12), ('Bruto con chaleco', 12)]
    print('\n## % de acertar del superviviente neutro (+1) por defensa del zombie\n')
    print('| Zombie | Defensa | Normal | Ventaja (tranquilo) | Desventaja (brazo der. / disparo de noche) |')
    print('|---|---|---|---|---|')
    for zn, D in zombies:
        print(f'| {zn} | {D} | {pct(p_hit(1, D))} | {pct(p_hit(1, D, "v"))} | {pct(p_hit(1, D, "d"))} |')

    print('\n## Daño esperado por ataque (superviviente neutro, Fuerza +1, Destreza +1)\n')
    print('| Arma | Ruido | ' + ' | '.join(f'{zn} (D{D})' for zn, D in zombies) + ' |')
    print('|---|---|' + '---|' * len(zombies))
    for w, (n, f, usaF, ru, fuego) in ARMAS.items():
        print(f'| {w} | {ru} | ' + ' | '.join(f'{float(exp_dmg(w, 1, 1, D)):.2f}' for zn, D in zombies) + ' |')

    print('\n## Caminante (Defensa 8, vitalidad 5): PA para matarlo\n')
    print('| Arma | % acierto (normal / ventaja) | Daño medio si acierta | % mata de un golpe (1.er ataque, tranquilo) | PA esperados (tranquilo) | PA esperados (alerta) | P(muere en 1 / 2 / 3 PA), tranquilo | P(muere en 3 PA), alerta |')
    print('|---|---|---|---|---|---|---|---|')
    for w, (n, f, usaF, ru, fuego) in ARMAS.items():
        e1, ps = pa_to_kill(w, 1, 1, 8, 5, True)
        e2, ps2 = pa_to_kill(w, 1, 1, 8, 5, False)
        mod = 1 if usaF else 0
        avg = n * (f + 1) / 2 + mod
        print(f'| {w} | {pct(p_hit(1, 8))} / {pct(p_hit(1, 8, "v"))} | {avg:.1f} | {pct(ps[0])} | {float(e1):.2f} | {float(e2):.2f} | {" / ".join(pct(x) for x in ps)} | {pct(ps2[2])} |')

    print('\n## Efecto de la Fuerza (bate d6+F y cuchillo d4+F contra caminante, zombie alerta)\n')
    print('| Fuerza (mod) | % acierto | PA esperados cuchillo | PA esperados bate | P(mata en 3 PA) bate |')
    print('|---|---|---|---|---|')
    for F in range(1, 6):
        m = F - 2
        ec, _ = pa_to_kill('Cuchillo d4+F', m, m, 8, 5, False)
        eb, pb = pa_to_kill('Bate d6+F', m, m, 8, 5, False)
        print(f'| {F} ({m:+d}) | {pct(p_hit(m, 8))} | {float(ec):.2f} | {float(eb):.2f} | {pct(pb[2])} |')

    print('\n## Ataque zombie: d20 + 2 contra la Defensa del superviviente\n')
    print('| Defensa | Destreza | % que te golpee | Sangre esperada por golpe | Sangre esperada por zombie y turno (inmediata) | + laceraciones abiertas por zombie y turno |')
    print('|---|---|---|---|---|---|')
    sangre_golpe = 1 + Fr(2, 6) * Fr(4, 6)
    for D in range(9, 15):
        p = p_hit(2, D)
        print(f'| {D} | {"(" + str(D - 8) + ")" if D <= 13 else "chaleco"} | {pct(p)} | {float(sangre_golpe):.3f} | {float(p * sangre_golpe):.2f} | {float(p * Fr(1, 3)):.2f} |')

    print('\n## Golpes recibidos hasta morir (sangre 6; muerte por sangre 0 o 2.ª herida en la cabeza)\n')
    res = heridas_hasta_morir()
    print('| Golpes | ' + ' | '.join(str(k) for k in range(1, 9)) + ' |')
    print('|---|' + '---|' * 8)
    print('| P(muerto) | ' + ' | '.join(pct(x) for x in res) + ' |')
    print('\nPor golpe: P(mordedura) = 16.7 %, P(laceración) = 33.3 %, P(cabeza) = 16.7 %, P(fractura) = 16.7 %.')

if __name__ == '__main__':
    main()
