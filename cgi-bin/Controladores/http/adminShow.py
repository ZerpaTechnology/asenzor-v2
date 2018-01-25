
if "action" in p and p["action"]=="show": #and "args" in p:
 #print "esto se a enviado ",p
 """
 estructura del los controladores
 #condicional de action
 HEADERS()#la funcion header imprime las cabeceras si estas han sido impresas anteriormente
 

 """
 

 
 if ("admin" in p and p["admin"]==True or p["control"]=="admin") and "login" in p and p["login"]==True:
  
  if p["method"]=="ajax": 
   HEADERS.show()

   

   if "kwargs" in p:

    
    if "db" in normalizar(p["kwargs"]):

     
     if "id" in normalizar(p["kwargs"]) and normalizar(p["kwargs"])["id"]!=None:
      tabla=None

      for elem in list(p["model"]["main"].db.tablas):



        if len(p["model"]["main"].db.tablas[elem])>0:

          temp=p["model"]["main"].db(elem).obtenerFilaValores(0)
          if len(temp)>2:
            if normalizar(p["kwargs"])["tabla"]==list(temp[2])[0]:
              tabla=elem
      if tabla!=None:

        print p["model"][normalizar(p["kwargs"])["db"]].obtenerFilas(tabla)[normalizar(p["kwargs"])["id"]]

     else:


      if normalizar(p["kwargs"])["tabla"] in list(p["model"]["main"].db.tablas):


        for elem in list(p["model"]["main"].db.tablas):


          if len(p["model"]["main"].db.tablas[elem])>0:

            temp=p["model"]["main"].db(elem).obtenerFilaValores(0)

            if len(temp)>2:
              
              if normalizar(p["kwargs"])["tabla"]==list(temp[2])[0]:

                tabla=elem
        print p["model"][normalizar(p["kwargs"])["db"]].obtenerFilas(normalizar(p["kwargs"])["tabla"])
      else:
        print p["model"][normalizar(p["kwargs"])["db"]].obtenerFilas(normalizar(p["kwargs"])["tabla"])
    if "path" in p["kwargs"] and (p["user"]["permisologia"]==0 or p["user"]["permisologia"]==1):
     
     if p["kwargs"]["path"][0]=="admin":
      if p["kwargs"]["path"][1]=="Template":

       print config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir
      elif p["kwargs"]["path"][1]=="Widget":

       print config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder
     elif  normalizar(p["kwargs"])["path"][0]=="user":
      if normalizar(p["kwargs"])["path"][1]=="Template":
       print config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir
      elif normalizar(p["kwargs"])["path"][1]=="Widget":
       print config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_folder+routes.widgets_folder
     elif  p["kwargs"]["path"][0]=="Controlador":
      print config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+config.controller_folder
     elif  p["kwargs"]["path"][0]=="Modelo":
      print config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.models_folder


    
    if p["args"]==[123456]:

     
     f=open(p["base_root"]+"../admin/"+settings.model_folder+settings.dbs[1]+"_db.py","r")
     db=f.read()
     f.close()
     print db#.replace(" ","&amps;")


     data["zform"]=zform(modelo.db("Menus"),"editar",display="block-justify")
    

    elif list(normalizar(p["kwargs"]))==["widget"]:
     import os


     if normalizar(p["admin"])==True:

      if p["login"]==True:  

        
        if normalizar(p["kwargs"])["widget"].strip()+".html" in os.listdir(config.base_root+config.apps_dir+"/"+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder if normalizar(p["isglobal"])==False else "../"+config.vistas_folder+"widgets/"):

          f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_folder+routes.widgets_folder+normalizar(p["kwargs"])["widget"].strip()+".html" if normalizar(p["isglobal"])==False else "../"+config.vistas_folder+"widgets/"+normalizar(p["kwargs"])["widget"].strip()+".html","r")
          print f.read()
          f.close()
        else:
          print None
      else:
        print "Necesitas loguearte para acceder al widget"
     else:

      if p["kwargs"]["widget"].strip()+".html" in os.listdir(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_folder+routes.widgets_folder):
        f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_folder+routes.widgets_folder+p["kwargs"]["widget"].strip()+".html","r")
        print f.read()
        f.close()
      else:
        print None
    elif p["kwargs"]=={"Contacto":"jesus26abraham1996@gmail.com"}:
     
     print "data['Contactos']="+str(modelo.obtenerContactos(p["kwargs"]["Contacto"]))

    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="Controlador":

     try:

      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+decode(p["kwargs"]["Controlador"]).strip()+".py","r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+decode(p["kwargs"]["Controlador"]).strip()+".py"
      print f.read()
      f.close()
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="Modelo":

     try:

      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+decode(p["kwargs"]["Modelo"]).strip()+".py","r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+decode(p["kwargs"]["Modelo"]).strip()+".py"
      print f.read()
      f.close()
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="user":
     

     try:
      
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir+"/"+p["kwargs"]["user"].strip()+".html","r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_folder+p["kwargs"]["user"].strip()+".html"
      print f.read()
      f.close()
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="admin":

     try:
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir+"/"+p["kwargs"]["admin"].strip()+".html","r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_folder+p["kwargs"]["admin"].strip()+".html"
      print f.read()
      f.close()
     except:
      pass
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="user-widgets":

     try:
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir+"/"+routes.widgets_folder+"/"+p["kwargs"]["user-widgets"].strip()+".html","r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+routes.vistas_dir+"/"+routes.widgets_folder+"/"+p["kwargs"]["user-widgets"].strip()+".html"
      print f.read()
      f.close()
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="admin-widgets":

     try:
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir+"/"+routes.widgets_folder+p["kwargs"]["admin-widgets"].strip()+".html","r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.vistas_dir+"/"+routes.widgets_folder+p["kwargs"]["admin-widgets"].strip()+".html"
      print f.read()
      f.close()
    
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="user-scripts":

     try:
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+settings.static_dir+"/"+p["kwargs"]["user-scripts"].strip(),"r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+settings.static_dir+"/"+p["kwargs"]["user-scripts"].strip()
      print f.read()
      f.close()
    
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="admin-scripts":

     try:
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+settings.static_dir+"/"+p["kwargs"]["admin-scripts"].strip(),"r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+settings.static_dir+"/"+p["kwargs"]["admin-scripts"].strip()
      print f.read()
      f.close()
    
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="globales-scripts":

     try:
      
      f=open(config.base_root+config.static_folder+p["kwargs"]["globales-scripts"].strip(),"r")
      print "#"+config.base_root+config.static_folder+p["kwargs"]["globales-scripts"].strip()
      print f.read()
      f.close()
    
     except Exception,e:
      print e      
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="ajustes":

     try:
      
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+p["kwargs"]["ajustes"].strip(),"r")
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/admin/"+p["kwargs"]["ajustes"].strip()
      print f.read()
      f.close()
    
     except Exception,e:
      print e
    elif len(list(p["kwargs"]))>0 and list(p["kwargs"])[0]=="Plugin":
     

     try:
      f=open(config.base_root+config.plugins_folder+p["kwargs"]["Plugin"].strip(),"r")
      print "#"+config.base_root+config.plugins_folder+p["kwargs"]["Plugin"].strip()
      print f.read()
      f.close()
    
     except Exception,e:
      print e
    elif list(p["kwargs"])==["Contacto"]:
      contacto=p["model"]["conversaciones"].obtenerContacto(p["kwargs"]["Contacto"])
      print contacto
      pass
    elif p["args"]==["Contactos"]:
      contactos=p["model"]["conversaciones"].obtenerContactos()
      print contactos
      pass
   else:
    pass
  
  else:
   #solo para pruebas
   
   if "kwargs" in p:

    if p["kwargs"].keys()[0]=="user":



     try:
      f=open(config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+config.vistas_dir+"/"+p["kwargs"]["user"].strip()+".html","r")
      HEADERS.show()
      print "#"+config.base_root+(config.apps_dir+"/" if p["manager"]==False else config.projects_folder)+settings.app+"/user/"+config.vistas_dir+"/"+p["kwargs"]["user"].strip()+".html"
      print f.read()
      f.close()
      
     except Exception, e:
      HEADERS.show()
      print str(e)[1:-1]












