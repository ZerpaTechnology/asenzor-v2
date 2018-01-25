	__nest__ (
		__all__,
		're', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 're';
					var translate = __init__ (__world__.translate).translate;
					var MatchObject = __class__ ('MatchObject', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, rgx, groups, named_groups, txt, start_pos, end_pos) {
							self.start_index = groups.index;
							self.groups_list = groups.map ((function __lambda__ (g) {
								return (g !== void (0) ? g : null);
							}));
							self.named_groups = named_groups;
							self.pos = start_pos;
							self.endpos = end_pos;
							self.re = rgx;
							self.string = txt;
							self.lastindex = len (groups) - 1;
							self.lastgroup = null;
							var __iterable0__ = Object.keys (self.named_groups);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var gName = __iterable0__ [__index0__];
								var gId = self.named_groups [gName];
								if (gId == self.lastindex) {
									self.lastgroup = gName;
									break;
								}
							}
							var id = 0;
							var __iterable0__ = groups;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var group = __iterable0__ [__index0__];
								self [id] = group;
								id++;
							}
						});},
						get group () {return __get__ (this, function (self) {
							var groupIds = tuple ([].slice.apply (arguments).slice (1));
							if (len (groupIds) == 0) {
								return self.groups_list [0];
							}
							var result = list ([]);
							var __iterable0__ = groupIds;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var id = __iterable0__ [__index0__];
								if (py_typeof (id) === str) {
									result.append (self.groups_list [self.named_groups [id]]);
								}
								else {
									result.append (self.groups_list [id]);
								}
							}
							if (len (result) == 1) {
								return result [0];
							}
							return result;
						});},
						get groups () {return __get__ (this, function (self, py_default) {
							if (typeof py_default == 'undefined' || (py_default != null && py_default .hasOwnProperty ("__kwargtrans__"))) {;
								var py_default = null;
							};
							return self.groups_list.__getslice__ (1, null, 1).map ((function __lambda__ (g) {
								return (g !== null ? g : py_default);
							}));
						});},
						get groupdict () {return __get__ (this, function (self, py_default) {
							if (typeof py_default == 'undefined' || (py_default != null && py_default .hasOwnProperty ("__kwargtrans__"))) {;
								var py_default = null;
							};
							var d = dict ();
							var __iterable0__ = Object.keys (self.named_groups);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var gName = __iterable0__ [__index0__];
								var gId = self.named_groups [gName];
								var value = self.groups_list [gId];
								d [gName] = (value === null ? py_default : value);
							}
							return d;
						});},
						get end () {return __get__ (this, function (self, group) {
							if (typeof group == 'undefined' || (group != null && group .hasOwnProperty ("__kwargtrans__"))) {;
								var group = null;
							};
							if (group !== null) {
								var __except0__ = Error ('match.end() with argument is not supported');
								__except0__.__cause__ = null;
								throw __except0__;
							}
							return self.start_index + self.groups_list [0].length;
						});},
						get start () {return __get__ (this, function (self, group) {
							if (typeof group == 'undefined' || (group != null && group .hasOwnProperty ("__kwargtrans__"))) {;
								var group = null;
							};
							if (group !== null) {
								var __except0__ = Error ('match.start() with argument is not supported');
								__except0__.__cause__ = null;
								throw __except0__;
							}
							return self.start_index;
						});},
						get span () {return __get__ (this, function (self, group) {
							if (typeof group == 'undefined' || (group != null && group .hasOwnProperty ("__kwargtrans__"))) {;
								var group = null;
							};
							if (group !== none) {
								var __except0__ = Error ('match.span() with argument is not supported');
								__except0__.__cause__ = null;
								throw __except0__;
							}
							return tuple ([self.start (), self.end ()]);
						});}
					});
					var PyRegExp = __class__ ('PyRegExp', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, jsStrPattern, jsTokens, jsFlags, named_groups) {
							self.pattern = RegExp (jsStrPattern, jsFlags);
							self.jsTokens = jsTokens;
							self.jsFlags = jsFlags;
							self.named_groups = named_groups;
						});},
						get getFirstMatch () {return __get__ (this, function (self, txt, start, end) {
							var pattern = self.pattern;
							if (start === 0) {
								var match = txt.match (pattern);
							}
							else if (!__in__ ('m', self.jsFlags) || txt [start - 1] != '\n') {
								var strRgx = '';
								var __iterable0__ = self.jsTokens;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var token = __iterable0__ [__index0__];
									if (token == '^') {
										var token = '[^\\S\\s]';
									}
									strRgx += token;
								}
								var pattern = RegExp (strRgx, self.jsFlags);
							}
							var match = txt.__getslice__ (start, end, 1).match (pattern);
							if (match === null) {
								return null;
							}
							return match;
						});},
						get search () {return __get__ (this, function (self, txt, start, end) {
							if (typeof start == 'undefined' || (start != null && start .hasOwnProperty ("__kwargtrans__"))) {;
								var start = null;
							};
							if (typeof end == 'undefined' || (end != null && end .hasOwnProperty ("__kwargtrans__"))) {;
								var end = null;
							};
							if (start === null) {
								var start = 0;
							}
							if (end === null) {
								var end = len (txt);
							}
							var match = self.getFirstMatch (txt, start, end);
							if (match !== null) {
								return MatchObject (self, match, self.named_groups, txt, start, end);
							}
							return match;
						});},
						get match () {return __get__ (this, function (self, txt, start, end) {
							if (typeof start == 'undefined' || (start != null && start .hasOwnProperty ("__kwargtrans__"))) {;
								var start = null;
							};
							if (typeof end == 'undefined' || (end != null && end .hasOwnProperty ("__kwargtrans__"))) {;
								var end = null;
							};
							if (start === null) {
								var start = 0;
							}
							if (end === null) {
								var end = len (txt);
							}
							var match = self.getFirstMatch (txt, start, end);
							if (match === null || match.index > start) {
								return null;
							}
							return MatchObject (self, match, self.named_groups, txt, start, end);
						});},
						get py_split () {return __get__ (this, function (self, txt, maxsplit) {
							if (typeof maxsplit == 'undefined' || (maxsplit != null && maxsplit .hasOwnProperty ("__kwargtrans__"))) {;
								var maxsplit = null;
							};
							if (maxsplit === null) {
								var splitted = txt.py_split (self.pattern);
							}
							else {
								var splitted = txt ['split'] (self.pattern, maxsplit);
								var consumed = 0;
								var __iterable0__ = splitted;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var py_split = __iterable0__ [__index0__];
									consumed += len (py_split);
								}
								var last_el = txt.__getslice__ (consumed + 1, null, 1);
								var skip = len (last_el.match (self.pattern) [0]);
								splitted.append (last_el.__getslice__ (skip, null, 1));
							}
							return splitted;
						});},
						get findall () {return __get__ (this, function (self, txt, start, end) {
							if (typeof start == 'undefined' || (start != null && start .hasOwnProperty ("__kwargtrans__"))) {;
								var start = 0;
							};
							if (typeof end == 'undefined' || (end != null && end .hasOwnProperty ("__kwargtrans__"))) {;
								var end = 0 / 0;
							};
							var globalPattern = RegExp (self.patter, 'g');
							var matches = txt.match (globalPattern);
							while (txt.index (matches [0]) < start) {
								var matches = matches.__getslice__ (1, null, 1);
							}
						});}
					});
					var compile = function (pyPattern) {
						var __left0__ = translate (pyPattern);
						var jsStrPattern = __left0__ [0];
						var jsTokens = __left0__ [1];
						var jsFlags = __left0__ [2];
						var named_groups = __left0__ [3];
						return PyRegExp (jsStrPattern, jsTokens, jsFlags, named_groups);
					};
					__pragma__ ('<use>' +
						'translate' +
					'</use>')
					__pragma__ ('<all>')
						__all__.MatchObject = MatchObject;
						__all__.PyRegExp = PyRegExp;
						__all__.__name__ = __name__;
						__all__.compile = compile;
						__all__.translate = translate;
					__pragma__ ('</all>')
				}
			}
		}
	);
