#!/usr/bin/env python
# -*- coding: utf-8 -*-
#modulo para traducir datos


from zmodel import Model

class ZT(Model):
	def __init__(self,ruta,request_folder="request/",token="user",idioma="es",ext=".py"):
		
		Model.__init__(self,ruta,request_folder,token,ext=".py")
		

		self.idioma=idioma
		pass
		
	def __callback__(self,frase,letras=1):
		
		if self.update(self.originalFile+"-"+frase.strip()[:letras].upper()):
			if " " in frase:
				for k,elem in enumerate(self.obtenerFilas("Frases")):
					if elem[0]==frase:
						return self.contener(elem)[langs_destino]
			else:
				for k,elem in enumerate(self.obtenerFilas("Palabras")):
					if elem[0]==frase:
						return self.contener(elem)[langs_destino]
		
		
	def agregarNuevaFrase(self,frase,lang_destino,lang_origen="ES",letras=1):
			
			langs={"es":"Español","en":"ingles","it":"Italiano","ge":"Alemán","po":"Portugues"}
			if self.request(self.originalFile+"-"+frase.strip()[:letras].upper()):
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
								{langs[elem]:"text","name":elem,"value":langs_destino[elem]} for elem in langs_destino],
							{"Palabra":k+1},
							zu.Datetime(),
							[])
				return self.grabar()
			


	def t(self,oracion):
		pass
		
	def t2(self,oracion,contexto):
		pass		
		
	def agregar_exp(self,idioma_t,idioma_t2,exp1,exp2):
		pass
		
	def agregar_p(self,idioma_t,idioma_t2,p1,p2):
		pass
		
	def crear_i(self,idioma):
		pass
		
		
