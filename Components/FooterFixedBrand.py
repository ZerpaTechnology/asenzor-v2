__pragma__("alias","s","$")
from Widget import Widget
class FooterFixedBrand(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="This website use: zerpatechnology"):
		Widget.__init__(self,titulo)
		self.target.html("<b class='titulo'></b>")
		self.__button=self.target.find(">button")
		self._hmtl=""
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.titulo(self._titulo)
		self.__titulo=self.target.find(">.titulo")
	
	
		


		