	__nest__ (
		__all__,
		'_SidebarCustomize.ThemesOptions', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.ThemesOptions';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var RadioButtonList = __init__ (__world__.RadioButtonList).RadioButtonList;
					var RadioButton = __init__ (__world__.RadioButton).RadioButton;
					var Select = __init__ (__world__.Select).Select;
					var EnlaceButtonInput = __init__ (__world__.EnlaceButtonInput).EnlaceButtonInput;
					var ThemesOptions = __class__ ('ThemesOptions', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize ('Themes Options');
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var r = RadioButtonList ('Page Layout');
							r.descripcion = '\n\t\tWhen the two-column layout is assigned, \n\t\tthe page title is in one column and \n\t\tcontent is in the other.\n\t\t';
							self.add (r);
							var w = RadioButton ('One Column');
							r.add (w);
							var w = RadioButton ('Two Column');
							r.add (w);
							var w = Select ('From Page Section 1 Content');
							w.descripcion = '\n\t\tSelect pages to feature in each area \n\t\tfrom the dropdowns. Add an image to a \n\t\tsection by setting a featured image in \n\t\tthe page editor. Empty sections will not \n\t\tbe displayed.\n\t\t';
							w.opciones = list (['--Elegir--', 'Pagina de ejemplo', 'Inicio', 'Acerca de', 'Contacto', 'Blog']);
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
							var w = Select ('From Page Section 2 Content');
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
							var w = Select ('From Page Section 3 Content');
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
							var w = Select ('From Page Section 4 Content');
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
						});}
					});
					__pragma__ ('<use>' +
						'EnlaceButtonInput' +
						'HeaderCustomize' +
						'RadioButton' +
						'RadioButtonList' +
						'Select' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButtonInput = EnlaceButtonInput;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.RadioButton = RadioButton;
						__all__.RadioButtonList = RadioButtonList;
						__all__.Select = Select;
						__all__.ThemesOptions = ThemesOptions;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
