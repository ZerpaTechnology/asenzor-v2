
list=py_datos.list
type=py_datos.py_metatype
__pragma__("alias","s","$")

codeEditor="""
elem=document.getElementsByClassName("codeEditor")[document.getElementsByClassName("codeEditor").length-1]
editor = CodeMirror.fromTextArea(elem, {
    lineNumbers: true,
    mode: mixedMode,
    keyMap: "sublime",
    autoCloseBrackets: true,
    matchBrackets: true,
    showCursorWhenSelecting: true,
    theme: "monokai",
    tabSize: 2,
    selectionPointer: true
  });
emmetCodeMirror(editor);
editores.push(editor);
"""

config=Config.Config()
decode=Codificador.Codificador.decode
rest=nuclear.getRest()
normalizar=nuclear.normalizar



if "action" in rest and "codear" ==rest["action"]:
 
 s("#alert").removeClass("hidden")
 
if list(rest["kwargs"])[0]=="Diseño":
  
  s("#alert").html("""
  <div class="pad-1" style="z-index:100">
  <span id="alert-close">x</span>
  <h1>Nombre</h1>
  <input type="text" name="nombre" id="nombre" style="width:100%">
  </div>
  
  <div class="pad-1 d-inline-block">
  <label>Usuario</label>
  <select name="user" id="user">
   <option>admin</option>
   <option>user</option>
  </select>
  </div>
  <div class="pad-1 d-inline-block">
  <label>Diseño</label>
  <select name="opcion" id="widget">
   <option>Template</option>
   <option>Widget</option>
  </select>
  </div>
  
  <div class="text-center marg-t5">
  <button id="crear" class="white bg-blue pad-05">Crear</button>
  </div>
  
  """)

elif list(rest["kwargs"])[0]=="Controlador" or list(rest["kwargs"])[0]=="Modelo":
  s("#alert").html("""
  <div class="pad-1" style="z-index:100">
  <span id="alert-close">x</span>
  <h1>Nombre</h1>
  <input type="text" name="nombre" id="nombre" style="width:100%">
  </div>
  <div class="text-center marg-t5">
  <button id="crear" class="white bg-blue pad-05">Crear</button>
  </div>
  
  """)



s("#alert").css({"background-color":"white",
  "width":"300px",
  "height":"300px",
  "margin-left":str((window.innerWidth/2)-150)+"px",
  "margin-top":str((window.innerHeight/2)-150)+"px",
  "top":str(-s("#alert")[0].clientHeight/2)+"px",
  "left":str(-s("#alert")[0].clientWidth/2)+"px",
  "border":"solid",})


valores=[]

def _lambda( evt):
 
 for k,elem in enumerate(evt.target.parentNode.children):
  if elem==evt.target:
   
   if not s(evt.target.parentNode.children[k+1]).hasClass("hidden"):
    s(evt.target.parentNode.children[k+1]).addClass("hidden")

   else:
    s(evt.target.parentNode.children[k+1]).removeClass("hidden")
 

s(".folderclass").bind("click",_lambda )

def borrar(evt):
      for k,elem in enumerate(s(".tab")):
          if not s(elem).hasClass("hidden"):
           break
      if s(".path")[k].innerHTML!="":
        
        s.post(config.base_url,{"manager":True,"control":"admin","metodo":"delete","kwargs":{"path":s(".path")[k].innerHTML}}).done(
          lambda data: window.alert(data)
          )
        
        s("#tabs-btn")[0].removeChild(s("#tabs-btn")[0].children[k])
        s(".tab")[k].parentNode.removeChild(s(".tab")[k])
        __pragma__("js","{}","window.editores.splice(k,1)")

      if len(s(".tab"))==0 and s("#borrar").children()!=[]:
          s("#guardar")[0].parentNode.removeChild(s("#borrar")[0])
      
      if len(s(".tab"))==0:
        s("#guardar")[0].parentNode.removeChild(s("#guardar")[0])
      
      if len(s(".tab"))>0 and k!=0:
        s(s(".tab")[len(s(".tab"))-1]).removeClass("hidden")
      elif len(s(".tab"))>0 and k==0:
        s(s(".tab")[0]).removeClass("hidden")
      


