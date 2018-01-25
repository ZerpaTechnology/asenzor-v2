__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget


settings=nuclear.Settings()
config=Config.Config()

class Iframe(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="<iframe src='' name=''></iframe>"
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

		

		


		

		


		
		



		