#POST subcontroller
if  p["app"]==settings.app:
	if beforeAction=="Publicacion":
		if data["action"].value=="Registrar":
				
				p["model"]["publicaciones"].crearPublicacion(data["titulo"].value,p["model"]["publicaciones"].obtenerFilas("Opciones")[0][1].index(data["img"].value),data["publish"].value)
			
		elif data["action"].value=="Guardar":
			
			if p["model"]["publicaciones"].modificarPublicacion(indice,data["titulo"].value,p["model"]["publicaciones"].obtenerFilas("Opciones")[0][1].index(data["img"].value),data["publish"].value):
				redirecter("",settings.app,"index",admin=True,args="Publicaciones",action="listar")()
