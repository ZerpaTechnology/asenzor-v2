	__nest__ (
		__all__,
		'MediaButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'MediaButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var MediaButton = __class__ ('MediaButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, Media) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Subir archivo';
							};
							if (typeof Media == 'undefined' || (Media != null && Media .hasOwnProperty ("__kwargtrans__"))) {;
								var Media = null;
							};
							Widget.__init__ (self, titulo);
							self._html = '<button>{}</button>';
							self.Media = Media;
							self._titulo = self.titulo;
						});},
						get open () {return __get__ (this, function (self) {
							self.Media.updateTitulo (self._titulo);
							self.Media.open ();
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							$ (self.target).find ('button').bind ('click', self.open);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.MediaButton = MediaButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
