	__nest__ (
		__all__,
		'SelectColor', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SelectColor';
					var Widget = __init__ (__world__.Widget).Widget;
					var SelectColor = __class__ ('SelectColor', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<label>{}</label>\n\t\t<input type='color' name='{}'>\n\t\t";
							self.py_name = '';
							self.value = null;
						});},
						get change () {return __get__ (this, function (self) {
							self.value = $ (self.target).find ("input[type='color']").val ();
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.py_name));
							$ (self.target).find ("input[type='color']").bind ('change', self.change);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.SelectColor = SelectColor;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
