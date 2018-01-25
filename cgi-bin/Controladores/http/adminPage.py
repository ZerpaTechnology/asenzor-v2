#POST subcontroller
if p["multipart/form-data"]==True:
	if  p["app"]==settings.app and normalizar(p["cookies"]["beforeArgs"])!=[] and  normalizar(p["cookies"]["beforeArgs"])[0]=="Pagina":

		if data["action"].value=="Guardar":
			HEADERS.show()			
			
			p["model"]["paginas"].modificarPagina(indice,data)

			redirecter(config,settings.app,"admin","index","Paginas",action="listar")()

		elif data["action"].value=="Registrar":
			HEADERS.show()
			p["model"]["paginas"].crearPagina(data)
			redirecter(config,settings.app,"admin","index","Paginas",action="listar")()