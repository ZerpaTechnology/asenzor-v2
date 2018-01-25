__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget

class ImagenRandom(Widget):
	"""docstring for Widget"""
	def __init__(self,titulo="Sugerido"):
		Widget.__init__(self,titulo)
		self._html="""
		<b class='titulo'>{}</b>
		<p>{}</p>
		<div class='visor'>
		<p>{}</p>
		<img src='{}' class='hidden'>
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
		self.value=None

	def add(self,target):
		target.update()
		s(self.target).append(target.target)
		
	def updateValue(self,valor):
		self.value=valor

		if type(self.value)==list:
			self.value=self.value[0]
		s(self.target).find(">.visor").find("img").attr("src",self.value.url)
		if self.value!=None and len(s(self.target).find(".btns").find(".btn1"))==0:
			
			s(self.target).find(">.btns").find(".btn1").bind("click",self.delete)
			s(self.target).find(">.visor").find("img").removeClass("hidden")
			s(self.target).find(">.visor").find("p").addClass("hidden")

	def change(self):
		self.Media.open(self.updateValue)

		
	def delete(self):
		self.value=None
		s(self.target).find(">.visor").find("p").removeClass("hidden")
		s(self.target).find(">.visor").find("img").attr("src","")
		s(self.target).find(">.visor").find("img").addClass("hidden")

		s(self.target).find(">.btns").find("button").remove(".btn1")

	def update(self):
		if self.value!=None:
			self.img=self.value

		s(self.target).html(self._html.format(self.titulo,self.descripcion,self.placeholder,self.img,self.btn))
		s(self.target).find(".btns").find(".btn2").bind("click",self.change)
		if self.value!=None and len(s(self.target).find(">.btns").find(".btn1"))==0:
			s(self.target).find(">.btns").find(".btn2").before("<button class='btn1'>{}</button>".format(self.btn1))
			s(self.target).find(">.btns").find(".btn1").bind("click",self.delete)
			s(self.target).find(">.visor").find("img").removeClass("hidden")
			s(self.target).find(">.visor").find("p").addClass("hidden")

		

	

	

