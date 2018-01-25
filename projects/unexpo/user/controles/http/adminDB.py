if p["multipart/form-data"]==False:
	if p["control"]=="admin" and p["app"]==settings.app:
		if p["action"]=="db":

			
			args=p["kwargs"]["args"].keys()

			args.remove("campos")
			args.remove("nombre")

			tabla=args[0]
			if p["args"]["args"][tabla]==None:
				p["model"]["main"].crearPlantilla(p["args"]["args"]["nombre"],p["args"]["args"]["campos"])
				print "Plantilla creada"
			else:
				p["model"]["main"].modificarPlantilla(p["args"]["args"][tabla],p["args"]["args"]["nombre"],p["args"]["args"]["campos"])

