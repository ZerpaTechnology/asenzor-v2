from modulos.ztec.zred import Headers
from modulos.ztec.zu import redict
from config import config
class apps(object):
	"""docstring for apps"""
	def __init__(self,data):
		self.data=data
		self.HEADERS=Headers()
		self.HEADERS.set_headers({"Content-type":"text/plain\n"})
		self.HEADERS.show()
		apps=[]
		if self.data["metodo"]==None:
			self.HEADERS.show()
			for elem in self.data["model"]["global"].obtenerFilas("apps"):
				if "Suspendida" in elem[4] and elem[0]==self.data["app"]:
					self.data["app"]=None
				apps.append(elem[0])
			
			print {"apps":apps,"default_app":config.default_app}

		pass

	def versiones_disponibles(self):
		versiones={}

		self.HEADERS.show()
		if len(self.data["args"])>2:
			if self.data["args"][2]=="sizes":
				for elem in config.versiones_disponibles:
					for elem2 in self.data["model"]["global"].obtenerFilas("Asenzor"):
						if elem2[1][0]["value"]==elem:
							versiones[elem2[1][4]["value"]]=elem2[1][5]["value"]
				print versiones

		else:

			for elem in config.versiones_disponibles:
					for elem2 in self.data["model"]["global"].obtenerFilas("Asenzor"):						
						if elem2[1][0]["value"]==elem:
							versiones[elem]=elem2[1][4]["value"]
			print versiones

	def webapp(self):
		self.HEADERS.show()
		if self.data["action"]=="install":
			import urllib2,urllib
			

			params={"app":"asenzor","control":self.data["control"],"action":"download","item":self.data["item"]}
			
			params = urllib.urlencode(params) 
			

			
			f=urllib2.urlopen(config.asenzor_host+config.controller_folder+"ajax.py",params)
			
			ruta=f.read().strip()
			zred.download2(ruta,config.base_root+config.apps_folder)
			f.close()
			
			zred.zipextract(config.base_root+config.apps_folder+ruta.split("/")[-1])
			os.remove(config.base_root+config.apps_folder+ruta.split("/")[-1])
			self.data["model"]["global"].instalarApp(self.data["item"])
	def download(self):
		zred.downloader(config,config.base_root+config.projects_folder+self.data["item"]+".zip",get=False)
		pass
	def unistall(self):
		pass
	def install(self):
		pass
	def allapps(self):
		
		self.HEADERS.show()
		d=redict({"[D|d]estacad[a|o]s?":[],
		   "[P|p]opular(es)?":[],
		   "[R|r]ecientes?":[],
		   "[F|f]avorit[a|o]s?":[],
		  })
		

		for elem in self.data["model"]["global"].obtenerFilas("Gestor-apps"):
			
			if "Destacada" in elem[-1] or "Destacado" in elem[-1] or  "Destacados" in elem[-1] or "Destacadas" in elem[-1]:
				
				d["Destacada"].append(elem)
			if "Popular" in elem[-1]:
				d["Popular"].append(elem)
			if "Reciente" in elem[-1]:
				d["Reciente"].append(elem)
			if "Favorita" in elem[-1] or "Favoritas" in elem[-1] or "Favoritos" in elem[-1]:
				d["Favorita"].append(elem)
			
		
		print d

	
		



