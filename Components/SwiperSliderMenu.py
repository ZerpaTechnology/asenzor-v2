__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class SwiperSliderMenu(Widget):
	"""docstring for Button"""
	def __init__(self, titulo=""):
		Widget.__init__(self,titulo)
		self._html="""
		div class="swiper-container">
		<div class="swiper-wrapper">
			<div class="swiper-slide menu">Menu slide</div>
			<div class="swiper-slide content">
				<div class="menu-button">
					<div class="bar"></div>
					<div class="bar"></div>
					<div class="bar"></div>
				</div>
				Content slide
			</div>
		</div>
	</div>
		"""
		self._img=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self.target.html(self._html)
		self._html=""
		self._enlace=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
	def pagination():
		html="""
		 <div class="swiper-pagination"></div>
	    <!-- Add Arrows -->
	    <div class="swiper-button-next"></div>
	    <div class="swiper-button-prev"></div>
		"""
		self.target.find(">.swiper-container").append(html)

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

		"""
		var menuButton = document.querySelector('.menu-button');
    var swiper = new Swiper('.swiper-container', {
      slidesPerView: 'auto',
      initialSlide: 1,
      resistanceRatio: 0,
      slideToClickedSlide: true,
      on: {
        init: function () {
          var slider = this;
          menuButton.addEventListener('click', function () {
            if (slider.activeIndex === 0) {
              slider.slideNext();
            } else {
              slider.slidePrev();
            }
          }, true);
        },
        slideChange: function () {
          var slider = this;
          if (slider.activeIndex === 0) {
            menuButton.classList.add('cross');
          } else {
            menuButton.classList.remove('cross');
          }
        },
      }
    });
		"""
	
	
		


		