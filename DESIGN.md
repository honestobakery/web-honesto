# DESIGN.md — Honesto

> Sistema de diseño de Honesto · Bakery & Cafe / Comida Fresca.
> Este documento define los lineamientos visuales, tipográficos, cromáticos y de tono que cualquier agente (humano o IA) debe respetar para generar interfaces, piezas y comunicaciones coherentes con la marca.

---

## 1. Brand Overview

**Nombre:** honesto
**Categoría:** Bakery & Café / Comida Fresca
**Posicionamiento:** *Lo esencial puede ser extraordinario.*
**Diferencial:** Mientras otros compiten por impresionar, Honesto compite por hacer bien lo esencial.

### Contexto cultural
La gastronomía se volvió performática: más relato, más estética, más concepto. El consumidor quiere calidad, pero está cansado de la pose. Honesto responde a esa tensión —*performance estética vs. autenticidad real, discurso inflado vs. oficio visible*— poniendo el producto y al servicio en el centro: producción propia, masa madre real, café bien calibrado, procesos a la vista. Sin espectáculo innecesario.

### Propuesta de valor
Coherencia absoluta entre lo que se dice y lo que se sirve. Producto real. Experiencia simple. Bien hecha.

### Rol de marca
Convertirse en referencia local de calidad real. Demostrar que la verdadera sofisticación es la coherencia.

### Valores de marca

| Valor | Qué significa en la práctica |
| --- | --- |
| **Coherencia** | Lo que decimos es lo que servimos. Precios, carta, comunicación y servicio responden al mismo criterio. |
| **Maestría artesanal** | El saber hacer: tiempo de fermentación, punto exacto del café, el detalle que no se negocia. |
| **Transparencia** | No ocultamos procesos. Mostramos cómo trabajamos porque confiamos en lo que hacemos. |
| **Cercanía** | Cerca sin invadir. Lenguaje simple, trato humano, espacio cómodo para quedarse o pasar. |

### Audiencia principal

- **Oficinistas (70%):** pausas rápidas, desayuno, almuerzo liviano, reuniones informales. Buscan calidad, rapidez y constancia.
- **Estudiantes (20%):** usan el espacio para estudiar o como punto de encuentro. Buscan comodidad y ambiente sin pretensión.
- **Trámites / turistas (10%):** descubren el local, buscan algo representativo y bien hecho con identidad local.

---

## 2. Brand Principles

Estos principios son innegociables y aplican a cualquier decisión de diseño.

- **Producto real por sobre artificio visual.** El pan, el café y la comida son la estrella. Todo lo demás acompaña.
- **Fotografía honesta, cálida y cotidiana.** No posada, no estilizada en exceso.
- **Espacios visuales limpios y respirables.** El silencio gráfico también comunica.
- **Recursos gráficos usados con intención, no como decoración.** Cada elemento tiene un porqué.
- **Coherencia estética antes que variedad excesiva.** Pocas piezas, bien resueltas.

**Honesto no es:** solemne · pretenciosa · moda pasajera · concepto inflado · sofisticación impostada · espectáculo gastronómico · tendencia vacía · urgencia artificial · relato más grande que el producto.

**Reglas de oro:**
1. La identidad no vive en adornos: vive en cómo se ve el producto, cómo se muestra el oficio y cómo se transmite la experiencia.
2. Los recursos secundarios *acompañan*. Nunca *reemplazan* a los activos principales (logo, isotipo, fotografía).
3. Si una pieza necesita explicarse, sobra algo.

---

## 3. Color System

La paleta es deliberadamente acotada: 7 colores que conviven en armonía cálida y honesta. Ninguno es decorativo; cada uno tiene un rol.

### Paleta principal

| Token | HEX | RGB | Rol |
|---|---|---|---|
| `--color-rose` | `#D7CCD0` | 215, 204, 208 | Fondo cálido / piezas suaves / superficies "humanas" |
| `--color-blue-primary` | `#2051C6` | 32, 81, 198 | Color signature de marca / fondos plenos / fuerza visual |
| `--color-blue-deep` | `#004DBA` | 0, 77, 186 | Variante intensa del azul / contraste sobre claros |
| `--color-yellow` | `#EBDB8E` | 235, 219, 142 | Calidez / acento / categoría secundaria |
| `--color-cream` | `#F4F2E7` | 244, 242, 231 | Fondo base claro / "papel" / sustituto del blanco puro |
| `--color-charcoal` | `#3B3B3B` | 59, 59, 59 | Texto principal / logos sobre fondos claros |
| `--color-olive` | `#A3A081` | 163, 160, 129 | Tono terroso / detalles |

