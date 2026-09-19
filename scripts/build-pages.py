#!/usr/bin/env python3
"""Genera las páginas de contenido (/masa-madre, /cafe-especialidad, /laminados, /centro-cordoba).

Uso: python3 scripts/build-pages.py
Cada página vive en <slug>/index.html y usa rutas absolutas (/css, /assets). El contenido está en
PAGES más abajo: editá ahí y volvé a correr. Reglas: hechos confirmados por el dueño o conocimiento
general; nada inventado sobre horarios de horneada, orígenes de café ni historia del local.
"""
import json, os, re

ROOT = os.path.join(os.path.dirname(__file__), '..')
SITE = 'https://honesto.com.ar'
TEL = '+543516016091'; TEL_SHOW = '+54 351 601-6091'
WA = 'https://wa.me/543516016091'
FUDO = 'https://menu.fu.do/independencia180/qr-menu'
DATE = '2026-09-19'
HOURS = 'Lun–Vie 8:00–21:00 · Sáb 9:00–15:00 · Dom cerrado'

def img(slot, alt, sizes, w=800, h=600, eager=False):
    base = f'/assets/images/{slot}'
    srcset = ', '.join(f'{base}-{x}.webp {x}w' for x in (480, 800, 1200, 1600))
    extra = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{base}-{1200 if eager else 800}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'alt="{alt}" width="{1200 if eager else w}" height="{900 if eager else h}" {extra}>')

HERO_SIZES = '(min-width: 1024px) 480px, calc(100vw - 48px)'
BODY_SIZES = '(min-width: 1024px) 736px, calc(100vw - 48px)'

def header(active):
    return f'''<!-- HEADER -->
<header class="lp-header">
  <div class="topbar">
    <p>Bakery &amp; Café / Comida Fresca — Centro, Córdoba</p>
  </div>
  <nav class="mainnav" aria-label="Navegación principal">
    <div class="mainnav__links">
      <a href="/">Inicio</a>
      <a href="/#nosotros">Nosotros</a>
    </div>
    <a class="mainnav__brand" href="/">honesto</a>
    <div class="mainnav__links">
      <a href="/#carta">Carta</a>
      <a href="/#preguntas">Preguntas</a>
      <a class="mainnav__cta" href="/bakery.html">Bakery B2B</a>
    </div>
    <button class="mainnav__toggle" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-menu">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M4 5h16"/><path d="M4 12h16"/><path d="M4 19h16"/>
      </svg>
    </button>
  </nav>
  <nav class="mobile-menu" id="mobile-menu" aria-label="Menú móvil">
    <a href="/">Inicio</a>
    <a href="/#nosotros">Nosotros</a>
    <a href="/#carta">Carta</a>
    <a href="/#preguntas">Preguntas</a>
    <a href="/bakery.html">Bakery B2B</a>
    <p class="mobile-menu__group">Más</p>
    <a href="/masa-madre/"{' aria-current="page"' if active=='masa-madre' else ''}>Masa madre</a>
    <a href="/cafe-especialidad/"{' aria-current="page"' if active=='cafe-especialidad' else ''}>Café de especialidad</a>
    <a href="/laminados/"{' aria-current="page"' if active=='laminados' else ''}>Laminados</a>
    <a href="/centro-cordoba/"{' aria-current="page"' if active=='centro-cordoba' else ''}>Centro de Córdoba</a>
  </nav>
</header>
'''

FOOTER = f'''<!-- FOOTER -->
<footer class="footer-v2" id="contacto">
  <div class="footer-v2__inner">
    <div class="footer-v2__grid">
      <div>
        <a class="footer-v2__brand" href="/">honesto</a>
        <p class="footer-v2__tagline">Bakery &amp; Café / Comida Fresca</p>
        <p class="footer-v2__desc">Lo esencial puede ser extraordinario.</p>
        <ul class="footer-v2__links" aria-label="Más sobre honesto">
          <li><a href="/masa-madre/">Masa madre</a></li>
          <li><a href="/cafe-especialidad/">Café de especialidad</a></li>
          <li><a href="/laminados/">Laminados</a></li>
          <li><a href="/centro-cordoba/">Centro de Córdoba</a></li>
          <li><a href="/bakery.html">Bakery B2B</a></li>
        </ul>
      </div>
      <div class="footer-v2__col">
        <h3>Ubicación</h3>
        <div class="footer-v2__location">
          <svg class="footer-v2__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/>
            <circle cx="12" cy="10" r="3"/>
          </svg>
          <address>
            <p>Independencia 180, Centro</p>
            <p class="footer-v2__col-sub">Córdoba, Argentina</p>
          </address>
        </div>
      </div>
      <div class="footer-v2__col">
        <h3>Horarios</h3>
        <div class="footer-v2__location">
          <svg class="footer-v2__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M12 6v6l4 2"/>
            <circle cx="12" cy="12" r="10"/>
          </svg>
          <div class="footer-v2__hours">
            <p>Lun - Vie: <time datetime="08:00">8:00</time> - <time datetime="21:00">21:00</time></p>
            <p>Sáb: <time datetime="09:00">9:00</time> - <time datetime="15:00">15:00</time></p>
            <p class="muted">Dom: Cerrado</p>
          </div>
        </div>
      </div>
      <div class="footer-v2__col">
        <h3>Contacto</h3>
        <div class="footer-v2__contact">
          <a href="tel:{TEL}">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"/>
            </svg>
            {TEL_SHOW}
          </a>
          <a href="mailto:hola@honesto.com.ar">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/>
              <rect x="2" y="4" width="20" height="16" rx="2"/>
            </svg>
            hola@honesto.com.ar
          </a>
          <a href="https://instagram.com/honesto.bakery" target="_blank" rel="noopener noreferrer">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <rect width="20" height="20" x="2" y="2" rx="5" ry="5"/>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/>
              <line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/>
            </svg>
            @honesto.bakery
          </a>
        </div>
      </div>
    </div>
    <div class="footer-v2__bottom">
      <p class="footer-v2__copy">© 2026 honesto. Todos los derechos reservados.</p>
      <span class="footer-v2__sign">hasta mañana.</span>
    </div>
  </div>
</footer>

<script>
  const toggle = document.querySelector('.mainnav__toggle');
  const menu = document.getElementById('mobile-menu');
  toggle.addEventListener('click', () => {{
    const open = menu.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
    if (open) menu.querySelector('a').focus();
  }});
  menu.querySelectorAll('a').forEach(a => {{
    a.addEventListener('click', () => {{
      menu.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus();
    }});
  }});
</script>

</body>
</html>
'''

