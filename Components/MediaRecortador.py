__pragma__("alias","s","$")
__pragma__("xpath",["","../../../Components"])

from Widget import Widget
from BasicTabs import BasicTabs
from FileUpload import FileUpload
from Biblioteca import Biblioteca
config=Config.Config()
settings=nuclear.Settings()

class MediaRecortador(Widget):
	"""docstring for ClassName"""
	def __init__(self,titulo="Gestor de Archivos"):
		Widget.__init__(self,titulo)

		self._html="""
		<div><b class='titulo'>{}</b><span class='close'>x</span></div>
		<div class='botonera'>
		<span class='btn'>{}</span>
		<span class='btn'>{}</span>
		</div>
		<div class='content'>
		</div>
		<div>
		<button class='elegir'>{}</button>
		</div>
		"""
		self.tabsManger=BasicTabs()
		self.btn1="Subir archivos"
		self.btn2="Biblioteca Multimedia"
		self.btn3="Elegir"
		self.css_selected={"color":"gray",
			"border":"solid",
			"border-width":"1px",
			"border-radius":"12px 12px 0px 0px"}
		self.css_deselected={"color":"blue","border":"none"}
		self.url=config.base_url+settings.app+"/admin/Archivos/action=ver"
		self.archivos=[]
		self.biblioteca=Biblioteca()
		self.biblioteca.Media=self
		self.biblioteca.url=self.url
		self.activador=None
		self.value=[]

	def subir(self,evt):
		pass
	def open(self,activador):
		self.activador=activador
		s(self.target).removeClass("hidden")

	def close(self,evt=None):
		s(self.target).addClass("hidden")
	def updateTitulo(self,titulo):
		s(self.target).find(".titulo").text(titulo)

	def clickTab(self,evt):
		s(self.target).find(".botonera").find(".btn").css(self.css_deselected)
		s(evt.target).css(self.css_selected)
		indice=s(self.target).find(".botonera").find(".btn").index(evt.target)
		self.tabsManger.showTab(indice)


	def selectTab(self,tab):
		for elem in range(2):
			if elem==tab:
				s(s(self.target).find(".botonera").find(".btn")[tab]).css(self.css_selected)
			else:
				s(s(self.target).find(".botonera").find(".btn")[tab]).css(self.css_deselected)
	def noSeleccionados(self):
		
		self.biblioteca.currents=[]
		self.biblioteca.clearDetalles()
		s(self.target).find(".elegir").css({"color":"gray","background-color":"gray"})
	def seleccionados(self,seleccion):
		self.biblioteca.currents=seleccion
		self.currents=seleccion

		s(self.target).find(".elegir").css({"color":"white","background-color":"blue"})

	def elegir(self):
		self.value=[]
		if self.currents!=[]:
			for elem in self.currents:
				self.value.append(elem.indice)
			self.close()
			self.activador(self.currents)
			return self.currents
		


	def update(self):
		upload=FileUpload()
		upload.automatico=True
		upload.action=config.base_url+settings.app+"/admin/Archivo/None/action=save"
		upload.categorias=nuclear.VAR("categorias")
		upload.tipos=nuclear.VAR("tipos")

		upload.enlazar(self.biblioteca.nueva)
		
		


		self.tabsManger.appendToTab(0,upload)
		self.tabsManger.appendToTab(1,self.biblioteca)

		s(self.target).html(self._html.format(self.titulo,self.btn1,self.btn2,self.btn3))
		s(self.target).addClass("hidden")
		s(self.target).find(".close").bind("click",self.close)


		s(s(self.target).find(".botonera").find(".btn")[1]).css(self.css_selected)
		s(self.target).find(".botonera").find(".btn").bind("click",self.clickTab)

		

		if self.tabsManger!=None:
			self.tabsManger.bind("subir",self.subir)
			s(self.target).find(".content").html(self.tabsManger.target)
		s(self.target).find(".elegir").bind("click",self.elegir)
			


