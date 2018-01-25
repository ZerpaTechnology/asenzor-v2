Component=nuclear.Component
from Widget import Widget
__pragma__("alias","s","$")
class BoxText(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="""
		<h1 class='titulo'></h1>
		<div class='content'> 
		</div>
		"""
		
		
		self._update=True
		

		
		self.textos=[]

	def text(self,cadena,estilos=None):
		lcadena=cadena.split(".\n")
		if self._update:
			p=s(("<p>{}</p>".repeat(len(lcadena))).format(*lcadena))
			if estilos!=None:
				p.css(estilos)
			self.target.find(">.content").html(p)


		else:
			self.textos.html(self.target.find(">.content").append(("<p>{}</p>".repeat(len(lcadena))).format(*lcadena)))
	def h3(self,cadena,estilos=None):
		lcadena=cadena.split("\n")
		if self._update:
			_h3=s(("<h3>{}</h3>".repeat(len(lcadena))).format(*lcadena))
			if estilos!=None:
				_h3.css(estilos)
			self.target.find(">.content").append(_h3)


		else:
			self.textos.append(self.target.find(">.content").append(("<h3>{}</h3>".repeat(len(lcadena))).format(*lcadena)))
	def h4(self,cadena,estilos=None):
		lcadena=cadena.split("\n")
		if self._update:
			_h4=s(("<h4>{}</h4>".repeat(len(lcadena))).format(*lcadena))
			if estilos!=None:
				_h4.css(estilos)
			self.target.find(">.content").append(_h4)


		else:
			self.textos.append(self.target.find(">.content").append(("<h4>{}</h4>".repeat(len(lcadena))).format(*lcadena)))
	def h5(self,cadena,estilos=None):
		lcadena=cadena.split("\n")
		if self._update:
			_h5=s(("<h5>{}</h5>".repeat(len(lcadena))).format(*lcadena))
			if estilos!=None:
				_h5.css(estilos)
			self.target.find(">.content").append(_h3)


		else:
			self.textos.append(self.target.find(">.content").append(("<h5>{}</h5>".repeat(len(lcadena))).format(*lcadena)))
	def h2(self,cadena,estilos=None):
		lcadena=cadena.split("\n")
		if self._update:
			_h2=s(("<h2>{}</h2>".repeat(len(lcadena))).format(*lcadena))
			if estilos!=None:
				_h2.css(estilos)
			self.target.find(">.content").append(_h2)


		else:
			self.textos.append(self.target.find(">.content").append(("<h2>{}</h2>".repeat(len(lcadena))).format(*lcadena)))
	
	def img(self,url,estilos=None):
		i=s("<img url='{}'>".format(url))
		self.target.find(">.content").append(i)
		if estilos!=None:
			i.css(estilos)
	def b(self,cadena,estilos=None):
		lcadena=cadena.split("\n")

		if self._update:
			_b=s(("<b>{}</b>".repeat(len(lcadena))).format(*lcadena))
			if estilos!=None:
				_b.css(estilos)
			self.target.find(">.content").append(b)
		else:
			self.textos.append(self.target.find(">.content").append(("<b>{}</b>".repeat(len(lcadena))).format(*lcadena)))

	def span(self,cadena,estilos=None):
		lcadena=cadena.split("\n")
		if self._update:
			_span=("<span>{}</span>".repeat(len(lcadena))).format(*lcadena)
			if estilos!=None:
				_span.css(estilos)
			self.target.find(">.content").append(_span)
		else:
			self.textos.append(self.target.find(">.content").append(("<span>{}</span>".repeat(len(lcadena))).format(*lcadena)))
	def lista(self,lista,estilos=None,selector=None):
		def listar(l):
			cad="<ul>"
			for elem in l:
				if type(elem)!=list:
					cad+="<li>{}</li>".format(elem)
				else:
					cad+="<li>{}</li>".format(listar(elem))
			cad+="</ul>"
			return cad
		l=s(listar(lista))
		self.target.find(">.content").append(l)
		if estilos!=None and selector!=None:
			l.find(selector).css(estilos)

		elif estilos!=None and selector==None:
			l.css(estilos)
		




	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.__titulo=self.target.find(">.titulo")
		self.__content=self.target.find(">.content")
		self.__titulo.text(self._titulo)
		for elem in self.textos:
			self.target.find(">.content").append(elem)

	
	
		


		