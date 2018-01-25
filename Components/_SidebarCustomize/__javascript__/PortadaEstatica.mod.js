	__nest__ (
		__all__,
		'_SidebarCustomize.PortadaEstatica', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.PortadaEstatica';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var RadioButtonList = __init__ (__world__.RadioButtonList).RadioButtonList;
					var Select = __init__ (__world__.Select).Select;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var PortadaEstatica = __class__ ('PortadaEstatica', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = self.__doc__;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							w.descripcion = '\n\t\tTu tema permite una página estatica como\n\t\tportada\n\t\t';
							self.add (w);
							var w = RadioButtonList ('Pagina frontal muestra');
							self.add (w);
							w.addOptions (list (['Tus ultimas entradas', 'Una pagina estatica']), 1);
							var w = Select ('Portada');
							w.opciones = list (['Pagina de ejemplo', 'Inicio', 'Acerca de', 'Contacto', 'Blog']);
							self.add (w);
							var w = EnlaceButton ('+Añadir nueva pagina');
							self.add (w);
							var w = Select ('Página de entradaa');
							w.opciones = list (['Pagina de ejemplo', 'Inicio', 'Acerca de', 'Contacto', 'Blog']);
							self.add (w);
							var w = EnlaceButton ('+Añadir nueva pagina');
							self.add (w);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'EnlaceButton' +
						'HeaderCustomize' +
						'RadioButtonList' +
						'Select' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButton = EnlaceButton;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.RadioButtonList = RadioButtonList;
						__all__.Select = Select;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
