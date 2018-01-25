
if  p["app"]==settings.app and  p["multipart/form-data"]==False and "action" in p:
	HEADERS.show()
	if p["action"]=="menus":

		menus=p["model"]["main"].obtenerFilas("Menus")
		l=[]
		for elem in menus:
			l.append(elem[1])
		print l
	elif p["action"]=="save-menu":
		p["model"]["main"].guardarMenu(data["menu"].value,data["nombre"].value,p["nuevo"])
		print "menu guardado"

		
		
