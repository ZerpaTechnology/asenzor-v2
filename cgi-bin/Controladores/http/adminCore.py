# -*- coding: utf-8 -*-


from Controladores.http.Login import Login
from settings import config as settings
from settings import routes
from config import config
from modulos.ztec.zred import normalizar,renderTree,decode


class adminCore(Login):
	def __init__(self,data):
		from modulos.ztec import zu
		
		Login.__init__(self,data)
		self.isglobal=True

		#------------------------------------------------
		#SECCION DE VARIABLES CONTRSTRUCTORAS
		self.data["creditos"]=self.data["model"]["global"].obtenerCreditos(settings.app)[settings.app]
		self.data["adminMenu"]=self.data["model"]["main"].obtenerAdminMenu()
		self.data["archivos"]=self.data["model"]["archivos"].obtenerFilas("Archivos")
		self.data["actionbase"]="app="+settings.app+"&vista=index&admin=True"
		self.modelo=data["model"]["main"]
		self.data["licencias"]=config.licencias
		#-------------------------------
		#SECCION DE HOOKS
		self.data["hook1"]=[ 
             ["listar",["list"]], 
             ["content",["content"]],
             ["editar",["edit"]],
             ["editar2",["edit2"]],
             ["editar3",["edit3"]],
             ["codear",["edit2"]],
             ["plugins",["gestor"]],
             ["plugin",["plugin"]],
             ["post",["post"]],
             ["update",["update"]],
             ["allapps",["gestor"]],
             ["menus",["menus"]],
             ["explorar",["explorar"]],
             ["download",["download"]],
        ]
		self.data["base_url"]=config.base_url+config.apps_folder+settings.app+"/user/"

		
		#--------------------------------
		#SECCION DE SELECCION DE VISTA
		if  self.data["login"]==True:
			self.vista="index"
			self.data["vars"]["login"]=True
		else:
			self.vista="login"
			self.data["vars"]["login"]=False
		#--------------------------------
		#SECCION DE ACCIONES
		if self.data["login"]==True :

			if self.data["action"]=="allapps":

				import os

				import urllib,urllib2
				from modulos.ztec.zu import redict


				l=self.data["model"]["global"].obtenerFilas("apps")
				for k,elem in enumerate(l):
					if os.path.isdir("../"+config.apps_folder+elem[0]):
						l[k][1].append({"Screenshot":"url","name":"screenshot","value":config.base_url+config.apps_folder+elem[0]+"/screenshot.png"})
				data["items"]=l
				params = urllib.urlencode({"global_control":"apps","metodo":"allapps","manager":True})
				self.HEADERS.show()
				print config.asenzor_host
				f=urllib2.urlopen(config.asenzor_host,params)

				item=redict(normalizar(f.read()))

				data["items-destacadas"]=item["Destacada"]
				data["items-populares"]=item["Populares"]
				data["items-recientes"]=item["Recientes"]
				data["items-favoritos"]=item["Favoritos"]
				f.close()
			
			elif self.data["action"]=="plugins":
				import os
				import urllib,urllib2
				from modulos.ztec.zu import redict

				l=self.data["model"]["global"].obtenerFilas("Plugins")
				l2=self.data["model"]["main"].obtenerFilas("Plugins")
				for k,elem in enumerate(l):
					if os.path.isdir("../"+config.plugins_folder+elem[0]):
						l[k][1].append({"Screenshot":"url","name":"screenshot","value":config.base_url+config.plugins_folder+elem[0]+"/screenshot.png"})
						self.HEADERS.show()
				data["items"]=l
				params = urllib.urlencode({"global_control":"plugins","manager":True})
				f=urllib2.urlopen(config.asenzor_host,params)
				item=redict(normalizar(f.read()))
				data["items-destacadas"]=item["Destacada"]
				data["items-populares"]=item["Popular"]
				data["items-recientes"]=item["Reciente"]
				data["items-favoritos"]=item["Favorita"]
				f.close()
			elif self.data["action"]=="editar2" or self.data["action"]=="codear":
				app=settings.app


				if list(self.data["kwargs"])==["Diseño"]:
					self.data["titulo"]="Diseños"
					user="../"+config.apps_dir+"/"+app+"/user/"+routes.vistas_folder
					admin="../"+config.apps_dir+"/"+app+"/admin/"+routes.vistas_folder
					globales=config.base_root+config.vistas_folder
					self.data["trees"]=[{"user":zu.treeFolder(user)},
						{"admin":zu.treeFolder(admin)},
						]
					if self.data["isGlobalUser"]:
						self.data["trees"].append({"global":zu.treeFolder(globales)})
					self.data["excluir"]=".py"
				elif list(self.data["kwargs"])==["Controlador"]:
					self.data["titulo"]="Controles"
					user="../"+config.apps_dir+"/"+app+"/user/"+routes.controller_folder
					globales=config.base_root+config.controller_folder

					self.data["trees"]=[{"user":zu.treeFolder(user)},
					]
					if self.data["isGlobalUser"]:
						self.data["trees"].append({"global":zu.treeFolder(globales)})
					self.data["excluir"]=".pyc"
				elif list(self.data["kwargs"])==["Modelo"]:
					self.data["titulo"]="Modelos"
					admin="../"+config.apps_dir+"/"+app+"/admin/"+routes.models_folder
					globales=config.base_root+config.modelos_folder
					self.data["trees"]=[{"admin":zu.treeFolder(admin)},
					]
					if self.data["isGlobalUser"]:
						self.data["trees"].append({"global":zu.treeFolder(globales)})
					self.data["excluir"]=".pyc"
				elif list(self.data["kwargs"])==["Script"]:
					self.data["titulo"]="Scripts"
					user="../"+config.apps_dir+"/"+app+"/user/"+routes.static_folder
					admin="../"+config.apps_dir+"/"+app+"/admin/"+routes.static_folder
					globales=config.base_root+"static/"

					self.data["trees"]=[{"user":zu.treeFolder(user)},{"admin":zu.treeFolder(admin)},]
					if self.data["isGlobalUser"]:
						self.data["trees"].append({"global":zu.treeFolder(globales)})

					self.data["excluir"]=".pyc"   
				elif list(self.data["kwargs"])==["Ajustes"]:
					self.data["titulo"]="Ajustes"
					admin="../"+config.apps_folder+app+"/admin/"+config.settings_folder
					_global="../config/"
					self.data["trees"]=[{"admin":zu.treeFolder(admin),}]
					if self.data["isGlobalUser"]:
						self.data["trees"].append({"global":zu.treeFolder(_global),})
					self.data["excluir"]=".pyc"
				elif list(self.data["kwargs"])==["Plugin"]:
					self.data["titulo"]="Plugins"
					admin=config.base_root+config.plugins_folder
					self.data["trees"]=[{"plugins":zu.treeFolder(admin),}]
					self.data["excluir"]=[".pyc"]
				self.data["renderTree"]=renderTree
			elif self.data["action"]=="editar":
				self.data["vars"]["opciones"]=self.data["opciones"]
				self.data["vars"]["Tablas"]=["Usuarios","Formularios"]
				self.data["vars"]["modelos"]=["formularios"]
				self.data["vars"]["campos"]=["formularios"]				
				self.data["vars"]["boxes"]=[[{"Titulo":"text","name":"nombre","value":"aaaa"}]]	
			elif self.data["action"]=="personalizar":
				self.vista="personalizar"
				self.data["vars"]["categorias"]=self.data["model"]["archivos"].obtenerFilas("Opciones")[3][1]
				self.data["vars"]["tipos"]=self.data["model"]["archivos"].obtenerFilas("Opciones")[4][1]
				self.servir()							
		
			
		   
	def consultarLogin(self):		  
		self.HEADERS.show()

		print self.data["login"]
	def optimizarImagenes(self):
		self.HEADERS.set_headers({"Connection": "Keep-Alive\n","Keep-Alive": "timeout=60, max=3600\n"})
		self.HEADERS.show()
		if self.data["login"]:
			try:
			    
				
				
				from modulos.ztec.zgrafic import postOptimizar
				postOptimizar(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"archivos/Imagenes/")
			except Exception as e:
				pass
			print "Optimización finalizada"
						

	def Plugin(self):
		self.HEADERS.show()
		
		exec('self.data["plugins"]["'+str(self.data["args"][0])+'"].'+str(self.data["args"][1])+"()")
		self.servir()

	def Show(self):
		self.HEADERS.set_headers({"Content-type":"text/plain"})
		self.HEADERS.show()
		from modulos.ztec.intervalor.control import generar2
		import os
		
		if self.data["login"]:
		    
			
		    if "db" in normalizar(self.data["kwargs"]):
		     """
		     Muestra contenido directamente desde la base de datos
		     """
		     if "id" in normalizar(self.data["kwargs"]) and normalizar(self.data["kwargs"])["id"]!=None:
		      tabla=None
		      for elem in list(self.data["model"]["main"].db.tablas):
		        if len(self.data["model"]["main"].db.tablas[elem])>0:
		          temp=self.data["model"]["main"].db(elem).obtenerFilaValores(0)
		          if len(temp)>2:
		            if normalizar(self.data["kwargs"])["tabla"]==list(temp[2])[0]:
		              tabla=elem
		      if tabla!=None:
		        print self.data["model"][normalizar(self.data["kwargs"])["db"]].obtenerFilas(tabla)[normalizar(self.data["kwargs"])["id"]]

		     else:


		      if normalizar(self.data["kwargs"])["tabla"] in list(self.data["model"]["main"].db.tablas):


		        for elem in list(self.data["model"]["main"].db.tablas):


		          if len(self.data["model"]["main"].db.tablas[elem])>0:

		            temp=self.data["model"]["main"].db(elem).obtenerFilaValores(0)

		            if len(temp)>2:
		              
		              if normalizar(self.data["kwargs"])["tabla"]==list(temp[2])[0]:

		                tabla=elem
		        print self.data["model"][normalizar(self.data["kwargs"])["db"]].obtenerFilas(normalizar(self.data["kwargs"])["tabla"])
		      else:
		        print self.data["model"][normalizar(self.data["kwargs"])["db"]].obtenerFilas(normalizar(self.data["kwargs"])["tabla"])

		    if len(self.data["args"])>2:
			    """
		    	Muestra el codigo de diseños, modelos y controladores
		    	"""

			    if self.data["args"][0]=="layout":
			    	if self.data["args"][1]=="user":
			    		
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+"/".join(self.data["args"][2:])):

			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1]

				    			generar2(config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+(routes.templates_folder if self.data["args"][2]!=routes.widgets_dir else "")+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+(routes.templates_folder if self.data["args"][2]!=routes.widgets_dir else "")+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()

			    		else:
			    			print None
			    	elif self.data["args"][1]=="admin":
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1]
				    			generar2(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+(routes.templates_folder if self.data["args"][2]!=routes.widgets_dir else "")+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+(routes.templates_folder if self.data["args"][2]!=routes.widgets_dir else "")+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()
			    		else:
			    			print None
			    	elif self.data["args"][1]=="global":
			    		
			    		if os.path.exists(config.base_root+config.vistas_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.vistas_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.vistas_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1]
				    			generar2(config.base_root+config.vistas_folder+"/".join(self.data["args"][2:]),config.base_root+config.vistas_folder+(routes.templates_folder if self.data["args"][2]!=routes.widgets_dir else "")+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.vistas_folder+(routes.templates_folder if self.data["args"][2]!=routes.widgets_dir else "")+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()

			    		else:
			    			print None
			    		pass
			    	
			    elif self.data["args"][0]=="controlador":

			    	if self.data["args"][1]=="user":
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			"""
				    			ext=self.data["args"][-1].split(".")[-1]
				    			generar2(config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()
				    			"""
			    		else:
			    			print None
			    	elif self.data["args"][1]=="global":
			    		if os.path.exists(config.base_root+config.controller_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.controller_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.controller_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			"""
				    			ext=self.data["args"][-1].split(".")[-1]
				    			generar2(config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()
				    			"""
			    		else:
			    			print None
			    elif self.data["args"][0]=="plugins":
			    	
			    		if os.path.exists(config.base_root+config.plugins_folder+"/".join(self.data["args"][1:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.plugins_folder+"/".join(self.data["args"][1:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.plugins_folder+"/".join(self.data["args"][1:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			
				    			ext=self.data["args"][-1].split(".")[-1]
				    			_ext=self.data["ext"] if "ext" in self.data else "py"
				    			generar2(config.base_root+config.plugins_folder+"/".join(self.data["args"][1:]),config.base_root+config.plugins_folder+"/".join(self.data["args"][1:])[:-len(ext)]+_ext)
				    			f=open(config.base_root+config.plugins_folder+"/".join(self.data["args"][1:])[:-len(ext)]+_ext,"r")
				    			print f.read()
				    			f.close()
				    			
			    		else:
			    			print None			    		

			    elif self.data["args"][0]=="modelo":
			    	if self.data["args"][1]=="admin":
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1]
				    			generar2(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()
			    		else:
			    			print None
			    	elif self.data["args"][1]=="global":

			    		if os.path.exists(config.base_root+config.modelos_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.modelos_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.modelos_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1]
				    			generar2(config.base_root+config.modelos_folder+"/".join(self.data["args"][2:]),config.base_root+config.modelos_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py")
				    			f=open(config.base_root+config.modelos_folder+"/".join(self.data["args"][2:])[:-len(ext)]+"py","r")
				    			print f.read()
				    			f.close()
			    		else:
			    			print None
			    elif self.data["args"][0]=="static":
			    	if self.data["args"][1]=="user":
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1] 
				    			_ext="py" if "ext" not in self.data else self.data["ext"]
				    			generar2(config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+"/".join(self.data["args"][2:])[:-len(ext)]+_ext)
				    			f=open(config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+"/".join(self.data["args"][2:])[:-len(ext)]+_ext,"r")
				    			print f.read()
				    			f.close()


			    		else:
			    			print None
			    	elif self.data["args"][1]=="admin":
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1] if "ext" not in self.data else self.data["ext"]
				    			_ext="py" if "ext" not in self.data else self.data["ext"]
				    			generar2(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/".join(self.data["args"][2:]),config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/".join(self.data["args"][2:])[:-len(ext)]+_ext)
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/".join(self.data["args"][2:])[:-len(ext)]+_ext,"r")
				    			print f.read()
				    			f.close()
			    		else:
			    			print None
			    	elif self.data["args"][1]=="global":
			    		if os.path.exists(config.base_root+config.static_folder+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.static_folder+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.static_folder+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		elif self.data["action"]=="componer":
				    			ext=self.data["args"][-1].split(".")[-1] 
				    			_ext="py" if "ext" not in self.data else self.data["ext"]
				    			generar2(config.base_root+config.static_folder+"/".join(self.data["args"][2:]),config.base_root+config.static_folder+"/".join(self.data["args"][2:])[:-len(ext)]+_ext)
				    			f=open(config.base_root+config.static_folder+"/".join(self.data["args"][2:])[:-len(ext)]+_ext,"r")
				    			print f.read()
				    			f.close()


			    		else:
			    			print None
			    elif self.data["args"][0]=="ajustes":
			    	
			    	if self.data["args"][1]=="admin":
			    		if os.path.exists(config.base_root+config.apps_folder+settings.app+"/admin/settings/"+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+config.apps_folder+settings.app+"/admin/settings/"+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+config.apps_folder+settings.app+"/admin/settings/"+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		
			    		else:
			    			print None
			    	elif self.data["args"][1]=="global":
			    		if os.path.exists(config.base_root+"config/"+"/".join(self.data["args"][2:])):
			    			if self.data["action"]==None or self.data["action"]=="router":
			    				print config.base_root+"config/"+"/".join(self.data["args"][2:])
			    			if self.data["action"]==None or self.data["action"]=="incluir":
				    			f=open(config.base_root+"config/"+"/".join(self.data["args"][2:]),"r")
				    			print f.read()
				    			f.close()
				    		

			    		else:
			    			print None
			    			    
			    elif self.data["args"][0]=="path":
					if self.data["args"][1]=="admin":
						if self.data["args"][2]=="layouts":
							print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder
						elif self.data["args"][2]=="widgets":
							print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder
						elif self.data["args"][2]=="modelos":
							print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder

					elif self.data["args"][1]=="user":
						if self.data["args"][2]=="layouts":
							print config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder
						elif self.data["args"][2]=="widgets":
							print config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder+routes.widgets_folder
						elif self.data["args"][2]=="controladores":
							print config.base_root+config.apps_folder+settings.app+"/user/"+routes.controller_folder
						

		else:
			self.HEADERS.show()
			print "None"
		pass
	def write(self):

		if self.data["login"]:
				if self.data["user"]["permisologia"]==0:
				       self.HEADERS.show()
				       
				       f=open(decode(self.data["request"]["path"].value),"w")
				       f.write(decode(self.data["request"]["file"].value))
				       f.close()
				       print "Archivo guardado"
				else:
					self.HEADERS.show()
					print self.data["user"]["permisologia"]==0
					print "No tiene permisos para hacer esto"
		   
	def delete(self):
			if self.data["login"]:
				if self.data["user"]["permisologia"]==0:
				      import os
				      self.HEADERS.show()
				      os.remove(self.data["args"]["path"])
		
				      print "El archivo a sido eliminado"
				else:
				      self.HEADERS.show()
				      print "No tiene permisos para hacer esto"



