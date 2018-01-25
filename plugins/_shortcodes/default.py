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
__path__=__file__[:__file__.rfind("/")]
#==============================================================
#SETTINGS
vistas_folder="vistas"
vistas_dir=vistas_folder+"/"
import sys

from config import config
from settings import config as settings
from settings import routes
sys.path.append(__path__)

from modulos.Plugin import Plugin, Shortcode







plugin_settings=imp.load_source("plugin_settings",__path__+"/config.py")
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
		

class Plugin:
	"""docstring for Plugin"""
	def __init__(self,data):
		from modulos.ztec.zred import  Headers
		self.HEADERS=Headers()
		
		self.model={}
		self.data=data
		self.HEADERS.show()
		self.app_model=self.data["model"]		
		
		
	def cnt(self,data):
		"""
		Este es el docstrings
		"""
		global config
	def metodo_desconocido(self):
		pass


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


