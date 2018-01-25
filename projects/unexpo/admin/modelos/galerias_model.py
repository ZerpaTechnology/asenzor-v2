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
		
		def crearGaleria(self,nombre,imagenes):
			if self.request():
				imgs=[{"Galeria":"text","name":"galeria","value":nombre}]
				for elem in imagenes:
					imgs.append({"Imagen 10":"select","name":"img","value":elem,"opcion":0})

				self.db("Galerias").insertar(nombre,
					imgs,
					{"Galeria":len(self.obtenerFilas("Galerias"))-1},
					zu.DateTime(),
					[]
					)
				self.grabar()
				return True
		def eliminarGaleria(self,indice):
			if self.request():
				tabla="Galerias"
				if len(self.obtenerFilas(tabla))>0:
					self.db(tabla).delFila(indice)
					self.grabar()
					return True
				else:
					return False

			
		
		def modificarGaleria(self,indice,nombre,imagenes):
			import shutil
			import Image
			if self.request():
				filas=self.obtenerFilas("Galerias")[indice][1][0][1:]

				self.db("Galerias").modificarCampo(indice,"Nombre",
					nombre
					)
				imgs=[[{"Galeria":"text","name":"galeria","value":nombre}]]
				options=self.obtenerFilas("Opciones")
				for k,elem in enumerate(imagenes):
					if k>len(filas)-1:
						current=imagenes[k]

						shutil.move(os.getcwd()+"/apps/"+settings.app+"/admin/static/archivos/"+current,os.getcwd()+"/apps/"+settings.app+"/admin/static/archivos/Galerias/"+current)
						im1 = Image.open(os.getcwd()+"/apps/"+settings.app+"/admin/static/archivos/Galerias/"+current)
						width=500
						height=420
						img=im1.resize((width, height), Image.NEAREST)
						img.save(os.getcwd()+"/apps/"+settings.app+"/admin/static/archivos/Galerias/min/"+current)

					

					imgs[0].append({"Imagen "+str(k+1):"select","name":"img","value":options[0][1].index(elem),"opcion":0})

				self.db("Galerias").modificarCampo(indice,"Contenido",
					imgs
					)
				self.db("Galerias").modificarCampo(indice,"Fecha",
					zu.DateTime(),
					[]
					)
				return  self.grabar()
		
		def reportarError(self,errores):
			"""
			error=[[[exc_type,exc_obj,exc_tb],[direccion]],]
			"""
			if self.request():
				msj=""
				tabla=self.obtenerFilas("Log")

				import traceback
				import os
				
				lineascod=[]

				for error in errores:
					
					
					lineas=[]
					
					cuenta=0
					for linea in traceback.format_exception(error[0][0],error[0][1],error[0][2]):
						if "line" in linea:
							lineas.append(int(linea.split(",")[1].replace(" line ","")))

							cuenta=linea.count("<string>")
					msj+="".join(traceback.format_exception(error[0][0],error[0][1],error[0][2]))
					i=0

 					print lineas

					for v in range(cuenta+1):
						

						i=msj.find("<string>",i+1)
						if i+len("<string>")< len(msj):

							msj=msj[:i]+error[1][v]+msj[i+len("<string>"):]
						else:

							msj=msj[:i]+error[1][v]

						
						f=open(os.path.abspath(error[1][v]),"r")
						rlineas=f.readlines()
						
						
						lineascod.append(rlineas[lineas[v]-1])


						f.close()


				

				
				token=zu.randomString()
				anteriores=[]

				for elem in tabla:
					anteriores.append(elem[0])

				while token in anteriores:
					token=zu.randomString()
				i=0
				cuenta=msj.count("\n")-1

				
				for salto in range(cuenta-1):
					i=msj.find("\n",i+1)
					i=msj.find("\n",i+1)

					try:
						msj=msj[:i]+"\n\n"+lineascod[salto]+msj[i:]
						i=msj.find("\n",i+1)
						i=msj.find("\n",i+1)
					except:
						if salto<len(lineascod)-1:
							msj=msj[:i]+"\n\n"+lineascod[salto]
				print tabla[-1][1]	
				if tabla!=[] and tabla[-1][1]!=msj:
					
					self.db("Log").insertar(str(token),
						msj,
						{"Error":len(tabla)},
						zu.DateTime(),
						False
						)

					return [self.grabar(),token]
				elif tabla==[]:

					
					self.db("Log").insertar(str(token),
						msj,
						{"Error":len(tabla)},
						zu.DateTime(),
						False
						)

					return [self.grabar(),token]
				else:

					return [self.grabar(),tabla[-1][0]]

				

		def buscarError(self,token):
			if self.update():
				for elem in self.obtenerFilas("Log"):
					if elem[0]==token:
						return elem
				
		def corregirError(self,indice):
			if self.request():
				self.db("Log").modificarCampo(indice,"Status",True)
				self.grabar()

		def limpiarErrores(self):
			if self.request():
				for k,elem in enumerate(self.obtenerFilas("Log")):
					self.db("Log").delFila(k)
				self.db("Log").id(0)
				self.grabar()



		
		def borrarFila(self,c,tabla):
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

		
		def obtenerGaleria(self,galeria):
			if self.update():
				return self.obtenerFilas("Galerias")[galeria]
			

				
		
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
	
		def closeSession(self,token):
			if self.request():
				filas=self.db("usuarios").obtenerFilasValores(token)
				if filas[6]==token:
					self.db("usuarios").modificarCampo(self.db("usuarios").obtenerFilasId(token)[0],"login",False)
					newToken=zu.randomString()
					while newToken in self.db.obtenerColumna("valor","tokens"):
						newToken=zu.randomString()
					self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(token)[0],"valor",newToken)
					return self.grabar()
					
				else:
					return False


except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e