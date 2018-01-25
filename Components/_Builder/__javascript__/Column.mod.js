	__nest__ (
		__all__,
		'_Builder.Column', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_Builder.Column';
					var Widget = __init__ (__world__.Widget).Widget;
					var Column = __class__ ('Column', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<sidebar class=\'controls\'>\n\t\t\t<b class=\'titulo\'></b>\n\t\t\t<span class=\'menu\'></span>\n\t\t\t<span class=\'duplicate\'></span>\n\t\t\t<span class=\'quit\'></span>\n\t\t</sidebar>\n\t\t<div class="content">\n\t\t<span class=\'add\'> Añadir </span>\n\t\t</div>\n\t\t';
							self.size = 12;
							self.row = 0;
							self.i = 0;
							self.dataChildren = list ([]);
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.content').find ('>.add');
							});
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get add () {return __get__ (this, function (self, widget, ntarget) {
							if (__in__ ('py_update', dir (widget))) {
								widget.py_update ();
								self.children.append (widget);
								if (ntarget == 1) {
									$ (self.content (self)).before (widget.target);
								}
								else if (ntarget == 2) {
									$ (self.content (self)).before (widget.target2);
								}
								else if (ntarget == 3) {
									$ (self.content (self)).before (widget.target3);
								}
								else if (ntarget == 4) {
									$ (self.content (self)).before (widget.target4);
								}
								else if (ntarget == 5) {
									$ (self.content (self)).before (widget.target5);
								}
							}
							else {
								self.target.find ('>.content').find ('>.add').before (widget.clone ());
							}
						});},
						get addModulo () {return __get__ (this, function (self, evt) {
							self.window.InsertModulo.row = self.row;
							self.window.InsertModulo.col = self.i;
							self.window.InsertModulo.column = self;
							self.window.open ('InsertModulo');
						});},
						get done () {return __get__ (this, function (self) {
							self.__button = self.target.find ('>button');
							self.target.css (dict ({'width': ('calc(' + str ((200 * self.size) / 12)) + '% - 20px)'}));
							self.__titulo = self.target.find ('>.controls').find ('>.titulo');
							self.__add = self.target.find ('>.content').find ('>.add');
							self.__add.bind ('click', self.addModulo);
							self.__titulo.text (self._titulo);
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
						__all__.Column = Column;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
