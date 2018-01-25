#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div class="bg-ubuntu_porcelain pad-1"><div ><link rel="stylesheet" type="text/css" href=""><span class="font-s50" id="table-title">'''
try: doc+=str(data["titulo"].replace("-"," "))
except Exception, e: doc+=str(e)
doc+='''</span><hr class="height-1 bg-ubuntu_green"><span><a class="link-status"href="">Todos</a></span>'''
for elem in data['filtros']:
  doc+='''	<span> | <a class="link-status" href="">'''
  try: doc+=str(elem)
  except Exception, e:   doc+=str(e)
  doc+='''</a> ('''
  try: doc+=str(len(data['filtros'][elem]))
  except Exception, e:   doc+=str(e)
  doc+=''')</span>'''
  pass
doc+='''<div class="d-inline-block right">	<input type="text" name="" placeholder="Buscar..." class="search"></div></div><nav><div class="width-60p d-inline-block">	<select class="table-actions">		'''
for elem in data["acciones"].keys():
  doc+='''		<option >'''
  try: doc+=str(elem)
  except Exception, e:   doc+=str(e)
  doc+='''</option>		'''
  pass
doc+='''			</select>	<button class="btn-aplicar">Aplicar</button>	<select class="hidden">		'''
for opciones in data["filtrar"]:
  doc+='''		<option>'''
  try: doc+=str(opciones)
  except Exception, e:   doc+=str(e)
  doc+='''</option>		'''
  pass
doc+='''	</select>	<button class="hidden">Filtrar</button></div><div class="d-inline-block"><span class="table-before"> </span>	<button class="table-firt"><<</button>	<button class="table-back"><</button>	<input type="number" name="" value="1" class="table-pag width-5" max="'''
try: doc+=str(len(data['listar'])/data['n-pag']+1)
except Exception, e: doc+=str(e)
doc+='''" min="0" step="0">	<span class="n-pag"></span>	<button class="table-next">></button>	<button class="table-last">>></button></div></nav>	<table class="table table-hover" id="tabla-1">  <tr>  	<td>Cargando...</td>  	  </tr>   </table><nav class="tabla-nav">	</nav><script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/tablas.by"></script></div>'''