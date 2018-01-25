	__nest__ (
		__all__,
		'DragSlider', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'DragSlider';
					var BasicSlider = __init__ (__world__.BasicSlider).BasicSlider;
					var DragSlider = __class__ ('DragSlider', [BasicSlider], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, tabs) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							if (typeof tabs == 'undefined' || (tabs != null && tabs .hasOwnProperty ("__kwargtrans__"))) {;
								var tabs = 3;
							};
							BasicSlider.__init__ (self, titulo, tabs);
							self.presionado = false;
							self.i = 0;
							self._left = 0;
							self.tempWrappers = null;
							self.posInicial = list ([0, 0]);
							self.onlyActiveVisible = false;
							self._loop = true;
							self.movimiento = 0;
						});},
						get presionar () {return __get__ (this, function (self, evt) {
							self.presionado = true;
							var div = $ ('<div>');
							self.tempWrappers = div;
							self.posInicial = list ([evt.clientX, evt.clientY]);
							$ ('iframe').parent ().append (div);
							div.css (dict ({'position': 'absolute', 'top': '0px', 'left': '0px', 'width': '100%', 'height': '100%', '-webkit-user-select': 'none', '-moz-user-select': 'none', '-ms-user-select': 'none', 'user-select': 'none'}));
						});},
						get soltar () {return __get__ (this, function (self, evt) {
							if (self.presionado == true) {
								self.tempWrappers.remove ();
								self.presionado = false;
								self.i = -(int ((self._left + (self.loop == true ? self.tabWidth * 3 : 0)) / self.tabWidth));
								self.showTab (self.i);
								self.__tabs.css (dict ({'-webkit-user-select': 'inherit', '-moz-user-select': 'inherit', '-ms-user-select': 'inherit', 'user-select': 'inherit'}));
							}
							$ (document).css (dict ({'cursor': 'inherit'}));
							self.movimiento = 0;
						});},
						get arrastrar () {return __get__ (this, function (self, evt) {
							if (self.presionado == true) {
								self.movimiento = (evt.clientX - self.posInicial [0]) * 1.4;
								self._left = (self.movimiento - self.tabWidth * self.i) - (self.loop == true ? self.tabWidth * 3 : 0);
								$ (self.__tabs [0]).css (dict ({'margin-left': str (self._left) + 'px'}));
								self.__tabs.css (dict ({'-webkit-user-select': 'none', '-moz-user-select': 'none', '-ms-user-select': 'none', 'user-select': 'none'}));
								$ (document).css (dict ({'cursor': 'move'}));
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							BasicSlider.py_update (self);
							var __iterable0__ = self.tabs;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.on ('mousedown', self.presionar);
							}
							$ (document).on ('mousemove', self.arrastrar);
							$ (document).on ('mouseup', self.soltar);
							$ (document).on ('mouseout', self.salio);
						});}
					});
					__pragma__ ('<use>' +
						'BasicSlider' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicSlider = BasicSlider;
						__all__.DragSlider = DragSlider;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
