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
from Input import Input
from Textarea import Textarea
from FooterCustomize import FooterCustomize
settings=nuclear.Settings()

class SidebarCustomize(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""
			<div class='header-top'>
				<span class='close'> X </span><button name='save'>{}</button>
			</div>
			<div class='content'>
			</div>
			<div class='footer-bottom'>
				
				<span class='ocultar'> 
					<span class='icon'></span>
					<span class='text'>{}</span>
				</span>
				<div class='responsive'>
					<span class='desktop'></span>
					<span class='tablet'></span>
					<span class='phone'></span>
				</div>
				
			</div>
		"""
		self.content=lambda self=self:self.target.find(">.content")
		self.btn_save="Guardar"
		self.btn_desing="Ocultar"
		self.btn_desktop=config.base_url+"static/imgs/iconos/desktop.png"
		self.btn_tablet=config.base_url+"static/imgs/iconos/tablet.png"
		self.btn_phone=config.base_url+"static/imgs/iconos/smartphone.png"


	def update(self):
		self._update=True
		self.format=[self.btn_save,self.btn_desing]
		self.__update__()
		self.target.find(">.footer-bottom").find(">.responsive").find(">.desktop").css("background-image","url('{}')".format(self.btn_desktop))
		self.target.find(">.footer-bottom").find(">.responsive").find(">.tablet").css("background-image","url('{}')".format(self.btn_tablet))
		self.target.find(">.footer-bottom").find(">.responsive").find(">.phone").css("background-image","url('{}')".format(self.btn_phone))
		screens1=BasicTabs("",10)
		screens1.tabWidth=280
		screens2=BasicTabs("",10)
		screens2.tabWidth=280

		slider=BasicSlider()
		slider.tabWidth=280
		self.add(slider)
		slider.appendToTab(1,screens1)
		slider.appendToTab(2,screens2)
		
		
		
		

		w=HeaderCustomizeMain(settings.app)
		slider.appendToTab(0,w)
		w=BandaTema()
		slider.appendToTab(0,w)
		

		w=ButtonSettings("Identidad del sitio")		
		w.slider=slider
		w.screen=screens1
		w._screen=0
		slider.appendToTab(0,w)

		w=ButtonSettings("Colores")
		w.slider=slider
		w.screen=screens1
		w._screen=1
		slider.appendToTab(0,w)
		
		w=ButtonSettings("Cabecera multimedia")
		w.slider=slider
		w.screen=screens1
		w._screen=2
		slider.appendToTab(0,w)

		w=ButtonSettings("Menús")
		w.slider=slider
		w.screen=screens1

		w._screen=3
		slider.appendToTab(0,w)

		w=ButtonSettings("Widgets")
		w.slider=slider
		w.screen=screens1
		w._screen=4
		slider.appendToTab(0,w)

		w=ButtonSettings("Portada estatica")
		w.slider=slider
		w.screen=screens1
		w._screen=5
		slider.appendToTab(0,w)
		
		w=ButtonSettings("Themes Options")
		w.slider=slider
		w.screen=screens1
		w._screen=6
		slider.appendToTab(0,w)

		w=ButtonSettings("CSS adicional")
		w.slider=slider
		w.screen=screens1
		w._screen=7
		slider.appendToTab(0,w)
		

		

		"""
		
		w.add(Input("texto"))
		w.add(Textarea("texto"))
		"""
		
		
		
		
		
		
		
		
		
		
		w=Identidad_del_sitio("Identidad del sitio")

		w.Media=self.Media
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(0,w)

		w=Colores("Colores")
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(1,w)
		
		w=CabeceraMultimedia("Cabecera multimedia")
		w.Media=self.Media
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(2,w)

		w=Menus("Menús")
		w.screen=screens2
		w.slider=slider
		w._atras=0
		w._screen=0

		screens1.appendToTab(3,w)

		w=Widgets("Widgets")
		w.screen=screens2
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(4,w)

		w=PortadaEstatica("Portada estática")
		w.Media=self.Media
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(5,w)
		
		w=ThemesOptions("Themes Options")
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(6,w)
		
		w=HeaderCustomize("CSS Adicional")
		w.slider=slider
		w._atras=0
		w._screen=0
		screens1.appendToTab(7,w)
		w=Textarea()
		
		w.value="""
		/*
		Puedes añadir tu propio CSS aquí.
		
		Haz clic en el icono de ayuda de arriba para averiguar más.
		*/
		"""
		
		screens1.appendToTab(7,w)
		w.target.find("textarea").css("height","90vh")

		

		

		
		#IDENTIDAD DEL SITIO
		
		
		






		