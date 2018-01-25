__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
class ButtonSettings(Widget):
	"""docstring for ButtonSettings"""
	def __init__(self,titulo,siguiente=1,_screen=0):
		Widget.__init__(self,titulo)
		self._html="""
		<span>
		<b class='titulo'>{}</b>
		<p>{}</p>
		</span>"""
		self.slider=None
		self.screen=None
		self.descripcion=""
		
		
		self._siguiente=siguiente
		self._screen=_screen

	def siguiente(self,evt):
		self.screen.showTab(self._screen)
		self.slider.showTab(self._siguiente)
	

	def update(self):
		self._update=True
		self._html=self._html.format(self.titulo,self.descripcion)
		self.target.bind("click",self.siguiente)
		s(self.target).html(self._html)


		
