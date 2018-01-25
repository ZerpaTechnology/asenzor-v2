__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
from CheckBox import CheckBox
class CheckBoxList(Widget):
	"""docstring for RadioButtonList"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""
		<h5>{}</h5>
		<div class='list'></div>
		"""
		self.value=[]
		self.content=lambda self:self.target.find(">.list")
		
	def add(self,target):
		if self._update:
			target.update()
			self.content(self).append(target.target)
		else:
			self.children.append(target)

		



	def update(self):
		

		self.format=[self.titulo]
		self.__update__()

		if len(self.value)!=0 and len(self.children)==0:
			if type(self.value)==list:
				for elem in self.value:
					opcion=elem[0]+("<span>"+elem[2]+"</span>" if len(elem)==3 else "")

					w=CheckBox(opcion)
					w.value=elem[1]
					w.update()
					self.content(self).append(w.target)
			elif type(self.value)==dict:
				for elem in self.value:
					w=CheckBox(elem)
					w.value=self.value[elem]
					w.update()
					self.content(self).append(w.target)



			





