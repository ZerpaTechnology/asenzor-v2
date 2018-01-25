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
from config import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		

		def crearMenu(self,nombre,estructura):

			if self.request():
				tabla="Menus"

				i=len(self.obtenerFilas(tabla))

				self.db(tabla).insertar(nombre,
					estructura,
					{"Menu":i},
					zu.DateTime(),
					["Publicada"])
				
				print "\n=================\n"
				return self.grabar()

		def modificarMenu(self,indice,nombre,estructura):
			if self.request():
				tabla="Menus"
				self.db(tabla).modificarCampo(indice,"Nombre",nombre)
				self.db(tabla).modificarCampo(indice,"Contenido",estructura)
				menus=self.obtenerFilas("Menus")
				for k, elem in enumerate(menus):
					if k!=indice:
						for clave in estructura[1]:
							if estructura[1][clave]!=elem[1][1][clave] and estructura[1][clave]==True:
								menus[k][1][1][clave]=False
						self.db(tabla).modificarCampo(k,"Contenido",menus[k][1])
						self.db(tabla).modificarCampo(k,"Fecha",zu.DateTime())
				self.db(tabla).modificarCampo(indice,"Fecha",zu.DateTime())
				
				return self.grabar()
		def obtenerMenu(self,posicion):#top,main,foot,my_count

			if self.update():

				menus=self.obtenerFilas("Menus")

				for k,menu in enumerate(menus):
					if posicion=="top":
						if menus[1][1][1]['menu-barra-superior']:
							return menu
					elif posicion=="main":
						
						if menus[k][1][1]['menu-principal']:
							return menu
					elif posicion=="foot":
						if menus[k][1][1]['menu-pie']:
							return menu
					elif posicion=="my_count":
						if menus[k][1][1]['menu-mi-cuenta']:
							return menu



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