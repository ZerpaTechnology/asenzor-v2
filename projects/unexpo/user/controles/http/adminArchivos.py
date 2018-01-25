#POST subcontroller
if  p["app"]==settings.app:
	if p["multipart/form-data"]==True:
		if data["action"].value=="Registrar" and beforeAction=="Archivo":
			
			
			if p["model"]["archivos"].subirArchivo(data):
				redirecter("",settings.app,"admin","index","Archivos",action="listar")()
			else:
				print "Ya existe un archivo con el mismo nombre,  por favor utilice otro nombre"
				time.sleep(1)
				print "<scritp>history.back()</script>"