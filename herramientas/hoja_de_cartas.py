#!/usr/bin/env python3
"""Une imágenes sueltas de cartas en hojas (sheets) válidas para Custom Deck de Tabletop Simulator.

Reglas de TTS que respeta:
  * Cuadrícula de como máximo 10 columnas x 7 filas (70 casillas).
  * La última casilla (abajo a la derecha) se reserva para la "carta oculta",
    la imagen que ven los demás cuando una carta está en tu mano.
    Por eso cada hoja lleva como máximo columnas*filas - 1 cartas.
  * Todas las casillas miden lo mismo; las casillas sobrantes se rellenan con papel liso.
  * Lado máximo de la hoja (por defecto 4096 px): si no entra, las cartas se reducen.

Uso típico:
  python3 herramientas/hoja_de_cartas.py arte/exportar/botin/ \
      --salida tts/cartas/botin/botin --oculta tts/cartas/botin/botin_dorso.png

  # Con copias físicas en la hoja (manifiesto CSV "archivo,copias"):
  python3 herramientas/hoja_de_cartas.py arte/exportar/botin/ --manifiesto botin.csv --expandir-copias ...

Por cada hoja escribe <salida>_hoja_NN.<jpg|png> y un <salida>.json con el orden de las
cartas, la cuadrícula y los valores para el diálogo de importación de TTS.
Requiere Pillow (pip install Pillow).
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageOps
except ImportError:  # pragma: no cover
    sys.exit("Falta Pillow: pip install Pillow")

MAX_COLS, MAX_FILAS = 10, 7
EXTENSIONES = {".png", ".jpg", ".jpeg", ".webp"}
PAPEL = (216, 200, 166)   # --papel de la dirección de arte (#d8c8a6)
NOCHE = (22, 25, 29)      # --noche (#16191d)
TINTA = (27, 26, 23)      # --tinta (#1b1a17)


def leer_entradas(rutas: list[str], manifiesto: str | None) -> list[tuple[Path, int]]:
    """Devuelve [(imagen, copias)] en orden alfabético, o en el orden del manifiesto."""
    if manifiesto:
        base = Path(manifiesto).parent
        salida = []
        with open(manifiesto, newline="", encoding="utf-8") as f:
            for fila in csv.reader(f):
                if not fila or fila[0].strip().startswith("#") or fila[0].strip().lower() == "archivo":
                    continue
                ruta = Path(fila[0].strip())
                if not ruta.is_absolute() and not ruta.exists():
                    ruta = base / ruta
                copias = int(fila[1]) if len(fila) > 1 and fila[1].strip() else 1
                if not ruta.exists():
                    sys.exit(f"No existe la imagen del manifiesto: {ruta}")
                salida.append((ruta, copias))
        return salida
    archivos: list[Path] = []
    for r in rutas:
        p = Path(r)
        if p.is_dir():
            archivos += sorted(x for x in p.iterdir() if x.suffix.lower() in EXTENSIONES)
        elif p.exists():
            archivos.append(p)
        else:
            sys.exit(f"No existe: {p}")
    return [(a, 1) for a in archivos]


def elegir_cuadricula(n: int, cols: int | None, filas: int | None) -> tuple[int, int]:
    """Cuadrícula más compacta que aloja n cartas + 1 casilla oculta (máx. 10x7)."""
    if cols and filas:
        return cols, filas
    mejor = None
    for c in range(2, MAX_COLS + 1):
        if cols and c != cols:
            continue
        for f in range(2, MAX_FILAS + 1):
            if filas and f != filas:
                continue
            capacidad = c * f - 1
            if capacidad < min(n, MAX_COLS * MAX_FILAS - 1):
                continue
            # menos casillas vacías primero; luego, la hoja más cuadrada
            clave = (c * f - 1 - min(n, capacidad), abs(c * 1.0 - f * 1.4))
            if mejor is None or clave < mejor[0]:
                mejor = (clave, c, f)
    if mejor is None:
        return cols or MAX_COLS, filas or MAX_FILAS
    return mejor[1], mejor[2]


def ajustar(img: Image.Image, w: int, h: int, modo: str) -> Image.Image:
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGBA")
    if img.mode == "RGBA":  # aplanar sobre papel: TTS no recorta cartas por transparencia
        fondo = Image.new("RGB", img.size, PAPEL)
        fondo.paste(img, mask=img.split()[3])
        img = fondo
    if modo == "estirar":
        return img.resize((w, h), Image.LANCZOS)
    if modo == "contener":
        return ImageOps.pad(img, (w, h), Image.LANCZOS, color=PAPEL)
    return ImageOps.fit(img, (w, h), Image.LANCZOS)  # "cubrir"


def carta_oculta_por_defecto(w: int, h: int) -> Image.Image:
    """Carta oculta genérica: noche con un '?' en papel (por si no se pasa --oculta)."""
    img = Image.new("RGB", (w, h), NOCHE)
    d = ImageDraw.Draw(img)
    m = max(4, w // 25)
    d.rectangle([m, m, w - m - 1, h - m - 1], outline=PAPEL, width=max(2, w // 120))
    r = w // 4
    cx, cy = w // 2, h // 2
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=PAPEL, width=max(3, w // 80))
    try:
        from PIL import ImageFont
        fuente = ImageFont.load_default(size=int(r * 1.2))
        d.text((cx, cy), "?", fill=PAPEL, font=fuente, anchor="mm")
    except Exception:
        pass
    return img


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entradas", nargs="*", help="Carpetas o imágenes de cartas (orden alfabético)")
    ap.add_argument("--manifiesto", help="CSV 'archivo,copias' que fija orden y copias")
    ap.add_argument("--expandir-copias", action="store_true",
                    help="Repite en la hoja cada carta tantas veces como copias tenga. "
                         "Sin esto, la hoja lleva solo caras únicas y las copias se hacen en TTS (ver JSON).")
    ap.add_argument("--salida", required=True, help="Prefijo de salida, p. ej. tts/cartas/botin/botin")
    ap.add_argument("--oculta", help="Imagen para la casilla oculta (normalmente el dorso del mazo)")
    ap.add_argument("--cols", type=int, help=f"Columnas (2..{MAX_COLS}); por defecto, automático")
    ap.add_argument("--filas", type=int, help=f"Filas (2..{MAX_FILAS}); por defecto, automático")
    ap.add_argument("--ancho", type=int, default=750, help="Ancho de carta de origen en px (750)")
    ap.add_argument("--alto", type=int, default=1050, help="Alto de carta de origen en px (1050)")
    ap.add_argument("--max-lado", type=int, default=4096, help="Lado máximo de la hoja en px (4096)")
    ap.add_argument("--ajuste", choices=["cubrir", "contener", "estirar"], default="cubrir",
                    help="Qué hacer si una imagen no tiene la proporción de la carta")
    ap.add_argument("--formato", choices=["jpg", "png"], default="jpg")
    ap.add_argument("--calidad", type=int, default=90, help="Calidad JPG (90)")
    a = ap.parse_args(argv)

    if a.cols and not 2 <= a.cols <= MAX_COLS or a.filas and not 2 <= a.filas <= MAX_FILAS:
        ap.error(f"La cuadrícula de TTS va de 2x2 a {MAX_COLS}x{MAX_FILAS}")
    if not a.entradas and not a.manifiesto:
        ap.error("Indica carpetas/imágenes o un --manifiesto")

    entradas = leer_entradas(a.entradas, a.manifiesto)
    if not entradas:
        sys.exit("No se encontraron imágenes (.png, .jpg, .webp)")
    cartas: list[tuple[Path, int]] = []  # (imagen, copias que representa)
    for ruta, copias in entradas:
        cartas += [(ruta, 1)] * copias if a.expandir_copias else [(ruta, copias)]

    cols, filas = elegir_cuadricula(len(cartas), a.cols, a.filas)
    n_hojas = math.ceil(len(cartas) / (cols * filas - 1))
    if n_hojas > 1 and not (a.cols and a.filas):
        # repartir parejo entre hojas (37 + 37 mejor que 69 + 5): cuadrícula más chica, cartas más nítidas
        cols, filas = elegir_cuadricula(math.ceil(len(cartas) / n_hojas), a.cols, a.filas)
    por_hoja = cols * filas - 1
    n_hojas = math.ceil(len(cartas) / por_hoja)
    por_hoja = math.ceil(len(cartas) / n_hojas)

    escala = min(1.0, a.max_lado / (cols * a.ancho), a.max_lado / (filas * a.alto))
    w, h = int(a.ancho * escala), int(a.alto * escala)
    if escala < 1:
        print(f"Aviso: cartas reducidas a {w}x{h} px ({escala:.0%}) para no pasar {a.max_lado} px por lado.")

    oculta = ajustar(Image.open(a.oculta), w, h, a.ajuste) if a.oculta else carta_oculta_por_defecto(w, h)
    salida = Path(a.salida)
    salida.parent.mkdir(parents=True, exist_ok=True)

    resumen = {"cuadricula": {"ancho_cartas": cols, "alto_cartas": filas}, "carta_px": [w, h], "hojas": []}
    for i in range(n_hojas):
        lote = cartas[i * por_hoja:(i + 1) * por_hoja]
        hoja = Image.new("RGB", (cols * w, filas * h), PAPEL)
        orden = []
        for j, (ruta, copias) in enumerate(lote):
            img = Image.open(ruta)
            if abs(img.width / img.height - a.ancho / a.alto) > 0.01:
                print(f"Aviso: {ruta.name} mide {img.width}x{img.height}; se aplica '{a.ajuste}'.")
            hoja.paste(ajustar(img, w, h, a.ajuste), ((j % cols) * w, (j // cols) * h))
            orden.append({"casilla": j, "card_id": (i + 1) * 100 + j, "archivo": ruta.name, "copias": copias})
        hoja.paste(oculta, ((cols - 1) * w, (filas - 1) * h))
        nombre = salida.with_name(f"{salida.name}_hoja_{i + 1:02d}.{a.formato}")
        if a.formato == "jpg":
            hoja.save(nombre, "JPEG", quality=a.calidad, optimize=True, progressive=True)
        else:
            hoja.save(nombre, "PNG", optimize=True)
        resumen["hojas"].append({
            "archivo": nombre.name, "px": list(hoja.size),
            "tts": {"Width": cols, "Height": filas, "Number": len(lote), "Back is Hidden": True},
            "cartas": orden,
        })
        print(f"{nombre}  {hoja.size[0]}x{hoja.size[1]} px  {cols}x{filas}  {len(lote)} cartas + oculta")

    resumen["total_caras"] = len(cartas)
    resumen["total_cartas_mazo"] = sum(c for _, c in cartas)
    resumen["nota"] = ("card_id = número de hoja x 100 + casilla (formato DeckIDs de TTS). "
                       "Si 'copias' > 1, duplica esa carta en TTS antes de guardar el mazo.")
    with open(salida.with_suffix(".json"), "w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)
    print(f"{salida.with_suffix('.json')}  ({resumen['total_caras']} caras, {resumen['total_cartas_mazo']} cartas en el mazo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
