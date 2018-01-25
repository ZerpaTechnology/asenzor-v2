
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Formularios(Controlador):
	def __init__(self,data):
		from modulos.ztec.zred import getCookie,normalizar
		Controlador.__init__(self,data)

	def Formularios(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		from modulos.ztec.zred import listar,listarAjax
		
		
		if self.data["ajax"]==False:
			if self.data["action"]=="listar":
				self.data["Tabla"]="Formularios"
				self.data["Modelos"]=["formularios"]
				self.HEADERS.show()
				listar(self.data,config)

				self.servir()
			elif self.data["action"]=="editar":
				self.servir()
		else:
			self.HEADERS.set_headers({"Content-type":"text/plain"})
			if self.data["action"]=="listar":
				self.HEADERS.show()
				self.data["Tabla"]="Formularios"
				self.data["Modelos"]=["formularios"]
				listarAjax(self.data,config)
	def Post_de_Formularios(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		from modulos.ztec.zred import listar,listarAjax
		
		
		if self.data["ajax"]==False:
			if self.data["action"]=="listar":
				self.data["Tabla"]="Post-de-Formulario"
				self.data["Modelos"]=["formularios"]
				self.HEADERS.show()
				listar(self.data,config)

				self.servir()
			elif self.data["action"]=="editar":
				self.servir()
		else:
			self.HEADERS.set_headers({"Content-type":"text/plain"})
			if self.data["action"]=="listar":
				self.HEADERS.show()
				self.data["Tabla"]="Post-de-Formulario"
				self.data["Modelos"]=["formularios"]
				listarAjax(self.data,config)
	def Formulario(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar,redirecter
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
					self.data["titulo"]=self.data["model"]["formularios"].obtenerFilas("Formularios")[i][0]
					self.data["layout"]=self.data["titulo"]

			                self.data["post"]=str(i)
			                self.data["pagina"]="{'pagina':'"+self.data["titulo"]+"'}"
			                l1=self.data["model"]["formularios"].obtenerFilas("Formularios")[i][1]
		
		
			                self.data["boxes"]=[l1]
				else:
					
					self.data["titulo"]="Subir nuevo archivo"
					self.data["boxes"]=self.data["model"]["formularios"].obtenerEstructura("Formularios")[1]
				self.servir()

			elif self.data["action"]=="save":            	
				self.data["model"]["formularios"].modificarFormulario(self.data["args"][0],self.data["request"])
				redirecter(config,settings.app,"admin","Formulario",str(self.data["args"][0]),action="editar")()
			elif self.data["action"]=="post":
				"""
				Esta accion es registrada por el usuario y no por el administrador
				"""
				
				self.data["model"]["formularios"].registrarFormulario(self.data["indice"],self.data["tabla"],self.data["request"])
				redirecter(config,settings.app,"")()
		
		
	def Post_de_Formulario(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""

		from modulos.ztec.zred import normalizar,redirecter
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
					
					self.data["titulo"]=self.data["model"]["formularios"].obtenerFilas("Post-de-Formulario")[i][0]

					self.data["layout"]=self.data["titulo"]


			                self.data["post"]=str(i)

			                self.data["pagina"]="{'pagina':'"+self.data["titulo"]+"'}"
			                l1=self.data["model"]["formularios"].obtenerFilas("Post-de-Formulario")[i][1]
		
		
			                self.data["boxes"]=[l1]
				else:
					data["titulo"]="Subir nuevo archivo"
					data["boxes"]=data["model"]["formularios"].obtenerEstructura("Post-de-Formulario")
				self.servir()

			elif self.data["action"]=="save":            	
				self.data["model"]["formularios"].registrarFormulario(self.data["indice"],self.data["tabla"],self.data["request"])
				redirecter(config,settings.app,"")()
		



