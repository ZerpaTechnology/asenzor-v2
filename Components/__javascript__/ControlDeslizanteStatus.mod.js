	__nest__ (
		__all__,
		'ControlDeslizanteStatus', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ControlDeslizanteStatus';
					var Widget = __init__ (__world__.Widget).Widget;
					var ControlDeslizanteStatus = __class__ ('ControlDeslizanteStatus', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Barra deslizante';
							};
							Widget.__init__ (self, titulo);
							self.orientacion = 'horizontal';
							self.target.html ("\n\t\t\t<span class='titulo'></span>\n\t\t\t<div>\n\t\t\t<div class='frames'>\n\t\t\t</div>\n\t\t<div>\n\t\t\t<div class='barra'>\n\t\t\t<button class='guia'>\n\t\t\t</button>\n\t\t</div>\n\t\t</div>\n\t\t</div>");
							self.grosor = 10;
							self.range = list ([0, 100]);
							self.frames = 10;
							self.largo = 300;
							self.presionado = false;
							self.value = 0;
							self.posInicial = 0;
							self.__barra = null;
							self.__guia = null;
							self.grosorFrames = 30;
							self.largo_guia = 20;
							self.colores = list ([tuple ([43, 118, 255]), tuple ([0, 255, 30]), tuple ([255, 0, 0])]);
						});},
						get getValueForRange () {return __get__ (this, function (self) {
							var delta = self.range [1] - self.range [0];
							return (self.value * delta) / 100;
						});},
						get arrastrar () {return __get__ (this, function (self, evt) {
							if (self.presionado) {
								var posRelative = self.__guia.position ();
								var width = self.__guia.outerWidth ();
								var height = self.__guia.outerHeight ();
								var posAbsolute = self.__guia.offset ();
								var deltaleft = evt.clientX - posAbsolute.left;
								var deltatop = evt.clientY - posAbsolute.top;
								if (self.orientacion == 'horizontal') {
									self.value = (posRelative.left * 100) / ((self.largo - self.grosor) - 10);
									if (deltaleft < 0) {
										if (posRelative.left + deltaleft >= 0) {
											self.__guia.css (dict ({'left': str (posRelative.left + deltaleft) + 'px'}));
										}
										else {
											self.__guia.css (dict ({'left': '0px'}));
										}
									}
									else if (((posRelative.left + deltaleft) + width) + 2 < self.largo) {
										self.__guia.css (dict ({'left': str (posRelative.left + deltaleft) + 'px'}));
									}
									else {
										self.__guia.css (dict ({'left': str ((self.largo - width) - 2) + 'px'}));
										self.value = 100;
									}
								}
								else if (self.orientacion == 'vertical') {
									self.value = (posRelative.top * 100) / ((self.largo - self.grosor) - 10);
									if (deltatop < 0) {
										if (posRelative.top + deltatop >= 0) {
											self.__guia.css (dict ({'top': str (posRelative.top + deltatop) + 'px'}));
											var delta = self.range [1] - self.range [0];
											self.value = (posRelative.top * 100) / (self.largo - self.grosor);
										}
										else {
											self.__guia.css (dict ({'top': '0px'}));
											self.value = (0 * 100) / (self.largo - self.grosor);
										}
									}
									else if (((posRelative.top + deltatop) + height) + 2 < self.largo) {
										self.__guia.css (dict ({'top': str (posRelative.top + deltatop) + 'px'}));
										self.value = (posRelative.top * 100) / (self.largo - self.grosor);
									}
									else {
										self.__guia.css (dict ({'top': str ((self.largo - height) - 2) + 'px'}));
										self.value = ((self.largo - self.grosor) * 100) / (self.largo - self.grosor);
									}
								}
							}
						});},
						get presionar () {return __get__ (this, function (self, evt) {
							self.presionado = true;
							self.posInicial = list ([evt.clientX, evt.clientY]);
						});},
						get soltar () {return __get__ (this, function (self, evt) {
							self.presionado = false;
						});},
						get mover () {return __get__ (this, function (self, valor) {
							// pass;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.__barra = self.target.find ('>div').find ('>div').find ('>.barra');
							self.__guia = self.__barra.find ('>.guia');
							self._frames = self.target.find ('>div').find ('>.frames');
							self.largo_guia = -(self.largo_guia);
							var i_limite = self.frames / len (self.colores);
							var deltaX = int (self.frames / len (self.colores));
							var color_current = 0;
							var c = 1;
							var __iterable0__ = enumerate (range (self.frames));
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var x = __left0__ [0];
								var elem = __left0__ [1];
								var i = $ ('<span></span>');
								if (x >= i_limite) {
									i_limite += deltaX;
									color_current++;
									var dr = self.colores [color_current] [0];
									var dg = self.colores [color_current] [1];
									var db = self.colores [color_current] [2];
									var c = 0;
								}
								else if (color_current < len (self.colores) - 1) {
									var dr = self.colores [color_current + 1] [0] - self.colores [color_current] [0];
									var dg = self.colores [color_current + 1] [1] - self.colores [color_current] [1];
									var db = self.colores [color_current + 1] [2] - self.colores [color_current] [2];
									var _dr = dr / deltaX;
									var _dg = dg / deltaX;
									var _db = db / deltaX;
									var dr = int (abs (self.colores [color_current] [0] + c * _dr));
									var dg = int (abs (self.colores [color_current] [1] + c * _dg));
									var db = int (abs (self.colores [color_current] [2] + c * _db));
								}
								else {
									var dr = self.colores [len (self.colores) - 1] [0];
									var dg = self.colores [len (self.colores) - 1] [1];
									var db = self.colores [len (self.colores) - 1] [2];
								}
								c++;
								var color = 'rgb' + str (tuple ([dr, dg, db]));
								self._frames.append (i);
								i.css (dict ({'background-color': color}));
							}
							var valor = ((self.value * self.largo) / 100 - self.grosor / 2) - 5;
							if (self.orientacion == 'horizontal') {
								self.target.find ('>div').css (dict ({'flex-direction': 'column'}));
								self.target.find ('>div').find ('>div').css (dict ({'flex-direction': 'row', 'display': 'flex'}));
								self._frames.css (dict ({'display': 'flex', 'flex-direction': 'row', 'width': str (abs (self.largo)), 'height': str (self.grosorFrames)}));
								self.__barra.css (dict ({'width': str (self.largo) + 'px', 'height': str (self.grosor) + 'px'}));
								self.__guia.css (dict ({'width': str (self.grosor + 10) + 'px', 'top': str (self.largo_guia) + 'px', 'left': str (valor) + 'px', 'height': str ((self.grosor + abs (self.largo_guia)) + 10) + 'px'}));
							}
							else if (self.orientacion == 'vertical') {
								self.target.find ('>div').find ('>span').css (dict ({'display': 'block'}));
								self.target.find ('>div').css (dict ({'text-align': 'center', 'display': 'flex', 'justify-content': 'flex-start'}));
								self._frames.css (dict ({'display': 'flex', 'flex-direction': 'column', 'height': str (abs (self.largo)), 'width': str (self.grosorFrames)}));
								self.__barra.css (dict ({'height': str (self.largo) + 'px', 'width': str (self.grosor) + 'px', 'display': 'inline-block'}));
								self.__guia.css (dict ({'height': str (self.grosor + 10) + 'px', 'left': str (self.largo_guia) + 'px', 'top': str (valor) + 'px', 'width': str ((self.grosor + abs (self.largo_guia)) + 10) + 'px'}));
							}
							$ (document).on ('mouseup', self.soltar);
							$ (document).on ('mousemove', self.arrastrar);
							self.__guia.on ('mousedown', self.presionar);
							self.titulo (self._titulo);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ControlDeslizanteStatus = ControlDeslizanteStatus;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
