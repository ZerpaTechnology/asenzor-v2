#POST subcontroller


if  p["app"]==settings.app and p["multipart/form-data"]==True:

	if p["method"]!="ajax":
		HEADERS.show()

		if len(normalizar(p["cookies"]["beforeArgs"]))>0 and  normalizar(p["cookies"]["beforeArgs"])[0]=="Info":
			if data["action"].value=="Registrar":					
					if p["model"]["informaciones"].crearInformacion(data["titulo"].value,data["contenido"].value):
						redirecter(config,settings.app,"admin","index","Informaciones",action="listar")()
			elif data["action"].value=="Guardar":

				if p["model"]["informaciones"].modificarInformacion(indice,data["titulo"].value,data["contenido"].value):
					redirecter(config,settings.app,"admin","index","Informaciones",action="listar")()