def update():
  
  def cerrar(evt):
    
      for k,elem in enumerate(s(".close-btn")):
        if elem==evt.target:
          s("#tabs-btn")[0].removeChild(evt.target.parentNode)
          s(".tab")[k].parentNode.removeChild(s(".tab")[k])
          __pragma__("js","{}","window.editores.splice(k,1)")
          
          if len(s(".tab"))>0:
            s(s(".tab")[k-1]).removeClass("hidden")
      
      if len(s(".tab-btn"))==0 and s("#borrar")!=[]:
        s("#guardar")[0].parentNode.removeChild(s("#borrar")[0])

      if len(s(".tab-btn"))==0:
        s("#guardar")[0].parentNode.removeChild(s("#guardar")[0])



  def mover(evt):
      for k,elem in enumerate(s(".tab-btn")):
        if elem==evt.target:
          break
      for k2,elem in enumerate(s(".tab")):
        if k2!=k:
          s(elem).addClass("hidden")
        else:
          s(elem).removeClass("hidden")
            
           
  def guardar(evt):
   
   s.post(config.base_url,
          {"app":rest["app"],
          "metodo":"write",
          "control":"admin",
          "kwargs":{"path":s(".path")[k].text},
          "file":window.editores[k].getDoc().getValue()},
    lambda data: window.alert(data)) 
   for k,tab in enumerate(s(".tab")):
    if not s(tab).hasClass("hidden"):
      break
   if len(s("#borrar"))==0:
        s("#btns-action")[0].innerHTML+="<button id='borrar'>Borrar</button>"
   
   
   


  try:
    s(".close-btn").unbind("click", cerrar)
  except:
    pass
  s(".close-btn").bind("click", cerrar)
  try:
    s("#guardar").unbind("click",guardar)
  except:
    pass
  s("#guardar").bind("click",guardar)
  try:
    s("#borrar").unbind("click",borrar)
  except:
    pass
  s("#borrar").bind("click",borrar)
  try:
    s(".tab-btn").unbind("click", mover)
  except:
    pass
  s(".tab-btn").bind("click", mover)
  
  if len(window.editores)==len(s(".tab"))-1:
    global codeEditor
    window.eval(codeEditor)

  
  
  
  """
  for k,elem in enumerate(valores):
    window.editores[k].getDoc().setValue(valores[k])
  """
  
def guardar(evt):
   for k,elem in enumerate(s(".tab")):
          if not s(elem).hasClass("hidden"):
           break
   data=__new__(FormData)
   data.append("manager",rest["manager"])
   data.append("app",rest["app"])
   data.append("metodo","write")
   data.append("control","admin")
   data.append("path",s(".path")[k].innerText)
   data.append("file",str(window.editores[k].getDoc().getValue()))
   
   s.ajax({
    "url":config.base_url,
    "data":data,
    "cache":False,
    "contentType":False,
    "processData":False,
    "type":"POST",
    "method":"POST",
    "success":lambda data: window.alert(data)
    }) 
   for k,tab in enumerate(s(".tab")):
    if not s(tab).hasClass("hidden"):
      break
   if s("#borrar")==[]:
        s("#btns-action")[0].innerHTML+="<button id='borrar'>Borrar</button>"
   
   update()

  window.shortcut.add("Ctrl+s",guardar)


