__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget

class SubidoAnteriormente(Widget):
	"""docstring for Widget"""
	def __init__(self,titulo="Sugerido"):
		Widget.__init__(self,titulo)
		self._html="""
		<b class='titulo'>{}</b>
		<p>{}</p>
		<div class='visor'>
		</div>
		<div class='btns'>
		<button class='btn'><span></span>{}</button>
		</div>
		"""
		self.img=""
		self.descripcion=""
		self.btn="Imagen sugeriada al azar"
		self.btn2="Cambiar image"
		self.btn1="Eliminar imagen"
		self.placeholder="No se ha elegido una imagen"
		self.value=[]
		self.activador=None

	def subida(self,url):
		self.value.insert(0,url)
		target=s("<div><img src='{}'><span class='close'> x </span></div>".format(url))
		s(self.target).find(">.visor").prepend(target)
		s(target).find(".close").bind("click",self.close)


	def add(self,target):
		target.update()
		s(self.target).append(target.target)
		
	def close(self,evt):
		indice=self.value.index(__pragma__("js","{}","$(evt.target).prev()[0].src"))
		__pragma__("js","{}","self.value.splice(indice,1)")
		evt.target.parentNode.parentNode.removeChild(evt.target.parentNode)
		
		self.estaVacio()

	def estaVacio(self):

		if len(self.value)==0:
			self.activador()




		
	def updateValue(self,valor):
		self.value=valor

		if type(self.value)==list:
			self.value=self.value[0]
		s(self.target).find(">.visor").find("img").attr("src",self.value.url)
		if self.value!=None and len(s(self.target).find(".btns").find(".btn1"))==0:
			
			s(self.target).find(">.btns").find(".btn1").bind("click",self.delete)
			s(self.target).find(">.visor").find("img").removeClass("hidden")
			s(self.target).find(">.visor").find("p").addClass("hidden")

	

		
	def delete(self):
		self.value=None
		s(self.target).find(">.visor").find("p").removeClass("hidden")
		s(self.target).find(">.visor").find("img").attr("src","")
		s(self.target).find(">.visor").find("img").addClass("hidden")

		s(self.target).find(">.btns").find("button").remove(".btn1")

	def update(self):
		if self.value!=None:
			self.img=self.value

		s(self.target).html(self._html.format(self.titulo,self.descripcion,self.btn))
		s(self.target).find(".btns").find(".btn2").bind("click",self.change)
		if self.value!=None and len(s(self.target).find(">.btns").find(".btn1"))==0:
			s(self.target).find(">.btns").find(".btn2").before("<button class='btn1'>{}</button>".format(self.btn1))
			s(self.target).find(">.btns").find(".btn1").bind("click",self.delete)
			s(self.target).find(">.visor").find("img").removeClass("hidden")
			s(self.target).find(">.visor").find("p").addClass("hidden")

		

	

	

