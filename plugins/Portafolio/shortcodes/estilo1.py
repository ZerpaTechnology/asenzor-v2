from modulos.Plugin import Shortcode

from config import config

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="estilo1"

		
	def run(self,atts,content):
		return self.incluir()

	