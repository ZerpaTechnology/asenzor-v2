__pragma__("alias","s","$")
__pragma__("xpath",["../"])
from Widget import Widget
from BasicTabs import BasicTabs

class BuilderModulo(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Insertar Columnas"):
		Widget.__init__(self,titulo)
		self._html="""
		<div class='caja'>
		</div>
		<div class='caja2'>
		</div>
		"""
		self.target.html(self._html)
		self.__button=self.target.find(">button")
		self._html=""
		self.BasicTabs=BasicTabs()
		self._modulos=[]
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.titulo(self._titulo)
		for elem in self._modulos:
			pass

		self.__titulo=self.target.find(">.titulo")
	
	
		


		