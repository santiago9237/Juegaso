#!/usr/bin/env python3
"""Economía de 30 días de Día 30: lo que entra por registro y por día contra lo que se consume.

Lee las tablas de edificios (zombies por fase y botín d20) directamente de
fuentes/base_y_losetas.html y el mazo de cartas de fuentes/cartas_de_objetos.html.
Uso: python3 herramientas/economia.py   (imprime tablas en Markdown). Solo librería estándar.

Supuestos que las fuentes no fijan (se pueden cambiar abajo):
  - REGISTROS_POR_EXPEDICION: registros que logra cada superviviente que sale (3 / 5 / 8).
  - Agua: 1 por superviviente y día (el consumo está "por definir").
  - Heridas: las de la simulación de la prueba 1 (estilo mixto, ~1,1 golpes por expedición).
"""
import ast
import os
import random
import re

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fuentes')
REGISTROS_POR_EXPEDICION = (3, 5, 8)
SUPERVIVIENTES_EN_BASE = 3   # se roban 3 al empezar, juegue 1, 2 o 3 personas
HERIDAS_POR_EXPEDICION = 1.1  # simular_prueba1.py, estilo mixto (12 turnos)


def leer_tablas():
    s = open(os.path.join(RAIZ, 'base_y_losetas.html'), encoding='utf-8').read()
    blk = s[s.index('const TABLAS = {') + len('const TABLAS = '):s.index('const ERRANTES')]
    blk = blk.strip().rstrip(';')
    blk = re.sub(r'(?m)^(\s*)(\w+): \{', r'\1"\2": {', blk)
    blk = re.sub(r'\b(z|b): \[', r'"\1": [', blk)
    blk = re.sub(r'\{ ((?:\w+: \d+(?:, )?)+) \}', lambda m: '{' + re.sub(r'(\w+): ', r'"\1": ', m.group(1)) + '}', blk)
    blk = blk.replace('null', 'None')
    tablas = ast.literal_eval(blk)
    err = s[s.index('const ERRANTES = ') + len('const ERRANTES = '):]
    err = ast.literal_eval(err[:err.index(';')])
    locs = []
    for m in re.finditer(r'\{ id: "(\w+)", n: "([^"]+)", t: "[^"]+", h: (\d), peligro: \d, pl: "\w+", pool: (\[[^\]]+\]), saqueados: (\d)', s):
        locs.append((m.group(1), m.group(2), int(m.group(3)), ast.literal_eval(m.group(4)), int(m.group(5))))
    return tablas, err, locs


def p_d20(mod):
    if mod == 'v':
        return {k: (2 * k - 1) / 400 for k in range(1, 21)}
    if mod == 'd':
        return {k: (41 - 2 * k) / 400 for k in range(1, 21)}
    return {k: 1 / 20 for k in range(1, 21)}


def clasificar(fila):
    """Convierte una fila de botín en recursos contables."""
    lo, hi, txt = fila[0], fila[1], fila[2]
    kind = fila[4] if len(fila) > 4 else ''
    mats = fila[5] if len(fila) > 5 else {}
    r = {}
    t = txt.lower()
    if kind == 'aah':
        if 'aparece' in t or 'sale' in t or 'se levanta' in t:
            r['zombie_en_tu_zona'] = 1
        else:
            r['ruido'] = 1
        return r
    if kind == 'rescate':
        r['rescate'] = 1
        return r
    if kind == 'senal':
        m = re.search(r'etapa (\d)', t)
        r['senal_%s' % m.group(1)] = 1
    m = re.findall(r'comida ×(\d)', t)
    if m:
        r['comida'] = sum(map(int, m))
    m = re.findall(r'agua ×(\d)', t)
    if m:
        r['agua'] = sum(map(int, m))
    elif t.startswith('agua'):
        r['agua'] = 1
    med = 0
    for palabra in ('vendas', 'desinfectante', 'analgésicos', 'antibióticos', 'botiquín', 'sutura'):
        if palabra in t:
            mm = re.search(palabra + r' ×(\d)', t)
            med += int(mm.group(1)) if mm else 1
    if 'botiquín completo' in t:
        med += 1  # vale por dos medicinas (vendas + desinfectante + férula)
    if med:
        r['medicina'] = med
    m = re.search(r'munición ×(\d)', t)
    if m:
        r['municion'] = int(m.group(1))
    if re.search(r'· d\d|· 2d8', t) and kind != 'senal':
        r['arma'] = 1
    for k, v in (mats or {}).items():
        r[k] = r.get(k, 0) + v
    if mats:
        r['materiales'] = sum(mats.values())
    return r


