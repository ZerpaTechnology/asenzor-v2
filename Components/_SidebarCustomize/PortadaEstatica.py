__pragma__("alias","s","$")
from Widget import Widget
from HeaderCustomize import HeaderCustomize
from RadioButtonList import RadioButtonList
from Select import Select
from EnlaceButton import EnlaceButton
class PortadaEstatica(Widget):
	"""
	Si añades un video, la imagen se utilizara como alternativa
	mientras que el video carga.
	"""
	def __init__(self,titulo):
		Widget.__init__(self,titulo)
		self.descripcion=self.__doc__
	def update(self):
		self.__update__()
		w=HeaderCustomize(self.titulo)
		w.slider=self.slider
		w._atras=self._atras
		w._screen=self._screen
		w.descripcion="""
		Tu tema permite una página estatica como
		portada
		"""
		self.add(w)
		w=RadioButtonList("Pagina frontal muestra")
		self.add(w)
		w.addOptions(["Tus ultimas entradas","Una pagina estatica"],1)

		
		w=Select("Portada")
		w.opciones=["Pagina de ejemplo",
					"Inicio",
					"Acerca de",
					"Contacto",
					"Blog",
					]
		self.add(w)
		w=EnlaceButton("+Añadir nueva pagina")
		self.add(w)
		w=Select("Página de entradaa")
		
		w.opciones=["Pagina de ejemplo",
					"Inicio",
					"Acerca de",
					"Contacto",
					"Blog",
					]
		self.add(w)
		w=EnlaceButton("+Añadir nueva pagina")
		self.add(w)
		self.css({"padding-left":"20px","padding-right":"20px"},None,">div:nth-child(n+2)")
		
		
		
		