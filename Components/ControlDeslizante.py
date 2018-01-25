
__pragma__("alias","s","$")
from Widget import Widget

class ControlDeslizante(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Barra deslizante"):
		Widget.__init__(self,titulo)
		self.orientacion="horizontal"
		self._html="<div><span class='titulo'>{}</span><div class='barra'><button class='guia'></button></div></div>"
		self.grosor=10
		self.range=[0,100]
		self.largo=300
		self.presionado=False
		self.value=0
		self.posInicial=0
		self.___barra=None
		self.___guia=None


	def arrastrar(self,evt):
		if self.presionado:
			
			posRelative=self.__guia.position()
			width=self.__guia.outerWidth()
			height=self.__guia.outerHeight()
			posAbsolute=self.__guia.offset()
			
			deltaleft=evt.clientX-posAbsolute.left
			deltatop=evt.clientY-posAbsolute.top
			
			

			if self.orientacion=="horizontal":
				self.value=(posRelative.left*100)/(self.largo-self.grosor-10)
				if deltaleft<0:
					if posRelative.left+deltaleft>=0:
						self.__guia.css({"left":str(posRelative.left+deltaleft)+"px"})
						
						


					else:
						self.__guia.css({"left":"0px"})
						
						

						

				else:
				
					if posRelative.left+deltaleft+width+2<self.largo:
						
						self.__guia.css({"left":str(posRelative.left+deltaleft)+"px"})
						

					else:
						self.__guia.css({"left":str(self.largo-width-2)+"px"})
						
						self.value=100



			elif self.orientacion=="vertical":
				self.value=(posRelative.top*100)/(self.largo-self.grosor-10)
				if deltatop<0:
					if posRelative.top+deltatop>=0:
						self.__guia.css({"top":str(posRelative.top+deltatop)+"px"})
						
					else:
						self.__guia.css({"top":"0px"})
						
						

				else:
				
					if posRelative.top+deltatop+height+2<self.largo:
						
						self.__guia.css({"top":str(posRelative.top+deltatop)+"px"})
						
					else:
						self.__guia.css({"top":str(self.largo-height-2)+"px"})
						
						self.value=100

			#print([evt.clientX,evt.clientY])

	def presionar(self,evt):
		self.presionado=True
		self.posInicial=[evt.clientX,evt.clientY]
	def soltar(self,evt):
		self.presionado=False
		

	def mover(self,valor):
		pass

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.__barra=self.target.find(">div").find(">.barra")
		self.__guia=self.__barra.find(">.guia")
		valor=((self.value*self.largo)/100)-(self.grosor/2)-5
		if self.orientacion=="horizontal":

			self.target.find(">div").css({"flex-direction":"column",
										  "display": "flex",
										  "justify-content":"space-between"})
			
			self.__barra.css({"width":str(self.largo)+"px",
											 "height":str(self.grosor)+"px"})
			self.__guia.css({"width":str(self.grosor+10)+"px",
															"top":"-5px",
															"left":str(valor)+"px",
															"height":str(self.grosor+10)+"px"})

		elif self.orientacion=="vertical":
			self.target.find(">div").find(">span").css({"display":"block"})				
			self.target.find(">div").css({"text-align":"center"})				

			self.__barra.css({"height":str(self.largo)+"px",
							"width":str(self.grosor)+"px",
							"display":"inline-block"})
			self.__guia.css({"height":str(self.grosor+10)+"px",
															"left":"-5px",
															"top":str(valor)+"px",
															"width":str(self.grosor+10)+"px"})
		
		s(document).on("mouseup",self.soltar)
		s(document).on("mousemove",self.arrastrar)
		self.__guia.on("mousedown",self.presionar)
		
		
	
		


		