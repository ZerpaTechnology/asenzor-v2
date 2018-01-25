	(function () {
		var __name__ = '__main__';
		var VAR = nuclear.VAR;
		var config = window.config;
		var normalizar = nuclear.normalizar;
		var zjoin = nuclear.zjoin;
		var rest = window.rest;
		var Component = nuclear.Component;
		var data = $.extend (dict ({}), rest);
		data ['ajax-data'] = VAR ('ajax-data');
		data ['baseAction'] = VAR ('baseAction');
		data ['titulo'] = VAR ('titulo');
		data ['filtrar'] = VAR ('filtrar');
		data ['acciones'] = VAR ('acciones');
		data ['addNew'] = VAR ('addNew');
		data ['n-pag'] = VAR ('n-pag');
		data ['table-headers'] = VAR ('table-headers');
		data ['pag'] = VAR ('pag');
		data ['status'] = VAR ('status');
		data ['filtros'] = VAR ('filtros');
		data ['keyNew'] = VAR ('keyNew');
		data ['campos'] = VAR ('campos');
		var doc = '';
		print (data ['table-headers']);
		var tabla = $ ('#tabla-1');
		var pag = 1;
		var status = 'Todos';
		var respuesta = '';
		var update_tabla = function (pag) {
			var tabla = document ['tabla-1'];
			tabla.py_clear ();
		};
		var paginar = function (x, y) {
			var a = float (x) / float (y);
			if (a > int (a)) {
				return int (a) + 1;
			}
			else {
				return int (a);
			}
		};
		var opciones = list ([]);
		var action_current = list ([0]);
		var Tabla = __class__ ('Tabla', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, py_selector, pag, paginacion) {
				if (typeof pag == 'undefined' || (pag != null && pag .hasOwnProperty ("__kwargtrans__"))) {;
					var pag = 1;
				};
				if (typeof paginacion == 'undefined' || (paginacion != null && paginacion .hasOwnProperty ("__kwargtrans__"))) {;
					var paginacion = 5;
				};
				self.py_selector = py_selector;
				self.lista = VAR ('listar');
				print (self.lista [0]);
				self.listaTemp = $.extend (list ([]), self.lista);
				self.pag = pag;
				self.paginacion = paginacion;
				self.contenido = Component ('tabla-contenido', data, true, true, true);
				self.btns_aplicar = $ (self.py_selector).find ('.btn-aplicar').bind ('click', self.checkear);
				$ (self.py_selector).find ('.link-status').bind ('click', self.filtrar);
				$ (self.py_selector).find ('.table-firt').bind ('click', self.goFirst);
				$ (self.py_selector).find ('.table-next').bind ('click', self.goNext);
				$ (self.py_selector).find ('.table-back').bind ('click', self.goBack);
				$ (self.py_selector).find ('.table-last').bind ('click', self.goLast);
				$ (self.py_selector).find ('.table-actions').bind ('change', self.accionar);
				$ (self.py_selector).find ("input[name='table-search']").bind ('keyup', self.search);
				var __iterable0__ = $ (self.py_selector).find ('.content') [0].children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var tabla = __iterable0__ [__index0__];
					var __iterable1__ = list (tabla.children [0].children [0].children);
					for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
						var th = __iterable1__ [__index1__];
						$ (th.children [0].children [0]).bind ('click', self.marcar);
					}
				}
			});},
			get accionar () {return __get__ (this, function (self, ev) {
				var rank = list (data ['acciones'].py_keys ()).index (ev.target.value);
				if (rank == 0) {
					self.marcar ();
				}
				else {
					var key = list (data ['acciones'].py_keys ()) [list (data ['acciones'].py_keys ()).index (ev.target.value)];
					action_current = list ([data ['acciones'] [key]]);
				}
			});},
			get marcar () {return __get__ (this, function (self, evt) {
				if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
					var evt = null;
				};
				if (evt == null) {
					var __iterable0__ = $ (self.py_selector).find ('.content') [0].children;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var tabla = __iterable0__ [__index0__];
						if (!__in__ ('hidden', tabla.class_name)) {
							var tabla = tabla.children [0];
							var __iterable1__ = list (tabla.children [0].children).__getslice__ (1, null, 1);
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var tr = __iterable1__ [__index1__];
								tr.children [0].children [0].checked = true;
							}
						}
					}
				}
				else if (evt.target.checked == true) {
					var __iterable0__ = $ (self.py_selector).find ('.content') [0].children;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var tabla = __iterable0__ [__index0__];
						if (!__in__ ('hidden', tabla.class_name)) {
							var tabla = tabla.children [0];
							var __iterable1__ = list (tabla.children [0].children).__getslice__ (1, null, 1);
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var tr = __iterable1__ [__index1__];
								tr.children [0].children [0].checked = true;
							}
						}
					}
				}
				else {
					var __iterable0__ = $ (self.py_selector).find ('.content') [0].children;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var tabla = __iterable0__ [__index0__];
						if (!__in__ ('hidden', tabla.class_name)) {
							var tabla = tabla.children [0];
							var __iterable1__ = list (tabla.children [0].children).__getslice__ (1, null, 1);
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var tr = __iterable1__ [__index1__];
								tr.children [0].children [0].checked = false;
							}
						}
					}
				}
			});},
			get goBack () {return __get__ (this, function (self, evt) {
				if (self.pag > 1) {
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).addClass ('hidden');
					self.pag--;
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).removeClass ('hidden');
					self.update_indice ();
				}
			});},
			get update_indice () {return __get__ (this, function (self) {
				var __iterable0__ = $ (self.py_selector).find ("input[name='table-indice']");
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					elem.value = self.pag;
				}
				var __iterable0__ = $ (self.py_selector).find ("span[name='from-indice']");
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					elem.text = str (Math.floor (len (self.listaTemp) / self.paginacion) + 1);
				}
			});},
			get update_tabla () {return __get__ (this, function (self) {
				var decode = Codificador.Codificador.decode;
				data ['listar'] = self.listaTemp;
				$ (self.py_selector).find ('.content') [0].outerHTML = self.contenido.run (data);
				self.pag = 1;
				self.update_indice ();
				var __iterable0__ = $ (self.py_selector).find ('.content') [0].children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var tabla = __iterable0__ [__index0__];
					var __iterable1__ = list (tabla.children [0].children [0].children);
					for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
						var th = __iterable1__ [__index1__];
						$ (th.children [0].children [0]).bind ('click', self.marcar);
					}
				}
			});},
			get goLast () {return __get__ (this, function (self, evt) {
				if (self.pag < paginar (len (self.listaTemp), self.paginacion)) {
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).addClass ('hidden');
					self.pag = paginar (len (self.listaTemp), self.paginacion);
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).removeClass ('hidden');
					self.update_indice ();
				}
			});},
			get goNext () {return __get__ (this, function (self, evt) {
				if (self.pag < len (self.listaTemp) / self.paginacion) {
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).addClass ('hidden');
					self.pag++;
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).removeClass ('hidden');
					self.update_indice ();
				}
			});},
			get goFirst () {return __get__ (this, function (self, evt) {
				if (self.pag > 1) {
					$ ($ (self.py_selector).find ('.content') [0].children [self.pag - 1]).addClass ('hidden');
					self.pag = 1;
					$ ($ (self.py_selector).find ('.content') [0].children [0]).removeClass ('hidden');
					self.update_indice ();
				}
			});},
			get filtrar () {return __get__ (this, function (self, evt) {
				evt.preventDefault ();
				var status = evt.target.text;
				self.update_tabla ();
			});},
			get checkear () {return __get__ (this, function (self, evt) {
				var c = 0;
				var opciones = list ([]);
				var enlaces = list ([]);
				var pag = int ($ ("input[name='table-indice']") [0].value);
				var __iterable0__ = $ (self.py_selector).find ('.content') [0].children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var tabla = __iterable0__ [__index0__];
					var tabla = tabla.children [0];
					var __iterable1__ = list (tabla.children [0].children).__getslice__ (1, null, 1);
					for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
						var tr = __iterable1__ [__index1__];
						opciones.append (tr.children [0].children [0].checked);
						if (tr.children [0].children [0].checked == true) {
							enlaces.append (tr.children [1].children [0].href);
						}
						else {
							enlaces.append (null);
						}
					}
				}
				req.set_header ('content-type', 'application/x-www-form-urlencoded');
				if (action_current [0] != 'editar') {
					// pass;
					$.ajax (dict ({'url': config.base_url, 'data': dict ({'marcados': opciones, 'action': action_current [0], 'metodo': rest ['metodo'], 'app': rest ['app'], 'control': rest ['control'], 'ajax': true}), 'method': 'POST', 'type': 'POST', 'contentType': false, 'processData': false}));
					var obtenerLista = function (data) {
						self.listar = normalizar (data);
					};
					$.post ((((((config.base_url + rest ['app']) + '/') + rest ['control']) + '/') + rest ['metodo']) + '/action=listar&ajax=True/').done (obtenerLista);
					self.listaTemp = $.extend (list ([]), self.lista);
					self.update_tabla ();
				}
				else {
					var __iterable0__ = enumerate (opciones);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var opcion = __left0__ [1];
						if (opcion == true) {
							window.open (enlaces [k]);
						}
					}
				}
			});},
			get search () {return __get__ (this, function (self, evt) {
				if (evt.target.value != '') {
					var c = 0;
					self.listaTemp = $.extend (list ([]), self.lista);
					var __iterable0__ = self.lista;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if (!__in__ (evt.target.value.lower (), elem [0].lower ())) {
							self.listaTemp.remove (elem);
							c++;
						}
					}
				}
				else {
					self.listaTemp = $.extend (list ([]), self.lista);
				}
				var __iterable0__ = $ (self.py_selector).find ('.table-pag');
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					elem.value = 1;
				}
				self.update_tabla ();
			});}
		});
		window.Tabla = Tabla;
		__pragma__ ('<all>')
			__all__.Component = Component;
			__all__.Tabla = Tabla;
			__all__.VAR = VAR;
			__all__.__name__ = __name__;
			__all__.action_current = action_current;
			__all__.config = config;
			__all__.data = data;
			__all__.doc = doc;
			__all__.normalizar = normalizar;
			__all__.opciones = opciones;
			__all__.pag = pag;
			__all__.paginar = paginar;
			__all__.respuesta = respuesta;
			__all__.rest = rest;
			__all__.status = status;
			__all__.tabla = tabla;
			__all__.update_tabla = update_tabla;
			__all__.zjoin = zjoin;
		__pragma__ ('</all>')
	}) ();
