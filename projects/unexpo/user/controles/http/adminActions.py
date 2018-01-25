#Get,Ajax subcontroller

if "action" in p: 
  if p["control"]=="admin" and "action" in p:



    if p["action"]=="listar":
      if p["method"]=="get":

        modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]


        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]


        
        
        data["listar"]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerFilas(tablas[data["args"][0]] if data["args"][0] else data["args"][0]) 
        


        data["ajax-data"]={"action":"listar","args":data["args"],"pag-action":None}
        data["baseAction"]="app="+data["app"]+"&admin=True&vista=index&args="+data["args"][0]
        data["titulo"]=decode(data["args"][0])
        data["acciones"]=["Acciones en lote","Editar","Mover a la papelera"]
        data["filtrar"]=["Todas las fechas","Septiembre 2014"]
        data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}
        data["addNew"]="Añadir nuevo"
        data["n-pag"]=5
        data['status']=["Publicada"]
        dicstatus={}
        for elem in data['status']:
          try:
            filtrados=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].filtrar([elem],data["args"][0])
            dicstatus[elem]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerIdsFiltrados(filtrados)
          except:
            filtrados=[]
            dicstatus={}
        data['filtros']=dicstatus
        if data["titulo"]=="Paginas":  
          data["keyNew"]="Pagina"
        elif data["titulo"]=="Editar tema":
          data["keyNew"]="Pagina"
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
          data["listar"]=data["model"]["negocio"].obtenerFilas(data["args"][0])
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
        elif data["titulo"]=="Ayuda":
          data["keyNew"]="Ayuda"
      elif p["method"]=="ajax":

        modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]
        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]
        

        
        lista=p["model"][modelos[normalizar(data["args"].value)[0]]].obtenerFilas(tablas[normalizar(data["args"].value)[0]])

        formato=p["model"][modelos[normalizar(data["args"].value)[0]]].db(tablas[normalizar(data["args"].value)[0]]).obtenerFormato("Fecha")
        titulo=data["args"].value
        print "data={}"
        
        #lista=p["model"][tablas[normalizar(data["args"].value)[0].lower()]].obtenerFilas(normalizar(data["args"].value)[0])
        for k,elem in enumerate(lista):
          del lista[k][1]
        print 'data["listar"]='+str(lista)
        print 'data["ajax-data"]='+str({"action":"listar","args":normalizar(data["args"].value)[0],"pag-action":None})
        print 'data["baseAction"]="'+zred.urlBuilder(config,p["app"],"admin","index",args=normalizar(data["args"].value))+'"'
        print 'data["titulo"]="'+str(data["args"].value)+'"'
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
        user="../"+config.apps_dir+"/"+app+"/user/"+config.controller_folder
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
        for elem in data["opciones"]:
          l.append(elem.value)
        for elem in data["opciones"]:
          c=0
          while c<len(l):
            if zred.normalizar(l[c])==True:
              p["model"]["main"].borrarFila(c,data["args"].value)
              del l[c]
              c=0
            else:
              c+=1
        print "data={}"
        #p["model"]["main"].db.delFila(,data["args"].value)
        tablas=p["model"]["main"].obtenerFilas("Tablas")[0][0]
        lista=p["model"][tablas[normalizar(data["args"].value)[0].lower()]].obtenerFilas(data["args"].value)
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

                      

        if p["method"]=="ajax":
          pass

        elif p["method"]=="get":
          if "args" in p:
            keys=p["args"][0]
            i=normalizar(p["args"][1])
            data["categorias"]={}
            data["titulo"]=p["args"][0]

            if i!=None:
              data["categorias"]={}

              
              if keys=="Menu":

                i=normalizar(p["args"][1])
                data["titulo"]=data["model"]["main"].obtenerFilas("Menus")[i][0]
                l1=data["model"]["main"].obtenerFilas("Menus")[i][1]
                data["boxes"]=[l1]
              elif keys=="Pagina":
                data["titulo"]=data["model"]["paginas"].obtenerFilas("Paginas")[i][0]
                data["layout"]=data["titulo"]
                data["post"]=str(i)
                data["pagina"]="{'pagina':'"+data["titulo"]+"'}"
                
                if len(data["args"])>2:
                  
                  l1=data["model"]["paginas"].obtenerFilas("Pagina-"+str(data["args"][2]) )[i][1]
                else:
                  l1=data["model"]["paginas"].obtenerFilas("Paginas")[i][1]

                data["boxes"]=[l1]

              elif keys=="Plantilla":
                data["titulo"]=data["model"]["main"].obtenerFilas("Plantillas")[i][0]
                data["pagina"]="{'pagina':'"+data["titulo"]+"'}"
                l1=data["model"]["main"].obtenerFilas("Plantillas")[i][1]
                data["boxes"]=[l1]

              elif keys=="Plugin":
                data["titulo"]=data["model"]["main"].obtenerFilas("Plugins")[i][0]
                l1=data["model"]["main"].obtenerFilas("Plugins")[i][1]
                
                data["boxes"]=[l1]
              elif keys=="Entrada":
                l1=[]             
                data["titulo"]=data["model"]["entradas"].obtenerFilas("Entradas")[i][0]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                l1=data["model"]["entradas"].obtenerFilas("Entradas")[i][1]
                data["boxes"]=l1
              elif keys=="Archivo":
                l1=[]
                l2=[]
                for elem in data["model"]["archivos"].obtenerFilas("Opciones"):
                 if elem[0] not in l2:
                  l2.append(elem[0])

                data["tablas"]={"Opciones":l2}
                data["titulo"]=data["model"]["archivos"].obtenerFilas("Archivos")[i][0]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]

                l1=data["model"]["archivos"].obtenerFilas("Archivos")[i][1]
                data["boxes"]=l1
              elif keys=="Usuario":
                l1=[]
                data["titulo"]=data["model"]["usuarios"].obtenerFilas("Usuarios")[i][0]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                l1=data["model"]["usuarios"].obtenerFilas("Usuarios")[i][1]
                data["boxes"]=l1
              elif keys=="Galeria":
                data["titulo"]=data["model"]["galerias"].obtenerFilas("Galerias")[i][0]
                l1=data["model"]["galerias"].obtenerFilas("Galerias")[i][1]
                data["boxes"]=l1
                data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Publicacion":             
                data["titulo"]=data["model"]["publicaciones"].obtenerFilas("Publicaciones")[i][0]
                l1=data["model"]["publicaciones"].obtenerFilas("Publicaciones")[i][1]
                data["boxes"]=l1
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Anuncio":
                data["titulo"]=data["model"]["anuncios"].obtenerFilas("Anuncios")[i][0]
                l1=data["model"]["anuncios"].obtenerFilas("Anuncios")[i][1]
                data["boxes"]=l1
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Cliente":
                data["titulo"]=data["model"]["clientes"].obtenerFilas("Clientes")[i][0]
                l1=data["model"]["clientes"].obtenerFilas("Clientes")[i][1]
                data["boxes"]=l1
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Info":
                data["titulo"]=data["model"]["informaciones"].obtenerFilas("Informaciones")[i][0]
                l1=data["model"]["informaciones"].obtenerFilas("Informaciones")[i][1]
                data["boxes"]=l1
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Formulario":
                i=p["args"][1]
                data["titulo"]=data["model"]["formularios"].obtenerFilas("Formularios")[i][0]
                l1=data["model"]["formularios"].obtenerFilas("Formularios")[i][1]
                data["boxes"]=l1
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Post-de-Formulario":
                data["titulo"]=data["model"]["formularios"].obtenerFilas("Post-de-Formulario")[i][0]
                l1=data["model"]["formularios"].obtenerFilas("Post-de-Formulario")[i][1]
                data["boxes"]=[l1]
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Negocio":
                l1=[]
                l2=[]
                for elem in p["model"]["negocios"].obtenerFilas("Categorias"):
                 if elem[0] not in l2:
                  l2.append(elem[0])
                data["tablas"]={"Categorias":l2}
                l2=[]
                for elem in p["model"]["negocios"].obtenerFilas("Categorias"):
                 if elem[0] not in l2:
                  l2.append(elem[0])
                data["tablas"]={"Categorias":l2}
                l2=[]
                for elem in p["model"]["negocios"].obtenerFilas("Imagenes"):
                  
                  if elem[0] not in l2:
                   l2.append(elem[0])
                 
                data["tablas"]["Imagenes"]=l2
                
                data["categorias"]={}
                
                data["imagenes"]=p["model"]["negocios"].obtenerFilas("Imagenes")
                for categoria in data["tablas"]["Categorias"]:
                 data["categorias"][categoria]={}
                 for subcategoria in p["model"]["negocios"].obtenerSubcategorias(categoria):
                  data["categorias"][categoria][subcategoria]=p["model"]["negocios"].obtenerSubcategoriasOpciones(categoria,subcategoria)
                data["titulo"]=p["model"]["negocios"].obtenerFilas("Negocios")[i][0]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                l1=p["model"]["negocios"].obtenerFilas("Negocios")[i][1]
                data["boxes"]=[l1]
              elif keys=="Ayuda":
                i=p["args"][1]
                data["titulo"]=data["model"]["main"].obtenerFilas("Ayuda")[i][0]
                l1=data["model"]["main"].obtenerFilas("Ayuda")[i][1]
                data["boxes"]=l1
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="PostdeFormulario":
                data["titulo"]=data["model"]["formularios"].obtenerFilas("Post-de-Formulario")[i][0]
                l1=data["model"]["formularios"].obtenerFilas("Post-de-Formulario")[i][1]
                data["boxes"]=[l1]
                #data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
            else:

              
              if keys=="Archivo":
                l1=[]
                i=p["args"][keys[0]]
                data["titulo"]="Subir nuevo archivo"
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                l2=[]
                 
                for elem in data["model"]["archivos"].obtenerFilas("Opciones"):
                  if elem[0] not in l2:
                    l2.append(elem[0])
                                                          
                data["tablas"]={"Opciones":l2}
                                                         
                for box in data["model"]["archivos"].obtenerFilas("Archivos")[0][1]:
                  l=[]
                  for campos in box:
                    if type(campos)==dict:
                      campos["value"]=""
                      l.append(campos)
                  if l!=[]:
                    l1.append(l)
                data["boxes"]=l1
              elif keys=="Formulario":
                data["titulo"]="Crear Nuevo formulario"
                data["boxes"]=[]
              elif keys=="Galeria":
                i=0
                data["titulo"]=data["model"]["galerias"].obtenerFilas("Galerias")[i][0]
                l1=data["model"]["galerias"].obtenerFilas("Galerias")[i][1]
                data["boxes"]=l1
                data["new"]=True #permite añadir un campo mas al formulario basado en el campo 1
              elif keys=="Usuario":
                l1=[]
                data["titulo"]=data["model"]["usuarios"].obtenerFilas("AdminMenu")[3][2]["titulo"]
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
              elif keys=="Ayuda":
                l1=[]
                data["titulo"]=data["model"]["main"].obtenerFilas("AdminMenu")[3][2]["titulo"]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                for box in data["model"]["main"].obtenerFilas("Usuarios")[0][1]:
                 l=[]
                 for campos in box:
                  if type(campos)==dict:
                   campos["value"]=""
                   l.append(campos)
                 if l!=[]:
                  l1.append(l)
                data["boxes"]=l1
              elif keys=="Pagina":
                l1=[]
                data["titulo"]=data["model"]["main"].obtenerFilas("AdminMenu")[1][2]["titulo"]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                if len(data["model"]["paginas"].obtenerFilas("Paginas"))>0:
                 for box in data["model"]["paginas"].obtenerFilas("Paginas")[0]:
                  l=[]
                  for campos in box:
                   if type(campos)==dict:
                    campos["value"]=""
                    l.append(campos)
                  if l!=[]:
                   l1.append(l)
                 data["boxes"]=l1
                else:
                 data["boxes"]=[]
              elif keys==["Plantilla"]:
                  data["titulo"]="Nueva plantilla"

              elif keys=="Menu":
                l1=[]
                i=0
                menus=data["model"]["main"].obtenerFilas("Menus")[0][1]
                data["titulo"]=data["model"]["main"].obtenerFilas("AdminMenu")[3][2]["titulo"]
                for box in data["model"]["main"].obtenerFilas("Menus")[0][1]:
                 l=[]
                 for campos in box:
                  if type(campos)==dict:
                   campos["value"]=""
                   l.append(campos)
                 if l!=[]:
                  l1.append(l)
                data["boxes"]=l1
              elif keys=="Publicacion":
                l1=[]
                i=0
                menus=data["model"]["main"].obtenerFilas("Menus")[0][1]
                data["titulo"]=data["model"]["main"].obtenerFilas("AdminMenu")[3][2]["titulo"]
                for box in data["model"]["main"].obtenerFilas("Menus")[0][1]:
                 l=[]
                 for campos in box:
                  if type(campos)==dict:
                   campos["value"]=""
                   l.append(campos)
                 if l!=[]:
                  l1.append(l)
                data["boxes"]=l1
              elif keys=="Info":
                l1=[]
                i=normalizar(p["args"][1])
                data["titulo"]=data["model"]["main"].obtenerFilas("AdminMenu")[3][2]["titulo"]
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                for box in data["model"]["informaciones"].obtenerFilas("Informaciones")[0][1]:
                 l=[]
                 for campos in box:
                  if type(campos)==dict:
                   campos["value"]=""
                   l.append(campos)
                 if l!=[]:
                  l1.append(l)
                data["boxes"]=l1
              elif keys=="Entrada":
                l1=[]
                i=normalizar(p["args"][1])
                data["titulo"]="Nueva Entrada"
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                for box in data["model"]["entradas"].obtenerFilas("Entradas")[0][1]:
                 l=[]
                 for campos in box:
                  if type(campos)==dict:
                   campos["value"]=""
                   l.append(campos)
                 if l!=[]:
                  l1.append(l)
                data["boxes"]=l1
              elif keys=="Negocio":
                l1=[]
                i=normalizar(p["args"][1])
                data["titulo"]="Nuevo Negocio"
                #data["model"]["main"].obtenerFilas("Paginas")[i][1]
                l2=[]
                for elem in p["model"]["negocios"].obtenerFilas("Categorias"):
                 if elem[0] not in l2:
                  l2.append(elem[0])
                  data["tablas"]={"Categorias":l2}
                  l2=[]
                for elem in p["model"]["negocios"].obtenerFilas("Categorias"):
                 if elem[0] not in l2:
                  l2.append(elem[0])
                  data["tablas"]={"Categorias":l2}
                  l2=[]
                for elem in p["model"]["negocios"].obtenerFilas("Imagenes"):
                
                  if elem[0] not in l2:
                   l2.append(elem[0])
                  data["tablas"]["Imagenes"]=l2
                  data["categorias"]={}
                  data["imagenes"]=p["model"]["negocios"].obtenerFilas("Imagenes")
                for categoria in data["tablas"]["Categorias"]:
                  data["categorias"][categoria]={}
                for subcategoria in p["model"]["negocios"].obtenerSubcategorias(categoria):
                  data["categorias"][categoria][subcategoria]=p["model"]["negocios"].obtenerSubcategoriasOpciones(categoria,subcategoria)
                for box in p["model"]["negocios"].obtenerFilas("Negocios")[0]:
                 l=[]
                 for campos in box:
                  l2=[]
                  if type(campos)==dict:
                   tmp=campos.keys()
                   tmp.remove("name") if "name" in tmp else tmp
                   tmp.remove("value") if "value" in tmp else tmp
                   tmp.remove("step") if "step" in tmp else tmp
                   tmp.remove("opcion") if "opcion" in tmp else tmp
                   tmp.remove("requerido") if "requerido" in tmp else tmp
                   tmp.remove("tabla") if "tabla" in tmp else tmp
                   tmp.remove("depende") if "depende" in tmp else tmp
                   tmp=tmp[0]
                   if campos[tmp]=="select":
                    campos["value"]=0
                   elif campos[tmp]!="fixed":

                    campos["value"]=""
                   l.append(campos)
                  elif type(campos)==list:
                   for sub in campos:
                    tmp=sub.keys()
                    tmp.remove("name") if "name" in tmp else tmp
                    tmp.remove("value") if "value" in tmp else tmp
                    tmp.remove("step") if "step" in tmp else tmp
                    tmp.remove("opcion") if "opcion" in tmp else tmp
                    tmp.remove("requerido") if "requerido" in tmp else tmp
                    tmp.remove("tabla") if "tabla" in tmp else tmp
                    tmp.remove("depende") if "depende" in tmp else tmp
                    tmp=tmp[0]
                    if sub[tmp]=="select":
                     sub["value"]=0
                    elif sub[tmp]!="fixed":
                     sub["value"]=""
                    l2.append(sub)

                   if l2!=[]:
                    l.append(l2)

               
                if l!=[]:
                  l1.append(l)
                  data["boxes"]=l1
     

    elif p["action"]=="plugin":
      plugin=p["args"]["plugin"]#nombre del plugin accedido
      namespace=p["args"]["namespace"]#global, local
    elif p["action"]=="allapps":
      l=[]
      import os
      
      for elem in os.listdir("../"+config.apps_folder):
      
        if os.path.isdir("../"+config.apps_folder+elem):
          l.append(elem)
      
      data["webapps"]=l
      









