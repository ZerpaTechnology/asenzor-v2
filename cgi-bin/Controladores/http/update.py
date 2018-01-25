try:
	
	if p["app"]==settings.app and len(p["args"])>0:


		

		if p["control"]=="admin" and p["login"]==True and p["args"][0]=="Actualizar":
			from ztec import zupdate
			


			if len(p["args"])>1 and p["action"]=="download" and p["args"][1]=="last":				
				try:

					dom=zupdate.descargarVersion(config,p["args"][1])
					data["status"]="Descarga exitosa. Presiona <a href='"+zred.urlBuilder(config,p["app"],"admin","index","Actualizar",p["args"][1],action="install")+"'>aquí</a> para instalar la nueva version"
				except Exception,e:
					
					data["status"]="No se ha podido descargar la version "+p["args"][1]+"<br>"+str(e)[1:-1]+"<br>"+str(dom)

			elif p["action"]=="download" and p["args"][1]!="last":
				"""
				try:

					print "Content-type: text/html\n"
					print "HTTP/1.1 200 OK"
					print "Status: 200 OK"
					
					print "Content-Disposition: attachment; filename='"+p["args"][1]+".zip'"
					print "Content-Type:application/octet-stream"
					
					print "Content-Type: application/force-download"
					
					dom=zupdate.descargarVersion(config,p["args"][1])
					data["status"]="Descarga exitosa. Presiona <a href='"+zred.urlBuilder(config,p["app"],"admin","index","Actualizar",p["args"][1],action="install")+"'>aquí</a> para instalar la nueva version"
					
					
				except Exception,e:
					
					data["status"]="No se a podido descargar la version "+p["args"][1]+"<br>"+str(e)[1:-1]+"<br>"+str(dom)
				"""
			elif p["action"]=="install" and p["args"][1]!="last" and p["method"]=="get":

				try:
					
					#dom=zupdate.actualizar(config,settings,p["args"][1])

					data["status"]="Actualización completada. version "+p["args"][1]
				except Exception,e:
					
					data["status"]="No se a podido instalar la version "+p["args"][1]+"<br>"+str(e)[1:-1]+"<br>"+str(dom)


			elif p["action"]=="install" and p["args"][1]=="last" and p["method"]=="get":
				try:

					#dom=zupdate.actualizar(config,settings,p["args"][1])
					data["status"]="Actualización completada. version "+p["args"][1]
				except Exception,e:
					
					data["status"]="No se a podido instalar la version "+p["args"][1]+"<br>"+str(e)[1:-1]+"<br>"+str(dom)
		
except Exception,e:
	print "Content-type: text/html\n"
	print e