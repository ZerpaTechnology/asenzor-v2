	__nest__ (
		__all__,
		'BTNS', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BTNS';
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonImage = __init__ (__world__.ButtonImage).ButtonImage;
					var BTNS = __class__ ('BTNS', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "<b class='titulo'>{}</b>";
							self.estilos = dict ({});
							self._imagen = 'img.png';
							self._btns = list ([]);
							self._randomBg = false;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							var __iterable0__ = self._btns;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var b = ButtonImage (elem [1]);
								self.children.append (b);
								b._randomBg = self._randomBg;
								b.height = 120;
								b.py_update ();
								b.img (elem [0]);
								b.titulo (elem [1]);
								self.target.append (b.target);
								if (len (elem) == 3) {
									b.target.css (elem [2]);
								}
							}
						});}
					});
					__pragma__ ('<use>' +
						'ButtonImage' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BTNS = BTNS;
						__all__.ButtonImage = ButtonImage;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
