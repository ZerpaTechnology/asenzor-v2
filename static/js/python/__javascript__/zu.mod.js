	__nest__ (
		__all__,
		'zu', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var math = {};
					var __name__ = 'zu';
					__nest__ (math, '', __init__ (__world__.math));
					var invertString = function (cad) {
						var c = '';
						var __iterable0__ = cad;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							var c = elem + c;
						}
						return c;
					};
					var randomString = function (lon, alp, noalp, num) {
						if (typeof lon == 'undefined' || (lon != null && lon .hasOwnProperty ("__kwargtrans__"))) {;
							var lon = 8;
						};
						if (typeof alp == 'undefined' || (alp != null && alp .hasOwnProperty ("__kwargtrans__"))) {;
							var alp = true;
						};
						if (typeof noalp == 'undefined' || (noalp != null && noalp .hasOwnProperty ("__kwargtrans__"))) {;
							var noalp = true;
						};
						if (typeof num == 'undefined' || (num != null && num .hasOwnProperty ("__kwargtrans__"))) {;
							var num = true;
						};
						var v_num = '0123456789';
						var v_alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
						var v_noalp = '.-!$()|@{[]}~>';
						if (alp == true && noalp == true && num == true) {
							var v = (v_num + v_alp) + v_noalp;
						}
						else if (alp == true && noalp == false && num == true) {
							var v = v_num + v_alp;
						}
						else if (alp == false && noalp == true && num == true) {
							var v = v_num + v_noalp;
						}
						else if (alp == true && noalp == true && num == false) {
							var v = v_alp + v_noalp;
						}
						else if (alp == false && noalp == false && num == true) {
							var v = v_num;
						}
						else if (alp == true && noalp == false && num == false) {
							var v = v_alp;
						}
						else if (alp == false && noalp == true && num == false) {
							var v = v_noalp;
						}
						else {
							return null;
						}
						var c = 0;
						var token = '';
						while (c < lon) {
							token += v [random.randrange (0, len (v))];
							c++;
						}
						return token;
					};
					var cmpString = function (cad1, cad2, orden, mayor) {
						if (typeof orden == 'undefined' || (orden != null && orden .hasOwnProperty ("__kwargtrans__"))) {;
							var orden = '1a.';
						};
						if (typeof mayor == 'undefined' || (mayor != null && mayor .hasOwnProperty ("__kwargtrans__"))) {;
							var mayor = true;
						};
						var c = (mayor == true ? 'aáàäbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzçḉ' : invertString ('aáàäbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzçḉ'));
						var c1 = c + c.upper ();
						var c2 = (mayor == true ? '0123456789' : invertString ('0123456789'));
						var c3 = (mayor == true ? ",;.·:_+-*/^%=&~@#|()[]{}¡!¿?<>«»ºª¬'‘´`¨“”€ł¶ŧ←↓→øþæßðđŋħł¢µΩŁ¢®Ŧ¥↑ıØÞÆ§ÐªŊĦŁ©" : invertString (",;.·:_+-*/^%=&~@#|()[]{}¡!¿?<>«»ºª¬'‘´`¨“”€ł¶ŧ←↓→øþæßðđŋħł¢µΩŁ¢®Ŧ¥↑ıØÞÆ§ÐªŊĦŁ©"));
						var rango = (len (cad1) <= len (cad2) ? len (cad1) : len (cad2));
						if (orden == '1a.') {
							var cadena = (c2 + c1) + c3;
						}
						else if (orden == '.a1') {
							var cadena = (c3 + c1) + c2;
						}
						else if (orden == '1.a') {
							var cadena = (c2 + c3) + c1;
						}
						else if (orden == 'a.1') {
							var cadena = (c1 + c3) + c2;
						}
						else if (orden == 'a1.') {
							var cadena = (c1 + c2) + c3;
						}
						else if (orden == '.1a') {
							var cadena = (c3 + c2) + c1;
						}
						for (var x = 0; x < rango; x++) {
							if (cadena.find (cad1 [x]) > cadena.find (cad2 [x])) {
								return true;
							}
							else if (cadena.find (cad1 [x]) < cadena.find (cad2 [x])) {
								return false;
							}
						}
						return null;
					};
					var ordenLargString = function (l, mayor, largo, orden) {
						if (typeof mayor == 'undefined' || (mayor != null && mayor .hasOwnProperty ("__kwargtrans__"))) {;
							var mayor = true;
						};
						if (typeof largo == 'undefined' || (largo != null && largo .hasOwnProperty ("__kwargtrans__"))) {;
							var largo = true;
						};
						if (typeof orden == 'undefined' || (orden != null && orden .hasOwnProperty ("__kwargtrans__"))) {;
							var orden = '1a.';
						};
						var nl = list ([]);
						var c = 0;
						var pos = 0;
						while (c < len (l)) {
							var cad = l [c];
							var c2 = 0;
							var pos = 0;
							while (c2 <= len (nl) - 1) {
								if (largo == true) {
									if (len (nl [c2]) > len (cad)) {
										pos++;
									}
									else if (len (nl [c2]) == len (cad)) {
										if (!(cmpString (nl [c2], cad, __kwargtrans__ ({mayor: mayor, orden: orden})))) {
											pos++;
										}
										else {
											// pass;
										}
									}
								}
								else if (len (nl [c2]) < len (cad)) {
									pos++;
								}
								else if (len (nl [c2]) == len (cad)) {
									if (cmpString (nl [c2], cad, __kwargtrans__ ({mayor: mayor, orden: orden}))) {
										// pass;
									}
									else {
										pos++;
									}
								}
								c2++;
							}
							nl.insert (pos, cad);
							c++;
						}
						return nl;
					};
					var getTab = function (linea) {
						var c = 0;
						var cadena = '';
						while (c < len (linea)) {
							if (linea [c] == '\t' || linea [c] == '\r' || linea [c] == ' ') {
								cadena += linea [c];
							}
							else {
								return cadena;
							}
							c++;
						}
						return cadena;
					};
					var siguienteNivel = function (codigo, funcion) {
						if (typeof funcion == 'undefined' || (funcion != null && funcion .hasOwnProperty ("__kwargtrans__"))) {;
							var funcion = null;
						};
						var cadena = '';
						var cadena2 = '';
						var c = 0;
						var tab = len (getTab (codigo [c]));
						while (c < len (codigo)) {
							if (len (getTab (codigo [c])) > tab) {
								cadena += codigo [c] + '\n';
							}
							else if (len (getTab (codigo [c])) == tab) {
								cadena2 += codigo [c] + '\n';
							}
							c++;
						}
						if (funcion != null) {
							return funcion (cadena.__getslice__ (0, -(1), 1).py_split ('\n')) + cadena2;
						}
						else {
							return cadena.__getslice__ (0, -(1), 1) + cadena2;
						}
					};
					var finIndex = function (cadena, busca) {
						return (cadena.index (busca) + len (busca)) - 1;
					};
					var compilarLambda = function (codigo) {
						var c = 0;
						var abierto = false;
						var tabulacion = 0;
						var cadena = '';
						var cadena2 = '';
						var punteros = list ([]);
						while (c < len (codigo) - 1) {
							if (__in__ ('lambda ', codigo [c]) && __in__ ('=', codigo [c]) && __in__ (':', codigo [c]) && abierto == false) {
								var abierto = true;
								var cadena = siguienteNivel (codigo.__getslice__ (c + 1, null, 1), compilarLambda);
								var f = finIndex (codigo [c], 'lambda') + 1;
								var parametros = codigo [c].__getslice__ (f, codigo [c].index (':'), 1);
								var cparametros = '';
								var __iterable0__ = parametros.py_split (',');
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									cparametros += ((elem + '=') + elem) + ',';
								}
								cadena2 += ((((codigo [c] + 'zlambda(') + cparametros.__getslice__ (0, -(1), 1)) + ",__codigo__='''") + cadena.__getslice__ (0, -(1), 1)) + "''')\n";
								c += len (cadena.py_split ('\n')) - 1;
							}
							else {
								cadena2 += codigo [c] + '\n';
							}
							c++;
						}
						return cadena2;
					};
					var remplazarFueraString = function (cadena, viejo, nuevo) {
						var inicio = 0;
						var fin = 0;
						var abierto = false;
						var abridor = null;
						while (fin < len (cadena) - 1) {
							if (cadena [fin] == "'" || cadena [fin] == '"') {
								if (abierto == false) {
									var abierto = true;
									var abridor = cadena [fin];
									var cadena = (cadena.__getslice__ (0, inicio, 1) + cadena.__getslice__ (inicio, fin, 1).py_replace (viejo, nuevo)) + cadena.__getslice__ (fin, null, 1);
								}
								else if (abridor == cadena [fin]) {
									var abierto = false;
									var abridor = null;
									var inicio = fin;
								}
							}
							fin++;
						}
						return cadena;
					};
					var ordLargString = function (lista, creciente) {
						if (typeof creciente == 'undefined' || (creciente != null && creciente .hasOwnProperty ("__kwargtrans__"))) {;
							var creciente = true;
						};
						var _lista = lista;
						var lista2 = list ([]);
						var valor = '';
						var valor2 = '';
						var __iterable0__ = _lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (lista2 == list ([])) {
								lista2.append (elem);
							}
							else {
								var __iterable1__ = lista2;
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var elem2 = __iterable1__ [__index1__];
									if (len (elem) > len (elem2)) {
										var valor = elem2;
									}
								}
								lista2.insert (lista2.index (elem), valor);
							}
						}
						return lista2;
					};
					var dimensionar = function (lista) {
						var c = '';
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							c += ('[' + str (elem)) + ']';
						}
						return c;
					};
					var add = function (lista, numero) {
						var l = len (lista);
						var c = 0;
						while (c < l) {
							lista [c] = lista [c] + numero;
							c++;
						}
					};
					var add2 = function (lista, lista2) {
						var l = len (lista);
						var c = 0;
						while (c < l) {
							lista [c] = list ([lista [c] [0] + lista2 [0], lista [c] [1] + lista2 [1]]);
							c++;
						}
					};
					var restar = function (lista, numero) {
						var l = len (lista);
						var c = 0;
						while (c < l) {
							lista [c] = lista [c] - numero;
							c++;
						}
					};
					var mayor = function (lista) {
						var i = 0;
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (py_typeof (elem) == int) {
								if (elem > i) {
									var i = elem;
								}
							}
						}
						return i;
					};
					var ciento = function (valor1, valor2) {
						return (valor1 * valor2) / 100;
					};
					var ciento2 = function (valor1, valor2) {
						return (valor1 * 100) / valor2;
					};
					var diferenciar = function (v1, v2) {
						var l = list ([]);
						var __iterable0__ = v1;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							var __iterable1__ = v2;
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var elem2 = __iterable1__ [__index1__];
								if (elem != elem2) {
									l.append (elem2);
								}
							}
						}
						return l;
					};
					var por = function (v1, v2, f) {
						if (typeof f == 'undefined' || (f != null && f .hasOwnProperty ("__kwargtrans__"))) {;
							var f = 1;
						};
						if (f == 1) {
							var c = 0;
							var d = dict ({});
							var __iterable0__ = v1;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								d [str (elem)] = v2 [c];
								c++;
							}
							return d;
						}
						if (f == 2) {
							var cadena = '';
							var __iterable0__ = v1;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								cadena += str (elem) + ',';
							}
							var cadena = cadena.__getslice__ (0, -(1), 1);
							return cadena;
						}
					};
					var mayor_f = function (lista, f) {
						if (typeof f == 'undefined' || (f != null && f .hasOwnProperty ("__kwargtrans__"))) {;
							var f = 1;
						};
						var lista2 = list ([]);
						var a = 0;
						var m = 0;
						var d = 0;
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							lista2.append (elem.py_split ('/'));
							print (elem.py_split ('/'));
						}
						var __iterable0__ = lista2;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (elem [0] > d) {
								var d = elem [0];
							}
							if (el6em [1] > m) {
								var m = elem [1];
							}
							if (elem [2] > a) {
								var a = elem [2];
							}
						}
						if (f == 1) {
							return list ([d, m, a]);
						}
						if (f == 2) {
							return (((str (d) + '/') + str (m)) + '/') + str (a);
						}
					};
					var u = function (valor, f) {
						if (typeof f == 'undefined' || (f != null && f .hasOwnProperty ("__kwargtrans__"))) {;
							var f = 1;
						};
						if (f == 1) {
							var c = 0;
							var __iterable0__ = valor;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								valor [c] = elem.decode ('utf-8');
								c++;
							}
							return valor;
						}
						if (f == 2) {
							var c = 0;
							var __iterable0__ = valor;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								valor [c] [0] = elem [0].decode ('utf-8');
								c++;
							}
							return valor;
						}
					};
					var u2 = function (valor) {
						return str (valor).py_replace ('\\xc3\\xb3', 'ó').py_replace ('\\xc3\\xba', 'ú').py_replace ('\\xc3\\xad', 'í').py_replace ('\\xc2\\xa1', '!').py_replace ('\\xc3\\xb1', 'ñ');
					};
					var nu2 = function (valor) {
						return str (valor).py_replace ('ó', 'o').py_replace ('ú', 'u').py_replace ('í', 'i').py_replace ('á', 'a').py_replace ('é', 'e');
					};
					var tipo_v = function (tipo) {
						if (tipo == str) {
							return '';
						}
						if (tipo == int) {
							return 0;
						}
						if (tipo == bool) {
							return false;
						}
						if (tipo == null) {
							return null;
						}
						if (tipo == float) {
							return 0.0;
						}
						if (tipo == list) {
							return list ([]);
						}
						if (tipo == tuple) {
							return tuple ([]);
						}
						if (tipo == dict) {
							return dict ({});
						}
					};
					var tipo = function (cadena) {
						var cadena = cadena.py_replace ("<type 'str'>", 'str');
						var cadena = cadena.py_replace ("<type 'int'>", 'int');
						var cadena = cadena.py_replace ("<type 'float'>", 'float');
						var cadena = cadena.py_replace ("<type 'list'>", 'list');
						var cadena = cadena.py_replace ("<type 'tuple'>", 'tuple');
						var cadena = cadena.py_replace ("<type 'None'>", 'None');
						var cadena = cadena.py_replace ("<type 'dict'>", 'dict');
						return cadena;
					};
					var concatenar = function (lista, separador) {
						if (typeof separador == 'undefined' || (separador != null && separador .hasOwnProperty ("__kwargtrans__"))) {;
							var separador = null;
						};
						var i = '';
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (separador != null) {
								i += str (elem) + separador;
							}
							else {
								i += str (elem);
							}
						}
						if (separador != null) {
							return i.__getslice__ (0, -(1), 1);
						}
						else {
							return i;
						}
					};
					var concatenar2 = function (lista) {
						var i = '';
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							i += str (elem) + '\n';
						}
						return i;
					};
					var posicionar = function (pantalla, t_posicion, posicion) {
						// pass;
					};
					var poligono = function (size, pos, radios) {
						print (radios);
						if (len (radios) == 4) {
							var top = arco (radios [0], 'top');
							add2 (top, list ([pos [0], pos [1]]));
							return top.__getslice__ (0, 50, 1);
						}
						else {
							print ('no hay los radios necesarios');
						}
					};
					var rect_radius = function (pos, size, radios, borde, inverso) {
						if (typeof borde == 'undefined' || (borde != null && borde .hasOwnProperty ("__kwargtrans__"))) {;
							var borde = false;
						};
						if (typeof inverso == 'undefined' || (inverso != null && inverso .hasOwnProperty ("__kwargtrans__"))) {;
							var inverso = false;
						};
						var angulo = 0;
						var rect = list ([]);
						var right = list ([]);
						var bottom = list ([]);
						var left = list ([]);
						var top = list ([]);
						while (angulo < 6.4) {
							var sen = math.sin (angulo);
							var cos = math.cos (angulo);
							if (angulo < 1.6) {
								var y = ((sen * radios [2] + pos [1]) + size [1]) - radios [2];
								var x = ((cos * radios [2] + pos [0]) + size [0]) - radios [2];
								bottom.append (tuple ([x, y]));
							}
							if (angulo > 1.6 && angulo < 3.2) {
								var y = ((sen * radios [3] + pos [1]) + size [1]) - radios [3];
								var x = (cos * radios [3] + pos [0]) + radios [3];
								left.append (tuple ([x, y]));
							}
							if (angulo > 3.2 && angulo < 4.8) {
								var y = (sen * radios [0] + pos [1]) + radios [0];
								var x = (cos * radios [0] + pos [0]) + radios [0];
								top.append (tuple ([x, y]));
							}
							if (angulo > 4.8 && angulo < 6.4) {
								var y = (sen * radios [1] + pos [1]) + radios [1];
								var x = ((cos * radios [1] + pos [0]) + size [0]) - radios [1];
								right.append (tuple ([x, y]));
							}
							angulo += 0.01;
						}
						if (borde == false) {
							var rect = ((top + right) + bottom) + left;
						}
						else {
							var rect = list ([top, right, bottom, left]);
						}
						if (inverso == true) {
							top.insert (0, tuple ([0, 0]));
							right.insert (0, tuple ([pos [0] + size [0], pos [1]]));
							bottom.insert (0, tuple ([pos [0] + size [0], pos [1] + size [1]]));
							left.insert (0, tuple ([pos [0], pos [1] + size [1]]));
							var rect = list ([top, right, bottom, left]);
						}
						return rect;
					};
					var css_convert = function (atributo, css) {
						if (__in__ (atributo, css)) {
							if (atributo == 'background' || atributo == 'background-color') {
								return 2;
							}
						}
						else {
							print ('este atributo no existe');
						}
					};
					var rect_radius2 = function (pos, size, radios, borde, inverso) {
						if (typeof borde == 'undefined' || (borde != null && borde .hasOwnProperty ("__kwargtrans__"))) {;
							var borde = false;
						};
						if (typeof inverso == 'undefined' || (inverso != null && inverso .hasOwnProperty ("__kwargtrans__"))) {;
							var inverso = false;
						};
						var angulo = 0;
						var rect = list ([]);
						var right = list ([]);
						var bottom = list ([]);
						var left = list ([]);
						var top = list ([]);
						while (angulo < 6.2) {
							var sen = math.sin (angulo);
							var cos = math.cos (angulo);
							if (angulo < 1.6) {
								var y = ((int (sen * radios [2] [1]) + pos [1]) + size [1]) - radios [2] [1];
								var x = ((int (cos * radios [2] [0]) + pos [0]) + size [0]) - radios [2] [0];
								bottom.append (tuple ([x, y]));
							}
							if (angulo > 1.6 && angulo < 3.2) {
								var y = ((int (sen * radios [3] [1]) + pos [1]) + size [1]) - radios [3] [1];
								var x = ((int (cos * radios [3] [0]) + pos [0]) + radios [3] [0]) - 1;
								left.append (tuple ([x, y]));
							}
							if (angulo > 3.2 && angulo < 4.8) {
								var y = (sen * radios [0] [1] + pos [1]) + radios [0] [1];
								var x = (cos * radios [0] [0] + pos [0]) + radios [0] [0];
								top.append (tuple ([x, y]));
							}
							if (angulo > 4.8 && angulo < 6.2) {
								var y = (sen * radios [1] [1] + pos [1]) + radios [1] [1];
								var x = (((cos * radios [1] [0] + pos [0]) + size [0]) - radios [1] [0]) + 1;
								right.append (tuple ([x, y]));
							}
							angulo += 0.002;
						}
						if (borde == false) {
							var rect = ((top + right) + bottom) + left;
						}
						else {
							var rect = list ([top, right, bottom, left]);
						}
						if (inverso == true) {
							top.insert (0, tuple ([0, 0]));
							right.insert (0, tuple ([pos [0] + size [0], pos [1]]));
							bottom.insert (0, tuple ([pos [0] + size [0], pos [1] + size [1]]));
							left.insert (0, tuple ([pos [0], pos [1] + size [1]]));
							var rect = list ([top, right, bottom, left]);
						}
						return rect;
					};
					var separar = function (cadena) {
						var c = 0;
						var start = 0;
						var l = list ([]);
						while (c < len (cadena)) {
							if (cadena [c] == 'x' || cadena [c] == '%' || cadena.__getslice__ (start, c + 1, 1) == 'bottom' || cadena.__getslice__ (start, c + 1, 1) == 'right' || cadena.__getslice__ (start, c + 1, 1) == 'left' || cadena.__getslice__ (start, c + 1, 1) == 'center' || cadena.__getslice__ (start, c + 1, 1) == 'top' || cadena.__getslice__ (start, c + 1, 1) == 'auto') {
								if (c < len (cadena)) {
									var a = 1;
								}
								else {
									var a = 0;
								}
								l.append (cadena.__getslice__ (start, c + a, 1));
								var start = c + a;
							}
							c++;
						}
						return l;
					};
					var css_posicionamiento = function (objetos) {
						var x = 0;
						var y = 0;
						var __iterable0__ = objetos;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (elem.css.get_style ('position') == 'static') {
								if (elem.css.get_style ('display') == 'inline') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'block') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'inline-block') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'run-in') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'inline-table') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-footer-group') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-column') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'none') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-row-group') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-row') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-cell') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'inherit') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'list-item') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-header-group') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-column') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-caption') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-footer-group') {
									// pass;
								}
							}
							if (elem.css.get_style ('position') == 'relative') {
								// pass;
							}
							if (elem.css.get_style ('position') == 'absolute') {
								// pass;
							}
							if (elem.css.get_style ('position') == 'fixed') {
								// pass;
							}
							if (elem.css.get_style ('position') == 'inherit') {
								// pass;
							}
						}
					};
					var listar_d = function (dic, clave) {
						var l = list ([]);
						var elem = dic [clave];
						if (elem != dict ({})) {
							var __iterable0__ = elem;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var i = __iterable0__ [__index0__];
								if (elem [i] != dict ({})) {
									var elemento = elem [i];
									while (elemento != dict ({})) {
										elemento;
									}
								}
							}
						}
					};
					var dicc = __class__ ('dicc', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							self.l_claves = list ([]);
							self.d = dict ({});
						});},
						get niveles () {return __get__ (this, function (self, clave, orden) {
							var contador = 0;
							if (self.py_get (clave) != null) {
								var ciclo = self.py_get (clave);
								while (ciclo.keys_all () != list ([])) {
									if (len (ciclo.keys_p) >= orden) {
										try {
											var ciclo = ciclo.py_get (ciclo.keys_p [orden]);
											contador++;
										}
										catch (__except0__) {
											break;
										}
									}
								}
							}
							return contador;
						});},
						get mapear () {return __get__ (this, function (self, niveles) {
							if (typeof niveles == 'undefined' || (niveles != null && niveles .hasOwnProperty ("__kwargtrans__"))) {;
								var niveles = 1;
							};
							var dic = self.d;
							if (niveles > 20) {
								var niveles = 20;
							}
							var l = list ([]);
							var base = 'for elem0 in dic:\n try:\n  if dic[elem0].d.keys()!=[]:\n   l.append([elem0])\n   pass\n  else:\n   l.append([elem0])\n except:\n  l.append([elem0])';
							var base2 = base;
							var codigo = base;
							var lista = 'l.append([elem0])';
							for (var elem = 0; elem < niveles; elem++) {
								if (elem != 0) {
									var base2 = base2.py_replace ('dic[elem0].d', 'dic' + diccionar_elem ('elem', elem + 1, '.d'));
									var base2 = base2.py_replace ('dic:', ('dic' + diccionar_elem ('elem', elem, '.d')) + ':');
									var base2 = base2.py_replace ('for elem0', 'for elem' + str (elem));
									var base2 = base2.py_replace (lista, lista.py_replace ('[elem0]', listar_elem ('elem', elem + 1)));
									var base2 = tabular (base2, get_tab2 (codigo, 'pass'));
									var l_codigo = codigo.py_split ('\n');
									var __iterable0__ = l_codigo;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem2 = __iterable0__ [__index0__];
										if (__in__ ('pass', elem2)) {
											l_codigo [l_codigo.index (elem2)] = base2;
										}
									}
									var codigo = concatenar2 (l_codigo);
									var base2 = base;
								}
							}
							var f = open ('/home/abraham/prueba.txt', 'w');
							f.write (codigo);
							f.close ();
							exec (codigo);
							return l;
						});},
						get get_keys () {return __get__ (this, function (self, valor) {
							var __iterable0__ = self.keys_p ();
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (self.d [elem] == valor) {
									return self.py_keys (elem);
								}
								else {
									print ('ese valor no se encuentra en el diccionario Z');
									return null;
								}
							}
						});},
						get py_get () {return __get__ (this, function (self, clave) {
							var indice = 0;
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (clave, elem)) {
									var indice = self.l_claves.index (elem);
									return self.d [self.l_claves [indice] [0]];
								}
							}
							if (!(__in__ (clave, elem))) {
								print ('la clave no existe');
								return null;
							}
						});},
						get set () {return __get__ (this, function (self, valor) {
							var claves = tuple ([].slice.apply (arguments).slice (2));
							var claves = list (claves);
							var __iterable0__ = claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (elem, self.keys_all ())) {
									claves.remove (elem);
								}
							}
							if (claves != list ([])) {
								self.l_claves.append (claves);
								self.d [claves [0]] = valor;
							}
							else {
								print ('las claves ya estaban agragadas anteriormente');
							}
						});},
						get set2 () {return __get__ (this, function (self, valor, claves) {
							var claves2 = list (claves);
							var __iterable0__ = claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (elem, self.keys_all ())) {
									claves2.remove (elem);
								}
							}
							if (claves != list ([])) {
								self.l_claves.append (claves2);
								self.d [claves2 [0]] = valor;
							}
							else {
								print ('las claves ya estaban agragadas anteriormente');
							}
						});},
						get key2 () {return __get__ (this, function (self, clave, lista) {
							var claves = self.py_keys (clave);
							var indice = self.l_claves.index (claves);
							var __iterable0__ = lista;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (!(__in__ (elem, self.l_claves [indice])) && !(__in__ (elem, self.keys_all ()))) {
									self.l_claves [indice].append (elem);
								}
							}
						});},
						get key () {return __get__ (this, function (self, clave1, clave2) {
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var indice = self.l_claves.index (elem);
								self.l_claves [indice] = list (self.l_claves [indice]);
								if (__in__ (clave1, self.l_claves [indice]) && !(__in__ (clave2, self.keys_all ()))) {
									self.l_claves [indice].append (clave2);
								}
							}
						});},
						get py_keys () {return __get__ (this, function (self, clave) {
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (clave, elem)) {
									var indice = self.l_claves.index (elem);
								}
							}
							return self.l_claves [indice];
						});},
						get keys_p () {return __get__ (this, function (self) {
							return self.d.py_keys ();
						});},
						get keys_p2 () {return __get__ (this, function (self, clave) {
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (clave, elem)) {
									return elem [0];
								}
							}
						});},
						get keys_all () {return __get__ (this, function (self) {
							var l = list ([]);
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var __iterable1__ = elem;
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var elem2 = __iterable1__ [__index1__];
									l.append (elem2);
								}
							}
							return l;
						});},
						get fusionar () {return __get__ (this, function (self, dic, sobrescribir) {
							if (typeof sobrescribir == 'undefined' || (sobrescribir != null && sobrescribir .hasOwnProperty ("__kwargtrans__"))) {;
								var sobrescribir = false;
							};
							var __iterable0__ = dic.keys_p ();
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.set2 (dic.py_get (elem), dic.py_keys (elem));
							}
						});},
						get show () {return __get__ (this, function (self) {
							print ('<');
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								print (elem, ':', self.d [elem [0]]);
							}
							print ('>');
						});}
					});
					var get_tab = function (cadena, palabra) {
						var l = cadena.py_split ('\n');
						var columna = '';
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (palabra, elem)) {
								var columna = elem;
							}
						}
						var x1 = 0;
						var x2 = 1;
						while (columna.__getslice__ (x1, x2, 1) == ' ' || columna.__getslice__ (x1, x2, 1) == '\t') {
							x1++;
							x2++;
						}
						return x1;
					};
					var get_tab2 = function (cadena, palabra) {
						var l = cadena.py_split ('\n');
						var columna = '';
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (palabra, elem)) {
								var columna = elem;
							}
						}
						var x1 = 0;
						var x2 = 1;
						while (columna.__getslice__ (x1, x2, 1) == ' ' || columna.__getslice__ (x1, x2, 1) == '\t') {
							x1++;
							x2++;
						}
						return columna.__getslice__ (0, x1, 1);
					};
					var tabular = function (cadena, tabs) {
						var l = cadena.py_split ('\n');
						if (py_typeof (tabs) == str) {
							var __iterable0__ = l;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								l [l.index (elem)] = tabs + elem;
							}
						}
						if (py_typeof (tabs) == int) {
							var __iterable0__ = l;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								l [l.index (elem)] = ' ' * tabs + elem;
							}
						}
						var cadena = '';
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							cadena += elem + '\n';
						}
						return cadena;
					};
					var listar_elem = function (palabra, numero) {
						var l = list ([]);
						for (var elem = 0; elem < numero; elem++) {
							l.append (palabra + str (elem));
						}
						return str (l).py_replace ("'", '');
					};
					var diccionar_elem = function (palabra, numero, medio, retorno) {
						if (typeof medio == 'undefined' || (medio != null && medio .hasOwnProperty ("__kwargtrans__"))) {;
							var medio = '';
						};
						if (typeof retorno == 'undefined' || (retorno != null && retorno .hasOwnProperty ("__kwargtrans__"))) {;
							var retorno = 0;
						};
						var l = list ([]);
						var cadena = '';
						for (var elem = 0; elem < numero; elem++) {
							l.append (palabra + str (elem));
						}
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							cadena += (('[' + elem) + ']') + medio;
						}
						if (retorno > 0) {
							return cadena.__getslice__ (0, -(retorno), 1);
						}
						else if (retorno < 0) {
							return cadena.__getslice__ (0, retorno, 1);
						}
						else if (retorno == 0) {
							return cadena;
						}
					};
					var mapear = function (dic, niveles, mapeo) {
						if (typeof niveles == 'undefined' || (niveles != null && niveles .hasOwnProperty ("__kwargtrans__"))) {;
							var niveles = 1;
						};
						if (typeof mapeo == 'undefined' || (mapeo != null && mapeo .hasOwnProperty ("__kwargtrans__"))) {;
							var mapeo = 'claves';
						};
						if (niveles > 20) {
							var niveles = 20;
						}
						var l = list ([]);
						var base = 'for elem0 in dic:\n if type(dic[elem0])==dict:\n  if dic[elem0].keys()!=[]:\n   l.append([elem0])\n   pass\n  else:\n   l.append([elem0])\n else:\n  l.append([elemento])';
						var base2 = base;
						var codigo = base;
						var lista = 'l.append([elem0])';
						for (var elem = 0; elem < niveles; elem++) {
							if (elem != 0) {
								var base2 = base2.py_replace ('dic[elem0]', 'dic' + diccionar_elem ('elem', elem + 1));
								var base2 = base2.py_replace ('dic:', ('dic' + diccionar_elem ('elem', elem)) + ':');
								var base2 = base2.py_replace ('for elem0', 'for elem' + str (elem));
								var base2 = base2.py_replace (lista, lista.py_replace ('[elem0]', listar_elem ('elem', elem + 1)));
								if (mapeo == 'claves') {
									var base2 = base2.py_replace ('([elemento])', ('([' + listar_elem ('elem', elem + 1)) + '])');
								}
								if (mapeo == 'valores') {
									var base2 = base2.py_replace ('([elemento])', ((('(' + listar_elem ('elem', elem + 1).__getslice__ (0, -(1), 1)) + ',dic') + diccionar_elem ('elem', elem + 1)) + '])');
								}
								var base2 = tabular (base2, get_tab2 (codigo, 'pass'));
								var l_codigo = codigo.py_split ('\n');
								var __iterable0__ = l_codigo;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem2 = __iterable0__ [__index0__];
									if (__in__ ('pass', elem2)) {
										l_codigo [l_codigo.index (elem2)] = base2;
									}
								}
								var codigo = concatenar2 (l_codigo);
								var base2 = base;
							}
						}
						exec (codigo);
						return l;
					};
					var buscar_ruta = function (dic, palabra, niveles, todo, mapeo) {
						if (typeof niveles == 'undefined' || (niveles != null && niveles .hasOwnProperty ("__kwargtrans__"))) {;
							var niveles = 1;
						};
						if (typeof todo == 'undefined' || (todo != null && todo .hasOwnProperty ("__kwargtrans__"))) {;
							var todo = 'todo';
						};
						if (typeof mapeo == 'undefined' || (mapeo != null && mapeo .hasOwnProperty ("__kwargtrans__"))) {;
							var mapeo = 'claves';
						};
						var l = mapear (dic, niveles, mapeo);
						var l_temp = list ([]);
						var l_remover = list ([]);
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (elem.count (palabra) >= 1) {
								l_temp.append (elem);
							}
						}
						if (mapeo == 'calves') {
							if (todo == 'solo') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 1] != palabra) {
										l_remover.append (elem);
									}
								}
								var __iterable0__ = l_remover;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									l_temp.remove (elem);
								}
							}
							if (todo == 'claves ruta') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 2] != palabra) {
										l_remover.append (elem);
									}
								}
								var __iterable0__ = l_remover;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									l_temp.remove (elem);
								}
							}
							if (todo == 'claves') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 1] != palabra && elem [len (elem) - 2] == palabra) {
										l_remover.append (elem [len (elem) - 1]);
									}
								}
								var l_temp = l_remover;
							}
							if (todo == 'padre') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									var l_temp = list ([]);
									if (__in__ (palabra, elem)) {
										var indice = elem.index (palabra);
										if (indice > 0) {
											l_temp.append (elem [indice - 1]);
										}
									}
								}
							}
						}
						if (mapeo == 'valores') {
							if (todo == 'solo') {
								var l2 = list ([]);
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 1] == palabra) {
										l2.append (elem);
									}
								}
								var l_temp = l2;
							}
						}
						return l_temp;
					};
					var unir_key_map = function (lista) {
						var l = list ([]);
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (len (elem) > 0) {
								l.append (elem [1]);
							}
							else {
								l.append (elem [0]);
							}
						}
						return l;
					};
					var estaEn = function (lista, cadena) {
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (elem, lista)) {
								return true;
							}
						}
						return false;
					};
					var movPosList = function (l, posActual, nuevaPos) {
						var lista = l;
						var elem = lista [posActual];
						delete lista [posActual];
						lista.insert (nuevaPos, elem);
						return lista;
					};
					var movPosStr = function (cadena, posActual, nuevaPos) {
						var espacio = '';
						var palabra = '';
						var espacios = list ([]);
						var palabras = list ([]);
						var c = 0;
						var primero = null;
						while (c < len (cadena)) {
							if (cadena [c] == ' ' || cadena [c] == '\n' || cadena [c] == '\t') {
								espacio += cadena [c];
								if (primero == null) {
									var primero = true;
								}
							}
							else if (espacio != '') {
								espacios.append (espacio);
								var espacio = '';
							}
							if (cadena [c] != ' ' && cadena [c] != '\n' && cadena [c] != '\t') {
								palabra += cadena [c];
								if (primero == null) {
									var primero = false;
								}
							}
							else {
								palabras.append (palabra);
								var palabra = '';
							}
							print ('cadena: ', list ([cadena [c]]));
							print (palabra);
							print (espacio);
							c++;
						}
						if (palabra != '') {
							palabras.append (palabra);
						}
						if (espacio != '') {
							espacios.append (espacio);
						}
						var palabras = movPosList (palabras, posActual, nuevaPos);
						print (palabras);
						var cadena = '';
						if (primero == true) {
							var c = 0;
							while (c < len (espacios)) {
								cadena += espacios [c];
								if (c < len (palabra)) {
									cadena += palabras [c];
								}
								c++;
							}
						}
						else if (primero == false) {
							var c = 0;
							while (c < len (palabras)) {
								cadena += palabras [c];
								if (c < len (espacios)) {
									cadena += espacios [c];
								}
								c++;
							}
						}
						return cadena;
					};
					var haveFolder = function (path) {
						var __iterable0__ = os.listdir (path);
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (os.isdir ((path + '/') + elem)) {
								return true;
							}
						}
						return false;
					};
					var rstr = function (cadena, sub, vez) {
						var cadena2 = '';
						var c = len (cadena) - 1;
						while (c >= 0) {
							var cadena2 = cadena [c] + cadena2;
							if (cadena2.count ('/') == vez) {
								return cadena2;
							}
							c--;
						}
					};
					var reKeyIn = function (patron, lista) {
						if (!__in__ ('*', patron)) {
							if (__in__ ('[', patron)) {
								// pass;
							}
						}
					};
					var getPattern = function (lista) {
						var exp1 = list ([]);
						var similitudes = list ([]);
						var previo = null;
						var iguallong = true;
						var temp = null;
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (temp == null) {
								var temp = len (elem);
							}
							else if (len (elem) != temp) {
								var iguallong = false;
							}
						}
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (previo != null) {
								var __iterable1__ = enumerate (previo);
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var __left0__ = __iterable1__ [__index1__];
									var k = __left0__ [0];
									var ch = __left0__ [1];
									if (ch == elem [k]) {
										if (similitudes == list ([])) {
											similitudes.append (elem [k]);
										}
										else {
											similitudes [-(1)] += elem [k];
										}
									}
									else if (k + 2 < len (previo)) {
										var temp = '';
										var __iterable2__ = enumerate (previo);
										for (var __index2__ = 0; __index2__ < len (__iterable2__); __index2__++) {
											var __left0__ = __iterable2__ [__index2__];
											var k2 = __left0__ [0];
											var ch2 = __left0__ [1];
											if (ch2 != elem [k2]) {
												temp += elem [k2];
											}
											else {
												if (!__in__ (elem.__getslice__ (k, null, 1), exp1)) {
													exp1.append (temp);
												}
												break;
											}
										}
									}
									else {
										if (!__in__ (elem.__getslice__ (k, null, 1), exp1)) {
											exp1.append (elem.__getslice__ (k, null, 1));
										}
										break;
									}
								}
							}
							else {
								var previo = elem;
							}
						}
					};
					var iterRelacionado = function () {
					};
					var filtrar_datos_planos = function (data) {
						if (py_typeof (data) == dict) {
							var d = dict ({});
							var __iterable0__ = data;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								d [elem] = filtrar_datos_planos (data [elem]);
							}
							return d;
						}
						else if (py_typeof (data) == list || py_typeof (data) == tuple) {
							var l = list ([]);
							var __iterable0__ = data;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								l.append (filtrar_datos_planos (elem));
							}
							return l;
						}
						else if (py_typeof (data) == int || py_typeof (data) == float || py_typeof (data) == str || py_typeof (data) == bool) {
							return data;
						}
					};
					var filtrar_del_dict = function (diccionario, py_keys) {
						var d = dict ({});
						var __iterable0__ = py_keys;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (elem, diccionario)) {
								d [elem] = diccionario [elem];
							}
						}
						return d;
					};
					__pragma__ ('<use>' +
						'math' +
					'</use>')
					__pragma__ ('<all>')
						__all__.__name__ = __name__;
						__all__.add = add;
						__all__.add2 = add2;
						__all__.buscar_ruta = buscar_ruta;
						__all__.ciento = ciento;
						__all__.ciento2 = ciento2;
						__all__.cmpString = cmpString;
						__all__.compilarLambda = compilarLambda;
						__all__.concatenar = concatenar;
						__all__.concatenar2 = concatenar2;
						__all__.css_convert = css_convert;
						__all__.css_posicionamiento = css_posicionamiento;
						__all__.dicc = dicc;
						__all__.diccionar_elem = diccionar_elem;
						__all__.diferenciar = diferenciar;
						__all__.dimensionar = dimensionar;
						__all__.estaEn = estaEn;
						__all__.filtrar_datos_planos = filtrar_datos_planos;
						__all__.filtrar_del_dict = filtrar_del_dict;
						__all__.finIndex = finIndex;
						__all__.getPattern = getPattern;
						__all__.getTab = getTab;
						__all__.get_tab = get_tab;
						__all__.get_tab2 = get_tab2;
						__all__.haveFolder = haveFolder;
						__all__.invertString = invertString;
						__all__.iterRelacionado = iterRelacionado;
						__all__.listar_d = listar_d;
						__all__.listar_elem = listar_elem;
						__all__.mapear = mapear;
						__all__.mayor = mayor;
						__all__.mayor_f = mayor_f;
						__all__.movPosList = movPosList;
						__all__.movPosStr = movPosStr;
						__all__.nu2 = nu2;
						__all__.ordLargString = ordLargString;
						__all__.ordenLargString = ordenLargString;
						__all__.poligono = poligono;
						__all__.por = por;
						__all__.posicionar = posicionar;
						__all__.randomString = randomString;
						__all__.reKeyIn = reKeyIn;
						__all__.rect_radius = rect_radius;
						__all__.rect_radius2 = rect_radius2;
						__all__.remplazarFueraString = remplazarFueraString;
						__all__.restar = restar;
						__all__.rstr = rstr;
						__all__.separar = separar;
						__all__.siguienteNivel = siguienteNivel;
						__all__.tabular = tabular;
						__all__.tipo = tipo;
						__all__.tipo_v = tipo_v;
						__all__.u = u;
						__all__.u2 = u2;
						__all__.unir_key_map = unir_key_map;
					__pragma__ ('</all>')
				}
			}
		}
	);
