#print "Content-type: text/html\n\n"

if p["app"]==settings.app and p["control"]=="static":

	
	
	if p["vista"]=="i" and len(p["args"])>0:
			for elem in p["model"]["archivos"].obtenerFilas("Archivos"):
				if p["model"]["archivos"].contener(elem[1])[0]["tipo"]["value"]=="Imagen" and p["model"]["archivos"].contener(elem[1])[0]["renombre"]["value"]==p["args"][0]:
					 print "Content-type: image/"+p["args"][0].split(".")[-1]+"\n"
					 print file(config.base_root+(config.apps_folder if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.static_folder+"archivos/Imagenes/"+p["args"][0], "rb").read()	
					 break
	elif p["vista"]=="screen":


		print "Content-type: image/png"+"\n"
		
		print file(config.base_root+(config.apps_folder if p["manager"]==False else config.projects_folder)+settings.app+"/screenshot.png", "rb").read()	


		