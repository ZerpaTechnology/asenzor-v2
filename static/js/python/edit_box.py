#!/usr/bin/python
# -*- coding: utf-8 -*-
__pragma__("alias","s","$")

s("input[type='datetime']").datepicker()


VAR=nuclear.VAR
normalizar=nuclear.normalizar
doc=document
config=window.config


opciones=None
seccion=True
current_section=None
tablas=None
Tabla=None
rest=nuclear.getRest()

modelos=VAR("modelos")
tablas=VAR("Tablas")
opciones=VAR("opciones")
decode=Codificador.Codificador.decode

def thumbails(cadena,sujifo="_540x540"):
  return cadena[:cadena.rfind(".")]+sujifo+cadena[cadena.rfind("."):]


def cambiar(evt):
    out=evt.target
    valor=out.value
    imagen=""


    for k,option  in enumerate(s(out).find("option")):   
     if int(valor)==k:
      imagen=option.text

      break
    opcion=out.getAttribute("opcion")
    s(s(out.parent).find("img")[0]).removeClass("hidden")
    #if not s("input[type='file']")[0].files[0].name.endswith(".zip"):

    url=config.base_url+"/apps/"+rest["app"]+"/admin/static/archivos/"+("Imagenes" if s(out.parentNode).find("img")[0].getAttribute("archivos").strip()=="" else s(out.parentNode).find("img")[0].getAttribute("archivos").strip())+"/"
    

            
    __pragma__("js","{}","""$.get(url+thumbails(imagen)).done(function(){
      $(out.parentNode).find("img")[0].src=url+thumbails(imagen);
      }).fail(
      function(){
      $(out.parentNode).find("img")[0].src=url+imagen;
      }
      )""")


    

    

s(".img-admin").bind("change",cambiar)
componentes={"widget-campo-box":__pragma__("js","{}","$.get(config.base_url+settings.app+'/admin/Show/layout/admin/widgets/widget-campo-box.html/action=componer/')"),
       "widget-campo":__pragma__("js","{}","$.get(config.base_url+settings.app+'/admin/Show/layout/admin/widgets/widget-campo.html/action=componer/')"),
       "widget-campo-boxes":__pragma__("js","{}","$.get(config.base_url+settings.app+'/admin/Show/layout/admin/widgets/widget-campo-boxes.html/action=componer/')")
       }




      
      





def upload_image(evt):
    
    
    file = s(".img-file").prop('files')[0]

    reader =__new__(FileReader)()
    imagen=s(evt.target.parentNode).find("img")[0]
    def pasarImagen(imagen):
      def funcion(evt, img=imagen):
       s(img).removeClass("hidden")
       
       img.src=evt.target.result
      return funcion
    reader.onload = pasarImagen(imagen)
    f = reader.readAsDataURL(file)
   
#===============================================




def customOpen(evt):
 if s("#custom").hasClass("hidden"):
  global seccion
  seccion=True if evt.target.id=="#add" else False
  s("#custom").removeClass("hidden")


s("#add").bind("click",customOpen) 
s("#add2").bind("click",customOpen) 


