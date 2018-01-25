
__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class BandaTema(Widget):
	"""docstring for BandaTema"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)

		self._html="""
		<div>
		<div class="text">
		{}
		</div>
		<button>{}</button>
		</div>
		"""
		self.text="Tema activo:<br>"+settings.app
		self.btn_titulo="Cambiar"
		self._html=self._html.format(self.text,self.btn_titulo)
		s(self.target).html(self._html)

	def update(self):
		pass
		
		

		

