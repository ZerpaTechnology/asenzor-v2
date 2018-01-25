__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomizeMain import HeaderCustomizeMain





from BandaTema import BandaTema
from Widget import Widget
from BasicSlider import BasicSlider
from HeaderCustomize import HeaderCustomize
from ButtonSettings import ButtonSettings
from BasicTabs import BasicTabs
from FileUpload import FileUpload
from MediaButton import MediaButton

from _SidebarCustomize.Identidad_del_sitio import Identidad_del_sitio
from _SidebarCustomize.CabeceraMultimedia import CabeceraMultimedia
from _SidebarCustomize.Menus import Menus
from _SidebarCustomize.Colores import Colores
from _SidebarCustomize.Widgets import Widgets
from _SidebarCustomize.Imagen_de_fondo import Imagen_de_fondo
from _SidebarCustomize.PortadaEstatica import PortadaEstatica
from _SidebarCustomize.ThemesOptions import ThemesOptions
from EnlaceButton import EnlaceButton
from Select import Select
from ButtonInput import ButtonInput
from TabAcordion import TabAcordion
from Acordion import Acordion
from InputSearch import InputSearch
from Textarea import Textarea
from FooterCustomize import FooterCustomize
from BoxScroll import BoxScroll
from AddItem import AddItem

settings=nuclear.Settings()

class SidebarAddWidgets(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)


	def update(self):
		self.__update__()
		w=InputSearch()
		self.add(w)
		w.target.css("height","8vh")

		b=BoxScroll()

		w=AddItem("Archivos")
		w.descripcion="Un listado mensual de las entradas de tu sitio"
		b.add(w)
		w=AddItem("Archivos")
		w.descripcion="Un listado mensual de las entradas de tu sitio"
		b.add(w)
		w=AddItem("Archivos")
		w.descripcion="Un listado mensual de las entradas de tu sitio"
		b.add(w)
		w=AddItem("Archivos")
		w.descripcion="Un listado mensual de las entradas de tu sitio"
		b.add(w)
		w=AddItem("Archivos")
		w.descripcion="Un listado mensual de las entradas de tu sitio"
		b.add(w)
		w=AddItem("Archivos")
		w.descripcion="Un listado mensual de las entradas de tu sitio"
		b.add(w)
		
		self.add(b)
		b.target.css("height","92vh")
		
		


		

		


		
		



		