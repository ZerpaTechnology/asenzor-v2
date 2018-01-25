__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class Select(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo,atras):
		Widget.__init__(self,titulo)		
		self._html="""
		<b>{}</b>
		<select></select>
		"""
		self.name=""
		self.placeholder="Nuevo nombre"
		self.btn="Añadir"
		self._atras=atras
		self.activador=None
		self.value=None
		self.open=False
	def click(self):
		if self.open:
			s(self.target).find(">.content").animate({"height":"0px"},1000)
			self.open=False
		else:
			s(self.target).find(">.content").animate({"height":"auto"},1000)
			self.open=True


	def submit(self,evt=None):
		self.value=s(self.target).find(">.content").find(">input").val()
		self.activador()
	def enter(self,evt):
		if evt.keyEnter==True:
			self.submit()
	
	def update(self):

		s(self.target).html(self._html.format(self.titulo))
		for elem in self.opciones:
			s(self.target).find(">select").append("<option>"+elem+"</option>")
		
		
	