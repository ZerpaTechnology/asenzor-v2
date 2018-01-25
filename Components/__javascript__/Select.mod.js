	__nest__ (
		__all__,
		'Select', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Select';
					var Widget = __init__ (__world__.Widget).Widget;
					var Select = __class__ ('Select', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<b>{}</b>\n\t\t<select></select>\n\t\t';
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.open = false;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								$ (self.target).find ('>.content').animate (dict ({'height': '0px'}), 1000);
								self.open = false;
							}
							else {
								$ (self.target).find ('>.content').animate (dict ({'height': 'auto'}), 1000);
								self.open = true;
							}
						});},
						get submit () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							self.activador ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								self.submit ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							var __iterable0__ = self.opciones;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ (self.target).find ('>select').append (('<option>' + elem) + '</option>');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Select = Select;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
