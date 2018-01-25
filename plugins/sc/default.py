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
from modulos.ztec.zred import redirecter,decode
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

		
		




	def Shortcodes(self):
		self.HEADERS.show()

		self.data["titulo"]="Shortcodes"
		self.data["Tabla"]="Shortcodes"
		
		self.data["plugin"]=plugin_settings.name


		self.data["Modelos-plugin"]=["shortcodes"]

		from modulos.ztec.zred import listar

		listar(self.data,config)
	def Galerias(self):
		self.HEADERS.show()
		self.data["titulo"]="Shortcodes"
		self.data["Tabla"]="Galerias"
		
		self.data["plugin"]=plugin_settings.name

		self.data["Modelos-plugin"]=["galerias"]

		from modulos.ztec.zred import listar

		listar(self.data,config)
	def Galeria(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar,gringolizar,redirecter
		
		if self.data["ajax"]==False:
			if self.data["action"]=="editar":
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()



				self.data["repeate"]=1
				self.data["plantillas"]=self.model["main"].obtenerFilas("Plantillas")


				
				keys=self.data["args"][1]


				i=self.data["args"][2]

				self.data["categorias"]={}

				self.data["titulo"]=self.data["metodo"]

				if i!=None:
					self.data["categorias"]={}


					tabla=self.model["galerias"].obtenerFilas("Galerias")[i]

					self.data["titulo"]=tabla[0]


					self.data["meta-layout"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"layout")
					self.data["meta-control"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"control")

					self.data["post"]=""
					self.data["control-post"]=gringolizar(self.data["titulo"],"-")


					
					l1=self.data["plugins"][plugin_settings.name].model["galerias"].obtenerFilas("Galerias")[i][1]
					self.data["boxes"]=[l1]
					self.data["vars"]={"titulos":[],"actual":self.data["titulo"]}

					for elem in self.data["plugins"][plugin_settings.name].model["galerias"].obtenerFilas("Galerias"):
						self.data["vars"]["titulos"].append(elem[0])

				else:
					self.data["titulo"]="Crea una nueva pagina"
					self.data["meta-layout"]=self.data["titulo"]
					self.data["post"]=gringolizar(self.data["titulo"],"-")
					self.data["control-post"]="Inicio"
					self.data["boxes"]=[self.model["galerias"].obtenerEstructura("Galerias")[1]]
				
				modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
				tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]

				self.data["vars"]["modelos"]=modelos
				self.data["vars"]["opciones"]=self.data["opciones"]
				self.data["vars"]["Tablas"]=tablas


				
			elif self.data["action"]=="save":           
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()

				if self.data["args"][2]!=None:

					self.model["galerias"].modificarGaleria(self.data["args"][2],self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Plugin",plugin_settings.name,"Galerias",action="listar")()
				else:

					self.model["galerias"].crearGaleria(self.data["request"],self.data["metadatos"])
				
					redirecter(config,settings.app,"admin","Plugin",plugin_settings.name,"Galeria",self.data["args"][2],action="listar")()
	def Sliders(self):
		self.HEADERS.show()
		self.data["titulo"]="Shortcodes"
		self.data["Tabla"]="Sliders"
		
		self.data["plugin"]=plugin_settings.name

		self.data["Modelos-plugin"]=["galerias"]

		from modulos.ztec.zred import listar

		listar(self.data,config)
	def Slider(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar,gringolizar,redirecter
		
		if self.data["ajax"]==False:
			if self.data["action"]=="editar":
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()



				self.data["repeate"]=1
				self.data["plantillas"]=self.model["main"].obtenerFilas("Plantillas")


				
				keys=self.data["args"][1]


				i=self.data["args"][2]

				self.data["categorias"]={}

				self.data["titulo"]=self.data["metodo"]

				if i!=None:
					self.data["categorias"]={}


					tabla=self.model["galerias"].obtenerFilas("Sliders")[i]

					self.data["titulo"]=tabla[0]


					self.data["meta-layout"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"layout")
					self.data["meta-control"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"control")

					self.data["post"]=""
					self.data["control-post"]=gringolizar(self.data["titulo"],"-")


					
					l1=self.data["plugins"][plugin_settings.name].model["galerias"].obtenerFilas("Sliders")[i][1]
					self.data["boxes"]=[l1]
					self.data["vars"]={"titulos":[],"actual":self.data["titulo"]}

					for elem in self.data["plugins"][plugin_settings.name].model["galerias"].obtenerFilas("Sliders"):
						self.data["vars"]["titulos"].append(elem[0])

				else:
					self.data["titulo"]="Crea una nueva pagina"
					self.data["meta-layout"]=self.data["titulo"]
					self.data["post"]=gringolizar(self.data["titulo"],"-")
					self.data["control-post"]="Inicio"
					self.data["boxes"]=[self.model["galerias"].obtenerEstructura("Sliders")[1]]
				
				modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
				tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]

				self.data["vars"]["modelos"]=modelos
				self.data["vars"]["opciones"]=self.data["opciones"]
				self.data["vars"]["Tablas"]=tablas


				
			elif self.data["action"]=="save":           
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()

				if self.data["args"][2]!=None:

					self.model["galerias"].modificarSlider(self.data["args"][2],self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Plugin",plugin_settings.name,"Slider",str(self.data["args"][2]),action="editar")()
				else:

					self.model["galerias"].crearSlider(self.data["request"],self.data["metadatos"])
				
					redirecter(config,settings.app,"admin","Plugin",plugin_settings.name,"Slider","None",action="editar")()
	def Shortcode(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar,gringolizar,redirecter
		
		if self.data["ajax"]==False:
			if self.data["action"]=="editar":
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()


				self.data["repeate"]=1
				self.data["plantillas"]=self.model["main"].obtenerFilas("Plantillas")

				
				keys=self.data["args"][1]


				i=self.data["args"][2]
				self.data["categorias"]={}

				self.data["titulo"]=self.data["metodo"]

				if i!=None:
					self.data["categorias"]={}

					tabla=self.model["shortcodes"].obtenerFilas("Shortcodes")[i]

					self.data["titulo"]=tabla[0]



					self.data["meta-layout"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"layout")
					self.data["meta-control"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"control")

					self.data["post"]=""
					self.data["control-post"]=gringolizar(self.data["titulo"],"-")


					
					l1=self.data["plugins"][plugin_settings.name].model["shortcodes"].obtenerFilas("Shortcodes")[i][1]
					self.data["boxes"]=[l1]
					self.data["vars"]={"titulos":[],"actual":self.data["titulo"]}

					for elem in self.data["plugins"][plugin_settings.name].model["shortcodes"].obtenerFilas("Shortcodes"):
						self.data["vars"]["titulos"].append(elem[0])

				else:
					self.data["titulo"]="Crea una nueva pagina"
					self.data["meta-layout"]=self.data["titulo"]
					self.data["post"]=gringolizar(self.data["titulo"],"-")
					self.data["control-post"]="Inicio"
					self.data["boxes"]=[self.model["shortcodes"].obtenerEstructura("Shortcodes")[1]]
				
				modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
				tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]

				self.data["vars"]["modelos"]=modelos
				self.data["vars"]["opciones"]=self.data["opciones"]
				self.data["vars"]["Tablas"]=tablas


				
			elif self.data["action"]=="save":           
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()
				titulo=self.data["request"]["titulo"].value.strip()[self.data["request"]["titulo"].value.strip().find("-")+1:]
				f=open(plugin_settings.__path__+plugin_settings.shortcodes_folder+titulo+".py","w")
				f.write(decode(self.data["request"]["controlador"].value))
				f.close()
				f=open(plugin_settings.__path__+plugin_settings.widgets_folder+titulo+".html","w")
				f.write(decode(self.data["request"]["layout"].value))
				f.close()
				
				if self.data["args"][2]!=None:


					self.model["shortcodes"].modificarShortcode(self.data["args"][2],self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Plugin",plugin_settings.name,"Shortcode",str(self.data["args"][2]),action="editar")()
				else:
					self.model["shortcodes"].crearShortcode(self.data["request"],self.data["metadatos"])

					redirecter(config,settings.app,"admin","Plugin",plugin_settings.name,"Shortcode",str(self.data["args"][2]),action="editar")()

	
			
		
		
		
		
	def cnt(self,data):
		"""
		Este es el docstrings
		"""
		global config
	def metodo_desconocido(self):
		self.HEADERS.show()
		print "Este no es un metodo del plugin"

	def widget(self):
		if len(self.data["args"])>0:
			self.HEADERS.set_headers({"Content-type":"text/html\n"})
			self.HEADERS.show()
			print self.incluir(self.data,"head",isglobal=True)
			print self.do_shortcode(self.data["args"][0])
			#print self.incluir(self.data,self.data["args"][0])



	def Entrar(self):
		self.HEADERS.set_headers({"Content-type":"text/html\n"})
		
		estudiante=self.model["main"].obtenerEstudiante(expediente=self.data["request"]["expediente"])

		if estudiante!=None:
			self.login.Entrar(estudiante[0]["email"]["value"],self.data["request"]["password"])
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