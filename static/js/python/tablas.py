#!/usr/bin/python
# -*- coding: utf-8 -*-



__pragma__("alias","s","$")
VAR=nuclear.VAR
config=window.config
normalizar=nuclear.normalizar
zjoin=nuclear.zjoin
rest=window.rest
Component=nuclear.Component

data=s.extend({},rest)
data["ajax-data"]=VAR("ajax-data")
data["baseAction"]=VAR("baseAction")
data["titulo"]=VAR("titulo")
data["filtrar"]=VAR("filtrar")
data["acciones"]=VAR("acciones")
data["addNew"]=VAR("addNew")
data["n-pag"]=VAR("n-pag")
data["table-headers"]=VAR("table-headers")
data["pag"]=VAR("pag")
data["status"]=VAR("status")
data["filtros"]=VAR("filtros")
data["keyNew"]=VAR("keyNew")
data["campos"]=VAR("campos")
doc=""
print(data["table-headers"])

tabla=s("#tabla-1")





pag=1

status="Todos"
respuesta=""	


def update_tabla(pag):
	tabla=document["tabla-1"]
	
	tabla.clear()	

	
	#pendiente para control de estatus
	
	"""
	cabecera=html.TR(html.TD(html.INPUT(type="checkbox",Class="marg-l05")))
	
	for campo in data["campos"]:
		cabecera<=html.TH(decode(campo))
	tabla<=cabecera
	#tabla<=html.TR(html.TD( Class="pad-1")+html.TD(data["campo1"], Class="pad-1")+html.TD(data["campo2"]),Class="pad-05")
	
	for k,fila in enumerate(__lista__[data["n-pag"]*(pag-1):data["n-pag"]*(pag)]):
		
		tabla<=html.TR(html.TH(html.INPUT(type="checkbox"), Class="pad-05")+html.TD(html.A(decode(fila[0]),href=urlBuilder(config,data["app"],"admin","",list(fila[1])[0],fila[1][list(fila[1])[0]],action="editar")), Class="pad-05")+html.TD(fila[2], Class="pad-05"))
	for elem in document.get(selector=".n-pag"):
		elem.innerHTML="de "+str(int(len(__lista__)/data["n-pag"])+1)
	"""



#__lista__=[]







#Pide los elementos a paginar
#req=ajax.ajax()
#req.open("POST",config.base_url,True)
#req.set_header('content-type','application/x-www-form-urlencoded')
#pasar una lista causa que se pasen los valores individuales en campos de un mismo nombre igual como ocurriria al usar varios campos con igual name
#ejem args ["hola","mundo"]
#MiniFieldStorage("args","hola") MiniFieldStorage("args","mundo")
#para convertirlo usare str
#req.send({"action":"listar","app":rest["app"],"metodo":rest["metodo"],"control":rest["control"],"ajax":True})	

"""
def complete(evt,req=req):
    
	try:
	    
		
		global pag
		global data
		global __lista__
		
		exec(req.text)

		
		__lista__=copy.copy(data["listar"])
		
		update_tabla(pag)
		for elem in document.get(selector=".table-pag"):
			if pag!=int(elem.value):
				elem.value=pag
		
	except Exception as e:
		print("Error en tablas.by")
		print(e.args)
		print(req.text)
		alert(req.text)
	
"""
#req.bind("complete",complete)
def paginar(x,y):
  
  a=float(x)/float(y)
  if a>int(a):
    return int(a)+1
  else:
    return int(a)




	



	



	

opciones=[]
action_current=[0]



		
	



	



