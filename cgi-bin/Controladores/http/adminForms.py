#POST subcontroller"

if  p["app"]==settings.app and  p["multipart/form-data"]==True:
	HEADERS.show()

	if beforeAction=="Formulario":

		if data["action"].value=="Enviar":
			p["model"]["formularios"].modificarFormulario(data)
			redirecter(config,settings.app,"admin","index","Paginas",action="listar")()
		elif data["action"].value=="Registrar":

			p["model"]["formularios"].crearFormulario(data)
	elif "Post-de-Formulario" in beforeAction:

		if "Post-de-Formulario:" in data["action"].value:	
			#al parecer recaptcha tiene algunos problemas 
			p["model"]["formularios"].registrarFormulario(data)
			redirecter(config,settings.app,None)()

	elif p["cookies"]["beforeControl"]==None and p["cookies"]["beforeVista"]==None:
		
		if "Post-de-Formulario:" in data["action"].value:
			

			p["model"]["formularios"].registrarFormulario(data)
			redirecter(config,settings.app,"index")()
	elif "Post de Formulario_" in beforeAction:
		p["model"]["formularios"].registrarFormulario(data)
		redirecter(config,settings.app,"index")()
