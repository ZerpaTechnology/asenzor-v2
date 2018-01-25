__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from EnlaceButton import EnlaceButton
class EnlaceButtonInput(EnlaceButton):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		EnlaceButton.__init__(self,titulo)		
		self._html+="""
		<div class='content'>
		<input name='{}' placeholder='{}'><button>{}</button>
		</div>
		"""
		self.name=""
		self.placeholder="Nuevo nombre"
		self.btn="Añadir"
		self._atras=atras
		
		self.value=None
		self.open=False
		self.activador=None
		self.submit=None

	def click(self):
		if self.open:
			self.cerrar()
		else:
			self.abrir()
		if self.activador!=None:
			self.activador(self)

	def abrir(self):
		s(self.target).find(">button").css({"display":"none"})
		s(self.target).find(">.content").css({"display":"block"})
		self.open=True

	def cerrar(self):
		s(self.target).find(">button").css({"display":"block"})
		s(self.target).find(">.content").css({"display":"none"})
		self.open=False


	def send(self,evt=None):
		self.value=s(self.target).find(">.content").find(">input").val()
		if self.submit!=None:
			self.submit(self)
		self.cerrar()

	def enter(self,evt):
		if evt.keyEnter==True:
			if self.submit!=None:
				self.submit(self)
			self.cerrar()
	
	def update(self):
		
		s(self.target).html(self._html.format(self.titulo,self.name,self.placeholder,self.btn))
		s(self.target).find(">button").bind("click",self.click)
		if not self.open:
			s(self.target).find(">.content").css({"display":"none"})
		s(self.target).find(">.content").find(">button").bind("click",self.send)



		
		
	