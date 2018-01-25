__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget

class Input(Widget):
	"""docstring for ClassName"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._descripcion=""
		self._html="<b>{}</b><p>{}</p><input>"
		s(self.target).css({"display":"inline-block"})
		self.value=None
		self.content=None
	def update(self):
		self.format=[self._titulo,self._descripcion]
		self.__update__()
		if self.value!=None:
			s(self.target).find(">input").val(str(self.value))

