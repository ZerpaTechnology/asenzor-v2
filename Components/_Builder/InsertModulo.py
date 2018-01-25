__pragma__("alias","s","$")
__pragma__("xpath",["../"])
from Widget import Widget
from BasicTabs import BasicTabs
from ModuloHTML import ModuloHTML
from Modulo import Modulo
class InsertModulo(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Insertar Modulo"):
		Widget.__init__(self,titulo)
		self._html="<div class='content'></div>"
		self.target.html(self._html)

		self.__button=self.target.find(">button")
		
		self.BasicTabs=BasicTabs()
		self._modulos=[ModuloHTML()]
		self.col=0
		self.column=None
		self.window=None

	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def open(self):
		self.target.show()

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.titulo(self._titulo)
		self.BasicTabs.update()

		self.Builder.window._nav=[["Nuevo Modulo","new",lambda self:lambda evt: None],
					["Cargar de la libreria","load",lambda self:lambda evt: None],
					]

		
			
		for modulo in self._modulos:
			modulo=modulo.clone()
			modulo.window=self.Builder.window
			modulo.column=self.column
			self.BasicTabs.appendToTab(0,modulo)					
			
		self.target.find(">.content").append(self.BasicTabs.target)
		
		
		

		self.__titulo=self.target.find(">.titulo")
	
	
		


		