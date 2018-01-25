#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import copy
email="<type 'email'>"
#Estado:
#version:v0.01
"""
la función DB permite crear base de datos de manera sencilla 
"""
from copy import copy
import zu
def decode(cadena):
    cadena=cadena.replace("\xc2\xa1","¡")
    cadena=cadena.replace("\xc2\xa2","¢")
    cadena=cadena.replace("\xc2\xa3","£")
    cadena=cadena.replace("\xc2\xa4","¤")
    cadena=cadena.replace("\xc2\xa5","¥")
    cadena=cadena.replace("\xc2\xa6","¦")
    cadena=cadena.replace("\xc2\xa7","§")
    cadena=cadena.replace("\xc2\xa8","¨")
    cadena=cadena.replace("\xc2\xa9","©")
    cadena=cadena.replace("\xc2\xaa","ª")
    cadena=cadena.replace("\xc2\xab","«")
    cadena=cadena.replace("\xc2\xac","¬")
    cadena=cadena.replace("\xc2\xae","®")
    cadena=cadena.replace("\xc2\xaf","¯")
    cadena=cadena.replace("\xc2\xb0","°")
    cadena=cadena.replace("\xc2\xb1","±")
    cadena=cadena.replace("\xc2\xb2","²")
    cadena=cadena.replace("\xc2\xb3","³")
    cadena=cadena.replace("\xc2\xb4","´")
    cadena=cadena.replace("\xc2\xb5","µ")
    cadena=cadena.replace("\xc2\xb6","¶")
    cadena=cadena.replace("\xc2\xb7","·")
    cadena=cadena.replace("\xc2\xb8","¸")
    cadena=cadena.replace("\xc2\xb9","¹")
    cadena=cadena.replace("\xc2\xba","º")
    cadena=cadena.replace("\xc2\xbb","»")
    cadena=cadena.replace("\xc2\xbc","¼")
    cadena=cadena.replace("\xc2\xbd","½")
    cadena=cadena.replace("\xc2\xbe","¾")
    cadena=cadena.replace("\xc2\xbf","¿")
    cadena=cadena.replace("\xc3\x80","À")
    cadena=cadena.replace("\xc3\x81","Á")
    cadena=cadena.replace("\xc3\x82","Â")
    cadena=cadena.replace("\xc3\x83","Ã")
    cadena=cadena.replace("\xc3\x84","Ä")
    cadena=cadena.replace("\xc3\x85","Å")
    cadena=cadena.replace("\xc3\x86","Æ")
    cadena=cadena.replace("\xc3\x87","Ç")
    cadena=cadena.replace("\xc3\x88","È")
    cadena=cadena.replace("\xc3\x89","É")
    cadena=cadena.replace("\xc3\x8a","Ê")
    cadena=cadena.replace("\xc3\x8b","Ë")
    cadena=cadena.replace("\xc3\x8c","Ì")
    cadena=cadena.replace("\xc3\x8d","Í")
    cadena=cadena.replace("\xc3\x8e","Î")
    cadena=cadena.replace("\xc3\x8f","Ï")
    cadena=cadena.replace("\xc3\x90","Ð")
    cadena=cadena.replace("\xc3\x91","Ñ")
    cadena=cadena.replace("\xc3\x92","Ò")
    cadena=cadena.replace("\xc3\x93","Ó")
    cadena=cadena.replace("\xc3\x94","Ô")
    cadena=cadena.replace("\xc3\x95","Õ")
    cadena=cadena.replace("\xc3\x96","Ö")
    cadena=cadena.replace("\xc3\x97","×")
    cadena=cadena.replace("\xc3\x98","Ø")
    cadena=cadena.replace("\xc3\x99","Ù")
    cadena=cadena.replace("\xc3\x9a","Ú")
    cadena=cadena.replace("\xc3\x9b","Û")
    cadena=cadena.replace("\xc3\x9c","Ü")
    cadena=cadena.replace("\xc3\x9d","Ý")
    cadena=cadena.replace("\xc3\x9e","Þ")
    cadena=cadena.replace("\xc3\x9f","ß")
    cadena=cadena.replace("\xc3\xa0","à")
    cadena=cadena.replace("\xc3\xa1","á")
    cadena=cadena.replace("\xc3\xa2","â")
    cadena=cadena.replace("\xc3\xa3","ã")
    cadena=cadena.replace("\xc3\xa4","ä")
    cadena=cadena.replace("\xc3\xa5","å")
    cadena=cadena.replace("\xc3\xa6","æ")
    cadena=cadena.replace("\xc3\xa7","ç")
    cadena=cadena.replace("\xc3\xa8","è")
    cadena=cadena.replace("\xc3\xa9","é")
    cadena=cadena.replace("\xc3\xaa","ê")
    cadena=cadena.replace("\xc3\xab","ë")
    cadena=cadena.replace("\xc3\xac","ì")
    cadena=cadena.replace("\xc3\xad","í")
    cadena=cadena.replace("\xc3\xae","î")
    cadena=cadena.replace("\xc3\xaf","ï")
    cadena=cadena.replace("\xc3\xb0","ð")
    cadena=cadena.replace("\xc3\xb1","ñ")
    cadena=cadena.replace("/xc3/xb1","ñ")
    cadena=cadena.replace("\xc3\xb2","ò")
    cadena=cadena.replace("\xc3\xb3","ó")
    cadena=cadena.replace("\xc3\xb4","ô")
    cadena=cadena.replace("\xc3\xb5","õ")
    cadena=cadena.replace("\xc3\xb6","ö")
    cadena=cadena.replace("\xc3\xb7","÷")
    cadena=cadena.replace("\xc3\xb8","ø")
    cadena=cadena.replace("\xc3\xb9","ù")
    cadena=cadena.replace("\xc3\xba","ú")
    cadena=cadena.replace("\xc3\xbb","û")
    cadena=cadena.replace("\xc3\xbc","ü")
    cadena=cadena.replace("\xc3\xbd","ý")
    cadena=cadena.replace("\xc3\xbe","þ")
    cadena=cadena.replace("\xc3\xbf","ÿ")
    cadena=cadena.replace("\xe2\x80\x91","‑") 
    cadena=cadena.replace("\xe2\x80\x92","‒") 
    cadena=cadena.replace("\xe2\x80\x93","–") 
    cadena=cadena.replace("\xe2\x80\x94","—") 
    cadena=cadena.replace("\xe2\x80\x95","―") 
    cadena=cadena.replace("\xe2\x80\x96","‖") 
    cadena=cadena.replace("\xe2\x80\x97","‗") 
    cadena=cadena.replace("\xe2\x80\x98","‘") 
    cadena=cadena.replace("\xe2\x80\x99","’") 
    cadena=cadena.replace("\xe2\x80\x9a","‚") 
    cadena=cadena.replace("\xe2\x80\x9b","‛") 
    cadena=cadena.replace("\xe2\x80\x9c","“") 
    cadena=cadena.replace("\xe2\x80\x9d","”") 
    cadena=cadena.replace("\xe2\x80\x9e","„") 
    cadena=cadena.replace("\xe2\x80\x9f","‟") 
    cadena=cadena.replace("\xe2\x80\xa0","†") 
    cadena=cadena.replace("\xe2\x80\xa1","‡") 
    cadena=cadena.replace("\xe2\x80\xa2","•") 
    cadena=cadena.replace("\xe2\x80\xa3","‣") 
    cadena=cadena.replace("\xe2\x80\xa4","․") 
    cadena=cadena.replace("\xe2\x80\xa5","‥") 
    cadena=cadena.replace("\xe2\x80\xa6","…") 
    cadena=cadena.replace("\xe2\x80\xa7","‧") 
    cadena=cadena.replace("\xe2\x80\xb0","‰") 
    cadena=cadena.replace("\xe2\x80\xb1","‱") 
    cadena=cadena.replace("\xe2\x80\xb2","′") 
    cadena=cadena.replace("\xe2\x80\xb3","″") 
    cadena=cadena.replace("\xe2\x80\xb4","‴") 
    cadena=cadena.replace("\xe2\x80\xb5","‵") 
    cadena=cadena.replace("\xe2\x80\xb6","‶") 
    cadena=cadena.replace("\xe2\x80\xb7","‷") 
    cadena=cadena.replace("\xe2\x80\xb8","‸") 
    cadena=cadena.replace("\xe2\x80\xb9","‹") 
    cadena=cadena.replace("\xe2\x80\xba","›") 
    cadena=cadena.replace("\xe2\x80\xbb","※") 
    cadena=cadena.replace("\xe2\x80\xbc","‼") 
    cadena=cadena.replace("\xe2\x80\xbd","‽") 
    cadena=cadena.replace("\xe2\x80\xbe","‾") 
    cadena=cadena.replace("\xe2\x80\xbf","‿") 
    cadena=cadena.replace("\xe2\x81\x80","⁀") 
    cadena=cadena.replace("\xe2\x81\x81","⁁") 
    cadena=cadena.replace("\xe2\x81\x82","⁂") 
    cadena=cadena.replace("\xe2\x81\x83","⁃") 
    cadena=cadena.replace("\xe2\x81\x84","⁄") 
    cadena=cadena.replace("\xe2\x81\x85","⁅") 
    cadena=cadena.replace("\xe2\x81\x86","⁆") 
    cadena=cadena.replace("\xe2\x81\x87","⁇") 
    cadena=cadena.replace("\xe2\x81\x88","⁈") 
    cadena=cadena.replace("\xe2\x81\x89","⁉") 
    cadena=cadena.replace("\xe2\x81\x8a","⁊") 
    cadena=cadena.replace("\xe2\x81\x8b","⁋") 
    cadena=cadena.replace("\xe2\x81\x8c","⁌") 
    cadena=cadena.replace("\xe2\x81\x8d","⁍") 
    cadena=cadena.replace("\xe2\x81\x8e","⁎") 
    cadena=cadena.replace("\xe2\x81\x8f","⁏") 
    cadena=cadena.replace("\xe2\x81\x90","⁐") 
    cadena=cadena.replace("\xe2\x81\x91","⁑") 
    cadena=cadena.replace("\xe2\x81\x92","⁒") 
    cadena=cadena.replace("\xe2\x81\x93","⁓") 
    cadena=cadena.replace("\xe2\x81\x94","⁔") 
    cadena=cadena.replace("\xe2\x81\x95","⁕") 
    cadena=cadena.replace("\xe2\x81\x96","⁖") 
    cadena=cadena.replace("\xe2\x81\x97","⁗") 
    cadena=cadena.replace("\xe2\x81\x98","⁘") 
    cadena=cadena.replace("\xe2\x81\x99","⁙") 
    cadena=cadena.replace("\xe2\x81\x9a","⁚") 
    cadena=cadena.replace("\xe2\x81\x9b","⁛") 
    cadena=cadena.replace("\xe2\x81\x9c","⁜") 
    cadena=cadena.replace("\xe2\x81\x9d","⁝") 
    cadena=cadena.replace("\xe2\x81\x9e","⁞") 
    cadena=cadena.replace("\xe2\x81\xb0","⁰") 
    cadena=cadena.replace("\xe2\x81\xb1","ⁱ") 
    cadena=cadena.replace("\xe2\x81\xb4","⁴") 
    cadena=cadena.replace("\xe2\x81\xb5","⁵") 
    cadena=cadena.replace("\xe2\x81\xb6","⁶") 
    cadena=cadena.replace("\xe2\x81\xb7","⁷") 
    cadena=cadena.replace("\xe2\x81\xb8","⁸") 
    cadena=cadena.replace("\xe2\x81\xb9","⁹") 
    cadena=cadena.replace("\xe2\x81\xba","⁺") 
    cadena=cadena.replace("\xe2\x81\xbb","⁻") 
    cadena=cadena.replace("\xe2\x81\xbc","⁼") 
    cadena=cadena.replace("\xe2\x81\xbd","⁽") 
    cadena=cadena.replace("\xe2\x81\xbe","⁾") 
    cadena=cadena.replace("\xe2\x81\xbf","ⁿ") 
    cadena=cadena.replace("\xe2\x81\xbf","ⁿ") 
     
    #url
    
    cadena=cadena.replace("%20",' ') 
    cadena=cadena.replace("%7B","{") 
    cadena=cadena.replace("%7D","}") 
    return cadena
