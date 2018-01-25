	__nest__ (
		__all__,
		'TabAcordion', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'TabAcordion';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var TabAcordion = __class__ ('TabAcordion', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, descripcion) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'tab';
							};
							if (typeof descripcion == 'undefined' || (descripcion != null && descripcion .hasOwnProperty ("__kwargtrans__"))) {;
								var descripcion = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span>\n\t\t<b class='titulo'>{}</b>\n\t\t<span>\n\t\t<span class='descripcion'>{}</span>\n\t\t<span class='switch'>\n\t\t</span>\n\t\t</span>\n\t\t\n\t\t</span>\n\t\t<div class='content'>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = descripcion;
							self.btn = config.base_url + 'static/imgs/iconos/arrow-4.png';
							self._btn = config.base_url + 'static/imgs/iconos/arrow-3.png';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = dict ({});
							self.open = false;
							self.height = 0;
							self.activador = null;
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.content');
							});
						});},
						get updateTitulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('>span').find ('>.titulo').text (titulo);
							self.titulo = titulo;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							self.children.append (target);
							if (self._update) {
								$ (self.target).find ('>.content').append (target.target);
								var recargar = function () {
									self.height = 0;
									var __iterable0__ = $ (self.target).find ('>.content').children ();
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										self.height += $ (elem).outerHeight ();
									}
								};
								setTimeout (recargar, 1e-06);
							}
						});},
						get addList () {return __get__ (this, function (self, lista) {
							var __iterable0__ = lista;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.add (elem);
							}
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>.content').animate (dict ({'height': '0px'}), 1000, (function __lambda__ () {
								return $ (self.target).find ('>.content').css (dict ({'height': '0px', 'padding': '0px'}));
							}));
							$ (self.target).find ('.switch').css ('background-image', ("url('" + self.btn) + "')");
							self.open = false;
						});},
						get abrir () {return __get__ (this, function (self) {
							var abrir = function () {
								$ (self.target).find ('>.content').css (dict ({'height': 'auto', 'padding': '5px'}));
							};
							$ (self.target).find ('>.content').animate (dict ({'height': str (self.height) + 'px'}), 1000, abrir);
							$ (self.target).find ('.switch').css ('background-image', ("url('" + self._btn) + "')");
							self.open = true;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
							if (self.activador != null) {
								self.activador (self);
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.descripcion]);
							self.__update__ ();
							if (self.open) {
								$ (self.target).find ('>.content').css ('height', 'auto');
								$ (self.target).find ('.switch').css ('background-image', ("url('" + self._btn) + "')");
							}
							else {
								$ (self.target).find ('>.content').css ('height', '0px');
								$ (self.target).find ('.switch').css ('background-image', ("url('" + self.btn) + "')");
							}
							$ (self.target).find ('>span').bind ('click', self.click);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TabAcordion = TabAcordion;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
