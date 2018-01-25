if rest["manager"]==True:
	if rest["app"]=="static":
	
		if rest["control"]=="plugin":

			for elem in rest["model"]["global"].obtenerFilas('Gestor-plugins'):
   
				if elem[0]==rest["vista"] and len(rest["args"])>0 and rest["args"][0]=="screen":

					print "Content-type: image/png"+"\n"
					print file(config.base_root+config.projects_folder+rest["vista"]+"/screenshot.png", "rb").read()	
		
		
	elif rest["app"]!=None:
		if rest["control"]=="static" and rest["vista"]=="screen":
			print "Content-type: image/png"+"\n"
			print file(config.base_root+config.projects_folder+rest["app"]+"/screenshot.png", "rb").read()	