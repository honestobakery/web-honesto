# web-honesto

Sitio web de **honesto** — café de especialidad, pan de masa madre y comida fresca, en Independencia 180, Centro, Córdoba, Argentina. Incluye **honesto bakery**, la unidad mayorista que abastece a cafeterías y restaurantes de la ciudad.

Sitio estático en HTML + CSS, sin framework ni paso de build. Desplegado en GitHub Pages sobre el dominio propio `https://honesto.com.ar/`.

Horario: Lun–Vie 8:00–21:00 · Sáb 9:00–15:00 · Dom cerrado.

---

## Estructura

```
index.html            ← página principal (hero, carta, proceso, nosotros, FAQ, CTA)
bakery.html            ← honesto bakery: mayorista para cafeterías y restaurantes (operativo)
404.html               ← página de error para GitHub Pages

masa-madre/            ← qué es la masa madre, por qué 24 horas, cómo conservar el pan
cafe-especialidad/     ← qué es el café de especialidad, tolva invitada, café en grano
laminados/             ← medialunas, croissants y demás laminados de manteca
desayuno/              ← desayuno y brunch (se sirven todo el día)
almuerzo/              ← menú del mediodía (12 a 15)
centro-cordoba/        ← ubicación, historia del local y del casco histórico, mapa
links/                 ← página de enlaces para la bio de Instagram (reemplaza Linktree)

css/main.css           ← todos los estilos y design tokens
robots.txt, sitemap.xml, llms.txt   ← discoverability para buscadores y asistentes de IA
*.txt (32 chars hex)   ← claves de verificación de IndexNow (Bing) y Google Search Console

scripts/
  build-images.py      ← genera assets/images (WebP, varios anchos) desde las fotos originales
  build-pages.py       ← genera las seis páginas de contenido de arriba desde un solo archivo

assets/
  fonts/               ← Almonde.otf, Satoshi-*.otf, SpaceMono-*.ttf
  icons/               ← favicons y apple-touch-icon
  images/              ← fotos reales del local en WebP (varios anchos) + og-honesto.jpg
  logo/                ← variantes del logo y el isotipo
  personajes/          ← ilustraciones de línea (personaje-01…24)
```

Las páginas de contenido (`masa-madre/`, `cafe-especialidad/`, `laminados/`, `desayuno/`, `almuerzo/`, `centro-cordoba/`) **no se editan a mano**: todo su texto vive en `scripts/build-pages.py`. Para cambiar algo, se edita ahí y se corre:

```bash
python3 scripts/build-pages.py
```

Para sumar o reemplazar una foto, se agrega un slot en `SLOTS` dentro de `scripts/build-images.py` (nunca se reutiliza una foto que ya esté en otro lado del sitio) y se corre:

```bash
python3 scripts/build-images.py /ruta/a/las/fotos/originales
```

---

## Redes sociales

El contenido de redes (calendario, copys, banco de fotos) **no vive en este repo**: está en una carpeta separada. `DESIGN.md` y `honesto-brand-adn.md` sí gobiernan también las redes, y por eso quedan acá.

---

## Fuentes de productos y precios

Los precios cambian seguido y **no se cargan en el sitio**: cada página enlaza a la carta correspondiente en Fudo.

- **Carta del café** (bebidas, desayuno, almuerzo, dulces): `https://menu.fu.do/ledureausas/qr-menu`
- **Carta del obrador / mayorista** ("Honesto Obrador"): `https://menu.fu.do/independencia180/qr-menu`
- **Ficha de Google Maps**: `https://maps.app.goo.gl/o1mb7m6Jnk81puLw9`

---

## Documentación de diseño

- **`DESIGN.md`** — tokens de color, tipografía, espaciado, grilla, componentes y reglas de layout.
- **`honesto-brand-adn.md`** — voz de marca, valores, audiencia y reglas para generación de contenido.

Cualquier cambio visual o de copy debe respetar estos documentos. No inventar estilos ni textos que los contradigan. `CLAUDE.md` tiene el detalle técnico completo (reglas de SEO/GEO, tokens, convenciones) para trabajar en el repo con Claude Code.

---

## Deploy

El sitio se publica automáticamente en GitHub Pages desde la rama `main`.
El dominio custom esperado es `https://honesto.com.ar/`.

---

## Indexación (SEO / GEO)

Tras publicar cambios de contenido:

**IndexNow** (avisa a Bing, y por extensión a Copilot y ChatGPT search). La clave es el archivo `*.txt` de 32 caracteres hex en la raíz — hay dos válidas, se usa la de Bing Webmaster Tools:

```bash
KEY=60cbe1a55ca942c4aac018228e2917f0   # clave de Bing Webmaster Tools
curl -s -X POST https://api.indexnow.org/indexnow -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"honesto.com.ar\",\"key\":\"$KEY\",\"keyLocation\":\"https://honesto.com.ar/$KEY.txt\",\"urlList\":[\"https://honesto.com.ar/\",\"https://honesto.com.ar/bakery.html\"]}" -w "%{http_code}\n"
```

**Google**: pedir la reindexación desde Search Console (Inspección de URL → Solicitar indexación).

**Brave** (de donde lee Claude su búsqueda web): pedir un re-fetch en `https://search.brave.com/submit-url` cuando una página cambia de forma significativa.

El resto del trabajo de visibilidad en IA —renombrar la ficha de Google Maps y TripAdvisor (hoy a nombre de Le Dureau, el negocio anterior en el mismo local), sumar reseñas nuevas— es fuera de este repo y queda documentado en los informes de investigación compartidos aparte.