### Reglas de uso del color

- **Azul (`#2051C6` / `#004DBA`)** es el color signature. Aparece como fondo pleno en piezas hero, perfiles sociales, packaging. Genera contraste y autoridad.
- **Rosa (`#D7CCD0`)** balancea al azul. Es el lado cálido, doméstico, cotidiano. Se usa para fondos de menús, coasters, contenido editorial.
- **Crema (`#F4F2E7`)** sustituye al blanco puro. Nunca uses `#FFFFFF` salvo en fotografía o ediciones que lo exijan técnicamente.
- **Carbón (`#3B3B3B`)** es el color del texto y del logo sobre fondos claros. Evita el negro puro `#000000`.
- **Amarillo y oliva** son acentos. No deben dominar nunca una composición.
- **Combinaciones canónicas:** Azul + Crema, Rosa + Carbón, Azul + Rosa (alto contraste con calidez), Crema + Carbón (editorial).
- **Combinaciones a evitar:** Amarillo + Rosa sin un tercer color que los separe; gradientes; sombras saturadas.

### Contraste y accesibilidad

- Texto largo: usar `--color-charcoal` sobre `--color-cream` o `--color-rose`.
- Sobre `--color-blue-primary`, usar `--color-cream` (no blanco puro) para títulos y CTAs.
- Verificar contraste mínimo WCAG AA (4.5:1 para texto regular, 3:1 para texto grande).

---

## 4. Typography

Tres familias tipográficas con roles bien diferenciados. No mezclar fuera de su uso previsto.

### Familias

| Tipografía | Uso | Pesos disponibles |
|---|---|---|
| **Almonde** | Destacados, frases ancla, logotipo | Regular |
| **Space Mono** | Textos info, etiquetas, metadata, números, "voz de máquina" | Regular, Italic, Bold, Bold Italic |
| **Satoshi** | Textos informativos largos, párrafos, UI | Regular, Italic, Bold, Bold Italic |

### Roles tipográficos

- **Almonde (manuscrita):** se reserva para frases con peso de marca —*"lo esencial bien hecho"*, *"ser extraordinario desde lo esencial"*, *"delicioso sin pose"*— y para el logotipo. Nunca usar para bloques largos de texto. Su valor está en la excepción.
- **Space Mono:** transmite oficio, código, ficha técnica. Ideal para etiquetas (`opc azul 1`, `cod color #`, `pie mail`, `BAKERY & CAFE / COMIDA FRESCA`), categorías, micro-copys y datos.
- **Satoshi:** caballo de batalla para textos descriptivos, párrafos editoriales y UI. Limpia, neutra, legible.

### Escala tipográfica sugerida (web)

```
Display (Almonde)        →  clamp(48px, 8vw, 96px) / line-height 1.1
H1 (Satoshi Bold)        →  40px / line-height 1.15
H2 (Satoshi Bold)        →  28px / line-height 1.2
H3 (Satoshi Bold)        →  20px / line-height 1.3
Body (Satoshi Regular)   →  16px / line-height 1.6
Caption (Space Mono)     →  12-13px / line-height 1.4 / letter-spacing 0.05em / UPPERCASE
```

### Reglas de composición

- Almonde no lleva mayúsculas forzadas. Respetar caja natural.
- Space Mono se ve mejor en MAYÚSCULAS con tracking abierto para etiquetas.
- Nunca poner Almonde sobre fotografías cargadas: necesita aire.
- Interlineado generoso. El blanco entre líneas es parte del mensaje.

---

## 5. Logo & Isotype

### Activos principales

1. **Logotipo principal:** "honesto" en Almonde (manuscrita).
2. **Lockup completo:** logotipo + bajada "BAKERY & CAFE / COMIDA FRESCA" en Space Mono, separados por una barra vertical.
3. **Isotipo:** el trazo suelto (squiggle / firma cursiva) que evoca un gesto manuscrito. Se usa para perfiles sociales, favicons, sellos y firmas.

### Versiones cromáticas válidas

