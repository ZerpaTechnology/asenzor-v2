__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class BasicTabs(Widget):
	"""docstring for BasicSlider"""
	def __init__(self, titulo="",tabs=3,tabdefault=0):
		Widget.__init__(self,titulo)
		self._html="<div></div>"
		self.children=[[] for elem in range(tabs)]
		self.ntabs=tabs
		self.tabWidth=300
		self.tabCurrent=0
		self.tabdefault=tabdefault
		self.width=self.tabWidth*tabs
		self.content=lambda self,k:self.tabs[k]
		
	def showTab(self,n):
		s(self.target).find(">div").find(">.tab").addClass("hidden")
		s(s(self.target).find(">div").find(">.tab")[n]).removeClass("hidden")

	def addToTab(self,n,target):
		if "update" in dir(target):
			target.update()
			self.children[n].append(target)
			s(s(self.target).find(">div").find(">.tab")[n]).html(target.target)
		else:
			s(s(self.target).find(">div").find(">.tab")[n]).html(target)
	def getTab(self,n):
		return s(s(self.target).find(">div").find(">.tab")[n])

	def appendToTab(self,n,target,ntarget=1):
		
		
		if "py_update" in dir(target):
			target.update()


			self.children[n].append(target)
			self.dataChildren.append({})
			if ntarget==1:
				s.when(self.tabs[n].append(target.target)).then(target.done)
				target.parent=self
				
			elif ntarget==2:
				s.when(self.tabs[n].append(target.target2)).then(target.done)
				target.parent2=self
				
			elif ntarget==3:
				s.when(self.tabs[n].append(target.target3)).then(target.done)
				target.parent3=self
				
			elif ntarget==4:
				s.when(self.tabs[n].append(target.target4)).then(target.done)
				target.parent4=self
				
			elif ntarget==5:
				s.when(self.tabs[n].append(target.target5)).then(target.done)
				target.parent5=self
				
			
		else:
			self.tabs[n].append(target)
		
		

	def update(self):
		
		


		self.__update__()
		self.tabs=[s("<div class='tab'></div>") if k==self.tabdefault else s("<div class='tab hidden'></div>")   for k,i in enumerate(range(self.ntabs))]
		

		for elem in self.tabs:
			s(self.target).find(">div").append(elem)

		s(self.target).find(">div").find(">.tab").css({"width":self.tabWidth})
		s(self.target).find(">div").css({"width":self.width})
