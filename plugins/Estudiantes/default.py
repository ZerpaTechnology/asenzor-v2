# -*- coding: utf-8 -*-
#==============================================================
#IMPORTACION DE LIBRERIAS
import os
import imp
#==============================================================

#META TAGS (globales)
__name__=__file__.split("/")[-2]
__version__="v0.0.1"
__author__="Jesus Abraham Zerpa Maldonado"
__email__="jesus26abraham1996@gmail.com"
__website__="https://zerpatechnology.com.ve"
__license__="GNU LESSER GENERAL PUBLIC LICENSE"
__path__=__file__[:__file__.rfind("/")+1]
#==============================================================
#SETTINGS
vistas_folder="vistas"
vistas_dir=vistas_folder+"/"
import sys

from config import config


sys.path.append(__path__)

from modulos.Plugin import Shortcode,Plugin






from modulos.ztec.intervalor.control import generar2
from modulos.ztec.zred import redirecter

plugin_settings=imp.load_source("",__path__+"plugin.py")
from Controladores.http.Login import Login

from modulos.Plugin import Plugin as plugin



#clase padre


								

class Widget(Shortcode):
	"""docstring for shor2"""
	def run(self,args=None,content=None,exterior=None):
		parametros={}
		
		
		if args!=None:
			"""
			if nargs!="":
				nargs=nargs.split(" ")
				for arg in nargs:
					clave,valor=arg.split("=")
					parametros[clave]=valor
			"""
		return "plugin incluido"			
		

class Plugin(plugin):
	"""docstring for Plugin"""
	def __init__(self,data):

		plugin.__init__(self,plugin_settings,data)



		self.ruta_widget=config.base_root+config.plugins_folder+plugin_settings.name+"/"+plugin_settings.widgets_folder
		self.ruta_python=config.base_root+config.plugins_folder+plugin_settings.name+"/"+plugin_settings.widgets_folder


		
	def Registrar(self):


		self.HEADERS.set_headers({"Content-type":"text/html"})
		self.HEADERS.show()

		
		
		print self.do_shortcode("["+plugin_settings.name+"-"+self.data["metodo"]+"]")

		
	def cnt(self,data):
		"""
		Este es el docstrings
		"""
		global config
	def metodo_desconocido(self):
		self.HEADERS.show()
		print "Esto no es un metodo del plugin"

	def widget(self):
		if len(self.data["args"])>0:
			self.HEADERS.set_headers({"Content-type":"text/html\n"})
			self.HEADERS.show()
			print self.incluir(self.data,"head",isglobal=True)
			print self.do_shortcode(self.data["args"][0])
			#print self.incluir(self.data,self.data["args"][0])



	def Entrar(self):

		self.HEADERS.set_headers({"Content-type":"text/html\n"})
		
		estudiante=self.model["main"].obtenerEstudiante(expediente=self.data["request"]["expediente"].value)

		if estudiante!=None:

		
			self.login.Entrar(estudiante[0]["email"]["value"],self.data["request"]["password"].value)

			redirecter(config,"Plugin",plugin_settings.name,"sc","iframe",sc="login",manager=True,app=self.data["app"])()
			

	def action(self,data):
		global config
'''
#==============================================================
def cnt(data,methods,modelos):
	"""
	Es el actuador en metodos get del FMK.
	"""
	plugin=Plugin(modelos)

	if data["args"]["plugin"]==__name__:
		if "action" in data["args"]:
			pass


def action(data,args,modelos):
	"""
	Es el actuador de los metodos post en el FMK.
	"""
	for modelo in modelos:
		if modelo.dbfile=="main":
			pass
		elif modelo.dbfile=="negocios":
			pass
'''


