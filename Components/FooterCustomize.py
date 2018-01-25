__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class FooterCustomize(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		Widget.__init__(self,titulo)		
		self._html="""
		<div>
		<span class='ocultar'> 
		<span class='icon'></span>
		<span class='text'>{}</span>
		</span>
		<div class='responsize'>
		<span class='desktop'></span>
		<span class='tablet'></span>
		<span class='phone'></span>
		</div>
		"""
		
		self._atras=atras
		self.status="desktop"
	def atras(self,evt):
		self.slider.showTab(self._atras)
		
	def update(self):
		s(self.target).html(self._html.format(self.titulo))
		s(self.target).find(".atras").bind("click",self.atras)

	
		
	