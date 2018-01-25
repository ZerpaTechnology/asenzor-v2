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
try:
	import config.config as config
except:
	import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		def traducir(self,frase,langs_destino,lang="es"):
			if self.update():
				import imp
				if " " in frase
					for k,elem in enumerate(self.obtenerFilas("Frases")):
						if elem[0]==frase:
							return self.contener(elem)[langs_destino]
				else:
					for k,elem in enumerate(self.obtenerFilas("Palabras")):
						if elem[0]==frase:
							return self.contener(elem)[langs_destino]
					
		def agregarNuevaFrase(self,frase,langs_destino,lang="ES"):
			langs={"es":"Español","en":"ingles","it":"Italiano","ge":"Alemán","po":"Portugues"}
			if self.request():
				import imp
				if " " in frase:
					modificar=False
					for k,elem in enumerate(self.obtenerFilas("Frases")):
						if elem[0]==frase:
							self.db("Fases").modificar(k,"Contenido",self.modificarContenido(elem,lang_destino))
							modificar=True
						else:
							modificar=False
					if modificar==False:
						self.db("Frases").insertar(frase,
							[{"Titulo":"text","name":"titulo","value":frase}],
							{"Frase":k+1},
							zu.Datetime(),
							[])
						

				else:
					modificar=False
					for k,elem in enumerate(self.obtenerFilas("Palabras")):
						if elem[0]==frase:
							self.db("Palabras").modificar(k,"Contenido",self.modificarContenido(elem,lang_destino))
							modificar=True
						else:
							modificar=False
					if modificar==False:
						self.db("Palabras").insertar(frase,
							[{"Titulo":"text","name":"titulo","value":frase}]+[ 
								{langs[elem]:"text","name":elem,"value":langs_destino[elem]} for elem in langs_destino]
							{"Palabra":k+1},
							zu.Datetime(),
							[])
				return self.grabar()
			
		

except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e