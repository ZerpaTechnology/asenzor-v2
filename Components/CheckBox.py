__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
class CheckBox(Widget):
	"""docstring for RadioButtonList"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="<input type='checkbox' name='{}'><span>{}</span>"
		self.name=""
		self.hermanos=[]
		self.activador=None
		self.desactivador=None
		self.value=False
	def desactivarHermanos(self):
		for elem in self.hermanos:
			if elem!=self:
				elem.desactivar()

	def click(self):
		if s(self.target).find("input[type='checkbox']").prop("checked"):
			self.activar()
		else:
			self.desactivar()
			


	def desactivar(self,desactivador=None):
		s(self.target).find("input[type='checkbox']").prop("checked",False)
		if desactivador!=None:
			self.desactivador=desactivador
			desactivador()
		elif self.desactivador!=None:
			self.desactivador()


	def activar(self,activador=None):
		s(self.target).find("input[type='checkbox']").prop("checked",True)
		if activador!=None:
			self.activador=activador
			activador()
		elif self.activador!=None:
			self.activador()


	def update(self):
		self.format=[self.name,self.titulo]
		self.__update__()
		s(self.target).find("input[type='checkbox']").prop("checked",self.value)
		s(self.target).find("input[type='checkbox']").bind("click",self.click)



