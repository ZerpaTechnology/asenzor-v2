#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from modulos.ztec.zmodel import Model
import sys
import os
import datetime
import modulos.ztec.zu as zu
sys.path.append("../")
import settings
try:
	import config.config as config
except:
	import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		def crearTema(self,data,metadatos=None):
			if self.request():
				nuevo=self.valorizarEstructura(data,self.obtenerEstructura("Ayuda"))
				nuevo[2]={"Ayuda":self.obtenerLongitud("Ayuda")}
				nuevo[3]=zu.DateTime()
				self.fusionarMetadatos(nuevo[4],metadatos)
				self.db("Ayuda").insertar(nuevo[0],nuevo[1],nuevo[2],nuevo[3],nuevo[4])
				self.grabar()

		def modificarTema(self,indice,data,metadatos=None):
			
			self.actualizarContenido(indice,data,metadatos,"Ayuda")
except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e