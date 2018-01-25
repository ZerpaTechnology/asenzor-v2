	__nest__ (
		__all__,
		'EnlaceButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'EnlaceButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var EnlaceButton = __class__ ('EnlaceButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<button>{}</button>\n\t\t';
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.open = false;
							self.submit = null;
							self.color = 'blue';
						});},
						get click () {return __get__ (this, function (self) {
							if (self.activador != null) {
								self.activador (self);
							}
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (self.submit != null) {
								self.submit (self);
							}
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								if (self.submit != null) {
									self.submit (self);
								}
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							self.target.find ('>button').css ('color', self.color);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButton = EnlaceButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
