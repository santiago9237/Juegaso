"""Genera los modelos 3D de los personajes para Tabletop Simulator (Custom Model).

Cada personaje sale como:
  modelos/<id>/<id>.obj       malla (Y hacia arriba, 1 unidad = 1 unidad de mesa de TTS)
  modelos/<id>/<id>.mtl       material que apunta a la textura (para visores; TTS usa solo .obj + imagen)
  modelos/<id>/<id>.png       textura (Diffuse/Image en TTS)
  modelos/<id>/<id>_collider.obj   collider simple (caja)

Zombies: figura de cartón de pie (standee) con la ilustración del juego al frente, el dorso
en tinta oscura y una base redonda con el nombre. Supervivientes: miniatura low-poly con
colores y un accesorio de su oficio, sobre una base con el nombre (no hay ilustraciones de
supervivientes todavía).

Uso: python3 herramientas/modelos_3d.py
"""
import math
import os

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(RAIZ, "arte", "img")
FUENTES = os.path.join(RAIZ, "arte", "fuentes")
SALIDA = os.path.join(RAIZ, "modelos")

PAPEL = (216, 200, 166)
TINTA = (27, 26, 23)
ROJO = (146, 43, 43)
OXIDO = (180, 88, 58)

BASE_R = 0.6      # radio de la base
BASE_H = 0.14     # alto de la base
SEG = 40          # segmentos del cilindro


def fuente(nombre, tam):
    try:
        return ImageFont.truetype(os.path.join(FUENTES, nombre), tam)
    except OSError:
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", tam)


# --------------------------------------------------------------------------- malla

