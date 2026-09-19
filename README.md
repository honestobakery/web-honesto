# web-honesto

Sitio web estático para **Honesto — Bakery & Café / Comida Fresca**, ubicado en Independencia 180, Córdoba, Argentina.

Una sola página HTML + CSS, sin framework ni paso de build. Desplegado en GitHub Pages.

---

## Estructura

```
index.html           ← página principal con todas las secciones
bakery.html          ← unidad mayorista (próximamente)
404.html             ← página de error para GitHub Pages
css/main.css         ← todos los estilos y design tokens
robots.txt           ← acceso para buscadores y motores de IA
sitemap.xml          ← mapa del sitio (con imágenes)
llms.txt             ← resumen del negocio para asistentes de IA (GEO)

assets/
  fonts/             ← Almonde.otf, Satoshi-*.otf, SpaceMono-*.ttf
  icons/             ← favicons y apple-touch-icon
  images/            ← fotos reales del local en WebP (varios anchos) + og-honesto.jpg
scripts/             ← build-images.py: regenera las fotos desde los originales
  logo/              ← variantes del logo y el isotipo
  personajes/        ← ilustraciones de línea (personaje-01…24)
```


---

## Documentación de diseño

- **`DESIGN.md`** — tokens de color, tipografía, espaciado, grilla, componentes y reglas de layout.
- **`honesto-brand-adn.md`** — voz de marca, valores, audiencia y reglas para generación de contenido.

Cualquier cambio visual o de copy debe respetar estos documentos. No inventar estilos ni textos que los contradigan.

---

## Deploy

El sitio se publica automáticamente en GitHub Pages desde la rama `main`.
El dominio custom esperado es `https://honesto.com.ar/`.

---

## Indexación

Tras publicar cambios de contenido, avisar a Bing/Copilot vía IndexNow (la clave es el archivo `*.txt` de 32 caracteres hex en la raíz):

```bash
KEY=60cbe1a55ca942c4aac018228e2917f0   # clave de Bing Webmaster Tools (hay una segunda clave propia en la raíz; ambas valen)
curl -s -X POST https://api.indexnow.org/indexnow -H "Content-Type: application/json; charset=utf-8" \
  -d "{\"host\":\"honesto.com.ar\",\"key\":\"$KEY\",\"keyLocation\":\"https://honesto.com.ar/$KEY.txt\",\"urlList\":[\"https://honesto.com.ar/\",\"https://honesto.com.ar/bakery.html\"]}" -w "%{http_code}\n"
```

Para Google, pedir la reindexación desde Search Console (Inspección de URL → Solicitar indexación).
