__pragma__("xpath",["","../../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomize import HeaderCustomize
from RadioButtonList import RadioButtonList
from RadioButton import RadioButton
from Select import Select
from EnlaceButtonInput import EnlaceButtonInput
class ThemesOptions(Widget):
	"""docstring for Colores"""
	def __init__(self,titulo):
		Widget.__init__(self,titulo)
	def update(self):
		self.__update__()
		w=HeaderCustomize("Themes Options")
		w.slider=self.slider
		w._atras=self._atras
		w._screen=self._screen
		self.add(w)
		r=RadioButtonList("Page Layout")
		r.descripcion="""
		When the two-column layout is assigned, 
		the page title is in one column and 
		content is in the other.
		"""
		self.add(r)
		w=RadioButton("One Column")
		r.add(w)
		w=RadioButton("Two Column")
		r.add(w)

		w=Select("From Page Section 1 Content")
		w.descripcion="""
		Select pages to feature in each area 
		from the dropdowns. Add an image to a 
		section by setting a featured image in 
		the page editor. Empty sections will not 
		be displayed.
		"""
		w.opciones=["--Elegir--",
					"Pagina de ejemplo",
					"Inicio",
					"Acerca de",
					"Contacto",
					"Blog",
					]
		self.add(w)
		w=EnlaceButtonInput("+Añadir nueva página")
		self.add(w)
		w=Select("From Page Section 2 Content")
		self.add(w)
		w=EnlaceButtonInput("+Añadir nueva página")
		self.add(w)
		w=Select("From Page Section 3 Content")
		self.add(w)
		w=EnlaceButtonInput("+Añadir nueva página")
		self.add(w)
		w=Select("From Page Section 4 Content")
		self.add(w)
		w=EnlaceButtonInput("+Añadir nueva página")
		self.add(w)


		



		