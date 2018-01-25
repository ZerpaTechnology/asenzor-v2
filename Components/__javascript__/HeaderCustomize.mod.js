	__nest__ (
		__all__,
		'HeaderCustomize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'HeaderCustomize';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __class__ ('HeaderCustomize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t\t<span class='atras'></span>\n\t\t\t<div class='text'>\n\t\t\t\t<p>{}</p>\n\t\t\t\t<h3>{}</h3>\n\t\t\t</div>\n\t\t</div>\n\t\t<p>{}</p>\n\t\t";
							self.pretitulo = 'Estas personalizando: ';
							self.descripcion = '';
							self._atras = atras;
						});},
						get atras () {return __get__ (this, function (self, evt) {
							self.slider.showTab (self._atras);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.pretitulo, self.titulo, self.descripcion]);
							self.__update__ ();
							$ (self.target).find ('.atras').bind ('click', self.atras);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