class Malla:
    def __init__(self):
        self.v, self.vt, self.vn, self.f = [], [], [], []

    def _v(self, p):
        self.v.append(p)
        return len(self.v)

    def _t(self, uv):
        self.vt.append(uv)
        return len(self.vt)

    def _n(self, n):
        self.vn.append(n)
        return len(self.vn)

    def quad(self, ps, uvs, normal=None):
        """ps: 4 puntos en sentido antihorario mirando desde afuera."""
        if normal is None:
            a, b, c = ps[0], ps[1], ps[2]
            u = [b[i] - a[i] for i in range(3)]
            w = [c[i] - a[i] for i in range(3)]
            normal = norm(cruz(u, w))
        ni = self._n(normal)
        idx = [(self._v(p), self._t(t), ni) for p, t in zip(ps, uvs)]
        self.f.append(idx)

    def tri(self, ps, uvs, normals):
        idx = [(self._v(p), self._t(t), self._n(n)) for p, t, n in zip(ps, uvs, normals)]
        self.f.append(idx)

    def caja(self, c, s, uv, rot_y=0.0, rot_x=0.0, rot_z=0.0):
        """Caja centrada en c, tamaño s, todas las caras con el mismo rectángulo de UV."""
        hx, hy, hz = s[0] / 2, s[1] / 2, s[2] / 2
        esquinas = {}
        for sx in (-1, 1):
            for sy in (-1, 1):
                for sz in (-1, 1):
                    p = rotar((sx * hx, sy * hy, sz * hz), rot_x, rot_y, rot_z)
                    esquinas[(sx, sy, sz)] = (p[0] + c[0], p[1] + c[1], p[2] + c[2])
        u0, v0, u1, v1 = uv
        uvq = [(u0, v0), (u1, v0), (u1, v1), (u0, v1)]
        caras = [
            [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)],     # frente +z
            [(1, -1, -1), (-1, -1, -1), (-1, 1, -1), (1, 1, -1)],  # atrás
            [(1, -1, 1), (1, -1, -1), (1, 1, -1), (1, 1, 1)],      # +x
            [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)],  # -x
            [(-1, 1, 1), (1, 1, 1), (1, 1, -1), (-1, 1, -1)],      # arriba
            [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)],  # abajo
        ]
        for cara in caras:
            self.quad([esquinas[k] for k in cara], uvq)

    def esfera(self, c, r, uv, sx=1.0, sy=1.0, sz=1.0, lat=8, lon=12):
        u0, v0, u1, v1 = uv
        um, vm = (u0 + u1) / 2, (v0 + v1) / 2

        def p(i, j):
            th = math.pi * i / lat
            ph = 2 * math.pi * j / lon
            n = (math.sin(th) * math.cos(ph), math.cos(th), math.sin(th) * math.sin(ph))
            return (c[0] + n[0] * r * sx, c[1] + n[1] * r * sy, c[2] + n[2] * r * sz), n

        for i in range(lat):
            for j in range(lon):
                a, na = p(i, j)
                b, nb = p(i + 1, j)
                cc, nc = p(i + 1, j + 1)
                d, nd = p(i, j + 1)
                self.tri([a, d, cc], [(um, vm)] * 3, [na, nd, nc])
                self.tri([a, cc, b], [(um, vm)] * 3, [na, nc, nb])

    def cilindro(self, c, r, h, uv_lado, uv_tapa=None, tapa_circular=None, seg=SEG, r_arriba=None):
        """Cilindro vertical con base en c[1]. tapa_circular=(cu, cv, ru, rv) mapea la tapa a un círculo de la textura."""
        r2 = r if r_arriba is None else r_arriba
        u0, v0, u1, v1 = uv_lado
        y0, y1 = c[1], c[1] + h
        for k in range(seg):
            a0 = 2 * math.pi * k / seg
            a1 = 2 * math.pi * (k + 1) / seg
            p00 = (c[0] + r * math.cos(a0), y0, c[2] + r * math.sin(a0))
            p01 = (c[0] + r * math.cos(a1), y0, c[2] + r * math.sin(a1))
            p11 = (c[0] + r2 * math.cos(a1), y1, c[2] + r2 * math.sin(a1))
            p10 = (c[0] + r2 * math.cos(a0), y1, c[2] + r2 * math.sin(a0))
            n0 = (math.cos(a0), 0, math.sin(a0))
            n1 = (math.cos(a1), 0, math.sin(a1))
            ua = u0 + (u1 - u0) * k / seg
            ub = u0 + (u1 - u0) * (k + 1) / seg
            self.tri([p00, p11, p01], [(ua, v0), (ub, v1), (ub, v0)], [n0, n1, n1])
            self.tri([p00, p10, p11], [(ua, v0), (ua, v1), (ub, v1)], [n0, n0, n1])
        # tapas
        for y, rr, arriba in ((y1, r2, True), (y0, r, False)):
            centro = (c[0], y, c[2])
            n = (0, 1 if arriba else -1, 0)
            for k in range(seg):
                a0 = 2 * math.pi * k / seg
                a1 = 2 * math.pi * (k + 1) / seg
                q0 = (c[0] + rr * math.cos(a0), y, c[2] + rr * math.sin(a0))
                q1 = (c[0] + rr * math.cos(a1), y, c[2] + rr * math.sin(a1))
                if arriba and tapa_circular:
                    cu, cv, ru, rv = tapa_circular
                    # mirando desde arriba: +x a la derecha, -z hacia arriba de la imagen
                    t0 = (cu + ru * math.cos(a0), cv - rv * math.sin(a0) * -1)
                    t1 = (cu + ru * math.cos(a1), cv - rv * math.sin(a1) * -1)
                    tc = (cu, cv)
                    t0 = (cu + ru * math.cos(a0), cv - rv * math.sin(a0))
                    t1 = (cu + ru * math.cos(a1), cv - rv * math.sin(a1))
                else:
                    uv = uv_tapa or uv_lado
                    tc = t0 = t1 = ((uv[0] + uv[2]) / 2, (uv[1] + uv[3]) / 2)
                if arriba:
                    self.tri([centro, q1, q0], [tc, t1, t0], [n, n, n])
                else:
                    self.tri([centro, q0, q1], [tc, t0, t1], [n, n, n])

    def guardar(self, ruta, nombre_mtl, material):
        with open(ruta, "w") as fh:
            fh.write(f"# Día 30 · modelo para Tabletop Simulator\nmtllib {nombre_mtl}\no {material}\n")
            for p in self.v:
                fh.write(f"v {p[0]:.5f} {p[1]:.5f} {p[2]:.5f}\n")
            for t in self.vt:
                fh.write(f"vt {t[0]:.5f} {t[1]:.5f}\n")
            for n in self.vn:
                fh.write(f"vn {n[0]:.5f} {n[1]:.5f} {n[2]:.5f}\n")
            fh.write(f"usemtl {material}\ns off\n")
            for cara in self.f:
                fh.write("f " + " ".join(f"{a}/{b}/{c}" for a, b, c in cara) + "\n")


