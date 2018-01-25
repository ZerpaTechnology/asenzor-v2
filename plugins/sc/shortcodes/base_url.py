from modulos.Plugin import Shortcode

from config import config

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		

		
	def run(self,atts,content):
		return config.base_url

	