class obj:
	def __init__(self,valor,tipo=None):
		self.valor=valor
		self.tipo=tipo
	

#Estado:finalizado 
#version:v0.01
"""dbtype permite identificar un tipo de dato que pertenece a los tipos de datos que trabaja la base de datos"""
def dbtype(dato,formato=None):
	try:
		if type(dato)==str:
			if "mailto:"==dato[:len("mailto:")] and "@" in dato and (".com" in dato[dato.index("@"):] or ".org" in dato[dato.index("@"):] or ".net" in dato[dato.index("@"):]):
				return "<type 'email'>"
			elif "date:"==dato[:len("date:")]:
				if formato!=None:
					try:
						data=dato[len("date:"):]
						sp=formato.replace("%d","").replace("%m","").replace("%y","")[0]
						if sp in data:
							for elem in data.split(sp):
								try:
									int(elem)
								except:
									return None
						return "<type 'date'>"
					except Exception,e:
						print "Error en dbtype -> date"
						print e
						raise
				else:
					print "Hace falta formato para ",dato
					return None

			elif "datetime:"==dato[:len("datetime:")]:
				if formato!=None:
					try:
							data=dato[len("datetime:"):]
							
							if " - " in data and " - " in formato and formato.count(" - ")==1:
								parts=data.split(" - ")
								fparts=formato.split(" - ")
								if dbtype(parts[0],fparts[0])=="<type 'date'>" and dbtype(parts[1],fparts[1])=="<type 'time'>":
									return "<type 'datetime'>"
								elif dbtype(parts[1],fparts[1])=="<type 'date'>" and dbtype(parts[0],fparts[0])=="<type 'time'>":
									return "<type 'datetime'>"
							elif " " in data and " " in formato and formato.count(" ")==1:
								
								parts=data.split(" ")
								fparts=formato.split(" ")
								

								if dbtype("date:"+parts[0],fparts[0])=="<type 'date'>" and dbtype("time:"+parts[1],fparts[1])=="<type 'time'>":
									return "<type 'datetime'>"
								elif dbtype("date:"+parts[1],fparts[1])=="<type 'date'>" and dbtype("time:"+parts[0],fparts[0])=="<type 'time'>":
									return "<type 'datetime'>"
							else:
								return None
							

						

					except Exception,e:
						print "error en dbtype -> datetime<br>"
						print e
						raise
				else:
					print "Hace falta formato para ",dato

					
			
			elif "time:"==dato[:len("time:")]:
				if formato!=None:
					try:
						data=dato[len("time:"):]
						if "%H" in formato and "%M" in formato and "%S" in formato:
							sp=formato.replace("%H","").replace("%M","").replace("%S","")[0]
							for elem in data.split(sp):
								try:
									if elem !="":
										int(elem)
								except:
									return None
							return "<type 'time'>"

						elif "%H" in formato and "%M" in formato and "%S" not in formato:
							sp=formato.replace("%H","").replace("%M","")[0]

							for elem in data.split(sp):
								
								try:
									if elem !="":
										int(elem)
								except:
									return None
							return "<type 'time'>"
						elif "%I" in formato and "%M" in formato and "%S" in formato:
							sp=formato.replace("%I","").replace("%M","").replace("%S","")[0]
							for elem in data.split(sp):
								try:
									if elem !="":
										int(elem)
								except:
									return None
							return "<type 'time'>"
						elif "%I" in formato and "%M" in formato and "%S" not in formato:
							sp=formato.replace("%I","").replace("%M","")[0]
							for elem in data.split(sp):
								try:
									if elem !="":
										int(elem)
								except:
									return None
							return "<type 'time'>"
						
						elif "%I" not in formato and "%H" not in formato and "%M" in formato and "%S" in formato:
							sp=formato.replace("%M","").replace("%S","")[0]
							for elem in data.split(sp):
								try:
									if elem !="":
										int(elem)
								except:
									return None
							return "<type 'time'>"
						elif "%I" not in formato and "%H" not in formato and "%M" not in formato and "%S" in formato:
							try:
								if elem !="":
										int(data)
							except:
								return None
							return "<type 'time'>"
						elif "%I" not in formato and "%H" not in formato and "%M" in formato and "%S" not in formato:
							try:
								if elem !="":
										int(data)
							except:
								return None
							return "<type 'time'>"
						else:
							return None

					except Exception,e:
						print "Error en dbtype -> time"
						print e
						raise
					
				else:
					print "Hace falta formato para ",dato


			elif "https://" == dato[:len("https://")] or "http://" == dato[:len("http://")] or "ftp://" == dato[:len("ftp://") or "news://" == dato[:len("news://")]] or "telnet://" == dato[:len("telnet://")]:
				return "<type 'url'>"

			elif "data:" == dato[:len("data:")]:
				return "<type 'binary'>"

			elif "password:" == dato[:len("password:")]:
				return "<type 'password'>"
				
			elif "ldap:" == dato[:len("ldap:")]:
				return "<type 'serverFolder'>"

			elif "file://" == dato[:len("file://")]:
				return "<type 'file'>"
			else:
				if len(dato)>= 70:
					return "<type 'doc'>"
				else:
					return str
		
		else:
			try:
				return dato.tipo
			except:
				return type(dato)


	except Exception, e:
		print "error en dbtype <br>"								
		print e
		raise

