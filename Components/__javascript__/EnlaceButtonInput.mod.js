	__nest__ (
		__all__,
		'EnlaceButtonInput', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'EnlaceButtonInput';
					var Widget = __init__ (__world__.Widget).Widget;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var EnlaceButtonInput = __class__ ('EnlaceButtonInput', [EnlaceButton], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							EnlaceButton.__init__ (self, titulo);
							self._html += "\n\t\t<div class='content'>\n\t\t<input name='{}' placeholder='{}'><button>{}</button>\n\t\t</div>\n\t\t";
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.value = null;
							self.open = false;
							self.activador = null;
							self.submit = null;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
							if (self.activador != null) {
								self.activador (self);
							}
						});},
						get abrir () {return __get__ (this, function (self) {
							$ (self.target).find ('>button').css (dict ({'display': 'none'}));
							$ (self.target).find ('>.content').css (dict ({'display': 'block'}));
							self.open = true;
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>button').css (dict ({'display': 'block'}));
							$ (self.target).find ('>.content').css (dict ({'display': 'none'}));
							self.open = false;
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (self.submit != null) {
								self.submit (self);
							}
							self.cerrar ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								if (self.submit != null) {
									self.submit (self);
								}
								self.cerrar ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.py_name, self.placeholder, self.btn));
							$ (self.target).find ('>button').bind ('click', self.click);
							if (!(self.open)) {
								$ (self.target).find ('>.content').css (dict ({'display': 'none'}));
							}
							$ (self.target).find ('>.content').find ('>button').bind ('click', self.send);
						});}
					});
					__pragma__ ('<use>' +
						'EnlaceButton' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButton = EnlaceButton;
						__all__.EnlaceButtonInput = EnlaceButtonInput;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
