#POST subcontroller
if p["multipart/form-data"]==True:
	if  p["app"]==settings.app and normalizar(p["cookies"]["beforeArgs"])!=[] and  normalizar(p["cookies"]["beforeArgs"])[0]=="Pagina":

		if data["action"].value=="Guardar":
			print "Content-type: text/html\n"
		
			"""
			try:
				d1=int(data["logo"].value)
			except Exception, e:
				print str(e)[1:-1]," d1"
				d1=""
			try:
				d2=int(data["fondo1"].value)
			except Exception, e:
				print str(e)[1:-1]," d2"
				d2=0
			try:
				d3=data["video1"].value
			except Exception, e:
				print str(e)[1:-1]," d3"
				d3=""
			try:
				d4=int(data["iconfacebook"].value)
			except Exception, e:
				print str(e)[1:-1]," d4"
				d4=""
			
			try:
				d5=int(data["icontwitter"].value)
			except Exception, e:
				print str(e)[1:-1]," d5"
				d5=""
			try:
				d6=int(data["iconinstagram"].value)
			except Exception, e:
				print str(e)[1:-1]," d6"
				d6=""
			try:
				d7=int(data["iconyoutube"].value)
			except Exception, e:
				print str(e)[1:-1]," d7"
				d7=""
			try:
				d8=int(data["fondo2"].value)
			except Exception, e:
				print str(e)[1:-1]," d8"
				d8=0
			try:
				d9=data["titulo"].value
			except Exception, e:
				print str(e)[1:-1]," d9"
				d9=""
			try:
				d10=data["subtitulo"].value
			except Exception, e:
				print str(e)[1:-1]," d10"
				d10=""
			try:
				d11=data["texto1"].value
			except Exception, e:
				print str(e)[1:-1]," d11"
				d11=""
			try:
				d12=int(data["fondo3"].value)
			except Exception, e:
				print str(e)[1:-1]," d12"
				d12=0
			try:
				d13=int(data["imgartista1"].value)
			except Exception, e:
				print str(e)[1:-1]," d13"
				d13=0
			try:
				d14=int(data["imgartista2"].value)
			except Exception, e:
				print str(e)[1:-1]," d14"
				d14=0
			try:
				d15=data["btndescargar_titulo"].value
			except Exception, e:
				print str(e)[1:-1]," d15"
				d15=""
			try:
				d16=data["btndescargar"].value
			except Exception, e:
				print str(e)[1:-1]," d16"
				d16=""
			try:
				d17=int(data["fondo4"].value)
			except Exception, e:
				print str(e)[1:-1]," d17"
				d17=0
			try:
				d27=data["wyoutube"].value
			except Exception, e:
				print str(e)[1:-1]," d27"
				d27=""
			try:
				d18=data["wtwitter"].value
			except Exception, e:
				print str(e)[1:-1]," d18"
				d18=""
			try:
				d19=data["winstagram"].value
			except Exception, e:
				print str(e)[1:-1]," d19"
				d19=""
			try:
				d20=int(data["fondo5"].value)
			except Exception, e:
				print str(e)[1:-1]," d20"
				d20=0	
			try:
				d21=data["wfacebook"].value
			except Exception, e:
				print str(e)[1:-1]," d21"
				d21=""
			try:
				d22=int(data["fondo6"].value)
			except Exception, e:
				print str(e)[1:-1]," d22"
				d22=0
			try:
				
				d23=int(data["fondo7"].value)
			except Exception, e:
				
				print str(e)[1:-1]," d23"
				d23=0
			try:
				
				d24=int(data["fondo8"].value)
			except Exception, e:
				
				print str(e)[1:-1]," d24"
				d24=0
			try:
				
				d25=data["video_titulo"].value
			except Exception, e:
				
				print str(e)[1:-1]," d25"
				d25=""
			try:
				
				d26=data["aviso"].value
			except Exception, e:
				
				print str(e)[1:-1]," d26"
				d26=""
			try:
				
				d26=data["aviso"].value
			except Exception, e:
				
				print str(e)[1:-1]," d26"
				d26=""
			
			"""

			p["model"]["paginas"].modificarPagina(indice,data)
			redirecter(config,settings.app,"admin","index","Paginas",action="listar")()
		elif data["action"].value=="Registrar":
			print "Content-type: text/html\n"
			p["model"]["paginas"].crearPagina(data)
			redirecter(config,settings.app,"admin","index","Paginas",action="listar")()