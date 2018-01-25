	(function () {
		var __name__ = '__main__';
		var Builder = __init__ (__world__.Builder).Builder;
		var b = Builder ();
		b.run ($ ('section'));
		b.appendRow ();
		b.appendRow ();
		__pragma__ ('<use>' +
			'Builder' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Builder = Builder;
			__all__.__name__ = __name__;
			__all__.b = b;
		__pragma__ ('</all>')
	}) ();
