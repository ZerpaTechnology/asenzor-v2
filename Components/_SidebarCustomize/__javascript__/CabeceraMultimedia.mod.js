	__nest__ (
		__all__,
		'_SidebarCustomize.CabeceraMultimedia', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.CabeceraMultimedia';
					var Widget = __init__ (__world__.Widget).Widget;
					var VideoManager = __init__ (__world__.VideoManager).VideoManager;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var Input = __init__ (__world__.Input).Input;
					var Imagen_de_cabecera = __init__ (__world__.Imagen_de_cabecera).Imagen_de_cabecera;
					var CabeceraMultimedia = __class__ ('CabeceraMultimedia', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = 'Si añades un video, la imagen se utilizara como alternativa\n\t\tmientras que el video carga.\n\t\t';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.descripcion = self.descripcion;
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = VideoManager ('Video de cabecera');
							self.add (w);
							var w = Input ();
							w.descripcion = 'O escribe una URL de YouTube:';
							self.add (w);
							var w = Imagen_de_cabecera ('Imagen de cabecera');
							w.Media = self.Media;
							self.add (w);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomize' +
						'Imagen_de_cabecera' +
						'Input' +
						'VideoManager' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CabeceraMultimedia = CabeceraMultimedia;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Imagen_de_cabecera = Imagen_de_cabecera;
						__all__.Input = Input;
						__all__.VideoManager = VideoManager;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
