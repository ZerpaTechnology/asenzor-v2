	__nest__ (
		__all__,
		'ImagenRandom', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ImagenRandom';
					var Widget = __init__ (__world__.Widget).Widget;
					var ImagenRandom = __class__ ('ImagenRandom', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Sugerido';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='visor'>\n\t\t<p>{}</p>\n\t\t<img src='{}' class='hidden'>\n\t\t</div>\n\t\t<div class='btns'>\n\t\t<button class='btn'><span></span>{}</button>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.btn = 'Imagen sugeriada al azar';
							self.btn2 = 'Cambiar image';
							self.btn1 = 'Eliminar imagen';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = null;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).append (target.target);
						});},
						get updateValue () {return __get__ (this, function (self, valor) {
							self.value = valor;
							if (py_typeof (self.value) == list) {
								self.value = self.value [0];
							}
							$ (self.target).find ('>.visor').find ('img').attr ('src', self.value.url);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});},
						get change () {return __get__ (this, function (self) {
							self.Media.open (self.updateValue);
						});},
						get delete () {return __get__ (this, function (self) {
							self.value = null;
							$ (self.target).find ('>.visor').find ('p').removeClass ('hidden');
							$ (self.target).find ('>.visor').find ('img').attr ('src', '');
							$ (self.target).find ('>.visor').find ('img').addClass ('hidden');
							$ (self.target).find ('>.btns').find ('button').remove ('.btn1');
						});},
						get py_update () {return __get__ (this, function (self) {
							if (self.value != null) {
								self.img = self.value;
							}
							$ (self.target).html (self._html.format (self.titulo, self.descripcion, self.placeholder, self.img, self.btn));
							$ (self.target).find ('.btns').find ('.btn2').bind ('click', self.change);
							if (self.value != null && len ($ (self.target).find ('>.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ImagenRandom = ImagenRandom;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
