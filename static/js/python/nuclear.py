#!/usr/bin/python
# -*- coding: utf-8 -*-
#no modificar con codemirror
import re
"""
>>> re.findall(re.compile("[for]\s(\w+)\s[in]"),"for hola in ")
['hola']

"""
list=py_datos.list
type=py_datos.py_metatype


__pragma__("alias","None","null")
__pragma__("alias","False","false")
__pragma__("alias","True","true")
__pragma__("alias","s","$")


def thumbail(img,sufijo="_540x540"):
  return img[:img.rfind(".")]+sufijo+img[img.rfind("."):]

def defaultValues():
  return [[None],[]]

def defaultEvents():
  eventos=[[["click", [] ],
           ["mouseenter",[]],
           ["mouseleave",[]],
           ["mouseover",[]],
           ["mouseout",[]],
           ["mousemove",[]],
           ["mousedown",[]],
           ["mouseup",[]],
           ["dblclick",[]],
           ["keypress",[]],
           ["keydonw",[]],
           ["keyup",[]],
           ["input",[]],
           ["blur",[]],
           ["focus",[]],
           ["drag",[]],
           ["dragend",[]],
           ["dragenter",[]],
           ["dragleave",[]],
           ["dragover",[]],
           ["dragstart",[]],
           ["drop",[]],
          ],[]]
  return eventos

def getEvents(elemento):#[ [[evt,[funciones]],[evt,[funciones]]] , [hijos] ]      lista=[]
      hijos=[]
      lista=[]
      eventos=["click","mouseenter","mouseleave","mouseover","mouseout","mousemove","mousedown","mouseup","dblclick","keypress","keydonw","keyup","input","blur","focus","drag","dragend","dragenter","dragleave","dragover","dragstart","drop"]
  
      if len(elemento.children)>0:
        for elem in elemento.children:
          hijos+=[getEvents(elem)]
          

      for elem in eventos:
        lista+=[[elem,elemento.events(elem)]]
      
      return [lista,hijos]
def getValues(elemento):#[ [[evt,[funciones]],[evt,[funciones]]] , [hijos] ]
      
      if "value" in dir(elemento):
        lista=[elemento.value]
      else:
        lista=[None]
      hijos=[]
      
      if len(elemento.children)>0:
        for elem in elemento.children:
          hijos+=[getValues(elem)]
          

      
      return [lista,hijos]

def updateEvent(listaEvent,padre):
      if type(listaEvent[0][0])==str:
        eventos=listaEvent[0][0]
        for k, eventolist in enumerate(eventos):
          if len(eventolist)>0:
          
            if eventolist!=None and type(eventolist)==list and type(eventolist[0])==str:
                  for funcion in eventolist[1]:
                    padre.bind(eventolist[0],funcion)

      else:
        eventos=listaEvent[0]
        
        for k, eventolist in enumerate(eventos):
          if len(eventolist)>0:
            if eventolist!=None and type(eventolist)==list:
              for funcion in eventolist[1]:
                    padre.bind(eventolist[0],funcion)


      hijos=listaEvent[1]
      c=0
      
        
          
          
   
      for k,hijo in enumerate(hijos):
        
        if hijo!=None and len(padre.children)>0:
          
          updateEvent(hijo,padre.children[k])
      
      
def updateValues(listaValues,padre):

  values=listaValues[0]
  hijos=listaValues[1]
  for k, valor in enumerate(values):
    if valor!=None:
      padre.value=valor
  for k,hijo in enumerate(hijos):
    if hijo!=None:
      updateValues(hijo,padre.children[k])





def zjoin(lista,sep):
  c=""
  for elem in lista:

    c+=str(elem)+sep
  return c[:-1]

