	(function () {
		var __name__ = '__main__';
		var config = window.config;
		var checkear = function () {
			var cookies = nuclear.getCookie ();
			if ((__in__ ('token', cookies) && cookies ['token'] == '') && (__in__ ('token2', cookies) && cookies ['token2'] == '')) {
				$ ('#login').removeClass ('hidden');
			}
			else {
				$ ('#login').addClass ('hidden');
			}
		};
		window.setInterval (checkear, 1000);
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.checkear = checkear;
			__all__.config = config;
		__pragma__ ('</all>')
	}) ();
