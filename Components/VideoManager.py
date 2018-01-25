__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget

class VideoManager(Widget):
	"""
	Sube tu vídeo en formato .mp4 y minimiza 
	su tamaño de archivo para obtener mejores 
	resultados. Tu tema recomienda unas 
	dimensiones de 2000 × 1200 pixeles.
	"""
	def __init__(self,titulo="Video"):
		Widget.__init__(self,titulo)
		self._html="""
		<b class='titulo'>{}</b>
		<p>{}</p>
		<div class='visor'>
		<p>{}</p>
		<img src='{}' class='hidden'>
		</div>
		<div class='btns'>
		<button class='btn2'>{}</button>
		</div>
		"""
		self.img=""
		self.descripcion="""
		Sube tu vídeo en formato .mp4 y minimiza 
		su tamaño de archivo para obtener mejores 
		resultados. Tu tema recomienda unas 
		dimensiones de 2000 × 1200 pixeles.
		"""
		self.btn="Seleccione vídeo"
		self.btn2="Cambiar vídeo"
		self.btn1="Eliminar vídeo"
		self.placeholder="No has seleccionado ningún vídeo"
		self.value=None

	def add(self,target):
		target.update()
		s(self.target).append(target.target)
		
	def updateValue(self,valor):
		self.value=valor

		if type(self.value)==list:
			self.value=self.value[0]
		s(self.target).find(".visor").find("img").attr("src",self.value.url)
		if self.value!=None and len(s(self.target).find(".btns").find(".btn1"))==0:
			s(self.target).find(".btns").find(".btn2").before("<button class='btn1'>{}</button>".format(self.btn1))
			s(self.target).find(".btns").find(".btn1").bind("click",self.delete)
			s(self.target).find(".visor").find("img").removeClass("hidden")
			s(self.target).find(".visor").find("p").addClass("hidden")

	def change(self):
		self.Media.open(self.updateValue)

		
	def delete(self):
		self.value=None
		s(self.target).find(".visor").find("p").removeClass("hidden")
		s(self.target).find(".visor").find("img").attr("src","")
		s(self.target).find(".visor").find("img").addClass("hidden")

		s(self.target).find(".btns").find("button").remove(".btn1")

	def update(self):
		s(self.target).html(self._html.format(self.titulo,self.descripcion,self.placeholder,self.img,self.btn))
		s(self.target).find(".btns").find(".btn2").bind("click",self.change)
		if self.value!=None and len(s(self.target).find(".btns").find(".btn1"))==0:
			s(self.target).find(".btns").find(".btn2").before("<button class='btn1'>{}</button>".format(self.btn1))
			s(self.target).find(".btns").find(".btn1").bind("click",self.delete)
			s(self.target).find(".visor").find("img").removeClass("hidden")
			s(self.target).find(".visor").find("p").addClass("hidden")

		

	

	

