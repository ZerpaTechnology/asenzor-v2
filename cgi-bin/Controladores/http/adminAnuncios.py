#POST subcontroller
if  p["app"]==settings.app:
	if beforeAction=="Galeria":
		if data["action"].value=="Registrar":
				imagenes=[]
				for elem in data["img1"]:
					imagenes.append(elem.value)
				p["model"]["galerias"].crearAnuncio(data["titulo"].value,p["model"]["galerias"].obtenerFilas("Opciones")[0][1].index(data["imagen"].value),data["contenido"].value)
				
		elif data["action"].value=="Guardar":
			imagenes=[]
			for elem in data["img1"]:
				imagenes.append(elem.value)
			
			if p["model"]["anuncios"].modificarAnuncio(indice,data["titulo"].value,p["model"]["galerias"].obtenerFilas("Opciones")[0][1].index(data["imagen"].value),data["contenido"].value):
				redirecter("",settings.app,"admin","index","Anuncios",action="listar")()
