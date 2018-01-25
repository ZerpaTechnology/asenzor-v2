	(function () {
		var __name__ = '__main__';
		var list = py_datos.list;
		var py_metatype = py_datos.py_metatype;
		var codeEditor = '\nelem=document.getElementsByClassName("codeEditor")[document.getElementsByClassName("codeEditor").length-1]\neditor = CodeMirror.fromTextArea(elem, {\n    lineNumbers: true,\n    mode: mixedMode,\n    keyMap: "sublime",\n    autoCloseBrackets: true,\n    matchBrackets: true,\n    showCursorWhenSelecting: true,\n    theme: "monokai",\n    tabSize: 2,\n    selectionPointer: true\n  });\nemmetCodeMirror(editor);\neditores.push(editor);\n';
		var config = Config.Config ();
		var decode = Codificador.Codificador.decode;
		var rest = nuclear.getRest ();
		var normalizar = nuclear.normalizar;
		if (__in__ ('action', rest) && 'codear' == rest ['action']) {
			$ ('#alert').removeClass ('hidden');
		}
		if (list (rest ['kwargs']) [0] == 'Diseño') {
			$ ('#alert').html ('\n  <div class="pad-1" style="z-index:100">\n  <span id="alert-close">x</span>\n  <h1>Nombre</h1>\n  <input type="text" name="nombre" id="nombre" style="width:100%">\n  </div>\n  \n  <div class="pad-1 d-inline-block">\n  <label>Usuario</label>\n  <select name="user" id="user">\n   <option>admin</option>\n   <option>user</option>\n  </select>\n  </div>\n  <div class="pad-1 d-inline-block">\n  <label>Diseño</label>\n  <select name="opcion" id="widget">\n   <option>Template</option>\n   <option>Widget</option>\n  </select>\n  </div>\n  \n  <div class="text-center marg-t5">\n  <button id="crear" class="white bg-blue pad-05">Crear</button>\n  </div>\n  \n  ');
		}
		else if (list (rest ['kwargs']) [0] == 'Controlador' || list (rest ['kwargs']) [0] == 'Modelo') {
			$ ('#alert').html ('\n  <div class="pad-1" style="z-index:100">\n  <span id="alert-close">x</span>\n  <h1>Nombre</h1>\n  <input type="text" name="nombre" id="nombre" style="width:100%">\n  </div>\n  <div class="text-center marg-t5">\n  <button id="crear" class="white bg-blue pad-05">Crear</button>\n  </div>\n  \n  ');
		}
		$ ('#alert').css (dict ({'background-color': 'white', 'width': '300px', 'height': '300px', 'margin-left': str (window.innerWidth / 2 - 150) + 'px', 'margin-top': str (window.innerHeight / 2 - 150) + 'px', 'top': str (-($ ('#alert') [0].clientHeight) / 2) + 'px', 'left': str (-($ ('#alert') [0].clientWidth) / 2) + 'px', 'border': 'solid'}));
		var valores = list ([]);
		var _lambda = function (evt) {
			var __iterable0__ = enumerate (evt.target.parentNode.children);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				if (elem == evt.target) {
					if (!($ (evt.target.parentNode.children [k + 1]).hasClass ('hidden'))) {
						$ (evt.target.parentNode.children [k + 1]).addClass ('hidden');
					}
					else {
						$ (evt.target.parentNode.children [k + 1]).removeClass ('hidden');
					}
				}
			}
		};
		$ ('.folderclass').bind ('click', _lambda);
		var borrar = function (evt) {
			var __iterable0__ = enumerate ($ ('.tab'));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				if (!($ (elem).hasClass ('hidden'))) {
					break;
				}
			}
			if ($ ('.path') [k].innerHTML != '') {
				$.post (config.base_url, dict ({'manager': true, 'control': 'admin', 'metodo': 'delete', 'kwargs': dict ({'path': $ ('.path') [k].innerHTML})})).done ((function __lambda__ (data) {
					return window.alert (data);
				}));
				$ ('#tabs-btn') [0].removeChild ($ ('#tabs-btn') [0].children [k]);
				$ ('.tab') [k].parentNode.removeChild ($ ('.tab') [k]);
				window.editores.splice(k,1)
			}
			if (len ($ ('.tab')) == 0 && $ ('#borrar').children () != list ([])) {
				$ ('#guardar') [0].parentNode.removeChild ($ ('#borrar') [0]);
			}
			if (len ($ ('.tab')) == 0) {
				$ ('#guardar') [0].parentNode.removeChild ($ ('#guardar') [0]);
			}
			if (len ($ ('.tab')) > 0 && k != 0) {
				$ ($ ('.tab') [len ($ ('.tab')) - 1]).removeClass ('hidden');
			}
			else if (len ($ ('.tab')) > 0 && k == 0) {
				$ ($ ('.tab') [0]).removeClass ('hidden');
			}
		};
		var py_update = function () {
			var cerrar = function (evt) {
				var __iterable0__ = enumerate ($ ('.close-btn'));
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var elem = __left0__ [1];
					if (elem == evt.target) {
						$ ('#tabs-btn') [0].removeChild (evt.target.parentNode);
						$ ('.tab') [k].parentNode.removeChild ($ ('.tab') [k]);
						window.editores.splice(k,1)
						if (len ($ ('.tab')) > 0) {
							$ ($ ('.tab') [k - 1]).removeClass ('hidden');
						}
					}
				}
				if (len ($ ('.tab-btn')) == 0 && $ ('#borrar') != list ([])) {
					$ ('#guardar') [0].parentNode.removeChild ($ ('#borrar') [0]);
				}
				if (len ($ ('.tab-btn')) == 0) {
					$ ('#guardar') [0].parentNode.removeChild ($ ('#guardar') [0]);
				}
			};
			var mover = function (evt) {
				var __iterable0__ = enumerate ($ ('.tab-btn'));
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var elem = __left0__ [1];
					if (elem == evt.target) {
						break;
					}
				}
				var __iterable0__ = enumerate ($ ('.tab'));
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k2 = __left0__ [0];
					var elem = __left0__ [1];
					if (k2 != k) {
						$ (elem).addClass ('hidden');
					}
					else {
						$ (elem).removeClass ('hidden');
					}
				}
			};
			var guardar = function (evt) {
				$.post (config.base_url, dict ({'app': rest ['app'], 'metodo': 'write', 'control': 'admin', 'kwargs': dict ({'path': $ ('.path') [k].text}), 'file': window.editores [k].getDoc ().getValue ()}), (function __lambda__ (data) {
					return window.alert (data);
				}));
				var __iterable0__ = enumerate ($ ('.tab'));
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var tab = __left0__ [1];
					if (!($ (tab).hasClass ('hidden'))) {
						break;
					}
				}
				if (len ($ ('#borrar')) == 0) {
					$ ('#btns-action') [0].innerHTML += "<button id='borrar'>Borrar</button>";
				}
			};
			try {
				$ ('.close-btn').unbind ('click', cerrar);
			}
			catch (__except0__) {
				// pass;
			}
			$ ('.close-btn').bind ('click', cerrar);
			try {
				$ ('#guardar').unbind ('click', guardar);
			}
			catch (__except0__) {
				// pass;
			}
			$ ('#guardar').bind ('click', guardar);
			try {
				$ ('#borrar').unbind ('click', borrar);
			}
			catch (__except0__) {
				// pass;
			}
			$ ('#borrar').bind ('click', borrar);
			try {
				$ ('.tab-btn').unbind ('click', mover);
			}
			catch (__except0__) {
				// pass;
			}
			$ ('.tab-btn').bind ('click', mover);
			if (len (window.editores) == len ($ ('.tab')) - 1) {
				window.eval (codeEditor);
			}
		};
		var guardar = function (evt) {
			var __iterable0__ = enumerate ($ ('.tab'));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				if (!($ (elem).hasClass ('hidden'))) {
					break;
				}
			}
			var data = new FormData;
			data.append ('manager', rest ['manager']);
			data.append ('app', rest ['app']);
			data.append ('metodo', 'write');
			data.append ('control', 'admin');
			data.append ('path', $ ('.path') [k].innerText);
			data.append ('file', str (window.editores [k].getDoc ().getValue ()));
			$.ajax (dict ({'url': config.base_url, 'data': data, 'cache': false, 'contentType': false, 'processData': false, 'type': 'POST', 'method': 'POST', 'success': (function __lambda__ (data) {
				return window.alert (data);
			})}));
			var __iterable0__ = enumerate ($ ('.tab'));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var tab = __left0__ [1];
				if (!($ (tab).hasClass ('hidden'))) {
					break;
				}
			}
			if ($ ('#borrar') == list ([])) {
				$ ('#btns-action') [0].innerHTML += "<button id='borrar'>Borrar</button>";
			}
			py_update ();
		};
		window.shortcut.add ('Ctrl+s', guardar);
		var crear = function (evt) {
			var show = function (data) {
				if (data.endswith ('/') || data.endswith ('\\')) {
					var ruta = data.strip ();
				}
				else {
					var ruta = data.strip () + '/';
				}
				if (len ($ ('.path')) == 1) {
					if ($ ('.path') [0].innerText.strip () == '') {
						if (list (rest ['kwargs']) [0] == 'Diseño') {
							$ ('.path') [0].innerHTML = (ruta + $ ('#nombre') [0].value) + '.html';
						}
						else if (list (rest ['kwargs']) [0] == 'Controlador' || list (rest ['kwargs']) [0] == 'Modelo') {
							$ ('.path') [0].innerHTML = (ruta + $ ('#nombre') [0].value) + '.py';
						}
						else {
							$ ('.path') [0].innerHTML = ruta + $ ('#nombre') [0].value;
						}
						$ ('.tab-btn') [0].innerHTML = $ ('#nombre') [0].value;
						if ($ ('#guardar') == list ([])) {
							$ ('#btns-action') [0].innerHTML += '<button class="bg-blue white" id="guardar">Guardar</button>';
						}
						$ ('#guardar') [0].parentNode.innerHTML += "<button id='borrar'>Borrar</button>";
					}
					else {
						if ($ ('#guardar') == list ([])) {
							$ ('#btns-action') [0].innerHTML += '<button class="bg-blue white" id="guardar">Guardar</button>';
						}
						$ ('#tabs-btn') [0].innerHTML += ('<span style="padding:2px"><button class="tab-btn">' + $ ('#nombre') [0].value) + '</button><button class="close-btn">x</button></span>';
						var __iterable0__ = enumerate ($ ('.tab'));
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var __left0__ = __iterable0__ [__index0__];
							var k = __left0__ [0];
							var elem = __left0__ [1];
							$ (elem).addClass ('hidden');
							// pass;
						}
						$ ('#content2') [0].children [len ($ ('.tab'))].innerHTML += ('<div class="tab"><div class="path" style="overflow-x:scroll">' + ruta) + '</div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>';
						if (list (rest ['kwargs']) [0] == 'Diseño') {
							$ ('.path') [k + 1].innerHTML = (ruta + $ ('#nombre') [0].value) + '.html';
						}
						else if (list (rest ['kwargs']) [0] == 'Controlador' || list (rest ['kwargs']) [0] == 'Modelo') {
							$ ('.path') [k + 1].innerHTML = (ruta + $ ('#nombre') [0].value) + '.py';
						}
						else {
							$ ('.path') [k + 1].innerHTML = ruta + $ ('#nombre') [0].value;
						}
					}
				}
				else {
					$ ('#tabs-btn') [0].innerHTML += ('<span style="padding:2px"><button class="tab-btn">' + $ ('#nombre') [0].value) + '</button><button class="close-btn">x</button></span>';
					var __iterable0__ = enumerate ($ ('.tab'));
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						$ (elem).addClass ('hidden');
					}
					$ ('#content2') [0].children [len ($ ('.tab'))].innerHTML += ('<div class="tab"><div class="path" style="overflow-x:scroll">' + ruta) + '</div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>';
					if ($ ('#guardar') == list ([])) {
						$ ('#btns-action') [0].innerHTML += '<button class="bg-blue white" id="guardar">Guardar</button>';
					}
					var k = 0;
					var __iterable0__ = enumerate ($ ('.tab'));
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						if (!($ (elem).hasClass ('hidden'))) {
							break;
						}
					}
					if (list (rest ['kwargs']) [0] == 'Diseño') {
						$ ('.path') [k].innerHTML = (ruta + $ ('#nombre') [0].value) + '.html';
					}
					else if (list (rest ['kwargs']) [0] == 'Controlador' || list (rest ['kwargs']) [0] == 'Modelo') {
						$ ('.path') [k].innerHTML = (ruta + $ ('#nombre') [0].value) + '.py';
					}
					else {
						$ ('.path') [k].innerHTML = ruta + $ ('#nombre') [0].value;
					}
				}
				py_update ();
				$ ('#alert').addClass ('hidden');
				$ ('#nombre') [0].value = '';
			};
			if (list (rest ['kwargs']) [0] == 'Diseño') {
				var url = ((((config.base_url + rest ['app']) + '/admin/Show/path/') + ($ ('#user') [0].value == 'user' ? 'user' : 'admin')) + '/') + ($ ('#widget') [0].value == 'Template' ? 'layouts' : 'widgets');
				$.get(url).done(show)
			}
			else if (list (rest ['kwargs']) [0] == 'Controlador') {
				var url = (config.base_url + rest ['app']) + '/admin/Show/path/user/controladores';
				$.get(url).done(show)
			}
			else if (list (rest ['kwargs']) [0] == 'Modelo') {
				var url = (config.base_url + rest ['app']) + '/admin/Show/path/admin/modelos';
				$.get(url).done(show)
			}
		};
		$ ('#crear').bind ('click', crear);
		var navegar = function (target) {
			var path = list ([]);
			while (target.parentNode.tagName == 'UL' || target.parentNode.tagName == 'LI') {
				if ($ (target).hasClass ('fileclass')) {
					path.insert (0, target.innerHTML);
					if ($ (target.parentNode.parentNode.previousSibling).hasClass ('folderclass')) {
						var target = target.parentNode.parentNode.previousSibling;
					}
					else {
						var target = target.parentNode;
					}
				}
				else if ($ (target).hasClass ('folderclass')) {
					path.insert (0, target.innerHTML);
					if ($ (target.parentNode.parentNode.previousSibling).hasClass ('folderclass')) {
						var target = target.parentNode.parentNode.previousSibling;
					}
					else {
						var target = target.parentNode;
					}
				}
				else {
					var target = target.parentNode;
				}
			}
			return path;
		};
		var seleccionar = function (evt) {
			var key = list (rest ['kwargs']);
			var archivo = evt.target.innerText.strip ();
			var path = '/'.join (navegar (evt.target));
			var modo = 'text/plain';
			var __iterable0__ = list (['.html', '.py', '.by', '.zby', '.js', '.css', '.php', '.xml', '.json']);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				if (len (elem) < len (archivo)) {
					if (archivo.__getslice__ (-(len (elem)), null, 1) == '.html') {
						var modo = 'htmlmixed';
						break;
					}
					else if (archivo.__getslice__ (-(len (elem)), null, 1) == '.py' || archivo.__getslice__ (-(len (elem)), null, 1) == '.by' || archivo.__getslice__ (-(len (elem)), null, 1) == '.zby') {
						var modo = 'python';
						break;
					}
					else if (archivo.__getslice__ (-(len (elem)), null, 1) == '.js') {
						var modo = 'javascript';
						break;
					}
					else if (archivo.__getslice__ (-(len (elem)), null, 1) == '.css') {
						var modo = 'text/css';
						break;
					}
					else if (archivo.__getslice__ (-(len (elem)), null, 1) == '.php') {
						var modo = 'php';
						break;
					}
					else if (archivo.__getslice__ (-(len (elem)), null, 1) == '.xml') {
						var modo = 'xml';
						break;
					}
					else if (archivo.__getslice__ (-(len (elem)), null, 1) == '.json') {
						var modo = 'json';
						break;
					}
				}
			}
			var obtenerArchivo = function (data) {
				var archivo = data.py_split ('\n');
				if (len ($ ('.tab')) == 1) {
					var k = 0;
				}
				else {
					var __iterable0__ = enumerate ($ ('.tab'));
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						if (!($ (elem).hasClass ('hidden'))) {
							break;
						}
					}
				}
				$ ('.path') [k].innerHTML = archivo [0];
				window.editores [k].getDoc ().setValue ('\n'.join (archivo.__getslice__ (1, null, 1)));
				window.editores [k].setOption ('mode', modo);
			};
			if (list (normalizar (rest ['kwargs'])) [0] == 'Diseño') {
				var path = 'layout/' + path;
				var url = ((((config.base_url + rest ['app']) + '/') + rest ['control']) + '/Show/') + path;
				$.get(url).done(
				      obtenerArchivo)
			}
			else if (list (rest ['kwargs']) == list (['Controlador'])) {
				var path = 'controlador/' + path;
				$.get(url).done(
				      obtenerArchivo)
			}
			else if (list (rest ['kwargs']) == list (['Modelo'])) {
				var path = 'modelo/' + path;
				$.get(url).done(
				      obtenerArchivo)
			}
			else if (list (rest ['kwargs']) == list (['Script'])) {
				var path = 'static/' + path;
				$.get(url).done(
				      obtenerArchivo)
			}
			else if (list (rest ['kwargs']) == list (['Ajustes'])) {
				var path = 'ajustes/' + path;
				$.get(url).done(
				      obtenerArchivo)
			}
			else if (list (rest ['kwargs']) == list (['Plugin'])) {
				$.get(url).done(
				      obtenerArchivo)
			}
			if (len ($ ('.tab')) == 1 && $ ('.path') [0].innerText == '') {
				var k = 0;
				$ ('.tab-btn') [0].innerText = evt.target.innerText;
				if (len ($ ('#guardar')) == 0) {
					$ ('#btns-action') [0].innerHTML += '<button class="bg-blue white" id="guardar">Guardar</button>';
				}
				$ ('#guardar') [0].parentNode.innerHTML += "<button id='borrar'>Borrar</button>";
			}
			else {
				var __iterable0__ = $ ('.tab');
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					$ (elem).addClass ('hidden');
					// pass;
				}
				var k = len ($ ('.tab'));
				$ ('#tabs-btn') [0].innerHTML += ('<span style="padding:2px"><button class="tab-btn">' + evt.target.innerText) + '</button><button class="close-btn">x</button></span>';
				if (len ($ ('.tab')) > 0) {
					$ ('#content2') [0].children [len ($ ('.tab'))].innerHTML += '<div class="tab"><div class="path" style="overflow-x:scroll"></div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>';
				}
				else {
					$ ('#content2') [0].children [0].innerHTML += '<div class="tab"><div class="path" style="overflow-x:scroll"></div><textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%"></textarea> </div>';
				}
				if ($ ('#guardar') == list ([])) {
					$ ('#btns-action') [0].innerHTML += '<button class="bg-blue white" id="guardar">Guardar</button>';
				}
				if ($ ('#borrar') == list ([])) {
					$ ('#guardar') [0].parentNode.innerHTML += "<button id='borrar'>Borrar</button>";
				}
				py_update ();
			}
			window.editores [k].getDoc ().setValue ('cargando...');
		};
		$ ('.fileclass').bind ('click', seleccionar);
		var cerrar = function (evt) {
			$ ('#alert').addClass ('hidden');
		};
		$ ('#alert-close').bind ('click', cerrar);
		var crear = function (evt) {
			$ ('#alert').removeClass ('hidden');
		};
		$ ('#nuevo').bind ('click', crear);
		var _lambda = function (evt) {
			if ($ ('#treefiles').hasClass ('hidden')) {
				$ ('#treefiles').removeClass ('hidden');
			}
			else {
				$ ('#treefiles').addClass ('hidden');
			}
		};
		$ ('#titulo').bind ('click', _lambda);
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__._lambda = _lambda;
			__all__.borrar = borrar;
			__all__.cerrar = cerrar;
			__all__.codeEditor = codeEditor;
			__all__.config = config;
			__all__.crear = crear;
			__all__.decode = decode;
			__all__.guardar = guardar;
			__all__.list = list;
			__all__.navegar = navegar;
			__all__.normalizar = normalizar;
			__all__.rest = rest;
			__all__.seleccionar = seleccionar;
			__all__.py_metatype = py_metatype;
			__all__.py_update = py_update;
			__all__.valores = valores;
		__pragma__ ('</all>')
	}) ();
