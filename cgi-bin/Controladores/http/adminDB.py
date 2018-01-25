if p["multipart/form-data"]==False:	

	if p["control"]=="admin" and p["app"]==settings.app and p["method"]=="ajax":

		if p["action"]=="db":

			if "motor" in p and normalizar(p["motor"])==True:

				#p["modelo"]="usuario"
				#p["metodo"]="login"
				#p["args"]=["usuario","password"]

				
				if normalizar(p["args"])==[] and p["kwargs"]:
					parametros=""
					for elem in list(p["kwargs"]):
						if type(normalizar(p["kwargs"])[elem])==str:
							parametros+=elem+"='"+p["kwargs"][elem]+"',"
						else:
							parametros+=elem+"="+p["kwargs"][elem]+","
					for elem in settings.admin_models_embebed:

						if elem==p["modelo"] and p["metodo"] in settings.admin_models_embebed[elem] and p["user"]["permisologia"]<1:
							exec('request=p["model"]["'+p["modelo"]+'"].'+p["metodo"]+"("+parametros+")")
							print request
					for elem in settings.models_embebed:

						if elem==p["modelo"] and p["metodo"] in settings.models_embebed[elem]:
							exec('request=p["model"]["'+p["modelo"]+'"].'+p["metodo"]+"("+parametros+")")
							print request
				else:
					try:

						for elem in settings.admin_models_embebed:


							if elem==p["modelo"] and p["metodo"] in settings.models_embebed[elem] and p["user"]["permisologia"]<1:
								exec('request=p["model"]["'+p["modelo"]+'"].'+p["metodo"]+"("+str(p["args"])[1:-1]+")")
								print request
						for elem in settings.models_embebed:
							
							if elem==p["modelo"] and p["metodo"] in settings.models_embebed[elem]:
								
								exec('request=p["model"]["'+p["modelo"]+'"].'+p["metodo"]+"("+str(p["args"])[1:-1]+")")

								print request

					except Exception,e:
						print e


			
				#["modelo","metodo",]
				

			else:
				"""
				args=p["kwargs"]["args"].keys()
				args.remove("campos")
				args.remove("nombre")

				tabla=args[0]
				if p["args"]["args"][tabla]==None:
					p["model"]["main"].crearPlantilla(p["args"]["args"]["nombre"],p["args"]["args"]["campos"])
					print "Plantilla creada"
				else:
					p["model"]["main"].modificarPlantilla(p["args"]["args"][tabla],p["args"]["args"]["nombre"],p["args"]["args"]["campos"])
				"""
