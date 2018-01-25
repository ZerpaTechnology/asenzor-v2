doc+='''<div >\n<form target="iframeUpload" method="post" enctype="multipart/form-data" action="'''
try: doc+=str(config.base_url+config.controller_folder)
except Exception as e: doc+=str(e)
doc+='''post.py" id="form-upload">\n<h2>'''
try: doc+=str("Webapps" if data["action"]=="allapps" else "Plugins")
except Exception as e: doc+=str(e)
doc+="""</h2>\n<input type="file" name="file" id="subir-app">\n<input type="hidden" name="upload" value='"""
try: doc+=str("webapp" if data["action"]=="allapps" else "plugin")
except Exception as e: doc+=str(e)
doc+="""' >\n<input type="hidden" name="action" value="upload">\n<input type="hidden" name="nombre" value="" >\n<div class="ff hidden" id="detalles">\n	<p></p>\n	\n</div>\n</form>\n<iframe name="iframeUpload" class="hidden" style="height: 50px;border: none;"></iframe>\n<button class="btn bg-blue white b-r5 hidden d-block" name="btn-instalar">Instalar</button>\n\n<div class="bg-gray font-ubuntu pad-l05 font-s14" id="gestor">\n	<style type="text/css">\n	.btn-webapps:hover{\n	color:#00a0d2;\n	cursor: pointer;\n	}\n		\n	</style>\n\n	<span style="border: solid; border-color: transparent;" class="btn-webapps">Instaladas</span>\n	<div class="d-inline-block bg-ubuntu_ash pad-05">\n	<b class="" style="color:rgb(155,0,0);">Nuevo: </b>\n	<div class="d-inline-block bg-gray pad-1">\n	<span class="btn-webapps" style="border: solid; border-color: transparent;">Destacadas</span>	\n	<span class="btn-webapps" style="border: solid; border-color: transparent;">Populares</span>	\n	<span class="btn-webapps" style="border: solid; border-color: transparent;">Recientes</span>	\n	<span class="btn-webapps" style="border: solid; border-color: transparent;">Favoritos</span>		\n	</div>\n	</div>\n	<input type="search" name="buscar" placeholder="Buscar webapps" style="height:30px">\n</div>\n<div class="tab">\n"""
try:
 for app in data["items"]:
  doc+='''\n<span class="marg-05 font-ubuntu d-inline-block b-s1">\n	<span>\n		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception as e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			\n		</div>\n	</span>\n	<div class="bg-white pad-1">\n		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception as e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="'''
  try: doc+=str('activar' if 'Desactivada' in app[4] else 'desactivar')
  except Exception as e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str("Activar" if "Desactivada" in app[4] else "Desactivar")
  except Exception as e:   doc+=str(e)
  doc+='''</button>\n		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception as e:   doc+=str(e)
  doc+='''\n	</div>\n</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n\n</div>\n<div class="tab hidden">\n'''
try:
 for app in data["items-destacadas"]:
  doc+='''\n<span class="marg-05 font-ubuntu d-inline-block b-s1">\n	<span>\n		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][0][-1]['value'])
  except Exception as e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			\n		</div>\n	</span>\n	<div class="bg-white pad-1">\n		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception as e:   doc+=str(e)
  doc+=''' </b> <button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception as e:   doc+=str(e)
  doc+="""</button> <span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception as e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception as e:   doc+=str(e)
  doc+='''</span>\n		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception as e:   doc+=str(e)
  doc+='''\n	</div>\n</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n<div class="tab hidden">\n'''
try:
 for app in data["items-populares"]:
  doc+='''\n<span class="marg-05 font-ubuntu d-inline-block b-s1">\n	<span>\n		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception as e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			\n		</div>\n	</span>\n	<div class="bg-white pad-1">\n		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception as e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception as e:   doc+=str(e)
  doc+="""</button><span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception as e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception as e:   doc+=str(e)
  doc+='''</span>\n		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception as e:   doc+=str(e)
  doc+='''\n	</div>\n</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n<div class="tab hidden">\n'''
try:
 for app in data["items-recientes"]:
  doc+='''\n<span class="marg-05 font-ubuntu d-inline-block b-s1">\n	<span>\n		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception as e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			\n		</div>\n	</span>\n	<div class="bg-white pad-1">\n		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception as e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception as e:   doc+=str(e)
  doc+="""</button><span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception as e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception as e:   doc+=str(e)
  doc+='''</span>\n		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception as e:   doc+=str(e)
  doc+='''\n	</div>\n</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n<div class="tab hidden">\n'''
try:
 for app in data["items-favoritos"]:
  doc+='''\n<span class="marg-05 font-ubuntu d-inline-block b-s1">\n	<span>\n		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception as e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			\n		</div>\n	</span>\n	<div class="bg-white pad-1">\n		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception as e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception as e:   doc+=str(e)
  doc+="""</button><span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception as e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception as e:   doc+=str(e)
  doc+='''</span>\n		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception as e:   doc+=str(e)
  doc+='''\n	</div>\n</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n<div class="tab hidden">\n</div>\n</div>\n<form target="online-install" method="post" enctype="multipart/form-data" action="'''
try: doc+=str(config.base_url+config.controller_folder)
except Exception as e: doc+=str(e)
doc+="""ajax.py" id="form-online-install">\n<input type="hidden" name="control" value='"""
try: doc+=str("webapp" if data["action"]=="allapps" else "plugin")
except Exception as e: doc+=str(e)
doc+="""'>\n<input type="hidden" name="app" value="asenzor">\n<input type="hidden" name='item' value="">\n<input type="hidden" name='action' value="install">\n\n<input type="hidden" name="clave" value="">"""
#clave sirve para mandar un codigo de orden por compra en apps y plugins de pago que se envia por correo
doc+='''\n</form>\n'''

data["content"]="""
<h3>Para instalar """+("esta app" if data["action"]=="allapps" else "este plugin")+"""</h3>
<p>Deberas insertar la clave de orden que se envio a tu correo electronico en el siguiente campo:</p>
<input type="text" name="user_clave">
<button name="insertar_clave">Aceptar</button>
"""

doc+='''\n\n'''
try: doc+=str(incluir(data,"alert",isglobal=True))
except Exception as e: doc+=str(e)
doc+='''\n<iframe name="online-install" class="hidden" >	\n</iframe>\n<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/gestor.by"></script>\n<script type="text/python3">\nfrom browser import window\nwindow.Gestor("#gestor")\n</script>'''