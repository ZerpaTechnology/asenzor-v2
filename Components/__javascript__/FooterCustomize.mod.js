	__nest__ (
		__all__,
		'FooterCustomize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'FooterCustomize';
					var Widget = __init__ (__world__.Widget).Widget;
					var FooterCustomize = __class__ ('FooterCustomize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t<span class='ocultar'> \n\t\t<span class='icon'></span>\n\t\t<span class='text'>{}</span>\n\t\t</span>\n\t\t<div class='responsize'>\n\t\t<span class='desktop'></span>\n\t\t<span class='tablet'></span>\n\t\t<span class='phone'></span>\n\t\t</div>\n\t\t";
							self._atras = atras;
							self.status = 'desktop';
						});},
						get atras () {return __get__ (this, function (self, evt) {
							self.slider.showTab (self._atras);
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							$ (self.target).find ('.atras').bind ('click', self.atras);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.FooterCustomize = FooterCustomize;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
