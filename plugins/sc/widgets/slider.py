#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<style type="text/css">\n.zslider{\n	position: relative;\n	background: black;\n}\n.f-left{\n  position: absolute;\n  \n  font-size: 50px;\n  color: blue;\n  top:45%;\n  left: 0;\n  cursor: pointer;\n\n  \n\n  z-index: 200;\n }\n  .exit{\n  \n  font-size: 30px;\n  color: white;\n  position: absolute;\n  right: 0px;\n  top: 0px;\n  cursor: pointer;\n\n\n }\n.f-right{\n  \n  position: absolute;\n  \n  font-size: 50px;\n  color: blue;\n  \n  right: 5%;top: 45%;\n  right: 0;\n  z-index: 200;\n  cursor: pointer;\n   }\n</style>\n\n<div>\n\n<div class="zslider" style="position: relative;width:400px;height: 400px">\n\n	<div class="content " style="height: 400px;overflow: hidden;">\n	'''
try:
 for k, elem in enumerate(data['plugin-widget']["slider"][1][1]):
  doc+='''\n		'''
  img=data['opciones'][elem['opciones']][0][1][elem['value']]
  doc+='''\n		<img src="'''
  try: doc+=str(config.base_url+config.apps_folder+settings.app+'/admin/'+routes.static_folder)
  except Exception as e:   doc+=str(e)
  doc+='''archivos/Imagenes/'''
  try: doc+=str(img)
  except Exception as e:   doc+=str(e)
  doc+='''"\n		style="max-height:100%;max-width: 100%;vertical-align: center" >\n\n	'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>\n  <div class="f-left"><img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f1.png"  class="height-5"></div>\n  <div class="f-right"><img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f2.png"  class="height-5"></div>\n</div>\n\n\n\n</div>\n	 '''