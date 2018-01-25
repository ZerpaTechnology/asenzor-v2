#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from modulos.ztec.zmodel import Model
import sys
import os
import datetime
import modulos.ztec.zu as zu
from modulos.ztec.zred import sufijar

sys.path.append("../")

if "settings" not in dir():
	from settings import config as settings
if "config" not in dir():
	try:
		import config.config as config
	except:
		import config

try:

	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		
		def crearPlantilla(self,nombre,campos):
			if self.request():
				tabla="Plantillas"
				i=len(self.obtenerFilas(tabla))
				self.db(tabla).insertar(nombre,
					campos,
					{"Plantilla":i},
					zu.DateTime(),
					["Publicada"]
					)
				return self.grabar()
		def modificarPlantilla(self,i,nombre,campos):
			if self.request():
				tabla="Plantillas"
				self.db(tabla).modificarCampo(i,"Nombre",nombre)
				self.db(tabla).modificarCampo(i,"Contenido",campos)
				self.db(tabla).modificarCampo(i,"Fecha",zu.DateTime())
				return self.grabar()

		def subirArchivo(self,data,metadatos=None):
			
			if self.request():
				tabla="Opciones"
				existe=True
				import os

				
				opciones=self.obtenerFilas(tabla)

				archivo=data["archivo"]
				

				for k,elem in enumerate(opciones):
					
					if elem[0]=="Categorias":
							tipo=opciones[k][1][int(data["tipo"].value)]
					elif elem[0]=="Archivos":
						opcion=opciones[k][1][int(data["opcion"].value)]
			


				if type(archivo)==list:
					for elem in archivo:
						
						if elem.filename!="":


							renombre=data["renombre"].value+elem.filename[elem.filename.find("."):] if "renombre" in data and data["renombre"].value!="" else elem.filename

							i=len(self.obtenerFilas("Archivos"))
							if tipo not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"):
								
								os.mkdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo)
							

							if renombre not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo) or ("sobrescribir" in data and data["sobrescribir"].value=="on"):
								#self.db(tabla).modificarCampo(opcion,"Valores",l+[renombre+"."+archivo.filename.split(".")[1]])

								f=open(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre,"w")
								f.write(elem.file.read())
								f.close()		
								optimizar(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre)				

							else:
								existe=False

							
							if existe==True:
								l=self.obtenerFilas("Opciones")[0][1]


								l=l+[renombre]
		                                                
								self.db("Opciones").modificarCampo(0,"Valores",l)
								self.db("Archivos").insertar(renombre,
										[
											[
											{"Imagen":"img-admin","name":"archivo","value":len(l)-1,"opcion":0,'opciones': 'archivos'},
											{"Título":"text","name":"renombre","value":renombre},							
											{"Enlace":"text","name":"enlace","value":config.base_url+config.apps_folder+settings.app+"/admin/static/archivos/"+data["tipo"].value+"/"+elem.filename},
											{"Típo":"text","name":"tipo","value":data["opcion"].value},
											]
										],
										{"Archivo":i},
										zu.DateTime(),
										[]
										)
								
								
							

				else:


					if archivo.filename!="":

						renombre=data["renombre"].value+archivo.filename[archivo.filename.find("."):] if "renombre" in data and data["renombre"].value!="" else archivo.filename

						i=len(self.obtenerFilas("Archivos"))

						if tipo not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"):
							
							os.mkdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo)
	
						if renombre not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo) or ("sobrescribir" in data and data["sobrescribir"].value=="on"):
							#self.db(tabla).modificarCampo(opcion,"Valores",l+[renombre+"."+archivo.filename.split(".")[1]])
							f=open(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre,"w")
							f.write(archivo.file.read())
							f.close()	
							try:
								from modulos.ztec.zgrafic import thumbails,optimizar
								thumbails(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre)
								optimizar(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre)
							except Exception as e:
									print e					
						else:
							existe=False


						if existe==True:
							l=self.obtenerFilas("Opciones")[0][1]


							l=l+[renombre]
	                                                
							self.db("Opciones").modificarCampo(0,"Valores",l)
							self.db("Archivos").insertar(renombre,
									[
										[
										{"Imagen":"img-admin","name":"archivo","value":len(l)-1,"opcion":0,'opciones': 'archivos'},
										{"Título":"text","name":"renombre","value":renombre},							
										{"Enlace":"text","name":"enlace","value":config.base_url+config.apps_folder+settings.app+"/admin/static/archivos/"+data["tipo"].value+"/"+archivo.filename},
										{"Típo":"text","name":"tipo","value":data["opcion"].value},
										]
									],
									{"Archivo":i},
									zu.DateTime(),
									[]
									)
							
							
						
				self.grabar()
				return True
					
		def actualizarArchivo(self,indice,data,metadatos=None):
			
			if self.request() and data["archivo"].filename!="":
				tabla="Opciones"
				existe=True
				import os
				import copy

				
				opciones=self.obtenerFilas(tabla)
				for k,elem in enumerate(opciones):
					
					if elem[0]=="Categorias":
							tipo=opciones[k][1][int(data["tipo"].value)]

				archivo=data["archivo"]
				

				renombre=data["renombre"].value

				i=len(self.obtenerFilas("Archivos"))

				
				f=open(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre,"w")
				f.write(archivo.file.read())
				f.close()
				l=self.obtenerFilas("Archivos")[int(indice)][1]
				for seccion in l:
						for campo in seccion:
							if campo["name"]=="archivo":
								anterior=copy.copy(campo["value"])
								campo["value"]=renombre
								try:
									from modulos.ztec.zgrafic import thumbails
									thumbails(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre)
									optimizar(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+renombre)
								except Exception as e:
									print e

				if renombre not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo) and anterior in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo):
					os.remove(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+tipo+"/"+anterior)
				self.db("Archivos").modificarCampo(int(indice),"Contenido",l)
				self.grabar()
				return True
		def eliminar(self,c,tabla):
			if self.request():
				if tabla=="Archivos":
					content=self.obtenerContenido(c,tabla)
					content=content[list(content)[0]]

					self.db(tabla).delFila(c)
					self.grabar()
					l=self.obtenerFilas("Opciones")
					for k,elem in enumerate(l):
						if elem[0]=="Imagenes":
							if content[0]["renombre"]["value"] in elem[1]:
								elem[1].remove(content[0]["renombre"]["value"])
								self.db("Opciones").modificarCampo(k,"Valores",elem[1])
								if content[0]["renombre"]["value"] in os.listdir("../"+config.apps_folder+settings.app+"/admin/static/archivos/Imagenes/"):
									os.remove("../"+config.apps_folder+settings.app+"/admin/static/archivos/Imagenes/"+content[0]["renombre"]["value"])
							break

				return self.grabar()
		def obtenerFilas(self,tabla):
			if self.update():
				c=0
				l=[]
				if tabla in self.db.tablas:
					try:
						while True:
				
							l.append(self.db(tabla).obtenerFilaValores(c))
							c+=1					
					except:

						return l




		def filtrar(self,status,tabla=None):
			#status=["activo"] todos los que tenga activo
			#status=["activo","aprobado"] todos los que tengan activo y aprodado no uno solo
			
			if self.update():	
				l2=[]

				if tabla!=None and type(tabla)!=str:
					l=tabla
				elif type(tabla)==str:
					l=self.obtenerFilas(tabla)
				else:
					l=self.obtenerFilas(self.db.seleccion)

				for k,fila in enumerate(l):
					if len(status)==1:
						for estado in status:
							if estado in fila[4]:
								l2.append(fila)

					else:
						pasa=True
						l3=[]


						for estado in status:
							if estado in fila[4]:
								l3.append(fila)
							else:
								pasa=False
						
						if pasa!=False:
							l2.extend(l3)
				


				return l2


					


		def ordenar(self,por="Fecha",ascendente=True,filtros=None):
			if por=="Fecha":
				formato=self.db.obtenerFormato("Fecha")

				l=[]
				for fila in self.obtenerFilas(self.db.seleccion):
					if l!=[]:
						

						if ascendente==True:
							if datetime.datetime.strptime(l[-1][3],formato)>=datetime.datetime.strptime(fila[3],formato):
								l.append(fila)

							else:
								l.insert(0,fila)

						else:

							if datetime.datetime.strptime(l[-1][3],formato)>=datetime.datetime.strptime(fila[3],formato):
								l.insert(0,fila)

							else:
								l.append(fila)

					else:
						l.append(fila)
				

			elif por=="Nombre":
				l=[]
				for fila in self.obtenerFilas(self.db.seleccion):
					if l!=[]:
						if ascendente==True:
							if zu.cmpString(l[-1][0],fila[0]):
								l.append(fila)
							else:
								l.insert(0,fila)

						else:
							if zu.cmpString(l[-1][0],fila[0]):
								l.insert(0,fila)
							else:
								l.append(fila)
					else:
						l.append(fila)
			


			else:
				pass

			if filtros!=None:
					return self.filtrar(filtros,l)
		def obtenerIdsFiltrados(self,lista):
			l=[]

			for elem in lista:
				

				clave=elem[2].keys()[0]
				l.append(elem[2][clave])
			return l
	

except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e