__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
settings=nuclear.Settings()
class SwiperSlider(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="",slide=10):
		Widget.__init__(self,titulo)
		self._html="""
		<div>
		<div class="swiper-container">
		
	    <div class="swiper-wrapper">
	    """+"".join(["<div class='swiper-slide'>Slide "+elem+"</div>" for elem in range(1,slide+1)])+"""
	    </div>
	    
	  </div>
		"""

		self._img=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		self.target.html(self._html)

		self._html=""
		self._enlace=config.base_url+"apps/"+settings.app+"/user/static/images/portfolio/1.jpg"
		
		self._load_css=[config.base_url+"static/css/swiperslider/swiper.min.css"]
		self._load_js=[config.base_url+"static/js/swiperslider/swiper.js"]
		self.height=400
		self._config={}

	def getSlide(self,n):
		return s(self.target.find(">div").find(">.swiper-container").find(">.swiper-wrapper").find(">.swiper-slide")[n])

	def appendToSlide(self,n,widget):
		widget.update()
		self.getSlide(n).append(widget.target)
	def addToSlide(self,n,widget):
		widget.update()
		self.getSlide(n).html(widget.target)


	def dinamicPagination(self):
		html="""
		<div class="swiper-pagination"></div>
		"""
		self.target.find(">div").find(">.swiper-container").append(html)
		
		self._config["pagination"]={"el": '.swiper-pagination',"dynamicBullets": True}
		
	def pagination(self):
		html="""
		<div class="swiper-pagination"></div>
		"""
		self.target.find(">div").find(">.swiper-container").append(html)
		self._config["pagination"]= {"el": '.swiper-pagination'}
	
	def slideTo(self,x,y):
		self.slider.slideTo(x, y)

    
	def navigation(self):
		html="""
		 
	    <div class="swiper-button-next"></div>
	    <div class="swiper-button-prev"></div>
		"""
		self._config["navigation"]= {
        "nextEl": '.swiper-button-next',
        "prevEl": '.swiper-button-prev',}
		self._config["nextButton"]='.swiper-button-next'
		self._config["prevButton"]='.swiper-button-prev'
		self.target.find(">div").find(">.swiper-container").append(html)

	def paginationProgress(self):
		html="""
		 <div class="swiper-pagination"></div>
	    <!-- Add Arrows -->
	    <div class="swiper-button-next"></div>
	    <div class="swiper-button-prev"></div>
		"""
		self._config["pagination"]={"el": ".swiper-pagination",
								  "type": "progressbar"}
		self._config["navigation"]={"nextEl": ".swiper-button-next",
      							   "prevEl": ".swiper-button-prev"}
		self._config["nextButton"]=".swiper-button-next"
		self._config["prevButton"]=".swiper-button-prev"
		self.target.find(">div").find(">.swiper-container").append(html)
	def paginationFraction(self):
		html="""
		 <div class="swiper-pagination"></div>
	    <!-- Add Arrows -->
	    <div class="swiper-button-next"></div>
	    <div class="swiper-button-prev"></div>
		"""
		self._config["pagination"]={"el": ".swiper-pagination",
								  "type": "fraction"}
		self._config["navigation"]={"nextEl": ".swiper-button-next",
      							   "prevEl": ".swiper-button-prev"}
		self._config["nextButton"]=".swiper-button-next"
		self._config["prevButton"]=".swiper-button-prev"
		self.target.find(">div").find(">.swiper-container").append(html)

	def paginationCustom(self):
		html="""
		 <div class="swiper-pagination"></div>
	    <!-- Add Arrows -->
	    <div class="swiper-button-next"></div>
	    <div class="swiper-button-prev"></div>
		"""
		self._config["pagination"]={"el": ".swiper-pagination",
								  "clickable":True,
								  "renderBullet":lambda index,className: '<span class="' + className + '">' + (index + 1) + '</span>'}
		self._config["navigation"]={"nextEl": ".swiper-button-next",
      							   "prevEl": ".swiper-button-prev"}
		self._config["nextButton"]=".swiper-button-next"
		self._config["prevButton"]=".swiper-button-prev"

		self.target.find(">div").find(">.swiper-container").append(html)


	def scrollbar(self):
		
		self._config["scrollbar"]={
        "el": '.swiper-scrollbar',
        "hide": True
        }

	def verticalSlider(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
        "el": '.swiper-pagination',
        "clickable": True}
	
		self.target.find(">div").find(">.swiper-container").append(html)
	def spaceBetween(self,n=30):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
        "el": '.swiper-pagination',
        "clickable": True}
		self._config["spaceBetween"]=n
	
		self.target.find(">div").find(">.swiper-container").append(html)

	def sliderPerView(self,perview=3,space=30):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]=perview
		self._config["spaceBetween"]=space
		self.target.find(">div").find(">.swiper-container").append(html)

	def carousel(self,space=30):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]="auto"
		self._config["spaceBetween"]=space
		self.target.find(">div").find(">.swiper-container").append(html)
	
	def centered(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]=4
		self._config["spaceBetween"]=30
		self.target.find(">div").find(">.swiper-container").append(html)

	def centeredAuto(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]="auto"
		self._config["centeredSlides"]=True
		self._config["spaceBetween"]=30
		self.target.find(">div").find(">.swiper-container").append(html)

	def freeMode(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]=3
		self._config["freeMode"]=True
		self._config["spaceBetween"]=30
		self.target.find(">div").find(">.swiper-container").append(html)
	def scrollContainer(self):
		html="""
		  <div class="swiper-scrollbar"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["direction"]="vertical"
		self._config["slidesPerView"]="auto"
		self._config["freeMode"]=True
		self._config["scrollbar"]={
		"el": '.swiper-scrollbar',
		}
		self._config["mousewheel"]=True
		self.target.find(">div").find(">.swiper-container").append(html)
	def slidesPerColumn(self,perview=3,percolumn=2,space=30):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]=perview
		self._config["slidesPerColumn"]=percolumn
		self._config["freeMode"]=True
		self._config["spaceBetween"]=space
		self.target.find(">div").find(">.swiper-container").append(html)

	def grabCursor(self,perview=3,space=30):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]=perview
		self._config["centeredSlides"]=True
		self._config["spaceBetween"]=space
		self._config["grabCursor"]=True
		self.target.find(">div").find(">.swiper-container").append(html)

	def infiniteLoop(self,perview=1,space=30):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config["pagination"]={
		"el": '.swiper-pagination',
		"clickable": True}
		self._config["slidesPerView"]=perview
		self._config["spaceBetween"]=space
		self._config["loop"]=True
		self._config["navigation"]={"nextEl": ".swiper-button-next",
      							   "prevEl": ".swiper-button-prev"}
		self.target.find(">div").find(">.swiper-container").append(html)

	def infiniteLoopWithSlidePerView(self,perview=1,space=30):
		html="""
		   <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config={
		      "slidesPerView": 3,
		      "spaceBetween": 30,
		      "slidesPerGroup": 3,
		      "loop": True,
		      "loopFillGroupWithBlank": True,
		      "pagination": {
		        "el": '.swiper-pagination',
		        "clickable": True,
		      },
		      "navigation": {
		        "nextEl": '.swiper-button-next',
		        "prevEl": '.swiper-button-prev',
		      },
		    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def effectFade(self):
		html="""		 
	    <div class="swiper-pagination swiper-pagination-white"></div>
	    <!-- Add Arrows -->
	    <div class="swiper-button-next swiper-button-white"></div>
	    <div class="swiper-button-prev swiper-button-white"></div>
		"""
		self._config={
	      "spaceBetween": 30,
	      "effect": 'fade',
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def effectCube(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	      "effect": 'cube',
	      "grabCursor": True,
	      "cubeEffect": {
	        "shadow": True,
	        "slideShadows": True,
	        "shadowOffset": 20,
	        "shadowScale": 0.94,
	      },
	      "pagination": {
	        "el": '.swiper-pagination',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def effectCoverFlow(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	      "effect": 'coverflow',
	      "grabCursor": True,
	      "centeredSlides": True,
	      "slidesPerView": 'auto',
	      "coverflowEffect": {
	        "rotate": 50,
	        "stretch": 0,
	        "depth": 100,
	        "modifier": 1,
	        "slideShadows" : true,
	      },
	      "pagination": {
	        "el": '.swiper-pagination',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def effectFlip(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	      "effect": 'flip',
	      "grabCursor": True,
	      "pagination": {
	        "el": '.swiper-pagination',
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def effectFlip(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	      "slidesPerView": 1,
	      "spaceBetween": 30,
	      "keyboard": {
	        "enabled": True,
	      },
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def mousewheel_control(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	        "direction": 'vertical',
	        "slidesPerView": 1,
	        "spaceBetween": 30,
	        "mousewheel": True  ,
	        "pagination": {
	          "el": '.swiper-pagination',
	          "clickable": True,
	        },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def autoplay(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	      "spaceBetween": 30,
	      "centeredSlides": True,
	      "autoplay": {
	        "delay": 2500,
	        "disableOnInteraction": False,
	      },
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def dinamicSlides(self):
		html="""
		 <div class="swiper-pagination"></div>
		"""
		self._config={
	      "slidesPerView": 3,
	      "centeredSlides": True,
	      "spaceBetween": 30,
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		"""
		    document.querySelector('.prepend-2-slides').addEventListener('click', function (e) {
		      e.preventDefault();
		      swiper.prependSlide([
		        '<div class="swiper-slide">Slide ' + (--prependNumber) + '</div>',
		        '<div class="swiper-slide">Slide ' + (--prependNumber) + '</div>'
		        ]);
		    });

		    document.querySelector('.prepend-slide').addEventListener('click', function (e) {
		      e.preventDefault();
		      swiper.prependSlide('<div class="swiper-slide">Slide ' + (--prependNumber) + '</div>');
		    });
		    document.querySelector('.append-slide').addEventListener('click', function (e) {
		      e.preventDefault();
		      swiper.appendSlide('<div class="swiper-slide">Slide ' + (++appendNumber) + '</div>');
		    });
		    document.querySelector('.append-2-slides').addEventListener('click', function (e) {
		      e.preventDefault();
		      swiper.appendSlide([
		        '<div class="swiper-slide">Slide ' + (++appendNumber) + '</div>',
		        '<div class="swiper-slide">Slide ' + (++appendNumber) + '</div>'
		        ]);
		    }
		    """
		self.target.find(">div").find(">.swiper-container").append(html)

	def thumsGallery(self):
		"""
		<!-- Swiper -->
  <div class="swiper-container gallery-top">
    <div class="swiper-wrapper">
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/1)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/2)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/3)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/4)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/5)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/6)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/7)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/8)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/9)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/10)"></div>
    </div>
    <!-- Add Arrows -->
    <div class="swiper-button-next swiper-button-white"></div>
    <div class="swiper-button-prev swiper-button-white"></div>
  </div>
  <div class="swiper-container gallery-thumbs">
    <div class="swiper-wrapper">
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/1)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/2)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/3)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/4)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/5)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/6)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/7)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/8)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/9)"></div>
      <div class="swiper-slide" style="background-image:url(http://lorempixel.com/1200/1200/nature/10)"></div>
    </div>
  </div>
		"""
		"""
		var galleryTop = new Swiper('.gallery-top', {
		  spaceBetween: 10,
		  navigation: {
		    nextEl: '.swiper-button-next',
		    prevEl: '.swiper-button-prev',
		  },
	    });
	    var galleryThumbs = new Swiper('.gallery-thumbs', {
	      spaceBetween: 10,
	      centeredSlides: true,
	      slidesPerView: 'auto',
	      touchRatio: 0.2,
	      slideToClickedSlide: true,
	    });
	    galleryTop.controller.control = galleryThumbs;
	    galleryThumbs.controller.control = galleryTop;
		"""
	def hashNavigation(self):
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config={
	      "spaceBetween": 30,
	      "hashNavigation": {
	        "watchState": True,
	      },
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def rtl(self):
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config={
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def parallax(self):
		"""
		 <!-- Swiper -->
  <div class="swiper-container">
    <div class="parallax-bg" style="background-image:url(http://lorempixel.com/900/600/nightlife/2/)" data-swiper-parallax="-23%"></div>
    <div class="swiper-wrapper">
      <div class="swiper-slide">
        <div class="title" data-swiper-parallax="-300">Slide 1</div>
        <div class="subtitle" data-swiper-parallax="-200">Subtitle</div>
        <div class="text" data-swiper-parallax="-100">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam dictum mattis velit, sit amet faucibus felis iaculis nec. Nulla laoreet justo vitae porttitor porttitor. Suspendisse in sem justo. Integer laoreet magna nec elit suscipit, ac laoreet nibh euismod. Aliquam hendrerit lorem at elit facilisis rutrum. Ut at ullamcorper velit. Nulla ligula nisi, imperdiet ut lacinia nec, tincidunt ut libero. Aenean feugiat non eros quis feugiat.</p>
        </div>
      </div>
      <div class="swiper-slide">
        <div class="title" data-swiper-parallax="-300" data-swiper-parallax-opacity="0">Slide 2</div>
        <div class="subtitle" data-swiper-parallax="-200">Subtitle</div>
        <div class="text" data-swiper-parallax="-100">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam dictum mattis velit, sit amet faucibus felis iaculis nec. Nulla laoreet justo vitae porttitor porttitor. Suspendisse in sem justo. Integer laoreet magna nec elit suscipit, ac laoreet nibh euismod. Aliquam hendrerit lorem at elit facilisis rutrum. Ut at ullamcorper velit. Nulla ligula nisi, imperdiet ut lacinia nec, tincidunt ut libero. Aenean feugiat non eros quis feugiat.</p>
        </div>
      </div>
      <div class="swiper-slide">
        <div class="title" data-swiper-parallax="-300">Slide 3</div>
        <div class="subtitle" data-swiper-parallax="-200">Subtitle</div>
        <div class="text" data-swiper-parallax="-100">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam dictum mattis velit, sit amet faucibus felis iaculis nec. Nulla laoreet justo vitae porttitor porttitor. Suspendisse in sem justo. Integer laoreet magna nec elit suscipit, ac laoreet nibh euismod. Aliquam hendrerit lorem at elit facilisis rutrum. Ut at ullamcorper velit. Nulla ligula nisi, imperdiet ut lacinia nec, tincidunt ut libero. Aenean feugiat non eros quis feugiat.</p>
        </div>
      </div>
		"""
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config= {
	      "speed": 600,
	      "parallax": True,
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def lazyLoadImages(self):
		"""
		      <div class="swiper-slide">
        <!-- Required swiper-lazy class and image source specified in data-src attribute -->
        <img data-src="http://lorempixel.com/1600/1200/nature/1/" class="swiper-lazy">
        <!-- Preloader image -->
        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
      </div>
      <div class="swiper-slide">
        <img data-src="http://lorempixel.com/1600/1200/nature/2/" class="swiper-lazy">
        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
      </div>
      <div class="swiper-slide">
        <img data-src="http://lorempixel.com/1600/1200/nature/3/" class="swiper-lazy">
        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
      </div>
      <div class="swiper-slide">
        <img data-src="http://lorempixel.com/1600/1200/nature/4/" class="swiper-lazy">
        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
      </div>
      <div class="swiper-slide">
        <img data-src="http://lorempixel.com/1600/1200/nature/5/" class="swiper-lazy">
        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
      </div>
      <div class="swiper-slide">
        <img data-src="http://lorempixel.com/1600/1200/nature/6/" class="swiper-lazy">
        <div class="swiper-lazy-preloader swiper-lazy-preloader-white"></div>
      </div>

		"""
		html="""
		     <!-- Add Pagination -->
    <div class="swiper-pagination swiper-pagination-white"></div>
    <!-- Navigation -->
    <div class="swiper-button-next swiper-button-white"></div>
    <div class="swiper-button-prev swiper-button-white"></div>
		"""
		self._config= {
	     
	      "lazy": True,
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def responsiveBreakPoints(self):
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config= {
	      "slidesPerView": 5,
	      "spaceBetween": 50,
	      # init: false,
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": true,
	      },
	      "breakpoints": {
	        1024: {
	          "slidesPerView": 4,
	          "spaceBetween": 40,
	        },
	        768: {
	          "slidesPerView": 3,
	          "spaceBetween": 30,
	        },
	        640: {
	          "slidesPerView": 2,
	          "spaceBetween": 20,
	        },
	        320: {
	          "slidesPerView": 1,
	          "spaceBetween": 10,
	        }
	      }
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def autoHeight(self):
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config={
	      "autoHeight": True, #enable auto height
	      "spaceBetween": 20,
	      "pagination": {
	        "el": '.swiper-pagination',
	        "clickable": True,
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
	def zoom(self):
		"""
		  <div class="swiper-container">
    <div class="swiper-wrapper">
      <div class="swiper-slide">
        <div class="swiper-zoom-container">
          <img src="http://lorempixel.com/800/800/sports/1/">
        </div>
      </div>
      <div class="swiper-slide">
        <div class="swiper-zoom-container">
          <img src="http://lorempixel.com/800/400/sports/2/">
        </div>
      </div>
      <div class="swiper-slide">
        <div class="swiper-zoom-container">
          <img src="http://lorempixel.com/400/800/sports/3/">
        </div>
      </div>
    </div>
    <!-- Add Pagination -->
    <div class="swiper-pagination swiper-pagination-white"></div>
    <!-- Add Navigation -->
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>
		"""
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		self._config={
	      "zoom": True,
	      "pagination": {
	        "el": '.swiper-pagination',
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)

	def virtualSlider(self):
		"""
		  <div class="swiper-container">
    <div class="swiper-wrapper"></div>
    <!-- Add Pagination -->
    <div class="swiper-pagination"></div>
    <!-- Add Arrows -->
    <div class="swiper-button-next"></div>
    <div class="swiper-button-prev"></div>
  </div>
  <p class="append-buttons">
    <a href="#" class="slide-1">Slide 1</a>
    <a href="#" class="slide-250">Slide 250</a>
    <a href="#" class="slide-500">Slide 500</a>
  </p>
		"""
		html="""
		    <!-- Add Pagination -->
		    <div class="swiper-pagination"></div>
		    <!-- Add Arrows -->
		    <div class="swiper-button-next"></div>
		    <div class="swiper-button-prev"></div>
		"""
		def funcion():
			slides=[]
			for i in range(600):
				slides.append("Slide "+str(i))
			return slides

		self._config={
	      "slidesPerView": 3,
	      "centeredSlides": True,
	      "spaceBetween": 30,
	      "pagination": {
	        "el": '.swiper-pagination',
	        "type": 'fraction',
	      },
	      "navigation": {
	        "nextEl": '.swiper-button-next',
	        "prevEl": '.swiper-button-prev',
	      },
	      "virtual": {
	        "slides": funcion,
	      },
	    }
		self.target.find(">div").find(">.swiper-container").append(html)
		"""
		document.querySelector('.slide-1').addEventListener('click', function (e) {
	      e.preventDefault();
	      swiper.slideTo(0, 0);
	    });
	    document.querySelector('.slide-250').addEventListener('click', function (e) {
	      e.preventDefault();
	      swiper.slideTo(249, 0);
	    });
	    document.querySelector('.slide-500').addEventListener('click', function (e) {
	      e.preventDefault();
	      swiper.slideTo(499, 0);
	    });
		"""
	def menu(self):
		"""
				.swiper-container {
			width: 100%;
			height: 100%;
		}
		.swiper-slide {
			text-align: center;
			font-size: 18px;
			background: #fff;
			/* Center slide text vertically */
			display: -webkit-box;
			display: -ms-flexbox;
			display: -webkit-flex;
			display: flex;
			-webkit-box-pack: center;
			-ms-flex-pack: center;
			-webkit-justify-content: center;
			justify-content: center;
			-webkit-box-align: center;
			-ms-flex-align: center;
			-webkit-align-items: center;
			align-items: center;
		}
		.menu {
			min-width: 100px;
			width: 70%;
			max-width: 320px;
			background-color: #2C8DFB;
			color: #fff;
		}
		.content {
			width: 100%;
		}
		.menu-button {
			position: absolute;
			top: 0px; left: 0px;
			padding: 15px;
			cursor: pointer;
			-webkit-transition: .3s;
			transition: .3s;
			background-color: #2C8DFB;
			/*margin: 14px;
			border-radius: 5px;*/
		}
		.menu-button .bar:nth-of-type(1) {
			margin-top: 0px;
		}
		.menu-button .bar:nth-of-type(3) {
			margin-bottom: 0px;
		}
		.bar {
			position: relative;
			display: block;
			width: 50px;
			height: 5px;
			margin: 10px auto;
			background-color: #fff;
			border-radius: 10px;
			-webkit-transition: .3s;
			transition: .3s;
		}
		.menu-button:hover .bar:nth-of-type(1) {
			-webkit-transform: translateY(1.5px) rotate(-4.5deg);
			-ms-transform: translateY(1.5px) rotate(-4.5deg);
			transform: translateY(1.5px) rotate(-4.5deg);
		}
		.menu-button:hover .bar:nth-of-type(2) {
			opacity: .9;
		}
		.menu-button:hover .bar:nth-of-type(3) {
			-webkit-transform: translateY(-1.5px) rotate(4.5deg);
			-ms-transform: translateY(-1.5px) rotate(4.5deg);
			transform: translateY(-1.5px) rotate(4.5deg);
		}
		.cross .bar:nth-of-type(1) {
			-webkit-transform: translateY(15px) rotate(-45deg);
			-ms-transform: translateY(15px) rotate(-45deg);
			transform: translateY(15px) rotate(-45deg);
		}
		.cross .bar:nth-of-type(2) {
			opacity: 0;
		}
		.cross .bar:nth-of-type(3) {
			-webkit-transform: translateY(-15px) rotate(45deg);
			-ms-transform: translateY(-15px) rotate(45deg);
			transform: translateY(-15px) rotate(45deg);
		}
		.cross:hover .bar:nth-of-type(1) {
			-webkit-transform: translateY(13.5px) rotate(-40.5deg);
			-ms-transform: translateY(13.5px) rotate(-40.5deg);
			transform: translateY(13.5px) rotate(-40.5deg);
		}
		.cross:hover .bar:nth-of-type(2) {
			opacity: .1;
		}
		.cross:hover .bar:nth-of-type(3) {
			-webkit-transform: translateY(-13.5px) rotate(40.5deg);
			-ms-transform: translateY(-13.5px) rotate(40.5deg);
			transform: translateY(-13.5px) rotate(40.5deg);
		}
	</style>
</head>
<body>
	<!-- Swiper -->
	<div class="swiper-container">
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

	<!-- Swiper JS -->
	<script src="../dist/js/swiper.min.js"></script>

	<!-- Initialize Swiper -->
	<script>
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
	</script>

		"""
	def fullscreen(self):
		self.navigation()
		self.target.css({"position":"fixed","top":"0px","width":"100%","z-index":"2000"})
		self.target.find(">div").find(">.swiper-container").find(">.swiper-wrapper").find(">.swiper-slide").css("height","100vh")
		close=s("<span class='close'>x</span>")
		self.height="100vh"
		self.target.append(close)
		self.target.hide()
		close.bind("click",lambda evt:self.target.hide())

	def show(self):
		self.target.show()


	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.__titulo=self.target.find(">div").find(">figure").find(">figcaption").find(">.titulo")
		self.__p=self.target.find(">div").find(">figure").find(">figcaption").find(">span").find(">p")
		self.__descripcion=self.__p
		self.__a=self.target.find(">div").find(">figure").find(">figcaption").find(">span").find(">a")
		self.__img=self.target.find(">div").find(">figure").find(">img")
		def cargar():
			nonlocal self
			print(self._config)
			self.slider = __new__(Swiper)(".swiper-container",self._config)
			self.target.find(".swiper-slide").css({"height":self.height})

		setTimeout(cargar,2000)
		

		self.titulo(self._titulo)
		self.descripcion(self._descripcion)
		self.__img.attr("src",self._img)
		self.__a.attr("href",self._enlace)
		
				




		
	
	
		


		