# ─────────────────────────────────────────────────────────────────────────────
# CONTENIDO
# ─────────────────────────────────────────────────────────────────────────────
PAGES = {
 'masa-madre': dict(
  title='Pan de masa madre en Córdoba: qué es, por qué 24 horas y cómo conservarlo | honesto',
  description='Qué es la masa madre, por qué nuestra hogaza fermenta 24 horas, con qué harinas la hacemos y cómo conservarla. honesto, panadería de masa madre en el centro de Córdoba.',
  headline='Pan de masa madre en Córdoba: qué es, por qué 24 horas y cómo conservarlo',
  keywords='pan de masa madre Córdoba, hogaza de masa madre, qué es la masa madre, fermentación 24 horas, pan sin levadura comercial, panadería masa madre centro Córdoba, cómo conservar pan de masa madre, pan de centeno Córdoba',
  eyebrow='Masa madre', crumb='Masa madre',
  h1='Pan de masa madre real. <em>Qué es y por qué se nota.</em>',
  lead='Nuestra hogaza fermenta 24 horas sin levadura comercial, con harinas de trigo, integral y centeno, y se hornea todos los días en Independencia 180. Acá contamos qué es la masa madre, por qué lleva tanto tiempo y cómo cuidar el pan en casa.',
  hero_img=('fermentacion','Bollos de masa fermentando en la placa, en la cocina de honesto'),
  hero_class='',
  resumen_title='¿Qué es el pan de masa madre de honesto?',
  resumen='Es pan hecho solo con harina, agua, sal y masa madre: un cultivo natural de levaduras y bacterias que fermenta la masa sin levadura comercial. Nuestra hogaza usa harinas de trigo, integral y centeno, fermenta 24 horas y se hornea todos los días en el centro de Córdoba. Pesa alrededor de 1 kg.',
  facts=[('Sale del horno','Desde las 8:00, todos los días'),('Fermentación','24 horas, natural, sin levadura comercial'),('Harinas','Trigo, integral y centeno (hogaza); trigo e integral (moldes)'),('Panes','Hogaza 1 kg · pan de molde blanco y semillado 1 kg · baguetín 400 g'),('Dónde','Independencia 180, Centro, Córdoba · '+HOURS)],
  sections=[
   ('¿Qué es la masa madre?', '''<p>La masa madre es un cultivo vivo de harina y agua. Con el tiempo, las levaduras y bacterias que están en la harina y en el aire se establecen en ese cultivo y lo hacen fermentar solo. Una parte de esa masa madre se mezcla con la masa del pan y hace el trabajo que en la panadería industrial hace la levadura comercial: levar. La diferencia es que lo hace despacio y, mientras, transforma la masa.</p>
<p>Esa transformación es lo que se siente en el pan: corteza más firme y crocante, miga con alvéolos irregulares, sabor con un fondo apenas ácido y una duración mayor sin conservantes. No es un estilo ni una etiqueta. Es un proceso, y se nota.</p>'''),
   ('¿Por qué fermentamos 24 horas?', '''<p>Porque el tiempo hace lo que ningún ingrediente puede hacer. En una fermentación larga las bacterias producen ácidos que dan sabor y ayudan a que el pan se conserve; las enzimas de la harina descomponen parte de los almidones y proteínas, lo que hace la miga más digerible y el sabor más profundo; y el gluten se desarrolla sin amasados agresivos.</p>
<p>Un pan con levadura comercial puede estar listo en dos o tres horas. El nuestro necesita un día entero entre el amasado, la fermentación en bloque, el formado y el reposo final en frío antes de entrar al horno. Por eso decimos que la masa madre lleva tiempo. Es literal.</p>'''),
   ('¿Qué harinas usamos?', '''<p>Para la <strong>hogaza</strong> mezclamos harina de trigo, harina integral y centeno. El trigo da estructura, la integral aporta sabor y fibra, y el centeno suma humedad y ese fondo rústico que caracteriza a la hogaza. Los <strong>panes de molde</strong> llevan trigo e integral; el semillado se cubre además con un mix de semillas y avena. El <strong>baguetín</strong> es el mismo proceso en un formato individual de 400 g.</p>
<p>No usamos mejoradores, premezclas ni levadura comercial en ninguno de los panes. Harina, agua, sal y masa madre.</p>'''),
   ('¿Qué panes de masa madre hacemos?', '''<ul>
<li><strong>Hogaza de masa madre.</strong> Trigo, integral y centeno. Corteza crocante, miga aireada, sabor profundo. Alrededor de 1 kg. Es nuestro producto principal.</li>
<li><strong>Pan de molde blanco.</strong> Trigo e integral, miga suave y esponjosa, corteza fina. Alrededor de 1 kg. Para tostadas y sándwiches.</li>
<li><strong>Pan de molde semillado.</strong> Igual que el blanco, cubierto con semillas y avena. Alrededor de 1 kg.</li>
<li><strong>Baguetín.</strong> Corteza crocante y miga tierna, unos 400 g. Formato individual.</li>
</ul>
<p>Los cuatro se hacen en nuestra cocina de Independencia 180. También los vendemos al por mayor a cafeterías y restaurantes a través de <a href="/bakery.html">honesto bakery</a>.</p>'''),
   ('¿A qué hora sale el pan del horno?', '''<p><strong>A las 8 de la mañana, cuando abrimos, el pan ya está en el mostrador.</strong> Las hogazas y los panes de molde se hornean temprano, todos los días, y se venden hasta que se terminan. Si querés asegurarte una hogaza o necesitás varias para tu negocio, escribinos por <a href="%s?text=Hola%%2C%%20quiero%%20reservar%%20pan%%20de%%20masa%%20madre." target="_blank" rel="noopener noreferrer">WhatsApp</a> y te la reservamos.</p>''' % WA),
   ('¿Cómo conservar el pan de masa madre?', '''<p>El pan de masa madre dura más que el pan común, pero hay que guardarlo bien:</p>
<ul>
<li><strong>Los primeros dos o tres días</strong>, a temperatura ambiente, en una bolsa de papel o envuelto en un paño de algodón, con el corte hacia abajo sobre la tabla. Así la corteza sigue crocante y la miga no se reseca.</li>
<li><strong>Evitá la heladera.</strong> El frío acelera el envejecimiento del pan y lo endurece.</li>
<li><strong>Para más tiempo, congelalo.</strong> Cortalo en rebanadas, guardalo en una bolsa cerrada y sacá lo que vayas a usar. Va directo a la tostadora o al horno.</li>
<li><strong>Para revivirlo</strong>, humedecé apenas la corteza y dale 8 a 10 minutos de horno a 180 °C. Vuelve a crujir.</li>
</ul>'''),
   ('¿En qué se diferencia del pan común?', '''<p>El pan industrial se leva con levadura comercial en pocas horas y suele llevar aditivos para acelerar el proceso y prolongar la vida útil. El pan de masa madre se leva con un cultivo natural durante un día entero, sin aditivos. El resultado es otro pan: más sabor, mejor corteza, miga más húmeda y una acidez suave que muchos describen como "más liviano". No hace falta saber de pan para notar la diferencia. Se nota al cortarlo.</p>'''),
  ],
  figure=('cocina','Cocina de honesto en Independencia 180: el equipo trabajando entre mesadas y hornos','La cocina y el horno están a la vista. El proceso no se esconde.'),
  faq=[
   ('¿Dónde comprar pan de masa madre en el centro de Córdoba?','En honesto, Independencia 180, a 200 metros de la Plaza San Martín. Horneamos hogazas, panes de molde y baguetines de masa madre todos los días. Abrimos de lunes a viernes de 8:00 a 21:00 y los sábados de 9:00 a 15:00.'),
   ('¿A qué hora sale el pan?','A las 8 de la mañana, en la apertura, el pan del día ya está en el mostrador. Se vende hasta que se termina; se puede reservar por WhatsApp.'),
   ('¿El pan de honesto lleva levadura?','No lleva levadura comercial. Se leva únicamente con masa madre, un cultivo natural de harina y agua, durante 24 horas.'),
   ('¿Cuánto dura el pan de masa madre?','Bien guardado, dos o tres días a temperatura ambiente con la corteza crocante, y más tiempo congelado en rebanadas. No lo guardes en la heladera.'),
   ('¿La hogaza es integral?','Es una mezcla: harina de trigo, harina integral y centeno. No es 100% integral, pero tiene el sabor y la fibra de la integral y del centeno.'),
   ('¿Hacen pan sin gluten?','No. Todos nuestros panes son de trigo, integral y centeno, y se elaboran en el mismo obrador. La única pieza con receta sin gluten es una cookie de avena y naranja, con posible contaminación cruzada.'),
   ('¿Venden pan de masa madre al por mayor?','Sí. honesto bakery abastece a cafeterías, restaurantes y tiendas de Córdoba con hogazas, panes de molde y baguetines, además de laminados y congelados. Los pedidos se coordinan por WhatsApp al +54 351 601-6091.'),
  ],
  aside_links=[('/laminados/','Laminados de masa madre y manteca'),('/cafe-especialidad/','Café de especialidad para acompañar'),('/bakery.html','Pan de masa madre al por mayor'),(FUDO,'Carta y precios del obrador')],
  cta=('elegí pan de verdad.','Hogaza de masa madre, horneada hoy en Independencia 180. Pasá a buscarla o reservala por WhatsApp.'),
 ),

 'cafe-especialidad': dict(
  title='Café de especialidad en el centro de Córdoba: qué es y cómo lo preparamos | honesto',
  description='Qué es el café de especialidad, qué significa calibrarlo todos los días y qué servimos en honesto, Independencia 180, centro de Córdoba: café de la casa, tolva invitada de tostadores locales y leches vegetales.',
  headline='Café de especialidad en el centro de Córdoba: qué es y cómo lo preparamos',
  keywords='café de especialidad Córdoba centro, cafetería de especialidad Córdoba, café calibrado, tostadores de café Córdoba, Chiquitito café, Ínfimo tostamos café, tolva invitada, espresso Córdoba centro, dónde tomar café de especialidad en Córdoba, cafetería para trabajar Córdoba centro, café y medialunas Córdoba',
  eyebrow='Café de especialidad', crumb='Café de especialidad',
  h1='Café de especialidad, <em>calibrado todos los días.</em>',
  lead='No hace falta saber de café para notar la diferencia. Acá explicamos qué es el café de especialidad, qué hacemos cada mañana antes de servir la primera taza y por qué el centro de Córdoba es un buen lugar para tomarlo despacio.',
  hero_img=('cafe-alfajor','Café de especialidad en vaso de vidrio junto a un alfajor, en una mesa de honesto'),
  hero_class='page-hero--blue',
  resumen_title='¿Qué es el café de especialidad de honesto?',
  resumen='Es café de especialidad, es decir, de granos seleccionados y trazables, que calibramos todos los días: ajustamos molienda, dosis, tiempo y temperatura cada mañana para que salga igual de bien en cada taza. Además del café de la casa, siempre hay una tolva invitada con un tostador local de Córdoba. Servimos espresso, café con leche (también con leches vegetales) y café negro, en Independencia 180, con medialunas y laminados recién horneados.',
  facts=[('Qué','Café de especialidad de la casa + tolva invitada de tostadores locales (Chiquitito, Ínfimo y otros)'),('Cómo','Espresso, café con leche (también leches vegetales) y café negro'),('Con qué','Medialunas, croissants, alfajores y pastelería propia'),('Dónde','Independencia 180, Centro, Córdoba · '+HOURS)],
  sections=[
   ('¿Qué es el café de especialidad?', '''<p>"Café de especialidad" es un término técnico. Se refiere a cafés que obtienen 80 puntos o más sobre 100 en una evaluación sensorial estandarizada, hecha por catadores certificados. Para llegar ahí, el grano tiene que estar libre de defectos, cultivado y procesado con cuidado, y ser trazable: se sabe de qué finca o cooperativa viene, de qué variedad y cómo se procesó.</p>
<p>Ese cuidado se pierde si el tostado es viejo o si la preparación es descuidada. Por eso en café de especialidad importa tanto lo que pasa en la barra como lo que pasó en origen.</p>'''),
   ('¿Qué significa que calibramos el café todos los días?', '''<p>El café es un producto vivo. Cambia con la humedad del ambiente, con la temperatura del local y con los días que pasan desde el tostado. La misma receta de ayer puede salir distinta hoy. Calibrar es ajustar cada mañana los cuatro parámetros que definen un espresso: la <strong>molienda</strong>, la <strong>dosis</strong> de café, el <strong>tiempo</strong> de extracción y la <strong>temperatura</strong> del agua. Se prueba, se corrige y se vuelve a probar hasta que la taza está donde tiene que estar.</p>
<p>No lo hacemos para contarlo. Lo hacemos porque es la única manera de que el café salga igual de bien un martes a las 8 que un sábado a las 14.</p>'''),
   ('¿Qué café servimos?', '''<p>Trabajamos con dos tolvas. En una está nuestro <strong>café de especialidad de la casa</strong>; en la otra, siempre, una <strong>tolva invitada</strong> que rota entre <strong>tostadores locales</strong> de Córdoba. Así el café de todos los días es el mismo y, a la vez, siempre hay algo nuevo para probar de la escena cordobesa.</p>
<p>Por la tolva invitada pasan tostadores como <a href="https://chiquitito.cafe/" target="_blank" rel="noopener noreferrer">Chiquitito</a>, tostadores de Córdoba que trabajan cafés de origen único de Brasil, Colombia, Bolivia, Honduras, Perú, Etiopía y Uganda, e <a href="https://www.instagram.com/infimo.tostamoscafe/" target="_blank" rel="noopener noreferrer">Ínfimo</a>, también tostadores locales. La tolva cambia; la idea es que siempre haya un café cordobés distinto para probar.</p>
<p>Servimos espresso y sus variantes con leche, y café negro. Hay <strong>leches vegetales</strong> para quien las prefiera. Lo preparamos sin pose: si te gusta más intenso, te lo decimos; si querés algo suave, también. Si querés saber qué tostador está en la tolva invitada esta semana, preguntá en la barra o escribinos por <a href="%s" target="_blank" rel="noopener noreferrer">WhatsApp</a>.</p>''' % WA),
   ('¿Con qué acompañarlo?', '''<p>Con lo que sale del horno. Medialunas de manteca estilo marplatense, croissant, pan de chocolate, roll de canela, danesas, alfajor de chocolate y frutos rojos, budines y cookies. Todo de producción propia, con <a href="/masa-madre/">masa madre</a> y 100% manteca en los <a href="/laminados/">laminados</a>. Al mediodía hay comida fresca para almorzar.</p>'''),
   ('¿Es un buen lugar para trabajar o estudiar?', '''<p>Sí. honesto está en el centro de Córdoba, a 200 metros de la Plaza San Martín, y está pensado para quedarse: mesas cómodas, luz natural, un patio con plantas y horario largo, de 8:00 a 21:00 de lunes a viernes. Vienen oficinistas a la mañana temprano, estudiantes a la tarde y gente que aprovecha un trámite en el centro para tomar un café bien hecho.</p>'''),
  ],
  figure=('mesas','Clientes conversando en las mesas del patio de honesto, con plantas al fondo','El patio, a media mañana. Un lugar para quedarse.'),
  faq=[
   ('¿Dónde tomar café de especialidad en el centro de Córdoba?','En honesto, Independencia 180, a una cuadra de la Catedral y a 200 metros de la Plaza San Martín. Café de especialidad calibrado todos los días, de lunes a viernes de 8:00 a 21:00 y sábados de 9:00 a 15:00.'),
   ('¿Qué diferencia hay entre café de especialidad y café común?','El café de especialidad viene de granos seleccionados, trazables y sin defectos, evaluados con 80 puntos o más sobre 100, tostados recientemente y preparados con parámetros controlados. El café común suele ser una mezcla de granos de menor calidad, tostado muy oscuro para uniformar el sabor.'),
   ('¿Qué es calibrar el café?','Ajustar cada día la molienda, la dosis, el tiempo de extracción y la temperatura del agua, probando hasta que el espresso sale como debe. Se hace porque el café cambia con el clima y con los días desde el tostado.'),
   ('¿Tienen leches vegetales?','Sí. Ofrecemos leches vegetales para el café con leche y sus variantes.'),
   ('¿Qué es la tolva invitada?','Además de nuestro café de especialidad de la casa, siempre hay una segunda tolva con un café de un tostador local de Córdoba, que va rotando. Entre los tostadores que pasan están Chiquitito e Ínfimo. Es una forma de probar lo que se tuesta en la ciudad.'),
   ('¿Se puede trabajar con la notebook?','Sí. Hay mesas cómodas, luz natural y horario corrido de 8:00 a 21:00 de lunes a viernes. Es un lugar pensado para quedarse.'),
  ],
  mentions=[{"@type":"Organization","name":"Chiquitito Café de Especialidad","url":"https://chiquitito.cafe/","sameAs":["https://www.instagram.com/chiquitito.cafe/"],"description":"Tostadores de café de especialidad en Córdoba, Argentina","address":{"@type":"PostalAddress","addressLocality":"Córdoba","addressCountry":"AR"}},
            {"@type":"Organization","name":"Ínfimo · tostamos café","sameAs":["https://www.instagram.com/infimo.tostamoscafe/"],"description":"Tostadores de café en Córdoba, Argentina","address":{"@type":"PostalAddress","addressLocality":"Córdoba","addressCountry":"AR"}}],
  aside_links=[('/laminados/','Medialunas y croissants para acompañar'),('/masa-madre/','Nuestro pan de masa madre'),('/centro-cordoba/','Cómo llegar y qué hay cerca'),('/#carta','La carta')],
  cta=('un café bien hecho, sin vueltas.','Independencia 180, centro de Córdoba. De lunes a viernes de 8 a 21, sábados de 9 a 15.'),
 ),

 'laminados': dict(
  title='Laminados de manteca y masa madre en Córdoba: medialunas, croissants, danesas | honesto',
  description='Medialunas marplatenses, croissants, pan de chocolate, rolls y danesas de masa madre y 100% manteca, horneados todos los días en el centro de Córdoba. Qué es un laminado y cómo conservarlo.',
  headline='Laminados de manteca y masa madre: medialunas, croissants y danesas en Córdoba',
  keywords='medialunas Córdoba centro, croissant Córdoba, laminados de manteca, medialunas de manteca marplatenses, pan de chocolate Córdoba, roll de canela Córdoba, danesas, facturas de masa madre Córdoba, laminados congelados para cafeterías',
  eyebrow='Laminados', crumb='Laminados',
  h1='Laminados de manteca y masa madre. <em>Las de siempre, bien hechas.</em>',
  lead='Medialunas estilo marplatense, croissants, pan de chocolate, rolls de canela, danesas y pepas de membrillo. Todo laminado con masa madre y 100% manteca, y horneado el mismo día en Independencia 180.',
  hero_img=('laminadora','Panadero pasando un bloque de masa con manteca por la laminadora en la cocina de honesto'),
  hero_class='',
  resumen_title='¿Qué son los laminados de honesto?',
  resumen='Son las piezas de masa y manteca en capas que hacemos todos los días: medialunas de manteca estilo marplatense, croissants, pan de chocolate, roll de canela, danesas con pastelera o crumble de manzana y pepa de membrillo. La masa se leva con masa madre y se lamina con manteca, sin margarina. Se venden en el local, en Independencia 180, y al por mayor a cafeterías de Córdoba.',
  facts=[('Salen del horno','Desde las 8:00, todos los días'),('Masa','Masa madre, sin levadura comercial'),('Manteca','100% manteca, sin margarina'),('Piezas','Medialunitas · croissant · pan de chocolate · roll de canela · danesas · pepa de membrillo'),('Dónde','Independencia 180, Centro, Córdoba · '+HOURS)],
  sections=[
   ('¿Qué es un laminado?', '''<p>Un laminado es una masa que se pliega muchas veces sobre una lámina de manteca hasta formar decenas de capas alternadas. En el horno, el agua de la manteca se evapora, separa las capas y las infla: por eso el croissant es liviano y crocante afuera, y tierno y con "panal" adentro. Es una técnica lenta, que necesita frío, precisión y una buena manteca. No admite atajos.</p>'''),
   ('¿Por qué masa madre y 100% manteca?', '''<p>Casi todos los laminados industriales usan margarina, porque es más barata y más fácil de trabajar. Nosotros usamos <strong>solo manteca</strong>: es lo que da el sabor, el color dorado y la textura que se deshace. Y en vez de levadura comercial, la masa se leva con <a href="/masa-madre/">masa madre</a>, lo que suma sabor, mejora la conservación y da una miga menos seca al día siguiente.</p>
<p>El resultado es un laminado que no necesita relleno ni azúcar para ser rico. Se nota en el primer mordisco.</p>'''),
   ('¿Medialuna o croissant?', '''<p>Son parientes, no lo mismo. La <strong>medialuna estilo marplatense</strong> es más chica, más tierna y con brillo, la de todos los días en Argentina. El <strong>croissant</strong> es el laminado francés: más grande, más hojaldrado, con capas abiertas y corteza crocante. Hacemos los dos, con la misma masa madre y la misma manteca, y cada uno tiene su momento: la medialuna va con el café de la mañana; el croissant, con un desayuno más largo.</p>'''),
   ('¿Qué laminados hacemos?', '''<ul>
<li><strong>Medialunitas.</strong> De manteca y masa madre, estilo marplatense: chicas, doradas y con brillo.</li>
<li><strong>Croissant.</strong> Laminado estilo francés, 100% manteca. Hojaldre abierto, exterior crocante.</li>
<li><strong>Pan de chocolate.</strong> Masa hojaldrada rellena de chocolate semiamargo.</li>
<li><strong>Roll de canela.</strong> Masa esponjosa con manteca de canela y azúcar morena, en un formato propio.</li>
<li><strong>Danesa con pastelera.</strong> Laminado con centro de crema pastelera.</li>
<li><strong>Danesa de crumble de manzana.</strong> Masa de croissant rellena de crumble de manzana.</li>
<li><strong>Pepa de membrillo.</strong> La pepa argentina clásica, en masa laminada con dulce de membrillo.</li>
</ul>'''),
   ('¿A qué hora salen los laminados?', '''<p><strong>A las 8, cuando abrimos, ya hay medialunas y croissants recién horneados.</strong> Se hornean temprano, todos los días, y se venden hasta que se terminan. Si querés asegurarte cantidad para una reunión o una hora puntual, avisanos por <a href="%s?text=Hola%%2C%%20quiero%%20reservar%%20laminados." target="_blank" rel="noopener noreferrer">WhatsApp</a> y te los reservamos.</p>''' % WA),
   ('¿Cómo conservarlos y recalentarlos?', '''<p>Los laminados están en su punto el mismo día. Si te sobran:</p>
<ul>
<li>Guardalos en una bolsa de papel a temperatura ambiente, no en la heladera.</li>
<li>Al día siguiente, 3 o 4 minutos en horno a 180 °C recuperan el crocante. Evitá el microondas: los ablanda.</li>
<li>Se pueden congelar ya horneados. Del freezer al horno, unos 6 a 8 minutos.</li>
</ul>'''),
   ('Laminados para cafeterías y restaurantes', '''<p>Los mismos laminados se venden al por mayor a través de <a href="/bakery.html">honesto bakery</a>, horneados o <strong>congelados sin fermentar</strong> en packs de 10 (croissant, pan de chocolate, danesa, roll de canela, medialunita) para descongelar, leudar y hornear en tu negocio. Te pasamos las indicaciones de leudado y horneado.</p>'''),
  ],
  figure=('cortante','Mano cortando discos de masa con un cortante sobre la placa, en la cocina de honesto','Cada pieza se corta y se forma a mano.'),
  faq=[
   ('¿Dónde comprar medialunas de manteca en el centro de Córdoba?','En honesto, Independencia 180, a 200 metros de la Plaza San Martín. Medialunas estilo marplatense de masa madre y 100% manteca, horneadas todos los días. Lunes a viernes de 8:00 a 21:00, sábados de 9:00 a 15:00.'),
   ('¿Los laminados llevan margarina?','No. Se laminan únicamente con manteca.'),
   ('¿Qué diferencia hay entre medialuna y croissant?','La medialuna estilo marplatense es más chica, tierna y con brillo; el croissant es el laminado francés, más grande, más hojaldrado y crocante. Los dos se hacen con masa madre y manteca.'),
   ('¿Puedo comprar laminados congelados para hornear en casa o en mi negocio?','Para negocios, sí: honesto bakery vende croissants, panes de chocolate, danesas, rolls de canela y medialunitas congelados sin fermentar, en packs de 10. Consultá por WhatsApp al +54 351 601-6091.'),
   ('¿Cómo recalentar un croissant?','Tres o cuatro minutos en horno a 180 °C. Nunca en microondas.'),
   ('¿A qué hora salen las medialunas?','A las 8 de la mañana, en la apertura, ya están recién horneadas. Se venden hasta que se terminan.'),
  ],
  aside_links=[('/masa-madre/','Por qué usamos masa madre'),('/cafe-especialidad/','El café que va con las medialunas'),('/bakery.html','Laminados al por mayor y congelados'),(FUDO,'Carta y precios del obrador')],
  cta=('medialunas de las de siempre, bien hechas.','Recién salidas, en Independencia 180. Sin vueltas.'),
 ),

 'centro-cordoba': dict(
  title='honesto en el centro de Córdoba: Independencia 180, a una cuadra de la Catedral',
  description='Dónde está honesto: Independencia 180, en el complejo de Santa Teresa, a 200 metros de la Plaza San Martín. Abierto en 2019 como Le Dureau, honesto desde 2026. Historia del casco histórico y por qué el centro de Córdoba.',
  headline='honesto en el centro de Córdoba: Independencia 180, a una cuadra de la Catedral',
  keywords='Le Dureau Córdoba, ex Le Dureau, cafetería centro Córdoba, panadería centro Córdoba, Independencia 180 Córdoba, complejo Santa Teresa Córdoba, café cerca de Plaza San Martín, desayuno centro histórico Córdoba, café cerca Manzana Jesuítica, café cerca Patio Olmos, casco histórico Córdoba cafetería',
  eyebrow='Centro de Córdoba', crumb='Centro de Córdoba',
  h1='En el centro de Córdoba, <em>donde empezó la ciudad.</em>',
  lead='honesto está en Independencia 180, la calle que baja desde la Plaza San Martín entre el Cabildo, la Catedral y la Manzana Jesuítica. A dos cuadras de todo lo que hace al casco histórico, y a la vuelta de las oficinas, los tribunales y las facultades del centro.',
  hero_img=('cartel','Cartel colgante de honesto en la fachada de Independencia 180, con árboles y cielo de fondo'),
  hero_class='',
  resumen_title='¿Dónde está honesto?',
  resumen='En Independencia 180, Centro, Córdoba, Argentina, en una casona del complejo de Santa Teresa. Es la calle que sale de la esquina sureste de la Plaza San Martín, sobre la que están el Cabildo y la Catedral, una cuadra antes de nuestro local. El local abrió en 2019 como Le Dureau y desde 2026 se llama honesto. La Manzana Jesuítica y el Colegio Monserrat quedan a menos de 200 metros; Patio Olmos, a 330; la Peatonal, a 430. Abrimos de lunes a viernes de 8:00 a 21:00 y los sábados de 9:00 a 15:00.',
  facts=[('Dirección','Independencia 180, Centro, Córdoba (X5000)'),('Referencia','Una cuadra al sur de la Catedral, en el complejo de Santa Teresa'),('Desde','2019 como Le Dureau · honesto desde 2026'),('Horario',HOURS),('Contacto',f'<a href="tel:{TEL}">{TEL_SHOW}</a> · <a href="https://instagram.com/honesto.bakery" target="_blank" rel="noopener noreferrer">@honesto.bakery</a>')],
  sections=[
   ('¿Cómo llegar y qué hay cerca?', '''<p>Desde la Plaza San Martín, tomá Independencia hacia el sur: pasás el Cabildo y la Catedral y en la cuadra siguiente, a la derecha, está honesto. Si venís caminando por la Peatonal, son cinco minutos. Estas son las distancias reales, medidas desde la puerta:</p>
<table class="dist-table">
<tr><td>Iglesia de Santa Teresa y Museo Juan de Tejeda</td><td>mismo complejo</td></tr>
<tr><td>Iglesia de la Compañía de Jesús y Manzana Jesuítica</td><td>170 m</td></tr>
<tr><td>Colegio Nacional de Monserrat</td><td>180 m</td></tr>
<tr><td>Plaza San Martín, Cabildo y Catedral</td><td>200 m</td></tr>
<tr><td>Legislatura histórica (Deán Funes)</td><td>280 m</td></tr>
<tr><td>Teatro del Libertador San Martín</td><td>310 m</td></tr>
<tr><td>Patio Olmos</td><td>330 m</td></tr>
<tr><td>Peatonal 25 de Mayo</td><td>430 m</td></tr>
<tr><td>Municipalidad de Córdoba</td><td>620 m</td></tr>
<tr><td>Paseo del Buen Pastor (Nueva Córdoba)</td><td>690 m</td></tr>
<tr><td>Tribunales I (Palacio de Justicia)</td><td>730 m</td></tr>
<tr><td>Mercado Norte</td><td>1 km</td></tr>
<tr><td>Terminal de Ómnibus</td><td>1,1 km</td></tr>
</table>'''),
   ('Un poco de historia: el casco histórico', '''<p>Córdoba se fundó en 1573 alrededor de lo que hoy es la Plaza San Martín. De ahí salen las calles del casco histórico, y una de ellas es Independencia. En sus primeras cuadras están el <strong>Cabildo</strong>, sede del gobierno colonial, y la <strong>Catedral</strong>, cuya construcción llevó casi dos siglos. Una cuadra al oeste, la <strong>Manzana Jesuítica</strong>, con la Iglesia de la Compañía de Jesús, el Colegio Monserrat y la primera universidad del país, es Patrimonio de la Humanidad desde el año 2000.</p>'''),
   ('La casona: parte del complejo de Santa Teresa', '''<p>Nuestro local está en una casona del <strong>complejo de Santa Teresa</strong>, sobre Independencia. El complejo nació en 1628, cuando Juan de Tejeda cedió la casa de su familia para fundar el <strong>Monasterio de San José de las Carmelitas Descalzas</strong> y la <strong>Iglesia de Santa Teresa de Jesús</strong>. Ahí vivió sus últimos años su hijo, <strong>Luis de Tejeda</strong>, considerado el primer poeta de estas tierras, y por eso una frase suya nos acompaña en la portada del sitio. Hoy el conjunto, Monumento Histórico Nacional desde 1941, reúne el monasterio de clausura, la iglesia y el Museo de Arte Religioso Juan de Tejeda.</p>
<p>Trabajar entre esas paredes tiene sentido para lo que hacemos: cosas que llevan tiempo, hechas todos los días, sin apuro.</p>'''),
   ('De Le Dureau a honesto', '''<p>El local abrió en <strong>2019</strong> con el nombre de <strong>Le Dureau</strong>, una de las primeras cafeterías de especialidad de Córdoba, junto a Superanfibio, cuando el café de especialidad todavía era una rareza en la ciudad. Desde <strong>2026</strong>, el proyecto se enfocó en lo que más había crecido puertas adentro: la producción propia de <a href="/masa-madre/">pan de masa madre</a> y <a href="/laminados/">laminados de manteca</a>, además del café. Con ese cambio llegó el nuevo nombre, <strong>honesto</strong>, y la unidad mayorista <a href="/bakery.html">honesto bakery</a>.</p>
<p>Misma casona, mismo café bien hecho, misma gente del centro. Ahora, también, el pan.</p>'''),
   ('¿Por qué el centro?', '''<p>Porque el centro de Córdoba es donde la gente trabaja, estudia y resuelve el día, y casi no tenía un lugar donde el pan y el café estuvieran a la altura. honesto nace de una idea simple: lo de todos los días también puede estar bien hecho. Una hogaza de <a href="/masa-madre/">masa madre</a> real, un <a href="/cafe-especialidad/">café de especialidad</a> calibrado cada mañana, <a href="/laminados/">medialunas de manteca</a> recién salidas y una mesa para quedarse, a dos cuadras de la plaza.</p>
<p>Y porque el centro es también el corazón gastronómico de la ciudad. Desde acá, con <a href="/bakery.html">honesto bakery</a>, abastecemos de pan, laminados y pastelería a cafeterías y restaurantes de toda Córdoba.</p>'''),
   ('¿Para quién es honesto?', '''<ul>
<li><strong>Para quien trabaja en el centro.</strong> Desayuno antes de la oficina, un almuerzo liviano, una reunión informal con buen café. Abrimos a las 8 y cerramos a las 21.</li>
<li><strong>Para quien estudia.</strong> Mesas cómodas, luz natural, patio y horario largo. Se puede quedar.</li>
<li><strong>Para quien pasa.</strong> Trámite, turismo, una vuelta por el casco histórico. Un lugar para probar el pan y el café de la ciudad, a metros de la Catedral.</li>
</ul>'''),
  ],
  figure=('puerta','Puerta abierta de honesto con la calle Independencia y gente pasando al fondo','La puerta a la calle Independencia. El centro pasa por acá.'),
  faq=[
   ('¿Dónde queda honesto en Córdoba?','En Independencia 180, Centro, Córdoba, Argentina. Es la calle de la Catedral y el Cabildo; honesto está una cuadra más al sur, a 200 metros de la Plaza San Martín.'),
   ('¿Cómo llego desde la Plaza San Martín?','Tomá Independencia desde la esquina sureste de la plaza, en dirección sur. Pasás el Cabildo y la Catedral, y honesto está en la cuadra siguiente. Son dos o tres minutos a pie.'),
   ('¿Qué horario tiene honesto?','Lunes a viernes de 8:00 a 21:00, sábados de 9:00 a 15:00, domingos cerrado.'),
   ('¿Hay lugar para quedarse a trabajar o estudiar?','Sí. Hay mesas cómodas, luz natural y un patio con plantas. El horario corrido de 8 a 21 los días de semana lo hace cómodo para trabajar.'),
   ('¿Qué hay cerca de honesto?','La Manzana Jesuítica y el Colegio Monserrat a menos de 200 metros; la Plaza San Martín, el Cabildo y la Catedral a 200; el Teatro del Libertador a 310; Patio Olmos a 330; la Peatonal a 430; la Municipalidad a 620 y Tribunales I a 730.'),
   ('¿honesto es el ex Le Dureau?','Sí. El local de Independencia 180 abrió en 2019 como Le Dureau, una de las primeras cafeterías de especialidad de Córdoba. Desde 2026 se llama honesto y se enfoca en pan de masa madre, laminados y café de especialidad. Misma casona, nuevo nombre.'),
   ('¿Cómo los contacto?','Por WhatsApp o teléfono al +54 351 601-6091, por correo a hola@honesto.com.ar o por Instagram en @honesto.bakery.'),
  ],
  aside_links=[('/masa-madre/','Nuestro pan de masa madre'),('/cafe-especialidad/','Café de especialidad'),('/laminados/','Medialunas y croissants'),('https://www.google.com/maps/search/?api=1&query=Independencia+180%2C+C%C3%B3rdoba%2C+Argentina','Abrir en Google Maps')],
  cta=('nos vemos en el centro.','Independencia 180, a una cuadra de la Catedral. Lunes a viernes de 8 a 21, sábados de 9 a 15.'),
 ),
}

