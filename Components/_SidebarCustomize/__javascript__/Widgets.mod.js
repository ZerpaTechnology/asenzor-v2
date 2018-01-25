	__nest__ (
		__all__,
		'_SidebarCustomize.Widgets', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Widgets';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Input = __init__ (__world__.Input).Input;
					var TyniMCE = __init__ (__world__.TyniMCE).TyniMCE;
					var Widgets = __class__ ('Widgets', [Widget], {
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
							self.add (w);
							var w = ButtonSettings ('Blog Sidebar');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 3;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonSettings ('Footer 1');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 4;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonSettings ('Footer 2');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 5;
							w._siguiente = 2;
							self.add (w);
							var w = HeaderCustomize ('Blog Sidebar');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 6;
							w.descripcion = '\n\t\tAdd widgets here to appear in your sidebar on\n\t\tblog posts and archive pages.\n\t\t';
							self.screen.appendToTab (3, w);
							var a = Acordion ();
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Encuentranos';
							var w = Input ('Titulo');
							w.value = 'Encuentranos';
							var w = TyniMCE ();
							t.add (w);
							a.addTab (t);
							var t = TabAcordion ('Buscar:');
							t.descripcion = 'Busqueda';
							var w = Input ('Titulo');
							w.value = 'Busqueda';
							a.addTab (w);
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Acerca del sitio';
							var w = Input ('Titulo');
							w.value = 'Acerca del sitio';
							var w = TyniMCE ();
							w.value = '\n\t\tEste puede ser un buen lugar para presentarte y presentar tu sitio o incluir algunos créditos.\n\t\t';
							self.screen.appendToTab (3, a);
							var w = HeaderCustomize ('Footer 1');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 7;
							self.screen.appendToTab (4, w);
							var a = Acordion ();
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Encuentranos';
							var w = Input ('Titulo');
							w.value = 'Encuentranos';
							t.add (w);
							var w = TyniMCE ();
							t.add (w);
							a.addTab (t);
							self.screen.appendToTab (4, a);
							var w = HeaderCustomize ('Footer 2');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 8;
							self.screen.appendToTab (5, w);
							var a = Acordion ();
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Acerca del sitio';
							var w = Input ('Titulo');
							w.value = 'Acerca del sitio';
							t.add (w);
							var w = TyniMCE ();
							w.value = '\n\t\tEste puede ser un buen lugar para presentarte y presentar tu sitio o incluir algunos créditos.\n\t\t';
							t.add (w);
							a.addTab (t);
							var t = TabAcordion ('Buscar:');
							t.descripcion = 'Busqueda';
							var w = Input ('Titulo');
							w.value = 'Busqueda';
							t.add (w);
							a.addTab (t);
							self.screen.appendToTab (5, a);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'ButtonSettings' +
						'HeaderCustomize' +
						'Input' +
						'TabAcordion' +
						'TyniMCE' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.ButtonSettings = ButtonSettings;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Input = Input;
						__all__.TabAcordion = TabAcordion;
						__all__.TyniMCE = TyniMCE;
						__all__.Widget = Widget;
						__all__.Widgets = Widgets;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
