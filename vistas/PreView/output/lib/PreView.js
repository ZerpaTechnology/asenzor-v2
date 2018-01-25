/* start module: PreView */
$pyjs['loaded_modules']['PreView'] = function (__mod_name__) {
	if($pyjs['loaded_modules']['PreView']['__was_initialized__']) return $pyjs['loaded_modules']['PreView'];
	var $m = $pyjs['loaded_modules']['PreView'];
	$m['__repr__'] = function() { return '<module: PreView>'; };
	$m['__was_initialized__'] = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'PreView';
	$m['__name__'] = __mod_name__;


	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['SimplePanel'] = $p['___import___']('pyjamas.ui.SimplePanel.SimplePanel', null, null, false);
	$m['alert'] = $p['___import___']('pyjamas.Window.alert', null, null, false);
	$m['PreView'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition['__module__'] = 'PreView';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this['__is_instance__'] === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var script,f;
			$m['SimplePanel']['__init__'](self);
			f = $p['open']('texto.txt', 'r');
			script = f['read']();
			f['close']();
			$m['alert'](script);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		var $bases = new Array($m['SimplePanel']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data['__setitem__']($item, $cls_definition[$item]); }
		return $p['_create_class']('PreView', $p['tuple']($bases), $data);
	})();
	if ($p['bool']($p['op_eq']((typeof __name__ == "undefined"?$m['__name__']:__name__), '__main__'))) {
		$m['RootPanel']()['add']($m['PreView']());
	}
	return this;
}; /* end PreView */


/* end module: PreView */


/*
PYJS_DEPS: ['pyjamas.ui.RootPanel.RootPanel', 'pyjamas', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.SimplePanel.SimplePanel', 'pyjamas.ui.SimplePanel', 'pyjamas.Window.alert', 'pyjamas.Window']
*/
