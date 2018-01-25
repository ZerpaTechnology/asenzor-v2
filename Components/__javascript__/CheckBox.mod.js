	__nest__ (
		__all__,
		'CheckBox', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'CheckBox';
					var Widget = __init__ (__world__.Widget).Widget;
					var CheckBox = __class__ ('CheckBox', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "<input type='checkbox' name='{}'><span>{}</span>";
							self.py_name = '';
							self.hermanos = list ([]);
							self.activador = null;
							self.desactivador = null;
							self.value = false;
						});},
						get desactivarHermanos () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem != self) {
									elem.desactivar ();
								}
							}
						});},
						get click () {return __get__ (this, function (self) {
							if ($ (self.target).find ("input[type='checkbox']").prop ('checked')) {
								self.activar ();
							}
							else {
								self.desactivar ();
							}
						});},
						get desactivar () {return __get__ (this, function (self, desactivador) {
							if (typeof desactivador == 'undefined' || (desactivador != null && desactivador .hasOwnProperty ("__kwargtrans__"))) {;
								var desactivador = null;
							};
							$ (self.target).find ("input[type='checkbox']").prop ('checked', false);
							if (desactivador != null) {
								self.desactivador = desactivador;
								desactivador ();
							}
							else if (self.desactivador != null) {
								self.desactivador ();
							}
						});},
						get activar () {return __get__ (this, function (self, activador) {
							if (typeof activador == 'undefined' || (activador != null && activador .hasOwnProperty ("__kwargtrans__"))) {;
								var activador = null;
							};
							$ (self.target).find ("input[type='checkbox']").prop ('checked', true);
							if (activador != null) {
								self.activador = activador;
								activador ();
							}
							else if (self.activador != null) {
								self.activador ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.py_name, self.titulo]);
							self.__update__ ();
							$ (self.target).find ("input[type='checkbox']").prop ('checked', self.value);
							$ (self.target).find ("input[type='checkbox']").bind ('click', self.click);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
