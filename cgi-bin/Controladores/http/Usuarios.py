
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Usuarios(Controlador):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar
		Controlador.__init__(self,data)

	def Usuarios(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		from modulos.ztec.zred import listar,listarAjax
		if self.data["ajax"]==False:
			if self.data["action"]=="listar":
				self.data["Tabla"]="Usuarios"
				self.data["Modelos"]=["usuarios","global"]
				
				listar(self.data,config)

				self.servir()
			elif self.data["action"]=="editar":
				self.servir()
		else:
			self.HEADERS.set_headers({"Content-type":"text/plain"})
			if self.data["action"]=="listar":
				self.HEADERS.show()
				listarAjax(self.data,config)
	def Usuario(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		variables a parasar por data 
		repeate, plantillas, categorias, post, pagina, boxes,titulo
		"""
		from modulos.ztec.zred import normalizar,redirecter
		
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
					

					self.data["titulo"]=self.data["model"]["usuarios"].obtenerFilas("Usuarios")[i][0]
			                self.data["layout"]=self.data["titulo"]
		
			                self.data["post"]=str(i)
			                self.data["pagina"]="{'pagina':'"+self.data["titulo"]+"'}"
			                l1=self.data["model"]["usuarios"].obtenerFilas("Usuarios")[i][1]
		                	self.data["boxes"]=[l1]
            			else:

		            		self.data["titulo"]="Agregar nuevo usuario"

            				self.data["boxes"]=self.data["model"]["usuarios"].obtenerEstructura("Usuarios")[1]
            			self.servir()
			elif self.data["action"]=="save":           
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()

				if self.data["args"][0]!=None:
					
					self.data["model"]["usuarios"].modificarUsuario(self.data["args"][0],
																	self.data["request"]["usuario"].value,
																	self.data["request"]["email"].value,
																	self.data["request"]["password"].value,
																	self.data["request"]["avatar"].value,
																	self.data["request"]["permisologia"].value,hours=4)
					redirecter(config,settings.app,"admin","Usuarios",action="listar")()
				else:
					self.data["model"]["usuarios"].registrarUsuario(self.data["request"]["usuario"].value,
																	self.data["request"]["email"].value,
																	self.data["request"]["password"].value,
																	self.data["request"]["avatar"].value,
																	self.data["request"]["permisologia"].value,
																	hours=4)
					redirecter(config,settings.app,"admin","Usuarios",action="listar")()
              
              