	__nest__ (
		__all__,
		'BuilderModulo', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BuilderModulo';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var BuilderModulo = __class__ ('BuilderModulo', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Insertar Columnas';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div class='caja'>\n\t\t</div>\n\t\t<div class='caja2'>\n\t\t</div>\n\t\t";
							self.target.html (self._html);
							self.__button = self.target.find ('>button');
							self._html = '';
							self.BasicTabs = BasicTabs ();
							self._modulos = list ([]);
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.titulo (self._titulo);
							var __iterable0__ = self._modulos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								// pass;
							}
							self.__titulo = self.target.find ('>.titulo');
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.BuilderModulo = BuilderModulo;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
