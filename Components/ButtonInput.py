__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class ButtonInput(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		Widget.__init__(self,titulo)		
		self._html="""
		<button>{}</button>
		<div class='content'>
		<input name='{}' placeholder='{}'>
		<button>{}</button>
		</div>
		"""
		self.name=""
		self.placeholder="Nuevo nombre"
		self.btn="Añadir"
		self._atras=atras
		self.activador=None
		self.value=None
		self.placeholder=""
		self.open=False
		self.submit=None
		self.height=0

	def click(self):
		if self.open:
			self.cerrar()
		else:
			self.abrir()
	def cerrar(self):
		s(self.target).find(">.content").animate({"height":"0px","padding":"0px"},1000,lambda: s(self.target).find(">.content").css({"height":"0px","padding":"0px"}))
		self.open=False

	def abrir(self):

		def abrir():
			nonlocal self
			s(self.target).find(">.content").css({"height":"auto","padding":"5px"})
		s(self.target).find(">.content").animate({"height":str(self.height)+"px","padding":"5px"},1000,abrir) 
		
		self.open=True

	def send(self,evt=None):
		self.value=s(self.target).find(">.content").find(">input").val()
		if submit!=None:
			self.submit(self)
		self.cerrar()

	def enter(self,evt):
		if evt.keyEnter==True:
			self.submit(self)
			self.cerrar()
	
	def update(self):
		
		s(self.target).html(self._html.format(self.titulo,self.name,self.placeholder,self.btn))
		def recargar():
			nonlocal self
			self.height=s(self.target).find(">.content").outerHeight()
			s(self.target).find(">.content").css({"height":"0px"})
		setTimeout(recargar,0.00001)

		s(self.target).find(">button").bind("click",self.click)
		s(self.target).find(">.content").find(">button").bind("click",self.send)
		s(self.target).find(">.content").find(">button").bind("keyup",self.enter)
	
		
	