	__nest__ (
		__all__,
		'CheckBoxList', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'CheckBoxList';
					var Widget = __init__ (__world__.Widget).Widget;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var CheckBoxList = __class__ ('CheckBoxList', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<h5>{}</h5>\n\t\t<div class='list'></div>\n\t\t";
							self.value = list ([]);
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.list');
							});
						});},
						get add () {return __get__ (this, function (self, target) {
							if (self._update) {
								target.py_update ();
								self.content (self).append (target.target);
							}
							else {
								self.children.append (target);
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo]);
							self.__update__ ();
							if (len (self.value) != 0 && len (self.children) == 0) {
								if (py_typeof (self.value) == list) {
									var __iterable0__ = self.value;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										var opcion = elem [0] + (len (elem) == 3 ? ('<span>' + elem [2]) + '</span>' : '');
										var w = CheckBox (opcion);
										w.value = elem [1];
										w.py_update ();
										self.content (self).append (w.target);
									}
								}
								else if (py_typeof (self.value) == dict) {
									var __iterable0__ = self.value;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										var w = CheckBox (elem);
										w.value = self.value [elem];
										w.py_update ();
										self.content (self).append (w.target);
									}
								}
							}
						});}
					});
					__pragma__ ('<use>' +
						'CheckBox' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.CheckBoxList = CheckBoxList;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