- Logotipo en `--color-charcoal` sobre `--color-rose`, `--color-cream`, `--color-yellow`.
- Logotipo en `--color-cream` sobre `--color-blue-primary` o `--color-blue-deep`.
- Isotipo en `--color-rose` sobre `--color-blue-primary` (recurso característico).
- Isotipo en `--color-charcoal` sobre claros.

### Reglas

- **Aire mínimo:** dejar al menos la altura de la "h" del logotipo como respiro alrededor.
- **No deformar, no rotar, no aplicar sombras, no contornear.**
- **Tamaño mínimo legible:** 80px de ancho en digital, 20mm en impreso.
- En usos pequeños (favicon, avatar), usar el isotipo, no el logotipo completo.

---

## 6. Photography

La fotografía es uno de los tres activos centrales de la marca. Define el tono más que el logo.

### Dirección de fotografía

| Eje | Clave visual | Bajada concreta |
|---|---|---|
| Concepto | Real > Genuino | Capturar momentos, no poses. La acción manda. |
| Luz | Natural y viva | Usar luz del espacio. Sombras y contrastes suman verdad. |
| Color | Cálido y honesto | Tonos reales + leve calidez. Nada artificial. |
| Composición | Espontánea | Encuadres imperfectos, cercanos, como "robados". |
| Movimiento | Presente | Incluir blur, manos en acción, flujo constante. |
| Personas | Protagonistas | Equipo real, interacción genuina, cero acting. |
| Producto | En contexto | El pan, café y comida viven en la escena, no aislados. |
| Textura | Sensorial | Harina, masa, corteza. Que casi se sienta. |

### Qué SÍ

- Manos en la masa, dedos enharinados, gestos del oficio.
- Equipo real riendo, trabajando, conviviendo.
- Producto en plena acción (saliendo del horno, siendo cortado, servido en barra).
- Blur de movimiento intencional.
- Blanco y negro para escenas de oficio íntimo.
- Color cálido para escenas de comunidad y producto.

### Qué NO

- Bodegones estilizados tipo "Instagram food porn".
- Personas posando frente a cámara con sonrisa de catálogo.
- Iluminación de estudio plana, sin textura.
- Filtros saturados, HDR, presets agresivos.
- Composiciones simétricas perfectas.
- Producto aislado sobre fondo blanco (salvo en piezas técnicas explícitas).

---

## 7. Graphic Resources

### Recursos primarios
Logo, isotipo y fotografía. Siempre dominan la composición.

### Recursos secundarios

- **Ilustraciones de personajes:** figuras humanas en línea suelta, sketchy, en acciones cotidianas (cargando pan, llevando bandejas, brindando, caminando con baguettes). Estilo naïf, trazo imperfecto, en `--color-charcoal` sobre fondos claros o en `--color-rose` sobre fondos azules.
- **Trazo / squiggle:** la firma cursiva que también funciona como isotipo. Sirve como separador, sello, detalle de cierre. Usar con moderación.
- **Texturas:** la propia textura del producto (miga, corteza, harina) actúa como textura visual sin necesidad de overlays artificiales.

### Reglas

- Los recursos secundarios **enriquecen**, no protagonizan.
- Una sola ilustración por pieza, salvo en composiciones tipo "grilla de personajes".
- No combinar más de 2 recursos secundarios distintos en una misma pieza.
- Nunca usar los personajes en piezas donde el producto real ya cuenta la historia.

---

## 8. Layout & Spacing

### Principios

- **Aire abundante.** El espacio en blanco (o crema) es parte de la identidad.
- **Asimetría tranquila.** Composiciones que respiran, sin centrados forzados.
- **Una idea por pieza.** Si una pieza compite con sí misma, dividirla en dos.

### Sistema de espaciado (base 4px)

```
--space-1:  4px
--space-2:  8px
--space-3:  16px
--space-4:  24px
--space-5:  32px
--space-6:  48px
--space-7:  64px
--space-8:  96px
--space-9:  128px
```

### Grilla

- Web: 12 columnas, gutter 24px, max-width 1280px, márgenes laterales mínimos de 24px (mobile) / 64px (desktop).
- Piezas sociales: respetar safe zones de cada plataforma. Logo nunca al borde.

### Radios

