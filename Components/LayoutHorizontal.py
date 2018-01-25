__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from HeaderCustomizeMain import HeaderCustomizeMain

settings=nuclear.Settings()
config=Config.Config()
class LayoutHorizontal(Widget):
	"""docstring for SidebarCustomize"""
	def __init__(self,*widgets):
		Widget.__init__(self,"")
		self._html="<div></div>"
		for elem in widgets:
			self.add(elem)
		
		self.icon=config.base_url+"static/imgs/iconos/document-2.png"
		self.content=lambda self,k:self.target.find(">div").find(">div")[k]

	def add(self,widget):
		self.format=[self.titulo]
		w=s("<div>")
		widget.update()
		
		self.children.append(widget)
		self.target.find(">div").append(w)
		w.html(widget.target)
		widget._update=True
		
		
			

	def hiddenTab(self,n):
		s(self.target.find(">div").find(">div")[n]).hide()
	def showTab(self,n):
		s(self.target.find(">div").find(">div")[n]).show()
	def sliderTab(self,n):
		width=s(self.find(">div").target.find(">div")[n]).outerWidth()
		s(self.target.find(">div").find(">div")[n]).css({"width":"0px"})
		self.hiddenTab(n)
		s(self.target.find(">div").find(">div")[n]).animate({"width":str(width)+"px"},1000)
		s(self.target.find(">div").find(">div")[n]).css({"width":str(width)+"px"})

	def reloadSizes(self):
		width=0
		
		for k,elem in enumerate(self.children):
			
			

			if k+1==len(self.children):
				
				s(self.target.find(">div").find(">div")[k]).css("width","calc( 100% - "+str(width)+"px)")
			width+=elem.target.outerWidth()
			

				
					





	def update(self):
		self.format=[]
		self.__update__()
		

		
		

		


		

		


		
		



		