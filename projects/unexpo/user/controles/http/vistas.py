#Get subcontroller

try:
    
  
  data["hidden"]=[]
  data["style"]={}
  data["css"]={}



  if p["control"]=="admin"  and "vista" in p: 

   
    """
    Cuando el admin esta activado.
    """
    
    if errores==[]:



      if  data["login"]==True:




       
       
       
       if p["vista"]=="pagNoticias":
        #modelo=model(p["base_root"]+"../admin/"+settings.model_folder+settings.dbs[0],p["base_root"]+"../admin/"+settings.resquest_folder,data["token"],debug=False,ext=".py")

        #data["zform"]=zform(data["model"]["main"].db("noticias"),"pagNoticias",display="block-justify")
        pass
       elif p["vista"]=="registrar":
        #modelo=model(p["base_root"]+"../admin/"+settings.model_folder+settings.dbs[0],p["base_root"]+"../admin/"+settings.resquest_folder,data["token"],debug=False,ext=".py")
        #data["zform"]=zform(data["model"]["main"].db("users"),"sing_up",display="block-justify",ignorar=["ip","token","login"],confirmar=["password"],valores={"token":None,"ip":None})
        pass
       elif p["vista"]=="logs" and "args" in p:
        error=data["model"]["main"].buscarError(p["args"]["ticket"])
        print error



       elif p["vista"]=="index2":
        """
        cookie=""
        if "HTTP_COOKIE" in os.environ:
         cookie=os.environ["HTTP_COOKIE"]

        ip=""
        if "REMOTE_ADDR" in os.environ:
         ip=os.environ["REMOTE_ADDR"]
        cookies=cookie.split(" ")
        token=""
        for elem in cookies:
         if "token=" in elem:
          token=elem.replace("token=","")
        #modelo=model(p["base_root"]+"../admin/"+settings.model_folder+settings.dbs[0],p["base_root"]+"../admin/"+settings.resquest_folder,data["token"],debug=False,ext=".py")

        respuesta=data["model"]["main"].consultarLogin(token,os.environ["REMOTE_ADDR"])
        if respuesta==True:
         #print "El usuario esta logueado"
         pass
        elif respuesta==False:
         #print "El usuario no esta logueado"
         pass
        else:
         #print "El token no es valido porfavor vuelvase a loguear"
         pass
        """
       elif p["vista"]=="licencias":
        data["licencias"]=os.listdir(config.base_root+"static/licencias")


       elif p["vista"]=="index":    



        data["opciones"]={"main":data["model"]["main"].obtenerFilas("Opciones"),
                         "archivos":data["model"]["archivos"].obtenerFilas("Opciones"),
                         "usuarios":data["model"]["usuarios"].obtenerFilas("Opciones"),
                         "formularios":data["model"]["formularios"].obtenerFilas("Opciones")
                        }


        
        i=0
        data["actionbase"]="app="+settings.app+"&vista="
        
        if p["control"]=="admin":
         
         data["user"]=data["model"]["usuarios"].getUser(p["token"])
         data["adminMenu"]=data["model"]["main"].obtenerAdminMenu()
         data["archivos"]=data["model"]["archivos"].obtenerFilas("Archivos")
         data["actionbase"]="app="+settings.app+"&vista=index&admin=True"
         #["action",["lista de widgets"]]
         data["hook1"]=[ 
             ["listar",["list"]], 
             ["content",["content"]],
             ["editar",["edit"]],
             ["editar2",["edit2"]],
             ["editar3",["edit3"]],
             ["codear",["edit2"]],
             ["plugins",["plugins"]],
             ["plugin",["plugin"]],
             ["post",["post"]],
             ["update",["update"]],
             ["allapps",["allapps"]],
             ["download",["download"]],
              ]

         
         servir("index",data)




       elif p["vista"]=="login":
         

         data["actionbase"]="app="+settings.app+"&vista=login&admin=True"
         if settings.seo_url==False:
           #redirecter("",settings.app,"index",admin=True)()
          pass
         else:
          #redirecter(settings.app+"/admin/index")()
          pass
         #data["hook1"]=[ ["sing_in",["list"]]]

       elif p["vista"]=="logs":
        if "args" in p: 
         data["errores"]=data["model"]["main"].buscarError(p["args"]["ticket"])[1].replace("\n","<br>")
        #redirecter("",settings.app,"index",admin=True)()

      elif p["vista"]!="login" and data["login"]!=True:
       servir("login",data)

       """
       Cuando el usuario no se a logeado y esta en el admin se redirecciona al login.
       """
       
       #redirecter(config.base_url,data["app"],"index",control="admin",action="login",seo_url=config.seo_url)()


      else:

        if  data["login"]==True:

         if p["vista"]=="logs":

          if "args" in p:
           ticket=data["model"]["main"].buscarError(p["args"]["ticket"])
           if ticket!=None:
            data["errores"]=ticket[1].replace("\n","<br>")
           else:
            data["errores"]="Ticket no encontrado"
         else:
          p["vista"]="logs"
          

          reporte=data["model"]["main"].reportarError(errores)

          
          data["errores"]=reporte[0]
          if data["errores"]:

           data["errores_link"]="app="+settings.app+"&admin=True&args={'ticket':'"+reporte[1]+"'}&vista=logs"
          else:
           print "No se a podido crear el ticket"
          #redirecter("",data["app"],"logs")()
          

        else:
         if p["vista"]!="login":


          #redirecter("",data["app"],"login",admin=True,args={"Login":True})()
          pass
         
  else:

    """
    Cuando el admin esta desactivado.
    """



    if errores==[]:



      if p["vista"]=="index":

       data["opciones"]={"archivos":data["model"]["archivos"].obtenerFilas("Opciones") ,}
       if "post" not in p:
        post=0
       else:
        post=p["post"]
       def _min(foto):
        return foto[:foto.find(".")]+"_540x540"+foto[foto.find("."):]
       data["min"]=_min

       data["page"]=data["model"]["paginas"].obtenerFilas("Paginas")[post][1]

       #data["pagina"]=data["model"]["main"].obtenerFilas("Paginas")[i][1]
       #data["entradas"]=data["model"]["main"].obtenerFilas("Entradas")
       data["actionbase"]="app="+settings.app+"&vista="
      elif (p["vista"]==None and  p["control"]=="index") or  p["control"]==None:
        
        #data["menus"]=modelo.obtenerMenus()
        #data["menu"]=modelo.obtenerMenus()[0]
        
        data["opciones"]={"main":data["model"]["main"].obtenerFilas("Opciones"),
                       "archivos":data["model"]["archivos"].obtenerFilas("Opciones"),
                      }
        
        def _min(foto):
          return foto[:foto.find(".")]+"_min"+foto[foto.find("."):]
        data["min"]=_min
        data["Info"]=p["model"]["informaciones"].obtenerFilas("Informaciones")
        if "post" not in p:
          post=0
        else:
          post=p["post"]

        data["page"]=data["model"]["paginas"].obtenerFilas("Paginas")[post][1]

        data["parrafer"]=zred.parrafer
        i=0
        #data["pagina"]=modelo.obtenerFilas("Paginas")[i][1]
        #data["entradas"]=modelo.obtenerFilas("Entradas")
        data["actionbase"]="app="+settings.app+"&vista="

        
        servir("index",data)
      elif p["vista"]==None   and p["control"]=="formulario":
        data["opciones"]={"main":data["model"]["main"].obtenerFilas("Opciones"),
                         "archivos":data["model"]["archivos"].obtenerFilas("Opciones"),
                         "usuarios":data["model"]["usuarios"].obtenerFilas("Opciones"),
                         "formularios":data["model"]["formularios"].obtenerFilas("Opciones")
                        }
        data["page"]=data["model"]["paginas"].obtenerFilas("Paginas")[0][1]
        data["boxes"]=[data["model"]["formularios"].obtenerFilas("Formularios")[0][1]]
        servir("formulario",data) 
      elif p["vista"]==None   and p["control"]=="galeria":
        data["opciones"]=p["model"]["main"].obtenerFilas("Opciones")
        data["galeria"]=p["model"]["galerias"].obtenerFilas("Galerias")
        servir("galeria",data)
      elif p["vista"]==None   and p["control"]=="chat":
        data["opciones"]=p["model"]["main"].obtenerFilas("Opciones")
        
        servir("chat",data)
      elif p["vista"]=="noticias":
       
       data["opciones"]=data["model"]["main"].obtenerFilas("Opciones") 
       i=0
       data["pagina"]=data["model"]["paginas"].obtenerFilas("Paginas")[i][1]

       data["entradas"]=data["model"]["entradas"].obtenerFilas("Entradas")

      elif p["vista"]=="formulario":
       data["opciones"]=data["model"]["main"].obtenerFilas("Opciones")     
       data["boxes"]=[data["model"]["formularios"].obtenerFilas("Formularios")[0][1]]
       data["action"]="Post de Formulario_0"
       if "post" not in p:
        post=0
       else:
        post=int(p["post"])

       data["page"]=data["model"]["formularios"].obtenerFilas("Formularios")


      elif p["vista"]=="galeria":
       
       data["opciones"]=data["model"]["main"].obtenerFilas("Opciones")
       data["galeria"]=data["model"]["galerias"].obtenerFilas("Galerias")
       
      elif p["vista"]=="logs":
       
       #redirecter("",settings.app,"index")()
       pass

      else:

        l1=[]
        if "args" not in data:
          data["args"]={"Login":True}


        data["titulo"]=data["model"]["usuarios"].obtenerFilas("Usuarios")[0][0]
        #data["model"]["main"].obtenerFilas("Paginas")[i][1]
        for box in data["model"]["usuarios"].obtenerFilas("Usuarios")[0][1]:
          l=[]
          for campos in box:
            if type(campos)==dict:
              campos["value"]=""
              l.append(campos)
          if l!=[]:
            l1.append(l)
        data["boxes"]=l1


        if  data["login"]==True:

          """
          Cuando el usuario esta logeado pero en el modo de usuario.


          Nota: eso le permitira hacer operaciones que se registren en la base 
          de datos que no nos necesariamentes las del dashboard, como por ejemplo
          comentar, comprar, etc

          """

        else:

          if p["vista"]!="logs":
           #redirecter("",settings.app,"logs")()
           pass

          else:

           if "args" not in p:

            
            reporte=data["model"]["main"].reportarError(errores)
            
            data["errores"]=reporte[0]
            if data["errores"]:

             data["errores_link"]="app="+settings.app+"&admin=True&args={'ticket':'"+reporte[1]+"'}&vista=logs"
            else:
             print "No se a podido crear el ticket"
            












except Exception, e:
 print "error en el subcontrolador vistas:<br>"
 print e






