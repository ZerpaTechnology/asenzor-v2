	__nest__ (
		__all__,
		'SidebarCustomize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SidebarCustomize';
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
					var Input = __init__ (__world__.Input).Input;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var FooterCustomize = __init__ (__world__.FooterCustomize).FooterCustomize;
					var settings = nuclear.Settings ();
					var SidebarCustomize = __class__ ('SidebarCustomize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t\t<div class='header-top'>\n\t\t\t\t<span class='close'> X </span><button name='save'>{}</button>\n\t\t\t</div>\n\t\t\t<div class='content'>\n\t\t\t</div>\n\t\t\t<div class='footer-bottom'>\n\t\t\t\t\n\t\t\t\t<span class='ocultar'> \n\t\t\t\t\t<span class='icon'></span>\n\t\t\t\t\t<span class='text'>{}</span>\n\t\t\t\t</span>\n\t\t\t\t<div class='responsive'>\n\t\t\t\t\t<span class='desktop'></span>\n\t\t\t\t\t<span class='tablet'></span>\n\t\t\t\t\t<span class='phone'></span>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n\t\t";
							self.content = (function __lambda__ (self) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								return self.target.find ('>.content');
							});
							self.btn_save = 'Guardar';
							self.btn_desing = 'Ocultar';
							self.btn_desktop = config.base_url + 'static/imgs/iconos/desktop.png';
							self.btn_tablet = config.base_url + 'static/imgs/iconos/tablet.png';
							self.btn_phone = config.base_url + 'static/imgs/iconos/smartphone.png';
						});},
						get py_update () {return __get__ (this, function (self) {
							self._update = true;
							self.format = list ([self.btn_save, self.btn_desing]);
							self.__update__ ();
							self.target.find ('>.footer-bottom').find ('>.responsive').find ('>.desktop').css ('background-image', "url('{}')".format (self.btn_desktop));
							self.target.find ('>.footer-bottom').find ('>.responsive').find ('>.tablet').css ('background-image', "url('{}')".format (self.btn_tablet));
							self.target.find ('>.footer-bottom').find ('>.responsive').find ('>.phone').css ('background-image', "url('{}')".format (self.btn_phone));
							var screens1 = BasicTabs ('', 10);
							screens1.tabWidth = 280;
							var screens2 = BasicTabs ('', 10);
							screens2.tabWidth = 280;
							var slider = BasicSlider ();
							slider.tabWidth = 280;
							self.add (slider);
							slider.appendToTab (1, screens1);
							slider.appendToTab (2, screens2);
							var w = HeaderCustomizeMain (settings.app);
							slider.appendToTab (0, w);
							var w = BandaTema ();
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Identidad del sitio');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 0;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Colores');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 1;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Cabecera multimedia');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 2;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Menús');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 3;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Widgets');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 4;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Portada estatica');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 5;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Themes Options');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 6;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('CSS adicional');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 7;
							slider.appendToTab (0, w);
							var w = Identidad_del_sitio ('Identidad del sitio');
							w.Media = self.Media;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (0, w);
							var w = Colores ('Colores');
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (1, w);
							var w = CabeceraMultimedia ('Cabecera multimedia');
							w.Media = self.Media;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (2, w);
							var w = Menus ('Menús');
							w.screen = screens2;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (3, w);
							var w = Widgets ('Widgets');
							w.screen = screens2;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (4, w);
							var w = PortadaEstatica ('Portada estática');
							w.Media = self.Media;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (5, w);
							var w = ThemesOptions ('Themes Options');
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (6, w);
							var w = HeaderCustomize ('CSS Adicional');
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (7, w);
							var w = Textarea ();
							w.value = '\n\t\t/*\n\t\tPuedes añadir tu propio CSS aquí.\n\t\t\n\t\tHaz clic en el icono de ayuda de arriba para averiguar más.\n\t\t*/\n\t\t';
							screens1.appendToTab (7, w);
							w.target.find ('textarea').css ('height', '90vh');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'BandaTema' +
						'BasicSlider' +
						'BasicTabs' +
						'ButtonInput' +
						'ButtonSettings' +
						'EnlaceButton' +
						'FileUpload' +
						'FooterCustomize' +
						'HeaderCustomize' +
						'HeaderCustomizeMain' +
						'Input' +
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
						__all__.BandaTema = BandaTema;
						__all__.BasicSlider = BasicSlider;
						__all__.BasicTabs = BasicTabs;
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
						__all__.MediaButton = MediaButton;
						__all__.Menus = Menus;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.Select = Select;
						__all__.SidebarCustomize = SidebarCustomize;
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
