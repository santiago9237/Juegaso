"""Pone los puntos rojos de posición sobre una loseta, siempre en el mismo lugar.

Las losetas se dibujan sin puntos (con ChatGPT u otra herramienta) y este script
los agrega encima, alineados a la cuadrícula de 3 × 3 zonas por loseta. Así todas
las losetas encajan y los puntos quedan iguales en todas.

Uso:
  python3 herramientas/puntos_loseta.py entrada.png salida.jpg --todos
  python3 herramientas/puntos_loseta.py entrada.png salida.jpg --zonas A1,B1,C1,B2,B3
  python3 herramientas/puntos_loseta.py hospital.png hospital.jpg --losetas 2x2 --zonas A1,C1,E1,B4,E5
  python3 herramientas/puntos_loseta.py casa.png casa.jpg --zonas A1,A2,A3 --libres 0.62,0.30 0.62,0.75

Zonas: letra = columna (A, B, C… de izquierda a derecha), número = fila (1, 2, 3… de arriba
abajo). Una loseta simple tiene A–C y 1–3; una de 2 × 2 losetas tiene A–F y 1–6.
--libres agrega puntos en posiciones fraccionarias (x, y de 0 a 1 sobre toda la imagen),
para habitaciones que no coinciden con el centro de una zona.
"""
import argparse

from PIL import Image, ImageDraw, ImageFilter

LADO_LOSETA = 1500  # px por loseta (500 px por zona)
ROJO = (176, 18, 24)
BRILLO = (255, 235, 200)


def zona_a_xy(zona, cols, filas):
    letra, num = zona[0].upper(), int(zona[1:])
    c, f = ord(letra) - ord("A"), num - 1
    if not (0 <= c < cols and 0 <= f < filas):
        raise SystemExit(f"Zona fuera de la loseta: {zona}")
    return (c + 0.5) / cols, (f + 0.5) / filas


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entrada")
    ap.add_argument("salida")
    ap.add_argument("--losetas", default="1x1", help="ancho x alto en losetas, p. ej. 1x1 o 2x2")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--todos", action="store_true", help="un punto en el centro de cada zona")
    g.add_argument("--zonas", default="", help="lista de zonas separadas por coma, p. ej. A1,B2")
    ap.add_argument("--libres", nargs="*", default=[], help="puntos extra x,y en fracciones de 0 a 1")
    ap.add_argument("--radio", type=int, default=46, help="radio del punto en px (con 500 px por zona)")
    a = ap.parse_args()

    lw, lh = (int(n) for n in a.losetas.lower().split("x"))
    cols, filas = 3 * lw, 3 * lh
    W, H = LADO_LOSETA * lw, LADO_LOSETA * lh

    img = Image.open(a.entrada).convert("RGB").resize((W, H), Image.LANCZOS)

    puntos = []
    if a.todos:
        puntos = [((c + 0.5) / cols, (f + 0.5) / filas) for f in range(filas) for c in range(cols)]
    elif a.zonas:
        puntos = [zona_a_xy(z.strip(), cols, filas) for z in a.zonas.split(",") if z.strip()]
    for par in a.libres:
        x, y = (float(v) for v in par.split(","))
        puntos.append((x, y))

    r = a.radio
    brillo = Image.new("L", (W, H), 0)
    dib_b = ImageDraw.Draw(brillo)
    for fx, fy in puntos:
        x, y = fx * W, fy * H
        dib_b.ellipse((x - r * 1.45, y - r * 1.45, x + r * 1.45, y + r * 1.45), fill=150)
    brillo = brillo.filter(ImageFilter.GaussianBlur(r * 0.45))
    img = Image.composite(Image.new("RGB", (W, H), BRILLO), img, brillo)

    dib = ImageDraw.Draw(img)
    for fx, fy in puntos:
        x, y = fx * W, fy * H
        dib.ellipse((x - r, y - r, x + r, y + r), fill=ROJO, outline=(70, 8, 10), width=max(2, r // 12))

    img.save(a.salida, quality=90)
    print(f"{a.salida}: {W}×{H} px, {len(puntos)} puntos")


if __name__ == "__main__":
    main()
