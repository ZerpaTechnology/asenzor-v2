	__nest__ (
		__all__,
		'InsertModulo', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'InsertModulo';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var ModuloHTML = __init__ (__world__.ModuloHTML).ModuloHTML;
					var Modulo = __init__ (__world__.Modulo).Modulo;
					var InsertModulo = __class__ ('InsertModulo', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Insertar Modulo';
							};
							Widget.__init__ (self, titulo);
							self._html = "<div class='content'></div>";
							self.target.html (self._html);
							self.__button = self.target.find ('>button');
							self.BasicTabs = BasicTabs ();
							self._modulos = list ([ModuloHTML ()]);
							self.col = 0;
							self.column = null;
							self.window = null;
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
							self.BasicTabs.py_update ();
							self.Builder.window._nav = list ([list (['Nuevo Modulo', 'new', (function __lambda__ (self) {
								return (function __lambda__ (evt) {
									return null;
								});
							})]), list (['Cargar de la libreria', 'load', (function __lambda__ (self) {
								return (function __lambda__ (evt) {
									return null;
								});
							})])]);
							var __iterable0__ = self._modulos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var modulo = __iterable0__ [__index0__];
								var modulo = modulo.clone ();
								modulo.window = self.Builder.window;
								modulo.column = self.column;
								self.BasicTabs.appendToTab (0, modulo);
							}
							self.target.find ('>.content').append (self.BasicTabs.target);
							self.__titulo = self.target.find ('>.titulo');
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'Modulo' +
						'ModuloHTML' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.InsertModulo = InsertModulo;
						__all__.Modulo = Modulo;
						__all__.ModuloHTML = ModuloHTML;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
