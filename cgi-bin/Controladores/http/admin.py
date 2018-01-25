# -*- coding: utf-8 -*-
from modulos.controlador import Controlador
from Controladores.http.adminCore import adminCore
import re
from settings import config as settings
from settings import routes
from config import config









def preLoad(data):
	
	if type(data["metodo"])==str:

		if "Pagina" in data["metodo"]:

			from Controladores.http.Paginas import Paginas
			class admin(adminCore,Paginas):
				def __init__(self,data):
					
					Paginas.__init__(self,data)
					adminCore.__init__(self,data)
		elif "Entrada" in data["metodo"]:
			from Controladores.http.Entradas import Entradas
			class admin(adminCore,Entradas):
				def __init__(self,data):
					
					Entradas.__init__(self,data)
					adminCore.__init__(self,data)
		elif re.search("[F|f]ormularios?",data["metodo"]):
			from Controladores.http.Formularios import Formularios
			class admin(adminCore,Formularios):
				def __init__(self,data):
					Formularios.__init__(self,data)
					adminCore.__init__(self,data)

		elif "Archivo" in data["metodo"]:
			from Controladores.http.Archivos import Archivos
			class admin(adminCore,Archivos):
				def __init__(self,data):
					
					Archivos.__init__(self,data)
					adminCore.__init__(self,data)
		elif "Plantilla" in data["metodo"]:
			
			from Controladores.http.Plantillas import Plantillas
			class admin(adminCore,Plantillas):
				def __init__(self,data):
					Plantillas.__init__(self,data)
					adminCore.__init__(self,data)
		elif "Menu" in data["metodo"]:
			
			from Controladores.http.Menus import Menus
			

			class admin(adminCore,Menus):
				def __init__(self,data):
					Menus.__init__(self,data)
					adminCore.__init__(self,data)

		elif "Ayuda" in data["metodo"]:
			
			from Controladores.http.Ayudas import Ayudas
			class admin(adminCore,Ayudas):
				def __init__(self,data):
					Ayudas.__init__(self,data)
					adminCore.__init__(self,data)
		elif re.search("Usuarios?",data["metodo"]):
			
			from Controladores.http.Usuarios import Usuarios
			class admin(adminCore,Usuarios):
				def __init__(self,data):
					Usuarios.__init__(self,data)
					adminCore.__init__(self,data)
		elif "globalUser" in data["metodo"]:
			
			from Controladores.http.globalUser import Usuarios
			class admin(adminCore,Usuarios):
				def __init__(self,data):
					
					Usuarios.__init__(self,data)
					adminCore.__init__(self,data)
		elif data["metodo"]=="Show":
			from Controladores.http.ShowAdmin import ShowAdmin
			class admin(adminCore,ShowAdmin):
				def __init__(self,data):
					ShowAdmin.__init__(self,data)
					adminCore.__init__(self,data)
		
		else:
			class admin(adminCore):
				def __init__(self,data):
					adminCore.__init__(self,data)
	else:

		class admin(adminCore):
				def __init__(self,data):


					adminCore.__init__(self,data)
	
	return admin