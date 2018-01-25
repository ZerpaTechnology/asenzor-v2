doc+='''<style type="text/css">\n  .btn-flash-info{\n    cursor: pointer;\n  }\n</style>\n<div class="bg-white container-fluid font-ubuntu font-s13" >\n  <div class="row hidden" id="flash-help">\n  <div  class="col-md-2">\n    <span class="btn-flash-info d-block bluelight pad-b05"><b>Vista previa</b></span>\n    <span class="btn-flash-info d-block bluelight pad-b05"><b>Navegación</b></span>\n    <span class="btn-flash-info d-block bluelight pad-b05"><b>Diseño de la pantalla</b></span>\n    <span class="btn-flash-info d-block bluelight pad-b05"><b>Contenido</b></span>\n  </div>\n  <div  class="col-md-7" style="background-color: rgb(200,200,200);">\n    <div class="info hidden">  \n      <p>¡Bienvenido a tu escritorio de AsenZor! Esta es la pantalla que verás cuando inicies sesión en tu sitio, que te da acceso a todas las funciones de gestión del sitio de AsenZor. Puedes obtener ayuda para cualquier pantalla haciendo clic en la pestaña Ayuda en la esquina superior.</p>\n    </div>\n    <div class="info hidden">\n      <p>El menú de navegación de la izquierda proporciona enlaces a todas las pantallas de administración de Asenzor, con elementos de submenú que aparecen al pasar el ratón sobre ellos. Puedes minimizar este menú para que sea una barra estrecha de iconos haciendo clic en la flecha del menú Cerrar en la parte inferior.</p>\n\n      <p>Enlaces en la Barra de Herramientas en la parte superior de la pantalla conecta tu escritorio y tu sitio, y proporciona acceso a tu perfil e información valiosa de AsenZor.</p>\n    </div>\n    <div class="info hidden">\n      <p>Puedes usar los controles siguientes para organizar tu escritorio de modo que se adapte a tu rutina de trabajo. Puedes hacer lo mismo en la mayoría de las secciones de administración.</p>\n\n      <p>Opciones de pantalla — Usa la pestaña de Opciones de pantalla para elegir qué cajas mostrar en tu escritorio.</p>\n\n      <p>Arrastrar y soltar — Para reorganizar las cajas arrástralas haciendo clic en la barra de título de la caja seleccionada y suéltala cuando veas aparecer un rectángulo de puntos en el lugar donde quieras situarla.</p>\n\n      <p>Controles de caja — Haz clic en la barra de título de la caja para expandirla o contraerla. Algunas cajas añadidas por plugins puede que tengan contenido que configurar, y mostrarán un enlace de “Configure” en la barra de título si pasas el cursor sobre ella.</p>\n    </div>\n    <div class="info pad-05">\n    <p>Las cajas en tu Escritorio son:</p>\n    <p>De un vistazo — Muestra un resumen del contenido de tu sitio e identifica qué tema y versión de AsenZor estás utilizando.</p>\n\n      <p>Actividad — Muestra las entradas programadas previstas, las entradas recientemente publicadas y los comentarios más recientes a tus entradas, y te permite moderarlos.</p>\n\n      <p>Borrador rápido — Te permite crear una nueva entrada y guardarla como borrador. También muestra enlaces a las 5 entradas en borrador más recientes que hayas empezado.</p>\n\n      <p>Noticias de AsenZor — Las últimas noticias sobre el proyecto oficial de AsenZor, el planeta AsenZor y los plugins más populares.</p>\n\n      <p>Bienvenido — Muestra enlaces a algunas de las tareas más comunes al configurar un nuevo sitio.\n    </p>\n    </div>\n  </div>\n  <div  class="col-md-3">\n    <b class="marg-b1">Para mas información:</b>\n    <span class="d-block bluelight pad-b05"><b>Documentación sobre el escritorio</b></span>\n    <span class="d-block bluelight pad-b05"><b>Foro de soporte</b></span>\n  </div>\n  </div>\n  <div class="text-right">\n    <button id="ayuda">Ayuda</button>\n  </div>\n</div>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/ayuda.js"></script>\n<!--<script type="text/python" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/ayuda.by"></script>-->'''