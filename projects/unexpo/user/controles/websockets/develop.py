
from browser import window, alert
s=window.s
Component=window.Component
componentes={}
componentes["widget-campo-boxes"]=Component("widget-campo-boxes",{},True)

def agregar(evt):
	ultimo=0
	global componentes

	data={"boxes":[]}
	l=[]
	for elem in s(".tab")[0].children:
	    if len(elem.children)>0:
	      widget=elem.children[0]
	      tipo=widget.get(selector="select[name=tipo]")[0].value
	      name=widget.get(selector="input[name=name]")[0].value
	      valor=widget.get(selector="input[name=value]")[0].value
	      titulo=widget.get(selector="input[name=titulo]")[0].value
	      opcion=widget.get(selector="select[name=opcion]")[0].value
	      tabla=widget.get(selector="select[name=tabla]")[0].value
	      depende=widget.get(selector="select[name=depende]")[0].value
	      campo={titulo:tipo,"name":name,"value":valor}
	      if opcion!="":
	      	campo["opcion"]=opcion
	      if tabla!="":
	      	campo["tabla"]=tabla
	      if depende!="":
	      	campo["depende"]=depende
	      l.append(campo)

	data["boxes"].append(l)
	for k,elem in enumerate(s(".custom-section").iterables):
	  if len(elem.children)==0:
	   if ultimo==None:
	    	ultimo=k
	  else:
	   	ultimo=None
	alert(componentes["widget-campo-boxes"].run(data))
	if componentes["widget-campo-boxes"]!=None and ultimo!=None:    
   		s(".custom-section")[ultimo].innerHTML=componentes["widget-campo-boxes"].run(data)



s("#agregar").bind("click",agregar)