	__nest__ (
		__all__,
		'SwiperSlider', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SwiperSlider';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var SwiperSlider = __class__ ('SwiperSlider', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, slide) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							if (typeof slide == 'undefined' || (slide != null && slide .hasOwnProperty ("__kwargtrans__"))) {;
								var slide = 10;
							};
							Widget.__init__ (self, titulo);
							self._html = ('\n\t\t<div>\n\t\t<div class="swiper-container">\n\t\t\n\t    <div class="swiper-wrapper">\n\t    ' + ''.join (function () {
								var __accu0__ = [];
								for (var elem = 1; elem < slide + 1; elem++) {
									__accu0__.append (("<div class='swiper-slide'>Slide " + elem) + '</div>');
								}
								return __accu0__;
							} ())) + '\n\t    </div>\n\t    \n\t  </div>\n\t\t';
							self._img = ((config.base_url + 'apps/') + settings.app) + '/user/static/images/portfolio/1.jpg';
							self.target.html (self._html);
							self._html = '';
							self._enlace = ((config.base_url + 'apps/') + settings.app) + '/user/static/images/portfolio/1.jpg';
							self._load_css = list ([config.base_url + 'static/css/swiperslider/swiper.min.css']);
							self._load_js = list ([config.base_url + 'static/js/swiperslider/swiper.js']);
							self.height = 400;
							self._config = dict ({});
						});},
						get getSlide () {return __get__ (this, function (self, n) {
							return $ (self.target.find ('>div').find ('>.swiper-container').find ('>.swiper-wrapper').find ('>.swiper-slide') [n]);
						});},
						get appendToSlide () {return __get__ (this, function (self, n, widget) {
							widget.py_update ();
							self.getSlide (n).append (widget.target);
						});},
						get addToSlide () {return __get__ (this, function (self, n, widget) {
							widget.py_update ();
							self.getSlide (n).html (widget.target);
						});},
						get dinamicPagination () {return __get__ (this, function (self) {
							var html = '\n\t\t<div class="swiper-pagination"></div>\n\t\t';
							self.target.find ('>div').find ('>.swiper-container').append (html);
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'dynamicBullets': true});
						});},
						get pagination () {return __get__ (this, function (self) {
							var html = '\n\t\t<div class="swiper-pagination"></div>\n\t\t';
							self.target.find ('>div').find ('>.swiper-container').append (html);
							self._config ['pagination'] = dict ({'el': '.swiper-pagination'});
						});},
						get slideTo () {return __get__ (this, function (self, x, y) {
							self.slider.slideTo (x, y);
						});},
						get navigation () {return __get__ (this, function (self) {
							var html = '\n\t\t \n\t    <div class="swiper-button-next"></div>\n\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config ['navigation'] = dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'});
							self._config ['nextButton'] = '.swiper-button-next';
							self._config ['prevButton'] = '.swiper-button-prev';
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get paginationProgress () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t    <!-- Add Arrows -->\n\t    <div class="swiper-button-next"></div>\n\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'type': 'progressbar'});
							self._config ['navigation'] = dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'});
							self._config ['nextButton'] = '.swiper-button-next';
							self._config ['prevButton'] = '.swiper-button-prev';
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get paginationFraction () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t    <!-- Add Arrows -->\n\t    <div class="swiper-button-next"></div>\n\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'type': 'fraction'});
							self._config ['navigation'] = dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'});
							self._config ['nextButton'] = '.swiper-button-next';
							self._config ['prevButton'] = '.swiper-button-prev';
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get paginationCustom () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t    <!-- Add Arrows -->\n\t    <div class="swiper-button-next"></div>\n\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true, 'renderBullet': (function __lambda__ (index, className) {
								return ((('<span class="' + className) + '">') + (index + 1)) + '</span>';
							})});
							self._config ['navigation'] = dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'});
							self._config ['nextButton'] = '.swiper-button-next';
							self._config ['prevButton'] = '.swiper-button-prev';
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get scrollbar () {return __get__ (this, function (self) {
							self._config ['scrollbar'] = dict ({'el': '.swiper-scrollbar', 'hide': true});
						});},
						get verticalSlider () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get spaceBetween () {return __get__ (this, function (self, n) {
							if (typeof n == 'undefined' || (n != null && n .hasOwnProperty ("__kwargtrans__"))) {;
								var n = 30;
							};
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['spaceBetween'] = n;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get sliderPerView () {return __get__ (this, function (self, perview, space) {
							if (typeof perview == 'undefined' || (perview != null && perview .hasOwnProperty ("__kwargtrans__"))) {;
								var perview = 3;
							};
							if (typeof space == 'undefined' || (space != null && space .hasOwnProperty ("__kwargtrans__"))) {;
								var space = 30;
							};
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = perview;
							self._config ['spaceBetween'] = space;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get carousel () {return __get__ (this, function (self, space) {
							if (typeof space == 'undefined' || (space != null && space .hasOwnProperty ("__kwargtrans__"))) {;
								var space = 30;
							};
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = 'auto';
							self._config ['spaceBetween'] = space;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get centered () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = 4;
							self._config ['spaceBetween'] = 30;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get centeredAuto () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = 'auto';
							self._config ['centeredSlides'] = true;
							self._config ['spaceBetween'] = 30;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get freeMode () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = 3;
							self._config ['freeMode'] = true;
							self._config ['spaceBetween'] = 30;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get scrollContainer () {return __get__ (this, function (self) {
							var html = '\n\t\t  <div class="swiper-scrollbar"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['direction'] = 'vertical';
							self._config ['slidesPerView'] = 'auto';
							self._config ['freeMode'] = true;
							self._config ['scrollbar'] = dict ({'el': '.swiper-scrollbar'});
							self._config ['mousewheel'] = true;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get slidesPerColumn () {return __get__ (this, function (self, perview, percolumn, space) {
							if (typeof perview == 'undefined' || (perview != null && perview .hasOwnProperty ("__kwargtrans__"))) {;
								var perview = 3;
							};
							if (typeof percolumn == 'undefined' || (percolumn != null && percolumn .hasOwnProperty ("__kwargtrans__"))) {;
								var percolumn = 2;
							};
							if (typeof space == 'undefined' || (space != null && space .hasOwnProperty ("__kwargtrans__"))) {;
								var space = 30;
							};
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = perview;
							self._config ['slidesPerColumn'] = percolumn;
							self._config ['freeMode'] = true;
							self._config ['spaceBetween'] = space;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get grabCursor () {return __get__ (this, function (self, perview, space) {
							if (typeof perview == 'undefined' || (perview != null && perview .hasOwnProperty ("__kwargtrans__"))) {;
								var perview = 3;
							};
							if (typeof space == 'undefined' || (space != null && space .hasOwnProperty ("__kwargtrans__"))) {;
								var space = 30;
							};
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = perview;
							self._config ['centeredSlides'] = true;
							self._config ['spaceBetween'] = space;
							self._config ['grabCursor'] = true;
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get infiniteLoop () {return __get__ (this, function (self, perview, space) {
							if (typeof perview == 'undefined' || (perview != null && perview .hasOwnProperty ("__kwargtrans__"))) {;
								var perview = 1;
							};
							if (typeof space == 'undefined' || (space != null && space .hasOwnProperty ("__kwargtrans__"))) {;
								var space = 30;
							};
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config ['pagination'] = dict ({'el': '.swiper-pagination', 'clickable': true});
							self._config ['slidesPerView'] = perview;
							self._config ['spaceBetween'] = space;
							self._config ['loop'] = true;
							self._config ['navigation'] = dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get infiniteLoopWithSlidePerView () {return __get__ (this, function (self, perview, space) {
							if (typeof perview == 'undefined' || (perview != null && perview .hasOwnProperty ("__kwargtrans__"))) {;
								var perview = 1;
							};
							if (typeof space == 'undefined' || (space != null && space .hasOwnProperty ("__kwargtrans__"))) {;
								var space = 30;
							};
							var html = '\n\t\t   <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'slidesPerView': 3, 'spaceBetween': 30, 'slidesPerGroup': 3, 'loop': true, 'loopFillGroupWithBlank': true, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get effectFade () {return __get__ (this, function (self) {
							var html = '\t\t \n\t    <div class="swiper-pagination swiper-pagination-white"></div>\n\t    <!-- Add Arrows -->\n\t    <div class="swiper-button-next swiper-button-white"></div>\n\t    <div class="swiper-button-prev swiper-button-white"></div>\n\t\t';
							self._config = dict ({'spaceBetween': 30, 'effect': 'fade', 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get effectCube () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'effect': 'cube', 'grabCursor': true, 'cubeEffect': dict ({'shadow': true, 'slideShadows': true, 'shadowOffset': 20, 'shadowScale': 0.94}), 'pagination': dict ({'el': '.swiper-pagination'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get effectCoverFlow () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'effect': 'coverflow', 'grabCursor': true, 'centeredSlides': true, 'slidesPerView': 'auto', 'coverflowEffect': dict ({'rotate': 50, 'stretch': 0, 'depth': 100, 'modifier': 1, 'slideShadows': py_true}), 'pagination': dict ({'el': '.swiper-pagination'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get effectFlip () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'effect': 'flip', 'grabCursor': true, 'pagination': dict ({'el': '.swiper-pagination'}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get effectFlip () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'slidesPerView': 1, 'spaceBetween': 30, 'keyboard': dict ({'enabled': true}), 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get mousewheel_control () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'direction': 'vertical', 'slidesPerView': 1, 'spaceBetween': 30, 'mousewheel': true, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get autoplay () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'spaceBetween': 30, 'centeredSlides': true, 'autoplay': dict ({'delay': 2500, 'disableOnInteraction': false}), 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get dinamicSlides () {return __get__ (this, function (self) {
							var html = '\n\t\t <div class="swiper-pagination"></div>\n\t\t';
							self._config = dict ({'slidesPerView': 3, 'centeredSlides': true, 'spaceBetween': 30, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get thumsGallery () {return __get__ (this, function (self) {
						});},
						get hashNavigation () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'spaceBetween': 30, 'hashNavigation': dict ({'watchState': true}), 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get rtl () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get parallax () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'speed': 600, 'parallax': true, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get lazyLoadImages () {return __get__ (this, function (self) {
							var html = '\n\t\t     <!-- Add Pagination -->\n    <div class="swiper-pagination swiper-pagination-white"></div>\n    <!-- Navigation -->\n    <div class="swiper-button-next swiper-button-white"></div>\n    <div class="swiper-button-prev swiper-button-white"></div>\n\t\t';
							self._config = dict ({'lazy': true, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get responsiveBreakPoints () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'slidesPerView': 5, 'spaceBetween': 50, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': py_true}), 'breakpoints': dict ({1024: dict ({'slidesPerView': 4, 'spaceBetween': 40}), 768: dict ({'slidesPerView': 3, 'spaceBetween': 30}), 640: dict ({'slidesPerView': 2, 'spaceBetween': 20}), 320: dict ({'slidesPerView': 1, 'spaceBetween': 10})})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get autoHeight () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'autoHeight': true, 'spaceBetween': 20, 'pagination': dict ({'el': '.swiper-pagination', 'clickable': true}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get zoom () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							self._config = dict ({'zoom': true, 'pagination': dict ({'el': '.swiper-pagination'}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get virtualSlider () {return __get__ (this, function (self) {
							var html = '\n\t\t    <!-- Add Pagination -->\n\t\t    <div class="swiper-pagination"></div>\n\t\t    <!-- Add Arrows -->\n\t\t    <div class="swiper-button-next"></div>\n\t\t    <div class="swiper-button-prev"></div>\n\t\t';
							var funcion = function () {
								var slides = list ([]);
								for (var i = 0; i < 600; i++) {
									slides.append ('Slide ' + str (i));
								}
								return slides;
							};
							self._config = dict ({'slidesPerView': 3, 'centeredSlides': true, 'spaceBetween': 30, 'pagination': dict ({'el': '.swiper-pagination', 'type': 'fraction'}), 'navigation': dict ({'nextEl': '.swiper-button-next', 'prevEl': '.swiper-button-prev'}), 'virtual': dict ({'slides': funcion})});
							self.target.find ('>div').find ('>.swiper-container').append (html);
						});},
						get menu () {return __get__ (this, function (self) {
						});},
						get fullscreen () {return __get__ (this, function (self) {
							self.navigation ();
							self.target.css (dict ({'position': 'fixed', 'top': '0px', 'width': '100%', 'z-index': '2000'}));
							self.target.find ('>div').find ('>.swiper-container').find ('>.swiper-wrapper').find ('>.swiper-slide').css ('height', '100vh');
							var close = $ ("<span class='close'>x</span>");
							self.height = '100vh';
							self.target.append (close);
							self.target.hide ();
							close.bind ('click', (function __lambda__ (evt) {
								return self.target.hide ();
							}));
						});},
						get show () {return __get__ (this, function (self) {
							self.target.show ();
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.__titulo = self.target.find ('>div').find ('>figure').find ('>figcaption').find ('>.titulo');
							self.__p = self.target.find ('>div').find ('>figure').find ('>figcaption').find ('>span').find ('>p');
							self.__descripcion = self.__p;
							self.__a = self.target.find ('>div').find ('>figure').find ('>figcaption').find ('>span').find ('>a');
							self.__img = self.target.find ('>div').find ('>figure').find ('>img');
							var cargar = function () {
								print (self._config);
								self.slider = new Swiper ('.swiper-container', self._config);
								self.target.find ('.swiper-slide').css (dict ({'height': self.height}));
							};
							setTimeout (cargar, 2000);
							self.titulo (self._titulo);
							self.descripcion (self._descripcion);
							self.__img.attr ('src', self._img);
							self.__a.attr ('href', self._enlace);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.SwiperSlider = SwiperSlider;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
