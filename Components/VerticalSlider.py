__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class VerticalSlider(Widget):
	"""docstring for BasicSlider"""
	def __init__(self, titulo="",tabs=3):
		Widget.__init__(self,titulo)
		self._html="""
		  """.repeat(tabs)
		s(self.target).html(self._html)
		self.tabs=[s("<div class='tab'></div>") for i in range(tabs)]
		for elem in self.tabs:
			s(self.target).append(elem)
		self.tabWidth=300
		self.tabCurrent=0
		self.width=self.tabWidth*tabs
		
	def showTab(self,n):
		s(s(self.target).find(".tab")[0]).animate({"margin-top":-self.tabWidth*n})

	def addToTab(self,n,target):
		target.update()
		s(s(self.target).find(".tab")[n]).html(target.target)
	def getTab(self,n):
		return s(s(self.target).find(".tab")[n])

	def appendToTab(self,n,target):
		target.update()
		self.tabs[n].append(target.target)

	def update(self):
		
		s(self.target).find(".tab").css({"width":self.tabWidth})
		s(self.target).css({"width":self.width})
		self.__update__()
