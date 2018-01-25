__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomizeMain import HeaderCustomizeMain

settings=nuclear.Settings()
config=Config.Config()

class InputSearch(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="<div><span class='search'></span><input type='search' value='{}' name='{}' placeholder='{}'></div>"
		self.icon=config.base_url+"static/imgs/iconos/lupa.png"
		self.placeholder="Buscar..."
		self.value=""


	def update(self):
		self.format=[self.value,self.name,self.placeholder]
		self.__update__()
		self.target.find(">div").find(">.search").css({"background-image":"url('{}')".format(self.icon)})
		
		
		
		

		


		

		


		
		



		