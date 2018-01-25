__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class BlueimpGallery(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="""
		<div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls blueimp-gallery-display" style="display: block;">

    	<!-- The container for the modal slides -->

    	<div class="slides" style="width: 15912px;"><div class="slide" data-index="0" style="width: 1326px; left: 0px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div><div class="slide" data-index="1" style="width: 1326px; left: -1326px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div><div class="slide" data-index="2" style="width: 1326px; left: -2652px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div><div class="slide" data-index="3" style="width: 1326px; left: -3978px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div><div class="slide" data-index="4" style="width: 1326px; left: -5304px; transition-duration: 0ms; transform: translate(1326px, 0px) translateZ(0px);"><img draggable="false" title="1" src="http://localhost:8000/PTC/apps/occoa/user/static/images/portfolio/5.jpg" class="slide-content"></div><div class="slide" data-index="5" style="width: 1326px; left: -6630px; transition-duration: 0ms; transform: translate(-1326px, 0px) translateZ(0px);"><img draggable="false" title="1" src="http://localhost:8000/PTC/apps/occoa/user/static/images/portfolio/6.jpg" class="slide-content"></div><div class="slide" data-index="6" style="width: 1326px; left: -7956px; transition-duration: 400ms; transform: translate(0px, 0px) translateZ(0px);"><img draggable="false" title="1" src="http://localhost:8000/PTC/apps/occoa/user/static/images/portfolio/7.jpg" class="slide-content"></div><div class="slide" data-index="7" style="width: 1326px; left: -9282px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"><img draggable="false" title="1" src="http://localhost:8000/PTC/apps/occoa/user/static/images/portfolio/8.jpg" class="slide-content"></div><div class="slide" data-index="8" style="width: 1326px; left: -10608px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"><img draggable="false" title="1" src="http://localhost:8000/PTC/apps/occoa/user/static/images/portfolio/9.jpg" class="slide-content"></div><div class="slide" data-index="9" style="width: 1326px; left: -11934px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div><div class="slide" data-index="10" style="width: 1326px; left: -13260px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div><div class="slide" data-index="11" style="width: 1326px; left: -14586px; transition-duration: 400ms; transform: translate(1326px, 0px) translateZ(0px);"></div></div>

    	<!-- Controls for the borderless lightbox -->

    	<h3 class="title">1</h3>

    	<a class="prev">‹</a>

    	<a class="next">›</a>

    	<a class="close">×</a>

    	<!-- The modal dialog, which will be used to wrap the lightbox content -->    

		</div>
		"""
		self._img=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self.target.html(self._html)
		self._html=""
		self._enlace=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.__titulo=self.target.find(">div").find(">figure").find(">figcaption").find(">.titulo")
		self.__p=self.target.find(">div").find(">figure").find(">figcaption").find(">span").find(">p")
		self.__descripcion=self.__p
		self.__a=self.target.find(">div").find(">figure").find(">figcaption").find(">span").find(">a")
		self.__img=self.target.find(">div").find(">figure").find(">img")
		self.titulo(self._titulo)
		self.descripcion(self._descripcion)
		self.__img.attr("src",self._img)
		self.__a.attr("href",self._enlace)

		
	
	
		


		