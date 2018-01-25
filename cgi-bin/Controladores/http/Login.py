# -*- coding: utf-8 -*-

from modulos.controlador import Controlador
import os
import Cookie

from config import config

from modulos.ztec.zred import getCookie,normalizar,renderTree,redirecter

class Login(Controlador):
	def __init__(self,data):

		from modulos.ztec.zred import getCookie,normalizar,renderTree
		from modulos.ztec import zu
		Controlador.__init__(self,data)
		self.data=data		

		#-------------------------------------------------
		#SECCION DE CONTROL DE USUARIO
		cookies=getCookie()
		token2=None
	
		
		tokens={}
		folder=os.getcwd().replace("\\","/").split("/")[-2]
		cookie=Cookie.SimpleCookie()


		if self.data["app"]!=None and self.data["user"]==None:

			from settings import config as settings
			from settings import routes

			if "token" in cookies:
				tokens=normalizar(cookies["token"]) if normalizar(cookies["token"])!="" else {}
			if "token2" in cookies:
				token2=normalizar(cookies["token2"]) 
			
		
			if settings.app in tokens and (token2==None or token2==""):

			    
			    self.data["token"]=tokens[settings.app]
			    
			    if data["model"]["usuarios"].isUser(token=tokens[settings.app]) and data["model"]["usuarios"].consultarLogin(tokens[settings.app]):

			      
			      self.data["user"]=data["model"]["usuarios"].getUser(self.data["token"])

			      self.data["login"]=True
			      self.data["isGlobalUser"]=False
			      
			    else:
			      
			      self.data["login"]=False
			      
			      cookie["token2"]=""
			      cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
			      cookie["token"]=""
			      cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
			      
			      print cookie

			

			elif token2!=None and data["model"]["global"].consultarLogin(token2):
			    self.data["token"]=token2
			    self.data["user"]=data["model"]["global"].getUser(self.data["token"])
			    self.data["login"]=True
			    self.data["isGlobalUser"]=True
			elif data["app"]==settings.app:
			    
			    self.data["login"]=False
		
			    cookie["token2"]=""
			    cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
			    cookie["token"]=""
			    cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
			    print cookie

			
			for elem in self.data["model"]:
			   if "token" in data:
			    self.data["model"][elem].token=self.data["token"]
			   else:
			    self.data["model"][elem].token="user"
			self.data["cookies"]=cookies
			self.isglobal=True

			if "token" in data:
				user=self.data["model"]["usuarios"].getUser(self.data["token"])
				
				if self.data["user"]=={}:
					self.data["user"]=self.data["model"]["global"].getUser(self.data["token"])
	

	def Entrar(self,email=None,password=None):
			"""
			Metodo de logeado de la pagina 
			"""
			
			if ("email" in self.data["request"] and "password" in self.data["request"]) or (email!=None and password!=None):
				from modulos.ztec.zred import getCookie,normalizar,redirecter

				
				import Cookie
				cookie=Cookie.SimpleCookie()
				token=False


				
				if self.data["model"]["global"].isUser(self.data["request"]["email"].value if email==None else email):
					

					token=self.data["model"]["global"].login(self.data["request"]["email"].value if email==None else email,self.data["request"]["password"].value if password==None else password)
					self.data["isGlobalUser"]=True
				elif self.data["model"]["usuarios"].isUser(self.data["request"]["email"].value if email==None else email):

					token=self.data["model"]['usuarios'].login(self.data["request"]["email"].value if email==None else email,self.data["password"] if password==None else password)					


					self.data["isGlobalUser"]=False
				
				if token!=False:
					#pendiente que de momento trabajamos solo con la cookie token
					cookies=getCookie()

					if "token" in cookies:

						tokens=normalizar(cookies["token"]) if normalizar(cookies["token"])!="" else {}

					else:
						tokens={}      
					if "token2" in cookies:
						token2=normalizar(cookies["token2"])
					else:
						token2="None"

					folder=os.getcwd().replace("\\","/").split("/")[-2]

					if self.data["isGlobalUser"]:

						cookie["token2"]=token
						cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")

					else:

						if self.data["app"]!=None and self.data["user"]==None:
							from settings import config as settings
							from settings import routes
							

							tokens[settings.app]=token

							cookie["token"]=tokens

							cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")

					
					print cookie
					self.HEADERS.show()



					
					
					contenttype=True
					if self.data["global_control"]==None:
						redirecter(config,self.data["app"],"admin","")()
						pass
				else:
					self.HEADERS.show()
					contenttype=True
					print "Datos incorrectos"
	def Salir(self):			
	   if "token" in self.data:

	     folder=os.getcwd().replace("\\","/").split("/")[-2]   
	     import Cookie
	     cookie=Cookie.SimpleCookie()


	     
	     if ((self.data["isGlobalUser"]==False and self.data["model"]["usuarios"].closeSession(self.data["token"])) or (self.data["isGlobalUser"]==True and self.data["model"]["global"].closeSession(self.data["token"]))):        


	        folder=os.getcwd().replace("\\","/").split("/")[-2]
	        cookies=getCookie()
	        if self.data["isGlobalUser"]==False:
	          cookie["token"]=cookies["token"]
	          cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
	          cookie["token"]["expires"]="Thu, 01 Jan 1970 00:00:01 GMT"
	        else:
	          cookie["token2"]=cookies["token2"]
	          cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
	          cookie["token2"]["expires"]="Thu, 01 Jan 1970 00:00:01 GMT"


	        
	        

	        print cookie
	        self.HEADERS.show()
	        contenttype=True
	        redirecter(config,self.data["app"],"admin","")()
	     else:

	      print "No se a podido cerrar la sesion"
	   else:
	      self.HEADERS.show()
	      redirecter(config,self.data["app"],"admin","")()
	def Registrarse(self):
	   try:
	    
	    self.data["model"]["usuarios" if self.data["isGlobalUser"]==False else "global"].registrarUsuario(self.data["request"]["usuario"]["value"],data["email"].value,self.data["request"]["password"].value,self.data["opciones"]["archivos"][1][1].index(data["avatar"].value),self.data["opciones"]["usuarios" if self.data["isGlobalUser"]==False else "global"][0][1].index(data["permisologia"].value))
	    

	    token=self.data["model"]["usuarios" if self.data["isGlobalUser"]==False else "global"].login(self.data["request"]["email"].value,self.data["request"]["password"].value)
	    
	    #pendiente que de momento trabajamos solo con la cookie token
	    
	    cookies=getCookie()
	    folder=os.getcwd().replace("\\","/").split("/")[-2]
	    if self.data["isGlobalUser"]==False:

	      if "token" in cookies:
	        tokens=normalizar(cookies["token"])

	      else:
	        tokens={}    
	      tokens[settings.app]=token
	      cookie["token"]=tokens
	      cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
	    else:

	      
	      cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
	    #print "token="+str(tokens)[1:-1].replace("'","").replace('"',"").replace(" ","")
	    
	    print cookie

	    HEADERS.show()
	    contenttype=True
	    
	    redirecter(config,self.data["app"],"admin","")()
	   except Exception,e :
	    print str(e)[1:-1]

	 
	 
	def Actualizar_usuario(self):
		HEADERS.show()
		if self.data["model"]["global"].isUser(self.data["user"]["email"]):
			self.data["model"]["usuarios"].modificarUsuario(indice,data["usuario"].value,self.data["request"]["email"].value,self.data["request"]["password"].value, self.data["opciones"]["archivos"][1][1].index(data["avatar"].value),self.data["opciones"]["usuarios" if self.data["isGlobalUser"]==False else "global"][0][1].index(self.data["permisologia"].value))
		redirecter(config,self.data["app"],"admin","Usuarios",action="listar")()


