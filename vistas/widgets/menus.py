doc+='''\n<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-ui-1.12.1.custom/jquery-ui.css">\n<style type="text/css">\n	#accordion{\n	width:300px;\n	font-size:14px;\n	\n	}\n	.ui-accordion .ui-accordion-content{\n		padding: 0px;\n		height: 300px\n	}\n	.ui-tabs-anchor{\n		padding: .1em .8em !important;\n	}\n	\n	li{\n		list-style: none;\n	}\n	span[name='seleccionar-todo']{\n		cursor: pointer;\n	}\n	\n</style>\n  <div class="tabs">\n  <ul>\n    <li><a href="#edit-menu"><b>Editar menu</b></a></li>\n    <li><a href="#manage-locations"><b>Manejar localizaciones</b></a></li>\n    </ul>\n  <div id="edit-menu">\n<div class="box">\n<div class="row">\n<div class="col-md-12">\n<div class="b-s1 b-r5 b-gray pad-05">\n<span>Selecciona un menu para editar </span>\n \n<select class="bg-white" style="width: 200px" name="seleccionar-menu">\n    <option></option>\n	'''
try:
 for elem in data["Menus"]:
  doc+='''\n	<option>'''
  try: doc+=str(elem[0])
  except Exception as e:   doc+=str(e)
  doc+='''</option>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</select>\n<button name="aplicar-menu">seleccionar</button>\no <a href="">crea un nuevo menu</a>\n</div>\n\n\n</div>\n</div>\n<div class="row">\n	<div class="col-md-4">\n		\n<div id="accordion">\n  <h3>Paginas</h3>\n  <div>\n  <div class="tabs">\n  <ul>\n    <li><a href="#tabs-1">Mas reciente</a></li>\n    <li><a href="#tabs-2">Ver todo</a></li>\n    <li><a href="#tabs-3">Buscar</a></li>\n  </ul>\n  <div id="tabs-1" class="sin-marg">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	'''
