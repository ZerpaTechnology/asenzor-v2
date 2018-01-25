	__nest__ (
		__all__,
		'InputSearch', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'InputSearch';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var InputSearch = __class__ ('InputSearch', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "<div><span class='search'></span><input type='search' value='{}' name='{}' placeholder='{}'></div>";
							self.icon = config.base_url + 'static/imgs/iconos/lupa.png';
							self.placeholder = 'Buscar...';
							self.value = '';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.value, self.py_name, self.placeholder]);
							self.__update__ ();
							self.target.find ('>div').find ('>.search').css (dict ({'background-image': "url('{}')".format (self.icon)}));
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.InputSearch = InputSearch;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
