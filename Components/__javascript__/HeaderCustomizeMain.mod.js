	__nest__ (
		__all__,
		'HeaderCustomizeMain', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'HeaderCustomizeMain';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __class__ ('HeaderCustomizeMain', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t<div class='text'>\n\t\t<span class='help'>?</span>\n\n\t\t<p>Estas personalizando</p>\n\t\t<h3>{}</h3>\n\t\t<div class='pro'>\n\t\t</div>\n\t\t</div>\n\t\t<div class='info' >\n\t\t<p>{}</p>\n\t\t</div>\n\t\t</div>\n\t\t";
							self._help = '\n\t\tEl personalizador te permite tener una \n\t\tvista previa de los cambios de tu sitio \n\t\tantes de publicarlos. Puedes navegar a \n\t\ttraves de las distintas páginas de tu \n\t\tsitio sin salir de la vista previa. Se \n\t\tmuestran enlaces de editar a algunos \n\t\telementos que lo apliquen.';
							self.proButton = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self._help));
							$ (self.target).find ('.info').addClass ('hidden');
							$ (self.target).find ('.help').bind ('click', (function __lambda__ (evt) {
								return ($(evt.target.parentNode).next().hasClass('hidden')
								 ? $(evt.target.parentNode).next().removeClass('hidden')
								 : $(evt.target.parentNode).next().addClass('hidden')
								);
							}));
							if (self.proButton != null) {
								$ (self.target).find ('.pro').html (self.proButton);
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
