from modulos.Plugin import Shortcode



class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="iframe"



		
	def run(self,atts,content):
		
		self.plugin.data["sc"]=atts["sc"]
		
		return self.incluir()

		