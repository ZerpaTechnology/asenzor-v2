__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class MediaButton(Widget):
	def __init__(self,titulo="Subir archivo",Media=None):
		Widget.__init__(self,titulo)
		self._html="<button>{}</button>"
		self.Media=Media
		self._titulo=self.titulo
	
	def open(self):
		self.Media.updateTitulo(self._titulo)
		self.Media.open()

	def update(self):
		
		s(self.target).html(self._html.format(self.titulo))
		s(self.target).find("button").bind("click",self.open)

