	__nest__ (
		__all__,
		'Acordion', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Acordion';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Acordion = __class__ ('Acordion', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Logo';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<div class='content'>\n\t\t</div>\n\t\t<div  class='btns'>\n\t\t<span class='reordenar'>{}</span>\n\t\t<button class='add'>{}</button>\n\t\t</div>\n\t\t<span class='borrar'>{}</span>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = dict ({});
							self.open = false;
							self.height = 0;
							self.children = list ([]);
							self.backgroundContents = '#999';
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.content');
							});
							self.span = 'Reordenar';
							self.btn = 'Añadir items';
							self.borrar = 'Borrar';
						});},
						get add () {return __get__ (this, function (self, titulo, content, descripcion) {
							if (typeof descripcion == 'undefined' || (descripcion != null && descripcion .hasOwnProperty ("__kwargtrans__"))) {;
								var descripcion = '';
							};
							var w = TabAcordion (titulo, descripcion);
							w.hermanos = self.children;
							w.activador = self.cerrarHermanos;
							w.py_update ();
							self.children.append (w);
							$ (self.target).find ('>.content').append (w.target);
							w.target.find ('>.content').css (dict ({'background-color': self.backgroundContents}));
							var __iterable0__ = content;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								w.add (elem);
							}
						});},
						get addTab () {return __get__ (this, function (self, tab) {
							tab.py_update ();
							self.children.append (tab);
							if (self._update) {
								$ (self.content (self)).append (tab.target);
							}
						});},
						get cerrarHermanos () {return __get__ (this, function (self, target) {
							var __iterable0__ = target.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem != target) {
									elem.cerrar ();
								}
							}
						});},
						get appendToTab () {return __get__ (this, function (self, tab, target) {
							target.py_update ();
							self.children [tab].add (target);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.span, self.btn, self.borrar]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'TabAcordion' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.TabAcordion = TabAcordion;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