class Tabla(object):
	"""docstring for Tabla"""
	def __init__(self,selector,pag=1,paginacion=5):
		self.selector=selector
		self.lista=VAR("listar")
		
		print(self.lista[0])
		self.listaTemp=s.extend([],self.lista)
		self.pag=pag
		self.paginacion=paginacion

		self.contenido=Component("tabla-contenido",data,True,True,True)
		
		self.btns_aplicar=s(self.selector).find(".btn-aplicar").bind("click",self.checkear)
		s(self.selector).find(".link-status").bind("click",self.filtrar)
		s(self.selector).find(".table-firt").bind("click",self.goFirst)
		s(self.selector).find(".table-next").bind("click",self.goNext)
		s(self.selector).find(".table-back").bind("click",self.goBack)
		s(self.selector).find(".table-last").bind("click",self.goLast)
		s(self.selector).find(".table-actions").bind("change",self.accionar)
		s(self.selector).find("input[name='table-search']").bind("keyup",self.search)

		for tabla in s(self.selector).find(".content")[0].children:
			
			for th in list(tabla.children[0].children[0].children):

				s(th.children[0].children[0]).bind("click",self.marcar)

	def accionar(self,ev):
		
		global action_current
		
		rank=list(data["acciones"].keys()).index(ev.target.value)
		if rank==0:
			self.marcar()
		else:
			key=list(data["acciones"].keys())[list(data["acciones"].keys()).index(ev.target.value)]
			
			action_current=[data["acciones"][key]]

	def marcar(self,evt=None):
		if evt==None:
			for tabla in s(self.selector).find(".content")[0].children:
					if "hidden" not in tabla.class_name:
						tabla=tabla.children[0]
						for tr in list(tabla.children[0].children)[1:]:
							tr.children[0].children[0].checked=True
		else:
			if evt.target.checked==True:
				for tabla in s(self.selector).find(".content")[0].children:
					if "hidden" not in tabla.class_name:
						tabla=tabla.children[0]
						for tr in list(tabla.children[0].children)[1:]:
							tr.children[0].children[0].checked=True
			else:
				for tabla in s(self.selector).find(".content")[0].children:
					if "hidden" not in tabla.class_name:
						tabla=tabla.children[0]
						for tr in list(tabla.children[0].children)[1:]:
							tr.children[0].children[0].checked=False


	def goBack(self,evt):
		
			if self.pag >1:
				s(s(self.selector).find(".content")[0].children[self.pag-1]).addClass("hidden")
				self.pag-=1
				s(s(self.selector).find(".content")[0].children[self.pag-1]).removeClass("hidden")
				self.update_indice()

	def update_indice(self):
		for elem in s(self.selector).find("input[name='table-indice']"):
			elem.value=self.pag
		for elem in s(self.selector).find("span[name='from-indice']"):

			elem.text=str(len(self.listaTemp)//self.paginacion+1)

	def update_tabla(self):
		global data
		
		decode=Codificador.Codificador.decode
		
		
		data["listar"]=self.listaTemp
		
		s(self.selector).find(".content")[0].outerHTML=self.contenido.run(data)
		self.pag=1
		self.update_indice()
		for tabla in s(self.selector).find(".content")[0].children:
			for th in list(tabla.children[0].children[0].children):
					s(th.children[0].children[0]).bind("click",self.marcar)

	def goLast(self,evt):
			
			if self.pag<paginar(len(self.listaTemp),self.paginacion):
				
				s(s(self.selector).find(".content")[0].children[self.pag-1]).addClass("hidden")
				self.pag=paginar(len(self.listaTemp),self.paginacion)
				
				s(s(self.selector).find(".content")[0].children[self.pag-1]).removeClass("hidden")

				self.update_indice()

	def goNext(self,evt):

			if self.pag<(len(self.listaTemp)/self.paginacion):
				
				s(s(self.selector).find(".content")[0].children[self.pag-1]).addClass("hidden")
				self.pag+=1
				s(s(self.selector).find(".content")[0].children[self.pag-1]).removeClass("hidden")
				self.update_indice()


	def goFirst(self,evt):
		if self.pag >1:
				s(s(self.selector).find(".content")[0].children[self.pag-1]).addClass("hidden")
				self.pag=1
				s(s(self.selector).find(".content")[0].children[0]).removeClass("hidden")
				self.update_indice()
		
	def filtrar(self,evt):
		evt.preventDefault()
		status=evt.target.text
		self.update_tabla()
	def checkear(self,evt):
		c=0
		opciones=[]
		enlaces=[]
		pag=int(s("input[name='table-indice']")[0].value)
		for tabla in s(self.selector).find(".content")[0].children:
			tabla=tabla.children[0]
		
			for tr in list(tabla.children[0].children)[1:]:
				opciones.append(tr.children[0].children[0].checked)
				if tr.children[0].children[0].checked==True:
					enlaces.append(tr.children[1].children[0].href)
				else:
					enlaces.append(None)


		
		
		
		
		req.set_header('content-type','application/x-www-form-urlencoded')
		if action_current[0]!="editar":#osea papelera
			pass
			s.ajax({"url":config.base_url,
				"data":{"marcados":opciones,"action":action_current[0],"metodo":rest["metodo"],"app":rest["app"],"control":rest["control"],"ajax":True},
				"method":"POST",
				"type":"POST",
				"contentType":False,
				"processData":False,
			})
			def obtenerLista(data):
				self.listar=normalizar(data)
			s.post(config.base_url+rest["app"]+"/"+rest["control"]+"/"+rest["metodo"]+"/action=listar&ajax=True/").done(obtenerLista)
			
			
			self.listaTemp=s.extend([],self.lista)
			self.update_tabla()

		else:
			for k,opcion in enumerate(opciones):
				if opcion==True:
					window.open(enlaces[k])
						
		
		

		

		
	def search(self,evt):
	
		
		if evt.target.value!="":
			c=0
			self.listaTemp=s.extend([],self.lista)
			for elem in self.lista:
				if evt.target.value.lower() not in elem[0].lower():
					self.listaTemp.remove(elem)
					c+=1
		else:

			self.listaTemp=s.extend([],self.lista)
		for elem in s(self.selector).find(".table-pag"):
			elem.value=1
		
		self.update_tabla()
		
		
		
window.Tabla=Tabla
