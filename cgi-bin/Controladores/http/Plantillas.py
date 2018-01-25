
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Plantillas(Controlador):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar
		
		Controlador.__init__(self,data)

	def Plantillas(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		from modulos.ztec.zred import listar,listarAjax
		if self.data["ajax"]==False:
			if self.data["action"]=="listar":
				
				self.HEADERS.show()
				listar(self.data,config)

				self.servir()
			elif self.data["action"]=="editar":
				self.servir()
		else:
			self.HEADERS.set_headers({"Content-type":"text/plain"})
			if self.data["action"]=="listar":
				self.HEADERS.show()
				listarAjax(self.data,config)
	def Plantilla(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar
		self.HEADERS.show()
		if self.data["ajax"]==False:
			if self.data["action"]=="editar":
				self.data["repeate"]=1
				self.data["plantillas"]=self.data["model"]["main"].obtenerFilas("Plantillas")

				
				keys=self.data["args"][0]
				i=normalizar(self.data["args"][0])
				self.data["categorias"]={}

				self.data["titulo"]=self.data["metodo"]
				if i!=None:

					self.data["categorias"]={}

					self.data["titulo"]=self.data["model"]["archivos"].obtenerFilas("Archivos")[i][0]
	                

	                
	                
	                l1=self.data["model"]["archivos"].obtenerFilas("Archivos")[i][1]


	                self.data["boxes"]=[l1]
            	else:
            		data["titulo"]="Subir nuevo archivo"
            		data["boxes"]=data["model"]["archivos"].obtenerEstructura("Archivos")
            	self.servir()
              
              