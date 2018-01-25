__pragma__("alias","s","$")
from Widget import Widget
from ButtonImage import ButtonImage
class BTNS(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="<b class='titulo'>{}</b>"
		self.estilos={}
		self._imagen="img.png"
		self._btns=[]
		self._randomBg=False


	def update(self):
		self.format=[self._titulo]
		
		self.__update__()
		
		for elem in self._btns:



			b=ButtonImage(elem[1])
			self.children.append(b)
			
			b._randomBg=self._randomBg
			b.height=120

			

			b.update()
			b.img(elem[0])
			

			b.titulo(elem[1])
			self.target.append(b.target)
			
			if len(elem)==3:
				b.target.css(elem[2])
	
	
		


		