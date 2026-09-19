#!/usr/bin/env python3
"""Recorta y exporta las fotos del sitio a WebP en varios anchos.

Uso:  python3 scripts/build-images.py <carpeta-con-originales>

Requiere Pillow y cwebp (brew install webp). Cada slot se recorta a 4:3
con un punto focal (fx, fy en 0..1) y se exporta a 480/800/1200/1600 px en
assets/images/<slot>-<ancho>.webp. También regenera og-<nombre>.jpg (1200x630).
Para agregar o cambiar una foto, editá SLOTS y volvé a correr el script.
"""
import os, subprocess, sys
from PIL import Image, ImageOps

SLOTS = {
    # slot        (archivo original,  aspecto, focal[, zoom])  — cada foto se usa UNA sola vez en el sitio
    # home
    'fachada':       ('_A744433.jpg', (4, 3), (0.5, 0.5)),        # hero principal
    'hogaza':        ('_A744449.jpg', (4, 3), (0.5, 1.0), 0.7),   # hero: hogazas adelante, equipo detrás
    'cafe':          ('_A744557.jpg', (4, 3), (0.5, 0.5)),        # hero: latte
    'medialuna':     ('_A744542.jpg', (4, 3), (0.5, 0.5)),        # hero: medialuna
    'manos':         ('_A744474.jpg', (4, 3), (0.5, 0.5)),        # hero: palo de amasar
    'corte':         ('_A744463.jpg', (4, 3), (0.5, 0.5)),        # happenings: cortando masa
    'desayuno':      ('_A744565.jpg', (4, 3), (0.5, 0.5)),        # happenings: croissant + latte
    'patio':         ('_A744498.jpg', (4, 3), (0.5, 0.5)),        # happenings: patio
    'hogazas-carro': ('_A744452.jpg', (4, 3), (0.3, 1.0), 0.65),  # carta: hogazas en el carro
    'cafe-negro':    ('_A744575-Editar.jpg', (4, 3), (0.5, 0.5)), # carta: café negro en vaso
    'mesa':          ('_A744596.jpg', (4, 3), (0.5, 0.5)),        # carta: mesa con uso real
    'laminados':     ('_A744569.jpg', (4, 3), (0.5, 0.5)),        # carta: croissant + medialuna
    'horno':         ('_A744492.jpg', (4, 3), (0.5, 0.5)),        # proceso: panadera junto a los hornos
    'mostrador':     ('_A744511.jpg', (4, 3), (0.6, 0.5)),        # nosotros: panadera y vitrina de panes
    # bakery B2B
    'equipo':        ('_A744503.jpg', (4, 3), (0.5, 0.5)),        # panadería: equipo produciendo
    'roll':          ('_A744551.jpg', (4, 3), (0.5, 0.5)),        # laminados: roll de canela
    'alfajor':       ('_A744585.jpg', (4, 3), (0.5, 0.5)),        # pastelería: alfajor
    'congelados':    ('_A744482.jpg', (4, 3), (0.5, 0.5)),        # congelados: bloque de masa laminada
    'hornos':        ('_A744488.jpg', (4, 3), (0.5, 0.5)),        # por qué: hornos
    # páginas de contenido
    'hogazas-masa':  ('_A744454.jpg', (4, 3), (0.5, 0.9), 0.92), # /masa-madre: hogazas en el carro y la panadería detrás (hero)
    'vitrina':       ('_A744505.jpg', (4, 3), (0.62, 0.5)),       # /masa-madre: panadera con la vitrina de panes
    'ventana':       ('_A744524.jpg', (4, 3), (0.5, 0.5)),        # /masa-madre: la panadería desde la ventana
    'cocina':        ('_A744597.jpg', (4, 3), (0.5, 0.5)),        # /masa-madre: cocina y equipo
    'cafe-alfajor':  ('_A744593.jpg', (4, 3), (0.5, 0.5)),        # /cafe-especialidad: café + alfajor
    'mesas':         ('_A744513.jpg', (4, 3), (0.5, 0.45)),       # /cafe-especialidad: clientes en el patio
    'laminadora':    ('_A744477.jpg', (4, 3), (0.5, 0.5)),        # /laminados: pasando la masa por la laminadora
    'cortante':      ('_A744461.jpg', (4, 3), (0.5, 0.5)),        # /laminados: cortando discos de masa
    'medialuna-2':   ('_A744545.jpg', (4, 3), (0.5, 0.5)),        # /laminados: medialuna (hero)
    'roll-2':        ('_A744554.jpg', (4, 3), (0.5, 0.5)),        # /laminados: roll de canela
    'cartel':        ('_A744437.jpg', (4, 3), (0.5, 0.45)),       # /centro-cordoba: cartel en la fachada
    'puerta':        ('_A744537.jpg', (4, 3), (0.5, 0.5)),        # /centro-cordoba: puerta abierta a la calle
    'salon':         ('_A744584.jpg', (4, 3), (0.5, 0.5)),        # /centro-cordoba: salón interior
}
# og-<nombre>.jpg 1200x630: (original, focal)
SQUARE = {'fachada': ('_A744433.jpg', (0.5, 0.5))}
OG = {
    'honesto': ('_A744433.jpg', (0.5, 0.5)),   # fachada (home)
    'bakery':  ('_A744449.jpg', (0.5, 0.42)),  # cocina / producción (bakery B2B)
}
WIDTHS = (480, 800, 1200, 1600)
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')


