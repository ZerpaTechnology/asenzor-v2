from modulos.Plugin import Shortcode

from config import config
from settings import config as settings

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="galeria"
        #prueba
		

		
	def run(self,atts,content):
		self.plugin.data['plugin-widget']={"galeria":self.plugin.model["galerias"].obtenerFilas("Galerias")[atts["id"]],
                                   "paginacion":6,
                                    "clase":"sc-galeria"}

		return self.incluir(self.plugin.data)