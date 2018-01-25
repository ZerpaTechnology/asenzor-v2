__pragma__("alias","s","$")
from Widget import Widget
class Popup(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self.target.html("<h2 class='titulo'></h2><div class='content'></div><span class='close'>x</span>")
		self.__button=self.target.find(">button")
		self._html=""
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def hide(self):
		self.target.hide()

	def show(self):
		self.target.show()

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.__titulo=self.target.find(">.titulo")
		self.target.find(">.close").bind("click",self.hide)
		self.titulo(self._titulo)
		
	
	
		


		