def por_registro(tabla_b, mod):
    pd = p_d20(mod)
    out = {}
    for fila in tabla_b:
        p = sum(pd[k] for k in range(fila[0], fila[1] + 1))
        for k, v in clasificar(fila).items():
            out[k] = out.get(k, 0) + p * v
    return out


def zcount(s):
    if not s or s == '—':
        return {}
    o = {}
    for part in s.split():
        o[part[-1]] = o.get(part[-1], 0) + int(part[:-1])
    return o


def edificio(tablas, tipo, fase):
    """Promedio sobre las 6 fichas: registros, botín total y zombies dentro."""
    t = tablas[tipo]
    regs = 0
    botin = {}
    zs = {}
    for fila in t['z']:
        n = fila[3]
        regs += n / 6
        for k, v in por_registro(t['b'], fila[4]).items():
            botin[k] = botin.get(k, 0) + v * n / 6
        for k, v in zcount(fila[fase]).items():
            zs[k] = zs.get(k, 0) + v / 6
    return regs, botin, zs


CLAVES = ['comida', 'agua', 'medicina', 'materiales', 'madera', 'clavos', 'chapa', 'alambre', 'cuerda', 'combustible', 'semillas', 'municion', 'arma', 'zombie_en_tu_zona', 'ruido', 'rescate', 'senal_1', 'senal_2', 'senal_3', 'senal_4']


def mazo():
    s = open(os.path.join(RAIZ, 'cartas_de_objetos.html'), encoding='utf-8').read()
    cartas = re.findall(r'\{ fam: "(\w+)",(?: sub: "([^"]+)",)? nombre: "([^"]+)", copias: (\d+)', s)
    return [(f, sub, n, int(c)) for f, sub, n, c in cartas]


