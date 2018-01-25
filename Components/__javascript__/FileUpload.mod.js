	__nest__ (
		__all__,
		'FileUpload', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'FileUpload';
					var Widget = __init__ (__world__.Widget).Widget;
					var FileUpload = __class__ ('FileUpload', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Arrastra archivos a cualquier lugar para subirlos';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t<form method='post' enctype='multipart/form-data' action='{}'>\n\t\t<h3>{}</h3>\n\t\t<div>o</div> \n\t\t<input type='file' name='archivo'>\n\t\t{}\n\t\t</form>\n\t\t<iframe name='fileupload' class='hidden'></iframe>\n\t\t</div>\n\t\t";
							self.restricciones = '\n\t\t<p>Tamaño máximo de archivo: 128 MB.</p>\n\t\t<p>Dimensiones de imagen sugeridas: 150 por 150 píxeles.</p>\n\t\t';
							self.avanzado = false;
							self.activador = true;
							self.automatico = false;
							self.action = '';
							self.categorias = list ([]);
							self.tipos = list ([]);
							self.iframe = '';
						});},
						get enlazar () {return __get__ (this, function (self, funcion) {
							self.activador = funcion;
						});},
						get subidaAutomatica () {return __get__ (this, function (self, evt) {
							var __iterable0__ = $ (evt.target) [0].files;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var _file = __iterable0__ [__index0__];
								if (self.activador != null) {
									$ (self.target).find ('form').submit ();
									self.activador (_file, null);
								}
							}
						});},
						get subir () {return __get__ (this, function (self, evt) {
							var files = $ (evt.target) [0].files;
							var reader = new FileReader ();
							var __iterable0__ = files;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var file = __iterable0__ [__index0__];
								if (!(self.automatico)) {
									var ver = function (evt, file) {
										if (typeof file == 'undefined' || (file != null && file .hasOwnProperty ("__kwargtrans__"))) {;
											var file = file;
										};
										if (self.activador != null) {
											self.activador (file, evt.target.result);
										}
									};
									reader.onload = ver;
									var f = reader.readAsDataURL (file);
								}
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.action, self.titulo, self.restricciones));
							if (self.avanzado == false) {
								var avanzado = " class='hidden'";
							}
							else {
								var avanzado = '';
							}
							var _html = ('<div ' + avanzado) + ">Renombrar: <input name='renombre' > </div>";
							_html += ('<div ' + avanzado) + ">Categorias: <select name='opcion'>";
							var __iterable0__ = enumerate (self.categorias);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								_html += ((((("<option value='" + str (k)) + "' ") + (k == 0 ? 'selected' : '')) + '>') + elem) + '</option>';
							}
							_html += '</select></div>';
							_html += ('<div ' + avanzado) + ">Tipo: <select name='tipo'>";
							var __iterable0__ = enumerate (self.tipos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								_html += ((((("<option value='" + str (k)) + "' ") + (k == 0 ? 'selected' : '')) + '>') + elem) + '</option>';
							}
							_html += '</select></div>';
							_html += ('<div ' + avanzado) + "> Sobrescribir: <input type='checkbox' name='sobrescribir'></div>";
							$ (self.target).find ('form').append (_html);
							$ (self.target).find ('form').attr ('target', 'fileupload');
							var archivo = $ (self.target).find ("input[type='file']");
							if (self.automatico) {
								archivo.bind ('change', self.subidaAutomatica);
							}
							else {
								archivo.bind ('change', self.subir);
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.FileUpload = FileUpload;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
