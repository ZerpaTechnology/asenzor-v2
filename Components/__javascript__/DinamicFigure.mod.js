	__nest__ (
		__all__,
		'DinamicFigure', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'DinamicFigure';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var DinamicFigure = __class__ ('DinamicFigure', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<div class=" clearfix grid"> \n\t\t<figure class="effect-oscar  wowload fadeIn animated" style="visibility: visible; animation-name: fadeIn;">\n        \t<img src="" alt="img01">\n        \t<figcaption>\n            \t<h2 class=\'titulo\'></h2>\n            \t<span>\n            \t<p>Lily likes to play with crayons and pencils</p>\n            \t<br>\n            \t<a href="" title="1" data-gallery="">View more</a>\n            \t</span>            \n        \t</figcaption>\n    \t</figure>\n    \t</div>\n\t\t';
							self._src = ((config.base_url + 'apps/') + settings.app) + '/user/static/images/portfolio/1.jpg';
							self.target.html (self._html);
							self._html = '';
							self.width = 300;
							self.height = 300;
							self._enlace = ((config.base_url + 'apps/') + settings.app) + '/user/static/images/portfolio/1.jpg';
							self.activador = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.__titulo = self.target.find ('>div').find ('>figure').find ('>figcaption').find ('>.titulo');
							self.__p = self.target.find ('>div').find ('>figure').find ('>figcaption').find ('>span').find ('>p');
							self.__descripcion = self.__p;
							self.__a = self.target.find ('>div').find ('>figure').find ('>figcaption').find ('>span').find ('>a');
							self.__img = self.target.find ('>div').find ('>figure').find ('>img');
							self.titulo (self._titulo);
							self.descripcion (self._descripcion);
							self.target.css (dict ({'width': self.width, 'height': self.height}));
							self.__img.attr ('src', self._src);
							self.__a.attr ('href', self._enlace);
							if (self.activador != null) {
								self.__a.bind ('click', self.activador (self));
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.DinamicFigure = DinamicFigure;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
