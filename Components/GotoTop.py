__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class GotoTop(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="""
		<a class="gototop "><i class="fa fa-angle-up  fa-3x"></i></a>
		"""
		
		self.target.html(self._html)
		self._html=""
		self._enlace=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self._img=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		

		
	
	
		


		