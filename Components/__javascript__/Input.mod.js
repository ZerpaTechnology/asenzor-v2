	__nest__ (
		__all__,
		'Input', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Input';
					var Widget = __init__ (__world__.Widget).Widget;
					var Input = __class__ ('Input', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._descripcion = '';
							self._html = '<b>{}</b><p>{}</p><input>';
							$ (self.target).css (dict ({'display': 'inline-block'}));
							self.value = null;
							self.content = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo, self._descripcion]);
							self.__update__ ();
							if (self.value != null) {
								$ (self.target).find ('>input').val (str (self.value));
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Input = Input;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
