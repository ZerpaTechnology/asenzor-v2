__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
from RadioButton import RadioButton
class RadioButtonList(Widget):
	"""docstring for RadioButtonList"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""
		<b>{}</b>
		<p>{}</p>
		<div class='content'>
		</div>
		"""
		self.descripcion=""

	def addOptions(self,lista,seleccionado=0):
		for k,elem in enumerate(lista):
			w=RadioButton(elem)

			if k==seleccionado:
				w.activar()
			self.children.append(w)
			self.add(w)

	def add(self,target):
		target.update()
		s(self.target).find(">.content").append(target.target)


	def update(self):
		s(self.target).html(self._html.format(self.titulo,self.descripcion))




