
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Blog(Controlador):
	def __init__(self,data):
		
		Controlador.__init__(self,data)
		self.vista="Blog"
		
		

	def Paginas(self):
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
	def Pagina(self):
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

					self.data["titulo"]=self.data["model"]["paginas"].obtenerFilas("Paginas")[i][0]
					self.data["layout"]=self.data["titulo"]
					self.data["post"]=str(i)
					self.data["pagina"]="{'pagina':'"+self.data["titulo"]+"'}"
					l1=self.data["model"]["paginas"].obtenerFilas("Paginas")[i][1]
					self.data["boxes"]=[l1]
				else:
					data["titulo"]="Subir nuevo archivo"
					data["boxes"]=data["model"]["archivos"].obtenerEstructura("Archivos")
				self.servir()
		elif self.data["ajax"]==True:
			if self.data["action"]=="modificar-atributo":
				self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.data["model"]["paginas"].updatesMetas(self.data["request"]["args"][0],self.data["request"]["meta"],tabla="Paginas")

              