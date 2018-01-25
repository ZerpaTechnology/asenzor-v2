__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget

class HeaderCustomizeMain(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)		
		self._html="""
		<div>
		<div class='text'>
		<span class='help'>?</span>

		<p>Estas personalizando</p>
		<h3>{}</h3>
		<div class='pro'>
		</div>
		</div>
		<div class='info' >
		<p>{}</p>
		</div>
		</div>
		"""
		self._help="""
		El personalizador te permite tener una 
		vista previa de los cambios de tu sitio 
		antes de publicarlos. Puedes navegar a 
		traves de las distintas páginas de tu 
		sitio sin salir de la vista previa. Se 
		muestran enlaces de editar a algunos 
		elementos que lo apliquen."""
		self.proButton=None

	def update(self):
		s(self.target).html(self._html.format(self.titulo,self._help))
		s(self.target).find(".info").addClass("hidden")

		s(self.target).find(".help").bind("click",lambda evt:__pragma__("js","{}","$(evt.target.parentNode).next().removeClass('hidden')") if __pragma__("js","{}","$(evt.target.parentNode).next().hasClass('hidden')") else __pragma__("js","{}","$(evt.target.parentNode).next().addClass('hidden')"))

		if self.proButton!=None:
			s(self.target).find(".pro").html(self.proButton)



	
		
	