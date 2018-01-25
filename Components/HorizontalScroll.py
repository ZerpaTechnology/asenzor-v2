__pragma__("alias","s","$")
from Widget import Widget
class HorizontalScroll(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self.content=self.target.find(">div")
		self._html="<div></div>"

	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def done(self):
		self.titulo(self._titulo)
		self.__titulo=self.target.find(">.titulo")
		self.reloadSize()
		
	def reloadSize(self):
		width=0
		
		for elem in self.target[0].children:
			
			print(elem.outerHTML)
			
			width+=s(elem).outerWidth()
		self.target.find(">div").css("width",width)

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		
		
		
	
	
		


		