#Estado:finalizado
#Version:v0.01
""" rtype permite corrige el string del tipo de dato"""
def rtype(tipo):
	c=str(tipo)
	return c[len("<type '"):-2]		
class DB:
		def __init__(self,dbfile=None,debug=False):
			self.dbfile=dbfile
			self.tablas={}
			self.campos={}
			self.clavePrimaria={}
			self.seleccion=None
			self.dbfile=dbfile
			self.log=[]
			self.errores=[]
			self.load=False
			self.modificacion=False
			self.debug=debug
			self.str=str
			self.int=int
			self.float=float
			self.bool=bool
			self.dict=dict
			self.list=list
			self.tuple=tuple
			self.object=object
			self.long=long
			self.all="<type 'all'>"
			self.password="<type 'password'>"
			self.email="<type 'email'>"
			self.time="<type 'time'>"
			self.date="<type 'date'>"
			self.datetime="<type 'datetime'>"
			self.url="<type 'url'>"
			self.file="<type 'file'>"
			self.bin="<type 'binary'>"
			self.doc="<type 'doc'>"
			self.t=None
			self.limite=1
			
			self.registro=[]

			if dbfile==None:
				
				self.registro=["# -*- coding: utf-8 -*-","db=DB()"]
				self.rcampos=["# -*- coding: utf-8 -*-","db=DB()"]
				
	
			else:
				x=dbcargar(dbfile,debug)

				


				if str(type(x))!="<type 'instance'>":
					try:
						
						
						import traceback
						import sys

						exc_type,exc_obj,exc_tb=sys.exc_info()


						fname = exc_tb.tb_frame.f_code.co_filename

						self.log.append("Ocurrio un error al cargar la base de datos "+dbfile+"\n"+str(x)+"\n"+"".join(traceback.format_exception(exc_type,fname,exc_tb)))
						self.errores.append("Ocurrio un error al cargar la base de datos "+dbfile+"\n"+str(x)+"\n"+"".join(traceback.format_exception(exc_type,fname,exc_tb)))
					except  Exception as e:
						
						
						self.log.append("Ocurrio un error al cargar la base de datos "+dbfile+"\n"+str(x))
						self.errores.append("Ocurrio un error al cargar la base de datos "+dbfile+"\n"+str(x)+"\n"+""+str(e))
					

				else:
					#hay que actualizar los atributos, al parecer estos no se soberescribes al sobrescribir self
					for elem in dir(x):
						exec("""temp=str(type(x."""+elem+"""))!="<type 'instancemethod'>" """)
						if temp:
							exec("self."+elem+"=x."+elem)

					


		    
		def consola(self,mensaje,error=False):
			self.log.append(mensaje)
			if error==True:
				self.errores.append(mensaje)
			if self.debug==True:
				print mensaje
			

		def __call__(self,tabla=None,herencia=None,copia=None):
			    self.t=tabla
			    self.error=[]			    
				#nuevo uso del registro, almacena todos los comandos utilizados
				#para que estos luego puedan ser escritos en un archivo aparte
			    if tabla not in self.tablas and tabla not in self.campos:
					self.campos[tabla]=[]
					self.clavePrimaria[tabla]=0
					if herencia!=None:
						self.campos[tabla]=copy.copy(self.campos[herencia])


					self.tablas[tabla]={}
					if copia!=None:
						self.tablas[tabla]=copy.copy(self.tablas[copia])
						self.clavePrimaria[tabla]=len(self.tablas[tabla])-1
						
					
					self.log=[]
					self.nmodif=0
					
					self.lrelaciones=[]

					
					self.relaciones={}
			    self.seleccion=tabla


			    self.idseleccion=None
			    #para direfebciar cuando se usa db("tabla")
			    return self
			    
			    
			    
			    					

				
			    
		def obtenerFormato(self,campo):
			    	
			    	for elem in self.campos[self.seleccion]:
			    		if elem[0]==campo:
			    			return elem[9]
				#Estado:finalizado
				#Version:v0.01
		def id(self,i):
					self.idseleccion=i
					return self

		def columna(self,camp):
			    	print self.idseleccion
			    	if self.t!=None:
			    		self.consola(str(self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)])+"\n",self)
					return self.tablas[self.seleccion][self.idseleccion][self.obtenerCampo(camp)]

		def campo(self,nombre,tipo,unico=False,vacio=True,unicaFila=False,unicacolumna=False,mini=0,maxi=-1,step=None,formato=None):
					try:
							self.campos[self.seleccion].append([nombre,tipo,unico,vacio,unicaFila,unicacolumna,mini,maxi,step,formato])
							if self.seleccion!=None:
								if type(formato)==str:
									formato="'"+formato+"'"

								self.registro.append("db('"+self.seleccion+"').campo('"+nombre+"',db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
								self.rcampos.append("db('"+self.seleccion+"').campo('"+nombre+"',db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")

								
					except Exception as e:
							print ""
							print "error al crear campos"
							print e
							self.registro.append("db.campo('"+nombre+"','db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
							self.rcampos.append("db.campo('"+nombre+"','db."+rtype(tipo)+","+str(unico)+","+str(vacio)+","+str(unicaFila)+","+str(unicacolumna)+","+str(mini)+","+str(maxi)+","+str(step)+","+str(formato)+")")
				
					return self					
                
		#Estado:finalizado
		#Version:v0.01
		"""
		Esta función permite insertar una lista de campos en la tabla ya seleccionada
		Ejemplo:
		 		self.insertar('miNombre','miApellido',12345678)
		"""
		def insertar(self,*campos,**args):
			    	
			    	try:
			    		
			    		if self.seleccion != None and self.campos[self.seleccion]!=[]:
							campos=copy(list(campos))

							valido=True
							if "sob" not in args:
								args["sob"]=False
							lcampos=[]
							razones=[]
							temp=[]
							c=0
							
							for elem in campos:
								if self.campos[self.seleccion][c][5]==True: #unicacolumna
									if campos.count(elem)>1:
										valido=False
										break
								if self.campos[self.seleccion][c][4]==True:	#unicaFila
									if self.tablas[self.seleccion]!={}:
										if tuple(self.obtenerFilaValores(campos[0],self.seleccion)) == campos:
												valido=False
												break
								c+=1
									
							
											

							

							if valido==True:
								c=0

								for elem in campos:
									try:
										if self.campos[self.seleccion][c][3]==True:#vacio
											try:
												if elem==None:
													lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9]) ))
												else:

													if self.campos[self.seleccion][c][2]==True:#unico
														try:

															if args["sob"]==True:
																try:

																	bloqueados=[]
																	for elem2 in self.obtenerColumna(self.obtenerCampos()[c]):

																		if dbtype(elem,self.campos[self.seleccion][c][9])==self.object:

																			bloqueados.append(elem2.valor)
																	if bloqueados==[]:
																		try:
																			if dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
																				if self.campos[self.seleccion][c][1]==self.doc and dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																					lcampos.append(obj(elem,self.doc))
																				else:
																					valido=False

																					razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1]+" para el campo "+str(self.campos[self.seleccion][c][0]))
																			else:
																				if self.campos[self.seleccion][c][1]==self.file:
																					if self.load==False:
																						f=open(elem.replace("file://",""),"rb")
																						b=f.read()
																						f.close()
																						campos[c]="file://"+b
																						if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																								if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																										lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9]) ))
																								else:
																										valido=False
																										razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																							
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9]) ))
																							else:
																								valido=False
																								razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9]) ))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9]) ))
																				else:
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9]) ))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:
																							if len(elem)>=self.campos[self.seleccion][c][6]:

																									lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:	
																							if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																	
																		except Exception as e:
																			print "Error en el bloque vacio -> unico : nobloqueados "
																			print e
																	else:
																		try:

																			if elem in bloqueados:

																				valido=False
																				razones.append(str(elem)+" se repite y es un campo unico")
																			else:

																				if self.campos[self.seleccion][c][1]==self.file:

																					if self.load==False:
																						f=open(elem.replace("file://",""),"rb")
																						b=f.read()
																						f.close()
																						campos[c]="file://"+b
																						if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																								if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																										lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																								else:
																										valido=False
																										razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																							
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:
																							if len(elem)>=self.campos[self.seleccion][c][6]:

																									lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:	
																							if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																				
																		except Exception as e:															
																			print "Error en el bloque vacio -> unico sobrescribir : bloqueados "
																			print e

															
																except Exception as e:
																	print "Error en el bloque vacio -> unico sobrescribir : bloqueados "
																	print e
															else:
																try:

																	if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
																		
																		valido=False
																		razones.append(str(elem)+" se repite y es un campo unico")
																	else:
																		if dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
																			if self.campos[self.seleccion][c][1]==self.doc and dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																				if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if len(elem)>=self.campos[self.seleccion][c][6]:
																						lcampos.append(obj(elem,self.doc))
																					else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																					
																					if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																						lcampos.append(obj(elem,self.doc))
																					else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																				elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																					lcampos.append(obj(elem,self.doc))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																			else:
																				valido=False
																				razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1]+" para el campo "+str(self.campos[self.seleccion][c][0]))
																		else:

																			if self.campos[self.seleccion][c][1]==self.file:
																					if self.load==False:
																						f=open(elem.replace("file://",""),"rb")
																						b=f.read()
																						f.close()
																						campos[c]="file://"+b
																						if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																								if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																										lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																								else:
																										valido=False
																										razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																							
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																					else:
																						lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:
																							if len(elem)>=self.campos[self.seleccion][c][6]:

																									lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:	
																							if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																						lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																except Exception as e:
																	print "Error en el bloque vacio -> unico nosobrescribir : bloqueados "
																	print e													

														except Exception as e:
															print "Error en bloque vacio -> unico "
															print e
													else:
														try:
															

															if dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
																
																
																if self.campos[self.seleccion][c][1]==self.doc and dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																	
																	try:



																		if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:

																			if len(elem)>=self.campos[self.seleccion][c][6]:
																				lcampos.append(obj(elem,self.doc))
																			else:
																				valido=False
																				razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																			
																			if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																				lcampos.append(obj(elem,self.doc))
																			else:
																				valido=False
																				razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:

																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																
																	except Exception as e:
																		print "Error en bloque vacio -> no-unico -> tipo igual -> tipo doc <br>"
																else:
																	valido=False
																	#print elem," ",self.campos[self.seleccion][c][0]," ",c,"<br>"
																	razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1]+" para el campo "+str(self.campos[self.seleccion][c][0]))


															else:
																try:

																	if self.campos[self.seleccion][c][1]==self.file:

																					if self.load==False:
																						f=open(elem.replace("file://",""),"rb")
																						b=f.read()
																						f.close()
																						campos[c]="file://"+b

																						if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																								if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																										lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																								else:
																										valido=False
																										razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																							
																							if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																						elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																						else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")


																					else:

																						lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																					
																					if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:
																							if len(elem)>=self.campos[self.seleccion][c][6]:

																									lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																									valido=False
																									razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																						if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																							if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																						else:	
																							if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																								lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																							else:
																								valido=False
																								razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																					elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:

																						lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																except Exception as e:
																	print "Error en bloque vacio -> no-unico -> tipo igual <br>"
																	print e


														except Exception as e:
															print "Error en bloque vacio -> no-unico <br>"
															print e
											except Exception as e:
												print "Error en bloque vacio "
												print e
											
										else:

											if self.campos[self.seleccion][c][2]==True:#unico

												if args["sob"]==True:
														bloqueados=[]
														for elem2 in self.obtenerColumna(self.obtenerCampos()[c]):
															if dbtype(elem,self.campos[self.seleccion][c][9])==self.object:

																bloqueados.append(elem2.valor)
														if bloqueados==[]:
															if dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
																if self.campos[self.seleccion][c][1]==self.doc and dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																	if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																		if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																		
																		if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																else:
																	valido=False
																	razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1]+" para el campo "+str(self.campos[self.seleccion][c][0]))
															else:
																	
																if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																	if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																	
																	if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																		lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																	lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
														else:
															if elem in bloqueados:
																valido=False
																razones.append(str(elem)+" se repite y es un campo unico")
															else:
																if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																	if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																	
																	if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																		lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																	lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																else:
																	valido=False
																	razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																
												else:

													if elem in self.obtenerColumna(self.campos[self.seleccion][c][0]):
														valido=False
														razones.append(str(elem)+" se repite y es un campo unico")
													else:
														if dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
															if self.campos[self.seleccion][c][1]==self.doc and dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																	if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																		if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																		
																		if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
															else:
																valido=False
																razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1]+" para el campo "+str(self.campos[self.seleccion][c][0]))
														else:

															if self.campos[self.seleccion][c][1]==self.file:
																		if self.load==False:
																			f=open(elem.replace("file://",""),"rb")
																			b=f.read()
																			f.close()
																			campos[c]="file://"+b
																			if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																			elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																				
																				if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																					lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																			elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																				lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																		else:
																			lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
															else:
																		if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																			if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																				if elem>=self.campos[self.seleccion][c][6]:
																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																			else:
																				if len(elem)>=self.campos[self.seleccion][c][6]:

																						lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																						valido=False
																						razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																			if dbtype(elem,self.campos[self.seleccion][c][9])==self.int or dbtype(elem,self.campos[self.seleccion][c][9])==self.float or dbtype(elem,self.campos[self.seleccion][c][9])==self.long:
																				if elem>=self.campos[self.seleccion][c][6] and elem<=self.campos[self.seleccion][c][7]:
																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																			else:	
																				if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																					lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																		elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																			lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

											else:

												if dbtype(elem,self.campos[self.seleccion][c][9])!=self.campos[self.seleccion][c][1] and "<type 'all'>"!= self.campos[self.seleccion][c][1]:
														if self.campos[self.seleccion][c][1]==self.doc and dbtype(elem,self.campos[self.seleccion][c][9])==self.str:
																	if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																		if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																		
																		if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																			lcampos.append(obj(elem,self.doc))
																		else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

																	elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																		lcampos.append(obj(elem,self.doc))
																	else:
																		valido=False
																		razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
														else:
															valido=False
															razones.append(str(elem)+" tiene que ser "+str(self.campos[self.seleccion][c][1])[1:-1]+" y es "+str(dbtype(elem,self.campos[self.seleccion][c][9]))[1:-1]+" para el campo "+str(self.campos[self.seleccion][c][0]))
												else:

													if self.campos[self.seleccion][c][1]==self.file:
																		if self.load==False:
																			f=open(elem.replace("file://",""),"rb")
																			b=f.read()
																			f.close()
																			campos[c]="file://"+b
																			if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																					if len(elem)+len("file://")>=self.campos[self.seleccion][c][6]:
																							lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																					else:
																							valido=False
																							razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																			elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
																				
																				if len(elem)+len("file://")>=self.campos[self.seleccion][c][6] and len(elem)+len("file://")<=self.campos[self.seleccion][c][7]:
																					lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																				else:
																					valido=False
																					razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")

																			elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
																				lcampos.append(obj("file://"+b,dbtype(elem,self.campos[self.seleccion][c][9])))
																			else:
																				valido=False
																				razones.append("El campo: "+str(self.campos[self.seleccion][c])+" no cumple con los valores minimos y maximos establecidos.")
																		else:
																			lcampos.append(obj(elem.replace("file://",""),dbtype(elem,self.campos[self.seleccion][c][9])))
													else:
														if self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]==-1:
																	if len(elem)>=self.campos[self.seleccion][c][6]:
																			lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
																	else:
																			valido=False
																			razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

														elif self.campos[self.seleccion][c][6]!=0 and self.campos[self.seleccion][c][7]!=-1:
															
															if len(elem)>=self.campos[self.seleccion][c][6] and len(elem)<=self.campos[self.seleccion][c][7]:
																lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
															else:
																valido=False
																razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")

														elif self.campos[self.seleccion][c][6]==0 and self.campos[self.seleccion][c][7]==-1:
															lcampos.append(obj(elem,dbtype(elem,self.campos[self.seleccion][c][9])))
														else:
															valido=False
															razones.append(str(elem)+" no cumple con los valores minimos y maximos establecidos.")
																		
									except Exception as e:
										print "Error en bloque Principal"						                                
									c+=1
								

							if valido==True:
								self.tablas[self.seleccion][self.clavePrimaria[self.seleccion]]=lcampos
								self.clavePrimaria[self.seleccion]+=1

								try:
									if self.seleccion!=None:



										self.registro.append("db('"+tabla+"').insertar("+str(campos)[1:-1]+")")
										



										self.consola("La inserción de datos fue realizada con exito en la tabla \n \x1b[1;31m "+self.seleccion+"\n Datos insertados:\n"+str(campos)+" \x1b[0m\n",self)


										
										

								except:

										self.registro.append("db('"+self.seleccion+"').insertar("+str(campos)[1:-1]+")")
										self.consola("La inserción de datos fue realizada con exito en la tabla \x1b[1;31m"+self.seleccion+"\x1b[0m \n Datos insertados:\n"+str(campos)+"\n",self)
									
							else:
							
									self.consola("La inserción de datos no puedo ser realizada en la tabla \x1b[1;31m"+self.seleccion+"\x1b[0m .\nRazones: \n "+str(razones)+"\n",True)

							
							return self
			    		else:

			    			self.errores.append("Debes crear la tabla '"+str(self.seleccion)+"' antes de insertar datos en ella")
			    			

			    	except Exception, e:
			    		if self.debug==True:
							print "Error al insertar "
							print e
                        
		#Estado:finalizado
		#Version:v0.01
		"""
		Esta función permite modificar los valores de los campos de la tabla seleccionada en el id especificado
		ejemplo:
			    
		self.modificar() 
		"""

		def modificarCampo(self,i,columna,campoNuevo,tabla=None):#columna es el nombre del campo
					if tabla==None:
						tabla=self.seleccion
					campoNuevo=copy(campoNuevo)
					
					if self.obtenerCampo(columna)!=None:

						
						self.tablas[self.seleccion][i][self.obtenerCampo(columna)].valor=campoNuevo
						self.registro.append("db('"+tabla+"').modificarCampo("+str(i)+",'"+columna+"',"+("'"+campoNuevo+"'" if type(campoNuevo)==str else str(campoNuevo))+")")

						#print "nmodif ", self.nmodif
						self.nmodif+=1

						
					else:
						print "esta columna "+columna+" no existe en la tabla"

		def delFila(self,i,tabla=None):
			
					c=0
					ids=0
					if tabla==None:
						tabla=self.seleccion

					for elem in self.registro:
						
						if "db('"+tabla+"').insertar(" in elem:


							if self.debug==True:
								print "#se ha eliminado ", self.registro[c]
							if ids==i:
								del self.registro[c]
								break
							ids+=1
						elif "tabla="+tabla in elem[elem.find("').relacionar(") :] and "id="+str(i) in elem[elem.find("').relacionar(") :]:
							if self.debug==True:
								print "#se ha eliminado ", self.registro[c]
							del self.registro[c]
							break
						c+=1


		#Estado: Pendiente
		#Version:v0.01
		def modificarFila(self,id,*campos):
					c=0
					for elem in campos:
						for elem2 in self.campos[self.seleccion]:
							print "<br>"
							print elem
							print "<br>"
							if elem2[1]==dbtype(elem,self.campos[self.seleccion][c][8]):
								if dbtype(elem[1],self.campos[self.seleccion][c][8])==self.campos[self.seleccion][c][1]:

									self.consola("modificarFila\n de: "+str(self.tablas[self.seleccion][id][c])+" a: "+str(obj(elem,dbtype(elem,self.campos[self.seleccion][c][8])))+"\n",self)
									self.tablas[self.seleccion][id][c]=obj(elem,dbtype(elem,self.campos[self.seleccion][c][8]))
							c+=1
					try:
							if tabla!=None:
								self.registro.append("db('"+tabla+"').modificar("+str(id)+","+str(campos)[1:-1]+")")
					except:
							self.registro.append("db('"+self.seleccion+"').modificar("+str(id)+","+str(campos)[1:-1]+")")
					
					return self				
			    
		#Estado: Pendiente
		#Versión: V0.01
		def grabar(self,dbfile=None):
					

					try:
						self.clear()
						if dbfile==None:
							dbfile=self.dbfile




						self.registro.insert(3,"db.load=True")

						self.registro.append("db.load=False")
						f=open(dbfile,"w")
						c=""
						
						for elem in self.registro:

							c+=elem+"\n"
						f.write(c)
						f.close()


						self.consola("La base de datos fue grabada con exito\n",self)

					except Exception,e:
						print e
		#Estado: Finalizado
		#Versión: V0.01
		#retorna una columna con todos los valores de la columna que forma el campo pasando el nombre del campo como parametro
		def obtenerColumna(self,campo,t=None):
					l=[]
					if t==None:
						t=self.seleccion

					for i in self.mostrarTablas()[t]:
						l.append(self.mostrarTablas()[t][i][self.obtenerCampo(campo,t)])
					if self.t!=None:
						self.consola("obtenerColumna "+self.t+"\n"+str(l)+"\n",self)
					return l
						
		#Estado: Finalizado
		#Version: V0.01
		#retorna la posicion de la primera fila que conicida en nombre del campo 
		def obtenerCampo(self,campo,t=None):
					c=0
					if t==None:
						t=self.seleccion
					for elem in self.campos[t]:
						if campo==elem[0]:
							if self.t!=None:
								self.consola("obtenerCampo\n"+str(c)+"\n",self)
							return c
						c+=1
		#Estado: Finalizado
		#Version: v0.01
		#retorna los id's de las filas donde se encuentra el campo 
		def obtenerFilasId(self,campo,t=None):
					"""
					>>obtenerFilasId("Contenido")
					[0]
					"""
					l=[]
					if t==None:
						t=self.seleccion
					
					for elem in self.tablas[t]:
						
						if campo in self.tablas[t][elem]:
							l.append(elem)

					
					return l
			    
		def obtenerFilas(self,t=None):
					l=[]
					if t==None:
						t=self.seleccion
				
					
					for elem in self.tablas[t]:
						l.append(self.tablas[t][elem])


					return l

			    
		def obtenerFilasValores(self,t=None):
					"""
					"""
					


					l3=[]
					if t==None:
						t=self.seleccion
					l=self.obtenerFilas(t)

					
					
					for fila in l:
						l2=[]

						
						for o in fila:
							if type(o.valor)==str:
								if "mailto:" in o.valor and o.valor[:len("mailto:")]=="mailto:":
									l2.append(o.valor[len("mailto:"):])
								elif "password:" in o.valor and o.valor[:len("password:")]=="password:":
									l2.append(o.valor[len("password:"):])
								elif "datetime:" in o.valor and o.valor[:len("datetime:")]=="datetime:":
									l2.append(o.valor[len("datetime:"):])
								elif "date:" in o.valor and o.valor[:len("date:")]=="date:":
									l2.append(o.valor[len("date:"):])
								elif "time:" in o.valor and o.valor[:len("time:")]=="time:":
									l2.append(o.valor[len("time:"):])

								else:
									l2.append(o.valor)
							else:
								l2.append(o.valor)
					
						l3.append(l2)
					

					return l3
		def obtenerFilasValoresPuro(self,campo,t=None):			
			"""
			Parecida a obtenerFilasValores a pero esta no filtra los valores especiales como password, datetime, mailto, date o time
			"""
			l=self.obtenerFilas(t)
			if t==None:
				t=self.seleccion
			l2=[]
			for fila in l:
				for o in fila:
						l2.append(o.valor)
			return l2
					
				
		def obtener(self,i,campo,t=None):
			    	if t==None:
			    		t=self.seleccion
			    	return self.tablas[t][i][self.obtenerCampo(campo,t)].valor

		def obtenerFilaValores(self,i,t=None):
			    	l=[]
			    	if t==None:
			    		t=self.seleccion
			    	if type(i)==int:
				    	for elem in self.tablas[t][i]:
			    			if type(elem.valor)==str:
								if "mailto:" in elem.valor and elem.valor[:len("mailto:")]=="mailto:":
									l.append(decode(elem.valor[len("mailto:"):]))
								elif "password:" in elem.valor and elem.valor[:len("password:")]=="password:":
									l.append(decode(elem.valor[len("password:"):]))
								elif "datetime:" in elem.valor and elem.valor[:len("datetime:")]=="datetime:":
									l.append(decode(elem.valor[len("datetime:"):]))
								elif "date:" in elem.valor and elem.valor[:len("date:")]=="date:":
									l.append(elem.valor[len("date:"):])
								elif "time:" in elem.valor and elem.valor[:len("time:")]=="time:":
									l.append(decode(elem.valor[len("time:"):]))

								else:
									l.append(decode(elem.valor))

			    			elif type(elem.valor)==list:
								for k,elem2 in enumerate(elem.valor):
									if type(elem2)==str:
										elem.valor[k]=decode(elem2)
								l.append(elem.valor)
			    			elif type(elem.valor)==dict:
			    				temp={}
			    				for elem2 in elem.valor:
									if type(elem.valor[elem2])==str:
										temp[decode(elem2)]=decode(elem.valor[elem2])
									else:
										temp[decode(elem2)]=elem.valor[elem2]
			    				l.append(temp)
			    			else:
								l.append(elem.valor)
			    	elif type(i)==str:
			    		for indice in self.tablas[t]:
			    			if len(self.tablas[t][indice])>0:
			    				if i==self.tablas[t][indice][0].value:
			    					i=indice
							    	for elem in self.tablas[t][i]:
						    			if type(elem.valor)==str:
											if "mailto:" in elem.valor and elem.valor[:len("mailto:")]=="mailto:":
												l.append(decode(elem.valor[len("mailto:"):]))
											elif "password:" in elem.valor and elem.valor[:len("password:")]=="password:":
												l.append(decode(elem.valor[len("password:"):]))
											elif "datetime:" in elem.valor and elem.valor[:len("datetime:")]=="datetime:":
												l.append(decode(elem.valor[len("datetime:"):]))
											elif "date:" in elem.valor and elem.valor[:len("date:")]=="date:":
												l.append(elem.valor[len("date:"):])
											elif "time:" in elem.valor and elem.valor[:len("time:")]=="time:":
												l.append(decode(elem.valor[len("time:"):]))

											else:
												l.append(decode(elem.valor))

						    			elif type(elem.valor)==list:
											for k,elem2 in enumerate(elem.valor):
												if type(elem2)==str:
													elem.valor[k]=decode(elem2)
											l.append(elem.valor)
						    			elif type(elem.valor)==dict:
						    				temp={}
						    				for elem2 in elem.valor:
												if type(elem.valor[elem2])==str:
													temp[decode(elem2)]=decode(elem.valor[elem2])
												else:
													temp[decode(elem2)]=elem.valor[elem2]
						    				l.append(temp)
						    			else:
											l.append(elem.valor)
			    	return l


		def obtenerFilaValoresPuro(self,i,t=None):
			    	l=[]
			    	if t==None:
			    		t=self.seleccion
			    	for elem in self.tablas[t][i]:
			    		l.append(elem.valor)
			    	return l
		


		#Estado: Finalizado
		#Version: v0.01
		#retorna los nombres de los campos de la tabla
		def obtenerCampos(self,t=None):
					c=0
					l=[]
					if t==None:
						t=self.seleccion
					for elem in self.campos[t]:
							l.append(elem[0])
					if self.t!=None:
						self.consola("obtenerCampos\n"+str(l)+"\n",self)
					return l

								
						
						
				
		#Estado: Finalizado
		#Version: v0.01		
		#Muestra las tablas de la base de datos, si se le pasa seleccion esta retorna la tabla especificada
		def mostrarTablas(self,mostrar=False,padres=False,seleccion=None):
					dtablas={}
					if seleccion==None:
						seleccion=self.seleccion
					for elem in self.tablas:
						if padres==False:
							dtablas[elem]={}
							for i in self.tablas[elem]:
								dtablas[elem][i]=[]
								for camp in self.tablas[elem][i]:
									dtablas[elem][i].append(camp.valor)


						else:

							if "." not in elem:
								dtablas[elem]={}
								for i in self.tablas[elem]:
									dtablas[elem][i]=[]
									for camp in self.tablas[elem][i]:
										dtablas[elem][i].append(camp.valor)

					
					if mostrar==False:	
						return dtablas
					else:
						return dtablas[seleccion]
				
		def clear(self):
			    	
			    	if self.nmodif>=self.limite:
			    		
				    	
				    	l=[]
				    	l2=self.rcampos
				    	for tabla in self.tablas:
				    		
				    		for i in self.tablas[tabla]:

				    			l.append("db('"+tabla+"').insertar("+str(self.obtenerFilaValoresPuro(i,tabla))[1:-1]+")")
				    	
				    	l2.extend(l)
				    	l2.extend(self.lrelaciones)
				    	
				    	self.registro=l2
				    	#self.registro.append("db.load=False")
				    	self.nmodif=0

		#Estado: Finalizado
		#Version: v0.01			
		#tabla1 (i,campo1) <- args["tabla"] (args["id"],args["campo"]) 	
		def relacionar(self,i,campo1,**args):

					try:

						if self.obtenerCampo(args["campo"],args["tabla"])!=None:
							
							if "id" in args:
								if "campo" in args:
									try:
										if self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])].tipo==self.object:	
												
												self.consola("Ya existe una relación para este campo\n",self)

										else:
											try:

												self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])].tipo=self.object
												
												self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]][args["id"]][self.obtenerCampo(args["campo"],args["tabla"])]									
												l=str(args)[1:-1].split(",")	
												c=""
												
												for elem in l:
															c+=elem.split(":")[0][1:-1].replace('"',"").replace("'","")+"="+elem.split(":")[1]+","
																		
											
												
												if tabla!=None:

													self.registro.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")
													#nuevo
													#self.campos[self.seleccion][self.obtenerCampos(args["tabla"]).index(args["campo"])][1]=self.object
													self.consola("La relación fue efectuada con exito\n",self)
													
													self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
													self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]
													self.lrelaciones.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")

													
											except Exception,e:
													print "Error relacionar en bloque tabla<br>"
													print e
													self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
													#nuevo
													#self.campos[self.seleccion][self.obtenerCampos(args["tabla"]).index(args["campo"])][1]=self.object
													self.consola("La relación fue efectuada con exito\n",self)
													self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
													self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]
													self.lrelaciones.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
													


									except Exception,e:
										print "Error en relacionar en bloque campo<br>"
										print e.args
										
							else:
								if self.tablas[args["tabla"]].tipo==self.object:
											self.consola("Ya existe una relacion para este campo\n",self)
								else:
									self.tablas[self.seleccion][i][self.obtenerCampo(campo1)]=self.tablas[args["tabla"]]		
									l=str(args)[1:-1].split(",")	
									c=""
									
									for elem in l:
												c+=elem.split(":")[0][1:-1].replace('"',"").replace("'","")+"="+elem.split(":")[1]+","
																
									try:
											if tabla!=None:
												self.registro.append("db('"+tabla+"').relacionar("+str(i)+",'"+campo1+"',"+c+")")	
												self.consola("La relación fue efectuada con exito\n")
												self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
												#nuevo
												self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]
									except:
											self.registro.append("db.relacionar("+str(i)+",'"+campo1+"',"+c+")")
											self.relaciones[self.seleccion]=[i,campo1,args["tabla"],args["id"],args["campo"]]
											#nuevo
											self.relaciones[args["tabla"]]=[args["id"],args["campo"],self.seleccion,i,campo1]

											self.consola("La relación fue efectuada con exito\n",self)
							return self
						else:
							print "El campo ",args["campo"]," a relacionar no existe en la tabla ",args["tabla"]
					except Exception,e:
						print "Error en relacionar "
						print e					
                  
			    
			    
        
        

        
    		
        
        

                
        
def dbcargar(dbfile=None,debug=False,log=[]):
        
        if dbfile!=None:

					f=open(dbfile,"r")
					instrucciones=f.read()
					f.close()
				

					try:

						exec(instrucciones)


						db.debug=debug
						db.consola("--------------------------------------------\nLa base de datos fue cargada con exito\n",db)
						db.t=None
						db.registro.append("db.load=True")
						
						return db
					except Exception,e:

						print e

						if debug==True:
							print "ocurrio un error al cargar la base de datos"
							print e
						else:

							return e
						

	