def cruz(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a):
    l = math.sqrt(sum(x * x for x in a)) or 1
    return tuple(x / l for x in a)


def rotar(p, rx, ry, rz):
    x, y, z = p
    if rx:
        c, s = math.cos(rx), math.sin(rx)
        y, z = y * c - z * s, y * s + z * c
    if rz:
        c, s = math.cos(rz), math.sin(rz)
        x, y = x * c - y * s, x * s + y * c
    if ry:
        c, s = math.cos(ry), math.sin(ry)
        x, z = x * c + z * s, -x * s + z * c
    return (x, y, z)


def escribir_mtl(ruta, material, textura):
    with open(ruta, "w") as fh:
        fh.write(f"newmtl {material}\nKa 1 1 1\nKd 1 1 1\nKs 0.05 0.05 0.05\nNs 10\nmap_Kd {textura}\n")


def collider(ruta, ancho, alto, prof):
    m = Malla()
    m.caja((0, alto / 2, 0), (ancho, alto, prof), (0, 0, 1, 1))
    with open(ruta, "w") as fh:
        for p in m.v:
            fh.write(f"v {p[0]:.4f} {p[1]:.4f} {p[2]:.4f}\n")
        for cara in m.f:
            fh.write("f " + " ".join(str(a) for a, _, _ in cara) + "\n")


# --------------------------------------------------------------------------- texturas

def textura_base(tam, color_anillo, nombre, subtitulo):
    """Tapa de la base vista desde arriba: disco oscuro con anillo de color y el nombre."""
    im = Image.new("RGB", (tam, tam), TINTA)
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, tam - 1, tam - 1), fill=(42, 38, 33))
    a = int(tam * 0.06)
    d.ellipse((a, a, tam - a, tam - a), outline=color_anillo, width=int(tam * 0.045))
    f1 = fuente("BigShouldersStencilDisplay.ttf", int(tam * 0.13))
    f2 = fuente("SpecialElite.ttf", int(tam * 0.075))
    # nombre en la mitad de adelante (abajo en la imagen = frente del modelo)
    d.text((tam / 2, tam * 0.78), nombre.upper(), font=f1, fill=PAPEL, anchor="mm")
    if subtitulo:
        d.text((tam / 2, tam * 0.89), subtitulo, font=f2, fill=(185, 166, 130), anchor="mm")
    return im


def textura_papel(tam):
    im = Image.new("RGB", tam, PAPEL)
    ruido = Image.effect_noise(tam, 28).convert("L")
    ruido = ImageOps.colorize(ruido, (170, 150, 115), (232, 220, 192))
    return Image.blend(im, ruido, 0.35)


# --------------------------------------------------------------------------- zombies

ZOMBIES = [
    ("caminante", "Caminante", "caminante.jpg", (120, 120, 110)),
    ("corredor", "Corredor", "corredor.jpg", OXIDO),
    ("bruto", "Bruto", "bruto.jpg", (90, 70, 50)),
    ("infectado_acido", "Infectado ácido", "infectado_acido.jpg", (130, 175, 60)),
    ("chillon", "Chillón", "chillon.jpg", (60, 90, 140)),
]


