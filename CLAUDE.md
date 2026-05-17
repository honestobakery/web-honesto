# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Web frontend for **Honesto**, a Bakery & Café at Independencia 180, Córdoba, Argentina. Pure HTML + CSS static site, hosted on GitHub Pages — no build step, no framework.

## Structure

```
index.html           ← single page, all sections
css/main.css         ← all styles + design tokens
assets/
  fonts/             ← Almonde.otf, Satoshi-*.otf, SpaceMono-*.ttf (all loaded via @font-face)
  logo/              ← logo-full-dark.png, logo-full-white.png, logo-dark.png (no tagline),
                        isotipo-dark.png, isotipo-white.png, logo-full-white-wide.png
  personajes/        ← personaje-01.png … personaje-24.png (charcoal line-art illustrations)
```

**Logo variants:** `*-dark` = charcoal on transparent (use on cream/rose backgrounds). `*-white` = white on transparent (use on blue/charcoal backgrounds). `logo-dark.png` = squiggle + "honesto" script only (no tagline) — used in nav. `isotipo-*` = squiggle alone.

## Brand & Design System

All visual and communication decisions must follow two canonical documents:

- **`DESIGN.md`** — design tokens, color palette, typography, spacing, grid, component specs (buttons, inputs, cards), and layout rules.
- **`honesto-brand-adn.md`** — brand voice, values, audience, narrative, and AI content generation rules.

These are authoritative. Do not invent styles, colors, or copy that contradict them.

## Design Tokens

```css
/* Colors */
--color-rose: #D7CCD0;
--color-blue-primary: #2051C6;
--color-blue-deep: #004DBA;
--color-yellow: #EBDB8E;
--color-cream: #F4F2E7;        /* use instead of #FFFFFF */
--color-charcoal: #3B3B3B;     /* use instead of #000000 */
--color-olive: #A3A081;

/* Typography */
--font-display: "Almonde", cursive;       /* display/headlines only — never long text */
--font-mono: "Space Mono", monospace;     /* labels, tags, captions — UPPERCASE + tracking */
--font-body: "Satoshi", "Inter", system-ui, sans-serif;

/* Spacing (base 4px) */
--space-1: 4px; --space-2: 8px; --space-3: 16px; --space-4: 24px;
--space-5: 32px; --space-6: 48px; --space-7: 64px; --space-8: 96px; --space-9: 128px;

/* Radius */
--radius-sm: 4px; --radius-md: 8px; --radius-lg: 16px; --radius-full: 9999px;

/* Elevation */
--shadow-soft: 0 2px 8px rgba(59, 59, 59, 0.08);
--shadow-medium: 0 4px 16px rgba(59, 59, 59, 0.12);
```

## Critical Design Rules

- **Never use `#FFFFFF` or `#000000`** — use `--color-cream` and `--color-charcoal` instead.
- **Never combine more than 3 palette colors** in a single component or section.
- **No gradients, no heavy shadows, no saturated drop shadows.**
- Canonical color pairings: Azul + Crema, Rosa + Carbón, Azul + Rosa, Crema + Carbón.
- Grid: 12 columns, 24px gutter, max-width 1280px, 24px side margins on mobile / 64px on desktop.
- Buttons: primary = `--color-blue-primary` bg + `--color-cream` text + `--radius-md` + `padding: 12px 24px`. Hover: `--color-blue-deep`.

## Brand Voice (for any copy or UI text)

Write as Honesto would: **clear, warm, direct, unpretentious**. In practice:

- Short sentences. Product and process first.
- No superlatives, no urgency ("última oportunidad"), no epic framing.
- No emojis in UI or institutional copy.
- Cordobese naturalness — human, never performative.

**Use:** `bien hecho` · `sin vueltas` · `real` · `masa madre real` · `oficio` · `lo justo`  
**Avoid:** `experiencia sublime` · `épico` · `premium` · `exclusivo` · `irresistible`