def build(slug, pg):
    url = f'{SITE}/{slug}/'
    faq_html = '\n'.join(f'        <details class="faq__item">\n          <summary>{q}</summary>\n          <p>{a}</p>\n        </details>' for q, a in pg['faq'])
    sections_html = '\n'.join(f'      <section>\n        <h2>{h}</h2>\n{body}\n      </section>' for h, body in pg['sections'])
    # figure inserted after the 3rd section
    parts = sections_html.split('      </section>\n')
    fig_slot, fig_alt, fig_cap = pg['figure']
    figure = f'      <figure class="article__figure">\n        {img(fig_slot, fig_alt, BODY_SIZES)}\n        <figcaption>{fig_cap}</figcaption>\n      </figure>'
    if len(parts) > 3:
        parts.insert(3, figure + '\n')
    sections_html = '      </section>\n'.join(parts)
    facts_html = '\n'.join(f'        <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in pg['facts'])
    def alink(h, t):
        ext = ' target="_blank" rel="noopener noreferrer"' if h.startswith('http') else ''
        return f'          <li><a href="{h}"{ext}>{t}</a></li>'
    aside_links = '\n'.join(alink(h, t) for h, t in pg['aside_links'])
    hero_slot, hero_alt = pg['hero_img']
    cta_h, cta_p = pg['cta']
    plain = lambda s: re.sub(r'<[^>]+>', '', s)

    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#pagina", "url": url, "name": pg['title'].split(' | ')[0], "description": pg['description'],
         "inLanguage": "es-AR", "isPartOf": {"@id": SITE + "/#sitio"}, "about": {"@id": SITE + "/#negocio"},
         "primaryImageOfPage": f"{SITE}/assets/images/{hero_slot}-1600.webp", "dateModified": DATE, "keywords": pg['keywords'],
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".resumen__text", ".faq__list"]},
         "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "honesto", "item": SITE + "/"},
             {"@type": "ListItem", "position": 2, "name": pg['crumb'], "item": url}]}},
        {"@type": "Article", "@id": url + "#articulo", "headline": pg['headline'], "description": pg['description'],
         "image": [f"{SITE}/assets/images/{hero_slot}-1600.webp", f"{SITE}/assets/images/{fig_slot}-1600.webp"],
         "author": {"@id": SITE + "/#negocio"}, "publisher": {"@id": SITE + "/#negocio"}, "about": {"@id": SITE + "/#negocio"},
         "mainEntityOfPage": {"@id": url + "#pagina"}, "datePublished": DATE, "dateModified": DATE, "inLanguage": "es-AR",
         "articleSection": pg['crumb'],
         **({"mentions": pg['mentions']} if pg.get('mentions') else {}),
         "articleBody": plain(pg['resumen']) + ' ' + ' '.join(plain(b) for _, b in pg['sections'])},
        {"@type": "FAQPage", "@id": url + "#preguntas", "isPartOf": {"@id": url + "#pagina"},
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in pg['faq']]}
    ]}
    schema_txt = '\n'.join('  ' + l for l in json.dumps(schema, ensure_ascii=False, indent=2).splitlines())

    html = f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{pg['title']}</title>
  <meta name="description" content="{pg['description']}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="theme-color" content="#F4F2E7">
  <meta name="geo.region" content="AR-X">
  <meta name="geo.placename" content="Córdoba, Argentina">
  <link rel="canonical" href="{url}">

  <!-- Icons -->
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/icons/icon-192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/apple-touch-icon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{pg['title'].split(' | ')[0]}">
  <meta property="og:description" content="{pg['description']}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/images/{hero_slot}-1600.webp">
  <meta property="og:image:width" content="1600">
  <meta property="og:image:height" content="1200">
  <meta property="og:image:alt" content="{hero_alt}">
  <meta property="og:locale" content="es_AR">
  <meta property="og:site_name" content="honesto">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{pg['title'].split(' | ')[0]}">
  <meta name="twitter:description" content="{pg['description']}">
  <meta name="twitter:image" content="{SITE}/assets/images/{hero_slot}-1600.webp">

  <!-- Schema.org: WebPage + Article + FAQPage -->
  <script type="application/ld+json">
{schema_txt}
  </script>

  <link rel="preload" as="image" href="/assets/images/{hero_slot}-1200.webp" imagesrcset="{', '.join(f'/assets/images/{hero_slot}-{x}.webp {x}w' for x in (480,800,1200,1600))}" imagesizes="{HERO_SIZES}" type="image/webp">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>