def nuevaSeccion(evt):
 ultimo=0

 data={}
 data["opciones"]=opciones if opciones!=None else []
 data["tablas"]=tablas
 


 for k,elem in enumerate(s(".custom")):
  if len(elem.children)==0:
   if ultimo==None:
    ultimo=k
  else:
   ultimo=None
 """
 if componentes["widget-campo"]!=None and ultimo!=None:    
      s("#custom .tab")[0].children[ultimo].innerHTML=componentes["widget-campo"].run(data)
 """
 agregar=False
 for elem in s("#custom .tab")[0].children:
    if len(elem.children)>0:
      agregar=True

 if agregar==True and len(s(".botonera")[0].get(selector="#agregar"))==0:
    s(".botonera").widget(-1,"<button id='agregar'>Agregar</button>")
    
    def agregar(evt):
      ultimo=0
      global componentes
      global opciones
      global seccion
      

      data={"boxes":[]}
      
      l=[]
      for elem in s(".tab")[0].children:
          if len(elem.children)>0:
            widget=elem.children[0]
            tipo=s(widget).find("select[name=tipo]")[0].value
            name=s(widget).find("input[name=name]")[0].value
            valor=s(widget).find("input[name=value]")[0].value
            titulo=s(widget).find("input[name=titulo]")[0].value
            opcion=s(widget).find("select[name=opcion]")[0].value
            tabla=s(widget).find("select[name=tabla]")[0].value
            depende=s(widget).find("input[name=depende]")[0].value
            modelo=s(widget).find("select[name=opciones]")[0].value
            campo={titulo:tipo,"name":name,"value":valor}
            if opcion!="":
              campo["opcion"]=opcion
            if modelo!="":
              campo["opciones"]=modelo
            if tabla!="":
              campo["tabla"]=tabla
            if depende!="":
              campo["depende"]=depende
            if tipo=="number":
              campo["max"]=_max
              campo["min"]=_min
              campo["step"]=step
            l.append(campo)



      data["boxes"].append(l)
      for k,elem in enumerate(s(".custom-section" if seccion==True else ".custom-subsection").iterables):
        if len(elem.children)==0:
         if ultimo==None:
            ultimo=k
        else:
          ultimo=None
      for elem in s(".tab")[0].children:
        if len(elem.children)>0:
            temp=elem.children[0]
            elem.removeChild(temp)
      s("#custom").addClass("hidden")
      if componentes["widget-campo-boxes"]!=None and ultimo!=None:    

          s(".custom-section" if seccion==True else ".custom-subsection")[ultimo].innerHTML=componentes["widget-campo-boxes"].run(data)
          if len(s(".botoneraCustom")[0].get(selector="#borrarCustom"))==0:
            def borrarCustom(evt):
              for k,elem in enumerate(s(".custom-section" if seccion==True else ".custom-subsection").iterables):
                  if len(elem.children)==0:
                   if ultimo==None:
                      ultimo=k
                  else:
                    ultimo=None
              if ultimo!=None and ultimo!=0:
                for elem in s(".custom-section" if seccion==True else ".custom-subsection")[ultimo-1].children:
                  s(".custom-section" if seccion==True else ".custom-subsection")[ultimo-1].removeChild(elem)
                  if ultimo-1==0:
                    s(".botoneraCustom")[0].removeChild(s(".botoneraCustom")[0].find("#borrarCustom")[0])
            s(".botoneraCustom").widget(-1,'<a class="pad-05 b-r5 marg-t1 btn bg-ubuntu_red font-ubuntu white" style="text-decoration: none" href="#borrarCustom" id="borrarCustom">Borrar sección personalizada</a>')
            s("#borrarCustom")[0].bind("click",borrarCustom)
            

    s("#agregar").bind("click",agregar)
    
s(".insertar").bind("click",nuevaSeccion) 

#===============================================
def customClose(evt):
 evt.target._ev=customClose
 if s("#custom").hasClass("hidden"):
  s("#custom").removeClass("hidden")
 else:
  s("#custom").addClass("hidden")

 
s("#custom-close").bind("click",customClose)

s(".img-file").bind("change",upload_image)





def borrar(evt):
 evt.target._ev=borrar
 for elem in s("#custom .tab")[0].children:
  if len(elem.children[0].children)>0:
   if elem.children[0].children[0].children[0].checked==True:
    s(elem).removeChild(elem.children[0])
 agregar=False
 for elem in s("#custom .tab")[0].children:
    if len(elem.children)>0:
      agregar=True
 if agregar==False:
    el=s(".botonera").find(selector="#agregar")[0]
    s(".botonera")[0].removeChild(el)
   
s(".borrar").bind("click",borrar)



