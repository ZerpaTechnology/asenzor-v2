from modulos.Plugin import Shortcode



class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="form-login"


		
	def run(self,atts,content):
	
		if self.plugin.data["login"]==True:

			contenido=self.plugin.model["main"].obtenerEstudiante(self.plugin.data["user"]["email"])
			self.plugin.data["estudiante"]={"nombre":contenido[0]["nombre"],
									"expediente":contenido[0]["expediente"]}
			self.widget="panel-min"

		return self.incluir()

		