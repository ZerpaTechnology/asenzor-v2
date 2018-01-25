	__nest__ (
		__all__,
		'BuilderSettings', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BuilderSettings';
					var Widget = __init__ (__world__.Widget).Widget;
					var BuilderSettings = __class__ ('BuilderSettings', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Insertar Modulo';
							};
							Widget.__init__ (self, titulo);
							self._html = '';
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get open () {return __get__ (this, function (self) {
							self.target.show ();
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.titulo (self._titulo);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BuilderSettings = BuilderSettings;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
