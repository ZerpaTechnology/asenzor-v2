	__nest__ (
		__all__,
		'_Builder.Window', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_Builder.Window';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var BuilderSettings = __init__ (__world__.BuilderSettings).BuilderSettings;
					var BuilderModulo = __init__ (__world__.BuilderModulo).BuilderModulo;
					var InsertColumns = __init__ (__world__.InsertColumns).InsertColumns;
					var InsertModulo = __init__ (__world__.InsertModulo).InsertModulo;
					var HorizontalScroll = __init__ (__world__.HorizontalScroll).HorizontalScroll;
					var config = Config.Config ();
					var Window = __class__ ('Window', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Ventana';
							};
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<div class=\'header\'>\n\t\t\t<div>\n\t\t\t<b class=\'titulo\'></b>\n\t\t\t<div>\n\t\t\t\t<span class=\'close\'>x</span>\n\t\t\t</div>\n\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class=\'btns\'>\n\t\t\t\t<div class=\'btns-left\'>\n\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n\t\t</div>\n\t\t<div class=\'content\'>\n\t\t\n\t\t</div>\t\t\n\t\t<div class="btnsFooter">\n\n\t\t</div>\n\t\t';
							self.target.html (self._html);
							self.__button = self.target.find ('>button');
							self._nav = list ([list (['Nuevo Modulo', 'save', (function __lambda__ (self2) {
								return (function __lambda__ (evt) {
									return null;
								});
							})]), list (['Cargar de la libreria', 'load', (function __lambda__ (self2) {
								return (function __lambda__ (evt) {
									return null;
								});
							})])]);
							self._footerNav = list ([]);
							self.BasicTabs = BasicTabs ();
							self.InsertColumns = InsertColumns ();
							self.InsertModulo = InsertModulo ();
							self.Modulo = null;
							self.data = dict ({});
							self.actual = 'InsertColumns';
							self.HorizontalScroll = HorizontalScroll ();
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get open () {return __get__ (this, function (self, ventana) {
							if (typeof ventana == 'undefined' || (ventana != null && ventana .hasOwnProperty ("__kwargtrans__"))) {;
								var ventana = 'InsertColumns';
							};
							self.target.show ();
							self.actual = ventana;
							self.InsertColumns.Builder = self.Builder;
							self.InsertModulo.Builder = self.Builder;
							self.done ();
							if (ventana == 'InsertColumns') {
								self.InsertColumns.py_update ();
								$.when (self.target.find ('>.content').html (self.InsertColumns.target)).then (self.InsertColumns.done);
							}
							else if (ventana == 'InsertModulo') {
								self.InsertModulo.py_update ();
								$.when (self.target.find ('>.content').html (self.InsertModulo.target)).then (self.InsertModulo.done);
							}
							else if (ventana == 'Modulo') {
								self.Modulo.py_update ();
								$.when (self.target.find ('>.content').html (self.Modulo.target3)).then (self.Modulo.done);
							}
						});},
						get close () {return __get__ (this, function (self, evt) {
							self.target.hide ();
						});},
						get updateNav () {return __get__ (this, function (self) {
							self.HorizontalScroll.py_update ();
							var __iterable0__ = self._nav;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var span = $ ('<span>');
								self.HorizontalScroll.add (span);
								span.addClass (elem [1]);
								span.text (elem [0]);
								span.on ('click', elem [2] (self));
							}
						});},
						get updateFooter () {return __get__ (this, function (self) {
							self.target.find ('>.content').css (dict ({'height': 'calc(100& - 200px)'}));
							var __iterable0__ = self._footerNav;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var span = $ ('<span>');
								span.addClass (elem [1]);
								span.text (elem [0]);
								self.__footerNav.append (span);
								span.on ('click', elem [2] (self));
							}
						});},
						get done () {return __get__ (this, function (self) {
							self.__nav = self.target.find ('>.header').find ('>.btns').find ('>.btns-left');
							self.__footerNav = self.target.find ('>.btnsFooter');
							$.when (self.__nav.html (self.HorizontalScroll.target)).done ($.when (self.updateNav ()).then (self.HorizontalScroll.done));
							self.__titulo = self.target.find ('>.titulo');
							self.__close = self.target.find ('>.header').find ('>div').find ('>div').find ('>.close');
							self.__close.on ('click', self.close);
							self.updateFooter ();
							self.titulo (self._titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'BuilderModulo' +
						'BuilderSettings' +
						'HorizontalScroll' +
						'InsertColumns' +
						'InsertModulo' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.BuilderModulo = BuilderModulo;
						__all__.BuilderSettings = BuilderSettings;
						__all__.HorizontalScroll = HorizontalScroll;
						__all__.InsertColumns = InsertColumns;
						__all__.InsertModulo = InsertModulo;
						__all__.Widget = Widget;
						__all__.Window = Window;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
