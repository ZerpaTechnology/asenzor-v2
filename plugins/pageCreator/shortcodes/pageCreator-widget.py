from zred import Shortcode

class shortcode(Shortcode):
	def __init__(self,models,app_models):
		Shortcode.__init__(self,False,models,app_models)
	def run(self,atts,content):
		return "soy el plugin"
		