import zu
import copy
import os
def Builder(file):
	f=open(file,"r")
	script=f.read()
	f.close()
	lineas=script.split("\n")
	inclusiones={}
	codigo=""
	c=0
	piezas={}
	hechos=[]
	tigger=True
	#fase de lectura
	while c<len(lineas):
		linea_current=lineas[c]
	
		if "#:include " in  linea_current and "#:include force " not in  linea_current:

			pieza=linea_current[len("#:include "):].split(",")
			for elem in pieza:
				
				f=open(elem,"r")
				pieza_cod2=convertir(f.read())
				pieza_cod=pieza_cod2.split("\n")
				f.close()
				f=open("logs/log.kv","w")
				f.write(pieza_cod2)
				f.close()
				c2=0
				widget=""
				widgets=[]
				while c2<len(pieza_cod):

					if ">:" in pieza_cod[c2] and "<" in pieza_cod[c2]:
						tmp_widget=pieza_cod[c2].replace(">:",":").replace("<","")

						if "@" in tmp_widget:


								tmp_widget=tmp_widget[:tmp_widget.find("@")]+":"
								
								

						piezas[tmp_widget]=[]
						widget=tmp_widget
					else:
						if widget!="":
							if "@" in widget:
								widget=widget[:widget.find("@")]+":"
							
							
							piezas[widget].append(pieza_cod[c2])
							widgets.append(widget)
					c2+=1

		else:
			tab=zu.getTab(linea_current)
			temp_piezas=copy.copy(piezas)

			for elem in temp_piezas:

				if elem in linea_current and linea_current.replace("\n","").replace("\t","".replace(" ",""))==elem:
					c3=0
					wcod=""

					while c3<len(temp_piezas[elem]):
						linea_widget_current=temp_piezas[elem]
						c4=c+1
						tab2= zu.getTab(lineas[c4])
						#print "#################"
						#print [tab2],[lineas[c4]]
						while tab2 == zu.getTab(lineas[c4]):
							linea_current=lineas[c4]
							if ":" in linea_current and ":" != linea_current:
								v=linea_current.split(":")
							
							linea_widget_current=tab+temp_piezas[elem][c3]
							
							if linea_widget_current[:len(v[0])]== linea_current[:len(v[0])] and linea_current[:len(v[0])] not in hechos:
								
								temp_piezas[elem][c3]=linea_current[len(tab):]
								hechos.append(linea_current[:len(v[0])])
							c4+=1
						wcod+=tab+temp_piezas[elem][c3]+"\n"
						c3+=1

					codigo+=wcod

					c=c4-1

				else:
					if len(codigo)>=len(lineas[c]+"\n"):
						if codigo[-len(lineas[c]+"\n"):]!=lineas[c]+"\n":
							codigo+=lineas[c]+"\n"
					else:
						codigo+=lineas[c]+"\n"


		c+=1

	return codigo


def Builder2(file):
	f=open(file,"r")
	script=f.read()
	f.close()
	lineas=script.split("\n")
	inclusiones={}
	codigo=""
	c=0
	piezas={}
	hechos=[]
	tigger=True
	#fase de lectura
	codigo=""
	while c<len(lineas):
		linea_current=lineas[c]
		if "#:include " in  linea_current and "#:include force " not in  linea_current:
			l=linea_current[len("#:include "):].split(",")

			for elem in l:
				f=open(elem,"r")
				codigo+=convertir(f.read())
				f.close()
		else:
			codigo+=linea_current+"\n"
		c+=1

	return convertir(codigo)



