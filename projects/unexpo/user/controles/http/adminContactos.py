#POST subcontroller
if  p["app"]==settings.app:
	if beforeAction=="Contacto":
		if data["action"].value=="Registrar":
				try:
					if p["model"]["contactos"].crearContacto(data["email"].value,data["contenido"].value):
						password=""
						email=""
						"""
						zu.sendEmail(email,email,password,
							"El sr(a). "+data["nombre"].value+" le pregunta:\n"+mensaje+"\n su email es: "+data["email"].value)
						"""
						pass
				except:
					print "No se envio la consulta"
		"""
		elif data["action"].value=="Guardar":
			imagenes=[]
			for elem in data["img1"]:
				imagenes.append(elem.value)
			modelo.modificarGaleria(indice,data["galeria"].value,imagenes)
		"""
