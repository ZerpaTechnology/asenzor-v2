__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget

class Textarea(Widget):
	"""docstring for ClassName"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self.descripcion=""
		self._html="<b class='titulo'>{}</b><p class='descripcion'>{}</p><textarea></textarea><p class='postdescripcion'></p>"
		self.postdescripcion
		s(self.target).css({"display":"inline-block"})
		self.value=None
		
	def update(self):
		s(self.target).html(self._html.format(self.titulo,self.descripcion))
		if self.value!=None:
			s(self.target).find(">textarea").val(str(self.value))
