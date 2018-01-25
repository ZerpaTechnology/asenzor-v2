__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
class RadioButton(Widget):
	"""docstring for RadioButtonList"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""<input type='radio'><span>{}</span>"""
		self.hermanos=[]

	def activar(self):
		s(self.target).find(">input").prop("checked",True)
		for elem in enumerate(self.hermanos):
			elem.desactivar()

	def desactivar(self):
		s(self.target).find(">input").prop("checked",False)

	def update(self):
		s(self.target).html(self._html.format(self.titulo))
