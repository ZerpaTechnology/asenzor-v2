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
		def registrarUsuario(self,username,password,email,name,lastname,rank,avatar,department_id,position_id,total_hours=0):
			import datetime
			import ztec.zu as zu
			
			x = datetime.datetime.now()
			if self.request():
				self.db("users").insertar(username,password,email,name,lastname,"%s"%x,rank,avatar,department_id,position_id,str(zu.DateTime(H=total_hours)))
				self.grabar()

		def registrarUsuario2(self,nick,email,password,avatar,hours=4):
			
			if self.request():
				muere=str(zu.DateTime(H=hours))
				x = datetime.datetime.now()
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				i=len(usuarios)
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
						 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1},
						 {"Token":"hidden","name":"token","value":token},
						 {"Muere":"hidden","name":"muere","value":muere},
						 {"Login":"hidden","name":"login","value":True},
						]],
						{"Usuario":i},
					   zu.DateTime(),
					   []
					   )
				self.grabar()
				
				return True
		def obtenerContactos(self,token):
			if self.update():
				pass



		def modificarUsuario2(self,indice,nick,email,password,avatar,hours=4):
			
			if self.request():
				muere=str(zu.DateTime(H=hours))
				x = datetime.datetime.now()
				
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				l=[]
				i=0
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

				token=l[0][4]["value"]

				self.db("Usuarios").modificarCampo(indice,"Nombre",nick)
				
				self.db("Usuarios").modificarCampo(indice,"Contenido",
						[[
						 {"Usuario":"text","name":"usuario","value":nick},
						 {"Email":"text","name":"email","value":email},
						 {"Password":"text","name":"password","value":password},
						 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1},
						 {"Token":"hidden","name":"token","value":token},
						 {"Muere":"hidden","name":"muere","value":muere},
						 {"Login":"hidden","name":"login","value":True},
						]])
				self.db("Usuarios").modificarCampo(indice,"args",
						{"Usuario":indice}
						)
				self.db("Usuarios").modificarCampo(indice,"Fecha",
					   zu.DateTime(),
					   []
					   )
				return self.grabar()
				
				
		def login2(self,email,password):
			if self.request():
				
				muere=str(zu.DateTime(H=1))
				
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
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
					while valido!=True:
						pasa=True

						token=zu.randomString()
						for fila in usuarios:
							if token==fila[1][0][4]["value"]:
								pasa=False
						if pasa==True:
							valido=True
					

					self.db("Usuarios").modificarCampo(i,"Contenido",
							[[
							 {"Usuario":"text","name":"usuario","value":nick},
							 {"Email":"text","name":"email","value":email},
							 {"Password":"text","name":"password","value":password},
							 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1},
							 {"Token":"hidden","name":"token","value":token},
							 {"Muere":"hidden","name":"muere","value":muere},
							 {"Login":"hidden","name":"login","value":True},
							]]
							)
			
					self.grabar()
					
					return token
				else:
					return False
		def crearContacto(self,nombre,contenido):
			if self.request():
				self.db("Contactos").insertar(nombre,
					[[
					{"Email":"text","value":nombre,"name":"email"},
					{"contenido":"textarea","value":contenido,"name":"contenido"}
					]],
					{"Contacto":len(self.obtenerFilas("Galerias"))-1},
					zu.DateTime(),
					[]
					)
				self.grabar()
				return True

		def elimnarContacto(self,nombre,contenido):
			if self.request():
				tabla="Contactos"
				if len(self.obtenerFilas(tabla))>0:
					self.db(tabla).delFila(indice)
					self.grabar()
					return True
				else:
					return False

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

			
		def modificarInformacion(self,indice,nombre,contenido):
			if self.request():
				self.db("Informaciones").modificarCampo(indice,"Nombre",
					nombre
					)
				self.db("Informaciones").modificarCampo(indice,"Contenido",
					[
					[
					{"Titulo":"text","name":"titulo","value":nombre},
					{"Contenido":"textarea","name":"contenido","value":contenido}
					],
					],
					)
				self.db("Informaciones").modificarCampo(indice,"Fecha",
					zu.DateTime(),
					[]
					)

				return self.grabar()
		def modificarAnuncio(self,indice,nombre,imagen):
			if self.request():
				self.db("Anuncios").modificarCampo(indice,"Nombre",
					nombre
					)
				self.db("Anuncios").modificarCampo(indice,"Contenido",
					[
					[
					{"Titulo":"text","name":"titulo","value":nombre,},
					{"Imagen 1":"select","name":"img","value":37,"opcion":imagen},
					],
					],
					)
				self.db("Anuncios").modificarCampo(indice,"Fecha",
					zu.DateTime(),
					[]
					)

				return self.grabar()
		def crearAnuncio(self,indice,nombre,imagen):
			if self.request():
				tabla="Anuncios"
				indice=len(self.obtenerFilas(tabla))
				db(tabla).insertar(nombre,[
								[
								{"Titulo":"text","name":"titulo","value":nombre,},
								{"Imagen 1":"select","name":"img","value":37,"opcion":imagen},
								]
								],
					{"Anuncio":indice},
					zu.DateTime(),
					[]
				)
				return self.grabar()
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
		def crearContacto(self,nombre,email,contenido):
			if self.request():
				tabla="Contactos"
				indice=len(self.obtenerFilas(tabla))
				self.db(tabla).insertar(
					nombre,
					[[
					{"Nombre":"text","name":"nombre","value":nombre},
					{"Email":"text","name":"email","value":email},
					{"Contenido":"text","name":"contenido","value":contenido}
					]],
					{"Contacto":indice},
					zu.DateTime(),
					[]
					)
				return self.grabar()
		def crearPublicacion(self,nombre,imagen,publicacion):
			if self.request():
				tabla="Publicaciones"
				indice=len(self.obtenerFilas(tabla))
				self.db(tabla).insertar(
					nombre,
					[[
					{"Titulo":"text","name":"titulo","value":nombre},
					{"Imagen":"select","name":"img","value":imagen,"opcion":0},
					{"Contenido":"textarea","name":"publish","value":publicacion}
					]],
					{"Publicacion":indice},
					zu.DateTime(),
					[]
					)
				return self.grabar()
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

		def modificarPublicacion(self,indice,nombre,imagen,publicacion):
			if self.request():
				tabla="Publicaciones"
				self.db(tabla).modificarCampo(indice,"Nombre",nombre)
				self.db(tabla).modificarCampo(indice,"Contenido",
					[[
						{"Titulo":"text","name":"titulo","value":nombre},
						{"Imagen":"select","name":"img","value":imagen,"opcion":0},
						{"Contenido":"textarea","name":"publish","value":publicacion}
						]])

				self.db(tabla).modificarCampo(indice,"Fecha",zu.DateTime())
				return self.grabar()
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



		def getUser(self,token):
			if self.update():
				
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
				return l[0]
		def obtenerUsuario(self,token):
			if self.update():
				tabla={}
				for usuario in self.obtenerFilas("Usuarios"):
					
					if usuario[1][0][4]["value"]==token:
						for elem in usuario[1][0]:
							tabla[elem["name"]]=elem["value"]
				return tabla
				

		def consultarLogin2(self,token):
			if self.request():
				
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
										elif "Token" in keys:
											if token==campos["value"]:
												valido=True
					if datetime.datetime.strptime(zu.DateTime(),'%d/%m/%Y %H:%M:%S')>muere2:
						self.db("Usuarios").modificarCampo(i,"Contenido",
								[[
								 {"Usuario":"text","name":"usuario","value":nick},
								 {"Email":"text","name":"email","value":email},
								 {"Password":"text","name":"password","value":password},
								 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1},
								 {"Token":"hidden","name":"token","value":token},
								 
								 {"Muere":"hidden","name":"muere","value":muere},
								 {"Login":"hidden","name":"login","value":False},
								]]
								)
						self.grabar()

						return False
					else:

						return True
				else:
					return False	



		def closeSession2(self,token):
			
			if self.request():
				
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
					self.db("Usuarios").modificarCampo(i,"Contenido",
							[[
							 {"Usuario":"text","name":"usuario","value":nick},
							 
							 {"Email":"text","name":"email","value":email},
							 {"Password":"text","name":"password","value":password},
							 {"Avatar":"select","name":"avatar","value":avatar,"opcion":1},
							 {"Token":"hidden","name":"token","value":token},
							 
							 {"Muere":"hidden","name":"muere","value":muere},
							 {"Login":"hidden","name":"login","value":False},
							]]
							)
					
					return self.grabar()
					
				else:
					return False

		def crearLibro(self,nombre,autores,colaboradores=[],referencias=[],editorial=None,fechaP=None,url=None,costo=None):
			if self.request():
				self.db("libros").insertar(nombre,autores,colaboradores,referencias,editorial,fechaP,url,costo)
				self.grabar()
		def crearPagina(self,data):
			if self.request():
				select=True
				l2=list(data)
				l2.sort()
				l2.remove("action")
				#Pendiente de que los nombres de los campos no deben repetirse
				for k,elem in enumerate(self.obtenerFilas("Plantillas")):
					campos=[]
					plantilla=k
					
					c=0
					try:
						l=[]
						for box in elem[1]:
							for campo in box:	
								
									
								l.append(campo["name"])
						l.sort()
						
						
						for campo in l:
							if l2[c]!=campo:
								select=False
							c+=1
						if select==True:
							break
							
						
					except:
						pass
					
				
				
				c=0
				boxes=[]
				
				for k2,box in enumerate(self.obtenerFilas("Plantillas")[plantilla][1]):
					for k,campo in enumerate(box):
						indice=l2.index(campo["name"])
						if k2==0 and k==0:
							titulo=data[l2[indice]].value
						if "opcion" in campo:

							box[k]["value"]=int(data[l2[indice]].value)
						else:
							box[k]["value"]=data[l2[indice]].value
						c+=1
					boxes.append(box)
				i=len(self.obtenerFilas("Paginas"))
				
				self.db("Paginas").insertar(titulo,boxes,{"Pagina":i},zu.DateTime(),[])
				self.grabar()
		def crearFormulario(self,data):
			if self.request():
				select=True
				l2=list(data)
				l2.sort()
				l2.remove("action")
				#Pendiente de que los nombres de los campos no deben repetirse
				
				for k,elem in enumerate(self.obtenerFilas("Plantillas")):
					campos=[]
					plantilla=k
					
					c=0
					try:
						l=[]
						for box in elem[1]:
							for campo in box:	
								
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
								tmp.remove("padre") if "padre" in tmp else tmp
						
								tipo=campo[tmp[0]]
								l.append(campo["name"])
								
						l.sort()
						
						
						for campo in l:
							if l2[c]!=campo:
								select=False
							c+=1
						if select==True:
							break
							
						
					except:
						pass
					
				
				
				c=0
				boxes=[]	

				for k2,box in enumerate(self.obtenerFilas("Plantillas")[plantilla][1]):
					for k,campo in enumerate(box):
						indice=l2.index(campo["name"])
						if k2==0 and k==1:
							titulo=data[l2[indice]].value
						else:

							if "opcion" in campo and data[l2[indice]].value!="":
								box[k]["value"]=int(data[l2[indice]].value)
							else:
								box[k]["value"]=data[l2[indice]].value
						c+=1
					boxes.append(box)
				i=len(self.obtenerFilas("Formularios"))
				
				self.db("Formularios").insertar(titulo,boxes,{"Formulario":i},zu.DateTime(),[])
				self.grabar()
		def registrarFormulario(self,data):
			if self.request():
				select=True
				l2=list(data)
				l2.sort()
				tabla,ide=data["action"].value.split("_")
				l2.remove("action")
				#Pendiente de que los nombres de los campos no deben repetirse
				l=[]
				for elem in l2:
					l.append(data[elem].value)
				c=0
				boxes=[]	
				i=len(self.obtenerFilas(tabla))
				opciones=self.obtenerFilas("Opciones")
				mensaje="<p>Un visitante a llenado el formulario de contacto puedes verlo en <a href='"+config.base_url+"app="+settings.app+"&admin=True&vista=index&action=editar&args="+str({"PostdeFormulario":i})+"'>visitando tu sitio</a> o mendiante este email:</p>"
				for k2,box in enumerate(self.obtenerFilas("Formularios")[int(ide)][1]):

					for k,campo in enumerate(box):
						
						if k2==0 and k==1:
							titulo=campo["value"]+" "+str(i+1)
						else:
							
							tmp=list(campo)
							tmp.remove("name") if "name" in tmp else tmp
							tmp.remove("value") if "value" in tmp else tmp
							tmp.remove("step") if "step" in tmp else tmp
							tmp.remove("opcion") if "opcion" in tmp else tmp
							tmp.remove("requerido") if "requerido" in tmp else tmp
							tmp.remove("tabla") if "tabla" in tmp else tmp
							tmp.remove("depende") if "depende" in tmp else tmp
							tmp.remove("categoria") if "captegoria" in tmp else tmp
							tmp.remove("descripcion") if "descripcion" in tmp else tmp
							tmp.remove("padre") if "padre" in tmp else tmp
							tmp=tmp[0]
							

							if campo[tmp]!="text-admin" and campo[tmp]!="img-admin" and campo[tmp]!="select-admin" :
								indice=campo["name"]
								
								if "opcion" in campo:
									
									mensaje+=tmp+"<br> &nbsp; &nbsp;"+opciones[int(campo["opcion"])][1][int(data[indice].value)]+"<br><br>"
									box[k]["value"]=int(data[indice].value)

								elif campo[tmp]=="number":
									mensaje+=tmp+"<br>  &nbsp; &nbsp;"+data[indice].value+"<br><br>"
									box[k]["value"]=int(data[indice].value)
									
								else:
									mensaje+=tmp+"<br>  &nbsp; &nbsp;"+data[indice].value+"<br><br>"
									box[k]["value"]=data[indice].value
						c+=1
					boxes.append(box)
				
				from ztec.zred import sendEmail	
				
				sendEmail("office@marquisrentalapartments.com","office@marquisrentalapartments.com","password",mensaje)
				boxes.insert(0,{"Formulario":"hidden-id","name":"id","value":ide})
				self.db(tabla).insertar(titulo,boxes,{tabla:i},zu.DateTime(),[])
				self.grabar()

		def modificarPagina(self,indice,data):
			if self.request():
				select=True
				l2=list(data)
				l2.sort()
				l2.remove("action")

				#Pendiente de que los nombres de los campos no deben repetirse
				for k,elem in enumerate(self.obtenerFilas("Plantillas")):
					campos=[]
					plantilla=k
					
					c=0
					try:
						l=[]
						for box in elem[1]:
							for campo in box:	
								
									
								l.append(campo["name"])
						l.sort()
						
						for campo in l:
							if l2[c]!=campo:
								select=False
							c+=1
						if select==True:
							break
							
						
					except:
						pass
					
				
				
				c=0
				boxes=[]
				
				for k2,box in enumerate(self.obtenerFilas("Plantillas")[plantilla][1]):
					for k,campo in enumerate(box):

						indice2=l2.index(campo["name"])
						if k2==0 and k==0:
							titulo=data[l2[indice2]].value
						if "opcion" in campo:

							box[k]["value"]=int(data[l2[indice2]].value)
						else:
							box[k]["value"]=data[l2[indice2]].value
						c+=1
					boxes.append(box)

				self.db("Paginas").modificarCampo(indice,"Nombre",titulo)
				self.db("Paginas").modificarCampo(indice,"Contenido",
					boxes)
				self.db("Paginas").modificarCampo(indice,"args",
					   {"Pagina":indice},
					   )
				self.db("Paginas").modificarCampo(indice,"Fecha",
						zu.DateTime())
				self.grabar()
		def eliminarEntrada(self,indice):
			if self.request():
				tabla="Entradas"
				print "#filas ",len(self.obtenerFilas(tabla))
				if len(self.obtenerFilas(tabla))>0:
					self.db(tabla).delFila(indice)
					self.grabar()
					print "#elimina ",indice 
					return True
				else:
					return False
		def eliminarMenu(self,indice):
			if self.request():
				tabla="Menus"
				if len(self.obtenerFilas(tabla))>0:
					self.db(tabla).delFila(indice)
					self.grabar()
					return True
				else:
					return False

		def modificarEntrada(self,indice,wnoticias_img,wnoticias_titulo,wnoticias):
			
			if self.request():
				tabla="Entradas"
				
				self.db(tabla).modificarCampo(indice,"Nombre",wnoticias_titulo)
				
				self.db(tabla).modificarCampo(indice,"Contenido",[[{"Imagen":"select","name":"wnoticias_img","value":wnoticias_img,"opcion":0},
																  {"Título":"text","name":"wnoticias_titulo","value":wnoticias_titulo},
																  {"Contenido":"textarea","name":"wnoticias","value":wnoticias}
																 ]])
				
				self.db(tabla).modificarCampo(indice,"args",
					   {"Entrada":indice}
					   )
				self.db(tabla).modificarCampo(i,"Fecha",
					   zu.DateTime()
					   )
				
				self.grabar()

		def crearEntrada(self,wnoticias_img,wnoticias_titulo,wnoticias):
			
			if self.request():
				tabla="Entradas"
				indice=len(self.obtenerFilas("Entradas"))
				self.db(tabla).insertar(wnoticias_titulo,[[{"Imagen":"select","name":"wnoticias_img","value":wnoticias_img,"opcion":0},
																  {"Título":"text","name":"wnoticias_titulo","value":wnoticias_titulo},
																  {"Contenido":"textarea","name":"wnoticias","value":wnoticias}
																 ]],
					   {"Entrada":indice},
					   zu.DateTime()

					   )
				
				
				self.grabar()
		def crearMenu(self,nombre,home,biografia,descargas,redes,twitter,instagram,facebook,noticias):
			
			if self.request():
				tabla="Menus"
				indice=len(self.obtenerFilas("Menus"))
				db("Menus").insertar(nombre,[
									 {"nombre":"text","name":"prensa","value":nombre},
									 {"Home":"text","name":"home","value":home},
									 {"Biografia":"text","name":"biografia","value":biografia},
									 {"Descargas":"text","name":"descargas","value":descargas},
									 [
									  {"Redes sociles":"text","name":"redes","value":redes},
									  {"Twitter":"text","name":"twitter","value":twitter},
									  {"Instagram":"text","name":"instagram","value":instagram},
									  {"Facebook":"text","name":"facebook","value":facebook},
									 ],
					 				 {"Prensa":"text","name":"prensa","value":noticias},

								],
					{"Menu":indice},
					zu.DateTime()
				)
				
				return self.grabar()
		def modiciarMenu(self,indice,nombre,home,biografia,descargas,redes,twitter,instagram,facebook,noticias):
			
			if self.request():
				tabla="Menus"
				
				db(tabla).modificarCampo(indice,"Nombre",nombre)
				db(tabla).modificarCampo(indice,"Contenido",[
									 {"nombre":"text","name":"prensa","value":nombre},
									 {"Home":"text","name":"home","value":home},
									 {"Biografia":"text","name":"biografia","value":biografia},
									 {"Descargas":"text","name":"descargas","value":descargas},
									 [
									  {"Redes sociles":"text","name":"redes","value":redes},
									  {"Twitter":"text","name":"twitter","value":twitter},
									  {"Instagram":"text","name":"instagram","value":instagram},
									  {"Facebook":"text","name":"facebook","value":facebook},
									 ],
					 				 {"Prensa":"text","name":"prensa","value":noticias},

								])
				db(tabla).modificarCampo(indice,"args",{"Menu":indice})
				db(tabla).modificarCampo(indice,"Fecha",zu.DateTime())

				
				self.grabar()

		def subirArchivo(self,data):
			
			if self.request():
				tabla="Opciones"
				existe=True
				import os
				
				opciones=self.obtenerFilas(tabla)
				
				archivo=data["archivo"]
				
				opcion=opciones[5][1].index(data["opcion"].value)

				tipo=opciones[3][1].index(data["tipo"].value)
				if archivo.filename!="":
					renombre=data["renombre"].value+archivo.filename[archivo.filename.find("."):] if "renombre" in data and data["renombre"].value!="" else archivo.filename

					i=len(self.obtenerFilas("Archivos"))
					if  data["opcion"].value not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"):
						
						os.mkdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value)
					

					if renombre not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value):
						#self.db(tabla).modificarCampo(opcion,"Valores",l+[renombre+"."+archivo.filename.split(".")[1]])

						f=open(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value+"/"+renombre,"w")
						f.write(archivo.file.read())
						f.close()						
					else:
						existe=False

					if existe==True:
						l=self.obtenerFilas("Opciones")[0][1]

						l=l+[renombre]
                                                print len(l)
						self.db("Opciones").modificarCampo(0,"Valores",l)
						self.db("Archivos").insertar(renombre,
								[
									[
									{"Imagen":"img","name":"archivo","value":len(l)-1,"opcion":0},
									{"Título":"text","name":"renombe","value":renombre},							
									{"Enlace":"text","name":"enlace","value":config.base_url+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value+"/"+archivo.filename},
									{"Típo":"text","name":"tipo","value":data["tipo"].value},
									]
								],
								{"Archivo":i},
								zu.DateTime(),
								[]
								)
						
						
						
						self.grabar()
						return True
					else:
						return False
				else:
					return False
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
		def obtenerContactos(self,correo):
			if self.update():
				return self.obtenerFilas("Contactos")

		def obtenerAdminMenu(self):
			if self.update():
				c=0
				l=[]
				try:
					while True:
			
						l.append(self.db("AdminMenu").obtenerFilaValores(c))
						c+=1					
				except:

					return l
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

		def obtenerMenus(self):
			if self.update():
				c=0
				l=[]
				try:
					while True:
			
						l.append(self.db("Menus").obtenerFilaValores(c))
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



		def guardarTema(self,app,libro,tema,text):
			
			if self.request():
				self.db("documentos").insertar(app,libro,tema,text)
				self.grabar()

		def registrarCuenta(self,redsocial,nombre,password):
			
			if self.update():
				self.db("cuentas").insertar(redsocial,nombre,"password:"+password)

		def programar(self,cuenta,texto,multimedia):
			pass
		def obtenerGaleria(self,galeria):
			if self.update():
				return self.obtenerFilas("Galerias")[galeria]
			

				
		def login(self,usuario,password):
			
			
			if self.update():


				if self.db("users").obtenerFilasValores(usuario)!=[]:
					filas=self.db("users").obtenerFilasValores(usuario)
					if filas[1]==password:
						return True
					else:
						print "la contraseña es incorrecta"
						return False
		#{act}
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

		def consultarLogin(self,token):
			
			if self.update():
				return self.db("usuarios").obtenerFilasValores(token)[-1]
		def cargarPlugins(self,pugins):
			import imp
			if self.update():
				allplugins={}
				tabla=self.obtenerFilas("Plugins")
				for plugin in plugins:
					if tabla[0]==plugin:
						if tabla[1][0][8]["value"]==True:
							allplugins[plugin]=imp.load_source(settings.base_root+settings.plugins_folder+plugin+"default.py")
				return allplugins			
						


		def activarplugins(self,indice):
			if self.request():
				if 1==self.obtenerFilas("Plugins")[indice][1][1][8]["value"]:
					pass
				else:
					pass

		def desactivarplugins(self,indice):
			if self.request():
				self.obtenerFilas("Plugins")
				if 1==self.obtenerFilas("Plugins")[indice][1][1][8]["value"]:
					pass
				else:
					pass


except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e