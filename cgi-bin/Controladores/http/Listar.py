# -*- coding: utf-8 -*-
from modulos.controlador import Controlador

from settings import config as settings
from config import config

class Listar(Controlador):
	def __init__(self,data):
		Controlador.__init__(self,data)
		
		self.data["vars"]["table-headers"]=["Nombre","Ultima modificación","Descripción"]
		self.data["vars"]["pag"]=1
		
	def Listar(self):
		from modulos.ztec.zred import listar,listarAjax
		modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
		tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]
		if self.data["ajax"]==False:
			if self.data["action"]=="listar":
				listar(self.data,config)
				self.servir()

			elif self.data["action"]=="editar":
				self.servir()
		else:
			if self.data["action"]=="eliminar":
				self.Eliminar()
			elif self.data["action"]=="listar":
				self.HEADERS.set_headers({"Content-type":"text/plain"})
				self.HEADERS.show()
				print self.data["model"][modelos[self.data["metodo"]] if self.data["metodo"] in modelos else self.data["metodo"]].obtenerFilas(self.data["metodo"])
	def Eliminar(self):
	        l=[]
	        from modulos.ztec.zred import normalizar
	        self.HEADERS.set_headers({"Content-type":"text/plain"})
	        self.HEADERS.show()


	        
	        for elem in self.data["marcados"]:
	          l.append(elem)
	        modelos=self.data["model"]["main"].obtenerFilas('Tablas,args>Modelos')[0][0]
	        tablas=self.data["model"]["main"].obtenerFilas('args>Tablas')[0][0]
	        
	        for c,elem in enumerate(self.data["marcados"]):
	          
	          
	          
	          
	          while c<len(l):
	            if normalizar(l[c])==True:

	              self.data["model"][modelos[self.data["metodo"]]].eliminar(c,tablas[self.data["metodo"]] if self.data["metodo"] in tablas else self.data["metodo"] )
	              del l[c]
	
	              c=0
	            else:
	              c+=1
	        
	        
	        data={}
	        
	        lista=self.data["model"][modelos[self.data["metodo"]] if self.data["metodo"] in modelos else self.data["metodo"]].obtenerFilas(self.data["metodo"])
	        for k,elem in enumerate(lista):
	          del lista[k][1]
	        data["listar"]=lista
	        data["ajax-data"]=str({"action":"listar","args":self.data["args"],"pag-action":None})
	        data["baseAction"]="app="+settings.app+"&admin=True&vista=index&args="+str(self.data["args"])
	        data["titulo"]=self.data["metodo"]
	        data["filtrar"]=["Todas las fechas","Septiembre 2014"]
	        data["addNew"]='Añadir nuevo'
	        data["n-pag"]=5
	        data['campos']=["Titulo","Fecha"]
	        data['app']=settings.app
	        data['vista']="index"
	        data["action"]=self.data["action"]
	        
	        data["beforeAction"]="listar"
	        data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}
	        print data
	
			
	
	
	