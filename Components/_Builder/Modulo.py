__pragma__("alias","s","$")
from Widget import Widget
class Modulo(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="""
		<span class='close'>x</span>
		<span class='titulo'></span>
		<span class='config'></span>
		"""
		self.modulo=None
		self.target.html(self._html)
		self.__button=self.target.find(">button")
		self._html=""
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.titulo(self._titulo)
		self.__titulo=self.target.find(">.titulo")
	
	
		


		