__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class CyrusNavbar(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="""
		<div class="navbar-wrapper">

	      <div class="container">



	        <div class="navbar navbar-default navbar-fixed-top" role="navigation" id="top-nav">

	          <div class="container">

	            <div class="navbar-header">

	              <!-- Logo Starts -->

	              <a class="navbar-brand" href="#home"><img src="" alt="logo" class='logo'></a>

	              <!-- #Logo Ends -->





	              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">

	                <span class="sr-only">Toggle navigation</span>

	                <span class="icon-bar"></span>

	                <span class="icon-bar"></span>

	                <span class="icon-bar"></span>

	              </button>



	            </div>





	            <!-- Nav Starts -->

	            <div class="navbar-collapse in right-nav" style="height: auto;" >

	              

	            </div>

	            <!-- #Nav Ends -->



	          </div>

	        </div>



	      </div>

	    </div>
		"""
		
		self.target.html(self._html)
		self._html=""
		self._enlace=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self._img=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self._load_css=[config.base_url+"static/css/bootstrap.css"]
		self._load_js=[config.base_url+"static/js/bootstrap.js"]
		self._logo=config.base_url+"apps/occoa/user/static/images/logo.png"
		self._menu=[["Home","#home",[]],
				   ["About","#about",[]],
				   ["Partners","#partners",[]],
				   ["Contact","#contact",[]],


		]# ["etiqueta","url",[]]
	def construir(self,menu):
		wrapper='<ul class="nav navbar-nav navbar-right scroll">'
		for elem in menu:
	                 wrapper+='<li class="'+(elem[3] if len(elem)==4 else '')+'"><a href="'+elem[1]+'">'+elem[0]+'</a>'+self.construir(elem[3])+'</li>'
		wrapper+="</ul>"
		return wrapper

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.target.find(".logo").attr("src",self._logo)
		self.target.find(".right-nav").html(self.construir(self._menu))
		

		
	
	
		


		