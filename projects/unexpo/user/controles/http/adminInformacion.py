#POST subcontroller
if  p["app"]==settings.app:
	if beforeAction=="Info":
		if data["action"].value=="Registrar":
				
				p["model"]["informaciones"].crearInformacion(data["titulo"].value,data["contenido"].value)
				
		elif data["action"].value=="Guardar":
			
			if p["model"]["informaciones"].modificarInformacion(indice,data["titulo"].value,data["contenido"].value):
				redirecter("",settings.app,"index",admin=True,args="Informaciones",action="listar")()
