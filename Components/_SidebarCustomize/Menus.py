__pragma__("xpath",["","../../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomize import HeaderCustomize
from ButtonSettings import ButtonSettings
from ButtonInput import ButtonInput
from Select import Select
from EnlaceButton import EnlaceButton
from Input import Input
from Acordion import Acordion
from TabAcordion import TabAcordion
from CheckBox import CheckBox
from CheckBoxList import CheckBoxList
from Textarea import Textarea
class Menus(Widget):
	"""docstring for Colores"""
	def __init__(self,titulo):
		Widget.__init__(self,titulo)
	def update(self):
		self.__update__()
		w=HeaderCustomize(self.titulo)
		w.slider=self.slider
		w._atras=self._atras
		w._screen=self._screen
		self.add(w)
		w=ButtonSettings("Ubicaciones de menús")
		w.slider=self.slider
		w.screen=self.screen
		w._screen=0
		w._siguiente=2
		self.add(w)

		self.addSeparador()

		w=ButtonSettings("Menús de enlaces de Redes Sociales")
		w.descripcion="(Actualmente fijado en: Menú de enlaces de Redes Sociales)"
		w.slider=self.slider
		w.screen=self.screen
		w._screen=1
		w._siguiente=2
		self.add(w)
		w=ButtonSettings("Top Menú")
		w.descripcion="(Actualmente fijado en: Top Menú)"

		w.slider=self.slider
		w.screen=self.screen
		w._screen=2
		w._siguiente=2
		self.add(w)
		w=ButtonInput("Añadir al menu")
		self.add(w)
		#
		w=HeaderCustomize("Ubicaciones de menús")
		w.slider=self.slider
		w._atras=1
		w._screen=3
		self.descripcion="""
		Tu tema soporta 2 menús. Elige qué menú debería aparecer en cada lugar.

		También puedes poner menús en los widgets con el widget “Menú personalizado”
		"""
		self.screen.appendToTab(0,w)
		w=Select("Top Menu")
		w.opciones=["--Eligir--","Menu de enlaces a redes sociales","Top menu",]
		self.screen.appendToTab(0,w)
		e=EnlaceButton("Editar menu")
		self.screen.appendToTab(0,e)
		w=Select("Top Menu")
		w.opciones=["--Eligir--","Menu de enlaces a redes sociales","Top menu",]
		self.screen.appendToTab(0,w)
		e=EnlaceButton("Editar menu")
		self.screen.appendToTab(0,e)
		
		self.screen.tabs[0].find(">div:nth-child(n+2)").css({"padding-left":"20px","padding-right":"20px"})
		
		w=HeaderCustomize("Menús de enlaces de Redes Sociales")
		w.slider=self.slider
		w._atras=1
		w._screen=3
		self.screen.appendToTab(1,w)

		w=Input()
		w.value="Menús de enlaces de Redes Sociales"
		self.screen.appendToTab(1,w)
		a=Acordion("")
		

		t=TabAcordion("Yelp")
		

		w=Input("URL")
		w.value="https://www.yelp.com"
		t.add(w)

		w=Input("Etiqueta de navegación")
		w.value="Yelp"
		t.add(w)

		w=CheckBox("Abrir enlace en una nueva pestaña")
		t.add(w)

		w=Input("Atributos del titulo")
		t.add(w)

		w=Input("Relacion con el enlace (XFN)")
		t.add(w)
		#se debe agregar el widget antes de clonar y despues aplicar un reload si se modifican atributos
		w=Textarea("Descripción")
		w.postdescripcion="La descripción se mostrará en los menús si el tema actual lo soporta."
		t.add(w)

		w=EnlaceButton("Eliminar")
		t.add(w)
		w.color="red"
		a.addTab(t)
		t2=t.clone()

		t2.titulo="Facebook"

		t2.children[0].value="https://facebook.com"
		t2.reload()
		a.addTab(t2)
		
		t3=t.clone()
		t3.titulo="Twitter"
		t3.children[0].value="https://Twitter.com"
		t3.reload()
		a.addTab(t3)
		t4=t.clone()
		t4.titulo="Instagram"
		t4.children[0].value="https://Instagram.com"
		
		a.addTab(t4)


		t5=t.clone()
		t5.titulo="Correo electronico"
		t3.children[0].value="jzerpa.occoa@gmail.com"
		a.addTab(t5)
		
		self.screen.appendToTab(1,a)
		check=CheckBoxList("Mostrar ubicación")
		check.value=[["Top Menu",False,"(Actual: Top Menu)"],
					["Menu de enlaces de Redes Sociales",False,"(Actual: Menu de enlaces de Redes Sociales)"],
					]
		self.screen.appendToTab(1,check)
		check2=CheckBoxList("Opciones de menú")
		check2.value=[["Agregar automaticamente nuevas paginas de nivel superior a este menu",False],
					]
		self.screen.appendToTab(1,check2)
		self.screen.tabs[1].find(">div:nth-child(n+2)").css({"padding-left":"20px","padding-right":"20px"})




		w=HeaderCustomize("Top Menú")
		w.slider=self.slider
		w._atras=1
		w._screen=3
		self.screen.appendToTab(2,w)
		w=Input()
		w.value="Top Menu"
		self.screen.appendToTab(2,w)


		a=Acordion()
		t=t.clone()
		t.titulo="Inicio"
		a.addTab(t)
		t=t.clone()
		t.titulo="Acerca de"
		t.descripcion="Pagina"
		a.addTab(t)
		t=t.clone()
		t.titulo="Blog"
		t.descripcion="Pagina"
		a.addTab(t)
		t=t.clone()
		t.titulo="Contacto"
		t.descripcion="Pagina"
		a.addTab(t)
		self.screen.appendToTab(2,a)

		check=check.clone()
		self.screen.appendToTab(2,check)

		check2=check2.clone()
		self.screen.appendToTab(2,check2.clone())
		self.css({"padding-left":"20px","padding-right":"20px"},None,">div:nth-child(n+2)")









		