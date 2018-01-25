from zmodel import Model
from modulos.ztec import zu
class model(Model):
	"""docstring for Model"""
	def obtenerShortcodes(self,id=None,alias=None):
		
		if self.update():
			if id!=None and alias==None:
				for k,elem in enumerate(self.obtenerFilas("Shortcodes")):
					if int(id)==k:
						return elem

			elif id==None and alias!=None:
				for k,elem in enumerate(self.obtenerFilas("Shortcodes")):
					if alias==elem[0]:
						return elem

	def crearShortcode(self,data,metadatos=None):
		if self.request(metodo=self.crearShortcode.__func__):
			
			nuevo=self.valorizarEstructura(data,self.obtenerEstructura("Shortcodes"),None,True)
			
			nuevo[2]={"Shortcode":self.obtenerLongitud("Shortcodes")}
			nuevo[3]=zu.DateTime()
			self.fusionarMetadatos(nuevo[4],metadatos)
			
			self.db("Shortcodes").insertar(nuevo[0],nuevo[1],nuevo[2],nuevo[3],nuevo[4])

			self.grabar()
			

	def modificarShortcode(self,indice,data,metadatos=None):
		self.actualizarContenido(indice,data,metadatos,"Shortcodes")
	
