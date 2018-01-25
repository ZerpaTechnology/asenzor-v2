#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from ztec.zmodel import Model
import sys
import os
import datetime
import ztec.zu as zu
sys.path.append("../")
import settings
import routes
try:
	import config.config as config
except:
	import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		def traducir(self,frase,lang="ES"):
			if self.update():
				import imp
				modelo=imp.load_source("modelo","traducciones-"+lang.upper()+"-"+frase.strip()[0]+"_model.py").
				return modelo.traducir(frase,lang="ES")


		def agregarNuevaFrase(self,frase,lang_destino,lang_origen="ES"):
			if self.update():
				import imp
				modelo=imp.load_source("modelo","traducciones-"+lang.upper()+"-"+frase.strip()[0]+"_model.py").model(
					config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"traducciones-ES","request/")

				return modelo.agregarNuevaFrase(frase,lang_destino,lang_origen="ES")
		

except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e