	__nest__ (
		__all__,
		'Collage', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var random = {};
					var __name__ = 'Collage';
					var Widget = __init__ (__world__.Widget).Widget;
					var Image = __init__ (__world__.Image).Image;
					__nest__ (random, '', __init__ (__world__.random));
					var Collage = __class__ ('Collage', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = "<b class='titulo'></b><div class='content'></div>";
							self.target.html (self._html);
							self._hmtl = '';
							self._imgs = list ([]);
							self.imgsWidth = 400;
							self.width = '100%';
							self.height = '100vh';
							self.area = list ([1200, 400]);
							self.rotaciones = list ([30, 12, -(32), 21, 45, -(20), 15, -(34), 40, 26, 6, -(22)]);
							self._hints = list ([]);
							self.i = 0;
							self.activadores = list ([]);
						});},
						get addImages () {return __get__ (this, function (self, widget) {
							if (py_typeof (widget) == list) {
								var __iterable0__ = enumerate (widget);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									elem.rotation = self.rotaciones [k];
									elem.py_update ();
									self.children.append (elem);
									self.target.find ('>.content').append (elem.target);
								}
							}
							else {
								widget.rotation = self.rotaciones [self.i];
								self.i++;
								widget.py_update ();
								self.children.append (widget);
								self.target.find ('>.content').append (widget.target);
							}
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('>.titulo').text (titulo);
							self._titulo = titulo;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.target.css (dict ({'width': self.width, 'height': self.height}));
							var area = list ([]);
							var y = 10;
							var por = 25;
							var _k = 0;
							var _pory = por;
							var _porx = 5;
							var __iterable0__ = enumerate (self._imgs);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								var img = Image ();
								img._src = elem;
								try {
									img._hint = self._hints [k];
								}
								catch (__except0__) {
									// pass;
								}
								if (_k < len (self.rotaciones)) {
									_k++;
								}
								else {
									var _k = 0;
								}
								img.rotation = self.rotaciones [_k];
								img.width = self.imgsWidth;
								try {
									img.activador = self.activadores [k];
								}
								catch (__except0__) {
									// pass;
								}
								img._hoverEffect = 'zoomOut';
								img._tooltip = 'top';
								img.target.find ('img').css (dict ({'-webkit-box-shadow': '10px 10px 33px -2px rgba(0,0,0,0.75)', '-moz-box-shadow': '10px 10px 33px -2px rgba(0,0,0,0.75)', 'box-shadow': '10px 10px 33px -2px rgba(0,0,0,0.75)'}));
								if (k == 0) {
									img._sources = true;
								}
								img.py_update ();
								self.target.find ('>.content').append (img.target);
								try {
									img.target.css (dict ({'position': 'absolute', 'top': str (_pory) + '%', 'left': str (_porx) + '%'}));
								}
								catch (__except0__) {
									// pass;
								}
								if (_porx < 80) {
									_porx += 20;
								}
								else {
									var _porx = 5;
									_pory += por;
								}
							}
							self.titulo (self._titulo);
							self.__titulo = self.target.find ('>.titulo');
						});}
					});
					__pragma__ ('<use>' +
						'Image' +
						'Widget' +
						'random' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Collage = Collage;
						__all__.Image = Image;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
