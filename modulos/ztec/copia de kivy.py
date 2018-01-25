import zu
import copy
def Builder(file):
	f=open(file,"r")
	script=f.read()
	f.close()
	lineas=script.split("\n")
	inclusiones={}
	codigo=""
	lwidget=[]
	c4=0
	for i,linea in enumerate(lineas):
		print "\n"
		print "linea:",[linea]
		if linea[:len("#:include ")]=="#:include ":
			if "force " in linea[len("#:include "):]:
				pass
			else:

				includes=linea[len("#:include "):].split(",")
				for elem in includes:
					f=open(elem,"r")
					inclusion=f.read().split("\n")
					f.close()
					inicio=True
					widget=""

					for incluir in inclusion:
						if incluir!="":
							if ">:" in incluir:
								lwidget.append(incluir.replace("<","").replace(">","")+"\n")
								widget=incluir.replace("<","").replace(">","")

								if inicio==False:
									inclusiones[widget]=temp

									lwidget=[]
								else:
									inicio=False
							else:
								lwidget.append(incluir.replace("<","").replace(">","")+"\n")
								
								
						else:
							lwidget.append(incluir+"\n")
					if lwidget!=[]:
						inclusiones[widget]=lwidget
						

		for elem in inclusiones:
			if  elem in linea:

				c=i+1
				#print c4
				c4+=1
				if c<len(lineas):
					tab=zu.getTab(lineas[c])
					tab2=zu.getTab(lineas[i])
					principio=0
					inclusion=""
					
					while tab==zu.getTab(lineas[c]):

						if ":" in lineas[c] and ":" != lineas[c]:
							c2=1
							v=lineas[c].split(":")
							vez=[]
							while c2<len(lwidget):
								lwidget=copy.copy(inclusiones[elem])
								lwidget[c2]=tab2+lwidget[c2]
								
								
								if v[0]== lineas[c][:len(v[0])] and v[0]==lwidget[c2][:len(v[0])] and lineas[c][:len(v[0])] not in vez :
									#print [lineas[c][:len(v[0])]]," ",[lwidget[c2][:len(v[0])]]		
									inclusion+="#"+lineas[c]+"\n"
									vez.append(tab2+lwidget[c2][:len(v[0])])
									#print vez
								else:
									inclusion+="@"+lwidget[c2]

								"""
								if v[0]== lineas[c][:len(v[0])] and v[0]==lwidget[c2][:len(v[0])] and lineas[c][:len(v[0])] not in vez :
									print [lwidget[c2]]," ",[lineas[c]]
									inclusion+="@"+lineas[c]
									vez.append(lineas[c][:len(v[0])])
									print inclusion
								else:
									inclusion+="@@"+lwidget[c2]
								"""
								c2+=1
						c+=1
					i=c

				lineas[i]=zu.getTab(linea)+elem+"\n"+inclusion
		codigo+=lineas[i]+"\n"
	return codigo








