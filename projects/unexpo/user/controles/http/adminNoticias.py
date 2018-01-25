#POST subcontroller
if data["action"].value=="Guardar" and beforeAction=="Entrada":
	if  p["app"]==settings.app:
		
		try:
                   img=int(data["wnoticias_img"].value)
                except:
                   img=0
                try:
                   titulo=data["wnoticias_titulo"].value
                except:
                   titulo=""
                try:
                   noticia=int(data["wnoticias_img"].value)
                except:
                   noticia=""

		p["model"]["noticias"].modificarEntrada(indice,img,titulo,noticia)
		redirecter("",settings.app,"admin","index")()
if data["action"].value=="Registrar" and beforeAction=="Entrada":
	if  p["app"]==settings.app:
		try:
			titulo=data["wnoticias_titulo"].value
		except:
			titulo=""
		try:
			noticia=data["wnoticias"].value
		except:
			noticia=""
		p["model"]["noticias"].crearEntrada(int(data["wnoticias_img"].value),titulo,noticia)
		redirecter("",settings.app,"admin","index","Entradas",action="listar")()