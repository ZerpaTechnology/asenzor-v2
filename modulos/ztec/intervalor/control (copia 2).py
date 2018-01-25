#!/usr/bin/python
#-*- codign:utf-8 -*-
#python {{}}
#php <?php ?>
#ruby <% %>
#java <$ $>


import sys
sys.path.append("../")
import os
#para identacion
def convertir(t):
	import intervalo as i
	import sys
	
	import ztec.zu as zu
	
	cpython=True
	ultimo=0
	#nota si dice list index out range estar pendiente que el embebido este dentro de
	#etiquestas por ejemplo <div></<div>
	PYTHON,ex=i.getConjuntos(t,["{{","}}"])


	HTML=i.borrarAll([0,len(t)],PYTHON)

	#"hola mundo"
	# 0123456789
	
	e=[[17, 40], [41, 65]]
	con=[0,len(t)]
	#print "=========================="
	#print "conjuntos: ",conjuntos
	#print i.mostrarConjuntos(t,[conjuntos])
	#print "---------------------------"
	#print "exclusiones: ",exclusiones
	#print i.mostrarConjuntos(t,exclusiones)
	l=[]
	#print "HTML ", HTML
	#print "python ",PYTHON
	iden=""
	
	if "{{" in t and "}}" in t:

		if type(HTML[0])==list:

			for html in HTML:
				codhtml="print '''"+t[html[0]:html[1]].replace("\n","")+"'''"+"\n"
				if codhtml!="print ''\n":
					l.append(iden+codhtml)
				for python in PYTHON:
					
					if html[1]==python[0]:
						
						codpython=t[python[0]:python[1]][2:-2]+"\n"
						tab=zu.getTab(codpython)
						lfor=len("for ")
						lwhile=len("while ")
						lif=len("if ")
						lelse=len("else:")
						ltry=len("try:")
						lexcept=len("except ")
						lelif=len("elif ")
						lpass=len("pass")
						lreturn=len("return ")
						
						if tab=="":
							
							if codpython[0:lfor]=="for ":
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lwhile]=="while ":
								
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lif]=="if ":
								
								l.append(iden+codpython)
								iden+="  "
							elif "else:" in codpython[0:lelse]:
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif "try:" in codpython[0:ltry]:
								
								l.append(iden+codpython)
								iden+="  "
							elif "except" in codpython[0:lexcept]:
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lelif]=="elif ":
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[0:lpass]=="pass" and codpython=="pass\n":
								l.append(iden+codpython)
								iden=iden[:-2]
							elif codpython[0:lreturn]=="return ":
								l.append(iden+codpython)
								iden=iden[:-2]
							else:
								l.append(iden+codpython)

						else:

							liden=len(iden)
							
							if codpython[liden:liden+lfor]=="for ":
								l.append(iden+codpython)
								iden+="  "
							elif codpython[liden:liden+lwhile]=="while ":
								l.append(iden+codpython)
								iden+="  "
							elif codpython[liden:liden+lif]=="if ":
								l.append(iden+codpython)
								iden+="  "

							elif "else:" in codpython[liden-2:liden+lelse]:
								
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif "try:" in codpython[liden:liden+ltry]:
								l.append(iden+codpython)
								iden+="  "
							elif "except" in codpython[liden-2:liden+lexcept]:
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[liden-2:liden+lelif]=="elif ":
								iden=iden[:-2]
								l.append(iden+codpython)
								iden+="  "
							elif codpython[:lpass]=="pass" and codpython=="pass\n":
								l.append(iden+codpython)
								iden=iden[:-2]
							
							elif codpython[liden:lreturn]=="return ":
								l.append(iden+codpython)
								iden=iden[:-2]	
							else:
								l.append(iden+codpython)

						

						
		else:
			l.append(t[HTML[0]:HTML[1]])
		txt=""
		for elem in l:
			txt+=elem
		return txt
	else:

		return 'print """'+t+'"""'

