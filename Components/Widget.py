__pragma__("alias","s","$")


			



class Widget(object):
	"""
	self.titulo #es un funcion que actualiza el titulo
	self._titulo #es el valor de la variable del titulo
	self.__titulo #es el target jquery del titulo
	"""
	def __init__(self,titulo=""):
		self._titulo=titulo
		self.target=s("<div class='"+self.__class__.__name__+"'></div>")
		self.target2=s("<div class='"+self.__class__.__name__+"'></div>")
		self.target3=s("<div class='"+self.__class__.__name__+"'></div>")
		self.target4=s("<div class='"+self.__class__.__name__+"'></div>")
		self.target5=s("<div class='"+self.__class__.__name__+"'></div>")

		self.content=lambda self=self,k=None:self.target#si no se crea un lugar especifico para el contendedor
		self.content2=lambda self=self,k=None:self.target#si no se crea un lugar especifico para el contendedor
		self.content3=lambda self=self,k=None:self.target#si no se crea un lugar especifico para el contendedor
		self.content4=lambda self=self,k=None:self.target#si no se crea un lugar especifico para el contendedor
		self.content5=lambda self=self,k=None:self.target#si no se crea un lugar especifico para el contendedor

		self._html=""
		self._html2=""
		self._html3=""
		self._html4=""
		self._html5=""

		self.media=None

		self.children=[]
		self.hermanos=[]
		self.children2=[]
		self.hermanos2=[]
		self.children3=[]
		self.hermanos3=[]
		self.children4=[]
		self.hermanos4=[]
		self.children5=[]
		self.hermanos5=[]

		self.value=None
		self.name=""
		self._update=False

		self.format=[self.titulo]
		self.format2=[self.titulo]
		self.format3=[self.titulo]
		self.format4=[self.titulo]
		self.format5=[self.titulo]

		self.primitivo=lambda self=self,k=None:self.target
		self.css_styles=[]
		self._descripcion=""
		self._sources=False
		self._load_js=[]
		self._load_css=[]
		self.parent=None
		self.parent2=None
		self.parent3=None
		self.parent4=None
		self.parent5=None
		self._last_js=None
		self.data={}
		self.dataChildren=[]




	def css(self,estilo1,estilo2=None,selector=None):
		if self._update:
			if type(estilo1)==str and type(estilo2)==str and selector==str:
				return self.target.find(selector).css(estilo1,estilo2)
			elif (type(estilo1)==str or type(estilo1)==dict) and estilo2==None and selector!=None:
				return self.target.find(selector).css(estilo1)
			elif type(estilo1)==dict and estilo2==None and selector==None:
				return self.target.find(selector).css(estilo1)

		else:
			self.css_styles.append([estilo1,estilo2,selector])
			
	def load_sources(self):
		if not self._sources:

			for css in self._load_css:

				for elem in s("link"):
					temp=css.split("/")
					cargar=False
					if s(elem).attr("href").endswith(temp[len(temp)-1]):
						cargar=True
						break
				if cargar==False:
					s("head").append("<link rel='stylesheet' href='{}'>".format(css))

			for js in self._load_js:
				
				for elem in s("script"):
					temp=js.split("/")
					cargar=False
					if s(elem).attr("src").endswith(temp[len(temp)-1]):
						cargar=True
						break
				if cargar==False:
					self._last_js=s("<script src='{}'></script>".format(js))

					s("head").append(self._last_js)

			
			def actualiza(evt):
				nonlocal self
				self._sources=True
			if self._last_js!=None:
				self._last_js.on("load",actualiza)

	def bind(self,evento,funcion,selector=None):
		if selector==None:
			self.target.bind(evento,funcion)
		else:
			s(self.target).find(selector).bind(evento,funcion)
	def addSeparador(self,hr=False):
		if hr:
			s(self.target).append("<hr>")
		else:
			s(self.target).append("<br>")
	def descripcion(self,descripcion):
		self.__descripcion.text(descripcion)
		self._descripcion=descripcion
	
	def add(self,target,n=1):
		self.format=[self.titulo]
		if "py_update" in dir(target):
			if self._update:
				target.update()
				self.children.append(target)
				self.dataChildren.append({})
				target._update=True
				if n==1:
					s.when(s(self.content(self)).append(target.target)).then(target.done)
					target.parent=self
				elif n==2:
					s.when(s(self.content(self)).append(target.target2)).then(target.done)
					target.parent2=self
				elif n==3:
					s.when(s(self.content(self)).append(target.target3)).then(target.done)
					target.parent3=self
				elif n==4:
					s.when(s(self.content(self)).append(target.target4)).then(target.done)
					target.parent4=self
				elif n==5:
					s.when(s(self.content(self)).append(target.target5)).then(target.done)
					target.parent5=self

				
			else:
				target.update()
				self.children.append(target)
		else:
			if n==1:
				s.when(s(self.content(self)).append(target)).then(target.done)
				target.parent=self
			elif n==2:
				s.when(s(self.content(self)).append(target)).then(target.done)
				target.parent2=self
			elif n==3:
				s.when(s(self.content(self)).append(target)).then(target.done)
				target.parent3=self
			elif n==4:
				s.when(s(self.content(self)).append(target)).then(target.done)
				target.parent4=self
			elif n==5:
				s.when(s(self.content(self)).append(target)).then(target.done)
				target.parent5=self


	def add2(self,target,n=1):
		self.format=[self.titulo]
		if self._update:
			target.update()
			self.children2.append(target)
			target._update=True
			self.dataChildren.append({})
			
			if n==1:
				s(self.content2(self)).append(target.target)
			elif n==2:
				s(self.content2(self)).append(target.target2)
			elif n==3:
				s(self.content2(self)).append(target.target3)
			elif n==4:
				s(self.content2(self)).append(target.target4)
			elif n==5:
				s(self.content2(self)).append(target.target5)
		else:
			target.update()
			self.children2.append(target)
	def add3(self,target,n=1):
		self.format=[self.titulo]
		if self._update:
			target.update()
			self.children3.append(target)
			target._update=True
			self.dataChildren.append({})
			
			if n==1:
				s(self.content3(self)).append(target.target)
			elif n==2:
				s(self.content3(self)).append(target.target2)
			elif n==3:
				s(self.content3(self)).append(target.target3)
			elif n==4:
				s(self.content3(self)).append(target.target4)
			elif n==5:
				s(self.content3(self)).append(target.target5)
		else:
			target.update()
			self.children3.append(target)
	def add4(self,target,n=1):
		self.format=[self.titulo]
		if self._update:
			target.update()
			self.children4.append(target)
			target._update=True
			self.dataChildren.append({})
			
			if n==1:
				s(self.content4(self)).append(target.target)
			elif n==2:
				s(self.content4(self)).append(target.target2)
			elif n==3:
				s(self.content4(self)).append(target.target3)
			elif n==4:
				s(self.content4(self)).append(target.target4)
			elif n==5:
				s(self.content4(self)).append(target.target5)
		else:
			target.update()
			self.children4.append(target)
	def add5(self,target,n=1):
		self.format=[self.titulo]
		if self._update:
			target.update()
			self.children5.append(target)
			target._update=True
			self.dataChildren.append({})
			if n==1:
				s(self.content5(self)).append(target.target)
			elif n==2:
				s(self.content5(self)).append(target.target2)
			elif n==3:
				s(self.content5(self)).append(target.target3)
			elif n==4:
				s(self.content5(self)).append(target.target4)
			elif n==5:
				s(self.content5(self)).append(target.target5)
		else:
			target.update()
			self.children5.append(target)

	def show(self):
		self.target.show()

	def hidden(self):
		self.target.hide()

	def titulo(self,titulo):
		self.__titulo.text(titulo)
		self._titulo=titulo

	def val(self):
		value={self.name:[]}
		if self.children!=[]:
			for elem in self.children:
				value[self.name]=elem.val()
			return value
		else:
			return self.value
	def clone(self,target):
		
		
		def copy(objeto):
			if "__class__" in dir(objeto):
				if objeto.prototype!=None: 
					
					o=__new__(objeto.prototype.constructor)
					for elem in dir(o):
						if __pragma__("js","{}"," typeof getattr(o,elem)!='function'"):
							setattr(o,elem,copy(getattr(objeto,elem)))
					
				else:
					
					if __pragma__("js","{}","objeto.__proto__.constructor==Array"):
						l=[]
						for elem in objeto:
							l.append(copy(elem))
						o=Object.assign([],l)
					elif objeto==None:
						o=objeto
					elif __pragma__("js","{}","objeto.__proto__.constructor==String") or __pragma__("js","{}","objeto.__proto__.constructor==Number") or __pragma__("js","{}","objeto.__proto__.constructor==Boolean"):
						o=objeto
					elif __pragma__("js","{}","objeto.__proto__.constructor==Function") :
						o=objeto.prototype.constructor
					else:
						
						d={}
						for elem in objeto:
							
							d[elem]=copy(objeto[elem])				
						o=Object.assign({},d)


			else:
				if type(objeto)==str or type(objeto)==int or type(objeto)==float or type(objeto)==bool:
					
					o=objeto.valueOf()
				elif type(objeto)!=str and type(objeto)!=int and type(objeto)!=float and type(objeto)!=bool and type(objeto)!=None:
					o=objeto
				
				else:
					o=objeto

			return o
		
		

		
		clon=copy(self)
		

		
		def clonarChildren(widget):
			l=[]
			for k,elem in enumerate(widget.children):
				widget.children[k]=copy(widget.children[k])
				widget.children[k].target=s(elem.target[0].outerHTML)
				widget.children[k].target2=s(elem.target2[0].outerHTML)
				widget.children[k].target3=s(elem.target3[0].outerHTML)
				widget.children[k].target4=s(elem.target4[0].outerHTML)
				widget.children[k].target5=s(elem.target5[0].outerHTML)

				l.append(clonarChildren(widget.children[k]))
			widget.children=l
			return widget
		clonarChildren(clon)
		clon.target=s(clon.target[0].outerHTML)
		clon.target2=s(clon.target2[0].outerHTML)
		clon.target3=s(clon.target3[0].outerHTML)
		clon.target4=s(clon.target4[0].outerHTML)
		clon.target5=s(clon.target5[0].outerHTML)
		clon.reload()

		
		return clon


	def done(self):
		pass

	
	def __update__(self):
		
		self._update=True
		self.load_sources()
		

			
			
		
		self.target.html(self._html.format(*self.format))
		self.target2.html(self._html2.format(*self.format2))
		self.target3.html(self._html3.format(*self.format3))
		self.target4.html(self._html4.format(*self.format4))
		self.target5.html(self._html5.format(*self.format5))

		if self.children!=[]:
			for k,elem in enumerate(self.children):
				if type(elem)==list:
					for k2,elem2 in enumerate(elem):
						if self.content!=None:
							s(self.content(self,k,k2)).append(elem.target)

				else:
					if self.content!=None:

						s(self.content(self,k)).append(elem.target)
		if self.css_styles!=[]:
			for elem in self.css_styles:
				self.css(elem[0],elem[1],elem[2])


		self.__titulo=self.target.find(">.titulo")

		

	def update(self):
		self.__update__()


	def reload(self):
		self.update()
		for elem in self.children:
			elem.update()

	def updateData(self,data):
		for elem in data.keys():
			setattr(self,elem,data[elem])
		


	def run(self,selector=".widget"):
		self.update()
		s(selector).append(self.target)

	def run2(self,selector=".widget"):
		self.update()
		s(selector).append(self.target2)
	
	def run3(self,selector=".widget"):
		self.update()
		s(selector).append(self.target3)
	
	def run4(self,selector=".widget"):
		self.update()
		s(selector).append(self.target4)
	
	def run5(self,selector=".widget"):
		self.update()
		s(selector).append(self.target5)


