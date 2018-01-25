	__nest__ (
		__all__,
		'Image', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var random = {};
					var __name__ = 'Image';
					var Widget = __init__ (__world__.Widget).Widget;
					__nest__ (random, '', __init__ (__world__.random));
					var config = Config.Config ();
					var Image = __class__ ('Image', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "<b class='titulo'></b><figure><img></figure><span class='descripcion'></span>";
							self.target.html (self._html);
							self.__button = self.target.find ('>button');
							self._html = '';
							self._src = '';
							self.activador = null;
							self._hoverEffect = null;
							self.inMoving = null;
							self.rotation = null;
							self.width = 400;
							self._tooltip = null;
							self._load_css = list ([config.base_url + '/static/css/hint.css-master/hint.css']);
							self._hint = self._titulo;
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('>.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.target.trigger ('click', list ([self]));
							if (self.activador != null) {
								self.target.bind ('click', self.activador (self));
							}
							self.__titulo = self.target.find ('>.titulo');
							self.titulo (self._titulo);
							self.target.find ('>figure').find ('>img').attr ('src', self._src);
							if (self._hoverEffect == 'vibrar') {
								// pass;
							}
							else if (self._hoverEffect == 'oscurecer') {
								// pass;
							}
							else if (self._hoverEffect == 'zoomIn') {
								self.target.find ('>figure').addClass ('hover03');
							}
							else if (self._hoverEffect == 'zoomOut') {
								self.target.find ('>figure').addClass ('hover04');
								// pass;
							}
							else if (self._hoverEffect == 'slide') {
								self.target.find ('>figure').addClass ('hover05');
							}
							else if (self._hoverEffect == 'rotate') {
								self.target.find ('>figure').addClass ('hover06');
							}
							else if (self._hoverEffect == 'blur') {
								self.target.find ('>figure').addClass ('hover07');
							}
							else if (self._hoverEffect == 'grayScale') {
								self.target.find ('>figure').addClass ('hover08');
							}
							else if (self._hoverEffect == 'sepia') {
								self.target.find ('>figure').addClass ('hover09');
							}
							else if (self._hoverEffect == 'blurGrayScale') {
								self.target.find ('>figure').addClass ('hover10');
							}
							else if (self._hoverEffect == 'opacity') {
								self.target.find ('>figure').addClass ('hover11');
							}
							else if (self._hoverEffect == 'opacityColor') {
								self.target.find ('>figure').addClass ('hover12');
							}
							else if (self._hoverEffect == 'opacityColorRandom') {
								// pass;
							}
							else if (self._hoverEffect == 'flash') {
								self.target.find ('>figure').addClass ('hover13');
							}
							else if (self._hoverEffect == 'shine') {
								self.target.find ('>figure').addClass ('hover14');
							}
							else if (self._hoverEffect == 'circle') {
								self.target.find ('>figure').addClass ('hover15');
							}
							if (self.rotation != null) {
								if (py_typeof (self.rotation) == list) {
									self.target.find ('>figure').find ('>img').css (dict ({'transform': ('rotate(' + str (random.randint (self.rotation [0], self.rotation [1]))) + 'deg)', 'width': self.width}));
								}
								else if (self.rotation == 'random') {
									self.target.find ('>figure').find ('>img').css (dict ({'transform': ('rotate(' + str (random.random () * 10)) + 'deg)', 'width': self.width}));
								}
								else {
									self.target.find ('>figure').find ('>img').css (dict ({'transform': ('rotate(' + str (self.rotation)) + 'deg)', 'width': self.width}));
								}
							}
							if (self._tooltip != null) {
								self.target.addClass ('hint--' + self._tooltip);
								self.target.attr ('data-hint', self._hint);
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
						'random' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Image = Image;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