def generar(rutahtml,rutapython,cabecera=""):
	#vista html
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(rutahtml)
	#vista python
	if os.path.exists(rutapython):


		(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(rutapython)
		if mtime!=mtime2:
			f=open(rutahtml,"r")
			t=f.read()

			f.close()

			f=open(rutahtml,"w")

			
			f.write(t)
			f.close()
			txt=convertir(t)
			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()
			return True
	else:

			f=open(rutahtml,"r")
			t=f.read()
			f.close()
			
			f=open(rutahtml,"w")
			f.write(t)
			f.close()
			
			txt=convertir(t)

			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()	
			return True
	return False	



#para no indentacion
def convertir2(t,etiquetas=["{{","}}"],var="doc"):
	"""
	Es el utilizado actualmente por el motor de plantillas
	"""
	import intervalo as i
	import sys
	try:
		import ztec.zu as zu
	except Exception as e:
		import zu
	
	cpython=True
	ultimo=0
	PYTHON,ex=i.getConjuntos(t,etiquetas)


	HTML=i.borrarAll([0,len(t)],PYTHON)

	#"hola mundo"
	# 0123456789
	e=[[17, 40], [41, 65]]
	con=[0,len(t)]
	#print "=========================="
	#print "conjuntos: ",conjuntos
	#print i.mostrarConjuntos(t,[conjuntos])
	#print "---------------------------"
	#print "exclusiones: ",exclusiones
	#print i.mostrarConjuntos(t,exclusiones)
	l=[]
	#print "HTML ", HTML
	#print "python ",PYTHON
	iden=""
	inicial=True#si es la primera linea
	first=False #si hay un print en el html y no hay continuacion previa
	primero=False#si si hay un print en el python y hay continuacion
	comentarios=None

	if etiquetas[0] in t and etiquetas[1] in t:

		if type(HTML[0])==list:
			

			for html in HTML:
				if inicial==True:
					if first==False:
						if t[html[0]:html[1]][0]=="'" or t[html[0]:html[1]][-1]=="'":
							if comentarios==None:
								codhtml=var+'+="""'+t[html[0]:html[1]]+'"""'
						elif t[html[0]:html[1]][0]=='"' or t[html[0]:html[1]][-1]=='",':
							if comentarios==None:
								codhtml=+var+"+='''"+t[html[0]:html[1]]+"'''"
						else:
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"
						inicial=False
						first=True
						primero
					else:
						if t[html[0]:html[1]][0]=="'" or t[html[0]:html[1]][-1]=="'":
							if comentarios==None:
								codhtml=var+'+="""'+t[html[0]:html[1]]+'"""'
						elif t[html[0]:html[1]][0]=='"' or t[html[0]:html[1]][-1]=='"':
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"
						else:
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"
						
				else:
					
					if first==False:

						if t[html[0]:html[1]][-1]=="'" or t[html[0]:html[1]][0]=="'":
							if comentarios==None:
								codhtml=var+'+="""'+t[html[0]:html[1]]+'"""'
						elif t[html[0]:html[1]][-1]=='"' or t[html[0]:html[1]][0]=='"':
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"
						else:
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"
						first=True
						primero=True
						
					else:
						
						if t[html[0]:html[1]][-1]=='"' or t[html[0]:html[1]][0]=='"':
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"
						elif t[html[0]:html[1]][-1]=="'" or t[html[0]:html[1]][0]=="'":
							if comentarios==None:
								codhtml=var+'+="""'+t[html[0]:html[1]]+'"""'
						else:
							if comentarios==None:
								codhtml=var+"+='''"+t[html[0]:html[1]]+"'''"




				if codhtml!="''\n":
					if comentarios==None:
						l.append(iden+codhtml)
				for python in PYTHON:
					
					if html[1]==python[0] or (html[0]==python[1] and python[0]==0):
						codpython=t[python[0]:python[1]][len(etiquetas[0]):-len(etiquetas[1])]
						tab=zu.getTab(codpython)
						lfor=len("for ")
						lwhile=len("while ")
						lif=len("if ")
						lelse=len("else")
						ltry=len("try:")
						lexcept=len("except ")
						lelif=len("elif ")
						lpass=len("pass")
						lreturn=len("return ")
						lprint=len("print ")
						
						if tab=="":
							

							if codpython[0:lfor]=="for ":

								if ":" in codpython[lfor:]:
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								first=False
								primero=False
							elif codpython[0:lwhile]=="while ":
								
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif "print " in codpython[0:lprint]:
								
								if first==False:
									l.append(iden+codpython)				
								else:
									if primero==True:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[lprint:]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
									else:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[lprint:]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
										#estar pendiente de este primero ya que se hizo un cambio en la condicion
										primero=True
							elif "=" == codpython[0] and "=" != codpython[1]:
								
								if first==False:
									l.append(iden+"print "+codpython[1:])				
								else:
									if primero==True:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[len("="):]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
									else:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[len("="):]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
										#estar pendiente de este primero ya que se hizo un cambio en la condicion
										primero=True
				
							elif codpython[0:lif]=="if ":

								if ":" in codpython[lif:]:

								
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								first=False
								primero=False
								

							elif "else" in codpython[0:lelse]:
								first=False
								primero=False
								
								if ":" in codpython[lelse:]:
									iden=iden[:-2]
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								

							elif "try:" in codpython[0:ltry]:
								
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif "except" in codpython[0:lexcept]:
								iden=iden[:-2]
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif codpython[0:lelif]=="elif ":
								iden=iden[:-2]
								
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif codpython[0:lpass]=="pass" and len(codpython)==lpass:
								l.append("\n"+iden+codpython+"\n")
								iden=iden[:-2]
								first=False
								primero=False
							elif codpython[0:lreturn]=="return ":
								l.append("\n"+iden+codpython)
								iden=iden[:-2]
								first=False
								primero=False

							else:
								first=False
								primero=False
								

								
								if comentarios==None and (codpython[:3]=="'''" and "'''" not in codpython[3:] or codpython[:3]=='"""' and '"""' not in codpython[3:]):

									comentarios=codpython[:3]
									pass
								
								elif comentarios!=None and codpython[-3:]==comentarios:
									#and comentarios!=codpython[-3:]:
									#print codpython,"<br>"



								 	#print [comentarios,codpython[-3:]]
								 	#print comentarios==codpython[-3:]
									comentarios=None

									pass
								



								l.append("\n"+iden+codpython+"\n")

						else:
							

							liden=len(iden)

							
							
							if codpython[liden:liden+lfor]=="for ":
								
								first=False
								primero=False
								if ":" in codpython[liden+lfor:]:
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)

							elif codpython[liden:liden+lwhile]=="while ":
								first=False
								primero=False
								if ":" in codpython[liden+lwhile:]:
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)

							elif codpython[liden:liden+lif]=="if ":
								first=False
								primero=False
								if ":" in codpython[liden+lif:]:
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)



							elif "else" in codpython[liden-2:liden+lelse]:
								
								if ":" in codpython[liden+lelse:]:
									iden=iden[:-2]
									l.append("\n"+iden+codpython+"\n")
									iden+="  "
								else:
									l.append(iden+codpython)
								first=False
								primero=False

							elif "try:" in codpython[liden:liden+ltry]:
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif "except" in codpython[liden-2:liden+lexcept]:
								iden=iden[:-2]
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif codpython[liden-2:liden+lelif]=="elif ":
								iden=iden[:-2]
								l.append("\n"+iden+codpython+"\n")
								iden+="  "
								first=False
								primero=False
							elif codpython[:lpass]=="pass" and len(codpython)==lpass:
								l.append("\n"+iden+codpython+"\n")
								iden=iden[:-2]
								first=False
								primero=False
							
							elif codpython[liden:lreturn]=="return ":
								l.append("\n"+iden+codpython)
								iden=iden[:-2]
								first=False
								primero=False
							elif codpython[:lprint]=="print ":
								if first==False:
									l.append(iden+codpython)				
								else:
									if primero==True:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[lprint:]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
									else:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
							elif "=" == codpython[0] and "=" != codpython[1]:
								
								if first==False:
									l.append(iden+"print "+codpython[1:])				
								else:
									if primero==True:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[len("="):]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
									else:
										l.append("\n"+iden+"try: "+var+"+=str("+codpython[len("="):]+")\n"+iden+"except Exception as e:"+iden+" "+var+"+=str(e)\n")
										#estar pendiente de este primero ya que se hizo un cambio en la condicion
										primero=True
							


							else:



								l.append("\n"+iden+codpython)
								first=False
								primero=False
					

						
					
			

		else:
			l.append(t[HTML[0]:HTML[1]].replace("\n",""))#falta verificar el funcionamiento con el replace
		txt=""
		for elem in l:
			txt+=elem
		return txt
	else:

		return var+'+="""'+t.replace("\n","")+'"""'

