
from modulos.controlador import Controlador
from modulos.ztec.zred import normalizar

from settings import config as settings
from settings import routes
from config import config

class ShowAdmin(Controlador):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar
		Controlador.__init__(self,data)

	def Show(self):
		"""
		Este metodo se usa para mostrar datos planos en el framework
		"""
		if self.data["login"]:
		    self.HEADERS.show()
			
		    if "db" in normalizar(self.data["kwargs"]):
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
		    if "path" in self.data["kwargs"] and (self.data["user"]["permisologia"]==0 or self.data["user"]["permisologia"]==1):
		     
		     if self.data["kwargs"]["path"][0]=="admin":
		      if self.data["kwargs"]["path"][1]=="Template":

		       print config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir
		      elif self.data["kwargs"]["path"][1]=="Widget":

		       print config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder
		     elif  normalizar(self.data["kwargs"])["path"][0]=="user":
		      if normalizar(self.data["kwargs"])["path"][1]=="Template":
		       print config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir
		      elif normalizar(self.data["kwargs"])["path"][1]=="Widget":
		       print config.base_root+(config.apps_dir+"/" if self.dat["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_folder+routes.widgets_folder
		     elif  self.data["kwargs"]["path"][0]=="Controlador":
		      print config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+config.controller_folder
		     elif  self.data["kwargs"]["path"][0]=="Modelo":
		      print config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.models_folder


		    
		    

		    if list(normalizar(self.data["kwargs"]))==["widget"]:
		        import os		     
		        if normalizar(self.data["kwargs"])["widget"].strip()+".html" in os.listdir(config.base_root+config.apps_dir+"/"+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder if normalizar(self.data["isglobal"])==False else "../"+config.vistas_folder+"widgets/"):

		          f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder+normalizar(self.data["kwargs"])["widget"].strip()+".html" if normalizar(self.data["isglobal"])==False else "../"+config.vistas_folder+"widgets/"+normalizar(self.data["kwargs"])["widget"].strip()+".html","r")
		          print f.read()
		          f.close()
		        else:
		          print None
		     
		    elif self.data["kwargs"]=={"Contacto":"jesus26abraham1996@gmail.com"}:
		     
		     print "data['Contactos']="+str(modelo.obtenerContactos(self.data["kwargs"]["Contacto"]))

		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="Controlador":

		     try:

		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+decode(self.data["kwargs"]["Controlador"]).strip()+".py","r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+decode(self.data["kwargs"]["Controlador"]).strip()+".py"
		      print f.read()
		      f.close()
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="Modelo":

		     try:

		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+decode(self.data["kwargs"]["Modelo"]).strip()+".py","r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+decode(self.data["kwargs"]["Modelo"]).strip()+".py"
		      print f.read()
		      f.close()
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="user":
		     

		     try:
		      
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir+"/"+self.data["kwargs"]["user"].strip()+".html","r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_folder+self.data["kwargs"]["user"].strip()+".html"
		      print f.read()
		      f.close()
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="admin":

		     try:
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir+"/"+self.data["kwargs"]["admin"].strip()+".html","r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_folder+self.data["kwargs"]["admin"].strip()+".html"
		      print f.read()
		      f.close()
		     except:
		      pass
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="user-widgets":

		     try:
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir+"/"+routes.widgets_folder+"/"+self.data["kwargs"]["user-widgets"].strip()+".html","r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir+"/"+routes.widgets_folder+"/"+self.data["kwargs"]["user-widgets"].strip()+".html"
		      print f.read()
		      f.close()
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="admin-widgets":

		     try:
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir+"/"+routes.widgets_folder+self.data["kwargs"]["admin-widgets"].strip()+".html","r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir+"/"+routes.widgets_folder+self.data["kwargs"]["admin-widgets"].strip()+".html"
		      print f.read()
		      f.close()
		    
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="user-scripts":

		     try:
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+settings.static_dir+"/"+self.data["kwargs"]["user-scripts"].strip(),"r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/user/"+settings.static_dir+"/"+self.data["kwargs"]["user-scripts"].strip()
		      print f.read()
		      f.close()
		    
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="admin-scripts":

		     try:
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+settings.static_dir+"/"+self.data["kwargs"]["admin-scripts"].strip(),"r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+settings.static_dir+"/"+self.data["kwargs"]["admin-scripts"].strip()
		      print f.read()
		      f.close()
		    
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="globales-scripts":

		     try:
		      
		      f=open(config.base_root+config.static_folder+self.data["kwargs"]["globales-scripts"].strip(),"r")
		      print "#"+config.base_root+config.static_folder+self.data["kwargs"]["globales-scripts"].strip()
		      print f.read()
		      f.close()
		    
		     except Exception,e:
		      print e      
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="ajustes":

		     try:
		      
		      f=open(config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+self.data["kwargs"]["ajustes"].strip(),"r")
		      print "#"+config.base_root+(config.apps_dir+"/" if self.data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+self.data["kwargs"]["ajustes"].strip()
		      print f.read()
		      f.close()
		    
		     except Exception,e:
		      print e
		    elif len(list(self.data["kwargs"]))>0 and list(self.data["kwargs"])[0]=="Plugin":
		     

		     try:
		      f=open(config.base_root+config.plugins_folder+self.data["kwargs"]["Plugin"].strip(),"r")
		      print "#"+config.base_root+config.plugins_folder+self.data["kwargs"]["Plugin"].strip()
		      print f.read()
		      f.close()
		    
		     except Exception,e:
		      print e
		    elif list(self.data["kwargs"])==["Contacto"]:
		      contacto=self.data["model"]["conversaciones"].obtenerContacto(self.data["kwargs"]["Contacto"])
		      print contacto
		      pass
		    elif self.data["args"]==["Contactos"]:
		      contactos=self.data["model"]["conversaciones"].obtenerContactos()
		      print contactos
		      pass
		    else:
		      pass	
		else:
			self.HEADERS.show()
			print "None"