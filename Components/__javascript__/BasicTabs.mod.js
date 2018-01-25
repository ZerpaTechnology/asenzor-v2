	__nest__ (
		__all__,
		'BasicTabs', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BasicTabs';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __class__ ('BasicTabs', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, tabs, tabdefault) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							if (typeof tabs == 'undefined' || (tabs != null && tabs .hasOwnProperty ("__kwargtrans__"))) {;
								var tabs = 3;
							};
							if (typeof tabdefault == 'undefined' || (tabdefault != null && tabdefault .hasOwnProperty ("__kwargtrans__"))) {;
								var tabdefault = 0;
							};
							Widget.__init__ (self, titulo);
							self._html = '<div></div>';
							self.children = function () {
								var __accu0__ = [];
								for (var elem = 0; elem < tabs; elem++) {
									__accu0__.append (list ([]));
								}
								return __accu0__;
							} ();
							self.ntabs = tabs;
							self.tabWidth = 300;
							self.tabCurrent = 0;
							self.tabdefault = tabdefault;
							self.width = self.tabWidth * tabs;
							self.content = (function __lambda__ (self, k) {
								return self.tabs [k];
							});
						});},
						get showTab () {return __get__ (this, function (self, n) {
							$ (self.target).find ('>div').find ('>.tab').addClass ('hidden');
							$ ($ (self.target).find ('>div').find ('>.tab') [n]).removeClass ('hidden');
						});},
						get addToTab () {return __get__ (this, function (self, n, target) {
							if (__in__ ('update', dir (target))) {
								target.py_update ();
								self.children [n].append (target);
								$ ($ (self.target).find ('>div').find ('>.tab') [n]).html (target.target);
							}
							else {
								$ ($ (self.target).find ('>div').find ('>.tab') [n]).html (target);
							}
						});},
						get getTab () {return __get__ (this, function (self, n) {
							return $ ($ (self.target).find ('>div').find ('>.tab') [n]);
						});},
						get appendToTab () {return __get__ (this, function (self, n, target, ntarget) {
							if (typeof ntarget == 'undefined' || (ntarget != null && ntarget .hasOwnProperty ("__kwargtrans__"))) {;
								var ntarget = 1;
							};
							if (__in__ ('py_update', dir (target))) {
								target.py_update ();
								self.children [n].append (target);
								self.dataChildren.append (dict ({}));
								if (ntarget == 1) {
									$.when (self.tabs [n].append (target.target)).then (target.done);
									target.parent = self;
								}
								else if (ntarget == 2) {
									$.when (self.tabs [n].append (target.target2)).then (target.done);
									target.parent2 = self;
								}
								else if (ntarget == 3) {
									$.when (self.tabs [n].append (target.target3)).then (target.done);
									target.parent3 = self;
								}
								else if (ntarget == 4) {
									$.when (self.tabs [n].append (target.target4)).then (target.done);
									target.parent4 = self;
								}
								else if (ntarget == 5) {
									$.when (self.tabs [n].append (target.target5)).then (target.done);
									target.parent5 = self;
								}
							}
							else {
								self.tabs [n].append (target);
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							self.tabs = function () {
								var __accu0__ = [];
								var __iterable0__ = enumerate (range (self.ntabs));
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var i = __left0__ [1];
									__accu0__.append ((k == self.tabdefault ? $ ("<div class='tab'></div>") : $ ("<div class='tab hidden'></div>")));
								}
								return __accu0__;
							} ();
							var __iterable0__ = self.tabs;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ (self.target).find ('>div').append (elem);
							}
							$ (self.target).find ('>div').find ('>.tab').css (dict ({'width': self.tabWidth}));
							$ (self.target).find ('>div').css (dict ({'width': self.width}));
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
