#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html><head>	'''
incluir(data,"head")
print '''</head><body>'''
incluir(data,"widget-navbar")
print '''<div class="container"><div class="row"><div class="col-md-12 pad-1 height-35">'''
if "errores_link" in data and type(data["errores"]):
  print '''<a href="'''  +str(data['errores_link'])  +'''">Ver Errores</a>'''
else:
  print ''''''  +str(data["errores"])  +'''		'''
  pass
print '''</div>	</div></div>'''
incluir(data,"footer")
print '''</body></html>'''