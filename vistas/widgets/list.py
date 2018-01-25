doc+='''<style>\n  @media(max-width:360px){\n    .center-xs{\n      float:inherit !important;\n    }\n  }\n</style>\n<div class="bg-ubuntu_porcelain pad-1">\n<div >\n\n<link rel="stylesheet" type="text/css" href="">\n<span class="font-s50" id="table-title">'''
try: doc+=str(data["titulo"])
except Exception as e: doc+=str(e)
doc+='''</span><a class="btn bg-gray blue " href="'''
try: doc+=str(data['addNew-enlace'])
except Exception as e: doc+=str(e)
doc+='''">'''
try: doc+=str(data["addNew"])
except Exception as e: doc+=str(e)
doc+='''</a>\n<hr class="height-1 bg-ubuntu_green">\n\n\n<style type="text/css">\n  .table-responsive > .paginacion{\n    display: none;\n  }\n</style>\n'''
data["table-headers"]=["Nombre","Ultima modificación","Descripción"]
doc+='''\n'''
data["vars"]["table-headers"]=["Nombre","Ultima modificación","Descripción"]
doc+='''\n\n<div class="table-responsive" id="tabla-1">\n<span><a class="link-status"href="">Todos</a></span>\n'''
try:
 for elem in data['filtros']:
  doc+='''\n <span> | <a class="link-status" href="">'''
  try: doc+=str(elem)
  except Exception as e:   doc+=str(e)
  doc+='''</a> ('''
  try: doc+=str(len(data['filtros'][elem]))
  except Exception as e:   doc+=str(e)
  doc+=''')</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n<nav>\n\n<div class="d-inline-block right center-xs">\n <input type="" placeholder="Buscar..." class="search" name="table-search">\n</div>\n\n'''
try:
 if data["listar"]==None:
  doc+='''\n'''
  data["listar"]=[]
  doc+='''\n'''
  data["vars"]["listar"]=[]
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n\n<div class="width-60p d-inline-block width-20-xs">\n <select class="table-actions">\n  '''
try:
 for elem in data["acciones"].keys():
  doc+='''\n  <option >'''
  try: doc+=str(elem)
  except Exception as e:   doc+=str(e)
  doc+='''</option>\n  '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n  \n </select>\n <button class="btn-aplicar">Aplicar</button>\n\n <select class="hidden">\n  \n  '''
try:
 for opciones in data["filtrar"]:
  doc+='''\n  <option>'''
  try: doc+=str(opciones)
  except Exception as e:   doc+=str(e)
  doc+='''</option>\n  '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n </select>\n \n <button class="hidden">Filtrar</button>\n</div>\n'''
data['pag']=1
doc+='''\n'''
data["vars"]['pag']=1
doc+='''\n'''

def paginar(x,y):
  
  a=float(x)/float(y)
  if a>int(a):
    return int(a)+1
  else:
    return int(a)

doc+='''\n<div class="d-inline-block">\n<span class="table-before"> </span>\n <button class="table-firt"><<</button>\n <button class="table-back"><</button>\n \n <input type="number" name="table-indice" value="'''
try: doc+=str(data['pag'])
except Exception as e: doc+=str(e)
doc+='''" class="table-pag width-5" max="'''
try: doc+=str(len(data['listar'])/data['n-pag']+1)
except Exception as e: doc+=str(e)
doc+='''" min="0" step="0"> de <span name="from-indice">'''
try: doc+=str(paginar(len(data['listar']),data['n-pag']))
except Exception as e: doc+=str(e)
doc+='''</span>\n <span class="n-pag"></span>\n <button class="table-next">></button>\n <button class="table-last">>></button>\n</div>\n</nav> \n\n'''
try: doc+=str(incluir(data,"tabla-contenido"))
except Exception as e: doc+=str(e)
doc+='''\n</div>\n<nav class="tabla-nav">\n \n</nav>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/tablas.js"></script>\n<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/tablas.by">\n</script>-->\n<script type="text/javascript">\ntablas.Tabla("#tabla-1")\n</script>\n</div>\n'''