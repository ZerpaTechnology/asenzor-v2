__pragma__("alias","s","$")
from Widget import Widget
from Image import Image
import random
class Collage(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="<b class='titulo'></b><div class='content'></div>"
		self.target.html(self._html)
		
		self._hmtl=""
		self._imgs=[]
		self.imgsWidth=400
		self.width="100%"
		self.height="100vh"
		self.area=[1200,400]
		self.rotaciones=[30,12,-32,21,45,-20,15,-34,40,26,6,-22]
		self._hints=[]
		self.i=0
		self.activadores=[]

	def addImages(self,widget):
		
		if type(widget)==list:
			for k,elem in enumerate(widget):
				elem.rotation=self.rotaciones[k]
				elem.update()
				
				self.children.append(elem)
				self.target.find(">.content").append(elem.target)
		else:
			widget.rotation=self.rotaciones[self.i]
			self.i+=1
			widget.update()

			self.children.append(widget)
			self.target.find(">.content").append(widget.target)


	def titulo(self,titulo):
		self.target.find(">.titulo").text(titulo)
		self._titulo=titulo


	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.target.css({"width":self.width,"height":self.height})
		area=[]
		y=10
		por=25
		
			
				
		_k=0
		_pory=por
		_porx=5
		for k,elem in enumerate(self._imgs):
			img=Image()
			img._src=elem
			try:
				img._hint=self._hints[k]
			except:
				pass
			if _k<len(self.rotaciones):
				_k+=1
			else:
				_k=0
			img.rotation=self.rotaciones[_k]
			img.width=self.imgsWidth
			try:
				img.activador=self.activadores[k]
			except:
				pass
			img._hoverEffect="zoomOut"
			img._tooltip="top"
			img.target.find("img").css({"-webkit-box-shadow": "10px 10px 33px -2px rgba(0,0,0,0.75)",
				"-moz-box-shadow": "10px 10px 33px -2px rgba(0,0,0,0.75)",
				"box-shadow": "10px 10px 33px -2px rgba(0,0,0,0.75)"})
			if k==0:
				img._sources=True

			img.update()

			self.target.find(">.content").append(img.target)
			try:
				img.target.css({"position":"absolute","top":str(_pory)+"%","left":str(_porx)+"%"})
			except:
				pass
			if _porx<80:
				_porx+=20
			else:
				_porx=5
				_pory+=por
				

				
			
		

		self.titulo(self._titulo)
		self.__titulo=self.target.find(">.titulo")

	
	
		


		
