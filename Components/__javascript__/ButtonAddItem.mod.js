	__nest__ (
		__all__,
		'ButtonAddItem', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ButtonAddItem';
					var Component = nuclear.Component;
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonAddItem = __class__ ('ButtonAddItem', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<button>\n\t\t<span class='left'>\n\t\t<span class='icon'></span>\n\t\t<b class='titulo'>{}</b>\n\t\t</span>\n\t\t<span class='right'>{}</span>\n\t\t</button>\n\t\t";
							self.descripcion = '';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.formato = list ([self.titulo, self.descripcion]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonAddItem = ButtonAddItem;
						__all__.Component = Component;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
