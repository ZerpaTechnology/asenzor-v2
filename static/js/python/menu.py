
__pragma__("alias","s","$")

l=[]
for elem in s(".menu"):
	l.append(elem.text)

def change(evt):
	evt.preventDefault()
	try:
		if str(evt.target)=="<HTMLSpanElement object>":
			for elem in s(".menu").iterables:
				if elem.children[0]==evt.target:
					
						s(evt.target.parent).addClass("bg-bluelight")
				
						
				else:
					
					s(elem.parent).removeClass("bg-bluelight")
					s(elem).removeClass("bg-bluelight")
		else:
			for elem in s(".menu").iterables:
				if elem==evt.target:
					
						
					s(evt.target).addClass("bg-bluelight")
				else:
					
					s(elem.parent).removeClass("bg-bluelight")
					s(elem).removeClass("bg-bluelight")


		indice=l.index(evt.target.text)
		subs=s(".sub")
		
		if "hidden" in subs[indice].class_name:
			for elem in subs:
				if "hidden" not  in elem.class_name:
					elem.class_name+=" hidden"
			subs[indice].class_name=subs[indice].class_name.replace("hidden","")
			



		else:
			subs[indice].class_name+=" hidden"

		
	except Exception as e:
		window.alert(e)
		window.alert("===")

def change(evt):
	
	for k,elem in enumerate(s("#main-menu").find("span[name='menu']")):

		if elem!=evt.target:
			s(elem).removeClass("bg-bluelight")

			s(elem.parentNode.children[1]).addClass("hidden")
		else:

			s(evt.target).addClass("bg-bluelight")
			s(evt.target.parentNode.children[1]).removeClass("hidden")
	
for k,elem in enumerate(s("#main-menu").find("span[name='menu']")):
	s(elem).bind("click",change)


def change2(evt):

	if s("#menu").hasClass("hidden"):

		s("#menu").removeClass("hidden")
		s("#content").removeClass("col-sm-offset-1")
		s("#content").addClass("col-sm-offset-2")
		
	else:
		s("#menu").addClass("hidden")
		s("#content").addClass("col-sm-offset-1")
		s("#content").removeClass("col-sm-offset-2")
		
		
		
s("#btn-menu").bind("click",change2)