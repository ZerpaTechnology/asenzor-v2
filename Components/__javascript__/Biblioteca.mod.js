	__nest__ (
		__all__,
		'Biblioteca', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Biblioteca';
					var Widget = __init__ (__world__.Widget).Widget;
					var DetalleImagen = __init__ (__world__.DetalleImagen).DetalleImagen;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var Biblioteca = __class__ ('Biblioteca', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, Media) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Subir archivo';
							};
							if (typeof Media == 'undefined' || (Media != null && Media .hasOwnProperty ("__kwargtrans__"))) {;
								var Media = null;
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div class='archivos'>\n\t\t<div><span>{}</span> <input type='search' placeholder='{}'></div>\n\t\t<div class='list'>\n\t\t</div>\n\t\t</div>\n\t\t<div class='detalles'>\n\t\t<b class='titulo'></b>\n\t\t<img class='hidden' src=''>\n\t\t<div class='info'></div>\n\t\t<hr>\n\t\t<table>\n\t\t<tr>\n\t\t<td> URL </td>\n\t\t<td><input name='url'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td>Titulo</td>\n\t\t<td><input name='titulo'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td>Leyenda</td>\n\t\t<td><textarea name='leyenda'></textarea></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td> Texto alternativo </td>\n\t\t<td><input name='alternativo'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td> Descripción </td>\n\t\t<td><textarea name='decripcion'></textarea></td>\n\t\t</tr>\n\t\t\n\t\t</table>\n\n\t\t</div>\n\t\t";
							self.Media = Media;
							self._titulo = self.titulo;
							self.sugerencias = 'Dimensiones de imagen sugeridas: 150 por 150 píxeles.';
							self.placeholder = 'Buscar elementos multimedia...';
							self.archivos = list ([]);
							self.currents = list ([]);
							self.base_url = ((config.base_url + config.apps_folder) + settings.app) + '/admin/static/archivos/Imagenes/';
						});},
						get open () {return __get__ (this, function (self) {
							self.Media.updateTitulo (self._titulo);
							self.Media.open ();
						});},
						get search () {return __get__ (this, function (self, evt) {
							var __iterable0__ = self.archivos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (!__in__ ($ (evt.target).val ().lower (), elem.titulo.lower ())) {
									$ (elem.target).addClass ('hidden');
								}
								else {
									$ (elem.target).removeClass ('hidden');
								}
							}
						});},
						get getFiles () {return __get__ (this, function (self) {
							var success = function (data) {
								var archivos = nuclear.normalizar (data);
								var __iterable0__ = archivos;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									var i = DetalleImagen ();
									i.titulo = elem [0];
									i.url = (((config.base_url + config.apps_folder) + settings.app) + '/admin/static/archivos/Imagenes/') + nuclear.thumbail (i.titulo);
									self.archivos.append (i);
								}
							};
							var error = function (objRequest) {
								// pass;
							};
							
							          $.ajax({url:self.url,
							                  async:false,
							                  success: success,
							                  error : error
							                  })
							          
						});},
						get nueva () {return __get__ (this, function (self, file, src) {
							var i = DetalleImagen ();
							var cargar = function () {
								i.refresh ();
								clearInterval (invervalo);
							};
							var invervalo = setInterval (cargar, 3000);
							self.Media.tabsManger.showTab (1);
							i.url = (src != null ? src : self.base_url + nuclear.thumbail (file.name
							));
							i.titulo = file.name
							i.ultimaModificacion = file.lastModified
							i.fechaUltimaModificacion = file.lastModifiedDate
							i.size = file.size
							i.tipo = file.type
							self.archivos.append (i);
							i.actualizarHermanos (self.archivos);
							i.Media = self.Media;
							i.py_update ();
							i.indice = len (self.archivos) - 1;
							$ (self.target).find ('.archivos').find ('.list').prepend (i.target);
						});},
						get clearDetalles () {return __get__ (this, function (self) {
							self.target.find ('.detalles').find ("[name='titulo']").val ('');
							self.target.find ('.detalles').find ('.titulo').html ('');
							self.target.find ('.detalles').find ('.info').html ('');
							self.target.find ('.detalles').find ("[name='url']").val ('');
							self.target.find ('.detalles').find ("[name='descripcion']").val ('');
							self.target.find ('.detalles').find ('img').attr ('src', '');
							self.target.find ('.detalles').find ('img').addClass ('hidden');
							self.currents.append (self.url);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.getFiles ();
							$ (self.target).html (self._html.format (self.sugerencias, self.placeholder));
							var __iterable0__ = enumerate (self.archivos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var i = __left0__ [1];
								i.Media = self.Media;
								i.actualizarHermanos (self.archivos);
								i.deseleccionar (self.archivos);
								i.py_update ();
								i.indice = k;
								$ (self.target).find ('.archivos').find ('.list').append (i.target);
							}
							$ (self.target).find ('.archivos').find ("input[type='search']").bind ('keyup', self.search);
							$ (self.target).find ('button').bind ('click', self.open);
						});}
					});
					__pragma__ ('<use>' +
						'DetalleImagen' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Biblioteca = Biblioteca;
						__all__.DetalleImagen = DetalleImagen;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
