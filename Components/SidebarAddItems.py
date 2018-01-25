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
from Input import Input
from Textarea import Textarea
from FooterCustomize import FooterCustomize
from BoxScroll import BoxScroll
from AddItem import AddItem
from Button import Button
from ButtonAddItem import ButtonAddItem
from InputAndButton import InputAndButton

settings=nuclear.Settings()

class SidebarAddItems(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)


	def update(self):
		self.__update__()
		w=InputSearch()
		self.add(w)
		w.target.css("height","8vh")

		b=BoxScroll()
		a=Acordion()
		t=TabAcordion("Enlaces personalizados")
		w=Input("URL")
		w.value="http://"
		t.add(w)
		w=Input("Texto del enlace")
		t.add(w)
		w=Button("Añadir al menu")
		t.add(w)
		a.addTab(t)

		t=TabAcordion("Páginas")
		_b=BoxScroll()
		_w=ButtonAddItem("Inicio")
		_w.descripcion="Enlace personalizado"
		_b.add(_w)
		_w=ButtonAddItem("Inicio")
		_w.descripcion="Página"
		_b.add(_w)
		t.add(_b)
		_w=InputAndButton("Añadir")
		_w.placeholder="Añadir nueva pagina"
		t.add(_w)

		a.addTab(t)

		t=TabAcordion("Entradas")
		_b=BoxScroll()
		t.add(_b)

		
		a.addTab(t)

		t=TabAcordion("Categorias")
		_b=BoxScroll()
		t.add(_b)
		
		a.addTab(t)

		t=TabAcordion("Etiquetas")
		_b=BoxScroll()
		t.add(_b)
		
		a.addTab(t)

		t=TabAcordion("Formato")
		_b=BoxScroll()
		t.add(_b)
		
		a.addTab(t)
		b.add(a)
		self.add(b)
		b.target.css("height","92vh")
		
		


		

		


		
		



		