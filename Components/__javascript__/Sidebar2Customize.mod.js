	__nest__ (
		__all__,
		'Sidebar2Customize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Sidebar2Customize';
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
					var Sidebar2Customize = __class__ ('Sidebar2Customize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							var h = $ ("\n\t\t<div class='header-top'>\n\t\t<span class='close'> X </span><button name='save'>{}</button>\n\t\t</div>".format ('Guardar y Publicar'));
							self.tabs = BasicTabs ('', 10);
							self.add (self.tabs);
							var w = Acordion ();
							self.tabs.appendToTab (0, w);
							w.target.css (dict ({'padding': '0px'}));
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
						__all__.Sidebar2Customize = Sidebar2Customize;
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
