#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
import sys
import os
import time
from zdb import DB
from modulos.ztec.zred import normalizar
ordenDB=[]
try:
	class Model:
		"""docstring for Model
		Pasar los campos a insertar mediantes variables y no mediante retorno de funciones
		a=len("a")
		db("tabla").insertar(a)
		
		y no 

		db("tabla").insertar(len("a"))
		ya que da errores
		"""

		def __init__(self,dbfile,resquest_folder,token,debug=False,ext=".zdb"):
			try:


				self.dbfile=dbfile
				self.originalFile=dbfile
				#extencion de la database, nota: en android .py se hace .pyo por lo cual no se debe usar
				self.ext=ext
				self.resquest_folder=resquest_folder
				self.token=token


				self.debug=debug
				self.ext=ext
				self.log=[]



				self.errores=[]
				self.db=None
				self.models={}

				self.root_db=self.dbfile+"_db"+self.ext
				try:
					os.mkdir(self.resquest_folder)
				except Exception,e:
					import sys
					import traceback
					exc_type,exc_obj,exc_tb=sys.exc_info()
					fname = exc_tb.tb_frame.f_code.co_filename
					self.log.append([["La carpeta de requests ya estaba creada",exc_type,exc_obj,exc_tb],
									 [__file__,self.dbfile+"_struct"+self.ext]
						])
					if self.debug==True:
						print e

				#Cabecera del modelo


				#sys.path.append("../config")
				
				import zu
				
				
				tiempo=time.time()
				self.ultimaModificacion=0

				
				if os.path.exists(self.dbfile+"_db"+ext):



					
					

					self.db=DB(self.dbfile+"_db"+ext,debug=debug)


					(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(self.dbfile+"_db"+self.ext)
					self.ultimaModificacion=mtime2



				else:

					try:

						if (self.dbfile+"_struct"+ext).split("/")[-1] in os.listdir(self.dbfile[:-len(self.dbfile.split("/")[-1])]):
							f=open(self.dbfile+"_struct"+ext,"r")

							struct=f.read()
							f.close()
							
							exec(struct)

							(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(self.dbfile+"_struct"+self.ext)

							self.ultimaModificacion=mtime2	


						else:
							print "No se puedo encontrar la estructura "+self.dbfile+" parar cargar, porfavor revisa si estas usando la 'ext' correcta"


					except Exception as e:

						
						self.errores.append("Error al cargar la estructura: "+self.dbfile[self.dbfile.rfind("/")+1:]+"\n"+str(e))
						import sys
						import traceback


						exc_type,exc_obj,exc_tb=sys.exc_info()
						fname = exc_tb.tb_frame.f_code.co_filename
						self.log.append([[exc_type,exc_obj,exc_tb],
										 [__file__,self.dbfile+"_struct"+self.ext]
							])
						if self.debug==True:
							print e
						
					
					

							
					self.db=db





				
				self.db.debug=debug

			except Exception, e:

				if self.debug==True:
					print "error en zmodel"

					print e
		def enrutar(self,nueva):
			import imp
			import copy
			ruta=copy.copy(self.dbfile)
			self.dbfile=nueva
			self.modelo=imp.load_source("modelo",ruta+"_model.py").model(self.dbfile,"request/","user")

		def update(self,dbfile=None):

			if dbfile!=None:
				self.dbfile=dbfile
			if os.path.exists(self.dbfile+"_db"+self.ext):

				(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(self.dbfile+"_db"+self.ext)
				if mtime2>self.ultimaModificacion:
					self.db=DB(self.dbfile+"_db"+self.ext)
					self.db.debug=self.debug
					self.ultimaModificacion=mtime2
					return True
				else:
					return True
			elif self.db!=None:
				return True
			else:
				return False
		def eliminar(self,c,tabla):
				if self.request():
					self.db(tabla).delFila(c)
					return self.grabar()

		def grabar(self,dbfile=None):
			"""
			siempre que exista un request debe terminar con un self.grabar
			asi no se hayan modificado datos ya que esto cierra la peticion
			y evita el tiempo de espera de la proxima peticion
			"""
			if os.path.exists(self.resquest_folder+"ordenDB.py"):
				if dbfile!=None:
					self.dbfile=dbfile
				self.root_db=self.dbfile+"_db"+self.ext

				self.db.grabar(self.root_db)
				os.remove(self.resquest_folder+"ordenDB.py")

				self.update()
				return True
			else:
				False
		
		def tipo(self,campo):
			"""
			Este metodo sirve para obtener el tipo de un campo
			en formato estandar de formularios ZDB
			"""
			ncampo=list(campo)
			for clave in ["opciones",
						  "opcion",
						  "value",
						  "name",
						  "step",
						  "requerido",
						  "tabla",
						  "depende",
						  "categoria",
						  "descripcion",
						  "padre",
				]:
				if clave in ncampo:
					ncampo.remove(clave)
			return campo[ncampo[0]]
		def exportarMetadato(self,listmeta,meta):
			for elem in listmeta:
				if elem["name"]==meta:
					return elem["value"]

		def obtenerMetadatos(self,tabla=None,fila=None):
				if self.update():	
					if tabla==None and self.db.seleccion!=None:
						tabla=self.db.seleccion
					paginas=[]
					for k,pagina in enumerate(self.obtenerFilas(tabla)):
							paginas.append([pagina[0],pagina[4]])
							if fila==k:
								return paginas[k]

					return paginas
		def formatearMetadatos(self,metas):
			"""
			se pasan metas como 
			[{"nombre":"meta","value":"valor"}]
			y retorna
			{"meta":"valor"}
			"""
			l={}
			for elem in metas:
				l[elem["name"]]=elem["value"]
			return l
		def desformatearMetadatos(self,metas):
			"""
			se pasa los metas como:
			{"meta":"valor"}
			y retorna 
			[{"nombre":"meta","value":"valor"}]
			"""
			l=[]

			if type(metas)==dict:
				for elem in metas:
					l.append({"name":elem,"value":metas[elem]})
			elif type(metas)==list:
				return metas
			return l
		def formatearListaMetadatos(self,metas):
			l=[]
			for elem in metas:
				d={}
				for meta in elem[1]:
					d[meta["name"]]=meta["value"]
				l.append(d)
			return l
		def modificarMetadatos(self,fila,meta,tabla=None):
			if self.request():	
				if type(meta)==list and type(meta[0])==dict and (list(meta[0])==["name","value"] or list(meta[0])==["value","name"]):
					if tabla==None and self.db.seleccion!=None:

							tabla=self.db.seleccion
					self.db(tabla).modificarCampo(fila,"Status",meta)
					self.grabar()
		def insertarCampoFormateado(self,titulo,data,args,metadatos=[],tabla=None):
			"""
			Este metodo sirve para insertar datos con el formato standar de ZDB
			"""
			if self.request():
				if tabla==None:
					tabla=self.db.seleccion
				i=len(self.obtenerFilas(tabla))
				self.insertar(titulo,
					data,
					{args:i},
					zu.DateTime(),
					metadatos)
				self.grabar()
		def valorizarContenido(self,data,estructura,request=False):
			agregados=[]
			for k,seccion in enumerate(estructura):
				if type(seccion)==list:

					for k2,campo in enumerate(seccion):

						if type(campo)==dict:
								if campo["name"] not in agregados:

									cuantos=self.contarNombres(campo["name"],seccion)

									c=0
									ind=0
									if type(data[campo["name"]])==list:
									 
										while cuantos+c<len(data[campo["name"]]):
										 	seccion.insert(k2+cuantos,campo)
										 	c+=1
						
										seccion[k2]["value"]=normalizar(data[campo["name"]][ind].value if request else data[campo["name"]][ind])
										ind+=1
										agregados.append(campo["name"])
									else:

										seccion[k2]["value"]=normalizar(data[campo["name"]].value if request else data[campo["name"]])



								else:

									if type(data[campo["name"]])==list:
										


										seccion[k2]["value"]=normalizar(data[campo["name"]][ind].value if request else data[campo["name"]][ind])
										ind+=1

				estructura[k]=seccion								

				"""
				elif type(seccion)==dict:

					if estructura[k]["name"]==seccion[k]["name"]:
						estructura[k]["value"]=(data[seccion[k]["name"]].value if request else data[seccion[k]["name"]])
				"""
			return estructura
		def valorizarEstructura(self,data,estructura,metadatos=None,request=False):
			
			estructura[0]=(data["titulo"].value if request else data["titulo"])

			self.valorizarContenido(data,estructura[1],request)
			if metadatos!=None:
				estructura[4]=self.desformatearMetadatos(metadatos)
			return estructura



		def formatear_personalizados(self,data):
			"""
			tipo:nombre
			"""
			l=[]
			for seccion in data:
				if type(seccion)==list:
					l2=[]
					for campo in seccion:
						if ":" in campo["name"]:
							custom=campo["name"].split(":")
							if len(custom)==2:
								l2.append({custom[0].capitalize():custom[0],"name":custom[0],"value":campo["value"]})
					l.append(l2)
				elif type(seccion)==dict:
					if ":" in seccion["name"]:
						custom=seccion["name"].split(":")
						if len(custom)==2:
							l.append({custom[0].capitalize():custom[0],"name":custom[0],"value":campo["value"]})
			return l



		def obtenerEstructura(self,nombre,tabla="Plantillas"):
			for elem in self.obtenerFilas(tabla):
				if elem[0]==nombre:
					return elem
		def contarNombres(self,nombre,contenido):
			c=0
			for elem in contenido:
				if elem["name"]==nombre:
					c+=1
			return c
		def actualizarContenido(self,indice,data,metadatos=None,tabla=None):
			"""
			sirve para actualizar el contenido segun el formato estandar del ZDB
			"""	
			import zu
			

			if self.request():
				if tabla==None:
					tabla=self.db.seleccion


				contenido=self.obtenerFilas(tabla)[indice][1]
				agregados=[]

				
				for k,seccion in enumerate(contenido):
					
					
					if type(seccion)==list:

						
						for k2,campo in enumerate(seccion):
							tmp=list(campo)
							
							
							tmp.remove("name") if "name" in tmp else tmp
							tmp.remove("value") if "value" in tmp else tmp
							tmp.remove("step") if "step" in tmp else tmp
							tmp.remove("opcion") if "opcion" in tmp else tmp
							tmp.remove("requerido") if "requerido" in tmp else tmp
							tmp.remove("tabla") if "tabla" in tmp else tmp
							tmp.remove("depende") if "depende" in tmp else tmp
							tmp.remove("categoria") if "categoria" in tmp else tmp
							tmp.remove("descripcion") if "descripcion" in tmp else tmp
							tmp.remove("opciones") if "opciones" in tmp else tmp
							tmp.remove("padre") if "padre" in tmp else tmp
							tmp.remove("carpeta") if "carpeta" in tmp else tmp
							tmp=tmp[0]	

							if campo["name"]=="titulo":

								titulo=data[campo["name"]].value



							if campo["name"] not in agregados:

								cuantos=self.contarNombres(campo["name"],seccion)

								c=0
								ind=0

								if type(data[campo["name"]])==list:
								 	
									while cuantos+c<len(data[campo["name"]]):
									 	seccion.insert(k2+cuantos,campo)
									 	c+=1
						
									seccion[k2]["value"]=normalizar(data[campo["name"]][ind].value)
									ind+=1
									agregados.append(campo["name"])
								else:
									seccion[k2]["value"]=normalizar(data[campo["name"]].value)



							else:

								if type(data[campo["name"]])==list:
									


									seccion[k2]["value"]=normalizar(data[campo["name"]][ind].value)
									ind+=1



							
													
					else:
						tmp=list(seccion)
						tmp.remove("name") if "name" in tmp else tmp
						tmp.remove("value") if "value" in tmp else tmp
						tmp.remove("step") if "step" in tmp else tmp
						tmp.remove("opcion") if "opcion" in tmp else tmp
						tmp.remove("requerido") if "requerido" in tmp else tmp
						tmp.remove("tabla") if "tabla" in tmp else tmp
						tmp.remove("depende") if "depende" in tmp else tmp
						tmp.remove("categoria") if "categoria" in tmp else tmp
						tmp.remove("descripcion") if "descripcion" in tmp else tmp
						tmp.remove("opciones") if "opciones" in tmp else tmp
						tmp.remove("padre") if "padre" in tmp else tmp
						tmp.remove("carpeta") if "carpeta" in tmp else tmp
						tmp=tmp[0]
						
						if seccion["name"]=="titulo":
							titulo=data[seccion["name"]].value
						
						if seccion["name"] not in agregados:
							 cuantos=self.contarNombres(seccion["name"],contenido)
							 c=0
							 while cuantos+c<len(data[seccion["name"]]):
							 	contenido.insert(k2+cuantos,campo)
							 	c+=1
							 agregados.append(seccion["name"])
						

						
						seccion["value"]=normalizar(data[seccion["name"]].value)
					
					contenido[k]=seccion
					

				
				
				self.db(tabla).modificarCampo(indice,"Nombre",titulo)
				self.db(tabla).modificarCampo(indice,"Contenido",
					contenido)

				self.db(tabla).modificarCampo(indice,"Fecha",
						zu.DateTime())

				if metadatos!=None:

					self.db(tabla).modificarCampo(indice,"Status",
						self.fusionarMetadatos(self.obtenerFilas(tabla)[indice][4],metadatos))

				self.grabar()
				
		def fusionarMetadatos(self,oldmetas,metas):
			"""
			este metodo trabaja sobre los datos reales y no sobre una copia
			es para fusionar metadatos con formato:
			[{"name":"nombre":"value":"valor"}] con {"nombre":"valor"}

			"""
			for meta in metas:
				for k,elem in enumerate(oldmetas):

					if meta==elem["name"]:
						oldmetas[k]["value"]=metas[meta]
						break
				else:
					oldmetas.append({"name":meta,"value":metas[meta]})

					pass
			
			return oldmetas
				
					

		def updateMetadatos(self,fila,meta,tabla=None):
			
			if self.request():
				if type(meta)==dict and (list(meta)==["name","value"] or list(meta)==["value","name"]):
					if tabla==None and self.db.seleccion!=None:
							tabla=self.db.seleccion
					metas=self.db(tabla).obtenerFilas(tabla)[fila]
					for k,elem in enumerate(metas):
						if elem["name"]==meta["name"]:
							metas[k]["value"]=meta["value"]
							break
					else:
						metas.append(meta)
					self.db(tabla).modificarCampo(fila,"Status",metas)
					self.grabar()
				elif type(meta)==list and (list(meta[0])==["name","value"] or list(meta[0])==["value","name"]):
					if tabla==None and self.db.seleccion!=None:
							tabla=self.db.seleccion
					metas=self.db(tabla).obtenerFilas(tabla)[fila]
					for k,elem in enumerate(meta):
						for k2,elem2 in enumerate(metas):
							if elem2["name"]==elem["name"]:
								metas[k2]["value"]=elem["value"]
								break
						else:
							metas.append(elem)
					self.db(tabla).modificarCampo(fila,"Status",metas)
					self.grabar()






		def request(self,dbfile=None,metodo=None):
			if dbfile!=None:
				self.dbfile=dbfile
			#espera a tener un listado de archivos
			#se mantiene en espera si se esta utilizando la base de datos
			import time
			tiempo=time.time()
			if "ordenDB.py" in os.listdir(self.resquest_folder):
				while "ordenDB.py" in os.listdir(self.resquest_folder):
					# Es normar que tarde ya que serian 5 segundos por cada operacion incompleta
					if time.time()-tiempo>5:
						for elem in os.listdir(self.resquest_folder):
							os.remove(self.resquest_folder+elem)
						break
			
			f=open(self.resquest_folder+"ordenDB.py","w")
			if metodo!=None:
				f.write("Modelo: "+str(metodo.__module__)+"\nmetodo: "+str(metodo.func_name))
			f.close()
			self.update(self.dbfile)
			
			return True
		def obtenerLongitud(self,tabla=None):
			if self.update():
				if tabla==None:
					tabla=self.db.seleccion
				return len(self.db.tablas[tabla])

		def obtenerFilas(self,tabla):
				if self.update():
					
					return self.db(tabla).obtenerFilasValores()
					
		def contener(self,contenido):
				content={}

				if type(contenido)==list:
					for k,elem in enumerate(contenido):
						
						if type(elem)==list:
							content[k]=self.contener(elem)
						elif type(elem)==dict:
							content[elem["name"]]=elem
				
				return content
		def modificarContenido(self,sinFormato,conFormato):
			for k,elem in enumerate(sinFormato):
				if type(elem)==list:
					sinFormato[k]=self.modificarContenido(elem,conFormato[k])
				elif type(elem)==dict:
					sinFormato["value"]=conFormato["name"].value
			return sinFormato

		def obtenerContenido(self,fila,tabla=None):
			"""
			Este metodo es para navegar atraves de la tabla como se hacen con los diccionarios
			valido para la estructura de tablas de asenzor 
			"""
			if tabla==None:
				tabla=self.db.seleccion
			if self.update():
				_tabla={}
				if type(fila)==int:
					_tabla[self.obtenerFilas(tabla)[fila][0]]=self.contener(self.obtenerFilas(tabla)[fila][1])

				else:
					for elem in self.obtenerFilas(tabla):
						if elem[0]==fila:
							_tabla[elem[0]]=self.contener(elem[1])
				return _tabla

					

except Exception as e:
	print "zmodel error: " ,e