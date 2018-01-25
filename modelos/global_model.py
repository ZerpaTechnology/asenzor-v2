
from modulos.ztec.zmodel import Model

from modulos.ztec import zu
import sys
try:
	from config import config
except:
	import config
from modulos.ztec.zdb import DB
from modulos.ztec import zu

class model(Model):
	def obtenerCreditos(self,app):
		if self.update():
			for k,elem in enumerate(self.obtenerFilas("apps")):
				if elem[0]==app:
					
					return self.obtenerContenido(k,"apps")

	def activarApp(self,app):#activa/desactiva
		if self.request():

			for k,elem in enumerate(self.obtenerFilas("apps")):
				if elem[0]==app:
					if "Suspendida" in elem[4]:
						elem[4].remove("Suspendida")
						elem[4].append("Activa")
						self.db("apps").modificarCampo(k,"Status",elem[4])
					elif "Activa" in elem[4]:
						elem[4].remove("Activa")
						elem[4].append("Suspendida")
						self.db("apps").modificarCampo(k,"Status",elem[4])
			self.grabar()
	def activarPlugin(self,plugin):#activa/desactiva
		if self.request():
			for k,elem in enumerate(self.obtenerFilas("Plugins")):
				if elem[0]==plugin:
					return self.models["main"].activarPlugin(plugin)





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

	def desactivarApp(self,app):
		if self.request():
			for k,elem in enumerate(self.obtenerFilas("apps")):
				if elem[0]==app:
					if "Activa" in elem[4]:
						elem[4].remove("Activa")
					if "Suspendida" not in elem[4]:
						elem[4].append("Suspendida")
						self.db("apps").modificarCampo(k,"Status",elem[4])
			self.grabar()

	def reportarError(self,error):
		if self.request():
			f=open(error[1],"r")

			msj="""Error: """+str(error[0])+"""
			Archivo: """+error[1]+"""
			Linea: """+str(error[2])+"""
			-------------------------
			"""+f.readlines()[error[2]]+"""
			"""
			f.close()
			tabla=self.obtenerFilas("Log")
			token=zu.randomString()
			anteriores=[]
			for elem in tabla:
				anteriores.append(elem[0])
			while token in anteriores:
				token=zu.randomString()



			self.db("Log").insertar(str(token),
				[str(error[0]),error[1],error[2],msj],
				{"Error":len(tabla)},
				zu.DateTime(),
				False
				)
			
			return [self.grabar(),token]

	def buscarError(self,token):
		if self.update():
			for elem in self.obtenerFilas("Log"):
				if elem[0]==token:
					return elem
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
				if self.models["usuarios"].isUser(email)==False:
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
							 {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': permisologia, 'Permisologia': 'select'},
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
				
				valido=None
				usuarios=self.obtenerFilas("Usuarios")
				if permisologia<self.data["user"]["permisologia"]:
					permisologia=self.data["user"]["permisologia"]
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
				usuarios2=self.models["usuarios"].obtenerFilas("Usuarios")
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
	

	def getUser(self,token):
			if self.update():
				import datetime
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

	def instalarApp(self,app):
		if self.request(metodo=self.instalarApp.__func__):
			
			f=open(config.base_root+config.apps_folder+app+"/admin/modelos/install_db.datay","r")
			source=f.read()
			f.close()
			db=self.db
			i=len(self.obtenerFilas("apps"))
			exec(source)
			
			self.db.registro=db.registro
			return self.grabar()

	def instalarPlugin(self,plugin):
		if self.request(metodo=self.instalarPlugin.__func__):
			
			f=open(config.base_root+config.datalugins_folder+plugin+"/install_db.datay","r")
			source=f.read()
			f.close()
			db=self.db
			insertar=True
			for k,elem in enumerate(self.obtenerFilas("Plugins")):
				if elem[0]==plugin:
					insertar=False
					break
			dbfile=self.models["main"].dbfile
			
			i=len(self.obtenerFilas("Plugins"))
			exec(source)
			
			if insertar:
				
				self.db.registro=db.registro
				self.grabar()

				for elem in self.obtenerFilas("apps"):
					temp=dbfile.split("/")
					pos=temp.index(config.apps_dir)
					temp[pos+1]=elem[0]
					temp="/".join(temp)
					
					if self.models["main"].request(temp):
						self.models["main"].db("Plugins").insertar(plugin,False)						
						self.models["main"].grabar()
						
			else:
				self.db("Plugins").modificarCampo(k,"Contenido",db("Plugins").obtenerFilasValores("Contenido")[-1])
				self.grabar()
			

			return True



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
