from zred import Shortcode

class shortcode(Shortcode):
	def __init__(self,data,models):
		Shortcode.__init__(self,data,models)
	def run(self,atts,content):
		return "soy el plugin"
		