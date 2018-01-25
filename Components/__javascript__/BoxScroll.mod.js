	__nest__ (
		__all__,
		'BoxScroll', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BoxScroll';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var BoxScroll = __class__ ('BoxScroll', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BoxScroll = BoxScroll;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
