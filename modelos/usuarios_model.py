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
		
		def registrarUsuario(self,nick,email,password,avatar,permisologia,hours=4):
		
			if self.request():
				import datetime
				muere=str(zu.DateTime(H=hours))
				x = datetime.datetime.now()
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				if permisologia<self.data["user"]["permisologia"]:
					permisologia=self.data["user"]["permisologia"]
				
				i=len(usuarios)

				if self.models["global"].isUser(email)==False:

					while valido==None:
						token=zu.randomString()
						for fila in usuarios:
							for campos in fila[1][0]:
								keys=campos.keys()
								if "Email" in keys:
									if email==campos["value"]:
										valido=False
								elif "Token" in keys:
									if token==campos["value"]:
										valido=False
						if valido==None:
							valido=True
						else:
							valido=None

					self.db("Usuarios").insertar(nick,
							[[
							 {"Usuario":"text","name":"usuario","value":nick},
							 {"Email":"text","name":"email","value":email},
							 {"Password":"text","name":"password","value":password},
							 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1,"opciones":"archivos"},
							 {"Token":"hidden","name":"token","value":token},
							 {"Muere":"hidden","name":"muere","value":muere},
							 {"Login":"hidden","name":"login","value":True},
							 {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': permisologia, 'Permisologia': 'select'}
							]],
							{"Usuario":i},
						   zu.DateTime(),
						   [],
						   )
					self.grabar()
					
					return True
				else:
					return False



		def modificarUsuario(self,indice,nick,email,password,avatar,permisologia,hours=4):
			
			if self.request():
				import datetime
				muere=str(zu.DateTime(H=hours))
				x = datetime.datetime.now()
				user_current=None

				if permisologia<self.data["user"]["permisologia"]:
					permisologia=self.data["user"]["permisologia"]

				
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				l=[]
				i=0
				for k,fila in enumerate(usuarios):
					i=k
					for campos in fila[1][0]:
						if campos["name"]=="email":
							if email==campos["value"]:
								valido=False
								l.append(fila[1][0])
								break
					if valido==False:
						break

				valido=None
				token=l[0][4]["value"]


				self.db("Usuarios").modificarCampo(indice,"Nombre",nick)
				
				self.db("Usuarios").modificarCampo(indice,"Contenido",
						[[
						 {"Usuario":"text","name":"usuario","value":nick},
						 {"Email":"text","name":"email","value":email},
						 {"Password":"text","name":"password","value":password},
						 {"Avatar":"img-admin","name":"avatar","value":int(avatar),"opcion":1,"opciones":"archivos","carpeta":"Avatares"},
						 {"Token":"hidden","name":"token","value":token},
						 {"Muere":"hidden","name":"muere","value":muere},
						 {"Login":"hidden","name":"login","value":True},
						 {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': permisologia, 'Permisologia': 'select'},
						]])
				self.db("Usuarios").modificarCampo(indice,"args",
						{"Usuario":indice}
						)
				self.db("Usuarios").modificarCampo(indice,"Fecha",
					   zu.DateTime(),
					   )

				return self.grabar()
				
		def login(self,email,password):


			if self.request():
				
				muere=str(zu.DateTime(H=1))
				
				valido=None
				
				usuarios=self.obtenerFilas("Usuarios")

				
				usuarios2=self.models["global"].obtenerFilas("Usuarios")
				c=0

				
				

				i=0
				l=[]

				for k,fila in enumerate(usuarios):
					
					i=k
					
					for campos in fila[1][0]:
						keys=campos.keys()
						if "Email" in keys:
							
							if email==campos["value"]:
								valido=False
								l.append(fila[1][0])

								break
					if valido==False:
						break
				valido=None				

				if l!=[] and l[0][1]["value"]==email and l[0][2]["value"]==password:
					
					nick=l[0][0]["value"]
					avatar=l[0][3]["value"]
					permisologia=l[0][7]["value"]
					while valido!=True:
						pasa=True

						token=zu.randomString()
						for fila in usuarios:
							if token==fila[1][0][4]["value"]:
								pasa=False
						for fila in usuarios2:
							if token==fila[1][0][4]["value"]:
								pasa=False

						if pasa==True:
							valido=True
					

					self.db("Usuarios").modificarCampo(i,"Contenido",
							[[
							 {"Usuario":"text","name":"usuario","value":nick},
							 {"Email":"text","name":"email","value":email},
							 {"Password":"text","name":"password","value":password},
							 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1,"opciones":"archivos"},
							 {"Token":"hidden","name":"token","value":token},
							 {"Muere":"hidden","name":"muere","value":muere},
							 {"Login":"hidden","name":"login","value":True},
							 {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': permisologia, 'Permisologia': 'select'},
							]]
							)
			
					self.grabar()
					
					return token
				else:
					return False
			

		def isUser(self,email=None,token=None):
			if self.update():
				usuarios=self.obtenerFilas("Usuarios")
				if token==None and email!=None:
					for k,fila in enumerate(usuarios):
						for campos in fila[1][0]:
							keys=campos.keys()
							if "Email" in keys:
								if email==campos["value"]:
									return True
				else:
					for k,fila in enumerate(usuarios):
						for campos in fila[1][0]:
							keys=campos.keys()
							if "Token" in keys:
								if token==campos["value"]:
									return True

				return False
		def getUser(self,token):
			if self.update():
				
				x = datetime.datetime.now()
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				i=[]
				l={}
				
				
				for k, fila in enumerate(usuarios):
					i=k

					for campos in fila[1][0]:


						keys=campos.keys()
						if "Token" in keys:


							if token==campos["value"]:


								valido=False
								for elem in fila[1][0]:

									l[elem["name"]]=elem["value"]

								
								break
					if valido==False:
						break
				
				return l
				

		def obtenerUsuario(self,token):
			if self.update():
				tabla={}
				for usuario in self.obtenerFilas("Usuarios"):
					
					if usuario[1][0][4]["value"]==token:
						for elem in usuario[1][0]:
							tabla[elem["name"]]=elem["value"]
				return tabla
				


		def closeSession(self,token):
			
			if self.request():
				import datetime

				muere=str(zu.DateTime())
				x = datetime.datetime.now()
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				i=0
				l=[]
				l2=[]

				
				for k,fila in enumerate(usuarios):
					

					for campos in fila[1][0]:
						keys=campos.keys()
						if "Token" in keys:
							if token==campos["value"]:
								valido=False
								l.append(fila[1][0])
								break
					i=k
					if valido==False:
						break
					
					
				
				
				if l!=[]:

					for elem in l[0]:
						keys=elem.keys()
						if "Usuario" in keys:
							nick=elem["value"]
						elif "Password" in keys:
							password=elem["value"]
						elif "Email" in keys:
							email=elem["value"]
						elif "Avatar" in keys:
							avatar=elem["value"]
						elif "Token" in keys:
							token=elem["value"]
						elif "Permisologia" in keys:
							permisologia=elem["value"]
					self.db("Usuarios").modificarCampo(i,"Contenido",
							[[
							 {"Usuario":"text","name":"usuario","value":nick},
							 
							 {"Email":"text","name":"email","value":email},
							 {"Password":"text","name":"password","value":password},
							 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1,"opciones":"archivos"},
							 {"Token":"hidden","name":"token","value":token},
							 
							 {"Muere":"hidden","name":"muere","value":muere},
							 {"Login":"hidden","name":"login","value":False},
							 {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': permisologia, 'Permisologia': 'select'},
							]]
							)
					
					return self.grabar()
					
				else:
					return False

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
	
		

		def consultarLogin(self,token):
				if self.update():
					import datetime
					
					x = datetime.datetime.now()
					valido=None
					usuarios=self.obtenerFilas("Usuarios")
					i=[]
					l=[]


					for k, fila in enumerate(usuarios):
						i=k
						for campos in fila[1][0]:
							keys=campos.keys()

							if "Token" in keys:	

								if token==campos["value"]:

									valido=False
									
									l.append(fila[1][0])
									break
						if valido==False:
							break


					
					if l!=[]:
						valido=None
						for elem in l[0]:
							keys=elem.keys()
							
							if "Token" in keys:
								while valido==None:
									
									for fila in l:
										

										for campos in fila:
											
											keys=campos.keys()



											if "Email" in keys:
												email=campos["value"]

											elif "Muere" in keys:
												muere=campos["value"]

												muere2=datetime.datetime.strptime(campos["value"],'%d/%m/%Y %H:%M:%S')


											elif "Usuario" in keys:
												nick=campos["value"]
											elif "Password" in keys:
												password=campos["value"]

											elif "Avatar" in keys:
												avatar=campos["value"]
											elif "Permisologia" in keys:
												
												permisologia=campos["value"]
											elif "Token" in keys:
												if token==campos["value"]:
													valido=True
											elif campos["name"]=="login":
												login=campos["value"]

						if datetime.datetime.strptime(zu.DateTime(),'%d/%m/%Y %H:%M:%S')>muere2 and login==True:
							if self.request():
								self.db("Usuarios").modificarCampo(i,"Contenido",
										[[
										 {"Usuario":"text","name":"usuario","value":nick},
										 {"Email":"text","name":"email","value":email},
										 {"Password":"text","name":"password","value":password},
										 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1,"opciones":"archivos"},
										 {"Token":"hidden","name":"token","value":token},
										 {"Muere":"hidden","name":"muere","value":muere},
										 {"Login":"hidden","name":"login","value":False},
										 {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': permisologia, 'Permisologia': 'select'},
										]]
										)
								
								return not self.grabar()
						else:
						
							return True

						
					else:
						
						return False	


except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e