def getPosTag(lista,strTag):
	for k,elem in enumerate(lista):
		if elem[0]==strTag:
			return k


def convertir3(t,etiquetas=[["{{","}}"]],etiquetas2=None,funcion=None,):
	
	i2=0

	temp_etiquetas=[]
	temp_etiquetas2=[]
	import sys
	
	sys.path.append(__file__[:__file__.rfind("/")]+"/../")
	from zred import normalizar

	for k,elem in enumerate(etiquetas):
		if temp_etiquetas!=[]:
			c2=1
			if len(elem)<=len(temp_etiquetas[0]):
				temp_etiquetas.insert(0,elem)
				temp_etiquetas2.insert(0,etiquetas2[k])
			else:
				while len(temp_etiquetas)<c2:
					if len(elem)<=len(temp_etiquetas[c2]):
						temp_etiquetas.insert(c2,elem)
						temp_etiquetas2.insert(c2,etiquetas2[k])
						break
					c2+=1
				if len(temp_etiquetas[-1])>len(elem):
					temp_etiquetas.insert(c2,elem)
					temp_etiquetas2.insert(c2,etiquetas2[k])
			
		else:
			temp_etiquetas.append(elem)
			temp_etiquetas2.append(etiquetas2[k])
			
	
	etiquetas=temp_etiquetas
	etiquetas2=temp_etiquetas2

	

	for k,elem in enumerate(etiquetas):
		hasContent=etiquetas2[k]
		for vez in range(t.count(elem[0])):

			

			i=t.find(elem[0])
			
			f=t.find(elem[1],i)

			tag=t[i:f]
			args={}
			
			if " " in tag:
				temp=tag.split(" ")
				plugin=temp[0]

				for at in temp[1:]:
					k,v=at.split("=")
					args[k]=normalizar(v)


				
				
			else:
				plugin=tag
				
			


			


			
			content=""

			f+=len(elem[1])


			if hasContent!=None:
				content=t[f:t.find(hasContent,f)]
				f=t.find(hasContent,f)+len(hasContent)
			
			t=t[:i]+str(funcion[plugin[1:]](args,content))+t[f:]


	return t

