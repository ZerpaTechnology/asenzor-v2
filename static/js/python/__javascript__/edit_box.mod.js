	(function () {
		var __name__ = '__main__';
		$ ("input[type='datetime']").datepicker ();
		var VAR = nuclear.VAR;
		var normalizar = nuclear.normalizar;
		var doc = document;
		var config = window.config;
		var opciones = null;
		var seccion = true;
		var current_section = null;
		var tablas = null;
		var Tabla = null;
		var rest = nuclear.getRest ();
		var modelos = VAR ('modelos');
		var tablas = VAR ('Tablas');
		var opciones = VAR ('opciones');
		var decode = Codificador.Codificador.decode;
		var thumbails = function (cadena, sujifo) {
			if (typeof sujifo == 'undefined' || (sujifo != null && sujifo .hasOwnProperty ("__kwargtrans__"))) {;
				var sujifo = '_540x540';
			};
			return (cadena.__getslice__ (0, cadena.rfind ('.'), 1) + sujifo) + cadena.__getslice__ (cadena.rfind ('.'), null, 1);
		};
		var cambiar = function (evt) {
			var out = evt.target;
			var valor = out.value;
			var imagen = '';
			var __iterable0__ = enumerate ($ (out).find ('option'));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var option = __left0__ [1];
				if (int (valor) == k) {
					var imagen = option.text;
					break;
				}
			}
			var opcion = out.getAttribute ('opcion');
			$ ($ (out.parent).find ('img') [0]).removeClass ('hidden');
			var url = ((((config.base_url + '/apps/') + rest ['app']) + '/admin/static/archivos/') + ($ (out.parentNode).find ('img') [0].getAttribute ('archivos').strip () == '' ? 'Imagenes' : $ (out.parentNode).find ('img') [0].getAttribute ('archivos').strip ())) + '/';
			$.get(url+thumbails(imagen)).done(function(){
			      $(out.parentNode).find("img")[0].src=url+thumbails(imagen);
			      }).fail(
			      function(){
			      $(out.parentNode).find("img")[0].src=url+imagen;
			      }
			      )
		};
		$ ('.img-admin').bind ('change', cambiar);
		var componentes = dict ({'widget-campo-box': $.get(config.base_url+settings.app+'/admin/Show/layout/admin/widgets/widget-campo-box.html/action=componer/')
		, 'widget-campo': $.get(config.base_url+settings.app+'/admin/Show/layout/admin/widgets/widget-campo.html/action=componer/')
		, 'widget-campo-boxes': $.get(config.base_url+settings.app+'/admin/Show/layout/admin/widgets/widget-campo-boxes.html/action=componer/')
		});
		var upload_image = function (evt) {
			var file = $ ('.img-file').prop ('files') [0];
			var reader = new FileReader ();
			var imagen = $ (evt.target.parentNode).find ('img') [0];
			var pasarImagen = function (imagen) {
				var funcion = function (evt, img) {
					if (typeof img == 'undefined' || (img != null && img .hasOwnProperty ("__kwargtrans__"))) {;
						var img = imagen;
					};
					$ (img).removeClass ('hidden');
					img.src = evt.target.result;
				};
				return funcion;
			};
			reader.onload = pasarImagen (imagen);
			var f = reader.readAsDataURL (file);
		};
		var customOpen = function (evt) {
			if ($ ('#custom').hasClass ('hidden')) {
				seccion = (evt.target.id == '#add' ? true : false);
				$ ('#custom').removeClass ('hidden');
			}
		};
		$ ('#add').bind ('click', customOpen);
		$ ('#add2').bind ('click', customOpen);
		var nuevaSeccion = function (evt) {
			var ultimo = 0;
			var data = dict ({});
			data ['opciones'] = (opciones != null ? opciones : list ([]));
			data ['tablas'] = tablas;
			var __iterable0__ = enumerate ($ ('.custom'));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				if (len (elem.children) == 0) {
					if (ultimo == null) {
						var ultimo = k;
					}
				}
				else {
					var ultimo = null;
				}
			}
			var agregar = false;
			var __iterable0__ = $ ('#custom .tab') [0].children;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				if (len (elem.children) > 0) {
					var agregar = true;
				}
			}
			if (agregar == true && len ($ ('.botonera') [0].py_get (__kwargtrans__ ({py_selector: '#agregar'}))) == 0) {
				$ ('.botonera').widget (-(1), "<button id='agregar'>Agregar</button>");
				var agregar = function (evt) {
					var ultimo = 0;
					var data = dict ({'boxes': list ([])});
					var l = list ([]);
					var __iterable0__ = $ ('.tab') [0].children;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if (len (elem.children) > 0) {
							var widget = elem.children [0];
							var tipo = $ (widget).find ('select[name=tipo]') [0].value;
							var py_name = $ (widget).find ('input[name=name]') [0].value;
							var valor = $ (widget).find ('input[name=value]') [0].value;
							var titulo = $ (widget).find ('input[name=titulo]') [0].value;
							var opcion = $ (widget).find ('select[name=opcion]') [0].value;
							var tabla = $ (widget).find ('select[name=tabla]') [0].value;
							var depende = $ (widget).find ('input[name=depende]') [0].value;
							var modelo = $ (widget).find ('select[name=opciones]') [0].value;
							var campo = dict ([[titulo, tipo], ['name', py_name], ['value', valor]]);
							if (opcion != '') {
								campo ['opcion'] = opcion;
							}
							if (modelo != '') {
								campo ['opciones'] = modelo;
							}
							if (tabla != '') {
								campo ['tabla'] = tabla;
							}
							if (depende != '') {
								campo ['depende'] = depende;
							}
							if (tipo == 'number') {
								campo ['max'] = _max;
								campo ['min'] = _min;
								campo ['step'] = step;
							}
							l.append (campo);
						}
					}
					data ['boxes'].append (l);
					var __iterable0__ = enumerate ($ ((seccion == true ? '.custom-section' : '.custom-subsection')).iterables);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						if (len (elem.children) == 0) {
							if (ultimo == null) {
								var ultimo = k;
							}
						}
						else {
							var ultimo = null;
						}
					}
					var __iterable0__ = $ ('.tab') [0].children;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if (len (elem.children) > 0) {
							var temp = elem.children [0];
							elem.removeChild (temp);
						}
					}
					$ ('#custom').addClass ('hidden');
					if (componentes ['widget-campo-boxes'] != null && ultimo != null) {
						$ ((seccion == true ? '.custom-section' : '.custom-subsection')) [ultimo].innerHTML = componentes ['widget-campo-boxes'].run (data);
						if (len ($ ('.botoneraCustom') [0].py_get (__kwargtrans__ ({py_selector: '#borrarCustom'}))) == 0) {
							var borrarCustom = function (evt) {
								var __iterable0__ = enumerate ($ ((seccion == true ? '.custom-section' : '.custom-subsection')).iterables);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									if (len (elem.children) == 0) {
										if (ultimo == null) {
											var ultimo = k;
										}
									}
									else {
										var ultimo = null;
									}
								}
								if (ultimo != null && ultimo != 0) {
									var __iterable0__ = $ ((seccion == true ? '.custom-section' : '.custom-subsection')) [ultimo - 1].children;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										$ ((seccion == true ? '.custom-section' : '.custom-subsection')) [ultimo - 1].removeChild (elem);
										if (ultimo - 1 == 0) {
											$ ('.botoneraCustom') [0].removeChild ($ ('.botoneraCustom') [0].find ('#borrarCustom') [0]);
										}
									}
								}
							};
							$ ('.botoneraCustom').widget (-(1), '<a class="pad-05 b-r5 marg-t1 btn bg-ubuntu_red font-ubuntu white" style="text-decoration: none" href="#borrarCustom" id="borrarCustom">Borrar sección personalizada</a>');
							$ ('#borrarCustom') [0].bind ('click', borrarCustom);
						}
					}
				};
				$ ('#agregar').bind ('click', agregar);
			}
		};
		$ ('.insertar').bind ('click', nuevaSeccion);
		var customClose = function (evt) {
			evt.target._ev = customClose;
			if ($ ('#custom').hasClass ('hidden')) {
				$ ('#custom').removeClass ('hidden');
			}
			else {
				$ ('#custom').addClass ('hidden');
			}
		};
		$ ('#custom-close').bind ('click', customClose);
		$ ('.img-file').bind ('change', upload_image);
		var borrar = function (evt) {
			evt.target._ev = borrar;
			var __iterable0__ = $ ('#custom .tab') [0].children;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				if (len (elem.children [0].children) > 0) {
					if (elem.children [0].children [0].children [0].checked == true) {
						$ (elem).removeChild (elem.children [0]);
					}
				}
			}
			var agregar = false;
			var __iterable0__ = $ ('#custom .tab') [0].children;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				if (len (elem.children) > 0) {
					var agregar = true;
				}
			}
			if (agregar == false) {
				var el = $ ('.botonera').find (__kwargtrans__ ({py_selector: '#agregar'})) [0];
				$ ('.botonera') [0].removeChild (el);
			}
		};
		$ ('.borrar').bind ('click', borrar);
		var customOpen2 = function (evt) {
			if (__in__ ('hidden', $ ('#custom2') [0].class_name)) {
				seccion = (evt.target.id == '#add' ? true : false);
				$ ('#custom2').removeClass ('hidden');
				current_section = evt.target;
			}
		};
		$ ('.agregar-custom2').bind ('click', customOpen2);
		var customClose2 = function (evt) {
			if ($ ('#custom2').havClass ('hidden')) {
				$ ('#custom2').removeClass ('hidden');
			}
			else {
				$ ('#custom2').addClass ('hidden');
			}
		};
		$ ('#custom-close2').bind ('click', customClose2);
		var nuevoCampo = function (evt) {
			var campo = dict ({});
			var widget = $ ('#custom2 .tab') [0].children [0];
			var tipo = $ (widget).find ('select[name=tipo]') [0].value;
			var py_name = $ (widget).find ('input[name=name]') [0].value;
			var valor = $ (widget).find ('input[name=value]') [0].value;
			var titulo = $ (widget).find ('input[name=titulo]') [0].value;
			var opcion = $ (widget).find ('select[name=opcion]') [0].value;
			var tabla = $ (widget).find ('select[name=tabla]') [0].value;
			var depende = $ (widget).find ('input[name=depende]') [0].value;
			var modelo = $ (widget).find ('select[name=opciones]') [0].value;
			var campo = dict ([[titulo, tipo], ['name', py_name], ['value', valor]]);
			if (opcion != '') {
				campo ['opcion'] = int (opcion);
			}
			if (opcion != '') {
				campo ['opciones'] = modelo;
			}
			if (tabla != '') {
				campo ['tabla'] = tabla;
			}
			if (depende != '') {
				campo ['depende'] = depende;
			}
			if (tipo == 'number') {
				campo ['max'] = _max;
				campo ['min'] = _min;
				campo ['step'] = step;
			}
			var data = dict ({'campo': campo});
			data ['opciones'] = VAR ('opciones');
			if (current_section != null) {
				var i = list (current_section.parent.children).index (current_section);
				data ['indice'] = len ($ (current_section.parentNode.children [i - 1]).find ("input[name^='custom:']")) + len ($ (current_section.parentNode.children [i - 1]).find ("select[name^='custom:']"));
				$ (current_section.parent.children [i - 1]).widget (-(1), componentes ['widget-campo-box'].run (data));
				$ ('.img-admin').bind ('change', cambiar);
			}
			customClose2 (evt);
		};
		var modificar_atributo = function () {
			var meta = dict ({'control': $ ("select[name='atributo-control']") [0].value, 'layout': $ ("select[name='atributo-layout']") [0].value});
			$ ('#form') [0].action = ($ ('#form') [0].action + '&metadatos=') + str (meta);
			var titulos = VAR ('titulos');
			titulos.remove (VAR ('actual'));
			if ($ ("input[name='titulo']") [0].value.strip () != '') {
				if (__in__ ($ ("input[name='titulo']") [0].value, titulos)) {
					alert ('Este titulo no esta permitido, ya existe');
					return false;
				}
				else {
					return true;
				}
			}
		};
		window.modificar_atributo = modificar_atributo;
		$ ('#custom2 .agregar').bind ('click', nuevoCampo);
		__pragma__ ('<all>')
			__all__.Tabla = Tabla;
			__all__.VAR = VAR;
			__all__.__name__ = __name__;
			__all__.borrar = borrar;
			__all__.cambiar = cambiar;
			__all__.componentes = componentes;
			__all__.config = config;
			__all__.current_section = current_section;
			__all__.customClose = customClose;
			__all__.customClose2 = customClose2;
			__all__.customOpen = customOpen;
			__all__.customOpen2 = customOpen2;
			__all__.decode = decode;
			__all__.doc = doc;
			__all__.modelos = modelos;
			__all__.modificar_atributo = modificar_atributo;
			__all__.normalizar = normalizar;
			__all__.nuevaSeccion = nuevaSeccion;
			__all__.nuevoCampo = nuevoCampo;
			__all__.opciones = opciones;
			__all__.rest = rest;
			__all__.seccion = seccion;
			__all__.tablas = tablas;
			__all__.thumbails = thumbails;
			__all__.upload_image = upload_image;
		__pragma__ ('</all>')
	}) ();
