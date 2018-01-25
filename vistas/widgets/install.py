#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div>
	'''
try: doc+=str(data["status"])
except Exception, e: doc+=str(e)
doc+='''
	<p>Para regresar al escritorio presione <a href="'''
try: doc+=str(urlBuilder(config,settings.app,'admin','index'))
except Exception, e: doc+=str(e)
doc+='''">aquí</a></p>
	<p>Gracias por usar Asenzor, esperamos que te agrade tu nueva actualización</p>
	<p>Recuerda que puedes enviarnos tus comentarios a <a href="mailto:soporte@zerpatechnology.com.ve">soporte@zerpatechnology.com.ve</a></p>
	<p>Ayudanos a hacer de Asenzor una de las mejores framework/cms para construir sitios web</p>
</div>'''