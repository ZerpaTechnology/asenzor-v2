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


		def modificarPagina(self,indice,data,metadatos=None):
			
			self.actualizarContenido(indice,data,metadatos,"Paginas")

		def crearEntrada(self,data,metadatos=None):
			if self.request():
				nuevo=self.valorizarEstructura(data,self.obtenerEstructura("Entradas"))
				nuevo[2]={"Entrada":self.obtenerLongitud("Entradas")}
				nuevo[3]=zu.DateTime()
				self.fusionarMetadatos(nuevo[4],metadatos)
				self.db("Entradas").insertar(nuevo[0],nuevo[1],nuevo[2],nuevo[3],nuevo[4])
				self.grabar()

		def crearPagina(self,data,metadatos=None):
			if self.request(metodo=self.crearPagina.__func__):
				
				nuevo=self.valorizarEstructura(data,self.obtenerEstructura("Paginas"))
				nuevo[2]={"Pagina":self.obtenerLongitud("Paginas")}
				nuevo[3]=zu.DateTime()
				self.fusionarMetadatos(nuevo[4],metadatos)
				self.db("Paginas").insertar(nuevo[0],nuevo[1],nuevo[2],nuevo[3],nuevo[4])
				self.grabar()
			

		def modificarEntrada(self,indice,data,metadatos=None):
			self.actualizarContenido(indice,data,metadatos,"Entradas")
		def obtenerAttPag(self,name):
			
			if self.update():
				l=self.obtenerFilas("Paginas")
				options=self.obtenerFilas("Opciones")
				l2=[]
				for elem in l[1]:
					if type(elem)==dict:
						tmp=elem.keys()
						tmp.remove("name") if "name" in tmp else tmp
						tmp.remove("opcion") if "opcion" in tmp else tmp
						tmp.remove("value") if "value" in tmp else tmp
						if elem[tmp]=="select" and tmp==name:
							return options[elem["opcion"]][1][elem["value"]]
						elif tmp==name:
							return elem["value"]
					elif type(elem)==list:
						l3=[]
						for sub in elem:
							if type(sub)==dict:
								tmp=sub.keys()
								tmp.remove("name") if "name" in tmp else tmp
								tmp.remove("opcion") if "opcion" in tmp else tmp
								tmp.remove("value") if "value" in tmp else tmp
								if elem[tmp]=="select" and tmp==name:
									return options[sub["opcion"]][1][sub["value"]]
								elif tmp==name:
									return sub["value"]

		




		def crearConfiguracionPagina(self,pagina,**kwargs):
			
			if self.request():
				campos=[]
				valores=[]
				for elem in kwargs:
					campos.append(elem)
					valores.append(kwargs)
				self.db("Paginas").insertar(pagina,campos,valores,zu.DateTime())
				self.grabar()

		def modificarConfiguracionPagina(pagina,**kwargs):

			
			if self.request():

				campos=[]
				valores=[]
				for elem in kwargs:
					campos.append(elem)
					valores.append(kwargs)

				_id=self.db("Paginas").obtenerColumna("Nombre").index(Pagina)
				self.db("Paginas").modificarFila(_id,pagina,campos,valores)
				self.grabar()
		



		def eliminar(self,c,tabla):
			if self.request():
				self.db(tabla).delFila(c)
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



		def borrarConfiguracionPagina(self,pagina,**kwargs):
			if self.request():
				campos=[]
				valores=[]
				for elem in kwargs:
					campos.append(elem)
					valores.append(kwargs)
				_id=self.db("Paginas").obtenerColumna("Nombre").index(Pagina)
				self.db("Paginas").modificarFila(_id,pagina,campos,valores)
				self.grabar()





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