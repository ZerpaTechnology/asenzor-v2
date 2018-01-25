__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
from ImagenRandom import ImagenRandom
from SubidoAnteriormente import SubidoAnteriormente
class Imagen_de_cabecera(Widget):
	"""
	Aunque puedes recortar las imágenes que
	te gustan después de hacer clic en Añadir 
	imagen, recomendamos que se ajuste al tamaño 
	de tu vídeo.
	"""
	def __init__(self,titulo="Imagen de cabecera"):
		Widget.__init__(self,titulo)
		self._html="""
		<b class='titulo'>{}</b>
		<p>{}</p>
		<b class='subtitulo'>{}</b>
		<div class='visor'>
		<p>{}</p>
		<img src='{}' class='hidden'>
		</div>
		<div class='btns'>
		<button class='btn2'>{}</button>
		
		</div>
		<div class='actual'>
		</div>
		<div class='sugerido'>
		</div>
		"""
		self.img=""
		self.descripcion=""
		self.subtitulo="Cabecera actual"
		self.btn="Añadir nueva imagen"
		self.btn2="Cambiar image"
		self.btn1="Eliminar imagen"
		self.placeholder="No se ha elegido una imagen"
		self.value=None
		self.Wanterior=SubidoAnteriormente("Subido anteriormente")
		self.Wsugerido=ImagenRandom("Sugerido")
		def quitar():
			nonlocal self
			s(self.target).find(">.btns").find(".btn1").remove()
			s(self.target).find(">.visor").find("img").addClass("hidden")
			s(self.target).find(">.visor").find("p").removeClass("hidden")
			s(self.target).find(">.visor").find("img").attr("src","")
			self.Wanterior.hidden()
		self.Wanterior.activador=quitar	

	

	def add(self,target):
		target.update()
		s(self.target).append(target.target)
		
	def updateValue(self,valor):
		self.value=valor
		
		
		if type(self.value)==list:
			self.value=self.value[0]
		s(self.target).find(">.visor").find("img").attr("src",self.value.url)
		self.Wanterior.show()
		self.Wanterior.subida(self.value.url)
		if self.value!=None and len(s(self.target).find(".btns").find(".btn1"))==0:
			s(self.target).find(">.btns").find(".btn2").before("<button class='btn1'>{}</button>".format(self.btn1))
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

		s(self.target).find(".btns").find("button").remove(".btn1")

	def update(self):
		s(self.target).html(self._html.format(self.titulo,self.descripcion,self.subtitulo,self.placeholder,self.img,self.btn))
		
		self.Wanterior.update()
		self.Wanterior.hidden()

		s(self.target).find(".actual").html(self.Wanterior.target)

		
		self.Wsugerido.value="http://localhost:8000/PTC/apps/woodridge/admin/static/archivos/Imagenes/Fondo Tampa otras opciones_540x540.png"

		self.Wsugerido.update()
		s(self.target).find(".sugerido").html(self.Wsugerido.target)
		s(self.target).find(".btns").find(".btn2").bind("click",self.change)

		if self.value!=None and len(s(self.target).find(".btns").find(".btn1"))==0:
			s(self.target).find(">.btns").find(">.btn2").before("<button class='btn1'>{}</button>".format(self.btn1))
			s(self.target).find(">.btns").find(">.btn1").bind("click",self.delete)
			s(self.target).find(">.visor").find(">img").removeClass("hidden")
			s(self.target).find(">.visor").find(">p").addClass("hidden")

		

	

	

