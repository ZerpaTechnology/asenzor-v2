__pragma__("alias","s","$")
from Widget import Widget
from VideoManager import VideoManager
from HeaderCustomize import HeaderCustomize
from Input import Input
from Imagen_de_cabecera import Imagen_de_cabecera
class CabeceraMultimedia(Widget):
	"""
	Si añades un video, la imagen se utilizara como alternativa
	mientras que el video carga.
	"""
	def __init__(self,titulo):
		Widget.__init__(self,titulo)
		

		self.descripcion="""Si añades un video, la imagen se utilizara como alternativa
		mientras que el video carga.
		"""


	def update(self):
		self.__update__()
		w=HeaderCustomize(self.titulo)
		w.descripcion=self.descripcion

		w.slider=self.slider
		w._atras=self._atras
		w._screen=self._screen
		self.add(w)
		
		w=VideoManager("Video de cabecera")
		self.add(w)
		w=Input()
		w.descripcion="O escribe una URL de YouTube:"
		self.add(w)
		w=Imagen_de_cabecera("Imagen de cabecera")
		w.Media=self.Media
		self.add(w)
		self.css({"padding-left":"20px","padding-right":"20px"},None,">div:nth-child(n+2)")


		
		
		
		
		