__pragma__("xpath",["","../../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomize import HeaderCustomize
from CheckBoxList import CheckBoxList
from CheckBox import CheckBox
from SelectColor import SelectColor
class Colores(Widget):
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
		w=CheckBoxList("Color Scheme")
		_w=CheckBox("Light")
		w.add(_w)
		_w=CheckBox("Negro")
		w.add(_w)
		_w=CheckBox("Custom")
		w.add(_w)
		color=SelectColor()
		

		
		self.add(w)
		def mostrar():
			nonlocal color
			color.show()
		def ocultar():
			nonlocal color
			color.hidden()

		_w.activador=mostrar
		_w.desactivador=ocultar
		color.hidden()
		self.add(color)
		self.css({"padding-left":"20px","padding-right":"20px"},None,">div:nth-child(n+2)")
		






		
		