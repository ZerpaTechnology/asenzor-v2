	__nest__ (
		__all__,
		'HorizontalScroll', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'HorizontalScroll';
					var Widget = __init__ (__world__.Widget).Widget;
					var HorizontalScroll = __class__ ('HorizontalScroll', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self.content = self.target.find ('>div');
							self._html = '<div></div>';
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get done () {return __get__ (this, function (self) {
							self.titulo (self._titulo);
							self.__titulo = self.target.find ('>.titulo');
							self.reloadSize ();
						});},
						get reloadSize () {return __get__ (this, function (self) {
							var width = 0;
							var __iterable0__ = self.target [0].children;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								print (elem.outerHTML);
								width += $ (elem).outerWidth ();
							}
							self.target.find ('>div').css ('width', width);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HorizontalScroll = HorizontalScroll;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
