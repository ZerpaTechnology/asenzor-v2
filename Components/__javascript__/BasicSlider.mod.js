	__nest__ (
		__all__,
		'BasicSlider', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BasicSlider';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var BasicSlider = __class__ ('BasicSlider', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, tabs) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							if (typeof tabs == 'undefined' || (tabs != null && tabs .hasOwnProperty ("__kwargtrans__"))) {;
								var tabs = 3;
							};
							Widget.__init__ (self, titulo);
							self._html = '';
							self.target.html ("<b class='titulo'></b><div></div>");
							self.ntabs = tabs;
							self.tabs = function () {
								var __accu0__ = [];
								for (var i = 0; i < tabs; i++) {
									__accu0__.append ($ ("<div class='tab'></div>"));
								}
								return __accu0__;
							} ();
							self.onlyActiveVisible = true;
							var __iterable0__ = enumerate (self.tabs);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								$ (self.target).find ('>div').append (elem);
							}
							self.tabWidth = 300;
							self.width = self.tabWidth * tabs;
							self.tabCurrent = 0;
							self.__titulo = $ (self.target).find ('>.titulo');
							self.content = (function __lambda__ (self, k) {
								return self.tabs [k];
							});
							self.__tabs = $ (self.target).find ('>div').find ('>.tab');
							self.target.find ('>.titulo');
							self.controles = false;
							self.paginacion = false;
							self.height = 500;
							self.movimiento = 0;
							self.btn_left = config.base_url + 'static/imgs/iconos/arrow-2_blanco.png';
							self.btn_right = config.base_url + 'static/imgs/iconos/arrow_blanco.png';
							self.clones = 3;
							self._loop = false;
							self.i = 0;
						});},
						get showTab () {return __get__ (this, function (self, n) {
							self.i = n;
							if (self._loop == true) {
								if (self.i > 0) {
									if (self.i >= self.ntabs) {
										while (self.i >= self.ntabs) {
											self.i = self.i - self.ntabs;
										}
										if (self.i <= 0) {
											$ (self.__tabs [0]).css (dict ({'margin-left': -(self.tabWidth) * (self.clones - 1) + self.movimiento}));
										}
									}
								}
								if (self.i < 0) {
									while (self.i < 0) {
										self.i += self.ntabs;
									}
									$ (self.__tabs [0]).css (dict ({'margin-left': -(self.tabWidth) * ((self.i + self.clones) + 1) + self.movimiento}));
								}
							}
							else if (self._loop == false) {
								if (self.i >= self.ntabs) {
									self.i = self.ntabs - 1;
								}
								else {
									self.i = 0;
								}
							}
							if (self.onlyActiveVisible) {
								var __iterable0__ = enumerate (self.tabs);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									if (k == n) {
										self.tabs [k].css (dict ({'opacity': '1'}));
									}
									else {
										self.tabs [k].css (dict ({'opacity': '0'}));
									}
								}
							}
							$ (self.__tabs [0]).animate (dict ({'margin-left': -(self.tabWidth) * self.i - (self._loop == true ? self.tabWidth * 3 : 0)}));
							$ (self.__tabs [0]).css (dict ({'margin-left': -(self.tabWidth) * self.i - (self._loop == true ? self.tabWidth * 3 : 0)}));
						});},
						get addToTab () {return __get__ (this, function (self, n, target) {
							target.py_update ();
							$ (self.__tabs [n]).html (target.target);
						});},
						get getTab () {return __get__ (this, function (self, n) {
							return $ (self.__tabs [n].children [0]);
						});},
						get appendToSlide () {return __get__ (this, function (self, n, target) {
							target.py_update ();
							self.tabs [n].append (target.target);
						});},
						get right () {return __get__ (this, function (self, evt) {
							if (self.i < len (self.tabs)) {
								self.i++;
								self.showTab (self.i);
							}
						});},
						get left () {return __get__ (this, function (self, evt) {
							if (self.i > 0) {
								self.i--;
								self.showTab (self.i);
							}
						});},
						get bgToSlide () {return __get__ (this, function (self, n, src) {
							self.tabs [n].css (dict ({'background-image': "url('{}')".format (src)}));
						});},
						get loop () {return __get__ (this, function (self, tiempo) {
							self.i = 0;
							self._loop = true;
							var play = function () {
								if (len (self.tabs) == self.i) {
									self.i = 0;
								}
								else {
									self.showTab (self.i);
									self.i++;
								}
							};
							setInterval (play, tiempo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.width = self.tabWidth * len (self.tabs);
							self.__titulo.text (self._titulo);
							$ (self.target).find ('>div').css (dict ({'width': str (self.width) + 'px'}));
							self.__update__ ();
							if (self.onlyActiveVisible) {
								var __iterable0__ = enumerate (self.tabs);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									if (k != 0) {
										elem.css (dict ({'opacity': '0'}));
									}
								}
							}
							self.__tabs.css (dict ({'width': str (self.tabWidth) + 'px'}));
							if (self._loop) {
								for (var i = 0; i < self.clones; i++) {
									$ (self.target).find ('>div').append ($ (self.tabs [i]).clone ());
								}
								for (var i = 0; i < self.clones; i++) {
									$ (self.target).find ('>div').prepend ($ (self.tabs [(self.ntabs - i) - 1]).clone ());
								}
							}
							self.__tabs = $ (self.target).find ('>div').find ('>.tab');
							$ (self.__tabs [0]).css (dict ({'margin-left': -(self.tabWidth) * self.i + (self._loop == true ? -(self.tabWidth) * 3 : 0)}));
							self.target.find ('>div').css (dict ({'height': str (self.height) + 'px', 'width': str ((self.ntabs + 6) * self.tabWidth) + 'px'}));
							self.target.append ("<div class='controles'> <span class='left'></span><span class='right'></span></div>");
							self.target.find ('>.controles').find ('>.left').css (dict ({'background-image': "url('{}')".format (self.btn_left), 'background-size': 'contain'}));
							self.target.find ('>.controles').find ('>.right').css (dict ({'background-image': "url('{}')".format (self.btn_right), 'background-size': 'contain'}));
							self.target.find ('>.controles').find ('>.left').bind ('click', self.left);
							self.target.find ('>.controles').find ('>.right').bind ('click', self.right);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicSlider = BasicSlider;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
