	__nest__ (
		__all__,
		'RadioButtonList', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'RadioButtonList';
					var Widget = __init__ (__world__.Widget).Widget;
					var RadioButton = __init__ (__world__.RadioButton).RadioButton;
					var RadioButtonList = __class__ ('RadioButtonList', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='content'>\n\t\t</div>\n\t\t";
							self.descripcion = '';
						});},
						get addOptions () {return __get__ (this, function (self, lista, seleccionado) {
							if (typeof seleccionado == 'undefined' || (seleccionado != null && seleccionado .hasOwnProperty ("__kwargtrans__"))) {;
								var seleccionado = 0;
							};
							var __iterable0__ = enumerate (lista);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								var w = RadioButton (elem);
								if (k == seleccionado) {
									w.activar ();
								}
								self.children.append (w);
								self.add (w);
							}
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).find ('>.content').append (target.target);
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion));
						});}
					});
					__pragma__ ('<use>' +
						'RadioButton' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.RadioButton = RadioButton;
						__all__.RadioButtonList = RadioButtonList;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