def normalizar(v):
    decode=Codificador.Codificador.decode
    __pragma__("alias","None","null")
    __pragma__("alias","False","false")
    __pragma__("alias","True","true")

    def dicccionar(json):
      l=[]
      #for (var elem in json) {
      #for elem in json:
      if json!=None:
        
        for k,elem in enumerate(__pragma__("js","{}","Object.keys(json)")):
          
         

          
          l.append([elem,json[elem] if type(json[elem] )!=dict and type(json[elem] )!=object else dicccionar(json[elem]) ])
          
      
      return dict(l)


    if type(v)==str  and v not in list(globals()):

        if ";" not in v:

            try:
                v=decode(v.strip())
                if v not in globals():

                
                  window.eval("False=false;True=true;None=null;a="+v)

              
                  if typeof(a)=="object" and not v.strip().startswith("[") and not v.strip().endswith("]"):
                    
                    return dicccionar(a)
                  else:
                    
                      return a
                else:
                    return v
            except:
              
             
              return v
        else:
            
            return v
    else:
        
        return v

def getCookie():
  cookies={}
  for elem in document.cookie.split(";"):
    if "=" in elem:                
        k,v=elem.split("=")
        cookies[k.strip()]=normalizar(v)
  return cookies
def getRest(): 
    
    config=Config.Config()
    decode=Codificador.Codificador.decode
    
    url=decode(window.location.href)[len(config.base_url):].split("#")
    gato=None
    if len(url)==2:
        gato=url[1]
    url=url[0].split("/")
    if "" in url:
        url.remove("")



    pos=["app","control","metodo","args","kwargs"]
    rest={"app":None,"control":None,"metodo":None,"args":[],"kwargs":{},"action":None,"manager":False,"request":{},"#":None}

    def identificar(elem,rest,pos):
        
        if "=" not in elem and "{" not in elem and "}" not in elem:
            if len(pos)>0:
                if pos[0]=="app":
                    if elem in config.apps:

                        rest["app"]=normalizar(elem)

                    pos.remove("app")
                elif pos[0]=="control":
                    rest["control"]=normalizar(elem)
                    pos.remove("control")
                elif pos[0]=="metodo":
                    rest["metodo"]=normalizar(elem)
                    pos.remove("metodo")
                elif pos[0]=="args":
                    rest["args"].append(normalizar(elem))
                    
                elif pos[0]=="kwargs":
                    pos.remove("kwargs")
            
        elif "="  in elem:
            if len(pos)>0:
                if pos[0]=="app":
                    pos.remove("app")
                elif pos[0]=="control":
                    pos.remove("control")
                elif pos[0]=="metodo":
                    pos.remove("metodo")
                elif pos[0]=="args":
                    pos.remove("args")
                elif pos[0]=="kwargs":
                    pos.remove("kwargs")
            
            for item in elem.split("&"):
                k,v=item.split("=")
                rest[k]=normalizar(v)
            
        elif "{" in elem and "}" in elem:
            if len(pos)>0:
                if pos[0]=="app":
                    pos.remove("app")
                elif pos[0]=="control":
                    pos.remove("control")
                elif pos[0]=="metodo":
                    pos.remove("metodo")
                elif pos[0]=="args":
                    pos.remove("args")
                elif pos[0]=="kwargs":
                  pos.remove("kwargs")
                rest["kwargs"]=normalizar(elem)
                
    for elem in url:
        
        identificar(elem,rest,pos)
    if gato!=None:
      rest["#"]=gato
    if rest["app"]==None:
      rest["app"]=config.default_app


    return rest
