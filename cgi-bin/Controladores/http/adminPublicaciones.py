#POST subcontrollerp

if  p["app"]==settings.app and "multipart/form-data" in p and p["multipart/form-data"]==True:
	
	
	if len(normalizar(p["cookies"]["beforeArgs"]))>0 and  normalizar(p["cookies"]["beforeArgs"])[0]=="Publicacion":
		if data["action"].value=="Registrar":

			  
				p["model"]["publicaciones"].crearPublicacion(data)
				redirecter(config,settings.app,"admin","index","Publicaciones",action="listar")()

			
		elif data["action"].value=="Guardar":
			
			if p["model"]["publicaciones"].modificarPublicacion(indice,data):
				redirecter(config,settings.app,"admin","index","Publicaciones",action="listar")()
				pass  
        		