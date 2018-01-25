#POST subcontroller
if  p["app"]==settings.app:
	if p["multipart/form-data"]==True:
		
		if data["action"].value=="Registrar" and beforeAction=="Archivo":
			
			resultado=p["model"]["archivos"].subirArchivo(data)
			if resultado:
				redirecter(config,settings.app,"admin","index","Archivos",action="listar")()
				pass
			elif resultado==False:
				
				print "Ya existe un archivo con el mismo nombre,  por favor utilice otro nombre,<br>"," regresando en 3 segundos..."
				print "<script>setTimeout(function(){history.back()},3000)</script>"
			else:
				
				
				print "No incluiste el archivo a subir,<br>"," regresando en  3 segundos..."
				print "<script>setTimeout(function(){history.back()},3000)</script>"