def crear(evt):
 def show(data): 
    
    if data.endswith("/") or data.endswith("\\"):
      ruta=data.strip()
    else:
      ruta=data.strip()+"/"
    
    if len(s(".path"))==1:    
      if s(".path")[0].innerText.strip()=="":
        if list(rest["kwargs"])[0]=="Diseño":
          s(".path")[0].innerHTML=ruta+s("#nombre")[0].value+".html"
        elif list(rest["kwargs"])[0]=="Controlador" or list(rest["kwargs"])[0]=="Modelo":
          s(".path")[0].innerHTML=ruta+s("#nombre")[0].value+".py"
        else:
          s(".path")[0].innerHTML=ruta+s("#nombre")[0].value
        s(".tab-btn")[0].innerHTML=s("#nombre")[0].value
        if s("#guardar")==[]:
            s("#btns-action")[0].innerHTML+='<button class="bg-blue white" id="guardar">Guardar</button>'
        s("#guardar")[0].parentNode.innerHTML+="<button id='borrar'>Borrar</button>"
        
      else:

          if s("#guardar")==[]:
            s("#btns-action")[0].innerHTML+='<button class="bg-blue white" id="guardar">Guardar</button>'
            
          s("#tabs-btn")[0].innerHTML+='<span style="padding:2px"><button class="tab-btn">'+s("#nombre")[0].value+'</button><button class="close-btn">x</button></span>'
          for k,elem in enumerate(s(".tab")):
            s(elem).addClass("hidden")
            pass

          
          s("#content2")[0].children[len(s(".tab"))].innerHTML+='<div class="tab"><div class="path" style="overflow-x:scroll">'+ruta+'</div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>'
          
          if list(rest["kwargs"])[0]=="Diseño":
            s(".path")[k+1].innerHTML=ruta+s("#nombre")[0].value+".html"
          elif list(rest["kwargs"])[0]=="Controlador" or list(rest["kwargs"])[0]=="Modelo":
            s(".path")[k+1].innerHTML=ruta+s("#nombre")[0].value+".py"
          else:
            s(".path")[k+1].innerHTML=ruta+s("#nombre")[0].value
          

    else: 

        s("#tabs-btn")[0].innerHTML+='<span style="padding:2px"><button class="tab-btn">'+s("#nombre")[0].value+'</button><button class="close-btn">x</button></span>'
        
        for k,elem in enumerate(s(".tab")):
          s(elem).addClass("hidden")
        
        s("#content2")[0].children[len(s(".tab"))].innerHTML+='<div class="tab"><div class="path" style="overflow-x:scroll">'+ruta+'</div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>'
        if s("#guardar")==[]:
            s("#btns-action")[0].innerHTML+='<button class="bg-blue white" id="guardar">Guardar</button>'
        
        k=0
        for k, elem in enumerate(s(".tab")):
          if not s(elem).hasClass("hidden"):
            break
        if list(rest["kwargs"])[0]=="Diseño":
          s(".path")[k].innerHTML=ruta+s("#nombre")[0].value+".html"
        elif list(rest["kwargs"])[0]=="Controlador" or list(rest["kwargs"])[0]=="Modelo":
          s(".path")[k].innerHTML=ruta+s("#nombre")[0].value+".py"
        else:
          s(".path")[k].innerHTML=ruta+s("#nombre")[0].value
        
    update()
    s("#alert").addClass("hidden")
    s("#nombre")[0].value="" 
 
 if list(rest["kwargs"])[0]=="Diseño":
  url=config.base_url+rest["app"]+"/admin/Show/path/"+("user" if s("#user")[0].value=="user" else "admin")+"/"+("layouts" if s("#widget")[0].value=="Template" else "widgets")
  __pragma__("js","{}","$.get(url).done(show)")
  

 elif list(rest["kwargs"])[0]=="Controlador":
  url=config.base_url+rest["app"]+"/admin/Show/path/user/controladores"
  __pragma__("js","{}","$.get(url).done(show)")

 elif list(rest["kwargs"])[0]=="Modelo":
  url=config.base_url+rest["app"]+"/admin/Show/path/admin/modelos"
  __pragma__("js","{}","$.get(url).done(show)")
 
  

 
 

s("#crear").bind("click",crear)



def navegar(target):
  path=[]
  while (target.parentNode.tagName=="UL" or target.parentNode.tagName=="LI"):

    if s(target).hasClass("fileclass"):
      path.insert(0,target.innerHTML)

      if s(target.parentNode.parentNode.previousSibling).hasClass("folderclass"):

        target=target.parentNode.parentNode.previousSibling

      else:
        target=target.parentNode


    elif s(target).hasClass("folderclass"):
      
      path.insert(0,target.innerHTML)
      
      if s(target.parentNode.parentNode.previousSibling).hasClass("folderclass"):

        target=target.parentNode.parentNode.previousSibling
      else:
        target=target.parentNode
    else:
      target=target.parentNode

  return path


