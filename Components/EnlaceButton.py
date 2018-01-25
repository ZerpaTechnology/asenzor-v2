__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class EnlaceButton(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		Widget.__init__(self,titulo)		
		self._html="""
		<button>{}</button>
		"""
		self.name=""
		self.placeholder="Nuevo nombre"
		self.btn="Añadir"
		self._atras=atras
		self.activador=None
		self.value=None
		self.open=False
		self.submit=None
		self.color="blue"

	def click(self):
		if self.activador!=None:
			self.activador(self)


	def send(self,evt=None):
		self.value=s(self.target).find(">.content").find(">input").val()
		if self.submit!=None:
			self.submit(self)

	def enter(self,evt):
		if evt.keyEnter==True:
			if self.submit!=None:
				self.submit(self)
	
	def update(self):

		s(self.target).html(self._html.format(self.titulo))
		self.target.find(">button").css("color",self.color)

		
		
	