def main():
    tablas, errantes, locs = leer_tablas()
    print('## Botín esperado por registro (d20, promedio de las 6 fichas con su ventaja/desventaja)\n')
    print('| Edificio | Registros medios | ' + ' | '.join(['Comida', 'Agua', 'Medicina', 'Materiales', 'Combust.', 'Munición', 'Zombie en tu zona', 'Ruido', 'Señal (cualquier etapa)']) + ' |')
    print('|---|---|' + '---|' * 9)
    resumen = {}
    for tipo in tablas:
        regs, botin, zs = edificio(tablas, tipo, 0)
        pr = {k: v / regs for k, v in botin.items()}
        resumen[tipo] = (regs, pr)
        sen = sum(pr.get('senal_%d' % i, 0) for i in range(1, 5))
        vals = [pr.get(k, 0) for k in ('comida', 'agua', 'medicina', 'materiales', 'combustible', 'municion', 'zombie_en_tu_zona', 'ruido')] + [sen]
        print(f'| {tipo} | {regs:.2f} | ' + ' | '.join(f'{v:.2f}' for v in vals) + ' |')

    print('\n## Zombies esperados dentro de cada edificio al revelarlo (C caminante, R corredor, B bruto, A ácido, H chillón)\n')
    print('| Edificio | Días 1–10 | Días 11–20 | Días 21–30 | Total 1–10 → 21–30 |')
    print('|---|---|---|---|---|')
    for tipo in tablas:
        cols = []
        tots = []
        for fase in range(3):
            _, _, zs = edificio(tablas, tipo, fase)
            cols.append(' '.join(f'{v:.1f}{k}' for k, v in sorted(zs.items())))
            tots.append(sum(zs.values()))
        print(f'| {tipo} | ' + ' | '.join(cols) + f' | {tots[0]:.1f} → {tots[2]:.1f} |')

    print('\n## Errantes por hora de reloj (d6), x2 de noche\n')
    nombres = ['Días 1–10', 'Días 11–20', 'Días 21–30']
    print('| Fase | Zombies por hora | Por expedición de 9 h de día |')
    print('|---|---|---|')
    pesos = {'1–2': 2, '3–4': 2, '5': 1, '6': 1}
    for f in range(3):
        e = sum(pesos[row[0]] / 6 * sum(zcount(row[f + 1]).values()) for row in errantes)
        print(f'| {nombres[f]} | {e:.2f} | {9 * e:.1f} |')

    print('\n## Botín por registro en cada barrio (registros repartidos según los edificios del barrio)\n')
    print('| Barrio | Horas de viaje | Horas para buscar | Registros disponibles | Comida | Agua | Medicina | Materiales | Señal 1 | Señal 2 | Señal 3 | Señal 4 |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    barrios = {}
    for lid, nombre, h, pool, saq in locs:
        tot_reg = 0
        acc = {}
        for i, tipo in enumerate(pool):
            if tipo not in tablas:
                continue
            regs, pr = resumen[tipo]
            peso = regs
            if i < saq:
                peso = 0  # saqueados de antemano (el mapa elige al azar; se aproxima)
            tot_reg += peso
            for k, v in pr.items():
                acc[k] = acc.get(k, 0) + v * peso
        # los saqueados se eligen al azar: corregimos repartiendo la pérdida en proporción
        if saq:
            tot_full = sum(resumen[t][0] for t in pool if t in tablas)
            acc = {}
            for tipo in pool:
                if tipo in tablas:
                    regs, pr = resumen[tipo]
                    for k, v in pr.items():
                        acc[k] = acc.get(k, 0) + v * regs
            frac = (len([t for t in pool if t in tablas]) - saq) / len([t for t in pool if t in tablas])
            tot_reg = tot_full * frac
            acc = {k: v * frac for k, v in acc.items()}
        pr = {k: v / tot_reg for k, v in acc.items()}
        barrios[lid] = (nombre, h, tot_reg, pr)
        print(f'| {nombre} | {h} | {11 - 2 * h} | {tot_reg:.1f} | ' + ' | '.join(f'{pr.get(k, 0):.3f}' for k in ('comida', 'agua', 'medicina', 'materiales', 'senal_1', 'senal_2', 'senal_3', 'senal_4')) + ' |')

    print('\n## Balance diario de comida y agua (tablas d20; consumo: 3 supervivientes en la base comen 1 cada uno)\n')
    print('| Jugadores (salen) | Registros por superviviente | Barrio | Registros usados | Comida que entra | Comida que sale | Saldo comida/día | Agua que entra | Saldo agua/día (1 por persona) | Medicina que entra | Medicina que sale (heridas) | Saldo medicina/día |')
    print('|---|---|---|---|---|---|---|---|---|---|---|---|')
    for nj in (1, 2, 3):
        for R in REGISTROS_POR_EXPEDICION:
            for lid in ('acacias', 'centro'):
                nombre, h, cap, pr = barrios[lid]
                used = min(nj * R, cap)
                food = used * pr.get('comida', 0)
                water = used * pr.get('agua', 0)
                med = used * pr.get('medicina', 0)
                gasto_med = nj * HERIDAS_POR_EXPEDICION * 2  # 2 medicinas quitan 1 carta de herida
                print(f'| {nj} | {R} | {nombre} | {used:.1f} | {food:.2f} | {SUPERVIVIENTES_EN_BASE} | {food - SUPERVIVIENTES_EN_BASE:+.2f} | {water:.2f} | {water - SUPERVIVIENTES_EN_BASE:+.2f} | {med:.2f} | {gasto_med:.2f} | {med - gasto_med:+.2f} |')

    # Mazo de cartas
    cartas = mazo()
    total = sum(c for *_, c in cartas)
    fam = {}
    for f, sub, n, c in cartas:
        k = sub or f
        fam[k] = fam.get(k, 0) + c
    print(f'\n## Mazo de cartas de objetos ({total} cartas): probabilidad por carta robada\n')
    print('| Familia / recurso | Copias | % por robo | Robos para 3 comidas (1 día, 3 personas) |')
    print('|---|---|---|---|')
    for k, c in sorted(fam.items(), key=lambda x: -x[1]):
        print(f'| {k} | {c} | {100 * c / total:.1f} | {3 * total / c:.1f} |')

    # robos esperados hasta tener las etapas 1, 2 y 4 con el mazo (sin reposición)
    rng = random.Random(1)
    nombres_senal = {'Radio portátil': 1, 'Generador': 2, 'Manual técnico': 4, 'GPS de mano': 4}
    deck = []
    for f, sub, n, c in cartas:
        deck += [n] * c
    pos_all = []
    for _ in range(20000):
        rng.shuffle(deck)
        got = set()
        for i, n in enumerate(deck):
            if n in nombres_senal:
                got.add(nombres_senal[n])
                if got == {1, 2, 4}:
                    pos_all.append(i + 1)
                    break
    pos_all.sort()
    print(f'\nMazo: robos hasta reunir radio + generador + manual o GPS: media {sum(pos_all) / len(pos_all):.1f}, mediana {pos_all[len(pos_all) // 2]} de {total}. La etapa 3 (baliza) no tiene carta en el mazo.')

    # señal con tablas d20: registros esperados por etapa en el mejor barrio
    print('\n## Señal con las tablas d20: registros esperados para encontrar cada etapa en el mejor barrio para ella\n')
    print('| Etapa | Mejor barrio | P por registro | Registros esperados | Días con 1 / 2 / 3 jugadores (5 registros c/u) |')
    print('|---|---|---|---|---|')
    tot_dias = {1: 0, 2: 0, 3: 0}
    for et in (1, 2, 3, 4):
        k = 'senal_%d' % et
        best = max(barrios.values(), key=lambda b: b[3].get(k, 0))
        p = best[3].get(k, 0)
        n = 1 / p if p else float('inf')
        dias = [n / (5 * nj) for nj in (1, 2, 3)]
        for i, nj in enumerate((1, 2, 3)):
            tot_dias[nj] += dias[i]
        print(f'| {et} | {best[0]} | {p:.3f} | {n:.0f} | ' + ' / '.join(f'{d:.1f}' for d in dias) + ' |')
    print(f'\nSuma de días buscando las 4 etapas una tras otra: 1 jugador {tot_dias[1]:.0f}, 2 jugadores {tot_dias[2]:.0f}, 3 jugadores {tot_dias[3]:.0f} (de 30, sin contar días de comida).')



def mazo_aparicion():
    """Zombies por expedición con el mazo de aparición (diseno/mazo_aparicion.md)."""
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from simular_prueba1 import _MAZO
    base = [(t, ns) for t, ns, c in _MAZO for _ in range(c)]
    rng = random.Random(3)
    print('\n## Mazo de aparición: zombies por expedición (12 turnos: 10 de día con 1 carta y 2 de noche con 2 = 14 cartas)\n')
    print('| Nivel (días) | Zombies por carta | Zombies por expedición | Caminantes | Corredores | Brutos | Ácidos | Chillones | Activaciones extra | % expediciones con carta Horda | Errantes d6 equivalentes (tramo) |')
    print('|---|---|---|---|---|---|---|---|---|---|---|')
    d6 = {1: 0.67 * 10 + 2 * 0.67 * 2, 2: 1.0 * 10 + 2 * 1.0 * 2, 3: 1.83 * 10 + 2 * 1.83 * 2}
    dias = {1: '1–7', 2: '8–14', 3: '15–20'}
    for nv in (1, 2, 3):
        reps = 40000
        tot = {}
        act = 0
        hordas = 0
        for _ in range(reps):
            mazo = base[:]
            rng.shuffle(mazo)
            desc = []
            vio_horda = False
            for _c in range(14):
                if not mazo:
                    mazo = desc
                    desc = []
                    rng.shuffle(mazo)
                t, ns = mazo.pop()
                desc.append((t, ns))
                if t == 'activacion':
                    act += 1
                elif t == 'horda':
                    vio_horda = True
                    tot['C'] = tot.get('C', 0) + [2, 3, 4][nv - 1]
                    tot['R'] = tot.get('R', 0) + [0, 1, 1][nv - 1]
                    mazo += desc
                    desc = []
                    rng.shuffle(mazo)
                else:
                    k = 'C' if t == 'atraidos' else t
                    tot[k] = tot.get(k, 0) + ns[nv - 1]
            hordas += vio_horda
        tz = sum(tot.values()) / reps
        print(f'| {nv} ({dias[nv]}) | {tz / 14:.2f} | {tz:.1f} | ' + ' | '.join(f"{tot.get(k, 0) / reps:.1f}" for k in 'CRBAH') + f' | {act / reps:.2f} | {100 * hordas / reps:.0f} | {d6[nv]:.1f} |')


def alimento():
    """Comida y agua fusionadas en Alimento: botín por registro y por día."""
    tablas, errantes, locs = leer_tablas()
    print('\n## Alimento (comida + agua en un solo recurso): entra por registro\n')
    print('| Edificio | Alimento por registro | Alimento por edificio entero |')
    print('|---|---|---|')
    for tipo in tablas:
        regs, botin, zs = edificio(tablas, tipo, 0)
        a = botin.get('comida', 0) + botin.get('agua', 0)
        print(f'| {tipo} | {a / regs:.2f} | {a:.2f} |')


if __name__ == '__main__':
    main()
    mazo_aparicion()
    alimento()
