	(function () {
		var __name__ = '__main__';
		var flash_help = function (evt) {
			if ($ ('#flash-help').hasClass ('hidden')) {
				$ ('#flash-help').removeClass ('hidden');
			}
			else {
				$ ('#flash-help').addClass ('hidden');
			}
		};
		$ ('#ayuda').bind ('click', flash_help);
		var flash_info = function (evt) {
			var __iterable0__ = enumerate ($ ('.info'));
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var elem = __left0__ [1];
				if (elem.text == $ ('.btn-flash-info') [k].text) {
					if ($ (elem).hasClass ('hidden')) {
						$ ($ ('.info') [k]).removeClass ('hidden');
					}
					else {
						$ ($ ('.info') [k]).addClass ('hidden');
					}
				}
			}
		};
		$ ('.btn-flash-info').bind ('click', flash_info);
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.flash_help = flash_help;
			__all__.flash_info = flash_info;
		__pragma__ ('</all>')
	}) ();
