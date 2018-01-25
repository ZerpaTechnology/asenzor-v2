
__pragma__("xpath",["","../"," ../../"])
__pragma__("alias","s","$")


from Widget import Widget

from BasicTabs import BasicTabs
from BuilderSettings import BuilderSettings

from BuilderModulo import BuilderModulo
from InsertColumns import InsertColumns
from InsertModulo import InsertModulo
from HorizontalScroll import HorizontalScroll

config=Config.Config()
class Window(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Ventana"):
		Widget.__init__(self,titulo)
		self._html="""
		<div class='header'>
			<div>
			<b class='titulo'></b>
			<div>
				<span class='close'>x</span>
			</div>

			</div>
			
			<div class='btns'>
				<div class='btns-left'>
					
					
				</div>
				
			</div>
		</div>
		<div class='content'>
		
		</div>		
		<div class="btnsFooter">

		</div>
		"""
		self.target.html(self._html)
	
		self.__button=self.target.find(">button")
		
		self._nav=[["Nuevo Modulo","save",lambda self2:lambda evt: None],
					["Cargar de la libreria","load",lambda self2:lambda evt: None],
					]
		self._footerNav=[
					]
		self.BasicTabs=BasicTabs()
		self.InsertColumns=InsertColumns()

		self.InsertModulo=InsertModulo()
		
	
		self.Modulo=None
		self.data={}
		self.actual="InsertColumns"
		self.HorizontalScroll=HorizontalScroll()
		
		
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def open(self,ventana="InsertColumns"):
		self.target.show()
		self.actual=ventana
		self.InsertColumns.Builder=self.Builder
		self.InsertModulo.Builder=self.Builder
		self.done()
		if ventana=="InsertColumns":
			self.InsertColumns.update()
			
			
			s.when(self.target.find(">.content").html(self.InsertColumns.target)).then(self.InsertColumns.done)
			

		elif ventana=="InsertModulo":
			self.InsertModulo.update()
		
			s.when(self.target.find(">.content").html(self.InsertModulo.target)).then(self.InsertModulo.done)
		
		elif ventana=="Modulo":
			self.Modulo.update()
			
			s.when(self.target.find(">.content").html(self.Modulo.target3)).then(self.Modulo.done)
			
		
		
		
	def close(self,evt):
		self.target.hide()

	def updateNav(self):
		self.HorizontalScroll.update()
		
		for elem in self._nav:
			span=s("<span>")
			self.HorizontalScroll.add(span)
			span.addClass(elem[1])
			span.text(elem[0])
			span.on("click",elem[2](self))
		


		

	def updateFooter(self):
		self.target.find(">.content").css({"height":"calc(100& - 200px)"})
		for elem in self._footerNav:
			span=s("<span>")
			span.addClass(elem[1])
			span.text(elem[0])
			self.__footerNav.append(span)
			span.on("click",elem[2](self))

	def done(self):
		self.__nav=self.target.find(">.header").find(">.btns").find(">.btns-left")
		self.__footerNav=self.target.find(">.btnsFooter")
		
		s.when(self.__nav.html(self.HorizontalScroll.target)).done(
			s.when(self.updateNav()).then(self.HorizontalScroll.done)
			)

		self.__titulo=self.target.find(">.titulo")
		self.__close=self.target.find(">.header").find(">div").find(">div").find(">.close")
		self.__close.on("click",self.close)

		
		self.updateFooter()
		self.titulo(self._titulo)
	

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		



		
		
	
	
		


		