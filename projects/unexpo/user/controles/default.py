#!/usr/bin/python
# -*- coding: utf-8 -*-
#============================================================
#Cabecera del controlador
import sys
import time
import urllib




try:
 def cnt(p,m):#Manejador de las paginas
  p["method"]="get"

  debug=False
  import sys
  

  import config
  import settings.config as settings
  import settings.routes as routes


  import ztec.zu as zu
  from ztec.zu import redict
  import ztec.zred as zred 
  from ztec.zred import zform 
  from ztec.zt import ZT
  import imp
  #print config.base_root+config.apps_folder+settings.app+"/admin/"+routes.models_folder+"traducciones-"+settings.lang.upper()
  
  routes.base_url=config.base_url+(settings.app+"/") if config.default_app!=settings.app else ""


  from ztec.zred import clienteSock,getCookie,setCookie, redirecter,normalizar,decode,Headers
  HEADERS=Headers()
  """
  for elem in settings.libs_python:
   exec("import "+elem,locals())
   pass
  """
  p["AsenZor:Detalles"]={"Versi贸n":0.1,"Autor original":"Jes煤s Abraham Zerpa Maldonado",
          "Email":"jesus26abraham1996@gmail.com","Website":"https://zerpatechnology.com.ve",
          "Actualizaciones":"AsenZor esta en su versi贸n mas reciente"}
  p["AsenZor:chat-box"]={"comentarios":1}

  p["defaultpath"]="../"+config.apps_folder+p["app"]+"/user/"

  #============================================================
  #Cuerpo del controlador
  #------------------------------------------------------------
  #Secci贸n de parametrisaje


  data=p
  data["login"]=False
  beforeAction=""
  contenido=p["model"]["global"].obtenerContenido(p["app"],"apps")[p["app"]]  
  embebe_request=[]
  errores=[]


  data["model"]["global"].p=p
  data["model"]["usuarios"].p=p

  
  try:
   for k,db in enumerate(contenido[1]):
    if contenido[1][db]["value"] in settings.dbs:
      exec("from modelos."+contenido[1][db]["value"]+"_model import model as model"+str(k),locals())    
      pass
      if "token" not in p:
       exec('data["model"][contenido[1][db]["value"]]=model'+str(k)+'(p["base_root"]+"../admin/"+routes.models_folder+contenido[1][db]["value"],p["base_root"]+"../admin/"+routes.request_folder,"user",debug=debug,ext=".py")',locals())
       data["model"][contenido[1][db]["value"]].models["global"]=data["model"]["global"]


       data["model"]["global"].models[contenido[1][db]["value"]]=data["model"][contenido[1][db]["value"]]
       
       if "Opciones" in data["model"][contenido[1][db]["value"]].db.tablas:
            
            data["opciones"][contenido[1][db]["value"]]=data["model"][contenido[1][db]["value"]].obtenerFilas("Opciones")
      else:
       exec('data["model"][contenido[1][db]["value"]]=model'+str(k)+'(p["base_root"]+"../admin/"+routes.models_folder+contenido[1][db]["value"],p["base_root"]+"../admin/"+routes.request_folder,p["token"],debug=debug,ext=".py")',locals())
       data["model"][contenido[1][db]["value"]].models["global"]=data["model"]["global"]


       data["model"]["global"].models[contenido[1][db]["value"]]=data["model"][contenido[1][db]["value"]]
       if "Opciones" in data["model"][contenido[1][db]["value"]].db.tablas:
            data["opciones"][contenido[1][db]["value"]]=data["model"][contenido[1][db]["value"]].obtenerFilas("Opciones")
       
  except Exception as e:

   if settings.mod_debug!=False:
    import traceback
    try:
      exc_type,exc_obj,exc_tb=sys.exc_info()
      fname = exc_tb.tb_frame.f_code.co_filename
      print "#===================================<br>"
      print "#No se pudo crear la base de datos"
      print "# ","".join(traceback.format_exception(exc_type,fname,exc_tb)).replace("%5Cn","<br>")+"<br>"
      print "#", e,"<br>"
      print "#==================================="
      raise

    except:
      pass
  
  
  

  cookies=getCookie()




  token2=None
  tokens={}





  

  if "token" in cookies:


   tokens=normalizar(cookies["token"])
  if "token2" in cookies:
    token2=normalizar(cookies["token2"])
   


   

  
  if settings.app in tokens and token2==None:
    
    p["token"]=tokens[settings.app]
    if p["model"]["usuarios"].isUser(token=tokens[settings.app]) and p["model"]["usuarios"].consultarLogin(tokens[settings.app]):
      p["user"]=p["model"]["usuarios"].getUser(p["token"])
      p["login"]=True
      p["isGlobalUser"]=False
    else:
      p["login"]=False
    
  elif token2!=None and p["model"]["global"].consultarLogin(token2):
    p["token"]=token2
    p["user"]=p["model"]["global"].getUser(p["token"])
    p["login"]=True
    p["isGlobalUser"]=True
  else:
    p["login"]=False
  
  for elem in data["model"]:
   if "token" in p:
    data["model"][elem].token=p["token"]
   else:
    data["model"][elem].token="user"
  data["cookies"]=cookies
  
  if p["login"]==True:
    
    miscookies=getCookie()
    import Cookie
    cookie=Cookie.SimpleCookie()  
    folder=os.getcwd().split("/")[-2]
    if "notification" not in miscookies:

          cookie["notification"]="False"
          cookie["notification"]["path"]="/"+(folder if folder!=config.host_folder else "")
          import time
          tiempo=time.gmtime()
          meses=[ "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "OcT",
            "Nov",
            "Dec"]
          dias=["Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"]
          
          cookie["notification"]["expires"]= str(dias[tiempo.tm_wday+1 if len(dias)<tiempo.tm_wday+1 else 0])+", "+str(tiempo.tm_mday+1)+" "+str(meses[tiempo.tm_mon])+"  "+str(tiempo.tm_hour)+":"+str(tiempo.tm_min)+":"+str(tiempo.tm_sec)+" UTC"     

          print cookie
  
  zt=ZT(config.base_root+(config.apps_folder if data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.models_folder+routes.traducciones_folder+"traducciones-"+settings.lang.upper(),"request/",p["token"] if "token" in p else "",ext=".py")  



  import urllib,urllib2
  temp_p={}
  for elem in p:
    if type(elem)==int:
      temp_p[elem]=p[elem]
    elif type(elem)==str:
      temp_p[elem]=p[elem]
    elif type(elem)==bool:
      temp_p[elem]=p[elem]
    elif type(elem)==float:
      temp_p[elem]=p[elem]
    elif type(elem)==dict:
      temp_p[elem]=p[elem]
    elif type(elem)==list:
      temp_p[elem]=p[elem]
    elif type(elem)==tuple:
      temp_p[elem]=p[elem]
  
  php_request={}

  #=================================================================================
  #CREAR LOS LANZADORES DEL LOS PLUGINS
  
  data["plugins"]={}
  data["plugins-hooks"]=[]
  for k,plugin in enumerate(data["model"]["main"].obtenerFilas("Plugins")):
    if plugin[1]==True:
      data["plugins"][plugin[0]]=imp.load_source("plugin"+str(k),config.base_root+config.plugins_folder+plugin[0]+"/"+"default.py").Plugin(p["model"])
      hook=data["model"]["global"].obtenerFilas("Plugins")[k][1][1]
      
      
      data["plugins"][plugin[0]].cnt(data)

      for accion in hook:
        data["plugins-hooks"].append([accion["name"].split("-")[1],accion["value"]])
      
      
  #========================================================================================

  def servir(vista,data=data,path1=None,path2=None,p=p,m=m,settings=settings,config=config,routes=routes,isglobal=None,plugins=data["plugins"]):    

    import __builtin__
    import os
    from ztec.zred import clienteSock,getCookie,setCookie, redirecter,normalizar,encode
    str=__builtin__.str

     
    data["isglobal"]=isglobal

    if p["control"]=="admin":
      if path1==__builtin__.None:
        
          path1=p["base_root"]+"../admin/"+routes.vistas_folder

      if path2==__builtin__.None:
        
          path2=p["base_root"]+"../admin/"+routes.templates_url


      

      #data["incluir"]=m["incluir"]

      m["servir"](vista,path1,path2,data=data,isglobal=isglobal,plugins=plugins)


    else:

     if vista in settings.vistas:
      if path1==__builtin__.None:
          path1=p["base_root"]+routes.vistas_folder
      if path2==__builtin__.None:
          path2=p["base_root"]+routes.templates_url
      
      #data["incluir"]=m["incluir"]

      m["servir"](vista,path1,path2,data=data,isglobal=isglobal,plugins=plugins)

  for elem in settings.get_php_controllers:
    try:

      params = urllib.urlencode({"p":temp_p})
      f=urllib2.urlopen(config.base_url+config.apps_folder+settings.app+"/user/"+routes.controller_folder+routes.http_folder+routes.php_folder+elem+".php",params)
      php_request[elem]=f.read()
      f.close()


    except Exception,e:
      print e
      errores.append([sys.exc_info(),[p["base_root"]+routes.controller_folder+"default.py",config.base_url+config.apps_folder+settings.app+"/user/"+routes.controller_folder+"http/"+elem+".php"]])


  
  
  for elem in settings.global_get_controllers:
   try:


    sub=open("../"+config.controller_folder+config.global_folder+routes.http_folder+elem+".py","r")
    script=sub.read()
    sub.close()
    
    exec(script,locals())

   except Exception as e:


    errores.append([sys.exc_info(),[p["base_root"]+routes.controller_folder+"default.py",p["base_root"]+routes.controller_folder+routes.http_folder+elem+".py"]])

  for elem in settings.get_controllers:
   try:

    sub=open(p["base_root"]+routes.controller_folder+routes.http_folder+elem+".py","r")
    script=sub.read()
    sub.close()
    exec(script,locals())

   except Exception as e:


    errores.append([sys.exc_info(),[p["base_root"]+routes.controller_folder+"default.py",p["base_root"]+routes.controller_folder+routes.http_folder+elem+".py"]])
  
  for elem in settings.get_custom_controllers:
   try:

    sub=open(p["base_root"]+routes.controller_folder+routes.custom_http_folder+elem+".py","r")
    script=sub.read()
    sub.close()
    exec(script,locals())

   except Exception as e:


    errores.append([sys.exc_info(),[p["base_root"]+routes.controller_folder+"default.py",p["base_root"]+routes.controller_folder+routes.custom_http_folder+elem+".py"]])

   
    
  
 def action(data,p):#manejador de los formularios
  
  sys.path.append(p["base_root"]+"../admin/")


  



  
  debug=False
  contenttype=False



  from config import config



  import settings.routes as routes
  
  import settings.config as settings
  import imp
  from ztec.zu import redict






  
  sys.path.append(p["base_root"]+"../admin/"+routes.libs_folder)
  sys.path.append(p["base_root"]+"../admin/"+routes.models_folder)

  
  
  
  errores=[]
  for elem in settings.libs_python:
   exec("import "+elem,locals())
  
  import ztec.zu as zu
  import ztec.zred as zred 


  

  

  
  from ztec.zred import clienteSock,getCookie,setCookie, redirecter,decode,normalizar,encode,Headers
  HEADERS=Headers()
  if p["method"]=="ajax":
    HEADERS.set_headers({"Content-type":"text/plain"})
  #==============================================================================
  #INICIALIZACION DE LOS MODELOS
  if "model" not in p:
    p["model"]={}
  if "opciones" not in p:
    p["opciones"]={}


  contenido=p["model"]["global"].obtenerContenido(p["app"],"apps")[p["app"]]  

  p["model"]["global"].p=p
  p["model"]["usuarios"].p=p
  for k,db in enumerate(contenido[1]):
    if contenido[1][db]["value"] in settings.dbs:

      exec("from "+contenido[1][db]["value"]+"_model import model as model"+str(k),locals())    
      if "token" not in p:
       
       exec('p["model"][contenido[1][db]["value"]]=model'+str(k)+'(p["base_root"]+"../admin/"+routes.models_folder+contenido[1][db]["value"],p["base_root"]+"../admin/"+routes.request_folder,"user",debug=debug,ext=".py")',locals())
       p["model"][contenido[1][db]["value"]].models["global"]=p["model"]["global"]

       p["model"]["global"].models[contenido[1][db]["value"]]=p["model"][contenido[1][db]["value"]]
       if "Opciones" in p["model"][contenido[1][db]["value"]].db.tablas:
            p["opciones"][contenido[1][db]["value"]]=p["model"][contenido[1][db]["value"]].obtenerFilas("Opciones")
       

      else:

       exec('p["model"][contenido[1][db]["value"]]=model'+str(k)+'(p["base_root"]+"../admin/"+routes.models_folder+contenido[1][db]["value"],p["base_root"]+"../admin/"+routes.request_folder,p["token"],debug=debug,ext=".py")',locals())
       p["model"][contenido[1][db]["value"]].models["global"]=p["model"]["global"]
       p["model"]["global"].models[contenido[1][db]["value"]]=p["model"][contenido[1][db]["value"]]

       if "Opciones" in p["model"][contenido[1][db]["value"]].db.tablas:
            p["opciones"][contenido[1][db]["value"]]=p["model"][contenido[1][db]["value"]].obtenerFilas("Opciones") 
    p["model"][contenido[1][db]["value"]].p=p



    
  
  #===================================================================================
  #MANEJO DE REGISTRO DE ACCIONES DE USARIO(SESION)
  

  cookies=getCookie()
  p["cookies"]=cookies
  token2=None
  tokens={}



  

  if "token" in cookies:

   tokens=normalizar(cookies["token"])
  if "token2" in cookies:
    token2=normalizar(cookies["token2"])
   


   

  if settings.app in tokens and token2==None:

    p["token"]=tokens[settings.app]
    if p["model"]["usuarios"].isUser(token=tokens[settings.app]) and p["model"]["usuarios"].consultarLogin(tokens[settings.app]):
      p["user"]=p["model"]["usuarios"].obtenerUsuario(p["token"])
      p["login"]=True
      p["isGlobalUser"]=False
    else:
      p["login"]=False
    
  elif token2!=None and p["model"]["global"].consultarLogin(token2):
    p["token"]=token2
    p["user"]=p["model"]["global"].obtenerUsuario(p["token"])
    p["login"]=True
    p["isGlobalUser"]=True
  else:
    p["login"]=False
  
  for elem in p["model"]:
   if "token" in p:
    p["model"][elem].token=p["token"]
   else:
    p["model"][elem].token="user"
  #=================================================================================
  #CREAR LOS LANZADORES DEL LOS PLUGINS
  p["plugins"]={}
  for k,plugin in enumerate(p["model"]["main"].obtenerFilas("Plugins")):
    if plugin[1]==True:
      p["plugins"][plugin[0]]=imp.load_source("plugin"+str(k),config.base_root+config.plugins_folder+plugin[0]+"/"+"default.py").Plugin(p["model"])
      p["plugins"][plugin[0]].action(data,p)


      


  #========================================================================================

  if p["cookies"]!={} and normalizar(p["cookies"]["beforeArgs"])!=[]:
    if len(normalizar(p["cookies"]["beforeArgs"]))>0:
      beforeAction=normalizar(p["cookies"]["beforeArgs"])[0]
      if len(normalizar(p["cookies"]["beforeArgs"]))>1:
          indice=normalizar(p["cookies"]["beforeArgs"])[1]
  else:
   try:
     beforeAction=data["action"].value
   except Exception as e:
     beforeAction=""
   indice=None

  #=========================================================================
  #CARGA DE SUBCONTROLADORES 
  
  for elem in settings.global_post_controllers:
   try:


    sub=open("../"+config.controller_folder+config.global_folder+routes.http_folder+elem+".py","r")
    script=sub.read()
    sub.close()
    exec(script,locals())

   except Exception as e:
    print "#error: ",elem," ",e
    errores.append([sys.exc_info(),[p["base_root"]+routes.controller_folder+"default.py",p["base_root"]+routes.controller_folder+routes.http_folder+elem+".py"]])

  for elem in settings.post_controllers:
    
    sub=open(config.base_root+config.apps_folder+p["app"]+"/user/"+config.controles_dir+"/"+routes.http_folder+elem+".py","r")
    script=sub.read()
    try:
     exec(script,locals()) 
    except Exception as e:
     if settings.mod_debug!=False:
      import traceback

      exc_type,exc_obj,exc_tb=sys.exc_info()
      fname = exc_tb.tb_frame.f_code.co_filename
      print "#==================================="
      print "#No se pudo cargar el modulo ",elem
      print "# ","".join(traceback.format_exception(exc_type,fname,exc_tb))
      print "#", e
      print "#==================================="

  for elem in settings.post_custom_controllers:
    sub=open(config.base_root+config.apps_folder+p["app"]+"/user/"+config.controles_dir+"/"+routes.custom_http_folder+elem+".py","r")
    script=sub.read()
    sub.close()
    try:
     exec(script,locals()) 
    except Exception as e:
     if settings.mod_debug!=False:
      import traceback
      exc_type,exc_obj,exc_tb=sys.exc_info()
      fname = exc_tb.tb_frame.f_code.co_filename
      print "#==================================="
      print "#No se pudo cargar el modulo ",elem
      print "# ","".join(traceback.format_exception(exc_type,fname,exc_tb))
      print "#", e
      print "#==================================="
        
except Exception, e:
 
 if settings.mod_debug!=False:
  print "#",str(e)[1:-1],"<br>"