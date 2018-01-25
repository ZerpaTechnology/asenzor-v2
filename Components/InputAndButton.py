__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class InputAndButton(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		Widget.__init__(self,titulo)		
		self._html="""
		<input name='{}' placeholder='{}'>
		<button>{}</button>
		"""
		self.name=""
		self.placeholder="Nuevo nombre"
		
		self._atras=atras
		self.activador=None
		self.value=None
		self.placeholder=""
		self.open=False
		self.submit=None
		self.height=0

	def click(self):
		pass
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
		self.formato=[self.name,self.placeholder,self.titulo]
		self.__update__()		
		

	
		
	