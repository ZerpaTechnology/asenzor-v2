
from modulos.controlador import Controlador

from settings import config as settings
from config import config
from modulos.ztec.zred import getCookie,normalizar,redirecter
class Entradas(Controlador):
	def __init__(self,data):
		
		Controlador.__init__(self,data)

	def Entradas(self):
		"""
		Este metodo se usa para controlar el conjunto de paginas
		"""
		self.data["addNew-enlace"]=config.base_url+settings.app+"/admin/Entrada/None/action=editar"
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
	def Entrada(self):
		"""
		Este metodo se usa para crear o modificar una pagina en espacifico
		"""
		from modulos.ztec.zred import normalizar,gringolizar
		
		if self.data["ajax"]==False:


			if self.data["action"]=="editar":
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()
				self.data["repeate"]=1
				self.data["plantillas"]=self.data["model"]["main"].obtenerFilas("Plantillas")

				
				keys=self.data["args"][0]
				i=normalizar(self.data["args"][0])
				self.data["categorias"]={}

				self.data["titulo"]=self.data["metodo"]
				if i!=None:

					self.data["categorias"]={}
					tabla=self.data["model"]["paginas"].obtenerFilas("Entradas")[i]
					self.data["titulo"]=tabla[0]
					self.data["meta-layout"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"layout")
					self.data["meta-control"]=self.data["model"]["paginas"].exportarMetadato(tabla[4],"control")

					self.data["post"]=gringolizar(self.data["titulo"],"-")
					self.data["control-post"]="Blog"
					l1=self.data["model"]["paginas"].obtenerFilas("Entradas")[i][1]
					self.data["boxes"]=[l1]
				else:
					self.data["titulo"]="Crea una nueva entrada"
					self.data["layout"]=self.data["titulo"]
					self.data["post"]=gringolizar(self.data["titulo"],"-")
					self.data["control-post"]="Inicio"
					self.data["boxes"]=[self.data["model"]["paginas"].obtenerEstructura("Entradas")[1]]

				modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
				tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]
				
				self.data["vars"]["modelos"]=modelos
				self.data["vars"]["opciones"]=self.data["model"][modelos[self.data["metodo"]]].obtenerFilas('Opciones')
				self.data["vars"]["Tablas"]=tablas
				self.servir()
			elif self.data["action"]=="save":           
				#self.HEADERS.set_headers({"Content-type":"text/plain\n"})
				self.HEADERS.show()

				if self.data["args"][0]!=None:
					self.data["model"]["paginas"].modificarEntrada(self.data["args"][0],self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Entrada",str(self.data["args"][0]),action="editar")()
				else:
					self.data["model"]["paginas"].crearEntrada(self.data["request"],self.data["metadatos"])
					redirecter(config,settings.app,"admin","Entrada","None",action="editar")()