Component=nuclear.Component
from Widget import Widget
__pragma__("alias","s","$")
class ButtonAddItem(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="""
		<button>
		<span class='left'>
		<span class='icon'></span>
		<b class='titulo'>{}</b>
		</span>
		<span class='right'>{}</span>
		</button>
		"""
		self.descripcion=""
	def update(self):
		self.formato=[self.titulo,self.descripcion]
		self.__update__()
	
	
		


		