def zombie(id_, nombre, archivo, color):
    carpeta = os.path.join(SALIDA, id_)
    os.makedirs(carpeta, exist_ok=True)
    W = 2048
    tex = Image.new("RGB", (W, W), PAPEL)
    # frente: ilustración 2:3 en (0,0)-(1024,1536)
    arte = Image.open(os.path.join(IMG, archivo)).convert("RGB")
    arte = ImageOps.fit(arte, (1024, 1536), Image.LANCZOS)
    tex.paste(arte, (0, 0))
    # dorso: la misma silueta en tinta, oscura y espejada, con el 30
    dorso = ImageOps.mirror(arte).convert("L")
    dorso = ImageEnhance.Contrast(dorso).enhance(1.4)
    dorso = ImageOps.colorize(dorso, (14, 14, 14), (70, 62, 52))
    dd = ImageDraw.Draw(dorso)
    dd.text((512, 1300), "DÍA 30", font=fuente("BigShouldersStencilDisplay.ttf", 150), fill=ROJO, anchor="mm")
    dd.text((512, 1420), nombre.upper(), font=fuente("SpecialElite.ttf", 64), fill=PAPEL, anchor="mm")
    tex.paste(dorso, (1024, 0))
    # franja de papel para cantos y base
    tex.paste(textura_papel((1024, 512)), (1024, 1536))
    tex.paste(textura_base(512, color, nombre, "zombie"), (0, 1536))
    ImageDraw.Draw(tex).rectangle((512, 1536, 1023, 2047), fill=(42, 38, 33))
    tex.save(os.path.join(carpeta, f"{id_}.png"))

    U = lambda x, y: (x / W, 1 - y / W)  # píxel → UV (v hacia arriba)
    m = Malla()
    # base
    m.cilindro((0, 0, 0), BASE_R, BASE_H, uv_lado=(U(512, 2047)[0], U(512, 2047)[1], U(1023, 1536)[0], U(1023, 1536)[1]),
               uv_tapa=(U(600, 1600)[0], U(600, 1600)[1], U(700, 1700)[0], U(700, 1700)[1]),
               tapa_circular=(U(256, 1792)[0], U(256, 1792)[1], 256 / W, 256 / W), r_arriba=BASE_R * 0.96)
    # cartón: 1.2 de ancho, 1.8 de alto, 0.04 de espesor, apenas detrás del centro
    w, h, e = 1.1, 1.65, 0.035
    x0, x1 = -w / 2, w / 2
    y0, y1 = BASE_H - 0.02, BASE_H - 0.02 + h
    z0, z1 = -0.12 - e / 2, -0.12 + e / 2
    fu0, fv0 = U(0, 1536)
    fu1, fv1 = U(1024, 0)
    m.quad([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], [(fu0, fv0), (fu1, fv0), (fu1, fv1), (fu0, fv1)])
    bu0, bv0 = U(1024, 1536)
    bu1, bv1 = U(2048, 0)
    m.quad([(x1, y0, z0), (x0, y0, z0), (x0, y1, z0), (x1, y1, z0)], [(bu0, bv0), (bu1, bv0), (bu1, bv1), (bu0, bv1)])
    pu0, pv0 = U(1100, 2000)
    pu1, pv1 = U(1900, 1600)
    uvp = [(pu0, pv0), (pu1, pv0), (pu1, pv1), (pu0, pv1)]
    m.quad([(x1, y0, z1), (x1, y0, z0), (x1, y1, z0), (x1, y1, z1)], uvp)
    m.quad([(x0, y0, z0), (x0, y0, z1), (x0, y1, z1), (x0, y1, z0)], uvp)
    m.quad([(x0, y1, z1), (x1, y1, z1), (x1, y1, z0), (x0, y1, z0)], uvp)
    m.guardar(os.path.join(carpeta, f"{id_}.obj"), f"{id_}.mtl", id_)
    escribir_mtl(os.path.join(carpeta, f"{id_}.mtl"), id_, f"{id_}.png")
    collider(os.path.join(carpeta, f"{id_}_collider.obj"), 1.2, BASE_H + h, 1.2)
    return id_


# --------------------------------------------------------------------------- supervivientes

# paleta: nombre → color (cada color ocupa un cuadrado de la textura)
PALETA = {
    "piel": (214, 170, 135), "piel2": (160, 110, 80), "pelo": (45, 32, 25), "canas": (190, 190, 185),
    "pantalon": (52, 58, 72), "jean": (60, 80, 110), "botas": (40, 32, 26), "blanco": (225, 220, 205),
    "celeste": (120, 165, 175), "azul": (35, 50, 85), "naranja": (200, 110, 40), "verde": (70, 90, 60),
    "rojo": (150, 40, 35), "gris": (110, 110, 105), "marron": (110, 80, 50), "metal": (150, 150, 150),
    "negro": (25, 25, 25), "mostaza": (190, 150, 60), "bordo": (110, 30, 40), "beige": (190, 170, 130),
}

