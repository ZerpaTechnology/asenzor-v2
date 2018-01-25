__pragma__("alias","s","$")
from Widget import Widget
import random
class ButtonImage(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="<button ><img><b class='titulo'></b></button>"
		self.__button=self.target.find(">button")
		self.__img=self.__button.find("img")
		self.__titulo=self.__button.find(">.titulo")
		
		self.paleta=["#1abc9c","#2ecc71","#3498db","#9b59b6","#34495e",
							  "#16a085","#27ae60","#2980b9","#8e44ad","#2c3e50",
							  "#f1c40f","#e67e22","#e74c3c","#ecf0f1","#95a5a6",
							  "#f39c12","#d35400","#c0392b","#bdc3c7","#7f8c8d"]
		self._randomBg=False
		self.height=90

	def titulo(self,titulo):
		self.__button.find(">.titulo").text(titulo)
		self._titulo=titulo
	def img(self,src):
		self.__button.find("img").attr("src",src)

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		if self._randomBg:
			self.__button.css("background-color",self.paleta[random.randint(0,len(self.paleta))])

		self.titulo(self._titulo)
		self.__button.css("height",self.height)
		
	
	
		


		