__pragma__("alias","s","$")
from Widget import Widget
class Column(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="""
		<sidebar class='controls'>
			<b class='titulo'></b>
			<span class='menu'></span>
			<span class='duplicate'></span>
			<span class='quit'></span>
		</sidebar>
		<div class="content">
		<span class='add'> Añadir </span>
		</div>
		"""
		self.size=12
		self.row=0
		self.i=0
		self.dataChildren=[]
		
		
		
		self.content=lambda self: self.target.find(">.content").find(">.add")
	
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def add(self,widget,ntarget):
		if "py_update" in dir(widget):
			widget.update()
			self.children.append(widget)
			if ntarget==1:
				s(self.content(self)).before(widget.target)
			elif ntarget==2:
				s(self.content(self)).before(widget.target2)
			elif ntarget==3:
				s(self.content(self)).before(widget.target3)
			elif ntarget==4:
				s(self.content(self)).before(widget.target4)
			elif ntarget==5:
				s(self.content(self)).before(widget.target5)
			
		else:
			self.target.find(">.content").find(">.add").before(widget.clone())

	def addModulo(self,evt):
		
		self.window.InsertModulo.row=self.row
		self.window.InsertModulo.col=self.i
		self.window.InsertModulo.column=self
		self.window.open("InsertModulo")
	def done(self):
		self.__button=self.target.find(">button")
		self.target.css({"width":"calc("+str(200*self.size/12)+"% - 20px)"})
		self.__titulo=self.target.find(">.controls").find(">.titulo")
		
		self.__add=self.target.find(">.content").find(">.add")
		self.__add.bind("click",self.addModulo)

		self.__titulo.text(self._titulo)

	def update(self):
		self.format=[self._titulo]

		self.__update__()

		
		
		


		
		
		
	
	
		


		