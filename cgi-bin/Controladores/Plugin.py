class Plugin():
	"""docstring for Plugin"""
	def __init__(self,data):
		import os
		self.data=data

		from config import config
		from modulos.ztec.zred import gringolizar
		import imp

		if self.data["control"] in os.listdir(config.base_root+config.plugins_folder):

			control=imp.load_source("",config.base_root+config.plugins_folder+self.data["control"]+"/default.py").Plugin(self.data)
			


			if self.data["metodo"]!=None:
				


				if gringolizar(self.data["metodo"]) in dir(control):
					
					exec("control."+gringolizar(self.data["metodo"])+"()")


				else:
					control.metodo_desconocido()
	def metodo_desconocido(self):
		pass
