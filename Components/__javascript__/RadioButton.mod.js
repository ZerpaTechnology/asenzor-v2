	__nest__ (
		__all__,
		'RadioButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'RadioButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var RadioButton = __class__ ('RadioButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "<input type='radio'><span>{}</span>";
							self.hermanos = list ([]);
						});},
						get activar () {return __get__ (this, function (self) {
							$ (self.target).find ('>input').prop ('checked', true);
							var __iterable0__ = enumerate (self.hermanos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.desactivar ();
							}
						});},
						get desactivar () {return __get__ (this, function (self) {
							$ (self.target).find ('>input').prop ('checked', false);
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.RadioButton = RadioButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
