#!/usr/bin/env python3
"""Recorta y exporta las fotos del sitio a WebP en varios anchos.

Uso:  python3 scripts/build-images.py <carpeta-con-originales>

Requiere Pillow y cwebp (brew install webp). Cada slot se recorta a 4:3
con un punto focal (fx, fy en 0..1) y se exporta a 480/800/1200/1600 px en
assets/images/<slot>-<ancho>.webp. También regenera og-honesto.jpg (1200x630).
Para agregar o cambiar una foto, editá SLOTS y volvé a correr el script.
"""
import os, subprocess, sys
from PIL import Image, ImageOps

SLOTS = {
    # slot        (archivo original,  aspecto, focal)
    'hero-local': ('_A744449.jpg', (4, 3), (0.5, 0.42)),
    'fachada':    ('_A744433.jpg', (4, 3), (0.5, 0.5)),
    'cafe':       ('_A744557.jpg', (4, 3), (0.5, 0.5)),
    'medialuna':  ('_A744542.jpg', (4, 3), (0.5, 0.5)),
    'manos':      ('_A744474.jpg', (4, 3), (0.5, 0.5)),
    'pan':        ('_A744501.jpg', (4, 3), (0.5, 0.5)),
    'desayuno':   ('_A744565.jpg', (4, 3), (0.5, 0.5)),
    'patio':      ('_A744498.jpg', (4, 3), (0.5, 0.5)),
    'horno':      ('_A744492.jpg', (4, 3), (0.5, 0.5)),
}
OG = ('_A744449.jpg', (0.5, 0.42))
WIDTHS = (480, 800, 1200, 1600)
OUT = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')


def crop(im, aspect, focal):
    W, H = im.size
    aw, ah = aspect
    if W / H > aw / ah:
        cw, ch = int(H * aw / ah), H
    else:
        cw, ch = W, int(W * ah / aw)
    fx, fy = focal
    x = min(max(int(fx * W - cw / 2), 0), W - cw)
    y = min(max(int(fy * H - ch / 2), 0), H - ch)
    return im.crop((x, y, x + cw, y + ch))


def load(src_dir, name):
    return ImageOps.exif_transpose(Image.open(os.path.join(src_dir, name))).convert('RGB')


def main(src_dir):
    os.makedirs(OUT, exist_ok=True)
    for slot, (src, aspect, focal) in SLOTS.items():
        c = crop(load(src_dir, src), aspect, focal)
        for w in WIDTHS:
            tmp = os.path.join(OUT, f'{slot}-{w}.png')
            c.resize((w, round(w * aspect[1] / aspect[0])), Image.LANCZOS).save(tmp)
            subprocess.run(['cwebp', '-quiet', '-q', '80', '-m', '6', '-sharp_yuv', tmp,
                            '-o', os.path.join(OUT, f'{slot}-{w}.webp')], check=True)
            os.remove(tmp)
        print('ok', slot)
    src, focal = OG
    og = crop(load(src_dir, src), (1200, 630), focal).resize((1200, 630), Image.LANCZOS)
    og.save(os.path.join(OUT, 'og-honesto.jpg'), quality=85, optimize=True, progressive=True)
    print('ok og-honesto.jpg')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
