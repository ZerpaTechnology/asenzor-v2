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
#==============================================================
#SETTINGS
vistas_folder="vistas"
vistas_dir=vistas_folder+"/"
import sys
sys.path.append("../modulos/ztec/")
global_config=imp.load_source("global_config","../config/config.py")
config=imp.load_source("","../plugins/"+__name__+"/config.py")
from settings import config as settings
from settings import routes
from zred import Shortcode

from intervalor.control import generar2

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
	def __init__(self,modelos):
		global config
		global settings
		global routes
		self.models={}
		self.app_models=modelos
		
		for w in config.widgets:
			generar2(global_config.base_root+global_config.plugins_folder+__name__+"/widgets/"+w+".html",global_config.base_root+global_config.plugins_folder+__name__+"/widgets/"+w+".py","#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")

		for elem in config.modelos:

			self.models[elem]=imp.load_source(elem+"_model","../plugins/"+__name__+"/modelos/"+elem+"_model.py").model(
				global_config.apps_folder+settings.app+"/admin/"+routes.models_folder+"plugins/"+__name__+"/"+elem,
				"../request/","user",ext=".py"
				)
			self.models[elem].models=modelos
		self.shortcodes={}
		for elem in config.shortcodes:
			
			self.shortcodes[elem]=imp.load_source(elem+"_model","../plugins/"+__name__+"/shortcodes/"+elem+".py").shortcode(
				self.models,self.app_models)


		
	def cnt(self,data):
		"""
		Este es el docstrings
		"""
		global config

	def action(self,data,p):
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


