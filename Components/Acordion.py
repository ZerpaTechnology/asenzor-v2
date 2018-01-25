__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
from TabAcordion import TabAcordion
class Acordion(Widget):
	"""docstring for Widget"""
	def __init__(self,titulo="Logo"):
		Widget.__init__(self,titulo)
		self._html="""
		<b class='titulo'>{}</b>
		<div class='content'>
		</div>
		<div  class='btns'>
		<span class='reordenar'>{}</span>
		<button class='add'>{}</button>
		</div>
		<span class='borrar'>{}</span>
		"""
		self.img=""
		self.descripcion=""
		
		self.placeholder="No se ha elegido una imagen"
		self.value={}
		self.open=False
		self.height=0
		self.children=[]
		self.backgroundContents="#999"
		self.content=lambda self: self.target.find(">.content")
		self.span="Reordenar"
		self.btn="Añadir items"
		self.borrar="Borrar"

		

	def add(self,titulo,content,descripcion=""):
		w=TabAcordion(titulo,descripcion)
		w.hermanos=self.children
		w.activador=self.cerrarHermanos
		w.update()
		self.children.append(w)
		s(self.target).find(">.content").append(w.target)
		w.target.find(">.content").css({"background-color":self.backgroundContents})
		for elem in content:
			w.add(elem)
		

	def addTab(self,tab):
		tab.update()
		
		self.children.append(tab)

		if self._update:
			s(self.content(self)).append(tab.target)
		


		
	def cerrarHermanos(self,target):
		for elem in target.hermanos:
			if elem!=target:
				elem.cerrar()
	
	def appendToTab(self,tab,target):
		target.update()
		self.children[tab].add(target)



	def update(self):
		self.format=[self.titulo,self.span,self.btn,self.borrar]
		self.__update__()
		
		

		

	

	

