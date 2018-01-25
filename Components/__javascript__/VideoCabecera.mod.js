	__nest__ (
		__all__,
		'VideoCabecera', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'VideoCabecera';
					var Button = __init__ (__world__.Button).Button;
					var VideoCabecera = __class__ ('VideoCabecera', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Vídeo de cabecera';
							};
							self.titulo = titulo;
							self.add (Button ('Seleccionar video'));
						});}
					});
					__pragma__ ('<use>' +
						'Button' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Button = Button;
						__all__.VideoCabecera = VideoCabecera;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
