__pragma__("alias","s","$")
from Widget import Widget
from HeaderCustomize import HeaderCustomize
from ButtonSettings import ButtonSettings
from Acordion import Acordion
from TabAcordion import TabAcordion
from Input import Input
from TinyMCE import TinyMCE

class Widgets(Widget):
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
		self.add(w)
		w=ButtonSettings("Blog Sidebar")
		w.slider=self.slider
		w.screen=self.screen
		w._screen=3
		w._siguiente=2
		self.add(w)
		w=ButtonSettings("Footer 1")
		w.slider=self.slider
		w.screen=self.screen
		w._screen=4
		w._siguiente=2
		self.add(w)

		
		w=ButtonSettings("Footer 2")
		w.slider=self.slider
		w.screen=self.screen
		w._screen=5
		w._siguiente=2
		self.add(w)
		#==================================
		w=HeaderCustomize("Blog Sidebar")
		
		w.slider=self.slider
		w._atras=1
		w._screen=6
		w.descripcion="""
		Add widgets here to appear in your sidebar on
		blog posts and archive pages.
		"""
		self.screen.appendToTab(3,w)
		a=Acordion()
		t=TabAcordion("HTML:")
		t.descripcion="Encuentranos"
		w=Input("Titulo")
		w.value="Encuentranos"
		w=TinyMCE()
		t.add(w)
		a.addTab(t)
		t=TabAcordion("Buscar:")
		t.descripcion="Busqueda"
		w=Input("Titulo")
		w.value="Busqueda"
		a.addTab(w)
		t=TabAcordion("HTML:")
		t.descripcion="Acerca del sitio"
		w=Input("Titulo")
		w.value="Acerca del sitio"
		w=TinyMCE()
		w.value="""
		Este puede ser un buen lugar para presentarte y presentar tu sitio o incluir algunos créditos.
		"""
		self.screen.appendToTab(3,a)
		
		


		w=HeaderCustomize("Footer 1")
		w.slider=self.slider
		w._atras=1
		w._screen=7
		self.screen.appendToTab(4,w)
		a=Acordion()
		t=TabAcordion("HTML:")
		t.descripcion="Encuentranos"
		w=Input("Titulo")
		w.value="Encuentranos"
		t.add(w)
		w=TinyMCE()
		t.add(w)
		a.addTab(t)
		self.screen.appendToTab(4,a)
		w=HeaderCustomize("Footer 2")
		w.slider=self.slider
		w._atras=1
		w._screen=8
		self.screen.appendToTab(5,w)
		a=Acordion()
		t=TabAcordion("HTML:")
		t.descripcion="Acerca del sitio"
		w=Input("Titulo")
		w.value="Acerca del sitio"
		t.add(w)
		w=TinyMCE()
		w.value="""
		Este puede ser un buen lugar para presentarte y presentar tu sitio o incluir algunos créditos.
		"""
		t.add(w)
		a.addTab(t)
		t=TabAcordion("Buscar:")
		t.descripcion="Busqueda"
		w=Input("Titulo")
		w.value="Busqueda"
		t.add(w)
		a.addTab(t)
		self.screen.appendToTab(5,a)
		self.css({"padding-left":"20px","padding-right":"20px"},None,">div:nth-child(n+2)")


		
		
		
		