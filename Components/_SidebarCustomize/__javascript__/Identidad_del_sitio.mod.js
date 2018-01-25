	__nest__ (
		__all__,
		'_SidebarCustomize.Identidad_del_sitio', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Identidad_del_sitio';
					var Widget = __init__ (__world__.Widget).Widget;
					var Input = __init__ (__world__.Input).Input;
					var MediaManager = __init__ (__world__.MediaManager).MediaManager;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var Identidad_del_sitio = __class__ ('Identidad_del_sitio', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = MediaManager ('Logo');
							w.btn2 = 'Elegir logo';
							w.btn1 = 'Eliminar logo';
							w.Media = self.Media;
							w.placeholder = 'No se a elegido un logo';
							self.add (w);
							var w = Input ('Titulo del sitio');
							self.add (w);
							var w = Input ('Descripción corta');
							self.add (w);
							var w = CheckBox ('Muestra el título y descripción del sitio');
							self.add (w);
							var w = MediaManager ('Icono del sitio');
							w.descripcion = '\n\t\tEl icono del sitio lo usa el navegador \n\t\tcomo icono de la aplicación para tu sitio. \n\t\tLos iconos deben ser cuadrados y al menos de 512 píxeles de ancho y alto.\n\t\t';
							w.placeholder = 'No se a elegido un logo';
							w.Media = self.Media;
							self.add (w);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'CheckBox' +
						'HeaderCustomize' +
						'Input' +
						'MediaManager' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Identidad_del_sitio = Identidad_del_sitio;
						__all__.Input = Input;
						__all__.MediaManager = MediaManager;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
