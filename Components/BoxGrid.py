__pragma__("alias","s","$")

from Widget import Widget
import random

class BoxGrid(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html=""
		
		self.container="container"
		
		
		self.colored=True
		self.paleta=["#1abc9c","#2ecc71","#3498db","#9b59b6","#34495e",
							  "#16a085","#27ae60","#2980b9","#8e44ad","#2c3e50",
							  "#f1c40f","#e67e22","#e74c3c","#ecf0f1","#95a5a6",
							  "#f39c12","#d35400","#c0392b","#bdc3c7","#7f8c8d"]

	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo
	def appendRow(self):
		html="<div class='row'></div>"
		self.target.append(html)

	def appendRows(self,n):
		html="<div class='row'></div>".repeat(n)
		self.target.html(html)

	def addCols(self,row,lista=["md-4","md-8"],padding=15):
		for elem in lista:
			if type(elem)!=str:
				clase=""
				for elem2 in elem:
					clase=clase+" col-"+elem2
				col=s("<div class='"+clase+"'></div>")
				s(self.target.find(">.row")[row]).append(col)
				if self.colored==True:
					col.css({"background-color":self.paleta[random.randint(0,20)],
						"min-height":"300px",
						"padding-left":padding,
						"padding-right":padding})

			else:
				col=s("<div class='col-"+elem+"'></div>")
				s(self.target.find(">.row")[row]).append(col)
				if self.colored==True:
					
					col.css({"background-color":self.paleta[random.randint(0,20)],
						"min-height":"300px",
						"padding-left":padding,
						"padding-right":padding})

	def addToCol(self,row,col,widget):
		widget.update()
		s(s(self.target.find(">.row")[row]).find(">div")[col]).html(widget.target)
		return s(s(self.target.find(">.row")[row]).find(">div")[col])





	



	def update(self):
		self.format=[self._titulo]
		self.__update__()
		

		self.__titulo=self.target.find(">.titulo")
		self.target.addClass(self.container)
	
	
		


		