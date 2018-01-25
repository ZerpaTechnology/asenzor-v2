# -*- coding: utf-8 -*-
from modulos.Plugin import Shortcode



class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="registro"
		

		
	def run(self,atts,content):
		
		return self.incluir()

		