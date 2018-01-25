	(function () {
		var __name__ = '__main__';
		var Config = __class__ ('Config', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self) {
				self.seo_url = '<%=config.seo_url%>';
				self.version = '<%=config.version%>';
				self.controller_folder = '<%=config.controller_folder%>';
				self.asenzor_host = '<%=config.asenzor_host%>';
				self.apps = '<%=config.apps%>';
				self.base_url = '<%=config.base_url%>';
				self.default_app = '<%=config.default_app%>';
			});}
		});
		window.config = Config ();
		__pragma__ ('<all>')
			__all__.Config = Config;
			__all__.__name__ = __name__;
		__pragma__ ('</all>')
	}) ();
