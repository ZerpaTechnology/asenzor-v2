try:
	
	if  p["app"]==settings.app:
		HEADERS.show()
		

		if p["multipart/form-data"]==True and p["method"]=="post":
			if data["action"].value=="upload":
				import os
				HEADERS.show()
				
				if data["nombre"].value not in  os.listdir(config.base_root+(config.apps_folder if data["upload"].value=="webapp" else config.plugins_folder)):
					f=open(config.base_root+(config.apps_folder if data["upload"].value=="webapp" else config.plugins_folder)+data["nombre"].value,"w")
					f.write(data["file"].value)
					f.close()
					
					print True
				else:
					
					print False
		elif p["multipart/form-data"]==False and p["method"]=="ajax":
			
			if p["action"]=="install":
				import zipfile
				HEADERS.show()
				
				zf=zipfile.ZipFile( config.base_root+(config.apps_folder if p["upload"]=="webapp" else config.plugins_folder) +p["nombre"], "r")
				import os
				carpetas=[]
				for m in zf.infolist():
					data = zf.read(m) # extract zipped data into memory
					# convert unicode file path to utf8
					disk_file_name = m.filename.encode('utf8')
					dir_name = os.path.dirname(config.base_root+(config.apps_folder if p["upload"]=="webapp" else config.plugins_folder)+disk_file_name)
					try:
						if dir_name[len(config.base_root+(config.apps_folder if p["upload"]=="webapp" else config.plugins_folder)):].split("/")[0] not in carpetas:
							carpetas.append(dir_name[len(config.base_root+(config.apps_folder if p["upload"]=="webapp" else config.plugins_folder)):].split("/")[0])
						os.makedirs(dir_name)
					except OSError as e:
						if e.errno == os.errno.EEXIST:
							pass
						else:
							raise
					try:
						with open(config.base_root+(config.apps_folder if p["upload"]=="webapp" else config.plugins_folder)+disk_file_name, 'wb') as fd:
							fd.write(data)
					except Exception as e:
						pass
				zf.close()
				os.remove(config.base_root+(config.apps_folder if p["upload"]=="webapp" else config.plugins_folder)+p["nombre"])
				if p["upload"]=="webapp":
					print p["model"]["global"].instalarApp(p["nombre"].replace(".zip",""))
				else:

					print p["model"]["global"].instalarPlugin(p["nombre"].replace(".zip",""))
			elif p["action"]=="activar":
				if p["upload"]=="webapp":
					print p["model"]["main"].activarApp(p["nombre"])
				else:
					print p["model"]["main"].activarPlugin(p["nombre"])
			






except Exception,e:
	print "Content-type: text/html\n"
	print e