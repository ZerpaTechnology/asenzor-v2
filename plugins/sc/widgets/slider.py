#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<style type="text/css">
try:
 for k, elem in enumerate(data['plugin-widget']["slider"][1][1]):
  doc+='''
  img=data['opciones'][elem['opciones']][0][1][elem['value']]
  doc+='''
  try: doc+=str(config.base_url+config.apps_folder+settings.app+'/admin/'+routes.static_folder)
  except Exception as e:   doc+=str(e)
  doc+='''archivos/Imagenes/'''
  try: doc+=str(img)
  except Exception as e:   doc+=str(e)
  doc+='''"
  pass
except Exception as e: doc+=str(e)
doc+='''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f1.png"  class="height-5"></div>
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f2.png"  class="height-5"></div>