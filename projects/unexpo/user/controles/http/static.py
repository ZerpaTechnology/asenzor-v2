#print "Content-type: text/html\n\n"
if "action" in p and p["action"]=="static":
	if "vista" not in p:

		if p["i"]=="icon_perfil":
			if p["t"]=="avatar":
				image={"icon_perfil":"icono_perfil.jpg"}	
				#f=file(,"rb")
				if "jpg"==image[p["i"]].split(".")[-1]:
					print "Content-type: image/jpg\n"
					print file(config.base_root+"apps/"+"JDYM"+"/user/static/imgs/"+p["t"]+"/"+image[p["i"]], "rb").read()