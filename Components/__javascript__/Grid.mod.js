	__nest__ (
		__all__,
		'Grid', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var random = {};
					var __name__ = 'Grid';
					var Widget = __init__ (__world__.Widget).Widget;
					__nest__ (random, '', __init__ (__world__.random));
					var BoxGrid = __class__ ('BoxGrid', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t';
							self.target.html (self._html);
							self.container = 'container';
							self.__button = self.target.find ('>button');
							self._hmtl = '';
							self.colored = true;
							self.paletadeColores = list (['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#16a085', '#27ae60', '#2980b9', '#8e44ad', '#2c3e50', '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1', '#95a5a6', '#f39c12', '#d35400', '#c0392b', '#bdc3c7', '#7f8c8d']);
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get appendRow () {return __get__ (this, function (self) {
							var html = "<div class='row'></div>";
							self.target.append (html);
						});},
						get appendRows () {return __get__ (this, function (self, n) {
							var html = "<div class='row'></div>".repeat (n);
							self.target.append (html);
						});},
						get addCols () {return __get__ (this, function (self, row, lista) {
							if (typeof lista == 'undefined' || (lista != null && lista .hasOwnProperty ("__kwargtrans__"))) {;
								var lista = list (['md-4', 'md-8']);
							};
							var __iterable0__ = lista;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (py_typeof (elem) == list) {
									var clase = '';
									var __iterable1__ = elem;
									for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
										var elem2 = __iterable1__ [__index1__];
										var clase = (clase + ' col-') + elem;
									}
									var col = $ (("<div class='" + clase) + "'></div>");
									$ (self.target.find ('>.row') [row]).add (col);
									if (colored == true) {
										col.css (dict ({'background-color': self.paleta [random.randrange (0, len (self.paleta))]}));
									}
								}
								else {
									var col = $ (("<div class='col-md-" + elem) + "'></div>");
									$ (self.target.find ('>.row') [row]).add (col);
									if (colored == true) {
										col.css (dict ({'background-color': self.paleta [random.randrange (0, len (self.paleta))]}));
									}
								}
							}
						});},
						get addToCol () {return __get__ (this, function (self, row, col, widget) {
							widget.py_update ();
							$ ($ (self.target.find ('>.row') [row]).find ('>div') [col]).html (widget.target);
							return $ ($ (self.target.find ('>.row') [row]).find ('>div') [col]);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.titulo (self._titulo);
							self.__titulo = self.target.find ('>.titulo');
							self.target.addClass ('container');
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
						'random' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BoxGrid = BoxGrid;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
