from modulos.ztec.zred import Headers
from modulos.ztec.zu import redict

class plugins(object):
	def __init__(self,data):
		self.HEADERS=Headers()
		self.HEADERS.show()
		self.data=data
		if self.data["metodo"]==None:
			d=redict({"[D|d]estacad[a|o]s?":[],
			   "[P|p]opular(es)?":[],
			   "[R|r]ecientes?":[],
			   "[F|f]avorit[a|o]s?":[],
			  })
			

			for elem in self.data["model"]["global"].obtenerFilas("Gestor-plugins"):
				
				if "Destacada" in elem[-1] or "Destacado" in elem[-1] or  "Destacados" in elem[-1] or "Destacadas" in elem[-1]:
					
					d["Destacada"].append(elem)
				if "Popular" in elem[-1]:
					d["Popular"].append(elem)
				if "Reciente" in elem[-1]:
					d["Reciente"].append(elem)
				if "Favorita" in elem[-1] or "Favoritas" in elem[-1] or "Favoritos" in elem[-1]:
					d["Favorita"].append(elem)
				
			
			print d
	def install(self):
		import urllib2,urllib
		params={"app":None,"control":self.data["control"],"action":"download","item":self.data["item"]}
		params = urllib.urlencode(params) 
		f=urllib2.urlopen(config.asenzor_host,params)
		
		ruta=f.read().strip()
		zred.download2(ruta,config.base_root+config.plugins_folder)
		f.close()
		
		zred.zipextract(config.base_root+config.plugins_folder+ruta.split("/")[-1])
		os.remove(config.base_root+config.plugins_folder+ruta.split("/")[-1])
		self.data["model"]["global"].instalarApp(self.data["item"])