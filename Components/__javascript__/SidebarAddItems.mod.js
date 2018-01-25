	__nest__ (
		__all__,
		'SidebarAddItems', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SidebarAddItems';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var BandaTema = __init__ (__world__.BandaTema).BandaTema;
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicSlider = __init__ (__world__.BasicSlider).BasicSlider;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var MediaButton = __init__ (__world__.MediaButton).MediaButton;
					var Identidad_del_sitio = __init__ (__world__._SidebarCustomize.Identidad_del_sitio).Identidad_del_sitio;
					var CabeceraMultimedia = __init__ (__world__._SidebarCustomize.CabeceraMultimedia).CabeceraMultimedia;
					var Menus = __init__ (__world__._SidebarCustomize.Menus).Menus;
					var Colores = __init__ (__world__._SidebarCustomize.Colores).Colores;
					var Widgets = __init__ (__world__._SidebarCustomize.Widgets).Widgets;
					var Imagen_de_fondo = __init__ (__world__._SidebarCustomize.Imagen_de_fondo).Imagen_de_fondo;
					var PortadaEstatica = __init__ (__world__._SidebarCustomize.PortadaEstatica).PortadaEstatica;
					var ThemesOptions = __init__ (__world__._SidebarCustomize.ThemesOptions).ThemesOptions;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var Select = __init__ (__world__.Select).Select;
					var ButtonInput = __init__ (__world__.ButtonInput).ButtonInput;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var InputSearch = __init__ (__world__.InputSearch).InputSearch;
					var Input = __init__ (__world__.Input).Input;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var FooterCustomize = __init__ (__world__.FooterCustomize).FooterCustomize;
					var BoxScroll = __init__ (__world__.BoxScroll).BoxScroll;
					var AddItem = __init__ (__world__.AddItem).AddItem;
					var Button = __init__ (__world__.Button).Button;
					var ButtonAddItem = __init__ (__world__.ButtonAddItem).ButtonAddItem;
					var InputAndButton = __init__ (__world__.InputAndButton).InputAndButton;
					var settings = nuclear.Settings ();
					var SidebarAddItems = __class__ ('SidebarAddItems', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = InputSearch ();
							self.add (w);
							w.target.css ('height', '8vh');
							var b = BoxScroll ();
							var a = Acordion ();
							var t = TabAcordion ('Enlaces personalizados');
							var w = Input ('URL');
							w.value = 'http://';
							t.add (w);
							var w = Input ('Texto del enlace');
							t.add (w);
							var w = Button ('Añadir al menu');
							t.add (w);
							a.addTab (t);
							var t = TabAcordion ('Páginas');
							var _b = BoxScroll ();
							var _w = ButtonAddItem ('Inicio');
							_w.descripcion = 'Enlace personalizado';
							_b.add (_w);
							var _w = ButtonAddItem ('Inicio');
							_w.descripcion = 'Página';
							_b.add (_w);
							t.add (_b);
							var _w = InputAndButton ('Añadir');
							_w.placeholder = 'Añadir nueva pagina';
							t.add (_w);
							a.addTab (t);
							var t = TabAcordion ('Entradas');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							var t = TabAcordion ('Categorias');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							var t = TabAcordion ('Etiquetas');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							var t = TabAcordion ('Formato');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							b.add (a);
							self.add (b);
							b.target.css ('height', '92vh');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'AddItem' +
						'BandaTema' +
						'BasicSlider' +
						'BasicTabs' +
						'BoxScroll' +
						'Button' +
						'ButtonAddItem' +
						'ButtonInput' +
						'ButtonSettings' +
						'EnlaceButton' +
						'FileUpload' +
						'FooterCustomize' +
						'HeaderCustomize' +
						'HeaderCustomizeMain' +
						'Input' +
						'InputAndButton' +
						'InputSearch' +
						'MediaButton' +
						'Select' +
						'TabAcordion' +
						'Textarea' +
						'Widget' +
						'_SidebarCustomize.CabeceraMultimedia' +
						'_SidebarCustomize.Colores' +
						'_SidebarCustomize.Identidad_del_sitio' +
						'_SidebarCustomize.Imagen_de_fondo' +
						'_SidebarCustomize.Menus' +
						'_SidebarCustomize.PortadaEstatica' +
						'_SidebarCustomize.ThemesOptions' +
						'_SidebarCustomize.Widgets' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.AddItem = AddItem;
						__all__.BandaTema = BandaTema;
						__all__.BasicSlider = BasicSlider;
						__all__.BasicTabs = BasicTabs;
						__all__.BoxScroll = BoxScroll;
						__all__.Button = Button;
						__all__.ButtonAddItem = ButtonAddItem;
						__all__.ButtonInput = ButtonInput;
						__all__.ButtonSettings = ButtonSettings;
						__all__.CabeceraMultimedia = CabeceraMultimedia;
						__all__.Colores = Colores;
						__all__.EnlaceButton = EnlaceButton;
						__all__.FileUpload = FileUpload;
						__all__.FooterCustomize = FooterCustomize;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Identidad_del_sitio = Identidad_del_sitio;
						__all__.Imagen_de_fondo = Imagen_de_fondo;
						__all__.Input = Input;
						__all__.InputAndButton = InputAndButton;
						__all__.InputSearch = InputSearch;
						__all__.MediaButton = MediaButton;
						__all__.Menus = Menus;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.Select = Select;
						__all__.SidebarAddItems = SidebarAddItems;
						__all__.TabAcordion = TabAcordion;
						__all__.Textarea = Textarea;
						__all__.ThemesOptions = ThemesOptions;
						__all__.Widget = Widget;
						__all__.Widgets = Widgets;
						__all__.__name__ = __name__;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
