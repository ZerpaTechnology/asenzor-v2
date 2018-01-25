	__nest__ (
		__all__,
		'Components', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Components';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var Biblioteca = __init__ (__world__.Biblioteca).Biblioteca;
					var Media = __class__ ('Media', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Gestor de Archivos';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div><b class='titulo'>{}</b><span class='close'>x</span></div>\n\t\t<div class='botonera'>\n\t\t<span class='btn'>{}</span>\n\t\t<span class='btn'>{}</span>\n\t\t</div>\n\t\t<div class='content'>\n\t\t</div>\n\t\t<div>\n\t\t<button>{}</button>\n\t\t</div>\n\t\t";
							self.tabsManger = BasicTabs ();
							self.btn1 = 'Subir archivos';
							self.btn2 = 'Biblioteca Multimedia';
							self.btn3 = 'Elegir';
							self.css_selected = dict ({'color': 'gray', 'border': 'solid', 'border-width': '1px', 'border-radius': '12px 12px 0px 0px'});
							self.css_deselected = dict ({'color': 'blue', 'border': 'none'});
						});},
						get subir () {return __get__ (this, function (self, evt) {
							// pass;
						});},
						get open () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
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
						get py_update () {return __get__ (this, function (self) {
							var upload = FileUpload ();
							self.tabsManger.appendToTab (0, upload);
							self.tabsManger.appendToTab (1, Biblioteca);
							$ (self.target).html (self._html.format (self.titulo, self.btn1, self.btn2, self.btn3));
							$ (self.target).addClass ('hidden');
							$ (self.target).find ('.close').bind ('click', self.close);
							$ ($ (self.target).find ('.botonera').find ('.btn') [1]).css (self.css_selected);
							$ (self.target).find ('.botonera').find ('.btn').bind ('click', self.clickTab);
							if (self.tabsManger != null) {
								self.tabsManger.bind ('subir', self.subir);
								$ (self.target).find ('.content').html (self.tabsManger.target);
							}
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
					__pragma__ ('</all>')
				}
			}
		}
	);
