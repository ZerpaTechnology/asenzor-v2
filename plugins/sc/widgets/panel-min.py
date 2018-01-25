#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''
<div class="ff">
	<H4>Bienvenido '''
try: doc+=str(data["user"]["usuario"])
except Exception, e: doc+=str(e)
doc+='''</H4>
	<a href="'''
config.base_url
doc+='''"class="btn d-block white">Horarios</a>
	<a href="'''
config.base_url
doc+='''"class="btn d-block white">Promedio</a>
	<a href="'''
config.base_url
doc+='''"class="btn d-block white">Materias</a>
	<a href="'''
config.base_url
doc+='''"class="btn d-block white">Profesores</a>
	<a href="'''
config.base_url
doc+='''"class="btn d-block white">Documentos</a>
</div>
'''