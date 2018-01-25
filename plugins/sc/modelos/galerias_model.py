from zmodel import Model
import zu
class model(Model):
	"""docstring for Model"""
	def obtenerGaleria(self,id=None,alias=None):
		
		if self.update():
			if id!=None and alias==None:
				for k,elem in enumerate(self.obtenerFilas("Galeria")):
					if int(id)==k:
						return elem

			elif id==None and alias!=None:
				for k,elem in enumerate(self.obtenerFilas("Galeria")):
					if alias==elem[0]:
						return elem

	def crearGaleria(self,data,metadatos=None):
		if self.request(metodo=self.crearGaleria.__func__):
			
			nuevo=self.valorizarEstructura(data,self.obtenerEstructura("Galerias"),None,True)
		
			nuevo[2]={"Galeria":self.obtenerLongitud("Galerias")}
			nuevo[3]=zu.DateTime()
			self.fusionarMetadatos(nuevo[4],metadatos)

			self.db("Galerias").insertar(nuevo[0],nuevo[1],nuevo[2],nuevo[3],nuevo[4])
			self.grabar()
			

	def modificarGaleria(self,indice,data,metadatos=None):
		self.actualizarContenido(indice,data,metadatos,"Galerias")
	
	def crearSlider(self,data,metadatos=None):
		if self.request(metodo=self.crearSlider.__func__):
			
			nuevo=self.valorizarEstructura(data,self.obtenerEstructura("Sliders"),None,True)

		
			nuevo[2]={"Slider":self.obtenerLongitud("Sliders")}
			nuevo[3]=zu.DateTime()
			self.fusionarMetadatos(nuevo[4],metadatos)

			self.db("Sliders").insertar(nuevo[0],nuevo[1],nuevo[2],nuevo[3],nuevo[4])
			self.grabar()
			

	def modificarSlider(self,indice,data,metadatos=None):
		

		self.actualizarContenido(indice,data,metadatos,"Sliders")
	