	__nest__ (
		__all__,
		'BoxText', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BoxText';
					var Component = nuclear.Component;
					var Widget = __init__ (__world__.Widget).Widget;
					var BoxText = __class__ ('BoxText', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<h1 class='titulo'></h1>\n\t\t<div class='content'> \n\t\t</div>\n\t\t";
							self._update = true;
							self.textos = list ([]);
						});},
						get text () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('.\n');
							if (self._update) {
								var p = $ ('<p>{}</p>'.repeat (len (lcadena)).format.apply (null, lcadena));
								if (estilos != null) {
									p.css (estilos);
								}
								self.target.find ('>.content').html (p);
							}
							else {
								self.textos.html (self.target.find ('>.content').append ('<p>{}</p>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get h3 () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('\n');
							if (self._update) {
								var _h3 = $ ('<h3>{}</h3>'.repeat (len (lcadena)).format.apply (null, lcadena));
								if (estilos != null) {
									_h3.css (estilos);
								}
								self.target.find ('>.content').append (_h3);
							}
							else {
								self.textos.append (self.target.find ('>.content').append ('<h3>{}</h3>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get h4 () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('\n');
							if (self._update) {
								var _h4 = $ ('<h4>{}</h4>'.repeat (len (lcadena)).format.apply (null, lcadena));
								if (estilos != null) {
									_h4.css (estilos);
								}
								self.target.find ('>.content').append (_h4);
							}
							else {
								self.textos.append (self.target.find ('>.content').append ('<h4>{}</h4>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get h5 () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('\n');
							if (self._update) {
								var _h5 = $ ('<h5>{}</h5>'.repeat (len (lcadena)).format.apply (null, lcadena));
								if (estilos != null) {
									_h5.css (estilos);
								}
								self.target.find ('>.content').append (_h3);
							}
							else {
								self.textos.append (self.target.find ('>.content').append ('<h5>{}</h5>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get h2 () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('\n');
							if (self._update) {
								var _h2 = $ ('<h2>{}</h2>'.repeat (len (lcadena)).format.apply (null, lcadena));
								if (estilos != null) {
									_h2.css (estilos);
								}
								self.target.find ('>.content').append (_h2);
							}
							else {
								self.textos.append (self.target.find ('>.content').append ('<h2>{}</h2>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get img () {return __get__ (this, function (self, url, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var i = $ ("<img url='{}'>".format (url));
							self.target.find ('>.content').append (i);
							if (estilos != null) {
								i.css (estilos);
							}
						});},
						get b () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('\n');
							if (self._update) {
								var _b = $ ('<b>{}</b>'.repeat (len (lcadena)).format.apply (null, lcadena));
								if (estilos != null) {
									_b.css (estilos);
								}
								self.target.find ('>.content').append (b);
							}
							else {
								self.textos.append (self.target.find ('>.content').append ('<b>{}</b>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get span () {return __get__ (this, function (self, cadena, estilos) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							var lcadena = cadena.py_split ('\n');
							if (self._update) {
								var _span = '<span>{}</span>'.repeat (len (lcadena)).format.apply (null, lcadena);
								if (estilos != null) {
									_span.css (estilos);
								}
								self.target.find ('>.content').append (_span);
							}
							else {
								self.textos.append (self.target.find ('>.content').append ('<span>{}</span>'.repeat (len (lcadena)).format.apply (null, lcadena)));
							}
						});},
						get lista () {return __get__ (this, function (self, lista, estilos, py_selector) {
							if (typeof estilos == 'undefined' || (estilos != null && estilos .hasOwnProperty ("__kwargtrans__"))) {;
								var estilos = null;
							};
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = null;
							};
							var listar = function (l) {
								var cad = '<ul>';
								var __iterable0__ = l;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (py_typeof (elem) != list) {
										cad += '<li>{}</li>'.format (elem);
									}
									else {
										cad += '<li>{}</li>'.format (listar (elem));
									}
								}
								cad += '</ul>';
								return cad;
							};
							var l = $ (listar (lista));
							self.target.find ('>.content').append (l);
							if (estilos != null && py_selector != null) {
								l.find (py_selector).css (estilos);
							}
							else if (estilos != null && py_selector == null) {
								l.css (estilos);
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self._titulo]);
							self.__update__ ();
							self.__titulo = self.target.find ('>.titulo');
							self.__content = self.target.find ('>.content');
							self.__titulo.text (self._titulo);
							var __iterable0__ = self.textos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.target.find ('>.content').append (elem);
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BoxText = BoxText;
						__all__.Component = Component;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
