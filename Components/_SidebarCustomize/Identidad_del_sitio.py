__pragma__("xpath",["","../../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from Input import Input
from MediaManager import MediaManager
from CheckBox import CheckBox
from HeaderCustomize import HeaderCustomize
class Identidad_del_sitio(Widget):
	"""

	"""
	def __init__(self, titulo):
		#datos estaticos
		Widget.__init__(self,titulo)
		
	def update(self):
		self.__update__()
		w=HeaderCustomize(self.titulo)
		w.slider=self.slider
		w._atras=self._atras
		w._screen=self._screen
		self.add(w)
		w=MediaManager("Logo")
		w.btn2="Elegir logo"
		w.btn1="Eliminar logo"
		w.Media=self.Media
		w.placeholder="No se a elegido un logo"
		self.add(w)
		
		w=Input("Titulo del sitio")
		self.add(w)
		w=Input("Descripción corta")
		self.add(w)
		w=CheckBox("Muestra el título y descripción del sitio")
		self.add(w)

		w=MediaManager("Icono del sitio")
		w.descripcion="""
		El icono del sitio lo usa el navegador 
		como icono de la aplicación para tu sitio. 
		Los iconos deben ser cuadrados y al menos de 512 píxeles de ancho y alto.
		"""
		w.placeholder="No se a elegido un logo"
		w.Media=self.Media
		self.add(w)
		self.css({"padding-left":"20px","padding-right":"20px"},None,">div:nth-child(n+2)")



		







