#!/usr/bin/env python
#!C:/Python27/python.exe
# -*- coding: utf-8 -*-
from Controladores.http.Listar import Listar
from settings import config as settings
from config import config
from modulos.ztec.zred import redirecter,decode
class Archivos(Listar):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar
		Listar.__init__(self,data)

	def Archivos(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		
		self.data["addNew-enlace"]=config.base_url+settings.app+"/admin/Archivo/None/action=editar"		
		self.data["titulo"]="Archivos"
		self.data["Tabla"]="Archivos"
		self.data["Modelos"]=["archivos"]
		self.Listar()
		if self.data["action"]=="ver":
			self.HEADERS.set_headers({"Content-type":"text/palin"})
			self.HEADERS.show()
			print self.data["model"]["archivos"].obtenerFilas("Archivos")
		
	def Archivo(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar
		self.HEADERS.show()
		if self.data["ajax"]==False:

			if self.data["action"]=="editar":
		            	self.data["repeate"]=1
		            	self.data["plantillas"]=self.data["model"]["main"].obtenerFilas("Plantillas")


				
		            	keys=self.data["args"][0]

		            	i=normalizar(self.data["args"][0])

		            	self.data["categorias"]={}

		            	self.data["titulo"]=self.data["metodo"]
				

		            	if i!=None:
		            		self.data["categorias"]={}

		            		self.data["titulo"]=self.data["model"]["archivos"].obtenerFilas("Archivos")[i][0]
		            		l1=self.data["model"]["archivos"].obtenerFilas("Archivos")[i][1]
		            		self.data["boxes"]=[l1]

		            	else:
		            		self.data["titulo"]="Subir nuevo archivo"
		            		self.data["boxes"]=[self.data["model"]["archivos"].obtenerEstructura("Archivos")[1]]
		            		
		            	modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
		            	tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]
		            	self.data["control-post"]="static"
		            	self.data["post"]=self.data["titulo"]
		            	self.data["vars"]["modelos"]=modelos
		            	self.data["vars"]["opciones"]=self.data["model"][modelos[self.data["metodo"]]].obtenerFilas('Opciones')
		            	self.data["vars"]["Tablas"]=tablas            	
		            	self.servir()
              
              
			elif self.data["action"]=="save":           
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()
				opciones=self.data["model"]["archivos"].obtenerFilas("Opciones")
				for k,elem in enumerate(opciones):
					if elem[0]=="Categorias":
							tipo=opciones[k][1][int(self.data["request"]["tipo"].value)]

				
				if self.data["args"][0]==None:

					resultado=self.data["model"]["archivos"].subirArchivo(self.data["request"],self.data["metadatos"] if "metadatos" in self.data else {})
					if resultado:
						redirecter(config,settings.app,"admin","Archivo","None",action="editar")()
						pass
					else:
						print "Ya existe un archivo con el mismo nombre,  por favor utilice otro nombre,<br>"," regresando en 3 segundos..."
						print "<script>setTimeout(function(){history.back()},3000)</script>"
				else:
					
					self.data["model"]["archivos"].actualizarArchivo(self.data["args"][0],self.data["request"],self.data["metadatos"] if "metadatos" in self.data else {} )
	
					redirecter(config,settings.app,"admin","Archivo",str(self.data["args"][0]),action="editar")()

					

