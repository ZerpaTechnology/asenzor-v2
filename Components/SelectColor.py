
__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class SelectColor(Widget):
	"""docstring for BandaTema"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)

		self._html="""
		<label>{}</label>
		<input type='color' name='{}'>
		"""
		self.name=""
		self.value=None
		
		
	def change(self):
		self.value=s(self.target).find("input[type='color']").val()

	def update(self):
		s(self.target).html(self._html.format(self.titulo,self.name))
		s(self.target).find("input[type='color']").bind("change",self.change)


		
		

		

