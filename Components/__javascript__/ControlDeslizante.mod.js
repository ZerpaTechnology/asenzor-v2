	__nest__ (
		__all__,
		'ControlDeslizante', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ControlDeslizante';
					var Widget = __init__ (__world__.Widget).Widget;
					var ControlDeslizante = __class__ ('ControlDeslizante', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Barra deslizante';
							};
							Widget.__init__ (self, titulo);
							self.orientacion = 'horizontal';
							self._html = "<div><span class='titulo'>{}</span><div class='barra'><button class='guia'></button></div></div>";
							self.grosor = 10;
							self.range = list ([0, 100]);
							self.largo = 300;
							self.presionado = false;
							self.value = 0;
							self.posInicial = 0;
							self.___barra = null;
							self.___guia = null;
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
										}
										else {
											self.__guia.css (dict ({'top': '0px'}));
										}
									}
									else if (((posRelative.top + deltatop) + height) + 2 < self.largo) {
										self.__guia.css (dict ({'top': str (posRelative.top + deltatop) + 'px'}));
									}
									else {
										self.__guia.css (dict ({'top': str ((self.largo - height) - 2) + 'px'}));
										self.value = 100;
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
							self.__barra = self.target.find ('>div').find ('>.barra');
							self.__guia = self.__barra.find ('>.guia');
							var valor = ((self.value * self.largo) / 100 - self.grosor / 2) - 5;
							if (self.orientacion == 'horizontal') {
								self.target.find ('>div').css (dict ({'flex-direction': 'column', 'display': 'flex', 'justify-content': 'space-between'}));
								self.__barra.css (dict ({'width': str (self.largo) + 'px', 'height': str (self.grosor) + 'px'}));
								self.__guia.css (dict ({'width': str (self.grosor + 10) + 'px', 'top': '-5px', 'left': str (valor) + 'px', 'height': str (self.grosor + 10) + 'px'}));
							}
							else if (self.orientacion == 'vertical') {
								self.target.find ('>div').find ('>span').css (dict ({'display': 'block'}));
								self.target.find ('>div').css (dict ({'text-align': 'center'}));
								self.__barra.css (dict ({'height': str (self.largo) + 'px', 'width': str (self.grosor) + 'px', 'display': 'inline-block'}));
								self.__guia.css (dict ({'height': str (self.grosor + 10) + 'px', 'left': '-5px', 'top': str (valor) + 'px', 'width': str (self.grosor + 10) + 'px'}));
							}
							$ (document).on ('mouseup', self.soltar);
							$ (document).on ('mousemove', self.arrastrar);
							self.__guia.on ('mousedown', self.presionar);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ControlDeslizante = ControlDeslizante;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
