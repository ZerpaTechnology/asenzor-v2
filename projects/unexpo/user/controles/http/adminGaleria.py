#POST subcontroller

if  p["app"]==settings.app:

	if beforeAction=="Galeria":
		if data["action"].value=="Registrar":
				imagenes=[]
				for elem in data["img"]:
					imagenes.append(elem.value)
				p["model"]["galerias"].crearGaleria(data["galeria"].value,imagenes)
				
		elif data["action"].value=="Guardar":
			imagenes=[]

			for elem in data["img"]:
				imagenes.append(elem.value)
			if p["model"]["galerias"].modificarGaleria(indice,data["galeria"].value,imagenes):
				redirecter(config,settings.app,"admin","index","Galerias",action="listar")()
				
