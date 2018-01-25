	(function () {
		var __name__ = '__main__';
		var rest = window.rest;
		var config = Config.Config ();
		var Component = nuclear.Component;
		var Components = dict ({'builder-box': Component ('builder-box', dict ({}), true, true, true)});
		if (rest ['action'] == 'personalizar') {
			$ ('[builder]').append ("<span class='builder'></span>");
			$ ('[builder]').append (Components ['builder-box'].run ());
			$ ('.builder').css (dict ({'background-image': ("url('" + config.base_url) + "static/imgs/iconos/pencil_blue.png')", 'height': '30px', 'width': '30px', 'position': 'absolute', 'top': '0px', 'left': '0px', 'background-size': 'cover', 'cursor': 'pointer'}));
			$ ('.builder-box').css (dict ({'width': '300px', 'height': '300px', 'position': 'relative', 'top': '0px', 'left': '0px', 'border': 'solid', 'border-width': '1px'}));
			var consultarConfiguracion = function (evt) {
				// pass;
			};
			$ ('.builder').bind ('click', consultarConfiguracion);
		}
		__pragma__ ('<all>')
			__all__.Component = Component;
			__all__.Components = Components;
			__all__.__name__ = __name__;
			__all__.config = config;
			__all__.consultarConfiguracion = consultarConfiguracion;
			__all__.rest = rest;
		__pragma__ ('</all>')
	}) ();