def convertir4(t,funcion,etiquetas=["{{","}}"]):
	i=0
	cadena=""

	while i<len(t)-1:
		pos=t.find(etiquetas[0],i)
		
		if pos!=-1:
			pos2=t.find(etiquetas[1],pos)
			cadena+=funcion(t[i:pos],t[pos+len(etiquetas[0]):pos2])
			i=pos2+len(etiquetas[1])
		else:
			cadena+=funcion(t[pos2+len(etiquetas[1]):],None)
			break

	return cadena

		
def generar2(rutahtml,rutapython,cabecera="",var="doc"):
	#vista html
	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(rutahtml)
	#vista pythonz

	if os.path.exists(rutapython):
		(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(rutapython)

		if mtime!=mtime2:
			try:

				f=open(rutahtml,"r")
				t=f.read()
				f.close()
				f=open(rutahtml,"w")				
				f.write(t)
				f.close()

				txt=convertir2(t,var=var)

				f=open(rutapython,"w")
				f.write(cabecera+txt)
				f.close()

				return True
			except Exception,e:
				print e
				print "Prueba colocar el contenido dentro de etiquetas"
	else:
			f=open(rutahtml,"r")
			t=f.read()
			f.close()
			
			f=open(rutahtml,"w")
			f.write(t)
			f.close()
		
			txt=convertir2(t,var=var)
			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()	
			return True
	return False	


def generar3(rutahtml,rutapython,funcion,cabecera=""):
	#vista html
	import os

	(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(rutahtml)
	#vista pythonz
	if os.path.exists(rutapython):
		(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(rutapython)

		if mtime!=mtime2:
			try:

				f=open(rutahtml,"r")
				t=f.read()
				f.close()
				f=open(rutahtml,"w")				
				f.write(t)
				f.close()

				txt=convertir4(t,funcion)
				mod=True
				if os.path.exists(rutapython):
					mod=False
				f=open(rutapython,"w")
				f.write(cabecera+txt)
				f.close()
				if mod:
					os.chmod(rutapython,755)

				return True
			except Exception,e:
				print e
				print "Prueba colocar el contenido dentro de etiquetas"
	else:
			f=open(rutahtml,"r")
			t=f.read()
			f.close()
			
			f=open(rutahtml,"w")
			f.write(t)
			f.close()
		
			txt=convertir4(t,funcion)
			mod=True
			if os.path.exists(rutapython):
				mod=False
			f=open(rutapython,"w")
			f.write(cabecera+txt)
			f.close()
			if mod:
				os.chmod(rutapython,755)	
			return True
	return False	
