
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Ayudas(Controlador):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar
		Controlador.__init__(self,data)

	def Ayuda(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		from modulos.ztec.zred import listar,listarAjax,normalizar,redirecter
		if self.data["ajax"]==False:
			if self.data["action"]=="listar":
				self.HEADERS.show()
				self.data["Tabla"]="Ayuda"
				self.data["Modelos"]=["ayuda"]
				listar(self.data,config)

				self.servir()
			elif self.data["action"]=="editar":
				self.data["repeate"]=1
				self.data["plantillas"]=self.data["model"]["main"].obtenerFilas("Plantillas")
				keys=self.data["metodo"]
				

				i=normalizar(self.data["args"][0])
				self.data["categorias"]={}
				self.data["titulo"]=self.data["metodo"]

				if i!=None:
					self.data["categorias"]={}
					
					self.data["titulo"]=self.data["model"]["ayuda"].obtenerFilas("Ayuda")[i][0]

					l1=self.data["model"]["ayuda"].obtenerFilas("Ayuda")[i][1]

					self.data["boxes"]=[l1]
				else:
					data["titulo"]="Subir nuevo archivo"
					data["boxes"]=data["model"]["ayuda"].obtenerEstructura("Ayuda")
				self.servir()
			elif self.data["action"]=="save":
				self.HEADERS.show()
				if self.data["args"][0]!=None:

					self.data["model"]["ayuda"].modificarTema(self.data["args"][0],self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Ayuda",action="listar")()
				else:
					self.data["model"]["ayuda"].crearTema(self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Ayuda",action="listar")()

		else:
			self.HEADERS.set_headers({"Content-type":"text/plain"})
			if self.data["action"]=="listar":
				self.HEADERS.show()
				listarAjax(self.data,config)


		
		
		
		
			
            	
              
              
    