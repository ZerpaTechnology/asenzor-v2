	__nest__ (
		__all__,
		'DetalleImagen', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'DetalleImagen';
					var Widget = __init__ (__world__.Widget).Widget;
					var DetalleImagen = __class__ ('DetalleImagen', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, Media) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Subir archivo';
							};
							if (typeof Media == 'undefined' || (Media != null && Media .hasOwnProperty ("__kwargtrans__"))) {;
								var Media = null;
							};
							Widget.__init__ (self, titulo);
							self._html = "<img src='{}' titulo='{}' leyenda='{}' _alt='{}' ><span class='select'></span>";
							self.Media = Media;
							self._titulo = self.titulo;
							self.url = '';
							self.leyenda = '';
							self._alt = '';
							self.marcado = null;
							self.hermanos = list ([]);
							self.tipo = '';
							self.ultimaModificacion = '';
							self.size = '';
							self.fechaUltimaModificacion = '';
							self.indice = 0;
						});},
						get click () {return __get__ (this, function (self, evt) {
							if (evt.shiftKey) {
								self.marcarHastaActual ();
							}
							else if (evt.ctrlKey) {
								if (self.marcado == null) {
									self.seleccionarMarcados ();
									self.marcar ();
								}
								else {
									self.desmarcar ();
								}
							}
							else if (self.marcado == false || self.marcado == null) {
								self.marcarSolo ();
							}
							else {
								self.desmarcarTodo ();
							}
							self.hayMarcas ();
						});},
						get marcar () {return __get__ (this, function (self) {
							var marcador = $ (self.target).find ('.select');
							self.Media.biblioteca.target.find ('.detalles').find ("[name='titulo']").val (self.titulo);
							self.Media.biblioteca.target.find ('.detalles').find ('.titulo').html ('DETALLES DE ADJUNTOS');
							self.Media.biblioteca.target.find ('.detalles').find ('.info').html ('<br>'.join (list ([self.titulo, self.fechaUltimaModificacion, self.size, self.tipo])));
							self.Media.biblioteca.target.find ('.detalles').find ("[name='url']").val (self.url);
							self.Media.biblioteca.target.find ('.detalles').find ("[name='descripcion']").val (self._alt);
							self.Media.biblioteca.target.find ('.detalles').find ('img').attr ('src', self.url);
							self.Media.biblioteca.target.find ('.detalles').find ('img').removeClass ('hidden');
							self.Media.biblioteca.currents.append (self.url);
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'blue'}));
							marcador.css (dict ({'border': 'solid', 'border-color': 'blue'}));
							self.marcado = true;
						});},
						get marcarSolo () {return __get__ (this, function (self) {
							self.desmarcarHermanos ();
							var marcador = $ (self.target).find ('.select');
							self.Media.biblioteca.target.find ('.detalles').find ("[name='titulo']").val (self.titulo);
							self.Media.biblioteca.target.find ('.detalles').find ('.titulo').html ('DETALLES DE ADJUNTOS');
							self.Media.biblioteca.target.find ('.detalles').find ('.info').html ('<br>'.join (list ([self.titulo, self.fechaUltimaModificacion, self.size, self.tipo])));
							self.Media.biblioteca.target.find ('.detalles').find ("[name='url']").val (self.url);
							self.Media.biblioteca.target.find ('.detalles').find ("[name='descripcion']").val (self._alt);
							self.Media.biblioteca.target.find ('.detalles').find ('img').attr ('src', self.url);
							self.Media.biblioteca.target.find ('.detalles').find ('img').removeClass ('hidden');
							self.Media.biblioteca.current = self.url;
							marcador.css (dict ({'border-color': 'blue'}));
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'blue'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'blue'}));
							self.marcado = true;
						});},
						get actualizarHermanos () {return __get__ (this, function (self, widgets) {
							self.hermanos = widgets;
						});},
						get deseleccionar () {return __get__ (this, function (self) {
							self.marcado = false;
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'transparent', 'box-shadow': '5px rgb(100,100,200)'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'gray'}));
						});},
						get desmarcar () {return __get__ (this, function (self) {
							self.marcado = null;
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'transparent', 'box-shadow': 'none'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'transparent'}));
						});},
						get desmarcarHermanos () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem.target != self.target) {
									elem.desmarcar ();
								}
							}
							self.marcado = null;
							self.hayMarcas ();
						});},
						get desmarcarTodo () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.desmarcar ();
							}
							self.hayMarcas ();
						});},
						get hayMarcas () {return __get__ (this, function (self) {
							var seleccionados = list ([]);
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem.marcado != null) {
									seleccionados.append (elem);
								}
							}
							if (len (seleccionados) == 0) {
								self.Media.noSeleccionados ();
							}
							else {
								self.Media.seleccionados (seleccionados);
							}
						});},
						get refresh () {return __get__ (this, function (self, src) {
							if (typeof src == 'undefined' || (src != null && src .hasOwnProperty ("__kwargtrans__"))) {;
								var src = null;
							};
							if (src == null) {
								var src = $ (self.target).find ('img').attr ('src');
							}
							$ (self.target).find ('img').attr ('src', src);
						});},
						get seleccionar () {return __get__ (this, function (self) {
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'gray', 'box-shadow': 'none'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'gray'}));
							self.marcado = false;
						});},
						get seleccionarMarcados () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem.marcado == true) {
									elem.seleccionar ();
								}
							}
						});},
						get marcarHastaActual () {return __get__ (this, function (self) {
							var desde = null;
							var __iterable0__ = enumerate (self.hermanos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								if (elem.marcado == true && desde == null) {
									var desde = k;
								}
							}
							var hasta = self.hermanos.index (self);
							if (desde < hasta) {
								var __iterable0__ = self.hermanos.__getslice__ (desde, hasta, 1);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									elem.seleccionar ();
								}
							}
							else {
								var __iterable0__ = self.hermanos.__getslice__ (hasta, desde + 1, 1);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									elem.seleccionar ();
								}
							}
							self.marcar ();
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.url, self.titulo, self.leyenda.py_replace ('"', '&#34;').py_replace ("'", '&#39;'), self._alt.py_replace ('"', '&#34;').py_replace ("'", '&#39;')));
							$ (self.target).find ('.select').addClass ('hidden');
							$ (self.target).bind ('click', self.click);
							$ (self.target).find ('img').bind ('click', (function __lambda__ (evt) {
								return $ (evt.target).trigger ('marcar', list ([self.target]));
							}));
							$ (self.target).find ('button').bind ('click', self.open);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.DetalleImagen = DetalleImagen;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
