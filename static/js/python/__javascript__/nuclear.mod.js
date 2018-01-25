	(function () {
		var re = {};
		var __name__ = '__main__';
		__nest__ (re, '', __init__ (__world__.re));
		var list = py_datos.list;
		var py_metatype = py_datos.py_metatype;
		var thumbail = function (img, sufijo) {
			if (typeof sufijo == 'undefined' || (sufijo != null && sufijo .hasOwnProperty ("__kwargtrans__"))) {;
				var sufijo = '_540x540';
			};
			return (img.__getslice__ (0, img.rfind ('.'), 1) + sufijo) + img.__getslice__ (img.rfind ('.'), null, 1);
		};
		var defaultValues = function () {
			return list ([list ([null]), list ([])]);
		};
		var defaultEvents = function () {
			var eventos = list ([list ([list (['click', list ([])]), list (['mouseenter', list ([])]), list (['mouseleave', list ([])]), list (['mouseover', list ([])]), list (['mouseout', list ([])]), list (['mousemove', list ([])]), list (['mousedown', list ([])]), list (['mouseup', list ([])]), list (['dblclick', list ([])]), list (['keypress', list ([])]), list (['keydonw', list ([])]), list (['keyup', list ([])]), list (['input', list ([])]), list (['blur', list ([])]), list (['focus', list ([])]), list (['drag', list ([])]), list (['dragend', list ([])]), list (['dragenter', list ([])]), list (['dragleave', list ([])]), list (['dragover', list ([])]), list (['dragstart', list ([])]), list (['drop', list ([])])]), list ([])]);
			return eventos;
		};
		var getEvents = function (elemento) {
			var hijos = list ([]);
			var lista = list ([]);
			var eventos = list (['click', 'mouseenter', 'mouseleave', 'mouseover', 'mouseout', 'mousemove', 'mousedown', 'mouseup', 'dblclick', 'keypress', 'keydonw', 'keyup', 'input', 'blur', 'focus', 'drag', 'dragend', 'dragenter', 'dragleave', 'dragover', 'dragstart', 'drop']);
			if (len (elemento.children) > 0) {
				var __iterable0__ = elemento.children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					hijos += list ([getEvents (elem)]);
				}
			}
			var __iterable0__ = eventos;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				lista += list ([list ([elem, elemento.events (elem)])]);
			}
			return list ([lista, hijos]);
		};
		var getValues = function (elemento) {
			if (__in__ ('value', dir (elemento))) {
				var lista = list ([elemento.value]);
			}
			else {
				var lista = list ([null]);
			}
			var hijos = list ([]);
			if (len (elemento.children) > 0) {
				var __iterable0__ = elemento.children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					hijos += list ([getValues (elem)]);
				}
			}
			return list ([lista, hijos]);
		};
		var updateEvent = function (listaEvent, padre) {
			if (py_typeof (listaEvent [0] [0]) == str) {
				var eventos = listaEvent [0] [0];
				var __iterable0__ = enumerate (eventos);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var eventolist = __left0__ [1];
					if (len (eventolist) > 0) {
						if (eventolist != null && py_typeof (eventolist) == list && py_typeof (eventolist [0]) == str) {
							var __iterable1__ = eventolist [1];
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var funcion = __iterable1__ [__index1__];
								padre.bind (eventolist [0], funcion);
							}
						}
					}
				}
			}
			else {
				var eventos = listaEvent [0];
				var __iterable0__ = enumerate (eventos);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var eventolist = __left0__ [1];
					if (len (eventolist) > 0) {
						if (eventolist != null && py_typeof (eventolist) == list) {
							var __iterable1__ = eventolist [1];
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var funcion = __iterable1__ [__index1__];
								padre.bind (eventolist [0], funcion);
							}
						}
					}
				}
			}
			var hijos = listaEvent [1];
			var c = 0;
			var __iterable0__ = enumerate (hijos);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var hijo = __left0__ [1];
				if (hijo != null && len (padre.children) > 0) {
					updateEvent (hijo, padre.children [k]);
				}
			}
		};
		var updateValues = function (listaValues, padre) {
			var py_values = listaValues [0];
			var hijos = listaValues [1];
			var __iterable0__ = enumerate (py_values);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var valor = __left0__ [1];
				if (valor != null) {
					padre.value = valor;
				}
			}
			var __iterable0__ = enumerate (hijos);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var hijo = __left0__ [1];
				if (hijo != null) {
					updateValues (hijo, padre.children [k]);
				}
			}
		};
		var zjoin = function (lista, sep) {
			var c = '';
			var __iterable0__ = lista;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				c += str (elem) + sep;
			}
			return c.__getslice__ (0, -(1), 1);
		};
		var normalizar = function (v) {
			var decode = Codificador.Codificador.decode;
			var dicccionar = function (json) {
				var l = list ([]);
				if (json != null) {
					var __iterable0__ = enumerate (Object.keys(json)
					);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						l.append (list ([elem, (py_typeof (json [elem]) != dict && py_typeof (json [elem]) != object ? json [elem] : dicccionar (json [elem]))]));
					}
				}
				return dict (l);
			};
			if (py_typeof (v) == str && !__in__ (v, list (__globals__ (__all__)))) {
				if (!__in__ (';', v)) {
					try {
						var v = decode (v.strip ());
						if (!__in__ (v, __globals__ (__all__))) {
							window.eval ('False=false;True=true;None=null;a=' + v);
							if (typeof (a) == 'object' && !(v.strip ().startswith ('[')) && !(v.strip ().endswith (']'))) {
								return dicccionar (a);
							}
							else {
								return a;
							}
						}
						else {
							return v;
						}
					}
					catch (__except0__) {
						return v;
					}
				}
				else {
					return v;
				}
			}
			else {
				return v;
			}
		};
		var getCookie = function () {
			var cookies = dict ({});
			var __iterable0__ = document.cookie.py_split (';');
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				if (__in__ ('=', elem)) {
					var __left0__ = elem.py_split ('=');
					var k = __left0__ [0];
					var v = __left0__ [1];
					cookies [k.strip ()] = normalizar (v);
				}
			}
			return cookies;
		};
		var getRest = function () {
			var config = Config.Config ();
			var decode = Codificador.Codificador.decode;
			var url = decode (window.location.href).__getslice__ (len (config.base_url), null, 1).py_split ('#');
			var gato = null;
			if (len (url) == 2) {
				var gato = url [1];
			}
			var url = url [0].py_split ('/');
			if (__in__ ('', url)) {
				url.remove ('');
			}
			var pos = list (['app', 'control', 'metodo', 'args', 'kwargs']);
			var rest = dict ({'app': null, 'control': null, 'metodo': null, 'args': list ([]), 'kwargs': dict ({}), 'action': null, 'manager': false, 'request': dict ({}), '#': null});
			var identificar = function (elem, rest, pos) {
				if (!__in__ ('=', elem) && !__in__ ('{', elem) && !__in__ ('}', elem)) {
					if (len (pos) > 0) {
						if (pos [0] == 'app') {
							if (__in__ (elem, config.apps)) {
								rest ['app'] = normalizar (elem);
							}
							pos.remove ('app');
						}
						else if (pos [0] == 'control') {
							rest ['control'] = normalizar (elem);
							pos.remove ('control');
						}
						else if (pos [0] == 'metodo') {
							rest ['metodo'] = normalizar (elem);
							pos.remove ('metodo');
						}
						else if (pos [0] == 'args') {
							rest ['args'].append (normalizar (elem));
						}
						else if (pos [0] == 'kwargs') {
							pos.remove ('kwargs');
						}
					}
				}
				else if (__in__ ('=', elem)) {
					if (len (pos) > 0) {
						if (pos [0] == 'app') {
							pos.remove ('app');
						}
						else if (pos [0] == 'control') {
							pos.remove ('control');
						}
						else if (pos [0] == 'metodo') {
							pos.remove ('metodo');
						}
						else if (pos [0] == 'args') {
							pos.remove ('args');
						}
						else if (pos [0] == 'kwargs') {
							pos.remove ('kwargs');
						}
					}
					var __iterable0__ = elem.py_split ('&');
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var item = __iterable0__ [__index0__];
						var __left0__ = item.py_split ('=');
						var k = __left0__ [0];
						var v = __left0__ [1];
						rest [k] = normalizar (v);
					}
				}
				else if (__in__ ('{', elem) && __in__ ('}', elem)) {
					if (len (pos) > 0) {
						if (pos [0] == 'app') {
							pos.remove ('app');
						}
						else if (pos [0] == 'control') {
							pos.remove ('control');
						}
						else if (pos [0] == 'metodo') {
							pos.remove ('metodo');
						}
						else if (pos [0] == 'args') {
							pos.remove ('args');
						}
						else if (pos [0] == 'kwargs') {
							pos.remove ('kwargs');
						}
						rest ['kwargs'] = normalizar (elem);
					}
				}
			};
			var __iterable0__ = url;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				identificar (elem, rest, pos);
			}
			if (gato != null) {
				rest ['#'] = gato;
			}
			if (rest ['app'] == null) {
				rest ['app'] = config.default_app;
			}
			return rest;
		};
		var Component = __class__ ('Component', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, url, data, admin, isglobal, offline) {
				if (typeof data == 'undefined' || (data != null && data .hasOwnProperty ("__kwargtrans__"))) {;
					var data = dict ({});
				};
				if (typeof admin == 'undefined' || (admin != null && admin .hasOwnProperty ("__kwargtrans__"))) {;
					var admin = true;
				};
				if (typeof isglobal == 'undefined' || (isglobal != null && isglobal .hasOwnProperty ("__kwargtrans__"))) {;
					var isglobal = true;
				};
				if (typeof offline == 'undefined' || (offline != null && offline .hasOwnProperty ("__kwargtrans__"))) {;
					var offline = false;
				};
				var widget = '';
				var data = str (data);
				self.admin = admin;
				self.isglobal = isglobal;
				if (offline == false) {
					self.py_update (data);
				}
				else {
					if (isglobal) {
						
						          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/global/widgets/'+url+'.html/action=componer/',
						                  
						                  async:false,
						                  
						                  success:  function(respuesta){
						                            widget=respuesta;
						                        },
						                  error : function(objXMLHttpRequest) {
						                    console.log("error1",objXMLHttpRequest);
						                    }
						                  })
						          
					}
					else if (admin) {
						
						          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/admin/widgets/'+url+'.html/action=componer/',
						             
						                  async:false,
						                  
						
						                  success:  function(respuesta){
						                            widget=respuesta;
						                        },
						                  error : function(objXMLHttpRequest) {
						                    console.log("error2",objXMLHttpRequest);
						                    }
						                  })
						          
					}
					else {
						
						          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/user/widgets/'+url+'.html/action=componer/',
						                  
						                  async:false,
						                  
						                  success:  function(respuesta){
						                            widget=respuesta;
						                        },
						                error : function(objXMLHttpRequest) {
						                console.log("error3",objXMLHttpRequest);
						                }
						
						                  })
						                
						          
					}
					var lineas = widget.py_split ('\n');
					var getTab = __init__ (__world__.zu).getTab;
					var AnteriorIdentacion = '';
					var abierta = false;
					var __iterable0__ = enumerate (lineas);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						var identacion = getTab (elem);
						if (__in__ ('#', elem)) {
							if (__in__ ('=', elem) && (elem [elem.find ('=') - 1] != '=' && elem [elem.find ('=') - 1] != '<' && elem [elem.find ('=') - 1] != '>' && elem [elem.find ('=') - 1] != '!')) {
								var c = elem.find ('=');
								while (c > 0) {
									if (elem [c] == '\t' || elem [c] == ' ') {
										break;
									}
									c--;
								}
								lineas [k] = (elem.__getslice__ (0, c, 1) + 'var ') + elem.__getslice__ (c, null, 1);
							}
							lineas [k] = lineas [k].py_replace ('#', ';//');
							var elem = lineas [k];
						}
						if (__in__ ('except Exception as e:', elem)) {
							lineas [k] = elem.py_replace ('except Exception as e:', '}catch(e){');
							if (lineas [k].strip ().endswith ('}catch(e){')) {
								var abierta = true;
							}
							else {
								lineas [k] += ';}';
								var elem = lineas [k];
								var abierta = false;
							}
						}
						else if (__in__ ('try:', elem)) {
							lineas [k] = elem.py_replace ('try:', 'try{');
							var elem = lineas [k] + (lineas [k].endswith ('try{') ? '' : ';');
							var abierta = true;
						}
						else if (__in__ ("'''", elem)) {
							lineas [k] = elem.py_replace ("'''", '`');
							var elem = lineas [k] + ';';
						}
						else if (__in__ ('"""', elem)) {
							lineas [k] = elem.py_replace ('"""', '`');
							var elem = lineas [k] + ';';
						}
						else if (__in__ ('elif ', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('elif ', '}else if(').py_replace (':', '){');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('if ', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('if ', 'if(').py_replace (':', '){');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('else', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('else', '}else').py_replace (':', '{');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('=', elem) && (elem [elem.find ('=') - 1] != '+' && elem [elem.find ('=') - 1] != '=' && elem [elem.find ('=') - 1] != '<' && elem [elem.find ('=') - 1] != '>' && elem [elem.find ('=') - 1] != '!' && !__in__ ('//', elem)) && elem [elem.find ('=') + 1] != '=') {
							var c = elem.find ('=') - 1;
							while (c > 0) {
								if (elem [c] == '\t' || elem [c] == ' ') {
									lineas [k] = ((elem.__getslice__ (0, c + 1, 1) + 'var ') + elem.__getslice__ (c + 1, null, 1)) + ';';
									break;
								}
								c--;
							}
						}
						else if (__in__ ('while ', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('while ', 'while(').py_replace (':', '){');
							var elem = lineas [k];
						}
						else if (__in__ ('for ', elem) && __in__ (':', elem)) {
							var des = '(\\w+)\\s*(?:,(\\s*\\w+))?';
							var _iter = '((?:\\w+)?(?:\\(?\\[[A-Za-z0-9_,\\-\'"]+?\\]\\)?)?)';
							var patron1 = re.compile (((('for\\s+' + des) + '\\s*in\\s+') + _iter) + ':');
							var descompresion = patron1.findall (lineas [k]) [0];
							var cond2 = '}else{';
							var i = lineas [k].find ('for ');
							print (descompresion);
							if (len (descompresion) > 2 && descompresion [1] != '' && descompresion [1] != null) {
								var f = lineas [k].find (':', lineas [k].find (descompresion [2]));
								var cond1 = ((('if (str(' + descompresion [2]) + ").strip()[0]=='[' && str(") + descompresion [2]) + ").strip().slice(-1)==']'){";
								var iterable = ((((('var ' + descompresion [1]) + '=') + descompresion [2]) + '[') + descompresion [0]) + '][1];';
								var iterable2 = ((((('var ' + descompresion [1]) + '= Object.keys(') + descompresion [2]) + ')[') + descompresion [0]) + '];';
								var bucle = ((((((('for (var ' + descompresion [0]) + ' = 0; ') + descompresion [0]) + ' < Object.keys(') + descompresion [2]) + ').length; ') + descompresion [0]) + '++) {';
								lineas [k] = ((((((lineas [k].__getslice__ (0, i, 1) + bucle) + cond1) + iterable) + cond2) + iterable2) + '}') + lineas [k].__getslice__ (f + 1, null, 1);
							}
							else {
								var f = lineas [k].find (':', lineas [k].find (descompresion [2]));
								var cond1 = ((('if (str(' + descompresion [2]) + ").strip()[0]=='[' && str(") + descompresion [2]) + ").strip().slice(-1)==']'){";
								var bucle = ('for (var _k = 0; _k < Object.keys(' + descompresion [2]) + ').length; _k++){/**/';
								var iterable = ((('var ' + descompresion [0]) + '=') + descompresion [2]) + '[_k];';
								var iterable2 = ((('var ' + descompresion [0]) + '= Object.keys(') + descompresion [2]) + ')[_k];';
								lineas [k] = ((((((lineas [k].__getslice__ (0, i, 1) + bucle) + cond1) + iterable) + cond2) + iterable2) + '}') + lineas [k].__getslice__ (f + 1, null, 1);
							}
						}
						else if (__in__ ('try:', elem)) {
							lineas [k] = elem.py_replace ('try:', 'try{');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('pass', elem)) {
							lineas [k] = elem.py_replace ('pass', '}//pass');
							var elem = lineas [k];
							var abierta = false;
						}
						else if (lineas [k].strip () != '') {
							lineas [k] += ';';
						}
						else if (len (AnteriorIdentacion) > len (identacion) && abierta == true) {
							if (!__in__ ('}', lineas [k])) {
								lineas [k] += '}';
							}
						}
						if (!(lineas [k].strip ().endswith ('{')) && !(lineas [k].strip ().endswith ('}')) && !(lineas [k].strip ().endswith (';')) && lineas [k].strip () != '') {
							lineas [k] += ';';
							var elem = lineas [k];
						}
						if (__in__ (' if ', elem) && __in__ (' else ', elem)) {
							if (elem.find ('=') > elem.find (' if ')) {
								var codigo = elem.__getslice__ (len ('str('), -(1), 1);
								var valor1 = codigo.__getslice__ (0, codigo.find (' if ') - len (' if '), 1);
								var condicion = codigo.__getslice__ (codigo.find (' if '), codigo.find (' else ') - len (' else '), 1);
								var valor2 = codigo.__getslice__ (codigo.find (' else '), null, 1);
								lineas [k] = ((((((variable + 'str(') + condicion) + '?') + valor1) + ':') + valor2) + ');';
							}
							else {
								var variable = elem.__getslice__ (0, elem.find ('str('), 1);
								var codigo = elem.__getslice__ (elem.find ('str(') + len ('str('), null, 1);
								var i = elem.rfind ('(', elem.find (' if '));
								var f = elem.find (')', elem.find (' else '));
								var bloque = elem.__getslice__ (i + 1, f, 1);
								var valor1 = bloque.__getslice__ (0, bloque.find (' if '), 1);
								var condicion = bloque.__getslice__ (bloque.find (' if ') + len (' if '), bloque.find (' else '), 1);
								var valor2 = bloque.__getslice__ (bloque.find (' else ') + len (' else '), null, 1);
								lineas [k] = ((((((variable + 'str((') + condicion) + ')?') + valor1) + ':') + valor2) + ');';
							}
						}
					}
					var widget = '\n'.join (lineas);
					self.widget = widget;
				}
				return widget;
			});},
			get run () {return __get__ (this, function (self, data) {
				if (typeof data == 'undefined' || (data != null && data .hasOwnProperty ("__kwargtrans__"))) {;
					var data = dict ({});
				};
				var doc = '';
				var decode = Codificador.Codificador.decode;
				try {
					eval (self.widget);
				}
				catch (__except0__) {
					print (__except0__);
				}
				return doc;
			});},
			get py_update () {return __get__ (this, function (self, data) {
				if (typeof data == 'undefined' || (data != null && data .hasOwnProperty ("__kwargtrans__"))) {;
					var data = dict ({});
				};
				if (self.isglobal) {
					
					          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/global/widgets/'+self.url+'.html/action=compuesto/'+data,
					                  async:false,
					                  success:  function(respuesta){
					                            self.widget=respuesta;
					                        },
					                  error : function(objXMLHttpRequest) {
					                    console.log("error1",objXMLHttpRequest);
					                    }
					                  })
					          
				}
				else if (self.admin) {
					
					          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/admin/widgets/'+self.url+'.html/action=compuesto/'+data,
					                  async:false,
					                  success:  function(respuesta){
					                            self.widget=respuesta;
					                        },
					                  error : function(objXMLHttpRequest) {
					                    console.log("error2",objXMLHttpRequest);
					                    }
					                  })
					          
				}
				else {
					
					          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/user/widgets/'+self.url+'.html/action=compuesto/'+data,
					                  async:false,
					                  success:  function(respuesta){
					                            self.widget=respuesta;
					                        },
					                error : function(objXMLHttpRequest) {
					                console.log("error3",objXMLHttpRequest);
					                }
					
					                  })
					          
				}
				return self.widget;
			});}
		});
		var VAR = function (nombre) {
			try {
				return normalizar ($ (("var[name='" + nombre) + "']") [0].innerText);
			}
			catch (__except0__) {
				print ('No se pudo encontrar la varible html: ' + nombre);
				print (__except0__);
			}
		};
		var Settings = __class__ ('Settings', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self) {
				var rest = getRest ();
				self.app = rest ['app'];
			});}
		});
		window.settings = Settings ();
		window.rest = getRest ();
		__pragma__ ('<use>' +
			're' +
			'zu' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Component = Component;
			__all__.Settings = Settings;
			__all__.VAR = VAR;
			__all__.__name__ = __name__;
			__all__.defaultEvents = defaultEvents;
			__all__.defaultValues = defaultValues;
			__all__.getCookie = getCookie;
			__all__.getEvents = getEvents;
			__all__.getRest = getRest;
			__all__.getValues = getValues;
			__all__.list = list;
			__all__.normalizar = normalizar;
			__all__.thumbail = thumbail;
			__all__.py_metatype = py_metatype;
			__all__.updateEvent = updateEvent;
			__all__.updateValues = updateValues;
			__all__.zjoin = zjoin;
		__pragma__ ('</all>')
	}) ();
