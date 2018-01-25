	__nest__ (
		__all__,
		'Builder', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Builder';
					var Widget = __init__ (__world__.Widget).Widget;
					var Row = __init__ (__world__._Builder.Row).Row;
					var Column = __init__ (__world__._Builder.Column).Column;
					var Modulo = __init__ (__world__._Builder.Modulo).Modulo;
					var Window = __init__ (__world__._Builder.Window).Window;
					var Builder = __class__ ('Builder', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, __kwargtrans__ ({titulo: 'Builder-Z'}));
							self._html = "\n\t\t<div class='header'>\n\t\t\t<div>\n\t\t\t<b class='titulo'></b>\n\t\t\t<div>\n\t\t\t\t<span class='minimizar'></span>\n\t\t\t</div>\n\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class='btns'>\n\t\t\t\t<div class='btns-left'>\n\t\t\t\t\t<span class='save'>Guardar libreria</span>\n\t\t\t\t\t<span class='load'>Cargar libreria</span>\n\t\t\t\t\t<span class='clear'>Limpiar layout</span>\n\t\t\t\t</div>\n\t\t\t\t<div class='btns-right'>\n\t\t\t\t\t<span class='deshacer'></span>\n\t\t\t\t\t<span class='rehacer'></span>\n\t\t\t\t\t<span class='historial'></span>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t\t<div class='content'>\n\t\t<span class='add'> Añadir </span>\n\t\t</div>\t\t\n\t\t<div class='window'></div>\n\t\t";
							self._rows = list ([]);
							self.window = Window ();
							self.window.Builder = self;
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get appendRow () {return __get__ (this, function (self) {
							var row = Row ();
							self._rows.append (row);
							row.i = self._rows.index (row);
							row.window = self.window;
							row.py_update ();
							$.when (self.target.find ('>.content').find ('>.add').before (row.target)).then (row.done);
						});},
						get moveRow () {return __get__ (this, function (self, acutal, destino) {
							// pass;
						});},
						get changeRow () {return __get__ (this, function (self, acutal, destino) {
							// pass;
						});},
						get addCols () {return __get__ (this, function (self, row, lista) {
							if (typeof lista == 'undefined' || (lista != null && lista .hasOwnProperty ("__kwargtrans__"))) {;
								var lista = null;
							};
							print (lista);
							if (lista == null) {
								self._rows [row].InsertColumns.open ();
							}
							else {
								var __iterable0__ = lista;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (py_typeof (elem) != str) {
										var clase = '';
										var col = Column ();
										var __iterable1__ = elem;
										for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
											var elem2 = __iterable1__ [__index1__];
											if (__in__ ('md-', elem2)) {
												col.size = int (elem2.py_replace ('md-', ''));
												col._titulo = str (col.size);
												col.window = self.window;
											}
											var clase = (clase + ' col-') + elem2;
										}
										self._rows [row].add (col);
									}
									else {
										var col = Column ();
										col.size = int (elem.py_replace ('md-', ''));
										col._titulo = str (col.size);
										col.window = self.window;
										self._rows [row].add (col);
									}
								}
							}
						});},
						get addToCol () {return __get__ (this, function (self, row, col, widget) {
							widget.py_update ();
							$.when ($ ($ (self.target.find ('>.row') [row]).find ('>div') [col]).html (widget.target)).then (widget.done);
							return $ ($ (self.target.find ('>.row') [row]).find ('>div') [col]);
						});},
						get addModulo () {return __get__ (this, function (self, row, col, modulo) {
							if (typeof modulo == 'undefined' || (modulo != null && modulo .hasOwnProperty ("__kwargtrans__"))) {;
								var modulo = null;
							};
							if (modulo == 'default') {
								var m = Modulo (modulo);
								self._rows [row].children [col].add (m);
							}
						});},
						get done () {return __get__ (this, function (self) {
							// pass;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.window.py_update ();
							self.__update__ ();
							self.__button = self.target.find ('>button');
							self.__add = self.target.find ('>.content').find ('>.add');
							self.__add.on ('click', self.appendRow);
							self.titulo (self._titulo);
							$.when (self.target.find ('>.window').html (self.window.target)).then (self.window.done);
							self.window.hidden ();
							self.__titulo = self.target.find ('>.titulo');
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
						'_Builder.Column' +
						'_Builder.Modulo' +
						'_Builder.Row' +
						'_Builder.Window' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Builder = Builder;
						__all__.Column = Column;
						__all__.Modulo = Modulo;
						__all__.Row = Row;
						__all__.Widget = Widget;
						__all__.Window = Window;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
