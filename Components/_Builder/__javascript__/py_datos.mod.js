	__nest__ (
		__all__,
		'py_datos', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'py_datos';
					var py_typeof = function (anObject) {
						
						    var aType = typeof anObject;
						    if (aType == 'object') {    // Directly trying '__class__ in anObject' turns out to wreck anObject in Chrome if its a primitive
						        try {
						            
						            
						            if(Object.keys(anObject).indexOf("__class__") >= 0 && anObject.__class__!=null){
						                return anObject.__class__;
						            }
						            else{
						                return object;
						            }
						
						            return dict;
						        }
						        catch (exception) {
						            console.log(exception);
						            return aType;
						        }
						    }
						    else {
						        return (    // Odly, the braces are required here
						            aType == 'boolean' ? bool :
						            aType == 'string' ? str :
						            aType == 'number' ? (anObject % 1 == 0 ? int : float) :
						            null
						        );
						    }
						    
						    
					};
					var list = function (iterable) {
						if (iterable.__class__ != null && iterable.__class__.__name__ == 'list') {
							return iterable;
						}
						
						
						    if (typeof(iterable)=="object"){
						        return Object.keys(iterable);
						    }
						    else{
						        var instance = iterable ? [] .slice.apply (iterable) : [];  // Spread iterable, n.b. array.slice (), so array before dot
						        // Sort is the normal JavaScript sort, Python sort is a non-member function
						        return instance;
						    }
						
						    
					};
					var copy = function (objeto) {
						if (__in__ ('__class__', dir (objeto))) {
							if (objeto.prototype != null) {
								var o = new objeto.prototype.constructor;
								var __iterable0__ = dir (o);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if ( typeof getattr(o,elem)!='function'
									) {
										setattr (o, elem, copy (getattr (objeto, elem)));
									}
								}
							}
							else if (objeto.__proto__.constructor==Array
							) {
								var l = list ([]);
								var __iterable0__ = objeto;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									l.append (copy (elem));
								}
								var o = Object.assign (list ([]), l);
							}
							else if (objeto == null) {
								var o = objeto;
							}
							else if (objeto.__proto__.constructor==String
							 || objeto.__proto__.constructor==Number
							 || objeto.__proto__.constructor==Boolean
							) {
								var o = objeto;
							}
							else if (objeto.__proto__.constructor==Function
							) {
								var o = objeto.prototype.constructor;
							}
							else {
								var d = dict ({});
								var __iterable0__ = objeto;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									d [elem] = copy (objeto [elem]);
								}
								var o = Object.assign (dict ({}), d);
							}
						}
						else if (py_typeof (objeto) == str || py_typeof (objeto) == int || py_typeof (objeto) == float || py_typeof (objeto) == bool) {
							var o = objeto.valueOf ();
						}
						else if (py_typeof (objeto) != str && py_typeof (objeto) != int && py_typeof (objeto) != float && py_typeof (objeto) != bool && py_typeof (objeto) != null) {
							var o = objeto;
						}
						else {
							var o = objeto;
						}
						return o;
					};
					__pragma__ ('<all>')
						__all__.__name__ = __name__;
						__all__.copy = copy;
						__all__.list = list;
						__all__.py_typeof = py_typeof;
					__pragma__ ('</all>')
				}
			}
		}
	);
