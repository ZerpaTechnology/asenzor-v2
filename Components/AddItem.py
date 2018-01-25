__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomizeMain import HeaderCustomizeMain

settings=nuclear.Settings()
config=Config.Config()
class AddItem(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""
		<span class='icon'></span>
		<div>
		<b>{}</b>
		<p>{}</p>
		<div>
		"""
		self.icon=config.base_url+"static/imgs/iconos/document-2.png"
		self.descripcion=""


	def update(self):
		self.format=[self.titulo,self.descripcion]
		self.__update__()
		self.target.find(">.icon").css({"background-image":"url('{}')".format(self.icon)})
		

		


		

		


		
		



		