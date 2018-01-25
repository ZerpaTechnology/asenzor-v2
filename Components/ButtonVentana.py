__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class ButtonVentana(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		Widget.__init__(self,titulo)		
		self._html="""
		<div>
		<span class='atras'></span>
		<div class='text'>
		<p>{}</p>
		<h3>{}</h3>
		</div>
		</div>
		<p>{}</p>
		"""
		self.pretitulo="Estas personalizando: "
		self.descripcion=""
		
		self._atras=atras

	def atras(self,evt):
		self.slider.showTab(self._atras)

	def update(self):
		s(self.target).html(self._html.format(self.pretitulo,self.titulo,self.descripcion))
		s(self.target).find(".atras").bind("click",self.atras)

	
		
	