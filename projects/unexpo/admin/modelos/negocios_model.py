# -*- coding: utf-8 -*-
import os
from ztec.zmodel import Model
from ztec import zu
try:
	import config.config as config
except:
	import config
try:
	class model(Model):

		def registrarNegocio(self,nombre,email,direccion,categoria,subcategoria,especialidad,imagen,pais="Holanda",latitud=None,longitud=None,estrellas=None,horario=None,telefono=None,pago="Formas de pago",efectivo=0,visa=0,mastercard=0,web=None,notas=None):
			try:
				indice=len(self.obtenerFilas("Negocios"))
				if self.request():
						try:

							os.mkdir(config.base_root+config.apps_folder+"Atei/"+"user/static/archivos")
						except Exception as e:
							pass
						
						n=len(self.obtenerFilas("Negocios"))
						self.db("Negocios").insertar(nombre,
						[
						{"Nombre":"text","value":nombre,"name":"nombre","requerido":True},
						{"Email":"text","value":email,"name":"email","requerido":True},
						{"País":"fixed","value":"Holanda","name":"pais"},
						{"Dirección":"text","value":direccion,"name":"pais","requerido":True},
						{"Categoria":"select","value":1,"name":categoria,"requerido":True, "subtabla":"Categorias"},
						{"Subcategorias":"select","value":subcategoria,"name":"subcategoria","requerido":True,"seleccion":"Categorias"},
						{"Especialidad":"select","value":especialidad,"name":"especialidad","requerido":True,"categoria":"subcategoria"},
						{"Imagen":"select","value":imagen,"name":"imagen","requerido":True, "Selección":"Imagenes"},
						{"Latitud":"number","value":latitud,"name":"latitud","requerido":True,"step":0.0000001 },
						{"Longitud":"number","value":longitud,"name":"longitud","requerido":True,"step":0.0000001},
						{"Estrellas":"number","value":estrellas,"name":"estrellas","requerido":True,"step":0.1},
						[
						{"Horario":"text","value":horario["value"],"name":"estrellas","requerido":True},
						{"Lunes":"text","value":horario["lunes"],"name":"lunes","requerido":True},
						{"Martes":"text","value":horario["martes"],"name":"martes","requerido":True},
						{"Miercoles":"text","value":horario["miercoles"],"name":"miercoles","requerido":True},
						{"Jueves":"text","value":horario["jueves"],"name":"jueves","requerido":True},
						{"Viernes":"text","value":horario["viernes"],"name":"viernes","requerido":True},
						{"Sabado":"text","value":horario["sabado"],"name":"sabado","requerido":True},
						{"Domingo":"text","value":horario["domingo"],"name":"domingo","requerido":True},
						[
						{"Opciones de pago":"text","value":pago,"name":"pago"},
						{"Efectivo":"select","value":efectivo,"name":"efectivo","opciones":0},
						{"Visa":"select","value":visa,"name":"Visa","opciones":0},
						{"MasterCard":"select","value":mastercard,"name":"MasterCard","opciones":0},
						]
						],

						{"Pagina web":"text","value":web,"name":"web"},
						],
						{"Negocio":indice},
						zu.DateTime()
						)


						self.grabar()

			except Exception, e:
				print str(e)[1:-1]
		def modificarNegocio(self,indice,nombre,email,direccion,categoria,imagen,pais="Holanda",latitud=None,longitud=None,estrellas=None,horarios=None,telefono=None,web=None,notas=None):
			if self.request():
				tabla="Negocios"
				self.db(tabla).modificarCampo(indice,"Nombre",nombre)
				self.db(tabla).modificarCampo(indice,"Contenido",
					[
						{"Nombre":"text","value":nombre,"name":"nombre","requerido":True},
						{"Email":"text","value":email,"name":"email","requerido":True},
						{"País":"fixed","value":"Holanda","name":"pais"},
						{"Dirección":"text","value":direccion,"name":"pais","requerido":True},
						{"Categoria":"select","value":1,"name":categoria,"requerido":True, "subtabla":"Categorias"},
						{"Subcategorias":"select","value":subcategoria,"name":"subcategoria","requerido":True,"seleccion":"Categorias"},
						{"Imagen":"select","value":imagen,"name":"pais","requerido":True, "Selección":"Imagenes"},
						{"Latitud":"number","value":latitud,"name":"latitud","requerido":True,"step":0.0000001 },
						{"Longitud":"number","value":longitud,"name":"longitud","requerido":True,"step":0.0000001},
						{"Estrellas":"number","value":estrellas,"name":"estrellas","requerido":True,"step":0.1},
						[
						{"Horario":"text","value":horario,"name":"estrellas","requerido":True},
						{"Lunes":"text","value":lunes,"name":"lunes","requerido":True},
						{"Martes":"text","value":martes,"name":"martes","requerido":True},
						{"Miercoles":"text","value":miercoles,"name":"miercoles","requerido":True},
						{"Jueves":"text","value":jueves,"name":"jueves","requerido":True},
						{"Viernes":"text","value":viernes,"name":"viernes","requerido":True},
						{"Sabado":"text","value":sabado,"name":"sabado","requerido":True},
						{"Domingo":"text","value":domingo,"name":"domingo","requerido":True},
						[
						{"Opciones de pago":"text","value":pago,"name":"pago"},
						{"Efectivo":"select","value":efectivo,"name":"efectivo","opciones":0},
						{"Visa":"select","value":visa,"name":"Visa","opciones":0},
						{"MasterCard":"select","value":mastercard,"name":"MasterCard","opciones":0},
						]
						],

						{"Pagina web":"text","value":web,"name":"web"},
						]
					)
				self.db(tabla).modificarCampo(indice,"Fecha",zu.DateTime())
				self.grabar()
		def subirArchivo(self,archivo,renombre):
			
			if self.request():
				tabla="Opciones"
				existe=True



				l=self.db(tabla).obtenerFilaValores(0)[1]
				i=len(self.obtenerFilas("Archivos"))
				if renombre!="":
					if renombre not in os.listdir(config.base_root+config.apps_folder+"CBK/admin/static/archivos/"):
						l.append(renombre)
						self.db(tabla).modificarCampo(0,"Valores",l)
						f=open(config.base_root+config.apps_folder+"ATEI/admin/static/archivos/"+renombre,"w")
						f.write(archivo.file.read())
						f.close()
						imagenes=self.obtenerFilas("Imagenes")
						self.db("Imagenes").modificarCampo("Valores",imagenes[0][1].append(renombre))
					else:
						existe=False
				else:
					if archivo.filename not in os.listdir(config.base_root+config.apps_folder+"CBK/admin/static/archivos/"):
						l.append(archivo.filename)
						self.db(tabla).modificarCampo(0,"Valores",l)
						f=open(config.base_root+config.apps_folder+"ATEI/admin/static/archivos/"+archivo.filename,"w")
						f.write(archivo.file.read())
						f.close()
						imagenes=self.obtenerFilas("Imagenes")
						self.db("Imagenes").modificarCampo("Valores",imagenes[0][1].append(archivo.filename))
					else:
						existe=False
				if existe==True:
					self.db("Archivos").insertar(archivo.filename,
							[
								[
								{"Imagen":"file","name":"archivo","value":archivo.filename},
								{"Título":"text","name":"renombe","value":renombre},							
								]
							],
							{"Archivo":i},
							zu.DateTime()
							)
					

					self.grabar()
					return True
				else:
					return False

		def obtenerSubcategorias(self,categoria):
			if self.update():
				l=[]
				categorias=self.obtenerFilas("Categorias")
				for fila in categorias:
					
					if fila[0]==categoria:
						l.append(fila[1])
				return l
		def obtenerSubcategoriasOpciones(self,categoria,subcategoria):
			if self.update():
				categorias=self.obtenerFilas("Categorias")
				for fila in categorias:
					if fila[0]==categoria and fila[1]==subcategoria:
						if type(fila[2])==list:
							return fila[2]
				


		def eliminarNegocio(self,_id):
			
			if self.request():
				if len(self.obtenerFilas("Negocios"))>1:
					self.db("Negocios").delFila(_id)

				self.grabar()

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
			
except Exception, e:
	if config.mod_debug==False:
		print "error en negocios_model<br>"
		print e