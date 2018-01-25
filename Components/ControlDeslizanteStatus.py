
__pragma__("alias","s","$")
from Widget import Widget

class ControlDeslizanteStatus(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Barra deslizante"):
		Widget.__init__(self,titulo)
		self.orientacion="horizontal"
		self.target.html("""
			<span class='titulo'></span>
			<div>
			<div class='frames'>
			</div>
		<div>
			<div class='barra'>
			<button class='guia'>
			</button>
		</div>
		</div>
		</div>""")

		self.grosor=10
		self.range=[0,100]
		self.frames=10
		self.largo=300
		self.presionado=False
		self.value=0
		self.posInicial=0
		self.__barra=None
		self.__guia=None
		self.grosorFrames=30
		self.largo_guia=20
		self.colores=[(43,118,255),(0,255,30),(255,0,0)]
	def getValueForRange(self):
		delta=self.range[1]-self.range[0]
		return (self.value*delta)/100

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
						
						#self.value=(posRelative.left*100)/self.largo
						
						


					else:
						self.__guia.css({"left":"0px"})
						#self.value=(0*100)/self.largo
						
						

						

				else:
				
					if posRelative.left+deltaleft+width+2<self.largo:
						
						self.__guia.css({"left":str(posRelative.left+deltaleft)+"px"})
						
						#self.value=(posRelative.left*100)/(self.largo-self.grosor-8)
						

					else:
						self.__guia.css({"left":str(self.largo-width-2)+"px"})
						self.value=100
						



			elif self.orientacion=="vertical":
				self.value=(posRelative.top*100)/(self.largo-self.grosor-10)
				if deltatop<0:
					if posRelative.top+deltatop>=0:
						self.__guia.css({"top":str(posRelative.top+deltatop)+"px"})
						delta=self.range[1]-self.range[0]
						self.value=(posRelative.top*100)/(self.largo-self.grosor)
						
					else:
						self.__guia.css({"top":"0px"})
						self.value=(0*100)/(self.largo-self.grosor)
						
						

				else:
				
					if posRelative.top+deltatop+height+2<self.largo:
						
						self.__guia.css({"top":str(posRelative.top+deltatop)+"px"})
						
						self.value=(posRelative.top*100)/(self.largo-self.grosor)
						
					else:
						self.__guia.css({"top":str(self.largo-height-2)+"px"})
						self.value=((self.largo-self.grosor)*100)/(self.largo-self.grosor)
						

			

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
		self.__barra=self.target.find(">div").find(">div").find(">.barra")
		self.__guia=self.__barra.find(">.guia")
		self._frames=self.target.find(">div").find(">.frames")
		self.largo_guia=-self.largo_guia

		i_limite=self.frames/len(self.colores)
		deltaX=int(self.frames/len(self.colores))
		color_current=0
		c=1
		
		for x,elem in enumerate(range(self.frames)):
			i=s("<span></span>")
			
			#cuantos frames hay entre un color y otro
			if x>=i_limite:
				i_limite+=deltaX
				color_current+=1
				dr=self.colores[color_current][0]
				dg=self.colores[color_current][1]
				db=self.colores[color_current][2]
				c=0
				
			else:
				if color_current<len(self.colores)-1:
					dr=self.colores[color_current+1][0]-self.colores[color_current][0]
					dg=self.colores[color_current+1][1]-self.colores[color_current][1]
					db=self.colores[color_current+1][2]-self.colores[color_current][2]
					_dr=dr/deltaX
					_dg=dg/deltaX
					_db=db/deltaX
					
					dr=int(abs(self.colores[color_current][0]+(c*_dr)))
					dg=int(abs(self.colores[color_current][1]+(c*_dg)))
					db=int(abs(self.colores[color_current][2]+(c*_db)))
					
				else:
					dr=self.colores[len(self.colores)-1][0]
					dg=self.colores[len(self.colores)-1][1]	
					db=self.colores[len(self.colores)-1][2]	
					
			c+=1
			
			

			color="rgb"+str((dr,dg,db))
			self._frames.append(i)
			i.css({"background-color":color})
		valor=((self.value*self.largo)/100)-(self.grosor/2)-5
		if self.orientacion=="horizontal":
			self.target.find(">div").css({"flex-direction":"column",
										  })
			self.target.find(">div").find(">div").css({"flex-direction":"row",
										  "display": "flex"})

			self._frames.css({"display":"flex","flex-direction":"row",
							  "width":str(abs(self.largo)),
							  "height":str(self.grosorFrames)})

			self.__barra.css({"width":str(self.largo)+"px",
											 "height":str(self.grosor)+"px"})
			self.__guia.css({"width":str(self.grosor+10)+"px",
															"top": str(self.largo_guia)+"px",
															"left":str(valor)+"px",
															"height":str(self.grosor+abs(self.largo_guia)+10)+"px"})

		elif self.orientacion=="vertical":
			
			self.target.find(">div").find(">span").css({"display":"block"})		

			self.target.find(">div").css({"text-align":"center",
										  "display":"flex",
										  "justify-content": "flex-start"})				

			self._frames.css({"display":"flex","flex-direction":"column",
							  "height":str(abs(self.largo)),
							  "width":str(self.grosorFrames)})

			self.__barra.css({"height":str(self.largo)+"px",
							"width":str(self.grosor)+"px",
							"display":"inline-block"})

			self.__guia.css({"height":str(self.grosor+10)+"px",
							"left":str(self.largo_guia)+"px",
							"top":str(valor)+"px",
							"width":str(self.grosor+abs(self.largo_guia)+10)+"px"})
		
		s(document).on("mouseup",self.soltar)
		s(document).on("mousemove",self.arrastrar)
		self.__guia.on("mousedown",self.presionar)
		self.titulo(self._titulo)
		
		
		
	
		


		