```
--radius-sm: 4px    /* inputs, etiquetas */
--radius-md: 8px    /* cards, botones */
--radius-lg: 16px   /* contenedores grandes */
--radius-full: 9999px /* píldoras, avatares */
```

Honesto tiende a formas rectas o ligeramente redondeadas. Evitar radios exagerados que infantilicen.

---

## 9. UI Components

### Botones

- **Primario:** fondo `--color-blue-primary`, texto `--color-cream`, Satoshi Bold, `--radius-md`, padding `12px 24px`.
- **Secundario:** fondo transparente, borde 1px `--color-charcoal`, texto `--color-charcoal`.
- **Terciario / link:** sin fondo, texto `--color-blue-primary`, subrayado en hover.
- **Estado hover:** oscurecer fondo 8% o usar `--color-blue-deep`.
- **Estado disabled:** opacidad 0.4, cursor `not-allowed`.

### Inputs

- Fondo `--color-cream`, borde 1px `--color-olive` al 40%, texto `--color-charcoal`, Satoshi Regular.
- Focus: borde `--color-blue-primary`, sin sombra.
- Label en Space Mono uppercase, 12px, encima del input.

### Cards

- Fondo `--color-cream` o `--color-rose`.
- Sin sombras pesadas. Si se necesita elevación: `0 2px 8px rgba(59,59,59,0.08)`.
- Padding interno mínimo `--space-5` (32px).

### Tags / Etiquetas

- Space Mono UPPERCASE, 11-12px, tracking 0.08em.
- Fondo `--color-charcoal` con texto `--color-cream`, o el inverso.

### Iconografía

- Estilo line, trazo 1.5px, esquinas suaves pero no infantiles.
- Compatible con el trazo de las ilustraciones secundarias.
- Tamaños: 16, 20, 24, 32 px.

---

## 10. Voice & Tone

### Voz

Honesta, cercana, sin solemnidad. Habla de oficio sin alardear. Reconoce el valor de lo simple. No vende: cuenta.

### Tono según contexto

- **Producto / menú:** descriptivo, sensorial, breve. *"Pan de masa madre. Fermentación de 24 horas."*
- **Comunicación de marca:** declarativo, con frases ancla. *"Lo esencial bien hecho."* / *"Delicioso sin pose."*
- **Redes sociales:** conversacional, cálido, con humor seco. Nunca cringe.
- **UI / sistema:** claro, funcional, en Satoshi. Sin emojis decorativos.

### Frases ancla canónicas

- *Lo esencial puede ser extraordinario.*
- *Ser extraordinario desde lo esencial.*
- *Lo esencial bien hecho.*
- *Delicioso sin pose.*
- *Elegí sabores reales.*

### Cómo debe sonar

Directa · Cálida · Segura · Cotidiana · Humana · Sin tecnicismos innecesarios · Sin épica exagerada · Con humor sutil cuando corresponde · Con identidad cordobesa natural, no forzada.

### Cómo no debe sonar

Grandilocuente · Pretenciosa · Fría · Académica · Excesivamente técnica · Urgente sin motivo · Demasiado "marketinera" · Como si estuviera actuando sofisticación.

### Palabras y expresiones recomendadas

`bien hecho` · `sin vueltas` · `real` · `de todos los días` · `masa madre real` · `café bien preparado` · `proceso` · `oficio` · `cerca` · `claro` · `fresco` · `a mano` · `lo justo` · `hasta mañana` · `como debería ser` · `sin explicación` · `menos show, más producto`

### Palabras y expresiones a evitar

`experiencia sublime` · `universo sensorial` · `ritual mágico` · `manifiesto gastronómico` · `obra maestra artesanal` · `premium experience` · `exclusivo` · `épico` · `irresistible de otro planeta` · `la revolución del café` · `el pan que cambiará tu vida` · `imperdible` · `última oportunidad` · `solo para entendidos`

### Qué evitar

- Superlativos vacíos ("el mejor", "increíble", "único").
- Tecnicismos gastronómicos innecesarios.
- Tono publicitario de los 2000s.
- Emojis en comunicación institucional.
- Mayúsculas para gritar.

---

## 11. Application Examples

Casos de aplicación que ejemplifican el sistema:

