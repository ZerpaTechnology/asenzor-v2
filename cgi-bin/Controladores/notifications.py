class notifications(object):
	"""docstring for notifications"""
	def __init__(self, data):
		self.data=data
	def versiones(self):
		versiones={}
		for elem in config.versiones_disponibles:
			for elem2 in self.data["model"]["global"].obtenerFilas("Asenzor"):
				if elem2[0]==elem:
					versiones[elem]=elem2[1][4]["value"]
		print versiones