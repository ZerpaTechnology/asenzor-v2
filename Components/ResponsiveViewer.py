__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget


settings=nuclear.Settings()
config=Config.Config()

class ResponsiveViewer(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html_tablet="""
		<div class='tablet'>
		<span class='camara'></span>
		<iframe src='' name=''></iframe>
		<div class='btns'>
			<span class='atras'></span>
			<span class='home'></span>
			<span class='menu'></span>
		</div>
		</div>
		"""
		self._html_phone="""
		<div class='phone'>
		<span class='bocina'></span><span class='camara'></span>
		<iframe src='' name=''></iframe>
		<div class='btns'>
			<span class='atras'></span>
			<span class='home'></span>
			<span class='menu'></span>
		</div>
		</div>
		"""


		self.target.html(self._html)
		self._html=""
		self.name=self.titulo
		self.source=""
		self.primitivo=lambda self:self.target.find("iframe")
		self.__iframe=self.target.find(">iframe")



	def update(self):
		self.__update__()
		self.__iframe.attr("src",self.source)
		self.__iframe.attr("name",self.name)

		

		


		

		


		
		



		