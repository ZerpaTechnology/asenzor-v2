from zmodel import Model
class model(Model):
	"""docstring for Model"""
	def obtenerEstudiante(self,email=None,expediente=None):
		
		if self.update():


			for elem in self.obtenerFilas("Estudiantes"):
				contenido=self.contener(elem[1])


				if expediente==None:
					if contenido[0]["email"]["value"]==email:
						return contenido
				else:
				
					if contenido[0]["expediente"]["value"]==int(expediente):
						return contenido


	def pagos_de_becas_acumulados(self):
		pass

	
