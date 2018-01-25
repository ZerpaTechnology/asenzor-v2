import sys
import imp


from config import config

try:
	from modulos.ztec.zred import getRest,normalizar,Headers,getCookie,gringolizar
except Exception as e:
	print e



from modelos.global_model import model


__path__=__file__[:__file__.rfind("/")+1]

class Asenzor:
	"""docstring for AsenZor"""
	def __init__(self):
		#====================================================================
		
		self.HEADERS=Headers()



		
		self.data={"ajax":False}
		self.vista="error404"
		
		self.data.update(getRest(config))

		import imp
		import cgi, cgitb
		cgitb.enable()

		data= cgi.FieldStorage()


		
		if (self.data["control"]==None and self.data['global_control']==None and self.data['metodo']== None and  self.data['app'] == None and self.data['args']==[]and self.data['request']=={}and self.data['manager']==False and self.data['ajax']==False and self.data['kwargs']== {} and self.data['action']== None):
			self.data["app"]=config.default_app
			
			

		




		


		
		import os		

		try:

		    if type(data.value)==list:
		    	d={}
		    	d2={}
		        for elem in data.value:

		        	if elem.name=="app":

		        		if elem.value!="None" and elem.value!=None:

		        			self.data[elem.name]=normalizar(elem.value)

		        			self.data["request"][elem.name]=elem
		        			
		        				
		        	else:
		        		if elem.name in d:
			        		d[elem.name].append(elem.value)
			        		d2[elem.name].append(elem)
			        		self.data[elem.name]=d[elem.name]
			        		self.data["request"][elem.name]=d2[elem.name]
			        	else:
			        		d[elem.name]=[elem.value]
			        		d2[elem.name]=[elem]
			        		self.data[elem.name]=normalizar(elem.value)
			        		self.data["request"][elem.name]=elem
			       

		        		
		    else:


		    	"""
		        params=data.value.split("/")[-1].split("&")


		        for elem in params:
		            k,v=elem.split("=")
		            self.data[k]=normalizar(v)                                                     
		            self.data["request"][k]={"value":normalizar(v)}                                                     
		        """
	            
		    

		
		except Exception,e :
			if "action" not in data:
				self.data["action"]=None
			else:
				self.data["action"]=data["action"].value
				self.data["request"]["action"]=data["action"]

		
			
		
		

		

		self.data["model"]={}

		self.data["errores"]=[]
		self.data["vars"]={}
		
		
		
		self.data["plugins"]={}


		self.data["login"]=False
		self.data["user"]=None
		self.data["isGlobalUser"]=False
		self.data["token"]=None
		self.data["model"]["global"]=model("../modelos/global","../modelos/request/","user",ext=".py")

		self.data["opciones"]={"global":self.data["model"]["global"].obtenerFilas("Opciones")}
		self.data["plugins-hooks"]=[]
		self.data["plugins"]={}






		
		
		if self.data["app"]!=None and self.data["global_control"]==None:



			sys.path.append(config.base_root+config.apps_folder+self.data["app"]+"/")

			from app import app
		
			self.app=app()

			sys.path.append(self.app.admin.__path__) if (self.app.admin.__path__ not in sys.path) else None

			self.data["base_url"]=self.app.user.__url__

			contenido=self.data["model"]["global"].obtenerContenido(self.data["app"],"apps")[self.data["app"]]

			settings=self.app.admin.settings




			routes=self.app.admin.routes
			base_root=self.app.admin.__path__
			
	
			#=======================================================================
			
			
			if len(contenido)>1 and self.data["app"]!=None:

				for k,elem in enumerate(contenido[1]):

					if contenido[1][elem]["value"] in settings.dbs:


						if os.path.exists(self.app.admin.modelos.__path__+str(contenido[1][elem]["value"])+"_model.py"):
							exec("model"+str(k)+"=imp.load_source('model"+str(k)+"' ,'"+self.app.admin.modelos.__path__+str(contenido[1][elem]["value"])+"_model.py').model")
							
							exec("self.data['model']['"+contenido[1][elem]["value"]+"']=model"+str(k)+"('"+self.app.admin.modelos.__path__+contenido[1][elem]["value"]+"','"+self.app.admin.modelos.__path__+"request/','"+self.data["app"]+"',ext='.py')")	
							
							self.data["model"][contenido[1][elem]["value"]].models["global"]=self.data["model"]["global"]
							self.data["model"]["global"].models[contenido[1][elem]["value"]]=self.data["model"][contenido[1][elem]["value"]]
							
							if "Opciones" in self.data["model"][contenido[1][elem]["value"]].db.tablas:
								self.data["opciones"][contenido[1][elem]["value"]]=self.data["model"][contenido[1][elem]["value"]].obtenerFilas("Opciones")
							if self.data["model"][contenido[1][elem]["value"]].errores!=[]:
								self.data["errores"].append(self.data["model"][contenido[1][elem]["value"]].errores)
							elif self.data["model"][contenido[1][elem]["value"]].db.errores:
								self.data["errores"].append(self.data["model"][contenido[1][elem]["value"]].db.errores)
					else:
						self.data["errores"].append("No se encontro el modelo: "+contenido[1][elem]["value"]+" en el directorio")

				for k,elem in enumerate(contenido[2]):


					if contenido[2][elem]["value"] in settings.dbs:
						if os.path.exists("../"+config.modelos_folder+str(contenido[2][elem]["value"])+"_model.py"):

							exec("model"+str(k)+"=imp.load_source('model"+str(k)+"' ,'../"+config.modelos_folder+str(contenido[2][elem]["value"])+"_model.py').model")
							exec("self.data['model']['"+contenido[2][elem]["value"]+"']=model"+str(k)+"('"+base_root+routes.models_folder+contenido[2][elem]["value"]+"','"+base_root+routes.models_folder+"request/','"+self.data["app"]+"',ext='.py')")	
							self.data["model"][contenido[2][elem]["value"]].models["global"]=self.data["model"]["global"]
							self.data["model"]["global"].models[contenido[2][elem]["value"]]=self.data["model"][contenido[2][elem]["value"]]
							if "Opciones" in self.data["model"][contenido[2][elem]["value"]].db.tablas:
								self.data["opciones"][contenido[2][elem]["value"]]=self.data["model"][contenido[2][elem]["value"]].obtenerFilas("Opciones")
							if self.data["model"][contenido[2][elem]["value"]].errores!=[]:
								self.data["errores"].append(self.data["model"][contenido[2][elem]["value"]].errores)
							elif self.data["model"][contenido[2][elem]["value"]].db.errores:
								self.data["errores"].append(self.data["model"][contenido[2][elem]["value"]].db.errores)
						else:
							self.data["errores"].append("No se encontro el modelo: "+contenido[2][elem]["value"]+" en el directorio")

			plugins={}


			self.data["base_url"]=self.app.user.__url__



			for elem in self.data["model"]["main"].obtenerFilas("Plugins"):
				plugins[elem[0]]=elem[1]


			for plugin in self.data["model"]["global"].obtenerFilas("Plugins"):

				if plugin[0] in plugins:
					
					
					if plugins[plugin[0]]==True:

						for elem in plugin[1][1]:
							self.data["plugins-hooks"].append([elem["name"],elem["value"]])
						
						if os.path.exists(config.base_root+config.plugins_folder+plugin[0]+"/default.py"):
							
							self.data["plugins"][plugin[0]]=imp.load_source("",config.base_root+config.plugins_folder+plugin[0]+"/default.py").Plugin(self.data)

						else:
							
							print "El plugin: "+plugin[0]+"No puede ser inicializado"




				else:

					if self.data["model"]["main"].request():
						self.data["model"]["main"].db("Plugins").insertar(plugin[0],False)
						self.data["model"]["main"].grabar()
				

					
			
			
			self.app.user.cnt(self.data)


		else:
			
			if self.data["app"]!=None:
				sys.path.append(config.base_root+config.apps_folder+self.data["app"]+"/")
				from app import app
				self.app=app()
				sys.path.append(self.app.admin.__path__) if (self.app.admin.__path__ not in sys.path) else None
				self.data["base_url"]=self.app.user.__url__
				from settings import config as settings
				from settings import routes
				base_root=self.app.admin.__path__





				contenido=self.data["model"]["global"].obtenerContenido(self.data["app"],"apps")[self.data["app"]]
				if len(contenido)>1:
					for k,elem in enumerate(contenido[1]):

						if contenido[1][elem]["value"] in settings.dbs:
							
							
							exec("model"+str(k)+"=imp.load_source('model"+str(k)+"' ,'"+self.app.admin.modelos.__path__+str(contenido[1][elem]["value"])+"_model.py').model")
							
							exec("self.data['model']['"+contenido[1][elem]["value"]+"']=model"+str(k)+"('"+self.app.admin.modelos.__path__+contenido[1][elem]["value"]+"','"+self.app.admin.modelos.__path__+"request/','"+self.data["app"]+"',ext='.py')")	
							
							self.data["model"][contenido[1][elem]["value"]].models["global"]=self.data["model"]["global"]
							self.data["model"]["global"].models[contenido[1][elem]["value"]]=self.data["model"][contenido[1][elem]["value"]]
							
							if "Opciones" in self.data["model"][contenido[1][elem]["value"]].db.tablas:
								self.data["opciones"][contenido[1][elem]["value"]]=self.data["model"][contenido[1][elem]["value"]].obtenerFilas("Opciones")
							if self.data["model"][contenido[1][elem]["value"]].errores!=[]:
								self.data["errores"].append(self.data["model"][contenido[1][elem]["value"]].errores)
							elif self.data["model"][contenido[1][elem]["value"]].db.errores:
								self.data["errores"].append(self.data["model"][contenido[1][elem]["value"]].db.errores)
					for k,elem in enumerate(contenido[2]):

						if contenido[2][elem]["value"] in settings.dbs:

							
							exec("model"+str(k)+"=imp.load_source('model"+str(k)+"' ,'../"+config.modelos_folder+str(contenido[2][elem]["value"])+"_model.py').model")
							exec("self.data['model']['"+contenido[2][elem]["value"]+"']=model"+str(k)+"('"+base_root+routes.models_folder+contenido[2][elem]["value"]+"','"+base_root+routes.models_folder+"request/','"+self.data["app"]+"',ext='.py')")	
							self.data["model"][contenido[2][elem]["value"]].models["global"]=self.data["model"]["global"]
							self.data["model"]["global"].models[contenido[2][elem]["value"]]=self.data["model"][contenido[2][elem]["value"]]
							
							if "Opciones" in self.data["model"][contenido[2][elem]["value"]].db.tablas:
								self.data["opciones"][contenido[2][elem]["value"]]=self.data["model"][contenido[2][elem]["value"]].obtenerFilas("Opciones")
							if self.data["model"][contenido[2][elem]["value"]].errores!=[]:
								self.data["errores"].append(self.data["model"][contenido[2][elem]["value"]].errores)
							elif self.data["model"][contenido[2][elem]["value"]].db.errores:
								self.data["errores"].append(self.data["model"][contenido[2][elem]["value"]].db.errores)



			
			if  self.data["manager"]==True and gringolizar(self.data["global_control"]) in config.controladores:
				
				if self.data["global_control"]=="Plugin":
					for plugin in self.data["model"]["global"].obtenerFilas("Plugins"):

						for elem in plugin[1][1]:
							self.data["plugins-hooks"].append([elem["name"],elem["value"]])

						
						self.data["plugins"][plugin[0]]=imp.load_source("",config.base_root+config.plugins_folder+plugin[0]+"/default.py").Plugin(self.data)
					

				control=imp.load_source("",config.base_root+config.controller_folder+"Controladores/"+gringolizar(self.data["global_control"])+".py")

				exec("control=control."+gringolizar(self.data["global_control"])+"(self.data)")

				
				if self.data["metodo"]!=None and self.data["metodo"] in dir(control):


					exec("control."+gringolizar(self.data["metodo"])+"()")
				"""
				Pendiente ya que plugin no lo utilizaria ya que el metodo desconocido des del plugin que carga no del global_control
				elif self.data["metodo"]!=None:
					
					exec("control.metodo_desconocido()")
				"""






			else:
				self.HEADERS.show()

				from modulos.ztec.intervalor.control import generar2
				generar2(config.base_root+config.vistas_folder+self.vista+".html",config.base_root+config.vistas_folder+config.templates_folder+self.vista+".py","#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
				doc=""
				f=open(config.base_root+config.vistas_folder+config.templates_folder+self.vista+".py","r")
				script=f.read()
				exec(script)
				print doc
		
		



			






		
		
	def run(self):
		pass
		
