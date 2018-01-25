__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
class TabAcordion(Widget):
	"""docstring for Widget"""
	def __init__(self,titulo="tab",descripcion=""):
		Widget.__init__(self,titulo)
		self._html="""
		<span>
		<b class='titulo'>{}</b>
		<span>
		<span class='descripcion'>{}</span>
		<span class='switch'>
		</span>
		</span>
		
		</span>
		<div class='content'>
		</div>
		"""
		self.img=""
		self.descripcion=descripcion
		self.btn=config.base_url+"static/imgs/iconos/arrow-4.png"
		self._btn=config.base_url+"static/imgs/iconos/arrow-3.png"
		
		self.placeholder="No se ha elegido una imagen"
		self.value={}
		self.open=False
		self.height=0
		self.activador=None
		self.content=lambda self:self.target.find(">.content")

	def updateTitulo(self,titulo):
		self.target.find(">span").find(">.titulo").text(titulo)
		self.titulo=titulo

		

	def add(self,target):
		target.update()
		self.children.append(target)
		if self._update:

			s(self.target).find(">.content").append(target.target)
			def recargar():
				nonlocal self
				self.height=0
				for elem in s(self.target).find(">.content").children():
					
					self.height+=s(elem).outerHeight()
			setTimeout(recargar,0.000001)

		

	def addList(self,lista):

		for elem in lista:
			self.add(elem)
		
		
		
		
	def cerrar(self):
		s(self.target).find(">.content").animate({"height":"0px"},1000,lambda: s(self.target).find(">.content").css({"height":"0px","padding":"0px"}))
		s(self.target).find(".switch").css("background-image","url('"+self.btn+"')")
		self.open=False

	def abrir(self):
		def abrir():
			nonlocal self
			s(self.target).find(">.content").css({"height":"auto","padding":"5px"})
		s(self.target).find(">.content").animate({"height":str(self.height)+"px"},1000,abrir) 
		s(self.target).find(".switch").css("background-image","url('"+self._btn+"')")
		self.open=True
	
	def click(self):
		if self.open:
			self.cerrar()
		else:
			self.abrir()
		if self.activador!=None:
			self.activador(self)


		

		
	

	def update(self):
		self.format=[self.titulo,self.descripcion]
		self.__update__()
		
		if self.open:
			s(self.target).find(">.content").css("height","auto")
			s(self.target).find(".switch").css("background-image","url('"+self._btn+"')")
		else:
			s(self.target).find(">.content").css("height","0px")
			s(self.target).find(".switch").css("background-image","url('"+self.btn+"')")
		s(self.target).find(">span").bind("click",self.click)


		

	

	

