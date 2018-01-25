try:
	if len(p["args"])>0:


		if p["control"]=="admin" and p["login"]==True and p["args"][0]=="Actualizar":
			from ztec import zupdate

			if len(p["args"])>1 and p["action"]=="download" and p["args"][1]=="last":				
				try:
					zupdate.descargarVersion(config,p["args"][1])
					data["status"]="Descarga exitosa. Presiona <a href='"+config.base_url+p["app"]+"/"+"/".join(p["args"])+"/action=install'>aquí</a> para instalar la nueva version"
				except:
					data["status"]="No se ha podido descargar la version "+p["args"][1]

			elif p["action"]=="download" and p["args"][1]!="last":
				try:
					zupdate.descargarVersion(config,p["args"][1])
					data["status"]="Descarga exitosa. Presiona <a href='"+config.base_url+p["app"]+"/"+"/".join(p["args"])+"/action=install'>aquí</a> para instalar la nueva version"
				except:
					data["status"]="No se a podido descargar la version "+p["args"][1]
			
			elif p["action"]=="install" and p["args"][1]!="last":
				try:

					zupdate.actualizar(config,settings,p["args"][1])
					data["status"]="Actualización completada. version "+p["args"][1]
				except:

					data["status"]="No se a podido instalar la version "+p["args"][1]


			elif p["action"]=="install" and p["args"][1]=="last":
				try:
					zupdate.actualizar(config,settings,p["args"][1])
					data["status"]="Actualización completada. version "+p["args"][1]
				except Exception,e:
					print e
					data["status"]="No se a podido instalar la version "+p["args"][1]
		
except Exception,e:
	print e