def crop(im, aspect, focal, zoom=1.0):
    """zoom < 1 recorta más cerca (fracción del encuadre máximo)."""
    W, H = im.size
    aw, ah = aspect
    if W / H > aw / ah:
        cw, ch = int(H * aw / ah), H
    else:
        cw, ch = W, int(W * ah / aw)
    cw, ch = int(cw * zoom), int(ch * zoom)
    fx, fy = focal
    x = min(max(int(fx * W - cw / 2), 0), W - cw)
    y = min(max(int(fy * H - ch / 2), 0), H - ch)
    return im.crop((x, y, x + cw, y + ch))


def load(src_dir, name):
    return ImageOps.exif_transpose(Image.open(os.path.join(src_dir, name))).convert('RGB')


def main(src_dir):
    os.makedirs(OUT, exist_ok=True)
    for slot, spec in SLOTS.items():
        src, aspect, focal = spec[:3]
        zoom = spec[3] if len(spec) > 3 else 1.0
        c = crop(load(src_dir, src), aspect, focal, zoom)
        for w in WIDTHS:
            tmp = os.path.join(OUT, f'{slot}-{w}.png')
            c.resize((w, round(w * aspect[1] / aspect[0])), Image.LANCZOS).save(tmp)
            subprocess.run(['cwebp', '-quiet', '-q', '80', '-m', '6', '-sharp_yuv', tmp,
                            '-o', os.path.join(OUT, f'{slot}-{w}.webp')], check=True)
            os.remove(tmp)
        print('ok', slot)
    for name, (src, focal) in OG.items():
        og = crop(load(src_dir, src), (1200, 630), focal).resize((1200, 630), Image.LANCZOS)
        og.save(os.path.join(OUT, f'og-{name}.jpg'), quality=85, optimize=True, progressive=True)
        print('ok', f'og-{name}.jpg')
    # 1:1 y 4:3 en JPG para el schema (Google pide 16:9, 4:3 y 1:1 para LocalBusiness/Organization)
    for name, (src, focal) in SQUARE.items():
        im = load(src_dir, src)
        crop(im, (1, 1), focal).resize((1200, 1200), Image.LANCZOS).save(os.path.join(OUT, f'{name}-1x1.jpg'), quality=85, optimize=True, progressive=True)
        crop(im, (4, 3), focal).resize((1200, 900), Image.LANCZOS).save(os.path.join(OUT, f'{name}-4x3.jpg'), quality=85, optimize=True, progressive=True)
        print('ok', f'{name}-1x1.jpg', f'{name}-4x3.jpg')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