def Builder3(file,root=None,screens=[],screens_folder="Screens/",debug=False):	
	try:
		script=""
		actualizarbase=False
		if file+".kv" in os.listdir("."):
			actualiza=False
			(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(file+".kv")
			
			for elem in os.listdir(screens_folder):
				
				if ".zkv" in elem:
					(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(screens_folder+elem)
					if abs(mtime-mtime2)>300:#actualiza
						f=open(screens_folder+elem,"r")
						r=f.read()
						f.close()
						f=open(screens_folder+elem,"w")
						f.write(r)
						f.close()
						f=open(screens_folder+elem[:-len(".zkv")]+".kv","w")
						con=convertir(r)
						f.write(con)
						f.close()
						script+=con
						actualiza=True
						actualizarbase=True
						
						
					elif elem[:-len(".zkv")]+".kv" not in os.listdir(screens_folder):#crea
						actualiza=True
						actualizarbase=True
						
						f=open(screens_folder+elem,"r")
						r=f.read()
						f.close()
						f=open(screens_folder+elem,"w")
						f.write(r)
						f.close()
						f=open(screens_folder+elem[:-len(".zkv")]+".kv","w")
						con=convertir(r)
						f.write(con)
						f.close()
						script+=con
					else:
						f=open(screens_folder+elem[:-len(".zkv")]+".kv","r")
						script+=f.read()
						f.close()
			if actualiza==False:
				f=open(file+".kv","r")
				resutl=f.read()
				f.close()
				return resutl
		else:

			for elem in os.listdir(screens_folder):
				if ".zkv" in elem:
					if elem[:-len(".zkv")]+".kv" not in os.listdir(screens_folder):#crea
						f=open(screens_folder+elem,"r")
						r=f.read()
						f.close()
						f=open(screens_folder+elem,"w")
						f.write(r)
						f.close()
						f=open(screens_folder+elem[:-len(".zkv")]+".kv","w")
						con=convertir(r)
						f.write(con)
						f.close()
						script+=con






		inclusiones={}
		codigo=""
		c=[0]
		piezas={}
		hechos=[]
		tigger=True
		"""
		#fase de lectura
		for elem in screens:
			if screens_folder+elem+".kv" in os.listdir(screens_folder):
				f=open(screens_folder+elem+".kv","r")
				script+=f.read()
				f.close()
			else:
				f=open(screens_folder+elem+".zkv","r")
				script+=f.read()
				f.close()
		if debug==True:
			f=open("logs/log5.kv","w")
			f.write(script)	
			f.close()
		
		script=convertir(script)
		"""


		l=[]
		o=None
		i=0
		nc=0
		ns=""

		for x in script:

			if (script[nc]=="'" or script[nc]=='"') and o==None:
				
				o=script[nc]
			elif script[nc]==o:

				o=None
			elif script[nc]=="\n" and o==None:
				l.append(script[i:nc].replace("\n","\\n"))
				
				i=nc+1
			nc+=1
		#l=script.split("\n")
		roots={}
		ncod=[""]
		ncod2=""
		
		def ordenar(l,c,roots,ncod,debug=debug):
				if "<" in l[c[0]] and ">:" in l[c[0]] and root not in l[c[0]]:
						
						if "@" in l[c[0]]:
							widget=l[c[0]][l[c[0]].find("<")+1:l[c[0]].find("@")]
						else:
							widget=l[c[0]][l[c[0]].find("<")+1:l[c[0]].find(">:")]
						
						tab=zu.getTab(l[c[0]])
						tab2=l[c[0]]
						
						roots[widget]=l[c[0]][len(tab):]+"\n"
						c2=c[0]
						
						c[0]+=1
						while c[0]<len(l) and (len(zu.getTab(l[c[0]]))>len(tab) or l[c[0]]==""):
							if "<" in l[c[0]] and ">:" in l[c[0]] and root not in l[c[0]]:
								ordenar(l,c,roots,ncod)
							else:
								if len(l[c[0]])>len(tab):
									
									roots[widget]+=l[c[0]][len(tab):]+"\n"
								
								c[0]+=1
						
						if debug==True:
							f=open("logs/log6_"+str(c2)+"-"+str(c[0])+".kv","w")
							f.write("["+tab2+"]\n"+roots[widget])	
							f.close()

						c[0]-=1
					

					

				else:
					#print "@@@@@@@"
					
					if len(l[c[0]])>len("#:include "):
						if "#:include " !=l[c[0]][:len("#:include ")]:
							ncod[-1]+=l[c[0]]+"\n"
					else:
						ncod[-1]+=l[c[0]]+"\n"
				
				
				c[0]+=1
			
		while c[0]<len(l):
				ordenar(l,c,roots,ncod)

		for elem in roots:
			ncod2+=roots[elem]
			
		if debug==True:
			f=open("logs/log6.kv","w")
			f.write(ncod2+ncod[0])	
			f.close()
		
		
		if file+".kv" not in os.listdir(".") or actualizarbase==True:
			f=open(file+".kv","w")
			f.write(ncod2+ncod[0])
			f.close()	
		return ncod2+ncod[0]	
		
	except Exception, e:
		return str(e)


	


		
		
def Builder4(script,root,widgets_folder="widgets/",debug=False):	
	
	
	inclusiones={}
	codigo=""
	c=[0]
	piezas={}
	hechos=[]
	tigger=True
	if debug==True:
		f=open("logs/log5.kv","w")
		f.write(script)	
		f.close()
	script=convertir(script)
	

	l=[]
	o=None
	i=0
	nc=0
	ns=""
	for x in script:

		if (script[nc]=="'" or script[nc]=='"') and o==None:
			
			o=script[nc]
		elif script[nc]==o:

			o=None
		elif script[nc]=="\n" and o==None:
			l.append(script[i:nc].replace("\n","\\n"))
			
			i=nc+1
		nc+=1
	#l=script.split("\n")
	roots={}
	ncod=[""]
	ncod2=""
	
	def ordenar(l,c,roots,ncod,debug=debug):
			if "<" in l[c[0]] and ">:" in l[c[0]] and root not in l[c[0]]:
					
					if "@" in l[c[0]]:
						widget=l[c[0]][l[c[0]].find("<")+1:l[c[0]].find("@")]
					else:
						widget=l[c[0]][l[c[0]].find("<")+1:l[c[0]].find(">:")]
					
					tab=zu.getTab(l[c[0]])
					tab2=l[c[0]]
					
					roots[widget]=l[c[0]][len(tab):]+"\n"
					c2=c[0]
					
					c[0]+=1
					while c[0]<len(l) and (len(zu.getTab(l[c[0]]))>len(tab) or l[c[0]]==""):
						if "<" in l[c[0]] and ">:" in l[c[0]] and root not in l[c[0]]:
							ordenar(l,c,roots,ncod)
						else:
							if len(l[c[0]])>len(tab):
								
								roots[widget]+=l[c[0]][len(tab):]+"\n"
							
							c[0]+=1
					
					if debug==True:
						f=open("logs/log6_"+str(c2)+"-"+str(c[0])+".kv","w")
						f.write("["+tab2+"]\n"+roots[widget])	
						f.close()

					c[0]-=1
				

				

			else:
				#print "@@@@@@@"
				
				if len(l[c[0]])>len("#:include "):
					if "#:include " !=l[c[0]][:len("#:include ")]:
						ncod[-1]+=l[c[0]]+"\n"
				else:
					ncod[-1]+=l[c[0]]+"\n"
			
			
			c[0]+=1
		
	while c[0]<len(l):
			ordenar(l,c,roots,ncod)

	for elem in roots:
		ncod2+=roots[elem]
		
	if debug==True:
		f=open("logs/log6.kv","w")
		f.write(ncod2+ncod[0])	
		f.close()
	return ncod2+ncod[0]

def ids(app):
	return app.root.current_screen.ids
def ajax(data=None,clear=False,path="ajax.dict"):
	if data==None:
		
		f=open(path,"r")
		script=f.read()
		f.close()

		exec("dic={"+script+"}")

		return dic
	else:
	
		f=open(path,"r")
		script=f.read()
		f.close()
		exec("dic={"+script+"}")
		dic.update(data)
		script=str(dic)[1:-1]

		
		f=open(path,"w")
		f.write(script)
		f.close()
		return True
		

	

def convertir(t=None,file=None,d={},debug=False):
	try:
		import intervalor.intervalo as i
		import sys
		
		import zu
		def incluir(widget,data={},folder="widgets/",tab="",convertir=convertir):
			global __builtins__

			open=__builtins__["open"]
			dir=__builtins__["dir"]		
			str=__builtins__["str"]		
			z=__builtins__["__import__"]("lib.ztec")
			zu=z.ztec.zu

			a=open(folder+widget+".zkv","r")
			#dentro de zkv
			s=a.read()

	
			a.close()
			c=0

			
			
			return "#"+widget+":\n"+zu.tabular(convertir(s,file=widget,d=data),tab)
		
			


		if file!=None and t==None:
			f=open(t,"r")
			t=f.read()
			f.close()
		elif t==None and file==None:
			pass

		t+="\n"
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
					giden=""
					if t[html[0]:html[1]][0]=='"' or t[html[0]:html[1]][-1]=='"':
						c0=-1
						while c0>-len(t[html[0]:html[1]]) and (t[html[0]:html[1]][c0]=="\t" or t[html[0]:html[1]][c0]==" "):
							giden+=t[html[0]:html[1]][c0]

							c0-=1
						
						codhtml="zkv+= '''"+t[html[0]:html[1]]+"'''"+"\n"
						
					elif t[html[0]:html[1]][0]=="'" or t[html[0]:html[1]][-1]=="'":
						c0=-1
						while c0>-len(t[html[0]:html[1]]) and (t[html[0]:html[1]][c0]=="\t" or t[html[0]:html[1]][c0]==" "):
							giden+=t[html[0]:html[1]][c0]

							c0-=1
						
						codhtml='zkv+= """'+t[html[0]:html[1]]+'"""'+"\n"
					else:
						c0=-1
						while c0>-len(t[html[0]:html[1]]) and (t[html[0]:html[1]][c0]=="\t" or t[html[0]:html[1]][c0]==" "):
							giden+=t[html[0]:html[1]][c0]

							c0-=1
						
						codhtml="zkv+= '''"+t[html[0]:html[1]]+"'''"+"\n"
					
					if codhtml!="zkv+= ''":
						

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
							lprint=len("print ")
							lreturn=len("return ")
							lincluir=len("incluir(")
							
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
								elif codpython[0:lprint]=="print ":

									if "incluir(" in codpython:
										ini=codpython.find("incluir(")
										fin=codpython.find(")",ini)
										_c=ini
										o=0
										d2="{}"
										while _c<fin:

											if codpython[_c]=="{":
												if o==0:
													dini=_c
												o+=1

											elif  codpython[_c]=="}":
												o-=1
												if o==0:
													d2=codpython[dini:_c+1]


											_c+=1
										
										l.insert(-1,iden+"data="+d2+"\n")
										codpython= codpython[:codpython.find(")",ini)]+",tab='"+giden+"'"+codpython[codpython.find(")",ini):]
										codpython[:codpython.find(")",ini)]+",tab='"+giden+"'"+codpython[codpython.find(")",ini):]
									
									
									l[-1]=l[-1][:-1]+"+"+iden+""+"str("+codpython.replace("print ","")[:-1]+")\n"

								
									
			

									#iden=iden[:-2]
									

								elif codpython[:1]=="=" and codpython[:2]!="=":
									l[-1]=l[-1][:-1]+"+"+iden+"str("+codpython.replace("print ","")[:-1]+")\n"

									
									
									#iden=iden[:-2]
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
							
									"""	
									elif codpython[liden-2:liden+lprint]=="print ":
										print "siiii"
										#iden=iden[:-2]
										l.append(iden+codpython)
										#iden+="  "
									"""
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
			#aqui esta la verdadera data
			txt="\nfile='"+str(file)+"'\ndata="+str(d)+"\nzkv=''\n"
			for elem in l:
				txt+=elem
			f2=open("log4.kv","w")
			f2.write(txt)
			f2.close()
			exec(txt)

			l=zkv.split("\n")
			
			c2=0
			ncod=""
			for elem in l:
				c=0
				e=""
				while c<len(elem) and elem!="" and (elem[c]==" " or elem[c]=="\t"):
					c+=1

				if c!=len(elem):
					if elem[0]=="\t":
						e=elem[1:]+"\n"
					else:
						e=elem+"\n"

				
				ncod+=e

				c2+=1
			return zkv
		else:

			return t
			
	except Exception,e:
		print "Error al convertir"
		print "Quizas son parametros que no has pasado en la data"
		print e

def errores(error):
	quizas="\nQuizas sea: \n"
	e="""
		Traceback (most recent call last):
File "main.py", line 131, in <module>
 Builder.load_file("logs/log2.kv")		
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1842, in load_file
 return self.load_string(data, **kwargs)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1889, in load_string
 parser = Parser(content=string, filename=fn)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1264, in __init__
 self.parse(content)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1366, in parse
 objects, remaining_lines = self.parse_level(0, lines)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1470, in parse_level
 level + 1, lines[i:], spaces)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1470, in parse_level
 level + 1, lines[i:], spaces)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1470, in parse_level
 level + 1, lines[i:], spaces)
File "/usr/lib/python2.7/dist-packages/kivy/lang.py", line 1529, in parse_level
 if current_property[:3] == 'on_':
TypeError: 'NoneType' object has no attribute '__getitem__'
		"""
	l=[e]
	for elem in l:
		if str(error) in elem:
			return quizas+"""recuerda que el embevido debe estar al mismo nivel que el kv
			ejemplo:

			{{for btn in btns:}}	
			Button:
				text: '{{print btn["text"]}}'
				height: 30
				{{if True:}}
				Image:
					source: ""
					height: 100
					
					
				{{pass}}
			{{pass}}

			"""