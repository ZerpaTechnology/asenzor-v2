	__nest__ (
		__all__,
		'BandaTema', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BandaTema';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var BandaTema = __class__ ('BandaTema', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<div>\n\t\t<div class="text">\n\t\t{}\n\t\t</div>\n\t\t<button>{}</button>\n\t\t</div>\n\t\t';
							self.text = 'Tema activo:<br>' + settings.app;
							self.btn_titulo = 'Cambiar';
							self._html = self._html.format (self.text, self.btn_titulo);
							$ (self.target).html (self._html);
						});},
						get py_update () {return __get__ (this, function (self) {
							// pass;
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BandaTema = BandaTema;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
