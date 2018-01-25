#Get,Ajax subcontroller
"""
if "action" in p: 
  
  if p["control"]=="admin" and "action" in p:

    if p["action"]=="listar":

      if p["method"]=="get":

        zred.listar(data,p,errores,config)

        
        
      elif p["method"]=="ajax":
        
        HEADERS.show()
        zred.listarAjax(data,p,errores,config)


        
    elif p["action"]=="actualizar":   
      data["keyNew"]="Actualizaciones"
    elif p["args"]==["contactar"]:  
      print "data['contactos']="+str(data["model"]["main"].obtenerContactos(p["args"]))
    elif p["action"]=="editar2" or p["action"]=="codear":
      

      app=settings.app

      if list(p["kwargs"])==["Diseño"]:
        data["titulo"]="Diseños"
        user="../"+config.apps_dir+"/"+app+"/user/"+routes.vistas_folder
        admin="../"+config.apps_dir+"/"+app+"/admin/"+routes.vistas_folder
        data["trees"]=[{"user":zu.treeFolder(user)},
              {"admin":zu.treeFolder(admin)},
         ]
        data["excluir"]=".py"
      elif list(p["kwargs"])==["Controlador"]:

        data["titulo"]="Controles"
        user="../"+config.apps_dir+"/"+app+"/user/"+routes.controles_folder
        
        data["trees"]=[{"controles":zu.treeFolder(user)},
         ]

        data["excluir"]=".pyc"
      elif list(p["kwargs"])==["Modelo"]:
        data["titulo"]="Modelos"
        admin="../"+config.apps_dir+"/"+app+"/admin/"+routes.models_folder
        data["trees"]=[{"modelos":zu.treeFolder(admin)},
         ]
        data["excluir"]=".pyc"
      elif list(p["kwargs"])==["Script"]:
        data["titulo"]="Scripts"
        user="../"+config.apps_dir+"/"+app+"/user/"+routes.static_folder
        admin="../"+config.apps_dir+"/"+app+"/admin/"+routes.static_folder
        globales=config.base_root+"static/"
        data["trees"]=[{"user":zu.treeFolder(user)},{"admin":zu.treeFolder(admin)},{"globales":zu.treeFolder(globales)},]
        data["excluir"]=".pyc"   

      elif list(p["kwargs"])==["Ajustes"]:
        data["titulo"]="Ajustes"
        admin="../"+config.apps_dir+"/"+app+"/admin/"+config.settings_folder
        
        data["trees"]=[{"settings":zu.treeFolder(admin),
                       }]
        data["excluir"]=".pyc"
      elif list(p["kwargs"])==["Plugin"]:
        data["titulo"]="Plugins"
        admin=config.base_root+config.plugins_folder
        
        data["trees"]=[{"plugins":zu.treeFolder(admin),
                       }]
        
        data["excluir"]=[".pyc"]
      data["renderTree"]=zred.renderTree
    elif p["action"]=="eliminar": 
      if p["method"]=="ajax":
        l=[]
        HEADERS.show()
        for elem in data["marcados"]:
          l.append(elem.value)
        

        for elem in data["marcados"]:
          c=0
          
          modelos=p["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
          tablas=p["model"]["main"].obtenerFilas('args>Tablas')[0][0]




          while c<len(l):
            if zred.normalizar(l[c])==True:
              p["model"][modelos[normalizar(data["args"].value)[0]]].eliminar(c,tablas[normalizar(data["args"].value)[0]] if normalizar(data["args"].value)[0] in tablas else normalizar(data["args"].value)[0] )
              del l[c]

              c=0
            else:
              c+=1
        
        
        print "data={}"
        #p["model"]["main"].db.delFila(,data["args"].value)
        
        lista=p["model"][modelos[normalizar(data["args"].value)[0]] if normalizar(data["args"].value)[0] in modelos else normalizar(data["args"].value)[0]].obtenerFilas(normalizar(data["args"].value)[0])
        for k,elem in enumerate(lista):
          del lista[k][1]
        print 'data["listar"]='+str(lista)
        print 'data["ajax-data"]='+str({"action":"listar","args":data["args"].value,"pag-action":None})
        print 'data["baseAction"]='+"'app="+settings.app+"&admin=True&vista=index&args="+str(data["args"].value)+"'"
        print 'data["titulo"]="'+str(data["args"].value)+'"'
        print 'data["filtrar"]='+str(["Todas las fechas","Septiembre 2014"])
        print 'data["addNew"]='+"'Añadir nuevo'"
        print 'data["n-pag"]='+str(5)
        print "data['campos']="+str(["Titulo","Fecha"])
        print "data['app']='"+settings.app+"'"
        print "data['vista']='"+"index"+"'"
        print 'data["action"]="'+p["action"]+'"'
        
        print 'data["beforeAction"]="listar"'
        print 'data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}'
    elif p["action"]=="licencias":
      import os
      data["licencias"]=os.listdir(config.base_root+"static/licencias")
    elif p["action"]=="post":




      if p["method"]=="get":
        data["listar"]=[]
        filtrados=[]
        dicstatus={}

        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]
        modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]
        
        if data["args"][0] in data["model"][modelos[data["args"][0]]].db.tablas:

          
          data["listar"]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerFilas(tablas[data["args"][0]] if data["args"][0] else data["args"][0])

          data['status']=["Publicada"]
          for elem in data['status']:
            filtrados=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].filtrar([elem],data["args"][0])
            dicstatus[elem]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerIdsFiltrados(filtrados)

        data["ajax-data"]={"action":"listar","args":data["args"],"pag-action":None}
        #data["baseAction"]="app="+data["app"]+"&admin=True&vista=index&args="+data["args"]
        data["titulo"]=data["args"][0]
        data["acciones"]=["Acciones en lote","Editar","Mover a la papelera"]
        data["filtrar"]=["Todas las fechas","Septiembre 2014"]
        data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}
        data["addNew"]="Añadir nuevo"
        data["n-pag"]=5
        
        
        
        data['filtros']=dicstatus
        if data["titulo"]=="Post-de-Formulario":
          data["keyNew"]="Post-de-Formularios"

        elif data["titulo"]=="Plantillas":
          data["keyNew"]="Plantilla"
        elif data["titulo"]=="Entradas":
          data["keyNew"]="Entrada"
        elif data["titulo"]=="Menus":
          data["keyNew"]="Menu"
        elif data["titulo"]=="Portafolio":
          data["keyNew"]="Portafolio"
        elif data["titulo"]=="Usuarios":
          data["keyNew"]="Usuario"
        elif data["titulo"]=="Formularios":
          data["keyNew"]="Formulario"
        elif data["titulo"]=="Negocios":
          data["keyNew"]="Negocio"
          data["listar"]=data["model"]["negocio"].obtenerFilas(data["args"])
        elif data["titulo"]=="Archivos":
          data["keyNew"]="Archivo"
          #data["listar"]=data["model"]["main"].obtenerFilas(data["args"])
        elif data["titulo"]=="Galerias":
          data["keyNew"]="Galeria"
        elif data["titulo"]=="Publicaciones":
          data["keyNew"]="Publicacion"
        elif data["titulo"]=="Anuncios":
          data["keyNew"]="Anuncio"
        elif data["titulo"]=="Informaciones":
          data["keyNew"]="Info"
        elif data["titulo"]=="Clientes":
          data["keyNew"]="Cliente"
        elif data["titulo"]=="Publicaciones":
          data["keyNew"]="Publicacion"
        elif data["titulo"]=="Escritorio":
          data["keyNew"]="Escritorio"
        elif data["titulo"]=="Plugins":
          data["keyNew"]="Plugin"

      elif p["method"]=="ajax":

        tablas=p["model"]["main"].obtenerFilas("Tablas")[0][0]
        lista=p["model"][tablas[normalizar(data["args"])[0].lower()]].obtenerFilas(data["args"].value)
        formato=p["model"][tablas[data["args"][0].lower()]].db(data["args"].value).obtenerFormato("Fecha")
        titulo=data["args"].value
        HEADERS.show()
        print "data={}"
        lista=p["model"]["main"].obtenerFilas(data["args"].value)
        for k,elem in enumerate(lista):
          del lista[k][1]
        print 'data["listar"]='+str(lista)
        print 'data["ajax-data"]='+str({"action":"post","args":data["args"].value,"pag-action":None})
        print 'data["baseAction"]='+"'app="+p["app"]+"&admin=True&vista=index&args="+str(data["args"].value)+"'"
        print 'data["titulo"]="'+str(normalizar(data["args"].value)[0])+'"'
        print 'data["filtrar"]='+str(["Todas las fechas","Septiembre 2014"])
        print 'data["addNew"]='+"'Añadir nuevo'"
        print 'data["n-pag"]='+str(5)
        print "data['campos']="+str(["Titulo","Fecha"])

         
        print "data['app']='"+p["app"]+"'"
        print "data['vista']='"+"index"+"'"
         
        print 'data["beforeAction"]="'+p["action"]+'"'
        print 'data["action"]="'+p["action"]+'"'
        print 'data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}'
         
        if titulo=="Paginas":
          pass

        elif titulo=="Entradas":
          pass

        elif titulo=="Menus":
          pass

        elif titulo=="Portafolio":
          pass

        elif titulo=="Usuarios":
          
          pass
        elif titulo=="Plugins":
          print "data['campos']="+str(["Plugin","Descripción"])

        elif titulo=="Negocios" or titulo=="Archivos":
            #{filto:[elementos filtrados]}
            
            status=["Publicada"]
            dicstatus={}

                                      
            for elem in status:

              filtrados=p["model"]["main"].ordenar(filtros=[elem])
              dicstatus[elem]=p["model"]["main"].obtenerIdsFiltrados(filtrados)
            
            print "data['filtros']="+str(dicstatus)
            
        else:
            print "data['campos']="+str(["Titulo","Fecha"])
     
    elif p["action"]=="editar":
        """
        se puede crear un prefijo custom:nombre en el name para saber cuando son nuevos campos 
        ejemplo
        {"Titulo":"text","value":"hola","name":"custom:nombre"}
        """
        data["repeate"]=1
        data["plantillas"]=data["model"]["main"].obtenerFilas("Plantillas")
        data["boxes"]=[]
        if p["method"]=="ajax":
          pass

        elif p["method"]=="get":
          if "args" in p:
            keys=p["args"][0]
            i=normalizar(p["args"][1])
            data["categorias"]={}
            data["titulo"]=p["args"][0]


    elif p["action"]=="plugin":
      plugin=p["args"]["plugin"]#nombre del plugin accedido
      namespace=p["args"]["namespace"]#global, local
    elif p["action"]=="allapps":
      l=p["model"]["global"].obtenerFilas("apps")
      import os

      for k,elem in enumerate(l):

        if os.path.isdir("../"+config.apps_folder+elem[0]):
          

          l[k][1].append({"Screenshot":"url","name":"screenshot","value":config.base_url+config.apps_folder+elem[0]+"/screenshot.png"})

      
      
      data["items"]=l
      
      params = urllib.urlencode({"control":"allapps","app":None,"asenzor":True})

      f=urllib2.urlopen(config.asenzor_host+config.controller_folder+"ajax.py",params)
      
      
      item=redict(normalizar(f.read()))






      
      data["items-destacadas"]=item["Destacada"]
      data["items-populares"]=item["Populares"]
      data["items-recientes"]=item["Recientes"]
      data["items-favoritos"]=item["Favoritos"]
      

      f.close()
      

    elif p["action"]=="plugins":
      l=p["model"]["global"].obtenerFilas("Plugins")
      l2=p["model"]["main"].obtenerFilas("Plugins")
      import os

      for k,elem in enumerate(l):

        if os.path.isdir("../"+config.plugins_folder+elem[0]):
          
          l[k][1].append({"Screenshot":"url","name":"screenshot","value":config.base_url+config.plugins_folder+elem[0]+"/screenshot.png"})
          HEADERS.show()
          #l[k][-1].append("Desactivada" if l2[k][-1]==False else "Activada")
      data["items"]=l
      
      
      
      
      
      params = urllib.urlencode({"control":"plugins","app":None,"asenzor":True})

      f=urllib2.urlopen(config.asenzor_host+config.controller_folder+"ajax.py",params)
      item=redict(normalizar(f.read()))
      
      data["items-destacadas"]=item["Destacada"]
      data["items-populares"]=item["Popular"]
      data["items-recientes"]=item["Reciente"]
      data["items-favoritos"]=item["Favorita"]


      f.close()
      
      

    elif p["action"]=="menus":
      if p["method"]=="get":
        HEADERS.show()
        data["Paginas"]=p["model"]["paginas"].obtenerMetadatos("Paginas")
        data["Menus"]=p["model"]["main"].obtenerFilas("Menus")
        data["Entradas"]=p["model"]["paginas"].obtenerMetadatos("Entradas")
        data["Categorias"]=p["model"]["paginas"].obtenerFilas("Categorias")
        
        data["other-tags"]=p["model"]["main"].obtenerFilas("Menus-categoria")[0][1]

        








"""