#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from ztec.zmodel import Model
import sys
import os
import datetime
import ztec.zu as zu
sys.path.append("../")
import settings
try:
	import config.config as config
except:
	import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo


		def crearPlantilla(self,nombre,campos):
			if self.request():
				tabla="Plantillas"
				i=len(self.obtenerFilas(tabla))
				self.db(tabla).insertar(nombre,
					campos,
					{"Plantilla":i},
					zu.DateTime(),
					["Publicada"]
					)
				return self.grabar()
		def modificarPlantilla(self,i,nombre,campos):
			if self.request():
				tabla="Plantillas"
				self.db(tabla).modificarCampo(i,"Nombre",nombre)
				self.db(tabla).modificarCampo(i,"Contenido",campos)
				self.db(tabla).modificarCampo(i,"Fecha",zu.DateTime())
				return self.grabar()

		def crearFormulario(self,data):
			if self.request():
				select=True
				l2=list(data)
				l2.sort()
				l2.remove("action")
				#Pendiente de que los nombres de los campos no deben repetirse
				
				for k,elem in enumerate(self.obtenerFilas("Plantillas")):
					campos=[]
					plantilla=k
					
					c=0
					try:
						l=[]
						for box in elem[1]:
							for campo in box:	
								
								tmp=list(campo)
								tmp.remove("name") if "name" in tmp else tmp
								tmp.remove("value") if "value" in tmp else tmp
								tmp.remove("step") if "step" in tmp else tmp
								tmp.remove("opcion") if "opcion" in tmp else tmp
								tmp.remove("requerido") if "requerido" in tmp else tmp
								tmp.remove("tabla") if "tabla" in tmp else tmp
								tmp.remove("depende") if "depende" in tmp else tmp
								tmp.remove("categoria") if "categoria" in tmp else tmp
								tmp.remove("descripcion") if "descripcion" in tmp else tmp
								tmp.remove("padre") if "padre" in tmp else tmp
						
								tipo=campo[tmp[0]]
								l.append(campo["name"])
								
						l.sort()
						
						
						for campo in l:
							if l2[c]!=campo:
								select=False
							c+=1
						if select==True:
							break
							
						
					except:
						pass
					
				
				
				c=0
				boxes=[]	

				for k2,box in enumerate(self.obtenerFilas("Plantillas")[plantilla][1]):
					for k,campo in enumerate(box):
						indice=l2.index(campo["name"])
						if k2==0 and k==1:
							titulo=data[l2[indice]].value
						else:

							if "opcion" in campo and data[l2[indice]].value!="":
								box[k]["value"]=int(data[l2[indice]].value)
							else:
								box[k]["value"]=data[l2[indice]].value
						c+=1
					boxes.append(box)
				i=len(self.obtenerFilas("Formularios"))
				
				self.db("Formularios").insertar(titulo,boxes,{"Formulario":i},zu.DateTime(),[])
				self.grabar()
		def registrarFormulario(self,data):
			if self.request():
				select=True

				l2=list(data)
				l2.sort()
				
				tabla,ide=data["action"].value.split(":")
				l2.remove("action")
				#Pendiente de que los nombres de los campos no deben repetirse
				l=[]
				for elem in l2:
					l.append(data[elem].value)
				c=0
				boxes=[]	
				i=len(self.obtenerFilas(tabla))
				opciones=self.obtenerFilas("Opciones")

				import config.config as config
				import settings.config as settings
				from ztec.zred import urlBuilder
				
				
				mensaje="<p>Un visitante a llenado el formulario de contacto puedes verlo en <a href='"+urlBuilder(config,settings.app,"admin","index","PostdeFormulario",i,action="editar")+"'>visitando tu sitio</a> o mendiante este email:</p>"

				for k2,box in enumerate(self.obtenerFilas("Formularios")[int(ide)][1]):

					for k,campo in enumerate(box):
						
						if k2==0 and k==1:
							titulo=campo["value"]+" "+str(i+1)
						else:
							
							tmp=list(campo)
							tmp.remove("name") if "name" in tmp else tmp
							tmp.remove("value") if "value" in tmp else tmp
							tmp.remove("step") if "step" in tmp else tmp
							tmp.remove("opcion") if "opcion" in tmp else tmp
							tmp.remove("requerido") if "requerido" in tmp else tmp
							tmp.remove("tabla") if "tabla" in tmp else tmp
							tmp.remove("depende") if "depende" in tmp else tmp
							tmp.remove("categoria") if "captegoria" in tmp else tmp
							tmp.remove("descripcion") if "descripcion" in tmp else tmp
							tmp.remove("padre") if "padre" in tmp else tmp
							tmp.remove("opciones") if "opciones" in tmp else tmp
							
							tmp=tmp[0]

							

							if campo[tmp]!="text-admin" and campo[tmp]!="img-admin" and campo[tmp]!="select-admin" :
								indice=campo["name"]
								
								if "opcion" in campo:
									

									
									mensaje+=tmp+"<br> &nbsp; &nbsp;"+opciones[int(campo["opcion"])][1][int(data[indice].value)]+"<br><br>"
									box[k]["value"]=int(data[indice].value)

								elif campo[tmp]=="number":
									mensaje+=tmp+"<br>  &nbsp; &nbsp;"+data[indice].value+"<br><br>"
									box[k]["value"]=int(data[indice].value)
									
								else:

									mensaje+=tmp+"<br>  &nbsp; &nbsp;"+data[indice].value+"<br><br>"
									box[k]["value"]=data[indice].value
						c+=1
					boxes.append(box)
				
				from ztec.zred import sendEmail	
				
				#sendEmail("office@marquisrentalapartments.com","office@marquisrentalapartments.com","password",mensaje)
				boxes.insert(0,{"Formulario":"hidden-id","name":"id","value":ide})
				self.db(tabla).insertar(titulo,boxes,{tabla:i},zu.DateTime(),[])
				self.grabar()

		def filtrar(self,status,tabla=None):
			#status=["activo"] todos los que tenga activo
			#status=["activo","aprobado"] todos los que tengan activo y aprodado no uno solo
			
			if self.update():	
				l2=[]

				if tabla!=None and type(tabla)!=str:
					l=tabla
				elif type(tabla)==str:
					l=self.obtenerFilas(tabla)
				else:
					l=self.obtenerFilas(self.db.seleccion)

				for k,fila in enumerate(l):
					if len(status)==1:
						for estado in status:
							if estado in fila[4]:
								l2.append(fila)

					else:
						pasa=True
						l3=[]


						for estado in status:
							if estado in fila[4]:
								l3.append(fila)
							else:
								pasa=False
						
						if pasa!=False:
							l2.extend(l3)
				


				return l2

		def ordenar(self,por="Fecha",ascendente=True,filtros=None):
			if por=="Fecha":
				formato=self.db.obtenerFormato("Fecha")

				l=[]
				for fila in self.obtenerFilas(self.db.seleccion):
					if l!=[]:
						

						if ascendente==True:
							if datetime.datetime.strptime(l[-1][3],formato)>=datetime.datetime.strptime(fila[3],formato):
								l.append(fila)

							else:
								l.insert(0,fila)

						else:

							if datetime.datetime.strptime(l[-1][3],formato)>=datetime.datetime.strptime(fila[3],formato):
								l.insert(0,fila)

							else:
								l.append(fila)

					else:
						l.append(fila)
				

			elif por=="Nombre":
				l=[]
				for fila in self.obtenerFilas(self.db.seleccion):
					if l!=[]:
						if ascendente==True:
							if zu.cmpString(l[-1][0],fila[0]):
								l.append(fila)
							else:
								l.insert(0,fila)

						else:
							if zu.cmpString(l[-1][0],fila[0]):
								l.insert(0,fila)
							else:
								l.append(fila)
					else:
						l.append(fila)
			


			else:
				pass

			if filtros!=None:
					return self.filtrar(filtros,l)
		def obtenerIdsFiltrados(self,lista):
			l=[]

			for elem in lista:
				

				clave=elem[2].keys()[0]
				l.append(elem[2][clave])
			return l
		def eliminar(self,c,tabla):
			if self.request():
				self.db(tabla).delFila(c)

				return self.grabar()
except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e