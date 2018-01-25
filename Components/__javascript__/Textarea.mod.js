	__nest__ (
		__all__,
		'Textarea', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Textarea';
					var Widget = __init__ (__world__.Widget).Widget;
					var Textarea = __class__ ('Textarea', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self.descripcion = '';
							self._html = "<b class='titulo'>{}</b><p class='descripcion'>{}</p><textarea></textarea><p class='postdescripcion'></p>";
							self.postdescripcion;
							$ (self.target).css (dict ({'display': 'inline-block'}));
							self.value = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion));
							if (self.value != null) {
								$ (self.target).find ('>textarea').val (str (self.value));
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Textarea = Textarea;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