- **Packaging / bolsa takeaway:** fondo crema o rosa, logotipo grande, isotipo como sello pequeño.
- **Menú QR:** fondo crema o azul, frase ancla en Almonde, QR centrado, isotipo al pie.
- **Posavasos:** fondo rosa, logotipo + bajada centrados, sutil textura de pan al fondo.
- **Delantal / uniforme:** azul marino con logotipo bordado en crema, isotipo en el bolsillo.
- **Instagram grid:** alternancia entre fotografías de producto/oficio y bloques de color plano (rosa, azul, amarillo) con el logotipo y la bajada.
- **Firma de mail:** fondo rosa, logotipo a la izquierda, datos en Space Mono, isotipo decorativo a la derecha.

---

## 12. Don'ts (resumen rápido)

- No usar `#FFFFFF` puro ni `#000000` puro.
- No mezclar Almonde con texto largo.
- No saturar las composiciones: priorizar respiración.
- No usar fotografía posada o de stock.
- No deformar el logotipo ni cambiarle el color fuera de la paleta.
- No combinar más de 3 colores de la paleta en una sola pieza.
- No usar sombras dramáticas, gradientes ni efectos brillantes.
- No usar emojis decorativos en comunicación institucional.
- No abusar de los recursos secundarios: ellos acompañan, no protagonizan.

---

## 13. Intenciones de comunicación

Toda pieza —visual o textual— debe tener una intención clara entre estas cuatro:

| Intención | Qué se busca | Ejemplo de tono |
| --- | --- | --- |
| **Normalizar la calidad real** | Comunicar que buen pan y buen café deberían ser lo normal, no la excepción. | *"Así debería ser siempre."* |
| **Educar sin pontificar** | Ayudar a entender lo que se consume, sin tecnicismos ni superioridad. | *"La masa madre lleva tiempo. Por eso se nota."* |
| **Construir confianza sostenida** | Transmitir estabilidad, coherencia y cumplimiento. Fidelidad > impacto. | *"Igual de bien, todos los días."* |
| **Defender la coherencia** | Tomar postura frente a la sobreactuación gastronómica: menos show, más producto. | *"Sin vueltas. Bien hecho."* |

---

## 14. Reglas para contenido IA

Este documento es guía para agentes IA. Cuando una IA cree contenido para Honesto debe aplicar estas reglas sin excepción.

### La IA debe

- Hablar simple y claro. Priorizar producto, proceso y experiencia real.
- Usar frases cortas cuando el canal lo permita.
- Transmitir calma, confianza y oficio.
- Mostrar calidad sin exagerarla.
- Usar humor sutil y natural cuando corresponda.
- Mantener identidad cordobesa sin caer en caricatura.
- Hacer que la marca suene segura, no desesperada por vender.
- Recordar que Honesto busca repetición y hábito, no impacto vacío.

### La IA no debe

- Usar lenguaje grandilocuente o excesivamente poético.
- Convertir cada producto en una experiencia épica.
- Sonar como una marca de lujo aspiracional.
- Usar urgencia artificial: *"última oportunidad"*, *"corré"*, *"no te lo pierdas"*.
- Sobreactuar cercanía o usar tecnicismos sin necesidad.
- Pontificar sobre café o pan.
- Prometer más de lo que se sirve.
- Escribir textos largos cuando una frase simple alcanza.

### Regla síntesis

**Decir menos, sostener más. Mostrar lo real. Hacer que el producto hable.**

---

## 15. Design Tokens (resumen para implementación)

```css
:root {
  /* Color */
  --color-rose: #D7CCD0;
  --color-blue-primary: #2051C6;
  --color-blue-deep: #004DBA;
  --color-yellow: #EBDB8E;
  --color-cream: #F4F2E7;
  --color-charcoal: #3B3B3B;
  --color-olive: #A3A081;

  /* Typography */
  --font-display: "Almonde", cursive;
  --font-mono: "Space Mono", monospace;
  --font-body: "Satoshi", "Inter", system-ui, sans-serif;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --space-6: 48px;
  --space-7: 64px;
  --space-8: 96px;
  --space-9: 128px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  /* Elevation */
  --shadow-soft: 0 2px 8px rgba(59, 59, 59, 0.08);
  --shadow-medium: 0 4px 16px rgba(59, 59, 59, 0.12);
}
```

---

*Última actualización: 2026-05-16. Fuente: Honesto Brandbook (Lola Vidal · Agilidad Estratégica & Dir. Creativa).*
