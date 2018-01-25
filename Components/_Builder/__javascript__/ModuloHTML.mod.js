	__nest__ (
		__all__,
		'ModuloHTML', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ModuloHTML';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var TinyMCE = __init__ (__world__.TinyMCE).TinyMCE;
					var Button = __init__ (__world__.Button).Button;
					var Input = __init__ (__world__.Input).Input;
					var ModuloHTML = __class__ ('ModuloHTML', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Insertar Modulo';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<button>\n\t\t<span class='icon'></span>\n\t\t<b class='titulo'></b>\n\t\t</button>\n\t\t";
							self._html2 = self._html;
							self._html3 = '';
							self.BasicTabs = BasicTabs ();
							self.window = null;
							self.column = null;
							self._contenido = '';
							self.dataChildren = list ([dict ({}), dict ({}), dict ({})]);
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.__titulo.text (titulo);
							self._titulo = titulo;
						});},
						get insertar () {return __get__ (this, function (self, evt) {
							self.column.add (self, 2);
							self.window.close ();
						});},
						get open () {return __get__ (this, function (self, evt) {
							self.window.Modulo = self;
							self.window._nav = list ([list (['General Settings', 'settings', (function __lambda__ (self2) {
								return (function __lambda__ (evt) {
									return self.BasicTabs.showTab (0);
								});
							})]), list (['Custom CSS', 'load', (function __lambda__ (self2) {
								return (function __lambda__ (evt) {
									return self.BasicTabs.showTab (1);
								});
							})])]);
							self.window._footerNav = list ([list (['Guardar', 'save', (function __lambda__ (self2) {
								return (function __lambda__ (evt) {
									return null;
								});
							})])]);
							self.window.open ('Modulo');
						});},
						get done () {return __get__ (this, function (self) {
							self.BasicTabs.width = '100%';
							self.BasicTabs.tabWidth = '100%';
							self.BasicTabs.py_update ();
							var i = Input ('Titulo:');
							var t = TinyMCE ('Contenido:');
							t.data = self.dataChildren [1];
							if (__in__ ('value', self.dataChildren [1])) {
								t.value = self.dataChildren [1] ['value'];
							}
							$.when (self.target3.html (self.BasicTabs.target)).then (self.BasicTabs.done);
							self.BasicTabs.appendToTab (0, i);
							self.BasicTabs.appendToTab (0, t);
							self.target.find ('>button').on ('click', self.insertar);
							self.target2.find ('>button').find ('>.titulo').text ('prueba');
							self.target2.find ('>button').on ('click', self.open);
							self.__titulo = self.target.find ('>button').find ('>.titulo');
							self.titulo (self._titulo);
							t.reconectar ();
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'Button' +
						'Input' +
						'TinyMCE' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.Button = Button;
						__all__.Input = Input;
						__all__.ModuloHTML = ModuloHTML;
						__all__.TinyMCE = TinyMCE;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
