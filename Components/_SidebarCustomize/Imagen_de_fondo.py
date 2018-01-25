__pragma__("alias","s","$")
from Widget import Widget
from HeaderCustomize import HeaderCustomize
class Imagen_de_fondo(Widget):
	"""
	Si añades un video, la imagen se utilizara como alternativa
	mientras que el video carga.
	"""
	def __init__(self,titulo):
		Widget.__init__(self,titulo)
		self.descripcion=self.__doc__
		
		
		
		
		