SUPERVIVIENTES = [
    # id, nombre, oficio, camisa, pantalón, pelo, piel, accesorios, escala
    ("marta_rios", "Marta Ríos", "enfermera", "celeste", "celeste", "pelo", "piel", ["bolso_medico", "cola"], 0.97),
    ("raul_ibarra", "Raúl Ibarra", "ex policía", "azul", "pantalon", "pelo", "piel2", ["chaleco", "gorra_policia"], 1.03),
    ("sofia_lenz", "Sofía Lenz", "mecánica", "naranja", "naranja", "pelo", "piel", ["llave", "cola"], 0.98),
    ("tomas_ferro", "Tomás Ferro", "cocinero", "blanco", "pantalon", "pelo", "piel", ["gorro_chef", "delantal", "cuchilla"], 1.05),
    ("nico_vidal", "Nico Vidal", "estudiante", "rojo", "jean", "pelo", "piel2", ["mochila"], 0.96),
    ("aurelio_pando", "Aurelio Pando", "cazador", "verde", "marron", "canas", "piel", ["rifle", "gorro_lana"], 1.0),
    ("elena_quiroga", "Elena Quiroga", "maestra", "bordo", "pantalon", "canas", "piel", ["rodete", "libro"], 0.97),
    ("elias_ortega", "Elías Ortega", "radioaficionado", "beige", "marron", "canas", "piel", ["radio", "lentes"], 0.95),
    ("carla_sosa", "Carla Sosa", "bombera", "mostaza", "mostaza", "pelo", "piel2", ["casco", "hacha"], 1.03),
    ("lu", "Lu", "12 años", "verde", "jean", "pelo", "piel", ["mochila_chica"], 0.78),
]


