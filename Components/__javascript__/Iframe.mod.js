	__nest__ (
		__all__,
		'Iframe', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Iframe';
					var Widget = __init__ (__world__.Widget).Widget;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var Iframe = __class__ ('Iframe', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "<iframe src='' name=''></iframe>";
							self.target.html (self._html);
							self._html = '';
							self.py_name = self.titulo;
							self.source = '';
							self.primitivo = (function __lambda__ (self) {
								return self.target.find ('iframe');
							});
							self.__iframe = self.target.find ('>iframe');
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							self.__iframe.attr ('src', self.source);
							self.__iframe.attr ('name', self.py_name);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Iframe = Iframe;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
