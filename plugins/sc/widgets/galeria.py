#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div class="'''
try: doc+=str(data['plugin-widget']['clase'])
except Exception as e: doc+=str(e)
doc+=''' galeria owl-carousel carousel-principal owl-theme owl-loaded owl-drag height-58 height-20-xs height-25-smx height-30-sm bg-ubuntu_jet">
c=0
doc+='''  
try:
 for k,item in enumerate(data['plugin-widget']["galeria"][1][1]):
  doc+='''
  try:
   if c==0:
    doc+='''<div>'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''
  try: doc+=str(data['base_url'])
  except Exception as e:   doc+=str(e)
  doc+='''../admin/static/archivos/Imagenes/'''
  try: doc+=str(data['opciones']['archivos'][0][1][item['value']])
  except Exception as e:   doc+=str(e)
  doc+='''"><img src="'''
  try: doc+=str(data['base_url'])
  except Exception as e:   doc+=str(e)
  doc+='''../admin/static/archivos/Imagenes/'''
  try: doc+=str(data['min'](data['opciones']['archivos'][0][1][item['value']]))
  except Exception as e:   doc+=str(e)
  doc+='''" style="width:33.33%;" alt="" class="height-24 height-15-sm height-10-xs height-12-smx pad-05"></span>
  c+=1
  doc+='''
  try:
   if c==data['plugin-widget']['paginacion'] or k==len(data['plugin-widget']["galeria"][1][1])-1:
    doc+='''
    c=0
    doc+='''
    pass
  except Exception as e: doc+=str(e)
  doc+='''
  pass
except Exception as e: doc+=str(e)
doc+='''      