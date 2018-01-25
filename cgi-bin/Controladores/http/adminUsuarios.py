
if p["multipart/form-data"]==True:
 
 import Cookie
 







 
 

 cookie=Cookie.SimpleCookie()
 import os




 
 if data["action"].value=="Login":
  


  if  p["app"]==settings.app:
   
   if p["model"]["global"].isUser(data["email"].value):
    

    
    token=p["model"]["global"].login(data["email"].value,data["password"].value)


    p["isGlobalUser"]=True


    
   elif p["model"]["usuarios"].isUser(data["email"].value):

    
    token=p["model"]['usuarios'].login(data["email"].value,data["password"].value)
    p["isGlobalUser"]=False
   
   
   if token!=False:

    #pendiente que de momento trabajamos solo con la cookie token
    cookies=getCookie()
    


    if "token" in cookies:
      tokens=normalizar(cookies["token"])
    else:
      tokens={}      
    if "token2" in cookies:
      token2=normalizar(cookies["token2"])
    else:
      token2="None"

    folder=os.getcwd().split("/")[-2]

    if p["isGlobalUser"]:

      cookie["token2"]=token

      cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
    else:
      
      tokens[settings.app]=token
      cookie["token"]=tokens
      cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
    
    #print "token="+str(tokens)[1:-1].replace("'","").replace('"',"").replace(" ","")
    #print modelo.consultarLogin2(token)
    
    
    
    #nota la las cabeceras de se escriben antes de la cabera content-type
    
    print cookie

    HEADERS.show()


    contenttype=True
    redirecter(config,p["app"],"admin","index")()


   else:
    HEADERS.show()
    contenttype=True
    print "Datos incorrectos"
   
 elif data["action"].value=="Salir" :
  if  p["app"]==settings.app:
   
   
   

   if "token" in p:
     folder=os.getcwd().split("/")[-2]   


     
     if ((p["isGlobalUser"]==False and p["model"]["usuarios"].closeSession(p["token"])) or (p["isGlobalUser"]==True and p["model"]["global"].closeSession(p["token"]))):        


        folder=os.getcwd().split("/")[-2]
        cookies=getCookie()
        if p["isGlobalUser"]==False:
          cookie["token"]=cookies["token"]
          cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
          cookie["token"]["expires"]="Thu, 01 Jan 1970 00:00:01 GMT"
        else:
          cookie["token2"]=cookies["token2"]
          cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
          cookie["token2"]["expires"]="Thu, 01 Jan 1970 00:00:01 GMT"


        
        

        print cookie
        HEADERS.show()
        contenttype=True
        redirecter(config,p["app"],"admin","index")()
     else:

      print "No se a podido cerrar la sesion"
   else:
      HEADERS.show()
      redirecter(config,p["app"],"admin","index")()

 elif data["action"].value=="Registrar" and normalizar(p["cookies"]["beforeArgs"])[0]=="Usuario":
  
  if  p["app"]==settings.app:

   try:
    
    
    


    p["model"]["usuarios" if p["isGlobalUser"]==False else "global"].registrarUsuario(data["usuario"].value,data["email"].value,data["password"].value,p["opciones"]["archivos"][1][1].index(data["avatar"].value),p["opciones"]["usuarios" if p["isGlobalUser"]==False else "global"][0][1].index(data["permisologia"].value))
    

    token=p["model"]["usuarios" if p["isGlobalUser"]==False else "global"].login(data["email"].value,data["password"].value)
    
    #pendiente que de momento trabajamos solo con la cookie token
    
    cookies=getCookie()
    folder=os.getcwd().split("/")[-2]


    if p["isGlobalUser"]==False:

      if "token" in cookies:
        tokens=normalizar(cookies["token"])

      else:
        tokens={}    


      tokens[settings.app]=token
      cookie["token"]=tokens



      






      cookie["token"]["path"]="/"+(folder if folder!=config.host_folder else "")
    else:

      
      cookie["token2"]["path"]="/"+(folder if folder!=config.host_folder else "")
    #print "token="+str(tokens)[1:-1].replace("'","").replace('"',"").replace(" ","")
    
    print cookie

    HEADERS.show()
    contenttype=True
    
    redirecter(config,p["app"],"admin","index")()
   except Exception,e :
    print str(e)[1:-1]

 elif data["action"].value=="Guardar" and len(normalizar(p["cookies"]["beforeArgs"]))>0 and  normalizar(p["cookies"]["beforeArgs"])[0]=="Usuario":
  if  p["app"]==settings.app:
   
   #print modelo.obtenerFilas("Opciones")[1][1].index(data["avatar"].value)
   HEADERS.show()
   if p["model"]["global"].isUser(p["user"]["email"]):
    p["model"]["usuarios"].modificarUsuario(indice,data["usuario"].value,data["email"].value,data["password"].value, p["opciones"]["archivos"][1][1].index(data["avatar"].value),p["opciones"]["usuarios" if p["isGlobalUser"]==False else "global"][0][1].index(data["permisologia"].value))
   
   redirecter(config,p["app"],"admin","index","Usuarios",action="listar")()

