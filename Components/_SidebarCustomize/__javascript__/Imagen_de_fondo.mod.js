	__nest__ (
		__all__,
		'_SidebarCustomize.Imagen_de_fondo', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Imagen_de_fondo';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var Imagen_de_fondo = __class__ ('Imagen_de_fondo', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = self.__doc__;
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomize' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Imagen_de_fondo = Imagen_de_fondo;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
