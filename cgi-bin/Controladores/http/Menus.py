
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Menus(Controlador):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar

		Controlador.__init__(self,data)
		

		


		if self.data["action"]=="menus":
				self.data["Paginas"]=self.data["model"]["paginas"].obtenerMetadatos("Paginas")
				self.data["Menus"]=self.data["model"]["menus"].obtenerFilas("Menus")
				self.data["Entradas"]=self.data["model"]["paginas"].obtenerMetadatos("Entradas")
				self.data["Categorias"]=self.data["model"]["paginas"].obtenerMetadatos("Categorias")
				
				self.data["other-tags"]=[]
				self.data["vars"]["Menus"]=self.data["Menus"]




	def Menus(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""


		if self.data["action"]=="save-menu":
			self.HEADERS.set_headers({"Content-type":"text/plain\n"})
			if self.data["request"]["nuevo"]==None:	
				self.HEADERS.show()			
				self.data["model"]["menus"].crearMenu(self.data["request"]["nombre"],self.data["request"]["menu"])
				print self.data["model"]["menus"].db.log
				print "Menu creado"
			else:
				self.HEADERS.show()			
				self.data["model"]["menus"].modificarMenu(self.data["request"]["nuevo"],
														 self.data["request"]["nombre"],
														 self.data["request"]["menu"])
				print "Menu modificado"
		

		elif self.data["ajax"]==False and self.data["login"]==True:
			self.servir()

