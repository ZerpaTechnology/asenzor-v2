try:
	if p["app"]==settings.app and p["method"]=="ajax":
		import os
		
		if p["action"]=="download":
			from ztec import zupdate
			
			completo=False
			#def verificar()
			size=None
			sizefile=p["model"]["global"].obtenerContenido("0ByJYMxvQwmxFNkpRa19hU3RZWWc","Asenzor")["0ByJYMxvQwmxFNkpRa19hU3RZWWc"]["size"]["value"]
			if len(normalizar(p["args"]))==2:
				if normalizar(p["args"])[1]+".zip" in os.listdir("../"+config.update_folder):
					(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat("../"+config.update_folder+normalizar(p["args"])[1]+".zip")
					if (size!=None or size<sizefile):
						dom=zupdate.descargarVersion(config,normalizar(p["args"])[1])
				else:
					dom=zupdate.descargarVersion(config,normalizar(p["args"])[1])
				
				HEADERS.show()

				print "|","Descarga en curso..."
			elif len(normalizar(p["args"]))==1:
				if normalizar(p["args"])[0]+".zip" in os.listdir("../"+config.update_folder):
					(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat("../"+config.update_folder+normalizar(p["args"])[0]+".zip")
					if (size!=None or size<sizefile):
						dom=zupdate.descargarVersion(config,normalizar(p["args"])[0])
				else:
					dom=zupdate.descargarVersion(config,normalizar(p["args"])[0])
				HEADERS.show()
				print "|","Descarga en curso..."

	
		elif p["action"]=="check":	

			HEADERS.show()




			sizefile=1
			size=None
			sizefile=p["model"]["global"].obtenerContenido("0ByJYMxvQwmxFNkpRa19hU3RZWWc","Asenzor")["0ByJYMxvQwmxFNkpRa19hU3RZWWc"]["size"]["value"]



			if normalizar(p["args"])[0]+".zip" in os.listdir("../"+config.update_folder):
				(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat("../"+config.update_folder+normalizar(p["args"])[0]+".zip")

				if  size>=sizefile:
					print "@"+"Descarga exitosa. Presiona <a href='"+zred.urlBuilder(config,p["app"],"admin","index","Actualizar",normalizar(p["args"])[0],action="install")+"'>aquí</a> para instalar la nueva version"
				else:
					print "#","Descargando...",(size*100)/sizefile,"%"
			else:
				print "$","Su descarga iniciara en breve"
				

except Exception,e:	
	HEADERS.show()
	print p["action"]
	print e.args