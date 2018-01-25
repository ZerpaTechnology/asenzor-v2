	__nest__ (
		__all__,
		'Modulo', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Modulo';
					var Widget = __init__ (__world__.Widget).Widget;
					var Modulo = __class__ ('Modulo', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span class='close'>x</span>\n\t\t<span class='titulo'></span>\n\t\t<span class='config'></span>\n\t\t";
							self.modulo = null;
							self.target.html (self._html);
							self.__button = self.target.find ('>button');
							self._html = '';
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.titulo (self._titulo);
							self.__titulo = self.target.find ('>.titulo');
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Modulo = Modulo;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
