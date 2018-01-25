__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
config=Config.Config()
class BasicSlider(Widget):
	"""docstring for BasicSlider"""
	def __init__(self, titulo="",tabs=3):
		Widget.__init__(self,titulo)
		self._html=""
		self.target.html("<b class='titulo'></b><div></div>")
		self.ntabs=tabs
		self.tabs=[s("<div class='tab'></div>") for i in range(tabs)]
		self.onlyActiveVisible=True
		for k,elem in enumerate(self.tabs):
			s(self.target).find(">div").append(elem)


		self.tabWidth=300
		self.width=self.tabWidth*tabs
		self.tabCurrent=0
		self.__titulo=s(self.target).find(">.titulo")
		
		self.content=lambda self,k:self.tabs[k]
		self.__tabs=s(self.target).find(">div").find(">.tab")
		self.target.find(">.titulo")
		self.controles=False
		self.paginacion=False
		self.height=500
		self.movimiento=0
		self.btn_left=config.base_url+"static/imgs/iconos/arrow-2_blanco.png"
		self.btn_right=config.base_url+"static/imgs/iconos/arrow_blanco.png"
		self.clones=3
		self._loop=False

		
		
		self.i=0

		
	def showTab(self,n):
		self.i=n
		
		if self._loop==True:
			if self.i>0:
				if self.i>=self.ntabs:
					while self.i>=self.ntabs:
						self.i=self.i-self.ntabs
					if self.i<=0:
						
						s(self.__tabs[0]).css({"margin-left":(-self.tabWidth*(self.clones-1))+self.movimiento})
			if self.i<0:
					while self.i<0:
						self.i+=self.ntabs
					
					s(self.__tabs[0]).css({"margin-left":(-self.tabWidth*(self.i+self.clones+1))+self.movimiento})
				

			
		elif self._loop==False:
			if self.i>=self.ntabs:
				self.i=self.ntabs-1
			else:
				self.i=0

			


		
		if self.onlyActiveVisible:
			for k,elem in  enumerate(self.tabs):
			
				if k==n:
					self.tabs[k].css({"opacity":"1"})
				else:
					self.tabs[k].css({"opacity":"0"})
		s(self.__tabs[0]).animate({"margin-left":(-self.tabWidth*self.i)-(self.tabWidth*3 if self._loop==True else 0)})
		s(self.__tabs[0]).css({"margin-left":(-self.tabWidth*self.i)-(self.tabWidth*3 if self._loop==True else 0)})

	def addToTab(self,n,target):
		target.update()
		s(self.__tabs[n]).html(target.target)
	def getTab(self,n):
		return s(self.__tabs[n].children[0])

	def appendToSlide(self,n,target):
		target.update()
		self.tabs[n].append(target.target)
	def right(self,evt):
		if self.i<len(self.tabs):
			self.i+=1
			self.showTab(self.i)

	def left(self,evt):
		if self.i>0:
			self.i-=1
			self.showTab(self.i)

	def bgToSlide(self,n,src):
		self.tabs[n].css({"background-image":"url('{}')".format(src)})

	def loop(self,tiempo):
		self.i=0
		self._loop=True
		def play():
			
			nonlocal self
			

			if len(self.tabs)==self.i:
				self.i=0
			else:
				self.showTab(self.i)
				self.i+=1

		setInterval(play,tiempo)

	def update(self):

		self.width=self.tabWidth*len(self.tabs)
		self.__titulo.text(self._titulo)

		s(self.target).find(">div").css({"width":str(self.width)+"px"})
		self.__update__()
		if self.onlyActiveVisible:
			for k,elem in enumerate(self.tabs):
				if k!=0:
					elem.css({"opacity":"0"})
		self.__tabs.css({"width":str(self.tabWidth)+"px"})
		if self._loop:
			
			for i in  range(self.clones):
				s(self.target).find(">div").append(s(self.tabs[i]).clone())

			for i in  range(self.clones):
				s(self.target).find(">div").prepend(s(self.tabs[self.ntabs-i-1]).clone())

		
		self.__tabs=s(self.target).find(">div").find(">.tab")
		s(self.__tabs[0]).css({"margin-left":(-self.tabWidth*self.i)+(-self.tabWidth*3 if self._loop==True else 0)})
		self.target.find(">div").css({"height":str(self.height)+"px","width":str((self.ntabs+6)*self.tabWidth)+"px"})
		


		self.target.append("<div class='controles'> <span class='left'></span><span class='right'></span></div>")
		self.target.find(">.controles").find(">.left").css({"background-image":"url('{}')".format(self.btn_left),"background-size": "contain"})
		self.target.find(">.controles").find(">.right").css({"background-image":"url('{}')".format(self.btn_right),"background-size": "contain"})
		self.target.find(">.controles").find(">.left").bind("click",self.left)
		self.target.find(">.controles").find(">.right").bind("click",self.right)

		
