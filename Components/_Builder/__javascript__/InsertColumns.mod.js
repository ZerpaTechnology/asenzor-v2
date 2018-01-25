	__nest__ (
		__all__,
		'InsertColumns', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'InsertColumns';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var config = Config.Config ();
					var InsertColumns = __class__ ('InsertColumns', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Insertar Columnas';
							};
							Widget.__init__ (self, titulo);
							self._html = "<div class='content'></div>";
							self._columns = dict ({'1': config.base_url + 'static/imgs/columna-1.png', '1/2-1/4-1/4': config.base_url + 'static/imgs/columna-1_2-1_4-1_4.png', '1/4-1/4-1/2': config.base_url + 'static/imgs/columna-1_4-1_4-1_2.png', '1/3': config.base_url + 'static/imgs/columna-1_3.png', '3/4-1/4': config.base_url + 'static/imgs/columna-3_4-1_4-.png', '1/4-3/4': config.base_url + 'static/imgs/columna-1_4-3_4-.png', '1/2': config.base_url + 'static/imgs/columna-1_2.png', '1/4': config.base_url + 'static/imgs/columna-1_4.png'});
							self.library = dict ({'nombre': list ([dict ({'1/2': list (['modulo'])})])});
							self.row = 0;
							self.BasicTabs = BasicTabs (2);
							self.BasicTabs.tabWidth = '100%';
							self.BasicTabs.width = '100%';
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get insertar () {return __get__ (this, function (self, evt) {
							var col = list (['md-12']);
							if ($ (evt.target).attr ('name') == '1') {
								var col = list (['md-12']);
							}
							else if ($ (evt.target).attr ('name') == '1/2-1/4-1/4') {
								var col = list (['md-6', 'md-3', 'md-3']);
							}
							else if ($ (evt.target).attr ('name') == '1/4-1/4-1/2') {
								var col = list (['md-3', 'md-3', 'md-6']);
							}
							else if ($ (evt.target).attr ('name') == '1/3') {
								var col = list (['md-4', 'md-4', 'md-4']);
							}
							else if ($ (evt.target).attr ('name') == '1/3') {
								var col = list (['md-4', 'md-4', 'md-4']);
							}
							else if ($ (evt.target).attr ('name') == '3/4-1/4') {
								var col = list (['md-8', 'md-4']);
							}
							else if ($ (evt.target).attr ('name') == '1/4-3/4') {
								var col = list (['md-4', 'md-8']);
							}
							else if ($ (evt.target).attr ('name') == '1/2') {
								var col = list (['md-6', 'md-6']);
							}
							else if ($ (evt.target).attr ('name') == '1/4') {
								var col = list (['md-3', 'md-3', 'md-3', 'md-3']);
							}
							self.Builder.addCols (self.row, col);
							self.Builder.window.close ();
						});},
						get tabNew () {return __get__ (this, function (self, evt) {
							self.BasicTabs.showTab (0);
						});},
						get tabLoad () {return __get__ (this, function (self, evt) {
							self.BasicTabs.showTab (1);
						});},
						get done () {return __get__ (this, function (self) {
							// pass;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.Builder.window._nav = list ([list (['Nueva columna', 'new', (function __lambda__ (self) {
								return (function __lambda__ (evt) {
									return null;
								});
							})]), list (['Cargar de la libreria', 'load', (function __lambda__ (self) {
								return (function __lambda__ (evt) {
									return null;
								});
							})])]);
							self.BasicTabs.py_update ();
							var __iterable0__ = self._columns.py_keys ();
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var img = $ ('<img>');
								self.BasicTabs.appendToTab (0, img);
								img.attr ('src', self._columns [elem]);
								img.attr ('name', elem);
								img.css (dict ({'width': '300px', 'margin': '10px', 'cursor': 'pointer'}));
								img.bind ('click', self.insertar);
							}
							self.target.find ('>.content').append (self.BasicTabs.target);
							return self.target;
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.InsertColumns = InsertColumns;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
