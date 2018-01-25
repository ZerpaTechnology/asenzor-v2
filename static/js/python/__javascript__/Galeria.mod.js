	(function () {
		var __name__ = '__main__';
		var decode = Codificador.Codificador.decode;
		var config = Config.Config ();
		var Galeria = __class__ ('Galeria', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, py_selector, preview, pos_default) {
				if (typeof preview == 'undefined' || (preview != null && preview .hasOwnProperty ("__kwargtrans__"))) {;
					var preview = '#out';
				};
				if (typeof pos_default == 'undefined' || (pos_default != null && pos_default .hasOwnProperty ("__kwargtrans__"))) {;
					var pos_default = 0;
				};
				self.posiciones = function () {
					var __accu0__ = [];
					var __iterable0__ = $ (py_selector);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var i = __iterable0__ [__index0__];
						__accu0__.append (pos_default);
					}
					return __accu0__;
				} ();
				self.iterables = list ([]);
				self.py_selector = py_selector;
				self.current = 0;
				self.widget = preview;
				self.preview = $ (preview + ' .preview') [0];
				var __iterable0__ = enumerate (self.posiciones);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var i = __left0__ [1];
					var l = list ([]);
					var __iterable1__ = $ (py_selector) [k].children;
					for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
						var tab = __iterable1__ [__index1__];
						var __iterable2__ = tab.children;
						for (var __index2__ = 0; __index2__ < len (__iterable2__); __index2__++) {
							var span = __iterable2__ [__index2__];
							if (window.innerHeight > 585 && window.innerWidth > 386) {
								l.append (span.getAttribute ('href'));
							}
							else {
								l.append (span.children [0].src);
							}
						}
					}
					self.iterables.append (l);
				}
				var abspath = function (cadena) {
					var l = cadena.py_split ('/');
					for (var i = 0; i < cadena.count ('../'); i++) {
						var f = l.index ('..');
						delete l [f - 1];
						delete l [f - 1];
					}
					return '/'.join (l);
				};
				var img_link = function (evt) {
					evt.preventDefault ();
					$ (preview).removeClass ('hidden');
					var __iterable0__ = enumerate ($ (self.py_selector));
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						if (elem == evt.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode) {
							self.posiciones [k] = self.iterables [k].index (evt.target.parentNode.getAttribute ('href'));
							$ (self.preview).css ('background-image', ("url('" + self.iterables [k] [self.posiciones [k]]) + "')");
							self.current = k;
						}
					}
				};
				$ (self.py_selector).bind ('click', img_link);
				var f_left = function (evt) {
					self.posiciones [self.current] = (self.posiciones [self.current] > 0 ? self.posiciones [self.current] - 1 : len (self.iterables [self.current]) - 1);
					$ (self.preview).css ('background-image', ("url('" + self.iterables [self.current] [self.posiciones [self.current]]) + "')");
				};
				$ ('.f-left').bind ('click', f_left);
				var f_right = function (evt) {
					self.posiciones [self.current] = (self.posiciones [self.current] < len (self.iterables [self.current]) - 1 ? self.posiciones [self.current] + 1 : 0);
					alert (self.iterables [self.current] [self.posiciones [self.current]]);
					$ (self.preview).css ('background-image', ("url('" + self.iterables [self.current] [self.posiciones [self.current]]) + "')");
				};
				$ ('.f-right').bind ('click', f_right);
				var _exit = function (evt) {
					$ (evt.target.parentNode.parentNode).addClass ('hidden');
				};
				$ ('.exit').bind ('click', _exit);
			});},
			get py_update () {return __get__ (this, function (self) {
				self.preview = $ (self.widget + ' .preview') [0];
			});}
		});
		var Slider = __class__ ('Slider', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, py_selector, pos_default) {
				if (typeof pos_default == 'undefined' || (pos_default != null && pos_default .hasOwnProperty ("__kwargtrans__"))) {;
					var pos_default = 0;
				};
				self.py_selector = py_selector;
				self.iterables = $ (self.py_selector);
				self.posiciones = function () {
					var __accu0__ = [];
					var __iterable0__ = self.iterables;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var i = __iterable0__ [__index0__];
						__accu0__.append (pos_default);
					}
					return __accu0__;
				} ();
				var __iterable0__ = enumerate ($ (self.py_selector));
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k2 = __left0__ [0];
					var selec = __left0__ [1];
					var content = $ (selec).find ('.content') [0];
					if (len (content.children) > 0) {
						var __iterable1__ = enumerate (content.children);
						for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
							var __left0__ = __iterable1__ [__index1__];
							var k = __left0__ [0];
							var elem = __left0__ [1];
							$ (elem).css (dict ({'max-width': '100%', 'max-height': '100%', 'text-align': 'center'}));
							$ (content).css (dict ({'padding-top': elem.height / 2 - elem.height / 2}));
							if (k != pos_default) {
								$ (elem).addClass ('hidden');
							}
						}
					}
				}
				var f_right = function (evt) {
					var __iterable0__ = enumerate (self.iterables);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						if (elem.children [2] == evt.target.parentNode) {
							var content = elem.children [0];
							$ (content.children [self.posiciones [k]]).addClass ('hidden');
							self.posiciones [k] = (self.posiciones [k] < len (content.children) - 1 ? self.posiciones [k] + 1 : 0);
							$ (content.children [self.posiciones [k]]).removeClass ('hidden');
							$ (content).css (dict ({'padding-top': $ (content) [0].height / 2 - content.children [self.posiciones [k]].height / 2}));
						}
					}
				};
				var f_left = function (evt) {
					var __iterable0__ = enumerate (self.iterables);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						if (elem.children [1] == evt.target.parentNode) {
							var content = elem.children [0];
							$ (content.children [self.posiciones [k]]).addClass ('hidden');
							self.posiciones [k] = (self.posiciones [k] > 0 ? self.posiciones [k] - 1 : len (content.children) - 1);
							$ (content.children [self.posiciones [k]]).removeClass ('hidden');
							$ (content).css (dict ({'padding-top': $ (content) [0].height / 2 - content.children [self.posiciones [k]].height / 2}));
						}
					}
				};
				$ (self.py_selector + ' .f-left').bind ('click', f_left);
				$ (self.py_selector + ' .f-right').bind ('click', f_right);
			});}
		});
		__pragma__ ('<all>')
			__all__.Galeria = Galeria;
			__all__.Slider = Slider;
			__all__.__name__ = __name__;
			__all__.config = config;
			__all__.decode = decode;
		__pragma__ ('</all>')
	}) ();
