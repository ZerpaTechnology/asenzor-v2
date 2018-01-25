	__nest__ (
		__all__,
		'_SidebarCustomize.Colores', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Colores';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var CheckBoxList = __init__ (__world__.CheckBoxList).CheckBoxList;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var SelectColor = __init__ (__world__.SelectColor).SelectColor;
					var Colores = __class__ ('Colores', [Widget], {
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
							var w = CheckBoxList ('Color Scheme');
							var _w = CheckBox ('Light');
							w.add (_w);
							var _w = CheckBox ('Negro');
							w.add (_w);
							var _w = CheckBox ('Custom');
							w.add (_w);
							var color = SelectColor ();
							self.add (w);
							var mostrar = function () {
								color.show ();
							};
							var ocultar = function () {
								color.hidden ();
							};
							_w.activador = mostrar;
							_w.desactivador = ocultar;
							color.hidden ();
							self.add (color);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'CheckBox' +
						'CheckBoxList' +
						'HeaderCustomize' +
						'SelectColor' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.CheckBoxList = CheckBoxList;
						__all__.Colores = Colores;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.SelectColor = SelectColor;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
