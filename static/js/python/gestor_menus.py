#!/usr/bin/python
__pragma__("alias","s","$")
var_update="""
$( "#accordion" ).accordion({
  collapsible: true
});
$( ".accordion" ).accordion({
  collapsible: true,
  active:false
});
$( "ul.droptrue" ).sortable({
connectWith: "ul"
});
$( "ul.dropfalse" ).sortable({
connectWith: "ul",
dropOnEmpty: false
});
$( ".sortable" ).disableSelection();

"""
config=Config.Config()
normalizar=nuclear.normalizar
rest=nuclear.getRest()
VAR=nuclear.VAR
def render(menu):
	cadena=""
	for elem in menu:
		cadena+=elem["name"]+"\n"
		if elem["children"]!=[]:
			cadena+=" "+render(elem["children"])+"\n"
	return cadena

class Gestor(object):
	"""docstring for gestor"""
	def __init__(self, selector):
		self.selector=selector
		
		self.rest=nuclear.getRest()
		self.nombre=None
		global config
		

		
		
		self.menus=VAR("Menus")

		self.nuevo=None
		def select_menu(evt,menu=None):

			def mapear(menu):
				mapa=''

				for elem in menu:
					
					mapa+='<li><li class="ui-state-default" >'+"""
					<div class="accordion" style="display: inline-block;width: 100%">
						<h3 ><span>"""+elem["name"]+"""</span></h3>
						<div class="pad-1" style="max-height: 120px">
							<b class="d-block">Etiqueta de navegación</b>
							<input type="" name="nombre" placeholder="" value='"""+elem["name"]+"""'>
							<div>Enlace:<span name="url">"""+construir(elem["url"])+"""</span></div>
							
						    <input type='hidden' name='modelo' value='"""+(elem["url"][0] if type("url")==list else "")+"""'>
						    <input type='hidden' name='tabla' value='"""+(elem["url"][1] if type("url")==list else "")+"""'>
						    <input type='hidden' name='indice' value='"""+(elem["url"][2] if type("url")==list else "")+"""'>
						    <input type='hidden' name='control' value='"""+(elem["url"][3] if type("url")==list else "")+"""'>
						    <input type='hidden' name='metodo' value='"""+(elem["url"][4] if type("url")==list else "")+"""'>
							<div><b>Mover a:</b><span class="blue">Abajo</span></div>
							<div>Original: Inicio</div>
							<div><b class="red">eliminar</b>|<b class="blue">Cancelar</b></div>
							</div>
						</div>
					</div>
					"""+'<ul  class="sortable droptrue marg-l2" style="min-height: 5px">'+mapear(elem["children"])+'</ul></li>' 
				
						

				mapa+='</li>' 
				
				return mapa
			if menu==None:
				for k,option in enumerate(s("select[name='seleccionar-menu']")[0].children):
					if option.selected:
						
						s(self.selector)[0].innerHTML=mapear(self.menus[k-1][1][0])
						for elem in self.menus[k-1][1][1]:
								if elem=="nivel-superior":
									s("input[name='nivel-superior']")[0].checked=self.menus[k-1][1][1][elem]
								if elem=="menu-principal":
									s("input[name='menu-principal']")[0].checked=self.menus[k-1][1][1][elem]
								if elem == "menu-pie":
									s("input[name='menu-pie']")[0].checked=self.menus[k-1][1][1][elem]
								if elem=="menu-barra-superior":
									s("input[name='menu-barra-superior']")[0].checked=self.menus[k-1][1][1][elem]
								if elem=="menu-mi-cuenta":
									s("input[name='menu-mi-cuenta']")[0].checked=self.menus[k-1][1][1][elem]
						eval(var_update)
						self.nombre=self.menus[k-1][0]
						self.nuevo=k-1
						break
			else:
				s(self.selector)[0].innerHTML=mapear(self.menus[menu][1][0])
				for k,option in enumerate(s("select[name='seleccionar-menu']")[0].children):
					if k-1==menu:
						option.selected=True
						self.nombre=self.menus[k-1][0]
						self.nuevo=k-1
						for elem in self.menus[k-1][1][1]:
								if elem=="nivel-superior":
									s("input[name='nivel-superior']")[0].checked=self.menus[k-1][1][1][elem]
								if elem=="menu-principal":
									s("input[name='menu-principal']")[0].checked=self.menus[k-1][1][1][elem]
								if elem == "menu-pie":
									s("input[name='menu-pie']")[0].checked=self.menus[k-1][1][1][elem]
								if elem=="menu-barra-superior":
									s("input[name='menu-barra-superior']")[0].checked=self.menus[k-1][1][1][elem]
								if elem=="menu-mi-cuenta":
									s("input[name='menu-mi-cuenta']")[0].checked=self.menus[k-1][1][1][elem]

			eval(var_update)

			

			
			s(self.selector+" input[name='nombre']").bind("keyup",escribir)
			
			"""
			for k,elem in enumerate(s("select[name='seleccionar-menu']")[0].children):
				if elem.text==
				s(self.selector)[0].innerHTML=maprear(self.menus[k])
			"""
		
		
		
				
		
		def clear_flechas():
			
			for elem in s(".accordion > H3"):
				cantidad=s(elem).find(".ui-accordion-header-icon")
				padre=cantidad[0].parentNode
				while len(cantidad)>1:
					padre.removeChild(cantidad[-1])
					cantidad.pop()
		def construir(url):
			
			if type(url)==list:
				return config.base_url+self.rest["app"]+("/"+url[3] if url[3]!="" else "")+("/"+url[4] if url[4]!="" else "")
			else:
				return url			


			
		def add_to_menu(evt):
			global var_update
			caja=s(s(evt.target).prev()).prev()[0]
			etiquetas=[]
			for elem in caja.children:
				
				if s(elem).find("input[type='checkbox']")[0].checked==True:
					etiquetas.append(s(elem).find("b")[0])
			for elem in etiquetas:
				
				s(self.selector)[0].innerHTML+='<li><li class="ui-state-default" >'+"""
				<div class="accordion" style="display: inline-block;width: 100%">
				<h3 ><span>"""+elem.text+"""</span></h3>
				<div class="pad-1" style="max-height: 120px">
					<b class="d-block">Etiqueta de navegación</b>
					<input type="" name="nombre" placeholder="" value='"""+elem.text+"""'>
					<div>Enlace:<span name="url">"""+elem.getAttribute("href")+"""</span></div>
					
					<input type='hidden' name='modelo' value='"""+elem.getAttribute("modelo")+"""'>
					<input type='hidden' name='tabla' value='"""+elem.getAttribute("tabla")+"""'>
					<input type='hidden' name='indice' value='"""+elem.getAttribute("indice")+"""'>
					<input type='hidden' name='control' value='"""+elem.getAttribute("control")+"""'>
					<input type='hidden' name='metodo' value='"""+elem.getAttribute("metodo")+"""'>

					<div><b>Mover a:</b><span class="blue">Abajo</span></div>
					<div>Original: Inicio</div>
					<div><b class="red">eliminar</b>|<b class="blue">Cancelar</b></div>
					</div>
				</div></div>
				"""+'<ul  class="sortable droptrue marg-l2" style="min-height: 5px"></ul></li></li>'
			eval(var_update)
			clear_flechas()
			s(self.selector+" input[name='nombre']").bind("keyup",escribir)
		
		def add_to_menu2(evt):
			"""
			Para enlaces personalizados
			"""
			global var_update
			text=s(evt.target).prev().find("input[name='custom-text']")[0]
			url=s(evt.target).prev().find("input[name='custom-url']")[0]

			s(self.selector)[0].innerHTML+='<li><li class="ui-state-default" >'+"""
				<div class="accordion" style="display: inline-block;width: 100%">
				<h3 ><span>"""+text.value+"""</span></h3>
				<div class="pad-1" style="max-height: 120px">
					<b class="d-block">Etiqueta de navegación</b>
					<input type="" name="nombre" placeholder="" value='"""+text.value+"""'>
					<div>Enlace:<span name="url">"""+url.value+"""</span></div>
					
					<input type='hidden' name='modelo' value=''>
					<input type='hidden' name='tabla' value=''>
					<input type='hidden' name='indice' value=''>
					<input type='hidden' name='control' value=''>
					<input type='hidden' name='metodo' value=''>

					
					<div><b>Mover a:</b><span class="blue">Abajo</span></div>
					<div>Original: Inicio</div>
					<div><b class="red">eliminar</b>|<b class="blue">Cancelar</b></div>
					</div>
				</div></div>
				"""+'<ul  class="sortable droptrue marg-l2" style="min-height: 5px"></ul></li></li>'
			window.eval(var_update)
		def select_all(evt):
			caja=s(evt.target).previousSibling.children[0].children
			for elem in caja:
				elem.children[0].checked=True

		def save_menu(evt):
			def mapear(menu):
				l=[]
				for elem in menu.children:
					if len(elem.children)>0:
						nombre=elem.children[0].children[1].find("input[name='nombre']")[0].value
						
						if ( elem.children[0].children[1].find("input[name='tabla']")[0].value.strip()!=""
							or  elem.children[0].children[1].find("input[name='modelo']")[0].value.strip()!=""
							or  elem.children[0].children[1].find("input[name='indice']")[0].value.strip()!=""
							or  elem.children[0].children[1].find("input[name='control']")[0].value.strip()!=""
							or elem.children[0].children[1].find("input[name='metodo']")[0].value.strip()!=""):

							url=[normalizar(elem.children[0].children[1].find("input[name='modelo']")[0].value.strip()),
							     normalizar(elem.children[0].children[1].find("input[name='tabla']")[0].value.strip()),
							     normalizar(elem.children[0].children[1].find("input[name='indice']")[0].value.strip()),
							     normalizar(elem.children[0].children[1].find("input[name='control']")[0].value.strip()),
							     elem.children[0].children[1].find("input[name='metodo']")[0].value.strip()]
						else:
							url=elem.children[0].children[1].find("span[name='url']")[0].text

						#[elem,hijos]
						l.append({"name":nombre,"url":url,"children":mapear(elem.children[1])})
				
				return l

			estructura=[mapear(s("#nav-menu")[0])]

			
			estructura.append({"nivel-superior":s("input[name='nivel-superior']")[0].checked,
							   "menu-principal":s("input[name='menu-principal']")[0].checked,
							   "menu-pie":s("input[name='menu-pie']")[0].checked,
							   "menu-barra-superior":s("input[name='menu-barra-superior']")[0].checked,
							   "menu-mi-cuenta":s("input[name='menu-mi-cuenta']")[0].checked,
							   })
			
			if s("input[name='nombre-menu']")[0].value.strip()!="":
				self.nombre=s("input[name='nombre-menu']")[0].value.strip()
			
			if self.nombre!=None:
				#para las listas hay que transformarla en str para poder enviarlas
				
				
				data={"app":self.rest["app"],
						 "metodo":self.rest["metodo"],
						 "action":"save-menu",
						 "control":self.rest["control"],
						 "menu":str(estructura),
						 "nombre":self.nombre,
						 "nuevo":self.nuevo}
				s.ajax({
					"data":data,
					"url":config.base_url,
					"method":"POST",
					}).done(lambda data:(alert(data),print("================\n"),print(data))
					)
				

				
			else:
				alert("debes darle nombre al menu")
				
		


		def escribir(evt):
			
			evt.target.parentNode.parentNode.children[0].children[1].text=evt.target.value

		
		s("button[name='add-to-menu']").bind("click",add_to_menu)
		s("button[name='add-to-menu2']").bind("click",add_to_menu2)
		s("span[name='seleccionar-todo']").bind("click",select_all)
		s("button[name='guardar-menu']").bind("click",save_menu)
		s("button[name='aplicar-menu']").bind("click",select_menu)





window.Gestor=Gestor