	(function () {
		var __name__ = '__main__';
		var config = Config.Config ();
		var scroll = function (evt, clase, grosor, posIni) {
			if (typeof clase == 'undefined' || (clase != null && clase .hasOwnProperty ("__kwargtrans__"))) {;
				var clase = '.text-parallax';
			};
			if (typeof grosor == 'undefined' || (grosor != null && grosor .hasOwnProperty ("__kwargtrans__"))) {;
				var grosor = 45;
			};
			if (typeof posIni == 'undefined' || (posIni != null && posIni .hasOwnProperty ("__kwargtrans__"))) {;
				var posIni = 70;
			};
			var activar = false;
			var __iterable0__ = enumerate ($ (clase));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				elem.style.transform = ('translate3d(0px,' + str (elem.parentNode.getBoundingClientRect ().top * 1.5 - posIni)) + 'px,-100px)';
				elem.style.webkitTransform = ('translate3d(0px,' + str (elem.parentNode.getBoundingClientRect ().top * 1.5 - posIni)) + 'px,-100px)';
				elem.style.MozTransform = ('translate3d(0px,' + str (elem.parentNode.getBoundingClientRect ().top * 1.5 - posIni)) + 'px,-100px)';
				elem.style.OTransform = ('translate3d(0px,' + str (elem.parentNode.getBoundingClientRect ().top * 1.5 - posIni)) + 'px,-100px)';
				elem.style.msTransform = ('translate3d(0px,' + str (elem.parentNode.getBoundingClientRect ().top * 1.5 - posIni)) + 'px,-100px)';
				if ($ (elem.children [0]).hasClass ('hidden')) {
					$ (elem.children [0]).removeClass ('hidden');
				}
			}
		};
		var render = function (evt, clase) {
			if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
				var evt = null;
			};
			if (typeof clase == 'undefined' || (clase != null && clase .hasOwnProperty ("__kwargtrans__"))) {;
				var clase = '.text-parallax';
			};
			var __iterable0__ = enumerate ($ (clase));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				elem.children [0].style.left = str (window.screen.width / 2 - elem.clientWidth / 2) + 'px';
				elem.style.width = '100%';
			}
		};
		render ();
		window.addEventListener ('scroll', scroll, true);
		window.addEventListener ('orientationchange', render, true);
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.config = config;
			__all__.render = render;
			__all__.scroll = scroll;
		__pragma__ ('</all>')
	}) ();
