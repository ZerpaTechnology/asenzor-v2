	__nest__ (
		__all__,
		'Media', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Media';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var Biblioteca = __init__ (__world__.Biblioteca).Biblioteca;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var Media = __class__ ('Media', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Gestor de Archivos';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div><b class='titulo'>{}</b><span class='close'>x</span></div>\n\t\t<div class='botonera'>\n\t\t<span class='btn'>{}</span>\n\t\t<span class='btn'>{}</span>\n\t\t</div>\n\t\t<div class='content'>\n\t\t</div>\n\t\t<div>\n\t\t<button class='elegir'>{}</button>\n\t\t</div>\n\t\t";
							self.tabsManger = BasicTabs ();
							self.btn1 = 'Subir archivos';
							self.btn2 = 'Biblioteca Multimedia';
							self.btn3 = 'Elegir';
							self.css_selected = dict ({'color': 'gray', 'border': 'solid', 'border-width': '1px', 'border-radius': '12px 12px 0px 0px'});
							self.css_deselected = dict ({'color': 'blue', 'border': 'none'});
							self.url = (config.base_url + settings.app) + '/admin/Archivos/action=ver';
							self.archivos = list ([]);
							self.biblioteca = Biblioteca ();
							self.biblioteca.Media = self;
							self.biblioteca.url = self.url;
							self.activador = null;
							self.value = list ([]);
						});},
						get subir () {return __get__ (this, function (self, evt) {
							// pass;
						});},
						get open () {return __get__ (this, function (self, activador) {
							self.activador = activador;
							$ (self.target).removeClass ('hidden');
						});},
						get close () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							$ (self.target).addClass ('hidden');
						});},
						get updateTitulo () {return __get__ (this, function (self, titulo) {
							$ (self.target).find ('.titulo').text (titulo);
						});},
						get clickTab () {return __get__ (this, function (self, evt) {
							$ (self.target).find ('.botonera').find ('.btn').css (self.css_deselected);
							$ (evt.target).css (self.css_selected);
							var indice = $ (self.target).find ('.botonera').find ('.btn').index (evt.target);
							self.tabsManger.showTab (indice);
						});},
						get selectTab () {return __get__ (this, function (self, tab) {
							for (var elem = 0; elem < 2; elem++) {
								if (elem == tab) {
									$ ($ (self.target).find ('.botonera').find ('.btn') [tab]).css (self.css_selected);
								}
								else {
									$ ($ (self.target).find ('.botonera').find ('.btn') [tab]).css (self.css_deselected);
								}
							}
						});},
						get noSeleccionados () {return __get__ (this, function (self) {
							self.biblioteca.currents = list ([]);
							self.biblioteca.clearDetalles ();
							$ (self.target).find ('.elegir').css (dict ({'color': 'gray', 'background-color': 'gray'}));
						});},
						get seleccionados () {return __get__ (this, function (self, seleccion) {
							self.biblioteca.currents = seleccion;
							self.currents = seleccion;
							$ (self.target).find ('.elegir').css (dict ({'color': 'white', 'background-color': 'blue'}));
						});},
						get elegir () {return __get__ (this, function (self) {
							self.value = list ([]);
							if (self.currents != list ([])) {
								var __iterable0__ = self.currents;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									self.value.append (elem.indice);
								}
								self.close ();
								self.activador (self.currents);
								return self.currents;
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							var upload = FileUpload ();
							upload.automatico = true;
							upload.action = (config.base_url + settings.app) + '/admin/Archivo/None/action=save';
							upload.categorias = nuclear.VAR ('categorias');
							upload.tipos = nuclear.VAR ('tipos');
							upload.enlazar (self.biblioteca.nueva);
							self.tabsManger.appendToTab (0, upload);
							self.tabsManger.appendToTab (1, self.biblioteca);
							$ (self.target).html (self._html.format (self.titulo, self.btn1, self.btn2, self.btn3));
							$ (self.target).addClass ('hidden');
							$ (self.target).find ('.close').bind ('click', self.close);
							$ ($ (self.target).find ('.botonera').find ('.btn') [1]).css (self.css_selected);
							$ (self.target).find ('.botonera').find ('.btn').bind ('click', self.clickTab);
							if (self.tabsManger != null) {
								self.tabsManger.bind ('subir', self.subir);
								$ (self.target).find ('.content').html (self.tabsManger.target);
							}
							$ (self.target).find ('.elegir').bind ('click', self.elegir);
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'Biblioteca' +
						'FileUpload' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.Biblioteca = Biblioteca;
						__all__.FileUpload = FileUpload;
						__all__.Media = Media;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