"""
def insertar(evt): 
 global componentes

 if evt.target.parent==s("#custom")[0]:
   ultimo=0
   for k,elem in enumerate(s("#custom")[0].children):
     if len(elem.children)==0:

       if ultimo==None:
         ultimo=k
     else:
       ultimo=None
   if ultimo!=None:    
     s(".tab")[1].children[ultimo].innerHTML=widgetCampo.run()

"""

def customOpen2(evt):
 if "hidden"  in s("#custom2")[0].class_name:
  global seccion
  global current_section
  seccion=True if evt.target.id=="#add" else False
  s("#custom2").removeClass("hidden")
  current_section=evt.target

s(".agregar-custom2").bind("click",customOpen2) 
def customClose2(evt):
 if s("#custom2").havClass("hidden"):
  s("#custom2").removeClass("hidden")
 else:
  s("#custom2").addClass("hidden")

 
s("#custom-close2").bind("click",customClose2)

def nuevoCampo(evt):
  global componentes
  global current_section
  campo={}
  widget=s("#custom2 .tab")[0].children[0]
  tipo=s(widget).find("select[name=tipo]")[0].value
  name=s(widget).find("input[name=name]")[0].value
  valor=s(widget).find("input[name=value]")[0].value
  titulo=s(widget).find("input[name=titulo]")[0].value
  opcion=s(widget).find("select[name=opcion]")[0].value
  tabla=s(widget).find("select[name=tabla]")[0].value
  depende=s(widget).find("input[name=depende]")[0].value
  modelo=s(widget).find("select[name=opciones]")[0].value

  campo={titulo:tipo,"name":name,"value":valor}
  if opcion!="":
    campo["opcion"]=int(opcion)
  if opcion!="":
    campo["opciones"]=modelo
  if tabla!="":
    campo["tabla"]=tabla
  if depende!="":
    campo["depende"]=depende
  if tipo=="number":
    campo["max"]=_max
    campo["min"]=_min
    campo["step"]=step
  data={"campo":campo}
  data["opciones"]=VAR("opciones")
  if current_section!=None:
    i=list(current_section.parent.children).index(current_section)
    data["indice"]=len(s(current_section.parentNode.children[i-1]).find("input[name^='custom:']"))+len(s(current_section.parentNode.children[i-1]).find("select[name^='custom:']"))
    s(current_section.parent.children[i-1]).widget(-1,componentes["widget-campo-box"].run(data))
    s(".img-admin").bind("change",cambiar)
  customClose2(evt)
"""
def modifica_atributo(evt):
  global config
  
  s("input[name='control']")[0].value=s("select[name='atributo-control']")[0].value
  s("input[name='layout']")[0].value=s("select[name='atributo-layout']")[0].value
  
  s("a[name='preview-enlace']")[0].href=config.base_url+rest["app"]+"/"+s("select[name='atributo-control']")[0].value+"/"+s("input[name='titulo']")[0].value
  s("a[name='preview-enlace']")[0].innerHTML=config.base_url+rest["app"]+"/"+s("select[name='atributo-control']")[0].value+"/"+s("input[name='titulo']")[0].value

s("select[name='atributo-control']").bind("change",modifica_atributo)
s("select[name='atributo-layout']").bind("change",modifica_atributo)
"""
def modificar_atributo():
  #req=ajax.ajax()
  
  meta={"control":s("select[name='atributo-control']")[0].value,
        "layout":s("select[name='atributo-layout']")[0].value}
  
  s("#form")[0].action=s("#form")[0].action+"&metadatos="+str(meta)
  titulos=VAR("titulos")
  titulos.remove(VAR("actual"))
  if s("input[name='titulo']")[0].value.strip()!="":
      if s("input[name='titulo']")[0].value in titulos:
          alert("Este titulo no esta permitido, ya existe")
          return False
      else:
          return True
          
  
          
      
        
    
  
window.modificar_atributo=modificar_atributo
s("#custom2 .agregar").bind("click",nuevoCampo)
