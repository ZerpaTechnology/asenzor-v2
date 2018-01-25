	__nest__ (
		__all__,
		'ButtonInput', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ButtonInput';
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonInput = __class__ ('ButtonInput', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<button>{}</button>\n\t\t<div class='content'>\n\t\t<input name='{}' placeholder='{}'>\n\t\t<button>{}</button>\n\t\t</div>\n\t\t";
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.placeholder = '';
							self.open = false;
							self.submit = null;
							self.height = 0;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>.content').animate (dict ({'height': '0px', 'padding': '0px'}), 1000, (function __lambda__ () {
								return $ (self.target).find ('>.content').css (dict ({'height': '0px', 'padding': '0px'}));
							}));
							self.open = false;
						});},
						get abrir () {return __get__ (this, function (self) {
							var abrir = function () {
								$ (self.target).find ('>.content').css (dict ({'height': 'auto', 'padding': '5px'}));
							};
							$ (self.target).find ('>.content').animate (dict ({'height': str (self.height) + 'px', 'padding': '5px'}), 1000, abrir);
							self.open = true;
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (submit != null) {
								self.submit (self);
							}
							self.cerrar ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								self.submit (self);
								self.cerrar ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.py_name, self.placeholder, self.btn));
							var recargar = function () {
								self.height = $ (self.target).find ('>.content').outerHeight ();
								$ (self.target).find ('>.content').css (dict ({'height': '0px'}));
							};
							setTimeout (recargar, 1e-05);
							$ (self.target).find ('>button').bind ('click', self.click);
							$ (self.target).find ('>.content').find ('>button').bind ('click', self.send);
							$ (self.target).find ('>.content').find ('>button').bind ('keyup', self.enter);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonInput = ButtonInput;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
