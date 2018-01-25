__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class DinamicFigure(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="""
		<div class=" clearfix grid"> 
		<figure class="effect-oscar  wowload fadeIn animated" style="visibility: visible; animation-name: fadeIn;">
        	<img src="" alt="img01">
        	<figcaption>
            	<h2 class='titulo'></h2>
            	<span>
            	<p>Lily likes to play with crayons and pencils</p>
            	<br>
            	<a href="" title="1" data-gallery="">View more</a>
            	</span>            
        	</figcaption>
    	</figure>
    	</div>
		"""
		self._src=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self.target.html(self._html)
		self._html=""
		self.width=300
		self.height=300
		self._enlace=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self.activador=None

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
		self.target.css({"width":self.width,"height":self.height})
		self.__img.attr("src",self._src)
		self.__a.attr("href",self._enlace)
		if self.activador!=None:
			self.__a.bind("click",self.activador(self))

		
	
	
		


		