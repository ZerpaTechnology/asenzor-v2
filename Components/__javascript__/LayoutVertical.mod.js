	__nest__ (
		__all__,
		'LayoutVertical', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'LayoutVertical';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var LayoutVertical = __class__ ('LayoutVertical', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							var widgets = tuple ([].slice.apply (arguments).slice (1));
							Widget.__init__ (self, '');
							self.target.html ('<div></div>');
							var __iterable0__ = widgets;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.add (elem);
							}
							self._html = '';
							self.icon = config.base_url + 'static/imgs/iconos/document-2.png';
							self.content = (function __lambda__ (self, k) {
								return self.target.find ('>div').find ('>div') [k];
							});
						});},
						get add () {return __get__ (this, function (self, widget) {
							self.format = list ([self.titulo]);
							var w = $ ('<div>');
							widget.py_update ();
							self.children.append (widget);
							self.target.find ('>div').append (w);
							widget._update = true;
						});},
						get hiddenTab () {return __get__ (this, function (self, n) {
							$ (self.target.find ('>div').find ('>div') [n]).hide ();
						});},
						get showTab () {return __get__ (this, function (self, n) {
							$ (self.target.find ('>div').find ('>div') [n]).show ();
						});},
						get sliderTab () {return __get__ (this, function (self, n) {
							var width = $ (self.find ('>div').target.find ('>div') [n]).outerWidth ();
							$ (self.target.find ('>div').find ('>div') [n]).css (dict ({'width': '0px'}));
							self.hiddenTab (n);
							$ (self.target.find ('>div').find ('>div') [n]).animate (dict ({'width': str (width) + 'px'}), 1000);
							$ (self.target.find ('>div').find ('>div') [n]).css (dict ({'width': str (width) + 'px'}));
						});},
						get reloadSizes () {return __get__ (this, function (self) {
							var width = 0;
							var __iterable0__ = enumerate (self.children);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								if (k + 1 == len (self.children)) {
									$ (self.target.find ('>div').find ('>div') [k]).css ('width', ('calc( 100% - ' + str (width)) + 'px)');
								}
								width += elem.target.outerWidth ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.LayoutVertical = LayoutVertical;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