class Component:
  def __init__(self,url,data={},admin=True,isglobal=True,offline=False):
      widget=""
      data=str(data)
      self.admin=admin
      self.isglobal=isglobal
      if offline==False:
        self.update(data)
      else:


        if isglobal:

          __pragma__("js","{}","""
          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/global/widgets/'+url+'.html/action=componer/',
                  
                  async:false,
                  
                  success:  function(respuesta){
                            widget=respuesta;
                        },
                  error : function(objXMLHttpRequest) {
                    console.log("error1",objXMLHttpRequest);
                    }
                  })
          """)
          
        elif admin:
          __pragma__("js","{}","""
          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/admin/widgets/'+url+'.html/action=componer/',
             
                  async:false,
                  

                  success:  function(respuesta){
                            widget=respuesta;
                        },
                  error : function(objXMLHttpRequest) {
                    console.log("error2",objXMLHttpRequest);
                    }
                  })
          """)
          
        else:
          __pragma__("js","{}","""
          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/user/widgets/'+url+'.html/action=componer/',
                  
                  async:false,
                  
                  success:  function(respuesta){
                            widget=respuesta;
                        },
                error : function(objXMLHttpRequest) {
                console.log("error3",objXMLHttpRequest);
                }

                  })
                
          """) 
        
        lineas=widget.split("\n")
        from zu import getTab
        AnteriorIdentacion=""
        abierta=False
        
        for k,elem in enumerate(lineas):
          
          identacion=getTab(elem)

          if "#" in elem:
            if "=" in elem and (elem[elem.find("=")-1]!="=" 
                                and elem[elem.find("=")-1]!="<" 
                                and elem[elem.find("=")-1]!=">" 
                                and elem[elem.find("=")-1]!="!"):
              c=elem.find("=")
              while c>0:
                if elem[c]=="\t" or elem[c]==" ":

                  break

                c-=1
              
              lineas[k]=elem[:c]+"var "+elem[c:]

            lineas[k]=lineas[k].replace("#",";//")
            
            elem=lineas[k]
          if "except Exception as e:" in elem:
            lineas[k]=elem.replace("except Exception as e:","}catch(e){")
            if lineas[k].strip().endswith("}catch(e){"):
              abierta=True
            else:
              lineas[k]+=";}"
              elem=lineas[k]
              abierta=False
            
          elif "try:" in elem:
            lineas[k]=elem.replace("try:","try{")
            elem=lineas[k]+("" if lineas[k].endswith("try{") else ";")
            abierta=True
          elif "'''" in elem:
            lineas[k]=elem.replace("'''","`")
            elem=lineas[k]+";"

          elif '"""' in elem:
            lineas[k]=elem.replace('"""',"`")
            elem=lineas[k]+";"
          elif "elif " in elem and ":" in elem:
            lineas[k]=elem.replace("elif ","}else if(").replace(":","){")
            elem=lineas[k]
            abierta=True
          elif "if " in elem and ":" in elem:
            lineas[k]=elem.replace("if ","if(").replace(":","){")
            elem=lineas[k]
            abierta=True

          elif "else" in elem and ":" in elem:
            lineas[k]=elem.replace("else","}else").replace(":","{")
            elem=lineas[k]
            abierta=True
          
          elif "=" in elem and (elem[elem.find("=")-1]!="+" 
                                and elem[elem.find("=")-1]!="=" 
                                and elem[elem.find("=")-1]!="<" 
                                and elem[elem.find("=")-1]!=">" 
                                and elem[elem.find("=")-1]!="!" 
                                and "//" not in elem 
                                ) and elem[elem.find("=")+1]!="=":
            c=elem.find("=")-1
            while c>0:
              if elem[c]=="\t" or elem[c]==" ":
                lineas[k]=elem[:c+1]+"var "+elem[c+1:]+";"
                break
              c-=1
          elif "while " in elem and ":" in elem:
            lineas[k]=elem.replace("while ","while(").replace(":","){")
            elem=lineas[k]
          elif "for " in elem and ":" in elem :
            des="(\w+)\s*(?:,(\s*\w+))?"
            _iter="((?:\w+)?(?:\(?\[[A-Za-z0-9_,\-'\"]+?\]\)?)?)"
            patron1=re.compile("for\s+"+des+"\s*in\s+"+_iter+":")
            descompresion=patron1.findall(lineas[k])[0]
            #lista

            #dict
            cond2="}else{"
            i=lineas[k].find("for ")
            
            print(descompresion)
            if len(descompresion)>2 and descompresion[1]!="" and descompresion[1]!=None:
              f=lineas[k].find(":",lineas[k].find(descompresion[2]))
              cond1="if (str("+descompresion[2]+").strip()[0]=='[' && str("+descompresion[2]+").strip().slice(-1)==']'){"
              iterable="var "+descompresion[1]+"="+descompresion[2]+"["+descompresion[0]+"][1];"
              iterable2="var "+descompresion[1]+"= Object.keys("+descompresion[2]+")["+descompresion[0]+"];"


              bucle="for (var "+descompresion[0]+" = 0; "+descompresion[0]+" < Object.keys("+descompresion[2]+").length; "+descompresion[0]+"++) {"



              
              lineas[k]=lineas[k][:i]+bucle+cond1+iterable+cond2+iterable2+"}"+lineas[k][f+1:]

              
            else:
              f=lineas[k].find(":",lineas[k].find(descompresion[2]))
              cond1="if (str("+descompresion[2]+").strip()[0]=='[' && str("+descompresion[2]+").strip().slice(-1)==']'){"
              bucle="for (var _k = 0; _k < Object.keys("+descompresion[2]+").length; _k++){/**/"
              iterable="var "+descompresion[0]+"="+descompresion[2]+"[_k];"
              iterable2="var "+descompresion[0]+"= Object.keys("+descompresion[2]+")[_k];"
              lineas[k]=lineas[k][:i]+bucle+cond1+iterable+cond2+iterable2+"}"+lineas[k][f+1:]

          elif "try:" in elem:
            lineas[k]=elem.replace("try:","try{")
            elem=lineas[k]
            abierta=True

          elif "pass" in elem:
            lineas[k]=elem.replace("pass","}//pass")
            elem=lineas[k]
            abierta=False
          elif lineas[k].strip()!="":
            lineas[k]+=";"
          elif len(AnteriorIdentacion)>len(identacion) and  abierta==True:
            if "}" not in lineas[k]:
              lineas[k]+="}"


          if not lineas[k].strip().endswith("{") and not lineas[k].strip().endswith("}") and not lineas[k].strip().endswith(";") and lineas[k].strip()!="":
            lineas[k]+=";"
            elem=lineas[k]
          if " if " in elem and " else " in elem:
            if elem.find("=")>elem.find(" if "):

              
              codigo=elem[len("str("):-1]
              
              valor1=codigo[:codigo.find(" if ")-len(" if ")]

              condicion=codigo[codigo.find(" if "):codigo.find(" else ")-len(" else ")]
              valor2=codigo[codigo.find(" else "):]

              lineas[k]=variable+"str("+condicion+"?"+valor1+":"+valor2+");"
            else:
              variable=elem[:elem.find("str(")]
              
              

              codigo=elem[elem.find("str(")+len("str("):]
              i=elem.rfind("(",elem.find(" if "))
              f=elem.find(")",elem.find(" else "))
              bloque=elem[i+1:f]
              
              

              valor1=bloque[:bloque.find(" if ")]
              condicion=bloque[bloque.find(" if ")+len(" if "):bloque.find(" else ")]
              valor2=bloque[bloque.find(" else ")+len(" else "):]

       


              lineas[k]=variable+"str(("+condicion+")?"+valor1+":"+valor2+");"              

          
        widget="\n".join(lineas)
        
        self.widget=widget
            
      return widget
  def run(self,data={}):
    doc=""
    
    decode=Codificador.Codificador.decode
    try:
      eval(self.widget)
    except:
      print(__except0__)
    
    return doc
  def update(self,data={}):
        if self.isglobal:

          __pragma__("js","{}","""
          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/global/widgets/'+self.url+'.html/action=compuesto/'+data,
                  async:false,
                  success:  function(respuesta){
                            self.widget=respuesta;
                        },
                  error : function(objXMLHttpRequest) {
                    console.log("error1",objXMLHttpRequest);
                    }
                  })
          """)
          
        elif self.admin:
          __pragma__("js","{}","""
          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/admin/widgets/'+self.url+'.html/action=compuesto/'+data,
                  async:false,
                  success:  function(respuesta){
                            self.widget=respuesta;
                        },
                  error : function(objXMLHttpRequest) {
                    console.log("error2",objXMLHttpRequest);
                    }
                  })
          """)
          
        else:
          __pragma__("js","{}","""
          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/user/widgets/'+self.url+'.html/action=compuesto/'+data,
                  async:false,
                  success:  function(respuesta){
                            self.widget=respuesta;
                        },
                error : function(objXMLHttpRequest) {
                console.log("error3",objXMLHttpRequest);
                }

                  })
          """)  
        return self.widget    

def VAR(nombre):

  
  try:

    return normalizar(s("var[name='"+nombre+"']")[0].innerText)
  except:
    print("No se pudo encontrar la varible html: "+nombre)
    print(__except0__)

class Settings:
  """docstring for Config"""
  def __init__(self):
    
    rest=getRest()
    self.app=rest["app"]

window.settings=Settings()
window.rest=getRest()
