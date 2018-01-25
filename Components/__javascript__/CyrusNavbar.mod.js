	__nest__ (
		__all__,
		'CyrusNavbar', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'CyrusNavbar';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var CyrusNavbar = __class__ ('CyrusNavbar', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<div class="navbar-wrapper">\n\n\t      <div class="container">\n\n\n\n\t        <div class="navbar navbar-default navbar-fixed-top" role="navigation" id="top-nav">\n\n\t          <div class="container">\n\n\t            <div class="navbar-header">\n\n\t              <!-- Logo Starts -->\n\n\t              <a class="navbar-brand" href="#home"><img src="" alt="logo" class=\'logo\'></a>\n\n\t              <!-- #Logo Ends -->\n\n\n\n\n\n\t              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n\n\t                <span class="sr-only">Toggle navigation</span>\n\n\t                <span class="icon-bar"></span>\n\n\t                <span class="icon-bar"></span>\n\n\t                <span class="icon-bar"></span>\n\n\t              </button>\n\n\n\n\t            </div>\n\n\n\n\n\n\t            <!-- Nav Starts -->\n\n\t            <div class="navbar-collapse in right-nav" style="height: auto;" >\n\n\t              \n\n\t            </div>\n\n\t            <!-- #Nav Ends -->\n\n\n\n\t          </div>\n\n\t        </div>\n\n\n\n\t      </div>\n\n\t    </div>\n\t\t';
							self.target.html (self._html);
							self._html = '';
							self._enlace = ((config.base_url + 'apps/') + settings.app) + '/user/static/images/portfolio/1.jpg';
							self._img = ((config.base_url + 'apps/') + settings.app) + '/user/static/images/portfolio/1.jpg';
							self._load_css = list ([config.base_url + 'static/css/bootstrap.css']);
							self._load_js = list ([config.base_url + 'static/js/bootstrap.js']);
							self._logo = config.base_url + 'apps/occoa/user/static/images/logo.png';
							self._menu = list ([list (['Home', '#home', list ([])]), list (['About', '#about', list ([])]), list (['Partners', '#partners', list ([])]), list (['Contact', '#contact', list ([])])]);
						});},
						get construir () {return __get__ (this, function (self, menu) {
							var wrapper = '<ul class="nav navbar-nav navbar-right scroll">';
							var __iterable0__ = menu;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								wrapper += ((((((('<li class="' + (len (elem) == 4 ? elem [3] : '')) + '"><a href="') + elem [1]) + '">') + elem [0]) + '</a>') + self.construir (elem [3])) + '</li>';
							}
							wrapper += '</ul>';
							return wrapper;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.target.find ('.logo').attr ('src', self._logo);
							self.target.find ('.right-nav').html (self.construir (self._menu));
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CyrusNavbar = CyrusNavbar;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