<a class="skip-link" href="#main">Ir al contenido</a>

{header(slug)}<!-- MAIN -->
<main id="main">

  <!-- HERO -->
  <section class="page-hero {pg['hero_class']}">
    <div class="page-hero__inner">
      <div>
        <nav class="breadcrumbs" aria-label="Migas de pan"><a href="/">honesto</a><span>/</span>{pg['crumb']}</nav>
        <p class="section-eyebrow">{pg['eyebrow']}</p>
        <h1>{pg['h1']}</h1>
        <p class="page-hero__lead">{pg['lead']}</p>
      </div>
      <figure class="page-hero__figure">
        {img(hero_slot, hero_alt, HERO_SIZES, eager=True)}
      </figure>
    </div>
  </section>

  <!-- EN POCAS PALABRAS -->
  <section class="resumen resumen--b2b" id="resumen" aria-labelledby="resumen-title">
    <div class="resumen__inner">
      <div>
        <p class="section-eyebrow">En pocas palabras</p>
        <h2 class="resumen__title" id="resumen-title">{pg['resumen_title']}</h2>
        <p class="resumen__text">{pg['resumen']}</p>
      </div>
      <dl class="resumen__facts">
{facts_html}
      </dl>
    </div>
  </section>

  <!-- ARTÍCULO -->
  <article class="article">
    <div class="article__inner">
      <div class="article__body">
{sections_html}
      </div>
      <aside class="article__aside">
        <div class="aside-card">
          <h3>Seguir leyendo</h3>
          <ul>
{aside_links}
          </ul>
        </div>
        <div class="aside-card aside-card--blue">
          <h3>Visitanos</h3>
          <p>Independencia 180, Centro, Córdoba.<br>{HOURS}.</p>
          <a class="btn-cream" href="{WA}" target="_blank" rel="noopener noreferrer">Escribinos por WhatsApp</a>
        </div>
      </aside>
    </div>
  </article>

  <!-- PREGUNTAS FRECUENTES -->
  <section class="faq faq--rose" id="preguntas" aria-labelledby="faq-title">
    <div class="faq__inner">
      <div class="faq__head">
        <p class="section-eyebrow">Preguntas frecuentes</p>
        <h2 class="faq__title" id="faq-title">Lo que nos preguntan <em>seguido.</em></h2>
      </div>
      <div class="faq__list">
{faq_html}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta-section">
    <div class="cta-section__inner">
      <p class="cta-section__eyebrow">honesto · Independencia 180</p>
      <h2>{cta_h}</h2>
      <p class="cta-section__body">{cta_p}</p>
      <div class="cta-section__actions">
        <a class="btn-primary" href="/#contacto">Visitanos</a>
        <a class="btn-outline-dark" href="/#carta">Ver la carta</a>
      </div>
      <p class="cta-section__tagline">Menos show, más producto.</p>
    </div>
  </section>

</main>

{FOOTER}'''
    out_dir = os.path.join(ROOT, slug); os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    # sanity
    for m in re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S):
        json.loads(m.group(1))
    return len(html)

if __name__ == '__main__':
    for slug, pg in PAGES.items():
        n = build(slug, pg)
        print('ok', f'/{slug}/', n, 'bytes')
