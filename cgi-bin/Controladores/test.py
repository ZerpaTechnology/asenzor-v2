def ordenar(lista):
	l=[]
	for elem in lista:
		if " - " in elem:

			k,v=elem.split(" - ")
			if len(l)>0:

				a,b,c=v.split(".")
				for k2,elem2 in enumerate(l):
					if " - " in elem2:
						k3,v3=elem2.split(" - ")
						a2,b2,c2=v3.split(".")
						
						if int(a)<=int(a2) and int(b)<=int(b2) and int(c)<=int(c2):
							l.insert(k2,elem)
							break

					else:
						a2,b2,c2=elem2.split(".")
						if int(a)<=int(a2) and int(b)<=int(b2) and int(c)<=int(c2):
							l.insert(k2,elem)
							break
				if elem not in l:
					l.append(elem)

					
			else:
				l.append(elem)
		else:
			a,b,c=elem.split(".")
			for k2,elem2 in enumerate(l):
				if " - " in elem2:
						k3,v3=elem2.split(" - ")
						a2,b2,c2=v3.split(".")

						if int(a)<=int(a2) and int(b)<=int(b2) and int(c)<=int(c2):
							l.insert(k2,elem)
							break
						

				else:
						a2,b2,c2=elem2.split(".")
						if int(a)<=int(a2) and int(b)<=int(b2) and int(c)<=int(c2):
							l.insert(k2,elem)
							break
			if elem not in l:
				l.append(elem)
				break
	return l
lista=["a - 0.0.1","b - 0.0.20","c - 0.0.1","a - 0.0.10"]
print ordenar(lista)