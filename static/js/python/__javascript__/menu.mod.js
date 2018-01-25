	(function () {
		var __name__ = '__main__';
		var l = list ([]);
		var __iterable0__ = $ ('.menu');
		for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
			var elem = __iterable0__ [__index0__];
			l.append (elem.text);
		}
		var change = function (evt) {
			evt.preventDefault ();
			try {
				if (str (evt.target) == '<HTMLSpanElement object>') {
					var __iterable0__ = $ ('.menu').iterables;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if (elem.children [0] == evt.target) {
							$ (evt.target.parent).addClass ('bg-bluelight');
						}
						else {
							$ (elem.parent).removeClass ('bg-bluelight');
							$ (elem).removeClass ('bg-bluelight');
						}
					}
				}
				else {
					var __iterable0__ = $ ('.menu').iterables;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if (elem == evt.target) {
							$ (evt.target).addClass ('bg-bluelight');
						}
						else {
							$ (elem.parent).removeClass ('bg-bluelight');
							$ (elem).removeClass ('bg-bluelight');
						}
					}
				}
				var indice = l.index (evt.target.text);
				var subs = $ ('.sub');
				if (__in__ ('hidden', subs [indice].class_name)) {
					var __iterable0__ = subs;
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var elem = __iterable0__ [__index0__];
						if (!__in__ ('hidden', elem.class_name)) {
							elem.class_name += ' hidden';
						}
					}
					subs [indice].class_name = subs [indice].class_name.py_replace ('hidden', '');
				}
				else {
					subs [indice].class_name += ' hidden';
				}
			}
			catch (__except0__) {
				if (isinstance (__except0__, Exception)) {
					var e = __except0__;
					window.alert (e);
					window.alert ('===');
				}
				else {
					throw __except0__;
				}
			}
		};
		var change = function (evt) {
			var __iterable0__ = enumerate ($ ('#main-menu').find ("span[name='menu']"));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				if (elem != evt.target) {
					$ (elem).removeClass ('bg-bluelight');
					$ (elem.parentNode.children [1]).addClass ('hidden');
				}
				else {
					$ (evt.target).addClass ('bg-bluelight');
					$ (evt.target.parentNode.children [1]).removeClass ('hidden');
				}
			}
		};
		var __iterable0__ = enumerate ($ ('#main-menu').find ("span[name='menu']"));
		for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
			var __left0__ = __iterable0__ [__index0__];
			var k = __left0__ [0];
			var elem = __left0__ [1];
			$ (elem).bind ('click', change);
		}
		var change2 = function (evt) {
			if ($ ('#menu').hasClass ('hidden')) {
				$ ('#menu').removeClass ('hidden');
				$ ('#content').removeClass ('col-sm-offset-1');
				$ ('#content').addClass ('col-sm-offset-2');
			}
			else {
				$ ('#menu').addClass ('hidden');
				$ ('#content').addClass ('col-sm-offset-1');
				$ ('#content').removeClass ('col-sm-offset-2');
			}
		};
		$ ('#btn-menu').bind ('click', change2);
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.change = change;
			__all__.change2 = change2;
			__all__.elem = elem;
			__all__.k = k;
			__all__.l = l;
		__pragma__ ('</all>')
	}) ();
