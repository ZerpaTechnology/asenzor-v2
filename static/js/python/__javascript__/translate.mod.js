	__nest__ (
		__all__,
		'translate', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'translate';
					var VERBOSE = false;
					var Group = __class__ ('Group', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, start, end, klass) {
							self.start = start;
							self.end = end;
							self.klass = klass;
						});},
						get __repr__ () {return __get__ (this, function (self) {
							return str (tuple ([self.start, self.end, self.klass]));
						});}
					});
					var generate_group_spans = function (tokens) {
						var group_info = list ([]);
						var idx = 0;
						var __iterable0__ = tokens;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var token = __iterable0__ [__index0__];
							if (token.py_name.startswith ('(')) {
								group_info.append (Group (idx, null, token.py_name));
							}
							else if (token.py_name == ')') {
								var __iterable1__ = py_reversed (group_info);
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var group = __iterable1__ [__index1__];
									if (group.end === null) {
										group.end = idx;
									}
								}
							}
							idx++;
						}
						return group_info;
					};
					var get_capture_group = function (group_info, named_groups, group_ref) {
						try {
							var id = int (group_ref);
						}
						catch (__except0__) {
							var id = named_groups [group_ref];
						}
						var search = 0;
						var __iterable0__ = group_info;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var group = __iterable0__ [__index0__];
							if (group.klass == '(') {
								search++;
								if (search == id) {
									return group;
								}
							}
						}
					};
					var split_if_else = function (tokens, named_groups) {
						var variants = list ([]);
						var group_info = generate_group_spans (tokens);
						var __iterable0__ = group_info;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var group = __iterable0__ [__index0__];
							if (group.klass == '(?<') {
								var iff = tokens.__getslice__ (0, null, 1);
								var els = tokens.__getslice__ (0, null, 1);
								var con_start = group.start;
								var con_end = group.end;
								var ref = tokens [con_start + 1].py_name;
								var capture_group = get_capture_group (group_info, named_groups, ref);
								var capture_group_modifier = tokens [capture_group.end + 1];
								if (__in__ (capture_group_modifier.py_name, list (['?', '*'])) || capture_group_modifier.py_name.startswith ('{0,')) {
									if (capture_group_modifier.py_name == '?') {
										iff [capture_group.end + 1] = null;
									}
									else if (capture_group_modifier.py_name == '*') {
										iff [capture_group.end + 1] = Token ('+');
									}
									else if (capture_group_modifier.py_name.startswith ('{0,')) {
										iff [capture_group.end + 1].py_name.__setslice__ (0, 3, null, '{1,');
									}
									els [capture_group.end + 1] = null;
									var has_else = false;
									for (var idx = con_start; idx < con_end; idx++) {
										if (tokens [idx].py_name == '|') {
											var has_else = true;
											els.py_pop (con_end);
											iff.__setslice__ (idx, con_end + 1, null, list ([]));
											els.__setslice__ (con_start, idx + 1, null, list ([]));
											break;
										}
									}
									if (!(has_else)) {
										els.__setslice__ (con_start, con_end + 1, null, list ([]));
										iff.py_pop (con_end);
									}
									iff.__setslice__ (con_start, con_start + 3, null, list ([]));
									els.__setslice__ (capture_group.start, capture_group.end + 1, null, list ([Token ('('), Token (')')]));
									iff.remove (null);
									els.remove (null);
									variants.append (iff);
									variants.append (els);
								}
								else {
									var past_iff = false;
									for (var idx = con_start; idx < con_end; idx++) {
										if (iff [idx].py_name == '|') {
											var iff = tokens.__getslice__ (0, idx, 1);
											iff.extend (tokens.__getslice__ (con_end + 1, null, 1));
											break;
										}
									}
									iff.__setslice__ (con_start, con_start + 3, null, list ([]));
									variants.append (iff);
								}
								break;
							}
						}
						if (!(variants)) {
							return list ([tokens]);
						}
						var all_variants = list ([]);
						var __iterable0__ = variants;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var variant = __iterable0__ [__index0__];
							all_variants.extend (split_if_else (variant, named_groups));
						}
						return all_variants;
					};
					var Token = __class__ ('Token', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, py_name, paras, pure) {
							if (typeof paras == 'undefined' || (paras != null && paras .hasOwnProperty ("__kwargtrans__"))) {;
								var paras = null;
							};
							if (typeof pure == 'undefined' || (pure != null && pure .hasOwnProperty ("__kwargtrans__"))) {;
								var pure = false;
							};
							if (paras === null) {
								var paras = list ([]);
							}
							self.py_name = py_name;
							self.paras = paras;
							self.pure = pure;
							self.isModeGroup = false;
						});},
						get __repr__ () {return __get__ (this, function (self) {
							return self.py_name;
						});},
						get resolve () {return __get__ (this, function (self) {
							var paras = '';
							var __iterable0__ = self.paras;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var para = __iterable0__ [__index0__];
								paras += str (para);
							}
							return self.py_name + paras;
						});}
					});
					var shift_reduce = function (stack, queue, named_groups, js_flags, dots_match_all) {
						var py_flags = 'iLmsux';
						var done = false;
						var high = len (stack) - 1;
						var s0 = (len (stack) > 0 ? stack [high] : Token (''));
						var s1 = (len (stack) > 1 ? stack [high - 1] : Token (''));
						var s2 = (len (stack) > 2 ? stack [high - 2] : Token (''));
						if (VERBOSE) {
							var __iterable0__ = stack;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var token = __iterable0__ [__index0__];
								console.log (token.resolve (), '\t', __kwargtrans__ ({end: ''}));
							}
							console.log ('');
						}
						if (s1.py_name == '\\') {
							if (s0.py_name == 'A') {
								stack.__setslice__ (-(2), null, null, list ([Token ('^')]));
							}
							else if (s0.py_name == 'a') {
								stack.__setslice__ (-(2), null, null, list ([Token ('\\07')]));
							}
							else if (s0.py_name == 'Z') {
								stack.__setslice__ (-(2), null, null, list ([Token ('$')]));
							}
							else {
								stack.__setslice__ (-(2), null, null, list ([Token ('\\' + s0.py_name)]));
							}
						}
						else if (s0.py_name == '$' && s0.pure) {
							stack.py_pop ();
							stack.extend (list ([Token ('(?='), Token ('\\n'), Token ('?'), Token ('$'), Token (')')]));
						}
						else if (s1.py_name == '{') {
							if (s0.py_name == ',' && len (s1.paras) == 0) {
								s1.paras.append ('0');
								s1.paras.append (',');
							}
							else if (s0.py_name == '}') {
								s1.paras.append ('}');
								s1.py_name = s1.resolve ();
								s1.paras = list ([]);
							}
							else {
								s1.paras.append (s0.py_name);
							}
							var stack = stack.__getslice__ (0, -(1), 1);
						}
						else if (s1.py_name == '[' && s0.py_name == '^') {
							stack.__setslice__ (-(2), null, null, list ([Token ('[^')]));
						}
						else if (s1.py_name == '(' && s0.py_name == '?') {
							stack.__setslice__ (-(2), null, null, list ([Token ('(?')]));
						}
						else if (__in__ (s1.py_name, list (['*', '+', '?'])) && s0.py_name == '?') {
							stack.__setslice__ (-(2), null, null, list ([Token (s1.py_name + '?')]));
						}
						else if (s1.isModeGroup && s0.py_name == ')') {
							var stack = stack.__getslice__ (0, -(2), 1);
						}
						else if (s1.py_name == '(?') {
							if (__in__ (s0.py_name, py_flags)) {
								if (s0.py_name == 'i') {
									js_flags += 'i';
								}
								else if (s0.py_name == 'm') {
									js_flags += 'm';
								}
								else if (s0.py_name == 's') {
									var dots_match_all = true;
								}
								else {
									var __except0__ = Error ('Unsupported flag: ' + s0.py_name);
									__except0__.__cause__ = null;
									throw __except0__;
								}
								stack.py_pop ();
								s1.isModeGroup = true;
							}
							else {
								if (s0.py_name == '(') {
									s0.py_name = '<';
								}
								var newToken = Token ('(?' + s0.py_name);
								stack.__setslice__ (-(2), null, null, list ([newToken]));
							}
						}
						else if (s1.py_name == '(?<') {
							if (s0.py_name == ')') {
								stack.__setslice__ (-(1), null, null, list ([Token (''.join (s1.paras)), Token ('>')]));
								s1.paras = list ([]);
							}
							else {
								s1.paras.append (s0.py_name);
								stack.py_pop ();
							}
						}
						else if (s1.py_name == '(?P') {
							stack.__setslice__ (-(2), null, null, list ([Token ('(?P' + s0.py_name)]));
						}
						else if (s1.py_name == '(?P<') {
							if (s0.py_name == '>') {
								named_groups [''.join (s1.paras)] = len (named_groups) + 1;
								stack.__setslice__ (-(2), null, null, list ([Token ('(')]));
							}
							else {
								s1.paras.append (s0.py_name);
								stack.py_pop ();
							}
						}
						else if (s1.py_name == '(?P=') {
							if (s0.py_name == ')') {
								stack.__setslice__ (-(2), null, null, list ([Token ('\\' + named_groups [s1.paras [0]])]));
							}
							else if (!(s1.paras)) {
								s1.paras.append (s0.py_name);
								stack.py_pop ();
							}
							else {
								s1.paras [0] += s0.py_name;
								stack.py_pop ();
							}
						}
						else if (s1.py_name == '(?#') {
							if (s0.py_name == ')') {
								var stack = stack.__getslice__ (0, -(2), 1);
							}
							else {
								var stack = stack.__getslice__ (0, -(1), 1);
							}
						}
						else if (!(queue)) {
							var done = true;
						}
						else {
							stack.append (Token (queue [0], list ([]), true));
							var queue = queue.__getslice__ (1, null, 1);
						}
						return tuple ([stack, queue, js_flags, dots_match_all, done]);
					};
					var translate = function (rgx) {
						var stack = list ([]);
						var queue = list (rgx);
						var js_flags = '';
						var named_groups = dict ({});
						var dots_match_all = false;
						var nloop = 0;
						while (true) {
							nloop++;
							if (nloop > 50) {
								console.log ('Failed to parse...');
								break;
							}
							var __left0__ = shift_reduce (stack, queue, named_groups, js_flags, dots_match_all);
							var stack = __left0__ [0];
							var queue = __left0__ [1];
							var js_flags = __left0__ [2];
							var dots_match_all = __left0__ [3];
							var done = __left0__ [4];
							if (done) {
								break;
							}
						}
						var variants = split_if_else (stack, named_groups);
						var final = list ([]);
						for (var i = 0; i < len (variants); i++) {
							final.extend (variants [i]);
							if (i < len (variants) - 1) {
								final.append (Token ('|'));
							}
						}
						var stack = final;
						var group_info = generate_group_spans (stack);
						var resolvedTokens = list ([]);
						var __iterable0__ = stack;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var token = __iterable0__ [__index0__];
							var stringed = token.resolve ();
							if (dots_match_all && stringed == '.') {
								var stringed = '[\\s\\S]';
							}
							resolvedTokens.append (stringed);
						}
						return tuple ([''.join (resolvedTokens), resolvedTokens, js_flags, named_groups, group_info]);
					};
					__pragma__ ('<all>')
						__all__.Group = Group;
						__all__.Token = Token;
						__all__.VERBOSE = VERBOSE;
						__all__.__name__ = __name__;
						__all__.generate_group_spans = generate_group_spans;
						__all__.get_capture_group = get_capture_group;
						__all__.shift_reduce = shift_reduce;
						__all__.split_if_else = split_if_else;
						__all__.translate = translate;
					__pragma__ ('</all>')
				}
			}
		}
	);
