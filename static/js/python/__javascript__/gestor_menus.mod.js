	(function () {
		var __name__ = '__main__';
		var var_update = '\n$( "#accordion" ).accordion({\n  collapsible: true\n});\n$( ".accordion" ).accordion({\n  collapsible: true,\n  active:false\n});\n$( "ul.droptrue" ).sortable({\nconnectWith: "ul"\n});\n$( "ul.dropfalse" ).sortable({\nconnectWith: "ul",\ndropOnEmpty: false\n});\n$( ".sortable" ).disableSelection();\n\n';
		var config = Config.Config ();
		var normalizar = nuclear.normalizar;
		var rest = nuclear.getRest ();
		var VAR = nuclear.VAR;
		var render = function (menu) {
			var cadena = '';
			var __iterable0__ = menu;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				cadena += elem ['name'] + '\n';
				if (elem ['children'] != list ([])) {
					cadena += (' ' + render (elem ['children'])) + '\n';
				}
			}
			return cadena;
		};
		var Gestor = __class__ ('Gestor', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, py_selector) {
				self.py_selector = py_selector;
				self.rest = nuclear.getRest ();
				self.nombre = null;
				self.menus = VAR ('Menus');
				self.nuevo = null;
				var select_menu = function (evt, menu) {
					if (typeof menu == 'undefined' || (menu != null && menu .hasOwnProperty ("__kwargtrans__"))) {;
						var menu = null;
					};
					var mapear = function (menu) {
						var mapa = '';
						var __iterable0__ = menu;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							mapa += ((((((((((((((((((('<li><li class="ui-state-default" >' + '\n\t\t\t\t\t<div class="accordion" style="display: inline-block;width: 100%">\n\t\t\t\t\t\t<h3 ><span>') + elem ['name']) + '</span></h3>\n\t\t\t\t\t\t<div class="pad-1" style="max-height: 120px">\n\t\t\t\t\t\t\t<b class="d-block">Etiqueta de navegación</b>\n\t\t\t\t\t\t\t<input type="" name="nombre" placeholder="" value=\'') + elem ['name']) + '\'>\n\t\t\t\t\t\t\t<div>Enlace:<span name="url">') + construir (elem ['url'])) + "</span></div>\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t    <input type='hidden' name='modelo' value='") + (py_typeof ('url') == list ? elem ['url'] [0] : '')) + "'>\n\t\t\t\t\t\t    <input type='hidden' name='tabla' value='") + (py_typeof ('url') == list ? elem ['url'] [1] : '')) + "'>\n\t\t\t\t\t\t    <input type='hidden' name='indice' value='") + (py_typeof ('url') == list ? elem ['url'] [2] : '')) + "'>\n\t\t\t\t\t\t    <input type='hidden' name='control' value='") + (py_typeof ('url') == list ? elem ['url'] [3] : '')) + "'>\n\t\t\t\t\t\t    <input type='hidden' name='metodo' value='") + (py_typeof ('url') == list ? elem ['url'] [4] : '')) + '\'>\n\t\t\t\t\t\t\t<div><b>Mover a:</b><span class="blue">Abajo</span></div>\n\t\t\t\t\t\t\t<div>Original: Inicio</div>\n\t\t\t\t\t\t\t<div><b class="red">eliminar</b>|<b class="blue">Cancelar</b></div>\n\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t') + '<ul  class="sortable droptrue marg-l2" style="min-height: 5px">') + mapear (elem ['children'])) + '</ul></li>';
						}
						mapa += '</li>';
						return mapa;
					};
					if (menu == null) {
						var __iterable0__ = enumerate ($ ("select[name='seleccionar-menu']") [0].children);
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var k = __left0__ [0];
							var option = __left0__ [1];
							if (option.selected) {
								$ (self.py_selector) [0].innerHTML = mapear (self.menus [k - 1] [1] [0]);
								var __iterable1__ = self.menus [k - 1] [1] [1];
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var elem = __iterable1__ [__index1__];
									if (elem == 'nivel-superior') {
										$ ("input[name='nivel-superior']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-principal') {
										$ ("input[name='menu-principal']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-pie') {
										$ ("input[name='menu-pie']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-barra-superior') {
										$ ("input[name='menu-barra-superior']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-mi-cuenta') {
										$ ("input[name='menu-mi-cuenta']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
								}
								eval (var_update);
								self.nombre = self.menus [k - 1] [0];
								self.nuevo = k - 1;
								break;
							}
						}
					}
					else {
						$ (self.py_selector) [0].innerHTML = mapear (self.menus [menu] [1] [0]);
						var __iterable0__ = enumerate ($ ("select[name='seleccionar-menu']") [0].children);
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var k = __left0__ [0];
							var option = __left0__ [1];
							if (k - 1 == menu) {
								option.selected = true;
								self.nombre = self.menus [k - 1] [0];
								self.nuevo = k - 1;
								var __iterable1__ = self.menus [k - 1] [1] [1];
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var elem = __iterable1__ [__index1__];
									if (elem == 'nivel-superior') {
										$ ("input[name='nivel-superior']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-principal') {
										$ ("input[name='menu-principal']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-pie') {
										$ ("input[name='menu-pie']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-barra-superior') {
										$ ("input[name='menu-barra-superior']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
									if (elem == 'menu-mi-cuenta') {
										$ ("input[name='menu-mi-cuenta']") [0].checked = self.menus [k - 1] [1] [1] [elem];
									}
								}
							}
						}
					}
					eval (var_update);
					$ (self.py_selector + " input[name='nombre']").bind ('keyup', escribir);
				};
				var clear_flechas = function () {
					var __iterable0__ = $ ('.accordion > H3');
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						var cantidad = $ (elem).find ('.ui-accordion-header-icon');
						var padre = cantidad [0].parentNode;
						while (len (cantidad) > 1) {
							padre.removeChild (cantidad [-(1)]);
							cantidad.py_pop ();
						}
					}
				};
				var construir = function (url) {
					if (py_typeof (url) == list) {
						return ((config.base_url + self.rest ['app']) + (url [3] != '' ? '/' + url [3] : '')) + (url [4] != '' ? '/' + url [4] : '');
					}
					else {
						return url;
					}
				};
				var add_to_menu = function (evt) {
					var caja = $ ($ (evt.target).prev ()).prev () [0];
					var etiquetas = list ([]);
					var __iterable0__ = caja.children;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if ($ (elem).find ("input[type='checkbox']") [0].checked == true) {
							etiquetas.append ($ (elem).find ('b') [0]);
						}
					}
					var __iterable0__ = etiquetas;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						$ (self.py_selector) [0].innerHTML += ((((((((((((((((('<li><li class="ui-state-default" >' + '\n\t\t\t\t<div class="accordion" style="display: inline-block;width: 100%">\n\t\t\t\t<h3 ><span>') + elem.text) + '</span></h3>\n\t\t\t\t<div class="pad-1" style="max-height: 120px">\n\t\t\t\t\t<b class="d-block">Etiqueta de navegación</b>\n\t\t\t\t\t<input type="" name="nombre" placeholder="" value=\'') + elem.text) + '\'>\n\t\t\t\t\t<div>Enlace:<span name="url">') + elem.getAttribute ('href')) + "</span></div>\n\t\t\t\t\t\n\t\t\t\t\t<input type='hidden' name='modelo' value='") + elem.getAttribute ('modelo')) + "'>\n\t\t\t\t\t<input type='hidden' name='tabla' value='") + elem.getAttribute ('tabla')) + "'>\n\t\t\t\t\t<input type='hidden' name='indice' value='") + elem.getAttribute ('indice')) + "'>\n\t\t\t\t\t<input type='hidden' name='control' value='") + elem.getAttribute ('control')) + "'>\n\t\t\t\t\t<input type='hidden' name='metodo' value='") + elem.getAttribute ('metodo')) + '\'>\n\n\t\t\t\t\t<div><b>Mover a:</b><span class="blue">Abajo</span></div>\n\t\t\t\t\t<div>Original: Inicio</div>\n\t\t\t\t\t<div><b class="red">eliminar</b>|<b class="blue">Cancelar</b></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div></div>\n\t\t\t\t') + '<ul  class="sortable droptrue marg-l2" style="min-height: 5px"></ul></li></li>';
					}
					eval (var_update);
					clear_flechas ();
					$ (self.py_selector + " input[name='nombre']").bind ('keyup', escribir);
				};
				var add_to_menu2 = function (evt) {
					var text = $ (evt.target).prev ().find ("input[name='custom-text']") [0];
					var url = $ (evt.target).prev ().find ("input[name='custom-url']") [0];
					$ (self.py_selector) [0].innerHTML += ((((((('<li><li class="ui-state-default" >' + '\n\t\t\t\t<div class="accordion" style="display: inline-block;width: 100%">\n\t\t\t\t<h3 ><span>') + text.value) + '</span></h3>\n\t\t\t\t<div class="pad-1" style="max-height: 120px">\n\t\t\t\t\t<b class="d-block">Etiqueta de navegación</b>\n\t\t\t\t\t<input type="" name="nombre" placeholder="" value=\'') + text.value) + '\'>\n\t\t\t\t\t<div>Enlace:<span name="url">') + url.value) + '</span></div>\n\t\t\t\t\t\n\t\t\t\t\t<input type=\'hidden\' name=\'modelo\' value=\'\'>\n\t\t\t\t\t<input type=\'hidden\' name=\'tabla\' value=\'\'>\n\t\t\t\t\t<input type=\'hidden\' name=\'indice\' value=\'\'>\n\t\t\t\t\t<input type=\'hidden\' name=\'control\' value=\'\'>\n\t\t\t\t\t<input type=\'hidden\' name=\'metodo\' value=\'\'>\n\n\t\t\t\t\t\n\t\t\t\t\t<div><b>Mover a:</b><span class="blue">Abajo</span></div>\n\t\t\t\t\t<div>Original: Inicio</div>\n\t\t\t\t\t<div><b class="red">eliminar</b>|<b class="blue">Cancelar</b></div>\n\t\t\t\t\t</div>\n\t\t\t\t</div></div>\n\t\t\t\t') + '<ul  class="sortable droptrue marg-l2" style="min-height: 5px"></ul></li></li>';
					window.eval (var_update);
				};
				var select_all = function (evt) {
					var caja = $ (evt.target).previousSibling.children [0].children;
					var __iterable0__ = caja;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						elem.children [0].checked = true;
					}
				};
				var save_menu = function (evt) {
					var mapear = function (menu) {
						var l = list ([]);
						var __iterable0__ = menu.children;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (len (elem.children) > 0) {
								var nombre = elem.children [0].children [1].find ("input[name='nombre']") [0].value;
								if (elem.children [0].children [1].find ("input[name='tabla']") [0].value.strip () != '' || elem.children [0].children [1].find ("input[name='modelo']") [0].value.strip () != '' || elem.children [0].children [1].find ("input[name='indice']") [0].value.strip () != '' || elem.children [0].children [1].find ("input[name='control']") [0].value.strip () != '' || elem.children [0].children [1].find ("input[name='metodo']") [0].value.strip () != '') {
									var url = list ([normalizar (elem.children [0].children [1].find ("input[name='modelo']") [0].value.strip ()), normalizar (elem.children [0].children [1].find ("input[name='tabla']") [0].value.strip ()), normalizar (elem.children [0].children [1].find ("input[name='indice']") [0].value.strip ()), normalizar (elem.children [0].children [1].find ("input[name='control']") [0].value.strip ()), elem.children [0].children [1].find ("input[name='metodo']") [0].value.strip ()]);
								}
								else {
									var url = elem.children [0].children [1].find ("span[name='url']") [0].text;
								}
								l.append (dict ({'name': nombre, 'url': url, 'children': mapear (elem.children [1])}));
							}
						}
						return l;
					};
					var estructura = list ([mapear ($ ('#nav-menu') [0])]);
					estructura.append (dict ({'nivel-superior': $ ("input[name='nivel-superior']") [0].checked, 'menu-principal': $ ("input[name='menu-principal']") [0].checked, 'menu-pie': $ ("input[name='menu-pie']") [0].checked, 'menu-barra-superior': $ ("input[name='menu-barra-superior']") [0].checked, 'menu-mi-cuenta': $ ("input[name='menu-mi-cuenta']") [0].checked}));
					if ($ ("input[name='nombre-menu']") [0].value.strip () != '') {
						self.nombre = $ ("input[name='nombre-menu']") [0].value.strip ();
					}
					if (self.nombre != null) {
						var data = dict ({'app': self.rest ['app'], 'metodo': self.rest ['metodo'], 'action': 'save-menu', 'control': self.rest ['control'], 'menu': str (estructura), 'nombre': self.nombre, 'nuevo': self.nuevo});
						$.ajax (dict ({'data': data, 'url': config.base_url, 'method': 'POST'})).done ((function __lambda__ (data) {
							return tuple ([alert (data), print ('================\n'), print (data)]);
						}));
					}
					else {
						alert ('debes darle nombre al menu');
					}
				};
				var escribir = function (evt) {
					evt.target.parentNode.parentNode.children [0].children [1].text = evt.target.value;
				};
				$ ("button[name='add-to-menu']").bind ('click', add_to_menu);
				$ ("button[name='add-to-menu2']").bind ('click', add_to_menu2);
				$ ("span[name='seleccionar-todo']").bind ('click', select_all);
				$ ("button[name='guardar-menu']").bind ('click', save_menu);
				$ ("button[name='aplicar-menu']").bind ('click', select_menu);
			});}
		});
		window.Gestor = Gestor;
		__pragma__ ('<all>')
			__all__.Gestor = Gestor;
			__all__.VAR = VAR;
			__all__.__name__ = __name__;
			__all__.config = config;
			__all__.normalizar = normalizar;
			__all__.render = render;
			__all__.rest = rest;
			__all__.var_update = var_update;
		__pragma__ ('</all>')
	}) ();
