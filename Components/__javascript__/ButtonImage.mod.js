	__nest__ (
		__all__,
		'ButtonImage', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var random = {};
					var __name__ = 'ButtonImage';
					var Widget = __init__ (__world__.Widget).Widget;
					__nest__ (random, '', __init__ (__world__.random));
					var ButtonImage = __class__ ('ButtonImage', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = "<button ><img><b class='titulo'></b></button>";
							self.__button = self.target.find ('>button');
							self.__img = self.__button.find ('img');
							self.__titulo = self.__button.find ('>.titulo');
							self.paleta = list (['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#16a085', '#27ae60', '#2980b9', '#8e44ad', '#2c3e50', '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1', '#95a5a6', '#f39c12', '#d35400', '#c0392b', '#bdc3c7', '#7f8c8d']);
							self._randomBg = false;
							self.height = 90;
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.__button.find ('>.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get img () {return __get__ (this, function (self, src) {
							self.__button.find ('img').attr ('src', src);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							if (self._randomBg) {
								self.__button.css ('background-color', self.paleta [random.randint (0, len (self.paleta))]);
							}
							self.titulo (self._titulo);
							self.__button.css ('height', self.height);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
						'random' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonImage = ButtonImage;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