metas=self.data["model"]["global"].formatearListaMetadatos(data["Paginas"])
doc+='''\n	'''
try:
 for k, pagina in enumerate(data["Paginas"]):
  doc+='''\n	'''
  meta=metas[k]
  doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+pagina[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" \n	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	\n	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" >'''
  try: doc+=str(pagina[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-2">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	'''
try:
 for pagina in data["Paginas"]:
  doc+='''\n	'''
  meta=metas[k]
  doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+pagina[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" \n	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	\n	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" >'''
  try: doc+=str(pagina[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-3">\n    <div>\n    	<input type="search" name="buscar-pagina" >\n    	<div style="overflow: scroll;height: 200px">\n    		\n    	</div>\n    </div>\n  </div>\n</div>\n \n  </div>\n  <h3>Entradas</h3>\n  <div>\n  <div class="tabs">\n  <ul>\n    <li><a href="#tabs-4">Mas reciente</a></li>\n    <li><a href="#tabs-5">Ver todo</a></li>\n    <li><a href="#tabs-6">Buscar</a></li>\n  </ul>\n  <div id="tabs-4" class="sin-marg">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	'''
metas=self.data["model"]["global"].formatearListaMetadatos(data["Entradas"])
doc+='''\n\n	'''
try:
 for k,entrada in enumerate(data["Entradas"]):
  doc+='''\n\n	'''
  meta=metas[k]
  doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+entrada[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" \n	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	\n	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" >'''
  try: doc+=str(entrada[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-5">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	\n	'''
try:
 for k,entrada in enumerate(data["Entradas"]):
  doc+='''\n	'''
  meta=metas[k]
  doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+entrada[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" \n	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	\n	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	 >'''
  try: doc+=str(entrada[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-6">\n    <div>\n    	<input type="search" name="buscar-pagina" >\n    	<div style="overflow: scroll;height: 200px">\n    		\n    	</div>\n    </div>\n  </div>\n  \n</div>\n \n  </div>\n  <h3>Enlaces personalizados</h3>\n  <div>\n  <table>\n  	<tr>\n  		<td><b>URL</b></td>\n  		<td><input type="" name="custom-url" value="http://"></td>\n  	</tr>\n  	<tr>\n  		<td><b>Texto del enlace</b></td>\n  		<td><input type="" name="custom-text"></td>\n  	</tr>\n  	\n  </table>\n  <button name="add-to-menu2">Añadir al menu</button>\n  </div>\n  <h3>Categorias</h3>\n  <div>\n  <div class="tabs">\n  <ul>\n    <li><a href="#tabs-7">Mas reciente</a></li>\n    <li><a href="#tabs-8">Ver todo</a></li>\n    <li><a href="#tabs-9">Buscar</a></li>\n  </ul>\n  <div id="tabs-7" class="sin-marg">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	'''
metas=self.data["model"]["global"].formatearListaMetadatos(data["Categorias"])
doc+='''\n	'''
try:
 for categoria in data["Categorias"]:
  doc+='''\n	'''
  meta=metas[k]
  doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+categoria[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" \n	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	\n	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str(categoria[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-8">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	\n	'''
try:
 for categoria in data["Categorias"]:
  doc+='''\n	'''
  meta=metas[k]
  doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+categoria[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" \n	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	\n	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" \n	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"\n	>'''
  try: doc+=str(categoria[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-9">\n    \n  </div>\n</div>\n \n  </div>\n  '''
try:
 for other_tag in data["other-tags"]:
  doc+='''\n  <h3>'''
  try: doc+=str(other_tag)
  except Exception as e:   doc+=str(e)
  doc+='''</h3>\n  <div>\n  <div class="tabs">\n  <ul>\n    <li><a href="#tabs-4">Mas reciente</a></li>\n    <li><a href="#tabs-5">Ver todo</a></li>\n    <li><a href="#tabs-6">Buscar</a></li>\n  </ul>\n  <div id="tabs-4" class="sin-marg">\n    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">\n	<ul style="text-align: left">\n	\n	'''
  try:
   for tag in data[other_tag]:
    doc+='''\n	<li><input type="checkbox"> <b \n	href="'''
    try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(tag[0]['control']+'/' if 'control' in tag[0] else '')+tag[0]['titulo'].replace(' ','-'))
    except Exception as e:     doc+=str(e)
    doc+='''" \n	modelo="'''
    try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''" 	\n	tabla="'''
    try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''" \n	indice="'''
    try: doc+=str(meta['indice'] if 'indice' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''"\n	control="'''
    try: doc+=str(meta['control'] if 'control' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''" \n	metodo="'''
    try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''"\n	>'''
    try: doc+=str(tag[0])
    except Exception as e:     doc+=str(e)
    doc+='''</b></li>\n	'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n	</ul>\n	</div>\n    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>\n  </div>\n  <div id="tabs-5">\n    \n  </div>\n  <div id="tabs-6">\n    <div>\n    	<input type="search" name="buscar-pagina" >\n    	<div style="overflow: scroll;height: 200px">\n    		\n    	</div>\n    </div>\n  </div>\n  \n</div>\n \n  </div>\n  '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n\n\n	</div>\n	<div class="col-md-8">\n	<div class="pad-1 bg-graylight">\n		<label><b>Nombre del menu</b></label><input type="" name="nombre-menu" placeholder="Menú">\n		<button name="guardar-menu">Guardar</button>\n	</div>\n	<div class=" pad-1">\n	<h2><b>Estructura del menu</b></h2>\n\n<p>Arrastre cada elemento en el orden que prefiera. Haga clic en la flecha a la derecha del elemento para mostrar opciones de configuración adicionales.</p>\n\n\n		<ul id="nav-menu" class="sortable droptrue">\n  \n  \n</ul>\n	</div>\n	<div>\n		<h2>Configuracion del menu</h2>\n		<table>\n			<tr>\n				<td>Añadir pagina automaticas</td>\n				<td><input type="checkbox" name="nivel-superior">\nAgregar automáticamente nuevas páginas de nivel superior a este menú</td>\n			</tr>\n			<tr>\n				<td>Mostrar localización</td>\n				<td><input type="checkbox" name="menu-principal">Menu principal</td>\n			</tr>\n			<tr>\n				<td></td>\n				<td><input type="checkbox" name="menu-pie">Menu de pie</td>\n			</tr>\n			<tr>\n				<td></td>\n				<td><input type="checkbox" name="menu-barra-superior">Menu barra superior</td>\n			</tr>\n			<tr>\n				<td></td>\n				<td><input type="checkbox" name="menu-mi-cuenta">Menu mi cuenta</td>\n			</tr>\n		</table>\n		<a href="" name="borrar-menu"> Borrar menu</a>\n		<button name="guardar-menu">Guardar menu</button>\n	</div>\n	</div>\n\n</div>\n</div>\n</div>\n<div id="manage-locations">\n<span>El tema admite 4 menús. Seleccione el menú que aparecerá en cada ubicación.</span>\n<div>\n	<table>\n		<tr>\n			<td style="padding-right: 30px;"><b>Localizacion del tema</b></td>\n			<td><b>Asignar menu</b></td>\n			<td></td>\n		</tr>\n		<tr>\n			<td>Menu principal</td>\n			<td><select style="width: 200px" name="asignar-menu-principal"><option></option></select></td>\n			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>\n		</tr>\n		<tr>\n			<td>Menu de pie</td>\n			<td><select style="width: 200px" name="asignar-menu-pie"><option></option></select></td>\n			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>\n		</tr>\n		<tr>\n			<td>Menu barra superior</td>\n			<td><select style="width: 200px" name="asignar-menu-barra-superior"><option></option></select></td>\n			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>\n		</tr>\n		<tr>\n			<td>Menu de mi cuenta</td>\n			<td><select style="width: 200px" name="asignar-menu-mi-cuenta"><option></option></select></td>\n			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>\n		</tr>\n\n	</table>\n</div>\n</div>\n\n <script>\n  $( function() {\n    $( "#accordion" ).accordion({\n      collapsible: true\n    });\n    $( ".accordion" ).accordion({\n      collapsible: true,\n      active:false\n    });\n     $( ".tabs" ).tabs();\n       $( "ul.droptrue" ).sortable({\n      connectWith: "ul"\n    });\n \n    $( "ul.dropfalse" ).sortable({\n      connectWith: "ul",\n      dropOnEmpty: false\n    });\n    $( ".sortable" ).disableSelection();\n\n  } );\n  </script>\n  <script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/gestor_menus.js"></script>\n <script >\n gestor_menus.Gestor("#nav-menu")\n </script>'''