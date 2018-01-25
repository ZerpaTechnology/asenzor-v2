	__nest__ (
		__all__,
		'_SidebarCustomize.Menus', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Menus';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var ButtonInput = __init__ (__world__.ButtonInput).ButtonInput;
					var Select = __init__ (__world__.Select).Select;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var Input = __init__ (__world__.Input).Input;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var CheckBoxList = __init__ (__world__.CheckBoxList).CheckBoxList;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var Menus = __class__ ('Menus', [Widget], {
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
							var w = ButtonSettings ('Ubicaciones de menús');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 0;
							w._siguiente = 2;
							self.add (w);
							self.addSeparador ();
							var w = ButtonSettings ('Menús de enlaces de Redes Sociales');
							w.descripcion = '(Actualmente fijado en: Menú de enlaces de Redes Sociales)';
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 1;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonSettings ('Top Menú');
							w.descripcion = '(Actualmente fijado en: Top Menú)';
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 2;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonInput ('Añadir al menu');
							self.add (w);
							var w = HeaderCustomize ('Ubicaciones de menús');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 3;
							self.descripcion = '\n\t\tTu tema soporta 2 menús. Elige qué menú debería aparecer en cada lugar.\n\n\t\tTambién puedes poner menús en los widgets con el widget “Menú personalizado”\n\t\t';
							self.screen.appendToTab (0, w);
							var w = Select ('Top Menu');
							w.opciones = list (['--Eligir--', 'Menu de enlaces a redes sociales', 'Top menu']);
							self.screen.appendToTab (0, w);
							var e = EnlaceButton ('Editar menu');
							self.screen.appendToTab (0, e);
							var w = Select ('Top Menu');
							w.opciones = list (['--Eligir--', 'Menu de enlaces a redes sociales', 'Top menu']);
							self.screen.appendToTab (0, w);
							var e = EnlaceButton ('Editar menu');
							self.screen.appendToTab (0, e);
							self.screen.tabs [0].find ('>div:nth-child(n+2)').css (dict ({'padding-left': '20px', 'padding-right': '20px'}));
							var w = HeaderCustomize ('Menús de enlaces de Redes Sociales');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 3;
							self.screen.appendToTab (1, w);
							var w = Input ();
							w.value = 'Menús de enlaces de Redes Sociales';
							self.screen.appendToTab (1, w);
							var a = Acordion ('');
							var t = TabAcordion ('Yelp');
							var w = Input ('URL');
							w.value = 'https://www.yelp.com';
							t.add (w);
							var w = Input ('Etiqueta de navegación');
							w.value = 'Yelp';
							t.add (w);
							var w = CheckBox ('Abrir enlace en una nueva pestaña');
							t.add (w);
							var w = Input ('Atributos del titulo');
							t.add (w);
							var w = Input ('Relacion con el enlace (XFN)');
							t.add (w);
							var w = Textarea ('Descripción');
							w.postdescripcion = 'La descripción se mostrará en los menús si el tema actual lo soporta.';
							t.add (w);
							var w = EnlaceButton ('Eliminar');
							t.add (w);
							w.color = 'red';
							a.addTab (t);
							var t2 = t.clone ();
							t2.titulo = 'Facebook';
							t2.children [0].value = 'https://facebook.com';
							t2.reload ();
							a.addTab (t2);
							var t3 = t.clone ();
							t3.titulo = 'Twitter';
							t3.children [0].value = 'https://Twitter.com';
							t3.reload ();
							a.addTab (t3);
							var t4 = t.clone ();
							t4.titulo = 'Instagram';
							t4.children [0].value = 'https://Instagram.com';
							a.addTab (t4);
							var t5 = t.clone ();
							t5.titulo = 'Correo electronico';
							t3.children [0].value = 'jzerpa.occoa@gmail.com';
							a.addTab (t5);
							self.screen.appendToTab (1, a);
							var check = CheckBoxList ('Mostrar ubicación');
							check.value = list ([list (['Top Menu', false, '(Actual: Top Menu)']), list (['Menu de enlaces de Redes Sociales', false, '(Actual: Menu de enlaces de Redes Sociales)'])]);
							self.screen.appendToTab (1, check);
							var check2 = CheckBoxList ('Opciones de menú');
							check2.value = list ([list (['Agregar automaticamente nuevas paginas de nivel superior a este menu', false])]);
							self.screen.appendToTab (1, check2);
							self.screen.tabs [1].find ('>div:nth-child(n+2)').css (dict ({'padding-left': '20px', 'padding-right': '20px'}));
							var w = HeaderCustomize ('Top Menú');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 3;
							self.screen.appendToTab (2, w);
							var w = Input ();
							w.value = 'Top Menu';
							self.screen.appendToTab (2, w);
							var a = Acordion ();
							var t = t.clone ();
							t.titulo = 'Inicio';
							a.addTab (t);
							var t = t.clone ();
							t.titulo = 'Acerca de';
							t.descripcion = 'Pagina';
							a.addTab (t);
							var t = t.clone ();
							t.titulo = 'Blog';
							t.descripcion = 'Pagina';
							a.addTab (t);
							var t = t.clone ();
							t.titulo = 'Contacto';
							t.descripcion = 'Pagina';
							a.addTab (t);
							self.screen.appendToTab (2, a);
							var check = check.clone ();
							self.screen.appendToTab (2, check);
							var check2 = check2.clone ();
							self.screen.appendToTab (2, check2.clone ());
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'ButtonInput' +
						'ButtonSettings' +
						'CheckBox' +
						'CheckBoxList' +
						'EnlaceButton' +
						'HeaderCustomize' +
						'Input' +
						'Select' +
						'TabAcordion' +
						'Textarea' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.ButtonInput = ButtonInput;
						__all__.ButtonSettings = ButtonSettings;
						__all__.CheckBox = CheckBox;
						__all__.CheckBoxList = CheckBoxList;
						__all__.EnlaceButton = EnlaceButton;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Input = Input;
						__all__.Menus = Menus;
						__all__.Select = Select;
						__all__.TabAcordion = TabAcordion;
						__all__.Textarea = Textarea;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
