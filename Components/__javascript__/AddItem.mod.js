	__nest__ (
		__all__,
		'AddItem', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'AddItem';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var AddItem = __class__ ('AddItem', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span class='icon'></span>\n\t\t<div>\n\t\t<b>{}</b>\n\t\t<p>{}</p>\n\t\t<div>\n\t\t";
							self.icon = config.base_url + 'static/imgs/iconos/document-2.png';
							self.descripcion = '';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.descripcion]);
							self.__update__ ();
							self.target.find ('>.icon').css (dict ({'background-image': "url('{}')".format (self.icon)}));
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.AddItem = AddItem;
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
