doc+='''\n'''
try: doc+=str(incluir(data,"flash-help",isglobal=True))
except Exception as e: doc+=str(e)
doc+='''\n<section class="container-fluid sin-pad ">\n\n\n'''
data["versiones"]=len(data["model"]["main"].db.tablas[str(data["metodo"])+"-"+str(data["args"][1])] ) if str(data["metodo"])+"-"+str(data["args"][0]) in  data["model"]["main"].db.tablas else None
doc+='''\n<div>\n\n<link href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/tinymce/js/tinymce/skins/lightgray/content.min.css" rel="stylesheet" type="text/css">\n\n<div class="row">\n<div class="col-md-9">\n\n<div>\n  \n'''
try:
 if "control-post" in data:
  doc+='''\n <span class="alg-top">Enlace: </span><div class="width-28-xs" style="overflow-x:scroll;display:inline-block"><a name="preview-enlace" href="'''
  try: doc+=str(urlBuilder(config,data['app'],data['control-post'],data['post']) )
  except Exception as e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str(urlBuilder(config,data['app'],data['control-post'],data['post']))
  except Exception as e:   doc+=str(e)
  doc+='''</a></div>\n '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n  \n\n<div class="hidden" id="vars">\n'''
try: doc+=str(data["categorias"])
except Exception as e: doc+=str(e)
doc+='''\n</div>\n\n\n<form id="form" method="post" action="'''
try: doc+=str(config.base_url+settings.app+'/'+data['control']+'/'+data['metodo']+('/'+'/'.join( [str(elem) for elem in data['args']] )))
except Exception as e: doc+=str(e)
doc+='''/action=save" enctype='multipart/form-data' onsubmit="return window.modificar_atributo();">\n'''
args=data['metodo']
doc+='''\n\n'''
try:
 if normalizar(data['args'][0])==None and data['metodo']!='login':
  doc+='''\n\n '''
  btn="Registrar"
  doc+='''\n'''
 elif data['metodo']=='login':
  doc+='''\n '''
  btn="Entrar"
  doc+='''\n'''
 else:
  doc+='''\n '''
  btn="Guardar"
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+=''' \n\n<div class="pad-1 b-s1 marg-1 bg-ubuntu_porcelain" id="edit" '''
try: doc+=str('new='+str(data['repeate']) if 'new' in data and 'repeate' in data else '')
except Exception as e: doc+=str(e)
doc+='''> \n<h1>'''
try: doc+=str(data["titulo"])
except Exception as e: doc+=str(e)
doc+='''</h1>\n<hr class="height-1 bg-ubuntu_blue">\n'''
try:
 if data["versiones"]!=None:
  doc+='''\n<div class="ff marg-b1">\n  '''
  try:
   for elem in range(data["versiones"]-1):
    doc+='''\n  <span class="btn bg-gray sin-marg b-r5 btn-version">'''
    try: doc+=str(elem)
    except Exception as e:     doc+=str(e)
    doc+='''</span>\n  '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n\n  <span class="btn bg-gray b-r5 btn-version">version actual</span>\n  <span class="btn bg-bluelight white b-r5" id="ir-version" >ir a la version</span>\n</div>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n<div id="edit-box">\n\n'''
try:
 if "boxes" in data:
  doc+='''\n'''
  try: doc+=str(incluir(data,"edit-box",isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+=''' \n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n\n\n</div>\n\n\n<input type="submit" id="enviar" value="'''
try: doc+=str(btn)
except Exception as e: doc+=str(e)
doc+='''" class="btn bg-blue white pad-05 b-r5">\n'''
brython_load("nuevo.by",python="3")
doc+='''\n<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/nuevo.by">-->\n</script>\n\n<div id="tablas">\n \n</div>\n\n</form>\n<form id="metadatos">\n\n  \n</form>\n<button id="insertar" class="hidden">Insertar Tabla</button>\n<div>\n <!-- plugins inicio-->\n '''
try:
 for elem in data["plugins-hooks"]:
  doc+='''\n    \n    '''
  try:
   if data["action"]==elem[0]:
    doc+='''\n    '''
    try: doc+=str(do_shortcode(elem[1]))
    except Exception as e:     doc+=str(e)
    doc+=''' \n    '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n    '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n    \n <!-- plugins fin-->\n \n</div>\n</div>\n<aside class="col-md-3 font-ubuntu">\n '''
try: doc+=str(incluir(data,"publicar-box",isglobal=True))
except Exception as e: doc+=str(e)
doc+='''\n <br>\n '''
try: doc+=str(incluir(data,"atributo-de-pagina",isglobal=True))
except Exception as e: doc+=str(e)
doc+='''\n \n <br>\n <div class="bg-white hidden">\n  <a href=""  style="text-decoration: none;color:black">\n  <div class="b-s1 pad-05">\n   <span><b>Imagen destacada</b></span>\n  </div>\n  </a>\n  <div>\n  \n  <div class="pad-1 font-s12  height-3  text-center">\n   <a href="" class="blue" style="text-decoration: none"><b>Asignar imagen destacada</b></a>\n  </div>\n </div>\n</aside>\n</div>\n</div>\n<div class="hidden bg-white" id="custom" style="width: 80%;height:500px;position: fixed;top:20px;left:10%;z-index: 100 ">\n<style type="text/css">\n  #custom-close{\n  position: absolute;\n  right: -10px;\n  top:-10px;\n  background-color: gray;\n  color:white;\n  border: solid;\n  border-width: 1px;\n  border-radius: 15px;\n  padding: 5px;\n  cursor: pointer;\n\n  }\n  .botonera{\n    position: absolute;\n    padding: 5px;\n    bottom: 0px\n  }\n</style>\n<span id="custom-close">x</span>\n  <div class="tab" style="overflow-y: scroll;height: 470px">\n  '''
try:
 for i in range(20):
  doc+='''\n  <div class="custom"></div>\n  '''
  pass
except Exception as e: doc+=str(e)
doc+=''' \n  </div>\n  <div class="botonera">\n    <button class="insertar">insertar</button>\n    <button class="borrar">Borrar</button>\n  </div>\n</div>\n<div class="hidden bg-white" id="custom2" style="width: 80%;height:500px;position: fixed;top:20px;left:10%;z-index: 100 ">\n<style type="text/css">\n  #custom-close2{\n  position: absolute;\n  right: -10px;\n  top:-10px;\n  background-color: gray;\n  color:white;\n  border: solid;\n  border-width: 1px;\n  border-radius: 15px;\n  padding: 5px;\n  cursor: pointer;\n\n  }\n  .botonera{\n    position: absolute;\n    padding: 5px;\n    bottom: 0px\n  }\n</style>\n<span id="custom-close2">x</span>\n  <div class="tab" style="overflow-y: scroll;height: 470px">\n  '''
try: doc+=str(incluir(data,"widget-campo",isglobal=True))
except Exception as e: doc+=str(e)
doc+='''\n  <div class="botonera">\n    <button class="agregar">insertar</button>\n  </div>\n</div>\n\n<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/edit.by"></script>-->\n</section>\n\n\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/edit_box.js"></script>\n\n<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/edit-box.by"></script>-->\n\n'''