def seleccionar( evt):
  key=list(rest["kwargs"])
  
  archivo=evt.target.innerText.strip()

  path="/".join(navegar(evt.target))
  
  modo="text/plain"
  for elem in [".html",".py",".by",".zby",".js",".css",".php",".xml",".json"]:
    if len(elem)<len(archivo):
     if archivo[-len(elem):]==".html":
      modo="htmlmixed"
      break
     elif archivo[-len(elem):]==".py" or archivo[-len(elem):]==".by" or archivo[-len(elem):]==".zby":
      modo="python"
      break
     elif archivo[-len(elem):]==".js":
      modo="javascript"
      
      break
     elif archivo[-len(elem):]==".css":
      modo="text/css"
      
      break
     elif archivo[-len(elem):]==".php":
      modo="php"
      
      break
     elif archivo[-len(elem):]==".xml":
      modo="xml"
      
      break
     elif archivo[-len(elem):]==".json":  
      modo="json"
      
      break
  
  def obtenerArchivo( data):
        
        archivo=data.split("\n")
        if len(s(".tab"))==1:
          k=0
        else:
          for k,elem in enumerate(s(".tab")):
            if not s(elem).hasClass("hidden"):
              break

        
        s(".path")[k].innerHTML=archivo[0]
        window.editores[k].getDoc().setValue("\n".join(archivo[1:]))
        window.editores[k].setOption("mode", modo)
  
  if list(normalizar(rest["kwargs"]))[0]=="Diseño":
    path="layout/"+path
    url=config.base_url+rest["app"]+"/"+rest["control"]+"/Show/"+path
    
    __pragma__("js","{}","""$.get(url).done(
      obtenerArchivo)""")
    
    
    
    
  elif list(rest["kwargs"])==["Controlador"]:
    #pendiente para incluir controles globales
    path="controlador/"+path
    __pragma__("js","{}","""$.get(url).done(
      obtenerArchivo)""")
    

  elif list(rest["kwargs"])==["Modelo"]:
    path="modelo/"+path
    __pragma__("js","{}","""$.get(url).done(
      obtenerArchivo)""")
    
  elif list(rest["kwargs"])==["Script"]:
    path="static/"+path
    __pragma__("js","{}","""$.get(url).done(
      obtenerArchivo)""")
    
  elif list(rest["kwargs"])==["Ajustes"]:
    path="ajustes/"+path
    
    __pragma__("js","{}","""$.get(url).done(
      obtenerArchivo)""")
    

  elif list(rest["kwargs"])==["Plugin"]:
    
    
    __pragma__("js","{}","""$.get(url).done(
      obtenerArchivo)""")
  
  if len(s(".tab"))==1 and s(".path")[0].innerText=="":
        k=0    

        s(".tab-btn")[0].innerText=evt.target.innerText
        if len(s("#guardar"))==0:
          s("#btns-action")[0].innerHTML+='<button class="bg-blue white" id="guardar">Guardar</button>'          
        s("#guardar")[0].parentNode.innerHTML+="<button id='borrar'>Borrar</button>"
        
  else:
        
        
        for elem in s(".tab"):
          s(elem).addClass("hidden")
          pass

        k=len(s(".tab"))
        s("#tabs-btn")[0].innerHTML+='<span style="padding:2px"><button class="tab-btn">'+evt.target.innerText+'</button><button class="close-btn">x</button></span>'
        if len(s(".tab"))>0:
          s("#content2")[0].children[len(s(".tab"))].innerHTML+='<div class="tab"><div class="path" style="overflow-x:scroll"></div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>'
        else:
          s("#content2")[0].children[0].innerHTML+='<div class="tab"><div class="path" style="overflow-x:scroll"></div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>'

        if s("#guardar")==[]:
          s("#btns-action")[0].innerHTML+='<button class="bg-blue white" id="guardar">Guardar</button>'
          
        
        if s("#borrar")==[]: 
          s("#guardar")[0].parentNode.innerHTML+="<button id='borrar'>Borrar</button>"

        update()    
  window.editores[k].getDoc().setValue("cargando...")
        
        

    

  


s(".fileclass").bind("click", seleccionar)




def cerrar( evt):
  s("#alert").addClass("hidden")
s("#alert-close").bind("click",cerrar  )
def crear( evt):
  s("#alert").removeClass("hidden")
s("#nuevo").bind("click",crear)

 
def _lambda( evt):
 if s("#treefiles").hasClass("hidden"):
  s("#treefiles").removeClass("hidden")
 else:
  s("#treefiles").addClass("hidden")
s("#titulo").bind("click",_lambda )
