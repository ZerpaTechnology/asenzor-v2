from modulos.Plugin import Shortcode

from config import config
from settings import config as settings

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="slider"

		
	def run(self,atts,content):
		self.plugin.data['plugin-widget']={'slider':self.plugin.model["galerias"].obtenerFilas("Sliders")[atts["id"]]}
		
		return self.incluir(self.plugin.data)