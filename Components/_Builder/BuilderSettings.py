__pragma__("alias","s","$")
__pragma__("xpath",["../"])
from Widget import Widget

class BuilderSettings(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Insertar Modulo"):
		Widget.__init__(self,titulo)
		self._html=""
		

	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo
	def open(self):
		self.target.show()

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.titulo(self._titulo)
	
	
		


		