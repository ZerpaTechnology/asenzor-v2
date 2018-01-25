
if p["multipart/form-data"]==True:
 
 import Cookie





 
 

 cookie=Cookie.SimpleCookie()
 import os




 
 if data["action"].value=="Login":
  
  if  p["app"]==settings.app:
   

   token=p["model"]["usuarios"].login2(data["email"].value,data["password"].value)




   if token!=False:

    #pendiente que de momento trabajamos solo con la cookie token
    cookies=getCookie()
    if "token" in cookies:
      tokens=normalizar(cookies["token"])
    else:
      tokens={}
    

    
      
    tokens[settings.app]=token

    

    




    #print "token="+str(tokens)[1:-1].replace("'","").replace('"',"").replace(" ","")
    
    folder=os.getcwd().split("/")[-2]

    #print modelo.consultarLogin2(token)
    
    cookie["token"]=tokens
    cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
    #nota la las cabeceras de se escriben antes de la cabera content-type
    
    print cookie




    print "Content-type: text/html\n"



    contenttype=True


    


    redirecter(config,p["app"],"admin","index")()


   else:
    print "Content-type: text/html\n"
    contenttype=True
    print "Datos incorrectos"
   
 elif data["action"].value=="Salir" :
  if  p["app"]==settings.app:
   
   
   if "token" in p:
     folder=os.getcwd().split("/")[-2]   

     if p["model"]["usuarios"].closeSession2(p["token"]):
        folder=os.getcwd().split("/")[-2]
        cookies=getCookie()
        cookie["token"]=cookies["token"]
        cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
        cookie["token"]["expires"]="Thu, 01 Jan 1970 00:00:01 GMT"

        print cookie
        print "Content-type: text/html\n"
        contenttype=True
        redirecter(config,p["app"],"admin","index")()
     else:
      print "No se a podido cerrar la sesion"
   else:
      print "Content-type: text/html\n"
      redirecter(config,p["app"],"admin","index")()

 elif data["action"].value=="Registrar" and normalizar(p["cookies"]["beforeArgs"])[0]=="Usuario":
  
  if  p["app"]==settings.app:

   try:
    
    p["model"]["usuarios"].registrarUsuario2(data["usuario"].value,data["email"].value,data["password"].value,p["model"]["usuarios"].obtenerFilas("Opciones")[1][1].index(data["avatar"].value))
    token=p["model"]["usuarios"].login2(data["email"].value,data["password"].value)
    
    #pendiente que de momento trabajamos solo con la cookie token
    
    cookies=getCookie()
    if "token" in cookies:
      tokens=normalizar(cookies["token"])
    else:
      tokens={}    
    tokens[settings.app]=token
    




    #print "token="+str(tokens)[1:-1].replace("'","").replace('"',"").replace(" ","")
    folder=os.getcwd().split("/")[-2]
    cookie["token"]=tokens
    cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")

    
    print cookie
    print "Content-type: text/html\n"
    contenttype=True
    
    redirecter(config,p["app"],"admin","index")()
   except Exception,e :
    print str(e)[1:-1]

 elif data["action"].value=="Guardar" and len(normalizar(p["cookies"]["beforeArgs"]))>0 and  normalizar(p["cookies"]["beforeArgs"])[0]=="Usuario":
  if  p["app"]==settings.app:
   
   #print modelo.obtenerFilas("Opciones")[1][1].index(data["avatar"].value)
   p["model"]["usuarios"].modificarUsuario2(indice,data["usuario"].value,data["email"].value,data["password"].value,p["model"]["usuarios"].obtenerFilas("Opciones")[1][1].index(data["avatar"].value))
   
   #redirecter("",p["app"],"index",admin=True)()

