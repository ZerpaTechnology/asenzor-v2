	__nest__ (
		__all__,
		'ButtonSettings', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ButtonSettings';
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonSettings = __class__ ('ButtonSettings', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, siguiente, _screen) {
							if (typeof siguiente == 'undefined' || (siguiente != null && siguiente .hasOwnProperty ("__kwargtrans__"))) {;
								var siguiente = 1;
							};
							if (typeof _screen == 'undefined' || (_screen != null && _screen .hasOwnProperty ("__kwargtrans__"))) {;
								var _screen = 0;
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span>\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t</span>";
							self.slider = null;
							self.screen = null;
							self.descripcion = '';
							self._siguiente = siguiente;
							self._screen = _screen;
						});},
						get siguiente () {return __get__ (this, function (self, evt) {
							self.screen.showTab (self._screen);
							self.slider.showTab (self._siguiente);
						});},
						get py_update () {return __get__ (this, function (self) {
							self._update = true;
							self._html = self._html.format (self.titulo, self.descripcion);
							self.target.bind ('click', self.siguiente);
							$ (self.target).html (self._html);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonSettings = ButtonSettings;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
