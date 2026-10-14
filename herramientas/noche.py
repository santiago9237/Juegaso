#!/usr/bin/env python3
"""Ataque nocturno a la base (reglamento v0.3, sección 17.6): probabilidad de irrupción por tramo.

Uso: python3 herramientas/noche.py   (tablas en Markdown). Solo librería estándar.
Cálculo exacto por enumeración de dados; el combate dentro de la base se estima por Monte Carlo.

Regla modelada:
  amenaza = d6 + tramo + extras  ->  <=4: 0 ataques, 5-6: 1, 7-8: 2, >=9: 3
  cada ataque: entrada por d6 (1-5 fija, 6 = la de menor defensa); fuerza = d6 + tramo + 1
  fuerza > defensa: irrupción; la barricada baja 1 nivel; entran 1 + (diferencia // 2) caminantes
  defensa = barricada + trampa + Percepción (valor) del guardia
"""
import random
from functools import lru_cache

ESCENARIOS = [
    ('Sin barricadas ni guardia', (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), 0),
    ('Sin barricadas, guardia P2', (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), 2),
    ('Sin barricadas, guardia P4', (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), 4),
    ('Ejemplo día 6 (2/1/1/0/1, alarma, guardia P2)', (2, 1, 1, 0, 1), (0, 0, 1, 0, 0), 2),
    ('Todo nivel 1, guardia P3', (1,) * 5, (0,) * 5, 3),
    ('Todo nivel 2, guardia P3', (2,) * 5, (0,) * 5, 3),
    ('Todo nivel 3, guardia P3', (3,) * 5, (0,) * 5, 3),
    ('Todo nivel 3 + trampa +2, guardia P5', (3,) * 5, (2,) * 5, 5),
]


def n_ataques(t):
    return 0 if t <= 4 else 1 if t <= 6 else 2 if t <= 8 else 3


def noche(barr, tramp, guard, tramo, extra):
    """Devuelve (P(al menos una irrupción), zombies esperados que entran)."""

    @lru_cache(None)
    def ataque(barr, k):
        # devuelve (P(sin irrupción en los k ataques restantes), zombies esperados)
        if k == 0:
            return 1.0, 0.0
        p_ok = 0.0
        ez = 0.0
        defs = [b + t + guard for b, t in zip(barr, tramp)]
        for e in range(1, 7):
            idx = e - 1 if e <= 5 else min(range(5), key=lambda i: defs[i])
            for f in range(1, 7):
                fuerza = f + tramo + 1
                p = 1 / 36
                if fuerza <= defs[idx]:
                    a, z = ataque(barr, k - 1)
                    p_ok += p * a
                    ez += p * z
                else:
                    entra = 1 + (fuerza - defs[idx]) // 2
                    nb = list(barr)
                    nb[idx] = max(0, nb[idx] - 1)
                    a, z = ataque(tuple(nb), k - 1)
                    ez += p * (entra + z)
        return p_ok, ez

    p_ok = 0.0
    ez = 0.0
    for d in range(1, 7):
        a, z = ataque(tuple(barr), n_ataques(d + tramo + extra))
        p_ok += a / 6
        ez += z / 6
    return 1 - p_ok, ez


def pelea(n_zombies, n_sup=3, sorpresa=False, rng=random.Random(7), reps=20000):
    """Golpes que reciben los supervivientes de la base contra n caminantes (bate d6+1, +1 al ataque)."""
    tot = 0
    for _ in range(reps):
        zs = [0] * n_zombies
        golpes = 0
        if sorpresa:
            for _z in zs:
                if max(rng.randint(1, 20), rng.randint(1, 20)) + 2 >= 11:
                    golpes += 1
        while zs:
            for _s in range(n_sup):
                if not zs:
                    break
                nat = rng.randint(1, 20)
                if nat == 20 or (nat > 1 and nat + 1 >= 8):
                    zs[0] += 6 + 1 if nat == 20 else rng.randint(1, 6) + 1
                    if zs[0] >= 5:
                        zs.pop(0)
            for _z in zs:
                if rng.randint(1, 20) + 2 >= 11:
                    golpes += 1
        tot += golpes
    return tot / reps


def main():
    print('## Ataques por noche según la tirada de amenaza\n')
    print('| Tramo | Extra | 0 ataques | 1 | 2 | 3 | Ataques esperados |')
    print('|---|---|---|---|---|---|---|')
    for tramo in (1, 2, 3):
        for extra in (0, 1, 3):
            c = [0] * 4
            for d in range(1, 7):
                c[n_ataques(d + tramo + extra)] += 1 / 6
            print(f'| {tramo} | +{extra} | ' + ' | '.join(f'{100 * x:.0f} %' for x in c) + f' | {sum(i * x for i, x in enumerate(c)):.2f} |')

    print('\n## Probabilidad de que entren esa noche (P irrupción / caminantes esperados)\n')
    cols = [(1, 0), (2, 0), (3, 0), (3, 3)]
    print('| Defensa de la base | Defensas | ' + ' | '.join(f'Tramo {t}{" + señal (+3)" if e else ""}' for t, e in cols) + ' |')
    print('|---|---|' + '---|' * len(cols))
    for nombre, barr, tramp, guard in ESCENARIOS:
        defs = '/'.join(str(b + t + guard) for b, t in zip(barr, tramp))
        celdas = []
        for tramo, extra in cols:
            p, ez = noche(barr, tramp, guard, tramo, extra)
            celdas.append(f'{100 * p:.0f} % / {ez:.2f}')
        print(f'| {nombre} | {defs} | ' + ' | '.join(celdas) + ' |')

    print('\n## Golpes recibidos en la base por irrupción (3 supervivientes con bate)\n')
    print('| Caminantes que entran | Con guardia o alarma | Sorprendidos (sin guardia ni alarma) |')
    print('|---|---|---|')
    for n in (1, 2, 3):
        print(f'| {n} | {pelea(n):.2f} | {pelea(n, sorpresa=True):.2f} |')

    # coste de fortificar
    print('\nFortificar las 5 entradas a nivel 3 cuesta 15 Madera, 15 Clavos, 5 Chapa y 15 fichas de construcción (15 días con 1 ficha/día).')


if __name__ == '__main__':
    main()
