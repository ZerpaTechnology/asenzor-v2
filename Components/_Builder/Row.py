__pragma__("alias","s","$")
__pragma__("xpath",["../"])
from Widget import Widget

class Row(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="""
		<sidebar class='controls'>
			<span class='menu'></span>
			<span class='duplicate'></span>
			<span class='quit'></span>
		</sidebar>
		<div class="content">
		<span class='add'> Añadir </span>
		</div>
		"""

		
		
		
		self.i=0
		self.window=None
	def add(self,widget):
		widget.update()
		self.children.append(widget)
		s.when(self.target.find(">.content").find(">.add").before(widget.target)).then(widget.done)

	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def addCols(self,evt):		
		
		self.window.InsertColumns.row=self.i
		self.window.update()
		self.window.open("InsertColumns")


	def done(self):

		self.__button=self.target.find(">button")
		#self.InsertarColumns.row=self

		self.__titulo=self.target.find(">.titulo")
		self.__add=self.target.find(">.content").find(".add")
		self.titulo(self._titulo)
		self.__add.bind("click",self.addCols)

	def update(self):

		

		self.format=[self._titulo]
		self.__update__()
		
		
	
	
		


		