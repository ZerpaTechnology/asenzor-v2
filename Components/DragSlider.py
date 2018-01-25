__pragma__("alias","s","$")
from BasicSlider import BasicSlider
class DragSlider(BasicSlider):
	"""docstring for Button"""
	def __init__(self, titulo="",tabs=3):
		#BasicSlider.__init__(self,titulo,tabs)
		BasicSlider.__init__(self,titulo,tabs)
		self.presionado=False
		self.i=0
		self._left=0
		self.tempWrappers=None
		self.posInicial=[0,0]
		self.onlyActiveVisible=False
		self._loop=True
		self.movimiento=0


	def presionar(self,evt):
		self.presionado=True
		div=s("<div>")
		
		self.tempWrappers=div
		self.posInicial=[evt.clientX,evt.clientY]
		s("iframe").parent().append(div)
		div.css({"position":"absolute",
							   "top":"0px",
							   "left":"0px",
							   "width":"100%",
							   "height":"100%",
							   "-webkit-user-select": "none",
							"-moz-user-select": "none",
    						"-ms-user-select": "none",
    						"user-select":"none"})
		



	def soltar(self,evt):
		if self.presionado==True:
			self.tempWrappers.remove()
			self.presionado=False
			
			
			
			self.i=-int((self._left+(self.tabWidth*3 if self.loop==True else 0))/self.tabWidth)

			self.showTab(self.i)
			self.__tabs.css({"-webkit-user-select": "inherit",
								"-moz-user-select": "inherit",
	    						"-ms-user-select":"inherit",
	    						"user-select":"inherit"})
		s(document).css({"cursor":"inherit"})
		self.movimiento=0

	def arrastrar(self,evt):
		if self.presionado==True:
			

			self.movimiento=(evt.clientX-self.posInicial[0])*1.4
			
			self._left=self.movimiento-(self.tabWidth*self.i)-(self.tabWidth*3 if self.loop==True else 0)
			
			s(self.__tabs[0]).css({"margin-left":str(self._left)+"px"})
			self.__tabs.css({"-webkit-user-select": "none",
							"-moz-user-select": "none",
    						"-ms-user-select": "none",
    						"user-select":"none"})
			s(document).css({"cursor":"move"})
			
	def update(self):
		self.format=[self._titulo]
		BasicSlider.update(self)
		for elem in self.tabs:
			elem.on("mousedown",self.presionar)
		s(document).on("mousemove",self.arrastrar)
		s(document).on("mouseup",self.soltar)
		s(document).on("mouseout",self.salio)

	
	
		


		