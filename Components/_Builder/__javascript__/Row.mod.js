	__nest__ (
		__all__,
		'_Builder.Row', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_Builder.Row';
					var Widget = __init__ (__world__.Widget).Widget;
					var Row = __class__ ('Row', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<sidebar class=\'controls\'>\n\t\t\t<span class=\'menu\'></span>\n\t\t\t<span class=\'duplicate\'></span>\n\t\t\t<span class=\'quit\'></span>\n\t\t</sidebar>\n\t\t<div class="content">\n\t\t<span class=\'add\'> Añadir </span>\n\t\t</div>\n\t\t';
							self.i = 0;
							self.window = null;
						});},
						get add () {return __get__ (this, function (self, widget) {
							widget.py_update ();
							self.children.append (widget);
							$.when (self.target.find ('>.content').find ('>.add').before (widget.target)).then (widget.done);
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get addCols () {return __get__ (this, function (self, evt) {
							self.window.InsertColumns.row = self.i;
							self.window.py_update ();
							self.window.open ('InsertColumns');
						});},
						get done () {return __get__ (this, function (self) {
							self.__button = self.target.find ('>button');
							self.__titulo = self.target.find ('>.titulo');
							self.__add = self.target.find ('>.content').find ('.add');
							self.titulo (self._titulo);
							self.__add.bind ('click', self.addCols);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Row = Row;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
