
if rest["method"]=="ajax":
	#muestra las versiones disponibles para descargar
	

	


	if rest["control"]=="versiones_disponibles":
		versiones={}
		HEADERS.show()


		if len(rest["args"])>2:
			if rest["args"][2]=="sizes":
				for elem in config.versiones_disponibles:
					for elem2 in rest["model"]["global"].obtenerFilas("Asenzor"):
						if elem2[1][0]["value"]==elem:
							versiones[elem2[1][4]["value"]]=elem2[1][5]["value"]
				print versiones

		else:

			for elem in config.versiones_disponibles:
					for elem2 in rest["model"]["global"].obtenerFilas("Asenzor"):						
						if elem2[1][0]["value"]==elem:
							versiones[elem]=elem2[1][4]["value"]
			print versiones
	#muestra las aplicaciones activas
	elif rest["control"]=="apps":
		apps=[]
		HEADERS.show()
		for elem in rest["model"]["global"].obtenerFilas("apps"):
			if "Suspendida" in elem[4] and elem[0]==rest["app"]:
				rest["app"]=None
			apps.append(elem[0])
		print {"apps":apps,"default_app":config.default_app}

	elif rest["control"]=="webapp":
		HEADERS.show()
		if rest["action"]=="install":
			import urllib2,urllib
			

			params={"app":"asenzor","control":rest["control"],"action":"download","item":rest["item"]}
			
			params = urllib.urlencode(params) 
			

			
			f=urllib2.urlopen(config.asenzor_host+config.controller_folder+"ajax.py",params)
			
			ruta=f.read().strip()
			zred.download2(ruta,config.base_root+config.apps_folder)
			f.close()
			
			zred.zipextract(config.base_root+config.apps_folder+ruta.split("/")[-1])
			os.remove(config.base_root+config.apps_folder+ruta.split("/")[-1])
			rest["model"]["global"].instalarApp(rest["item"])
			

			


		elif rest["action"]=="download":
			
			zred.downloader(config,config.base_root+config.projects_folder+rest["item"]+".zip",get=False)
			pass
			

		elif rest["action"]=="unistall":
			pass
	elif rest["control"]=="plugin":
		HEADERS.show()
		if rest["action"]=="install":
			import urllib2,urllib
			

			params={"app":None,"control":rest["control"],"action":"download","item":rest["item"]}
			
			params = urllib.urlencode(params) 
			

			
			f=urllib2.urlopen(config.asenzor_host+config.controller_folder+"ajax.py",params)
			
			ruta=f.read().strip()
			zred.download2(ruta,config.base_root+config.plugins_folder)
			f.close()
			
			zred.zipextract(config.base_root+config.plugins_folder+ruta.split("/")[-1])
			os.remove(config.base_root+config.plugins_folder+ruta.split("/")[-1])
			rest["model"]["global"].instalarApp(rest["item"])
		elif rest["action"]=="unistall":
			pass
	elif rest["control"]=="allapps":
		HEADERS.show()
		d=redict({"[D|d]estacad[a|o]s?":[],
		   "[P|p]opular(es)?":[],
		   "[R|r]ecientes?":[],
		   "[F|f]avorit[a|o]s?":[],
		  })
		

		for elem in rest["model"]["global"].obtenerFilas("Gestor-apps"):
			
			if "Destacada" in elem[-1] or "Destacado" in elem[-1] or  "Destacados" in elem[-1] or "Destacadas" in elem[-1]:
				
				d["Destacada"].append(elem)
			if "Popular" in elem[-1]:
				d["Popular"].append(elem)
			if "Reciente" in elem[-1]:
				d["Reciente"].append(elem)
			if "Favorita" in elem[-1] or "Favoritas" in elem[-1] or "Favoritos" in elem[-1]:
				d["Favorita"].append(elem)
			
		
		print d
	elif rest["control"]=="plugins":
		HEADERS.show()
		d=redict({"[D|d]estacad[a|o]s?":[],
		   "[P|p]opular(es)?":[],
		   "[R|r]ecientes?":[],
		   "[F|f]avorit[a|o]s?":[],
		  })
		

		for elem in rest["model"]["global"].obtenerFilas("Gestor-plugins"):
			
			if "Destacada" in elem[-1] or "Destacado" in elem[-1] or  "Destacados" in elem[-1] or "Destacadas" in elem[-1]:
				
				d["Destacada"].append(elem)
			if "Popular" in elem[-1]:
				d["Popular"].append(elem)
			if "Reciente" in elem[-1]:
				d["Reciente"].append(elem)
			if "Favorita" in elem[-1] or "Favoritas" in elem[-1] or "Favoritos" in elem[-1]:
				d["Favorita"].append(elem)
			
		
		print d



