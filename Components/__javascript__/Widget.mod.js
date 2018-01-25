	__nest__ (
		__all__,
		'Widget', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Widget';
					var Widget = __class__ ('Widget', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							self._titulo = titulo;
							self.target = $ (("<div class='" + self.__class__.__name__) + "'></div>");
							self.target2 = $ (("<div class='" + self.__class__.__name__) + "'></div>");
							self.target3 = $ (("<div class='" + self.__class__.__name__) + "'></div>");
							self.target4 = $ (("<div class='" + self.__class__.__name__) + "'></div>");
							self.target5 = $ (("<div class='" + self.__class__.__name__) + "'></div>");
							self.content = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self.content2 = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self.content3 = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self.content4 = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self.content5 = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self._html = '';
							self._html2 = '';
							self._html3 = '';
							self._html4 = '';
							self._html5 = '';
							self.media = null;
							self.children = list ([]);
							self.hermanos = list ([]);
							self.children2 = list ([]);
							self.hermanos2 = list ([]);
							self.children3 = list ([]);
							self.hermanos3 = list ([]);
							self.children4 = list ([]);
							self.hermanos4 = list ([]);
							self.children5 = list ([]);
							self.hermanos5 = list ([]);
							self.value = null;
							self.py_name = '';
							self._update = false;
							self.format = list ([self.titulo]);
							self.format2 = list ([self.titulo]);
							self.format3 = list ([self.titulo]);
							self.format4 = list ([self.titulo]);
							self.format5 = list ([self.titulo]);
							self.primitivo = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self.css_styles = list ([]);
							self._descripcion = '';
							self._sources = false;
							self._load_js = list ([]);
							self._load_css = list ([]);
							self.parent = null;
							self.parent2 = null;
							self.parent3 = null;
							self.parent4 = null;
							self.parent5 = null;
							self._last_js = null;
							self.data = dict ({});
							self.dataChildren = list ([]);
						});},
						get css () {return __get__ (this, function (self, estilo1, estilo2, py_selector) {
							if (typeof estilo2 == 'undefined' || (estilo2 != null && estilo2 .hasOwnProperty ("__kwargtrans__"))) {;
								var estilo2 = null;
							};
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = null;
							};
							if (self._update) {
								if (py_typeof (estilo1) == str && py_typeof (estilo2) == str && py_selector == str) {
									return self.target.find (py_selector).css (estilo1, estilo2);
								}
								else if ((py_typeof (estilo1) == str || py_typeof (estilo1) == dict) && estilo2 == null && py_selector != null) {
									return self.target.find (py_selector).css (estilo1);
								}
								else if (py_typeof (estilo1) == dict && estilo2 == null && py_selector == null) {
									return self.target.find (py_selector).css (estilo1);
								}
							}
							else {
								self.css_styles.append (list ([estilo1, estilo2, py_selector]));
							}
						});},
						get load_sources () {return __get__ (this, function (self) {
							if (!(self._sources)) {
								var __iterable0__ = self._load_css;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var css = __iterable0__ [__index0__];
									var __iterable1__ = $ ('link');
									for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
										var elem = __iterable1__ [__index1__];
										var temp = css.py_split ('/');
										var cargar = false;
										if ($ (elem).attr ('href').endswith (temp [len (temp) - 1])) {
											var cargar = true;
											break;
										}
									}
									if (cargar == false) {
										$ ('head').append ("<link rel='stylesheet' href='{}'>".format (css));
									}
								}
								var __iterable0__ = self._load_js;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var js = __iterable0__ [__index0__];
									var __iterable1__ = $ ('script');
									for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
										var elem = __iterable1__ [__index1__];
										var temp = js.py_split ('/');
										var cargar = false;
										if ($ (elem).attr ('src').endswith (temp [len (temp) - 1])) {
											var cargar = true;
											break;
										}
									}
									if (cargar == false) {
										self._last_js = $ ("<script src='{}'></script>".format (js));
										$ ('head').append (self._last_js);
									}
								}
								var actualiza = function (evt) {
									self._sources = true;
								};
								if (self._last_js != null) {
									self._last_js.on ('load', actualiza);
								}
							}
						});},
						get bind () {return __get__ (this, function (self, evento, funcion, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = null;
							};
							if (py_selector == null) {
								self.target.bind (evento, funcion);
							}
							else {
								$ (self.target).find (py_selector).bind (evento, funcion);
							}
						});},
						get addSeparador () {return __get__ (this, function (self, hr) {
							if (typeof hr == 'undefined' || (hr != null && hr .hasOwnProperty ("__kwargtrans__"))) {;
								var hr = false;
							};
							if (hr) {
								$ (self.target).append ('<hr>');
							}
							else {
								$ (self.target).append ('<br>');
							}
						});},
						get descripcion () {return __get__ (this, function (self, descripcion) {
							self.__descripcion.text (descripcion);
							self._descripcion = descripcion;
						});},
						get add () {return __get__ (this, function (self, target, n) {
							if (typeof n == 'undefined' || (n != null && n .hasOwnProperty ("__kwargtrans__"))) {;
								var n = 1;
							};
							self.format = list ([self.titulo]);
							if (__in__ ('py_update', dir (target))) {
								if (self._update) {
									target.py_update ();
									self.children.append (target);
									self.dataChildren.append (dict ({}));
									target._update = true;
									if (n == 1) {
										$.when ($ (self.content (self)).append (target.target)).then (target.done);
										target.parent = self;
									}
									else if (n == 2) {
										$.when ($ (self.content (self)).append (target.target2)).then (target.done);
										target.parent2 = self;
									}
									else if (n == 3) {
										$.when ($ (self.content (self)).append (target.target3)).then (target.done);
										target.parent3 = self;
									}
									else if (n == 4) {
										$.when ($ (self.content (self)).append (target.target4)).then (target.done);
										target.parent4 = self;
									}
									else if (n == 5) {
										$.when ($ (self.content (self)).append (target.target5)).then (target.done);
										target.parent5 = self;
									}
								}
								else {
									target.py_update ();
									self.children.append (target);
								}
							}
							else if (n == 1) {
								$.when ($ (self.content (self)).append (target)).then (target.done);
								target.parent = self;
							}
							else if (n == 2) {
								$.when ($ (self.content (self)).append (target)).then (target.done);
								target.parent2 = self;
							}
							else if (n == 3) {
								$.when ($ (self.content (self)).append (target)).then (target.done);
								target.parent3 = self;
							}
							else if (n == 4) {
								$.when ($ (self.content (self)).append (target)).then (target.done);
								target.parent4 = self;
							}
							else if (n == 5) {
								$.when ($ (self.content (self)).append (target)).then (target.done);
								target.parent5 = self;
							}
						});},
						get add2 () {return __get__ (this, function (self, target, n) {
							if (typeof n == 'undefined' || (n != null && n .hasOwnProperty ("__kwargtrans__"))) {;
								var n = 1;
							};
							self.format = list ([self.titulo]);
							if (self._update) {
								target.py_update ();
								self.children2.append (target);
								target._update = true;
								self.dataChildren.append (dict ({}));
								if (n == 1) {
									$ (self.content2 (self)).append (target.target);
								}
								else if (n == 2) {
									$ (self.content2 (self)).append (target.target2);
								}
								else if (n == 3) {
									$ (self.content2 (self)).append (target.target3);
								}
								else if (n == 4) {
									$ (self.content2 (self)).append (target.target4);
								}
								else if (n == 5) {
									$ (self.content2 (self)).append (target.target5);
								}
							}
							else {
								target.py_update ();
								self.children2.append (target);
							}
						});},
						get add3 () {return __get__ (this, function (self, target, n) {
							if (typeof n == 'undefined' || (n != null && n .hasOwnProperty ("__kwargtrans__"))) {;
								var n = 1;
							};
							self.format = list ([self.titulo]);
							if (self._update) {
								target.py_update ();
								self.children3.append (target);
								target._update = true;
								self.dataChildren.append (dict ({}));
								if (n == 1) {
									$ (self.content3 (self)).append (target.target);
								}
								else if (n == 2) {
									$ (self.content3 (self)).append (target.target2);
								}
								else if (n == 3) {
									$ (self.content3 (self)).append (target.target3);
								}
								else if (n == 4) {
									$ (self.content3 (self)).append (target.target4);
								}
								else if (n == 5) {
									$ (self.content3 (self)).append (target.target5);
								}
							}
							else {
								target.py_update ();
								self.children3.append (target);
							}
						});},
						get add4 () {return __get__ (this, function (self, target, n) {
							if (typeof n == 'undefined' || (n != null && n .hasOwnProperty ("__kwargtrans__"))) {;
								var n = 1;
							};
							self.format = list ([self.titulo]);
							if (self._update) {
								target.py_update ();
								self.children4.append (target);
								target._update = true;
								self.dataChildren.append (dict ({}));
								if (n == 1) {
									$ (self.content4 (self)).append (target.target);
								}
								else if (n == 2) {
									$ (self.content4 (self)).append (target.target2);
								}
								else if (n == 3) {
									$ (self.content4 (self)).append (target.target3);
								}
								else if (n == 4) {
									$ (self.content4 (self)).append (target.target4);
								}
								else if (n == 5) {
									$ (self.content4 (self)).append (target.target5);
								}
							}
							else {
								target.py_update ();
								self.children4.append (target);
							}
						});},
						get add5 () {return __get__ (this, function (self, target, n) {
							if (typeof n == 'undefined' || (n != null && n .hasOwnProperty ("__kwargtrans__"))) {;
								var n = 1;
							};
							self.format = list ([self.titulo]);
							if (self._update) {
								target.py_update ();
								self.children5.append (target);
								target._update = true;
								self.dataChildren.append (dict ({}));
								if (n == 1) {
									$ (self.content5 (self)).append (target.target);
								}
								else if (n == 2) {
									$ (self.content5 (self)).append (target.target2);
								}
								else if (n == 3) {
									$ (self.content5 (self)).append (target.target3);
								}
								else if (n == 4) {
									$ (self.content5 (self)).append (target.target4);
								}
								else if (n == 5) {
									$ (self.content5 (self)).append (target.target5);
								}
							}
							else {
								target.py_update ();
								self.children5.append (target);
							}
						});},
						get show () {return __get__ (this, function (self) {
							self.target.show ();
						});},
						get hidden () {return __get__ (this, function (self) {
							self.target.hide ();
						});},
						get titulo () {return __get__ (this, function (self, titulo) {
							self.__titulo.text (titulo);
							self._titulo = titulo;
						});},
						get val () {return __get__ (this, function (self) {
							var value = dict ([[self.py_name, list ([])]]);
							if (self.children != list ([])) {
								var __iterable0__ = self.children;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									value [self.py_name] = elem.val ();
								}
								return value;
							}
							else {
								return self.value;
							}
						});},
						get clone () {return __get__ (this, function (self, target) {
							var copy = function (objeto) {
								if (__in__ ('__class__', dir (objeto))) {
									if (objeto.prototype != null) {
										var o = new objeto.prototype.constructor;
										var __iterable0__ = dir (o);
										for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
											var elem = __iterable0__ [__index0__];
											if ( typeof getattr(o,elem)!='function'
											) {
												setattr (o, elem, copy (getattr (objeto, elem)));
											}
										}
									}
									else if (objeto.__proto__.constructor==Array
									) {
										var l = list ([]);
										var __iterable0__ = objeto;
										for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
											var elem = __iterable0__ [__index0__];
											l.append (copy (elem));
										}
										var o = Object.assign (list ([]), l);
									}
									else if (objeto == null) {
										var o = objeto;
									}
									else if (objeto.__proto__.constructor==String
									 || objeto.__proto__.constructor==Number
									 || objeto.__proto__.constructor==Boolean
									) {
										var o = objeto;
									}
									else if (objeto.__proto__.constructor==Function
									) {
										var o = objeto.prototype.constructor;
									}
									else {
										var d = dict ({});
										var __iterable0__ = objeto;
										for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
											var elem = __iterable0__ [__index0__];
											d [elem] = copy (objeto [elem]);
										}
										var o = Object.assign (dict ({}), d);
									}
								}
								else if (py_typeof (objeto) == str || py_typeof (objeto) == int || py_typeof (objeto) == float || py_typeof (objeto) == bool) {
									var o = objeto.valueOf ();
								}
								else if (py_typeof (objeto) != str && py_typeof (objeto) != int && py_typeof (objeto) != float && py_typeof (objeto) != bool && py_typeof (objeto) != null) {
									var o = objeto;
								}
								else {
									var o = objeto;
								}
								return o;
							};
							var clon = copy (self);
							var clonarChildren = function (widget) {
								var l = list ([]);
								var __iterable0__ = enumerate (widget.children);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									widget.children [k] = copy (widget.children [k]);
									widget.children [k].target = $ (elem.target [0].outerHTML);
									widget.children [k].target2 = $ (elem.target2 [0].outerHTML);
									widget.children [k].target3 = $ (elem.target3 [0].outerHTML);
									widget.children [k].target4 = $ (elem.target4 [0].outerHTML);
									widget.children [k].target5 = $ (elem.target5 [0].outerHTML);
									l.append (clonarChildren (widget.children [k]));
								}
								widget.children = l;
								return widget;
							};
							clonarChildren (clon);
							clon.target = $ (clon.target [0].outerHTML);
							clon.target2 = $ (clon.target2 [0].outerHTML);
							clon.target3 = $ (clon.target3 [0].outerHTML);
							clon.target4 = $ (clon.target4 [0].outerHTML);
							clon.target5 = $ (clon.target5 [0].outerHTML);
							clon.reload ();
							return clon;
						});},
						get done () {return __get__ (this, function (self) {
							// pass;
						});},
						get __update__ () {return __get__ (this, function (self) {
							self._update = true;
							self.load_sources ();
							self.target.html (self._html.format.apply (null, self.format));
							self.target2.html (self._html2.format.apply (null, self.format2));
							self.target3.html (self._html3.format.apply (null, self.format3));
							self.target4.html (self._html4.format.apply (null, self.format4));
							self.target5.html (self._html5.format.apply (null, self.format5));
							if (self.children != list ([])) {
								var __iterable0__ = enumerate (self.children);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									if (py_typeof (elem) == list) {
										var __iterable1__ = enumerate (elem);
										for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
											var __left0__ = __iterable1__ [__index1__];
											var k2 = __left0__ [0];
											var elem2 = __left0__ [1];
											if (self.content != null) {
												$ (self.content (self, k, k2)).append (elem.target);
											}
										}
									}
									else if (self.content != null) {
										$ (self.content (self, k)).append (elem.target);
									}
								}
							}
							if (self.css_styles != list ([])) {
								var __iterable0__ = self.css_styles;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									self.css (elem [0], elem [1], elem [2]);
								}
							}
							self.__titulo = self.target.find ('>.titulo');
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
						});},
						get reload () {return __get__ (this, function (self) {
							self.py_update ();
							var __iterable0__ = self.children;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.py_update ();
							}
						});},
						get updateData () {return __get__ (this, function (self, data) {
							var __iterable0__ = data.py_keys ();
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								setattr (self, elem, data [elem]);
							}
						});},
						get run () {return __get__ (this, function (self, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = '.widget';
							};
							self.py_update ();
							$ (py_selector).append (self.target);
						});},
						get run2 () {return __get__ (this, function (self, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = '.widget';
							};
							self.py_update ();
							$ (py_selector).append (self.target2);
						});},
						get run3 () {return __get__ (this, function (self, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = '.widget';
							};
							self.py_update ();
							$ (py_selector).append (self.target3);
						});},
						get run4 () {return __get__ (this, function (self, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = '.widget';
							};
							self.py_update ();
							$ (py_selector).append (self.target4);
						});},
						get run5 () {return __get__ (this, function (self, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = '.widget';
							};
							self.py_update ();
							$ (py_selector).append (self.target5);
						});}
					});
					__pragma__ ('<all>')
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