def superviviente(id_, nombre, oficio, camisa, pantalon, pelo, piel, acc, escala):
    carpeta = os.path.join(SALIDA, id_)
    os.makedirs(carpeta, exist_ok=True)
    W = 1024
    tex = Image.new("RGB", (W, W), PAPEL)
    d = ImageDraw.Draw(tex)
    celdas = {}
    for i, (k, col) in enumerate(PALETA.items()):
        cx, cy = (i % 8) * 64, (i // 8) * 64
        d.rectangle((cx, cy, cx + 63, cy + 63), fill=col)
        celdas[k] = ((cx + 8) / W, 1 - (cy + 56) / W, (cx + 56) / W, 1 - (cy + 8) / W)
    tex.paste(textura_base(512, PALETA[camisa], nombre, oficio), (0, 512))
    d.rectangle((512, 512, 1023, 1023), fill=(42, 38, 33))
    # sombreado suave de los colores para que no queden planos
    tex = tex.filter(ImageFilter.SMOOTH)
    tex.save(os.path.join(carpeta, f"{id_}.png"))

    C = celdas
    m = Malla()
    m.cilindro((0, 0, 0), BASE_R, BASE_H, uv_lado=(560 / W, 1 - 1000 / W, 1000 / W, 1 - 560 / W),
               tapa_circular=(256 / W, 1 - 768 / W, 256 / W, 256 / W), r_arriba=BASE_R * 0.96)
    s = escala
    y = BASE_H
    # piernas y botas
    for lado in (-1, 1):
        m.caja((0.1 * lado * s, y + 0.06 * s, 0.02 * s), (0.15 * s, 0.12 * s, 0.24 * s), C["botas"])
        m.caja((0.1 * lado * s, y + 0.38 * s, 0), (0.15 * s, 0.55 * s, 0.17 * s), C[pantalon])
    # torso
    ty = y + 0.65 * s
    m.caja((0, ty + 0.27 * s, 0), (0.42 * s, 0.56 * s, 0.24 * s), C[camisa])
    # brazos, un poco abiertos
    for lado in (-1, 1):
        m.caja((0.27 * lado * s, ty + 0.27 * s, 0), (0.12 * s, 0.52 * s, 0.14 * s), C[camisa], rot_z=0.12 * lado)
        m.caja((0.31 * lado * s, ty - 0.02 * s, 0.01 * s), (0.1 * s, 0.1 * s, 0.11 * s), C[piel])
    # cuello y cabeza
    hy = ty + 0.56 * s
    m.caja((0, hy + 0.04 * s, 0), (0.12 * s, 0.08 * s, 0.12 * s), C[piel])
    m.esfera((0, hy + 0.2 * s, 0), 0.15 * s, C[piel], sy=1.1)
    m.esfera((0, hy + 0.25 * s, -0.02 * s), 0.155 * s, C[pelo], sy=0.85, sz=1.0, lat=6)

    for a in acc:
        if a == "bolso_medico":
            m.caja((-0.3 * s, ty + 0.05 * s, 0.05 * s), (0.12 * s, 0.2 * s, 0.26 * s), C["blanco"])
            m.caja((-0.365 * s, ty + 0.05 * s, 0.05 * s), (0.01 * s, 0.1 * s, 0.03 * s), C["rojo"])
            m.caja((-0.365 * s, ty + 0.05 * s, 0.05 * s), (0.01 * s, 0.03 * s, 0.1 * s), C["rojo"])
        elif a == "cola":
            m.esfera((0, hy + 0.2 * s, -0.17 * s), 0.07 * s, C[pelo], sy=1.3)
        elif a == "chaleco":
            m.caja((0, ty + 0.3 * s, 0), (0.45 * s, 0.4 * s, 0.27 * s), C["negro"])
        elif a == "gorra_policia":
            m.cilindro((0, hy + 0.3 * s, 0), 0.16 * s, 0.08 * s, C["azul"], seg=14)
            m.caja((0, hy + 0.31 * s, 0.17 * s), (0.22 * s, 0.02 * s, 0.1 * s), C["negro"])
        elif a == "llave":
            m.caja((0.36 * s, ty - 0.12 * s, 0.05 * s), (0.04 * s, 0.32 * s, 0.07 * s), C["metal"], rot_x=0.4)
        elif a == "gorro_chef":
            m.cilindro((0, hy + 0.3 * s, 0), 0.14 * s, 0.2 * s, C["blanco"], seg=14, r_arriba=0.17 * s)
        elif a == "delantal":
            m.caja((0, ty + 0.05 * s, 0.13 * s), (0.36 * s, 0.6 * s, 0.02 * s), C["blanco"])
        elif a == "cuchilla":
            m.caja((-0.33 * s, ty - 0.13 * s, 0.06 * s), (0.02 * s, 0.22 * s, 0.1 * s), C["metal"])
        elif a == "mochila":
            m.caja((0, ty + 0.25 * s, -0.2 * s), (0.34 * s, 0.42 * s, 0.16 * s), C["mostaza"])
        elif a == "mochila_chica":
            m.caja((0, ty + 0.27 * s, -0.18 * s), (0.28 * s, 0.32 * s, 0.13 * s), C["naranja"])
        elif a == "rifle":
            m.caja((0.05 * s, ty + 0.3 * s, -0.17 * s), (0.05 * s, 0.85 * s, 0.06 * s), C["marron"], rot_z=-0.5)
        elif a == "gorro_lana":
            m.esfera((0, hy + 0.28 * s, 0), 0.16 * s, C["naranja"], sy=0.75, lat=6)
        elif a == "rodete":
            m.esfera((0, hy + 0.38 * s, -0.04 * s), 0.08 * s, C["canas"])
        elif a == "libro":
            m.caja((0.33 * s, ty + 0.05 * s, 0.08 * s), (0.05 * s, 0.24 * s, 0.18 * s), C["rojo"])
        elif a == "radio":
            m.caja((0.33 * s, ty + 0.02 * s, 0.06 * s), (0.1 * s, 0.18 * s, 0.24 * s), C["gris"])
            m.caja((0.33 * s, ty + 0.2 * s, 0.14 * s), (0.015 * s, 0.25 * s, 0.015 * s), C["metal"])
        elif a == "lentes":
            m.caja((0, hy + 0.22 * s, 0.15 * s), (0.2 * s, 0.035 * s, 0.02 * s), C["negro"])
        elif a == "casco":
            m.esfera((0, hy + 0.27 * s, 0), 0.18 * s, C["rojo"], sy=0.75, lat=6)
            m.caja((0, hy + 0.21 * s, -0.12 * s), (0.36 * s, 0.03 * s, 0.14 * s), C["rojo"])
        elif a == "hacha":
            m.caja((0.36 * s, ty + 0.05 * s, 0.05 * s), (0.04 * s, 0.6 * s, 0.04 * s), C["marron"])
            m.caja((0.36 * s, ty + 0.32 * s, 0.13 * s), (0.03 * s, 0.14 * s, 0.16 * s), C["rojo"])

    m.guardar(os.path.join(carpeta, f"{id_}.obj"), f"{id_}.mtl", id_)
    escribir_mtl(os.path.join(carpeta, f"{id_}.mtl"), id_, f"{id_}.png")
    collider(os.path.join(carpeta, f"{id_}_collider.obj"), 1.2, BASE_H + 1.6 * s, 1.2)
    return id_


def main():
    hechos = [zombie(*z) for z in ZOMBIES]
    hechos += [superviviente(*p) for p in SUPERVIVIENTES]
    for h in hechos:
        print("modelos/" + h)


if __name__ == "__main__":
    main()
