"use strict";
// Transcrypt'ed from Python, 2018-01-11 22:11:59
function personalizador () {
   var __symbols__ = ['__py3.5__', '__esv5__'];
    var __all__ = {};
    var __world__ = __all__;
    
    /* Nested module-object creator, part of the nesting may already exist and have attributes
    
    A Transcrypt applicaton consists of a main module and additional modules.
    Transcrypt modules constitute a unique, unambigous tree by their dotted names, no matter which of the alternative module root paths they come from.
    The main module is represented by a main function by the name of the application.
    The locals of this function constitute the outer namespace of the Transcrypt application.
    References to all local variables of this function are also assigned to attributes of local variable __all__, using the variable names as an attribute names.
    The main function returns this local variable __all__ (that inside the function is also known by the name __world__)
    Normally this function result is assigned to window.<application name>.
    The function may than be exited (unless its main line starts an ongoing activity), but the application namespace stays alive tby the reference that window has to it.
    In case of the ongoing activity including the script is enough to start it, in other cases it has to be started explicitly by calling window.<application name>.<a function>.
    There may be multiple such entrypoint functions.
    
    Additional modules are represented by objects rather than functions, nested into __world__ (so into __all__ of the main function).
    This nesting can be directly or indirectly, according to the dotted paths of the additional modules.
    One of the methods of the module object is the __init__ function, that's executed once at module initialisation time.
    
    The additional modues also have an __all__ variable, an attribute rather than a local variable.
    However this __all__ object is passed to the __init__ function, so becomes a local variable there.
    Variables in additional modules first become locals to the __init__ function but references to all of them are assigend to __all__ under their same names.
    This resembles the cause of affairs in the main function.
    However __world__ only referes to the __all__ of the main module, not of any additional modules.
    Importing a module boils down to adding all members of its __all__ to the local namespace, directly or via dotted access, depending on the way of import.
    
    In each local namespace of the module function (main function for main module, __init__ for additional modules) there's a variable __name__ holding the name of the module.
    Classes are created inside the static scope of a particular module, and at that (class creation) time their variable __module__ gets assigned a reference to __name__.
    This assignement is generated explicitly by the compiler, as the class creation function __new__ of the metaclass isn't in the static scope containing __name__.
    
    In case of
        import a
        import a.b
    a will have been created at the moment that a.b is imported,
    so all a.b. is allowed to do is an extra attribute in a, namely a reference to b,
    not recreate a, since that would destroy attributes previously present in a
    
    In case of
        import a.b
        import a
    a will have to be created at the moment that a.b is imported
    
    In general in a chain
        import a.b.c.d.e
    a, a.b, a.b.c and a.b.c.d have to exist before e is created, since a.b.c.d should hold a reference to e.
    Since this applies recursively, if e.g. c is already created, we can be sure a and a.b. will also be already created.
    
    So to be able to create e, we'll have to walk the chain a.b.c.d, starting with a.
    As soon as we encounter a module in the chain that isn't already there, we'll have to create the remainder (tail) of the chain.
    
    e.g.
        import a.b.c.d.e
        import a.b.c
    
    will generate
        var modules = {};
        __nest__ (a, 'b.c.d.e', __init__ (__world__.a.b.c.d.e));
        __nest__ (a, 'b.c', __init__ (__world__.a.b.c));
        
    The task of the __nest__ function is to start at the head object and then walk to the chain of objects behind it (tail),
    creating the ones that do not exist already, and insert the necessary module reference attributes into them.   
    */
    
    var __nest__ = function (headObject, tailNames, value) {    
        var current = headObject;
        // In some cases this will be <main function>.__all__,
        // which is the main module and is also known under the synonym <main function.__world__.
        // N.B. <main function> is the entry point of a Transcrypt application,
        // Carrying the same name as the application except the file name extension.
        
        if (tailNames != '') {  // Split on empty string doesn't give empty list
            // Find the last already created object in tailNames
            var tailChain = tailNames.split ('.');
            var firstNewIndex = tailChain.length;
            for (var index = 0; index < tailChain.length; index++) {
                if (!current.hasOwnProperty (tailChain [index])) {
                    firstNewIndex = index;
                    break;
                }
                current = current [tailChain [index]];
            }
            
            // Create the rest of the objects, if any
            for (var index = firstNewIndex; index < tailChain.length; index++) {
                current [tailChain [index]] = {};
                current = current [tailChain [index]];
            }
        }
        
        // Insert it new attributes, it may have been created earlier and have other attributes
        for (var attrib in value) {
            current [attrib] = value [attrib];          
        }       
    };
    __all__.__nest__ = __nest__;
    
    // Initialize module if not yet done and return its globals
    var __init__ = function (module) {
        if (!module.__inited__) {
            module.__all__.__init__ (module.__all__);
            module.__inited__ = true;
        }
        return module.__all__;
    };
    __all__.__init__ = __init__;
    
    
    
    
    // Since we want to assign functions, a = b.f should make b.f produce a bound function
    // So __get__ should be called by a property rather then a function
    // Factory __get__ creates one of three curried functions for func
    // Which one is produced depends on what's to the left of the dot of the corresponding JavaScript property
    var __get__ = function (self, func, quotedFuncName) {
        if (self) {
            if (self.hasOwnProperty ('__class__') || typeof self == 'string' || self instanceof String) {           // Object before the dot
                if (quotedFuncName) {                                   // Memoize call since fcall is on, by installing bound function in instance
                    Object.defineProperty (self, quotedFuncName, {      // Will override the non-own property, next time it will be called directly
                        value: function () {                            // So next time just call curry function that calls function
                            var args = [] .slice.apply (arguments);
                            return func.apply (null, [self] .concat (args));
                        },              
                        writable: true,
                        enumerable: true,
                        configurable: true
                    });
                }
                return function () {                                    // Return bound function, code dupplication for efficiency if no memoizing
                    var args = [] .slice.apply (arguments);             // So multilayer search prototype, apply __get__, call curry func that calls func
                    return func.apply (null, [self] .concat (args));
                };
            }
            else {                                                      // Class before the dot
                return func;                                            // Return static method
            }
        }
        else {                                                          // Nothing before the dot
            return func;                                                // Return free function
        }
    }
    __all__.__get__ = __get__;

    var __getcm__ = function (self, func, quotedFuncName) {
        if (self.hasOwnProperty ('__class__')) {
            return function () {
                var args = [] .slice.apply (arguments);
                return func.apply (null, [self.__class__] .concat (args));
            };
        }
        else {
            return function () {
                var args = [] .slice.apply (arguments);
                return func.apply (null, [self] .concat (args));
            };
        }
    }
    __all__.__getcm__ = __getcm__;
    
    var __getsm__ = function (self, func, quotedFuncName) {
        return func;
    }
    __all__.__getsm__ = __getsm__;
        
    // Mother of all metaclasses        
    var py_metatype = {
        __name__: 'type',
        __bases__: [],
        
        // Overridable class creation worker
        __new__: function (meta, name, bases, attribs) {
            // Create the class cls, a functor, which the class creator function will return
            var cls = function () {                     // If cls is called with arg0, arg1, etc, it calls its __new__ method with [arg0, arg1, etc]
                var args = [] .slice.apply (arguments); // It has a __new__ method, not yet but at call time, since it is copied from the parent in the loop below
                return cls.__new__ (args);              // Each Python class directly or indirectly derives from object, which has the __new__ method
            };                                          // If there are no bases in the Python source, the compiler generates [object] for this parameter
            
            // Copy all methods, including __new__, properties and static attributes from base classes to new cls object
            // The new class object will simply be the prototype of its instances
            // JavaScript prototypical single inheritance will do here, since any object has only one class
            // This has nothing to do with Python multiple inheritance, that is implemented explictly in the copy loop below
            for (var index = bases.length - 1; index >= 0; index--) {   // Reversed order, since class vars of first base should win
                var base = bases [index];
                for (var attrib in base) {
                    var descrip = Object.getOwnPropertyDescriptor (base, attrib);
                    Object.defineProperty (cls, attrib, descrip);
                }           
            }
            
            // Add class specific attributes to the created cls object
            cls.__metaclass__ = meta;
            cls.__name__ = name;
            cls.__bases__ = bases;
            
            // Add own methods, properties and own static attributes to the created cls object
            for (var attrib in attribs) {
                var descrip = Object.getOwnPropertyDescriptor (attribs, attrib);
                Object.defineProperty (cls, attrib, descrip);
            }
            // Return created cls object
            return cls;
        }
    };
    py_metatype.__metaclass__ = py_metatype;
    __all__.py_metatype = py_metatype;
    
    // Mother of all classes
    var object = {
        __init__: function (self) {},
        
        __metaclass__: py_metatype, // By default, all classes have metaclass type, since they derive from object
        __name__: 'object',
        __bases__: [],
            
        // Object creator function, is inherited by all classes (so could be global)
        __new__: function (args) {  // Args are just the constructor args       
            // In JavaScript the Python class is the prototype of the Python object
            // In this way methods and static attributes will be available both with a class and an object before the dot
            // The descriptor produced by __get__ will return the right method flavor
            var instance = Object.create (this, {__class__: {value: this, enumerable: true}});
            

            // Call constructor
            this.__init__.apply (null, [instance] .concat (args));

            // Return constructed instance
            return instance;
        }   
    };
    __all__.object = object;
    
    // Class creator facade function, calls class creation worker
    var __class__ = function (name, bases, attribs, meta) {         // Parameter meta is optional
        if (meta == undefined) {
            meta = bases [0] .__metaclass__;
        }
                
        return meta.__new__ (meta, name, bases, attribs);
    }
    __all__.__class__ = __class__;
    
    // Define __pragma__ to preserve '<all>' and '</all>', since it's never generated as a function, must be done early, so here
    var __pragma__ = function () {};
    __all__.__pragma__ = __pragma__;
    
    	__nest__ (
		__all__,
		'org.transcrypt.__base__', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'org.transcrypt.__base__';
					var __Envir__ = __class__ ('__Envir__', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							self.interpreter_name = 'python';
							self.transpiler_name = 'transcrypt';
							self.transpiler_version = '3.6.61';
							self.target_subdir = '__javascript__';
						});}
					});
					var __envir__ = __Envir__ ();
					__pragma__ ('<all>')
						__all__.__Envir__ = __Envir__;
						__all__.__envir__ = __envir__;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'org.transcrypt.__standard__', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'org.transcrypt.__standard__';
					var Exception = __class__ ('Exception', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							var kwargs = dict ();
							if (arguments.length) {
								var __ilastarg0__ = arguments.length - 1;
								if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
									var __allkwargs0__ = arguments [__ilastarg0__--];
									for (var __attrib0__ in __allkwargs0__) {
										switch (__attrib0__) {
											case 'self': var self = __allkwargs0__ [__attrib0__]; break;
											default: kwargs [__attrib0__] = __allkwargs0__ [__attrib0__];
										}
									}
									delete kwargs.__kwargtrans__;
								}
								var args = tuple ([].slice.apply (arguments).slice (1, __ilastarg0__ + 1));
							}
							else {
								var args = tuple ();
							}
							self.__args__ = args;
							try {
								self.stack = kwargs.error.stack;
							}
							catch (__except0__) {
								self.stack = 'No stack trace available';
							}
						});},
						get __repr__ () {return __get__ (this, function (self) {
							if (len (self.__args__)) {
								return '{}{}'.format (self.__class__.__name__, repr (tuple (self.__args__)));
							}
							else {
								return '{}()'.format (self.__class__.__name__);
							}
						});},
						get __str__ () {return __get__ (this, function (self) {
							if (len (self.__args__) > 1) {
								return str (tuple (self.__args__));
							}
							else if (len (self.__args__)) {
								return str (self.__args__ [0]);
							}
							else {
								return '';
							}
						});}
					});
					var IterableError = __class__ ('IterableError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, error) {
							Exception.__init__ (self, "Can't iterate over non-iterable", __kwargtrans__ ({error: error}));
						});}
					});
					var StopIteration = __class__ ('StopIteration', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, error) {
							Exception.__init__ (self, 'Iterator exhausted', __kwargtrans__ ({error: error}));
						});}
					});
					var ValueError = __class__ ('ValueError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, message, error) {
							Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
						});}
					});
					var KeyError = __class__ ('KeyError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, message, error) {
							Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
						});}
					});
					var AssertionError = __class__ ('AssertionError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, message, error) {
							if (message) {
								Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
							}
							else {
								Exception.__init__ (self, __kwargtrans__ ({error: error}));
							}
						});}
					});
					var NotImplementedError = __class__ ('NotImplementedError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, message, error) {
							Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
						});}
					});
					var IndexError = __class__ ('IndexError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, message, error) {
							Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
						});}
					});
					var AttributeError = __class__ ('AttributeError', [Exception], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, message, error) {
							Exception.__init__ (self, message, __kwargtrans__ ({error: error}));
						});}
					});
					var Warning = __class__ ('Warning', [Exception], {
						__module__: __name__,
					});
					var UserWarning = __class__ ('UserWarning', [Warning], {
						__module__: __name__,
					});
					var DeprecationWarning = __class__ ('DeprecationWarning', [Warning], {
						__module__: __name__,
					});
					var RuntimeWarning = __class__ ('RuntimeWarning', [Warning], {
						__module__: __name__,
					});
					var __sort__ = function (iterable, key, reverse) {
						if (typeof key == 'undefined' || (key != null && key .hasOwnProperty ("__kwargtrans__"))) {;
							var key = null;
						};
						if (typeof reverse == 'undefined' || (reverse != null && reverse .hasOwnProperty ("__kwargtrans__"))) {;
							var reverse = false;
						};
						if (arguments.length) {
							var __ilastarg0__ = arguments.length - 1;
							if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
								var __allkwargs0__ = arguments [__ilastarg0__--];
								for (var __attrib0__ in __allkwargs0__) {
									switch (__attrib0__) {
										case 'iterable': var iterable = __allkwargs0__ [__attrib0__]; break;
										case 'key': var key = __allkwargs0__ [__attrib0__]; break;
										case 'reverse': var reverse = __allkwargs0__ [__attrib0__]; break;
									}
								}
							}
						}
						else {
						}
						if (key) {
							iterable.sort ((function __lambda__ (a, b) {
								if (arguments.length) {
									var __ilastarg0__ = arguments.length - 1;
									if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
										var __allkwargs0__ = arguments [__ilastarg0__--];
										for (var __attrib0__ in __allkwargs0__) {
											switch (__attrib0__) {
												case 'a': var a = __allkwargs0__ [__attrib0__]; break;
												case 'b': var b = __allkwargs0__ [__attrib0__]; break;
											}
										}
									}
								}
								else {
								}
								return (key (a) > key (b) ? 1 : -(1));
							}));
						}
						else {
							iterable.sort ();
						}
						if (reverse) {
							iterable.reverse ();
						}
					};
					var sorted = function (iterable, key, reverse) {
						if (typeof key == 'undefined' || (key != null && key .hasOwnProperty ("__kwargtrans__"))) {;
							var key = null;
						};
						if (typeof reverse == 'undefined' || (reverse != null && reverse .hasOwnProperty ("__kwargtrans__"))) {;
							var reverse = false;
						};
						if (arguments.length) {
							var __ilastarg0__ = arguments.length - 1;
							if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
								var __allkwargs0__ = arguments [__ilastarg0__--];
								for (var __attrib0__ in __allkwargs0__) {
									switch (__attrib0__) {
										case 'iterable': var iterable = __allkwargs0__ [__attrib0__]; break;
										case 'key': var key = __allkwargs0__ [__attrib0__]; break;
										case 'reverse': var reverse = __allkwargs0__ [__attrib0__]; break;
									}
								}
							}
						}
						else {
						}
						if (py_typeof (iterable) == dict) {
							var result = copy (iterable.py_keys ());
						}
						else {
							var result = copy (iterable);
						}
						__sort__ (result, key, reverse);
						return result;
					};
					var map = function (func, iterable) {
						return function () {
							var __accu0__ = [];
							var __iterable0__ = iterable;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var item = __iterable0__ [__index0__];
								__accu0__.append (func (item));
							}
							return __accu0__;
						} ();
					};
					var filter = function (func, iterable) {
						if (func == null) {
							var func = bool;
						}
						return function () {
							var __accu0__ = [];
							var __iterable0__ = iterable;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var item = __iterable0__ [__index0__];
								if (func (item)) {
									__accu0__.append (item);
								}
							}
							return __accu0__;
						} ();
					};
					var __Terminal__ = __class__ ('__Terminal__', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							self.buffer = '';
							try {
								self.element = document.getElementById ('__terminal__');
							}
							catch (__except0__) {
								self.element = null;
							}
							if (self.element) {
								self.element.style.overflowX = 'auto';
								self.element.style.boxSizing = 'border-box';
								self.element.style.padding = '5px';
								self.element.innerHTML = '_';
							}
						});},
						get print () {return __get__ (this, function (self) {
							var sep = ' ';
							var end = '\n';
							if (arguments.length) {
								var __ilastarg0__ = arguments.length - 1;
								if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
									var __allkwargs0__ = arguments [__ilastarg0__--];
									for (var __attrib0__ in __allkwargs0__) {
										switch (__attrib0__) {
											case 'self': var self = __allkwargs0__ [__attrib0__]; break;
											case 'sep': var sep = __allkwargs0__ [__attrib0__]; break;
											case 'end': var end = __allkwargs0__ [__attrib0__]; break;
										}
									}
								}
								var args = tuple ([].slice.apply (arguments).slice (1, __ilastarg0__ + 1));
							}
							else {
								var args = tuple ();
							}
							self.buffer = '{}{}{}'.format (self.buffer, sep.join (function () {
								var __accu0__ = [];
								var __iterable0__ = args;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var arg = __iterable0__ [__index0__];
									__accu0__.append (str (arg));
								}
								return __accu0__;
							} ()), end).__getslice__ (-(4096), null, 1);
							if (self.element) {
								self.element.innerHTML = self.buffer.py_replace ('\n', '<br>');
								self.element.scrollTop = self.element.scrollHeight;
							}
							else {
								console.log (sep.join (function () {
									var __accu0__ = [];
									var __iterable0__ = args;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var arg = __iterable0__ [__index0__];
										__accu0__.append (str (arg));
									}
									return __accu0__;
								} ()));
							}
						});},
						get input () {return __get__ (this, function (self, question) {
							if (arguments.length) {
								var __ilastarg0__ = arguments.length - 1;
								if (arguments [__ilastarg0__] && arguments [__ilastarg0__].hasOwnProperty ("__kwargtrans__")) {
									var __allkwargs0__ = arguments [__ilastarg0__--];
									for (var __attrib0__ in __allkwargs0__) {
										switch (__attrib0__) {
											case 'self': var self = __allkwargs0__ [__attrib0__]; break;
											case 'question': var question = __allkwargs0__ [__attrib0__]; break;
										}
									}
								}
							}
							else {
							}
							self.print ('{}'.format (question), __kwargtrans__ ({end: ''}));
							var answer = window.prompt ('\n'.join (self.buffer.py_split ('\n').__getslice__ (-(16), null, 1)));
							self.print (answer);
							return answer;
						});}
					});
					var __terminal__ = __Terminal__ ();
					__pragma__ ('<all>')
						__all__.AssertionError = AssertionError;
						__all__.AttributeError = AttributeError;
						__all__.DeprecationWarning = DeprecationWarning;
						__all__.Exception = Exception;
						__all__.IndexError = IndexError;
						__all__.IterableError = IterableError;
						__all__.KeyError = KeyError;
						__all__.NotImplementedError = NotImplementedError;
						__all__.RuntimeWarning = RuntimeWarning;
						__all__.StopIteration = StopIteration;
						__all__.UserWarning = UserWarning;
						__all__.ValueError = ValueError;
						__all__.Warning = Warning;
						__all__.__Terminal__ = __Terminal__;
						__all__.__name__ = __name__;
						__all__.__sort__ = __sort__;
						__all__.__terminal__ = __terminal__;
						__all__.filter = filter;
						__all__.map = map;
						__all__.sorted = sorted;
					__pragma__ ('</all>')
				}
			}
		}
	);
    var __call__ = function (/* <callee>, <this>, <params>* */) {   // Needed for __base__ and __standard__ if global 'opov' switch is on
        var args = [] .slice.apply (arguments);
        if (typeof args [0] == 'object' && '__call__' in args [0]) {        // Overloaded
            return args [0] .__call__ .apply (args [1], args.slice (2));
        }
        else {                                                              // Native
            return args [0] .apply (args [1], args.slice (2));
        }
    };
    __all__.__call__ = __call__;

    // Initialize non-nested modules __base__ and __standard__ and make its names available directly and via __all__
    // They can't do that itself, because they're regular Python modules
    // The compiler recognizes their names and generates them inline rather than nesting them
    // In this way it isn't needed to import them everywhere

    // __base__

    __nest__ (__all__, '', __init__ (__all__.org.transcrypt.__base__));
    var __envir__ = __all__.__envir__;

    // __standard__

    __nest__ (__all__, '', __init__ (__all__.org.transcrypt.__standard__));

    var Exception = __all__.Exception;
    var IterableError = __all__.IterableError;
    var StopIteration = __all__.StopIteration;
    var ValueError = __all__.ValueError;
    var KeyError = __all__.KeyError;
    var AssertionError = __all__.AssertionError;
    var NotImplementedError = __all__.NotImplementedError;
    var IndexError = __all__.IndexError;
    var AttributeError = __all__.AttributeError;

    // Warnings Exceptions
    var Warning = __all__.Warning;
    var UserWarning = __all__.UserWarning;
    var DeprecationWarning = __all__.DeprecationWarning;
    var RuntimeWarning = __all__.RuntimeWarning;

    var __sort__ = __all__.__sort__;
    var sorted = __all__.sorted;

    var map = __all__.map;
    var filter = __all__.filter;

    __all__.print = __all__.__terminal__.print;
    __all__.input = __all__.__terminal__.input;

    var __terminal__ = __all__.__terminal__;
    var print = __all__.print;
    var input = __all__.input;

    // Complete __envir__, that was created in __base__, for non-stub mode
    __envir__.executor_name = __envir__.transpiler_name;

    // Make make __main__ available in browser
    var __main__ = {__file__: ''};
    __all__.main = __main__;

    // Define current exception, there's at most one exception in the air at any time
    var __except__ = null;
    __all__.__except__ = __except__;
    
     // Creator of a marked dictionary, used to pass **kwargs parameter
    var __kwargtrans__ = function (anObject) {
        anObject.__kwargtrans__ = null; // Removable marker
        anObject.constructor = Object;
        return anObject;
    }
    __all__.__kwargtrans__ = __kwargtrans__;

    // 'Oneshot' dict promotor, used to enrich __all__ and help globals () return a true dict
    var __globals__ = function (anObject) {
        if (isinstance (anObject, dict)) {  // Don't attempt to promote (enrich) again, since it will make a copy
            return anObject;
        }
        else {
            return dict (anObject)
        }
    }
    __all__.__globals__ = __globals__
    
    // Partial implementation of super () .<methodName> (<params>)
    var __super__ = function (aClass, methodName) {
        // Lean and fast, no C3 linearization, only call first implementation encountered
        // Will allow __super__ ('<methodName>') (self, <params>) rather than only <className>.<methodName> (self, <params>)
        
        for (var index = 0; index < aClass.__bases__.length; index++) {
            var base = aClass.__bases__ [index];
            if (methodName in base) {
               return base [methodName];
            }
        }

        throw new Exception ('Superclass method not found');    // !!! Improve!
    }
    __all__.__super__ = __super__
        
    // Python property installer function, no member since that would bloat classes
    var property = function (getter, setter) {  // Returns a property descriptor rather than a property
        if (!setter) {  // ??? Make setter optional instead of dummy?
            setter = function () {};
        }
        return {get: function () {return getter (this)}, set: function (value) {setter (this, value)}, enumerable: true};
    }
    __all__.property = property;
    
    // Conditional JavaScript property installer function, prevents redefinition of properties if multiple Transcrypt apps are on one page
    var __setProperty__ = function (anObject, name, descriptor) {
        if (!anObject.hasOwnProperty (name)) {
            Object.defineProperty (anObject, name, descriptor);
        }
    }
    __all__.__setProperty__ = __setProperty__
    
    // Assert function, call to it only generated when compiling with --dassert option
    function assert (condition, message) {  // Message may be undefined
        if (!condition) {
            throw AssertionError (message, new Error ());
        }
    }

    __all__.assert = assert;

    var __merge__ = function (object0, object1) {
        var result = {};
        for (var attrib in object0) {
            result [attrib] = object0 [attrib];
        }
        for (var attrib in object1) {
            result [attrib] = object1 [attrib];
        }
        return result;
    };
    __all__.__merge__ = __merge__;

    // Manipulating attributes by name
    
    var dir = function (obj) {
        var aList = [];
        for (var aKey in obj) {
            aList.push (aKey);
        }
        aList.sort ();
        return aList;
    };
    __all__.dir = dir;

    var setattr = function (obj, name, value) {
        obj [name] = value;
    };
    __all__.setattr = setattr;

    var getattr = function (obj, name) {
        return obj [name];
    };
    __all__.getattr= getattr;

    var hasattr = function (obj, name) {
        try {
            return name in obj;
        }
        catch (exception) {
            return false;
        }
    };
    __all__.hasattr = hasattr;

    var delattr = function (obj, name) {
        delete obj [name];
    };
    __all__.delattr = (delattr);

    // The __in__ function, used to mimic Python's 'in' operator
    // In addition to CPython's semantics, the 'in' operator is also allowed to work on objects, avoiding a counterintuitive separation between Python dicts and JavaScript objects
    // In general many Transcrypt compound types feature a deliberate blend of Python and JavaScript facilities, facilitating efficient integration with JavaScript libraries
    // If only Python objects and Python dicts are dealt with in a certain context, the more pythonic 'hasattr' is preferred for the objects as opposed to 'in' for the dicts
    var __in__ = function (element, container) {
        if (py_typeof (container) == dict) {        // Currently only implemented as an augmented JavaScript object
            return container.hasOwnProperty (element);
        }
        else {                                      // Parameter 'element' itself is an array, string or a plain, non-dict JavaScript object
            return (
                container.indexOf ?                 // If it has an indexOf
                container.indexOf (element) > -1 :  // it's an array or a string,
                container.hasOwnProperty (element)  // else it's a plain, non-dict JavaScript object
            );
        }
    };
    __all__.__in__ = __in__;

    // Find out if an attribute is special
    var __specialattrib__ = function (attrib) {
        return (attrib.startswith ('__') && attrib.endswith ('__')) || attrib == 'constructor' || attrib.startswith ('py_');
    };
    __all__.__specialattrib__ = __specialattrib__;

    // Compute length of any object
    var len = function (anObject) {
        if (anObject === undefined || anObject === null) {
            return 0;
        }

        if (anObject.__len__ instanceof Function) {
            return anObject.__len__ ();
        }

        if (anObject.length !== undefined) {
            return anObject.length;
        }

        var length = 0;
        for (var attr in anObject) {
            if (!__specialattrib__ (attr)) {
                length++;
            }
        }

        return length;
    };
    __all__.len = len;

    // General conversions and checks

    function __i__ (any) {  //  Convert to iterable
        return py_typeof (any) == dict ? any.py_keys () : any;
    }

    function __k__ (keyed, key) {  //  Check existence of dict key via retrieved element
        var result = keyed [key];
        if (typeof result == 'undefined') {
             throw KeyError (key, new Error());
        }
        return result;
    }

    // If the target object is somewhat true, return it. Otherwise return false.
    // Try to follow Python conventions of truthyness
    function __t__ (target) { 
        return (
            // Avoid invalid checks
            target === undefined || target === null ? false :
            
            // Take a quick shortcut if target is a simple type
            ['boolean', 'number'] .indexOf (typeof target) >= 0 ? target :
            
            // Use __bool__ (if present) to decide if target is true
            target.__bool__ instanceof Function ? (target.__bool__ () ? target : false) :
            
            // There is no __bool__, use __len__ (if present) instead
            target.__len__ instanceof Function ?  (target.__len__ () !== 0 ? target : false) :
            
            // There is no __bool__ and no __len__, declare Functions true.
            // Python objects are transpiled into instances of Function and if
            // there is no __bool__ or __len__, the object in Python is true.
            target instanceof Function ? target :
            
            // Target is something else, compute its len to decide
            len (target) !== 0 ? target :
            
            // When all else fails, declare target as false
            false
        );
    }
    __all__.__t__ = __t__;

    var bool = function (any) {     // Always truly returns a bool, rather than something truthy or falsy
        return !!__t__ (any);
    };
    bool.__name__ = 'bool';         // So it can be used as a type with a name
    __all__.bool = bool;

    var float = function (any) {
        if (any == 'inf') {
            return Infinity;
        }
        else if (any == '-inf') {
            return -Infinity;
        }
        else if (isNaN (parseFloat (any))) {    // Call to parseFloat needed to exclude '', ' ' etc.
            if (any === false) {
                return 0;
            }
            else if (any === true) {
                return 1;
            }
            else {  // Needed e.g. in autoTester.check, so "return any ? true : false" won't do
                throw ValueError ("could not convert string to float: '" + str(any) + "'", new Error ());
            }
        }
        else {
            return +any;
        }
    };
    float.__name__ = 'float';
    __all__.float = float;

    var int = function (any) {
        return float (any) | 0
    };
    int.__name__ = 'int';
    __all__.int = int;

    var py_typeof = function (anObject) {
        var aType = typeof anObject;
        if (aType == 'object') {    // Directly trying '__class__ in anObject' turns out to wreck anObject in Chrome if its a primitive
            try {
                return anObject.__class__;
            }
            catch (exception) {
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
    __all__.py_typeof = py_typeof;

    var isinstance = function (anObject, classinfo) {
        function isA (queryClass) {
            if (queryClass == classinfo) {
                return true;
            }
            for (var index = 0; index < queryClass.__bases__.length; index++) {
                if (isA (queryClass.__bases__ [index], classinfo)) {
                    return true;
                }
            }
            return false;
        }

        if (classinfo instanceof Array) {   // Assume in most cases it isn't, then making it recursive rather than two functions saves a call
            for (var index = 0; index < classinfo.length; index++) {
                var aClass = classinfo [index];
                if (isinstance (anObject, aClass)) {
                    return true;
                }
            }
            return false;
        }

        try {                   // Most frequent use case first
            return '__class__' in anObject ? isA (anObject.__class__) : anObject instanceof classinfo;
        }
        catch (exception) {     // Using isinstance on primitives assumed rare
            var aType = py_typeof (anObject);
            return aType == classinfo || (aType == bool && classinfo == int);
        }
    };
    __all__.isinstance = isinstance;

    var callable = function (anObject) {
        if ( typeof anObject == 'object' && '__call__' in anObject ) {
            return true;
        }
        else {
            return typeof anObject === 'function';
        }
    };
    __all__.callable = callable;

    // Repr function uses __repr__ method, then __str__, then toString
    var repr = function (anObject) {
        try {
            return anObject.__repr__ ();
        }
        catch (exception) {
            try {
                return anObject.__str__ ();
            }
            catch (exception) { // anObject has no __repr__ and no __str__
                try {
                    if (anObject == null) {
                        return 'None';
                    }
                    else if (anObject.constructor == Object) {
                        var result = '{';
                        var comma = false;
                        for (var attrib in anObject) {
                            if (!__specialattrib__ (attrib)) {
                                if (attrib.isnumeric ()) {
                                    var attribRepr = attrib;                // If key can be interpreted as numerical, we make it numerical
                                }                                           // So we accept that '1' is misrepresented as 1
                                else {
                                    var attribRepr = '\'' + attrib + '\'';  // Alpha key in dict
                                }

                                if (comma) {
                                    result += ', ';
                                }
                                else {
                                    comma = true;
                                }
                                result += attribRepr + ': ' + repr (anObject [attrib]);
                            }
                        }
                        result += '}';
                        return result;
                    }
                    else {
                        return typeof anObject == 'boolean' ? anObject.toString () .capitalize () : anObject.toString ();
                    }
                }
                catch (exception) {
                    return '<object of type: ' + typeof anObject + '>';
                }
            }
        }
    };
    __all__.repr = repr;

    // Char from Unicode or ASCII
    var chr = function (charCode) {
        return String.fromCharCode (charCode);
    };
    __all__.chr = chr;

    // Unicode or ASCII from char
    var ord = function (aChar) {
        return aChar.charCodeAt (0);
    };
    __all__.ord = ord;

    // Maximum of n numbers
    var max = Math.max;
    __all__.max = max;

    // Minimum of n numbers
    var min = Math.min;
    __all__.min = min;

    // Absolute value
    var abs = Math.abs;
    __all__.abs = abs;

    // Bankers rounding
    var round = function (number, ndigits) {
        if (ndigits) {
            var scale = Math.pow (10, ndigits);
            number *= scale;
        }

        var rounded = Math.round (number);
        if (rounded - number == 0.5 && rounded % 2) {   // Has rounded up to odd, should have rounded down to even
            rounded -= 1;
        }

        if (ndigits) {
            rounded /= scale;
        }

        return rounded;
    };
    __all__.round = round;

    // BEGIN unified iterator model

    function __jsUsePyNext__ () {       // Add as 'next' method to make Python iterator JavaScript compatible
        try {
            var result = this.__next__ ();
            return {value: result, done: false};
        }
        catch (exception) {
            return {value: undefined, done: true};
        }
    }

    function __pyUseJsNext__ () {       // Add as '__next__' method to make JavaScript iterator Python compatible
        var result = this.next ();
        if (result.done) {
            throw StopIteration (new Error ());
        }
        else {
            return result.value;
        }
    }

    function py_iter (iterable) {                   // Alias for Python's iter function, produces a universal iterator / iterable, usable in Python and JavaScript
        if (typeof iterable == 'string' || '__iter__' in iterable) {    // JavaScript Array or string or Python iterable (string has no 'in')
            var result = iterable.__iter__ ();                          // Iterator has a __next__
            result.next = __jsUsePyNext__;                              // Give it a next
        }
        else if ('selector' in iterable) {                              // Assume it's a JQuery iterator
            var result = list (iterable) .__iter__ ();                  // Has a __next__
            result.next = __jsUsePyNext__;                              // Give it a next
        }
        else if ('next' in iterable) {                                  // It's a JavaScript iterator already,  maybe a generator, has a next and may have a __next__
            var result = iterable
            if (! ('__next__' in result)) {                             // If there's no danger of recursion
                result.__next__ = __pyUseJsNext__;                      // Give it a __next__
            }
        }
        else if (Symbol.iterator in iterable) {                         // It's a JavaScript iterable such as a typed array, but not an iterator
            var result = iterable [Symbol.iterator] ();                 // Has a next
            result.__next__ = __pyUseJsNext__;                          // Give it a __next__
        }
        else {
            throw IterableError (new Error ()); // No iterator at all
        }
        result [Symbol.iterator] = function () {return result;};
        return result;
    }

    function py_next (iterator) {               // Called only in a Python context, could receive Python or JavaScript iterator
        try {                                   // Primarily assume Python iterator, for max speed
            var result = iterator.__next__ ();
        }
        catch (exception) {                     // JavaScript iterators are the exception here
            var result = iterator.next ();
            if (result.done) {
                throw StopIteration (new Error ());
            }
            else {
                return result.value;
            }
        }
        if (result == undefined) {
            throw StopIteration (new Error ());
        }
        else {
            return result;
        }
    }

    function __PyIterator__ (iterable) {
        this.iterable = iterable;
        this.index = 0;
    }

    __PyIterator__.prototype.__next__ = function () {
        if (this.index < this.iterable.length) {
            return this.iterable [this.index++];
        }
        else {
            throw StopIteration (new Error ());
        }
    };

    function __JsIterator__ (iterable) {
        this.iterable = iterable;
        this.index = 0;
    }

    __JsIterator__.prototype.next = function () {
        if (this.index < this.iterable.py_keys.length) {
            return {value: this.index++, done: false};
        }
        else {
            return {value: undefined, done: true};
        }
    };

    // END unified iterator model

    // Reversed function for arrays
    var py_reversed = function (iterable) {
        iterable = iterable.slice ();
        iterable.reverse ();
        return iterable;
    };
    __all__.py_reversed = py_reversed;

    // Zip method for arrays and strings
    var zip = function () {
        var args = [] .slice.call (arguments);
        for (var i = 0; i < args.length; i++) {
            if (typeof args [i] == 'string') {
                args [i] = args [i] .split ('');
            }
            else if (!Array.isArray (args [i])) {
                args [i] = Array.from (args [i]);
            }
        }
        var shortest = args.length == 0 ? [] : args.reduce (    // Find shortest array in arguments
            function (array0, array1) {
                return array0.length < array1.length ? array0 : array1;
            }
        );
        return shortest.map (                   // Map each element of shortest array
            function (current, index) {         // To the result of this function
                return args.map (               // Map each array in arguments
                    function (current) {        // To the result of this function
                        return current [index]; // Namely it's index't entry
                    }
                );
            }
        );
    };
    __all__.zip = zip;

    // Range method, returning an array
    function range (start, stop, step) {
        if (stop == undefined) {
            // one param defined
            stop = start;
            start = 0;
        }
        if (step == undefined) {
            step = 1;
        }
        if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
            return [];
        }
        var result = [];
        for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
            result.push(i);
        }
        return result;
    };
    __all__.range = range;

    // Any, all and sum

    function any (iterable) {
        for (var index = 0; index < iterable.length; index++) {
            if (bool (iterable [index])) {
                return true;
            }
        }
        return false;
    }
    function all (iterable) {
        for (var index = 0; index < iterable.length; index++) {
            if (! bool (iterable [index])) {
                return false;
            }
        }
        return true;
    }
    function sum (iterable) {
        var result = 0;
        for (var index = 0; index < iterable.length; index++) {
            result += iterable [index];
        }
        return result;
    }

    __all__.any = any;
    __all__.all = all;
    __all__.sum = sum;

    // Enumerate method, returning a zipped list
    function enumerate (iterable) {
        return zip (range (len (iterable)), iterable);
    }
    __all__.enumerate = enumerate;

    // Shallow and deepcopy

    function copy (anObject) {
        if (anObject == null || typeof anObject == "object") {
            return anObject;
        }
        else {
            var result = {};
            for (var attrib in obj) {
                if (anObject.hasOwnProperty (attrib)) {
                    result [attrib] = anObject [attrib];
                }
            }
            return result;
        }
    }
    __all__.copy = copy;

    function deepcopy (anObject) {
        if (anObject == null || typeof anObject == "object") {
            return anObject;
        }
        else {
            var result = {};
            for (var attrib in obj) {
                if (anObject.hasOwnProperty (attrib)) {
                    result [attrib] = deepcopy (anObject [attrib]);
                }
            }
            return result;
        }
    }
    __all__.deepcopy = deepcopy;

    // List extensions to Array

    function list (iterable) {                                      // All such creators should be callable without new
        var instance = iterable ? [] .slice.apply (iterable) : [];  // Spread iterable, n.b. array.slice (), so array before dot
        // Sort is the normal JavaScript sort, Python sort is a non-member function
        return instance;
    }
    __all__.list = list;
    Array.prototype.__class__ = list;   // All arrays are lists (not only if constructed by the list ctor), unless constructed otherwise
    list.__name__ = 'list';

    /*
    Array.from = function (iterator) { // !!! remove
        result = [];
        for (item of iterator) {
            result.push (item);
        }
        return result;
    }
    */

    Array.prototype.__iter__ = function () {return new __PyIterator__ (this);};

    Array.prototype.__getslice__ = function (start, stop, step) {
        if (start < 0) {
            start = this.length + start;
        }

        if (stop == null) {
            stop = this.length;
        }
        else if (stop < 0) {
            stop = this.length + stop;
        }
        else if (stop > this.length) {
            stop = this.length;
        }

        var result = list ([]);
        for (var index = start; index < stop; index += step) {
            result.push (this [index]);
        }

        return result;
    };

    Array.prototype.__setslice__ = function (start, stop, step, source) {
        if (start < 0) {
            start = this.length + start;
        }

        if (stop == null) {
            stop = this.length;
        }
        else if (stop < 0) {
            stop = this.length + stop;
        }

        if (step == null) { // Assign to 'ordinary' slice, replace subsequence
            Array.prototype.splice.apply (this, [start, stop - start] .concat (source));
        }
        else {              // Assign to extended slice, replace designated items one by one
            var sourceIndex = 0;
            for (var targetIndex = start; targetIndex < stop; targetIndex += step) {
                this [targetIndex] = source [sourceIndex++];
            }
        }
    };

    Array.prototype.__repr__ = function () {
        if (this.__class__ == set && !this.length) {
            return 'set()';
        }

        var result = !this.__class__ || this.__class__ == list ? '[' : this.__class__ == tuple ? '(' : '{';

        for (var index = 0; index < this.length; index++) {
            if (index) {
                result += ', ';
            }
            result += repr (this [index]);
        }

        if (this.__class__ == tuple && this.length == 1) {
            result += ',';
        }

        result += !this.__class__ || this.__class__ == list ? ']' : this.__class__ == tuple ? ')' : '}';;
        return result;
    };

    Array.prototype.__str__ = Array.prototype.__repr__;

    Array.prototype.append = function (element) {
        this.push (element);
    };

    Array.prototype.py_clear = function () {
        this.length = 0;
    };

    Array.prototype.extend = function (aList) {
        this.push.apply (this, aList);
    };

    Array.prototype.insert = function (index, element) {
        this.splice (index, 0, element);
    };

    Array.prototype.remove = function (element) {
        var index = this.indexOf (element);
        if (index == -1) {
            throw ValueError ("list.remove(x): x not in list", new Error ());
        }
        this.splice (index, 1);
    };

    Array.prototype.index = function (element) {
        return this.indexOf (element);
    };

    Array.prototype.py_pop = function (index) {
        if (index == undefined) {
            return this.pop ();  // Remove last element
        }
        else {
            return this.splice (index, 1) [0];
        }
    };

    Array.prototype.py_sort = function () {
        __sort__.apply  (null, [this].concat ([] .slice.apply (arguments)));    // Can't work directly with arguments
        // Python params: (iterable, key = None, reverse = False)
        // py_sort is called with the Transcrypt kwargs mechanism, and just passes the params on to __sort__
        // __sort__ is def'ed with the Transcrypt kwargs mechanism
    };

    Array.prototype.__add__ = function (aList) {
        return list (this.concat (aList));
    };

    Array.prototype.__mul__ = function (scalar) {
        var result = this;
        for (var i = 1; i < scalar; i++) {
            result = result.concat (this);
        }
        return result;
    };

    Array.prototype.__rmul__ = Array.prototype.__mul__;

    // Tuple extensions to Array

    function tuple (iterable) {
        var instance = iterable ? [] .slice.apply (iterable) : [];
        instance.__class__ = tuple; // Not all arrays are tuples
        return instance;
    }
    __all__.tuple = tuple;
    tuple.__name__ = 'tuple';

    // Set extensions to Array
    // N.B. Since sets are unordered, set operations will occasionally alter the 'this' array by sorting it

    function set (iterable) {
        var instance = [];
        if (iterable) {
            for (var index = 0; index < iterable.length; index++) {
                instance.add (iterable [index]);
            }
        }
        instance.__class__ = set;   // Not all arrays are sets
        return instance;
    }
    __all__.set = set;
    set.__name__ = 'set';

    Array.prototype.__bindexOf__ = function (element) { // Used to turn O (n^2) into O (n log n)
    // Since sorting is lex, compare has to be lex. This also allows for mixed lists

        element += '';

        var mindex = 0;
        var maxdex = this.length - 1;

        while (mindex <= maxdex) {
            var index = (mindex + maxdex) / 2 | 0;
            var middle = this [index] + '';

            if (middle < element) {
                mindex = index + 1;
            }
            else if (middle > element) {
                maxdex = index - 1;
            }
            else {
                return index;
            }
        }

        return -1;
    };

    Array.prototype.add = function (element) {
        if (this.indexOf (element) == -1) { // Avoid duplicates in set
            this.push (element);
        }
    };

    Array.prototype.discard = function (element) {
        var index = this.indexOf (element);
        if (index != -1) {
            this.splice (index, 1);
        }
    };

    Array.prototype.isdisjoint = function (other) {
        this.sort ();
        for (var i = 0; i < other.length; i++) {
            if (this.__bindexOf__ (other [i]) != -1) {
                return false;
            }
        }
        return true;
    };

    Array.prototype.issuperset = function (other) {
        this.sort ();
        for (var i = 0; i < other.length; i++) {
            if (this.__bindexOf__ (other [i]) == -1) {
                return false;
            }
        }
        return true;
    };

    Array.prototype.issubset = function (other) {
        return set (other.slice ()) .issuperset (this); // Sort copy of 'other', not 'other' itself, since it may be an ordered sequence
    };

    Array.prototype.union = function (other) {
        var result = set (this.slice () .sort ());
        for (var i = 0; i < other.length; i++) {
            if (result.__bindexOf__ (other [i]) == -1) {
                result.push (other [i]);
            }
        }
        return result;
    };

    Array.prototype.intersection = function (other) {
        this.sort ();
        var result = set ();
        for (var i = 0; i < other.length; i++) {
            if (this.__bindexOf__ (other [i]) != -1) {
                result.push (other [i]);
            }
        }
        return result;
    };

    Array.prototype.difference = function (other) {
        var sother = set (other.slice () .sort ());
        var result = set ();
        for (var i = 0; i < this.length; i++) {
            if (sother.__bindexOf__ (this [i]) == -1) {
                result.push (this [i]);
            }
        }
        return result;
    };

    Array.prototype.symmetric_difference = function (other) {
        return this.union (other) .difference (this.intersection (other));
    };

    Array.prototype.py_update = function () {   // O (n)
        var updated = [] .concat.apply (this.slice (), arguments) .sort ();
        this.py_clear ();
        for (var i = 0; i < updated.length; i++) {
            if (updated [i] != updated [i - 1]) {
                this.push (updated [i]);
            }
        }
    };

    Array.prototype.__eq__ = function (other) { // Also used for list
        if (this.length != other.length) {
            return false;
        }
        if (this.__class__ == set) {
            this.sort ();
            other.sort ();
        }
        for (var i = 0; i < this.length; i++) {
            if (this [i] != other [i]) {
                return false;
            }
        }
        return true;
    };

    Array.prototype.__ne__ = function (other) { // Also used for list
        return !this.__eq__ (other);
    };

    Array.prototype.__le__ = function (other) {
        return this.issubset (other);
    };

    Array.prototype.__ge__ = function (other) {
        return this.issuperset (other);
    };

    Array.prototype.__lt__ = function (other) {
        return this.issubset (other) && !this.issuperset (other);
    };

    Array.prototype.__gt__ = function (other) {
        return this.issuperset (other) && !this.issubset (other);
    };

    // String extensions

    function str (stringable) {
        try {
            return stringable.__str__ ();
        }
        catch (exception) {
            try {
                return repr (stringable);
            }
            catch (exception) {
                return String (stringable); // No new, so no permanent String object but a primitive in a temporary 'just in time' wrapper
            }
        }
    };
    __all__.str = str;

    String.prototype.__class__ = str;   // All strings are str
    str.__name__ = 'str';

    String.prototype.__iter__ = function () {new __PyIterator__ (this);};

    String.prototype.__repr__ = function () {
        return (this.indexOf ('\'') == -1 ? '\'' + this + '\'' : '"' + this + '"') .py_replace ('\t', '\\t') .py_replace ('\n', '\\n');
    };

    String.prototype.__str__ = function () {
        return this;
    };

    String.prototype.capitalize = function () {
        return this.charAt (0).toUpperCase () + this.slice (1);
    };

    String.prototype.endswith = function (suffix) {
        return suffix == '' || this.slice (-suffix.length) == suffix;
    };

    String.prototype.find  = function (sub, start) {
        return this.indexOf (sub, start);
    };

    String.prototype.__getslice__ = function (start, stop, step) {
        if (start < 0) {
            start = this.length + start;
        }

        if (stop == null) {
            stop = this.length;
        }
        else if (stop < 0) {
            stop = this.length + stop;
        }

        var result = '';
        if (step == 1) {
            result = this.substring (start, stop);
        }
        else {
            for (var index = start; index < stop; index += step) {
                result = result.concat (this.charAt(index));
            }
        }
        return result;
    }

    // Since it's worthwhile for the 'format' function to be able to deal with *args, it is defined as a property
    // __get__ will produce a bound function if there's something before the dot
    // Since a call using *args is compiled to e.g. <object>.<function>.apply (null, args), the function has to be bound already
    // Otherwise it will never be, because of the null argument
    // Using 'this' rather than 'null' contradicts the requirement to be able to pass bound functions around
    // The object 'before the dot' won't be available at call time in that case, unless implicitly via the function bound to it
    // While for Python methods this mechanism is generated by the compiler, for JavaScript methods it has to be provided manually
    // Call memoizing is unattractive here, since every string would then have to hold a reference to a bound format method
    __setProperty__ (String.prototype, 'format', {
        get: function () {return __get__ (this, function (self) {
            var args = tuple ([] .slice.apply (arguments).slice (1));
            var autoIndex = 0;
            return self.replace (/\{(\w*)\}/g, function (match, key) {
                if (key == '') {
                    key = autoIndex++;
                }
                if (key == +key) {  // So key is numerical
                    return args [key] == undefined ? match : str (args [key]);
                }
                else {              // Key is a string
                    for (var index = 0; index < args.length; index++) {
                        // Find first 'dict' that has that key and the right field
                        if (typeof args [index] == 'object' && args [index][key] != undefined) {
                            return str (args [index][key]); // Return that field field
                        }
                    }
                    return match;
                }
            });
        });},
        enumerable: true
    });

    String.prototype.isalnum = function () {
        return /^[0-9a-zA-Z]{1,}$/.test(this)
    }

    String.prototype.isalpha = function () {
        return /^[a-zA-Z]{1,}$/.test(this)
    }

    String.prototype.isdecimal = function () {
        return /^[0-9]{1,}$/.test(this)
    }

    String.prototype.isdigit = function () {
        return this.isdecimal()
    }

    String.prototype.islower = function () {
        return /^[a-z]{1,}$/.test(this)
    }

    String.prototype.isupper = function () {
        return /^[A-Z]{1,}$/.test(this)
    }

    String.prototype.isspace = function () {
        return /^[\s]{1,}$/.test(this)
    }

    String.prototype.isnumeric = function () {
        return !isNaN (parseFloat (this)) && isFinite (this);
    };

    String.prototype.join = function (strings) {
        return strings.join (this);
    };

    String.prototype.lower = function () {
        return this.toLowerCase ();
    };

    String.prototype.py_replace = function (old, aNew, maxreplace) {
        return this.split (old, maxreplace) .join (aNew);
    };

    String.prototype.lstrip = function () {
        return this.replace (/^\s*/g, '');
    };

    String.prototype.rfind = function (sub, start) {
        return this.lastIndexOf (sub, start);
    };

    String.prototype.rsplit = function (sep, maxsplit) {    // Combination of general whitespace sep and positive maxsplit neither supported nor checked, expensive and rare
        if (sep == undefined || sep == null) {
            sep = /\s+/;
            var stripped = this.strip ();
        }
        else {
            var stripped = this;
        }

        if (maxsplit == undefined || maxsplit == -1) {
            return stripped.split (sep);
        }
        else {
            var result = stripped.split (sep);
            if (maxsplit < result.length) {
                var maxrsplit = result.length - maxsplit;
                return [result.slice (0, maxrsplit) .join (sep)] .concat (result.slice (maxrsplit));
            }
            else {
                return result;
            }
        }
    };

    String.prototype.rstrip = function () {
        return this.replace (/\s*$/g, '');
    };

    String.prototype.py_split = function (sep, maxsplit) {  // Combination of general whitespace sep and positive maxsplit neither supported nor checked, expensive and rare
        if (sep == undefined || sep == null) {
            sep = /\s+/;
            var stripped = this.strip ();
        }
        else {
            var stripped = this;
        }

        if (maxsplit == undefined || maxsplit == -1) {
            return stripped.split (sep);
        }
        else {
            var result = stripped.split (sep);
            if (maxsplit < result.length) {
                return result.slice (0, maxsplit).concat ([result.slice (maxsplit).join (sep)]);
            }
            else {
                return result;
            }
        }
    };

    String.prototype.startswith = function (prefix) {
        return this.indexOf (prefix) == 0;
    };

    String.prototype.strip = function () {
        return this.trim ();
    };

    String.prototype.upper = function () {
        return this.toUpperCase ();
    };

    String.prototype.__mul__ = function (scalar) {
        var result = this;
        for (var i = 1; i < scalar; i++) {
            result = result + this;
        }
        return result;
    };

    String.prototype.__rmul__ = String.prototype.__mul__;

    // Dict extensions to object

    function __keys__ () {
        var keys = [];
        for (var attrib in this) {
            if (!__specialattrib__ (attrib)) {
                keys.push (attrib);
            }
        }
        return keys;
    }

    function __items__ () {
        var items = [];
        for (var attrib in this) {
            if (!__specialattrib__ (attrib)) {
                items.push ([attrib, this [attrib]]);
            }
        }
        return items;
    }

    function __del__ (key) {
        delete this [key];
    }

    function __clear__ () {
        for (var attrib in this) {
            delete this [attrib];
        }
    }

    function __getdefault__ (aKey, aDefault) {  // Each Python object already has a function called __get__, so we call this one __getdefault__
        var result = this [aKey];
        return result == undefined ? (aDefault == undefined ? null : aDefault) : result;
    }

    function __setdefault__ (aKey, aDefault) {
        var result = this [aKey];
        if (result != undefined) {
            return result;
        }
        var val = aDefault == undefined ? null : aDefault;
        this [aKey] = val;
        return val;
    }

    function __pop__ (aKey, aDefault) {
        var result = this [aKey];
        if (result != undefined) {
            delete this [aKey];
            return result;
        } else {
            // Identify check because user could pass None
            if ( aDefault === undefined ) {
                throw KeyError (aKey, new Error());
            }
        }
        return aDefault;
    }
    
    function __popitem__ () {
        var aKey = Object.keys (this) [0];
        if (aKey == null) {
            throw KeyError ("popitem(): dictionary is empty", new Error ());
        }
        var result = tuple ([aKey, this [aKey]]);
        delete this [aKey];
        return result;
    }
    
    function __update__ (aDict) {
        for (var aKey in aDict) {
            this [aKey] = aDict [aKey];
        }
    }
    
    function __values__ () {
        var values = [];
        for (var attrib in this) {
            if (!__specialattrib__ (attrib)) {
                values.push (this [attrib]);
            }
        }
        return values;

    }
    
    function __dgetitem__ (aKey) {
        return this [aKey];
    }
    
    function __dsetitem__ (aKey, aValue) {
        this [aKey] = aValue;
    }

    function dict (objectOrPairs) {
        var instance = {};
        if (!objectOrPairs || objectOrPairs instanceof Array) { // It's undefined or an array of pairs
            if (objectOrPairs) {
                for (var index = 0; index < objectOrPairs.length; index++) {
                    var pair = objectOrPairs [index];
                    if ( !(pair instanceof Array) || pair.length != 2) {
                        throw ValueError(
                            "dict update sequence element #" + index +
                            " has length " + pair.length +
                            "; 2 is required", new Error());
                    }
                    var key = pair [0];
                    var val = pair [1];
                    if (!(objectOrPairs instanceof Array) && objectOrPairs instanceof Object) {
                         // User can potentially pass in an object
                         // that has a hierarchy of objects. This
                         // checks to make sure that these objects
                         // get converted to dict objects instead of
                         // leaving them as js objects.
                         
                         if (!isinstance (objectOrPairs, dict)) {
                             val = dict (val);
                         }
                    }
                    instance [key] = val;
                }
            }
        }
        else {
            if (isinstance (objectOrPairs, dict)) {
                // Passed object is a dict already so we need to be a little careful
                // N.B. - this is a shallow copy per python std - so
                // it is assumed that children have already become
                // python objects at some point.
                
                var aKeys = objectOrPairs.py_keys ();
                for (var index = 0; index < aKeys.length; index++ ) {
                    var key = aKeys [index];
                    instance [key] = objectOrPairs [key];
                }
            } else if (objectOrPairs instanceof Object) {
                // Passed object is a JavaScript object but not yet a dict, don't copy it
                instance = objectOrPairs;
            } else {
                // We have already covered Array so this indicates
                // that the passed object is not a js object - i.e.
                // it is an int or a string, which is invalid.
                
                throw ValueError ("Invalid type of object for dict creation", new Error ());
            }
        }

        // Trancrypt interprets e.g. {aKey: 'aValue'} as a Python dict literal rather than a JavaScript object literal
        // So dict literals rather than bare Object literals will be passed to JavaScript libraries
        // Some JavaScript libraries call all enumerable callable properties of an object that's passed to them
        // So the properties of a dict should be non-enumerable
        __setProperty__ (instance, '__class__', {value: dict, enumerable: false, writable: true});
        __setProperty__ (instance, 'py_keys', {value: __keys__, enumerable: false});
        __setProperty__ (instance, '__iter__', {value: function () {new __PyIterator__ (this.py_keys ());}, enumerable: false});
        __setProperty__ (instance, Symbol.iterator, {value: function () {new __JsIterator__ (this.py_keys ());}, enumerable: false});
        __setProperty__ (instance, 'py_items', {value: __items__, enumerable: false});
        __setProperty__ (instance, 'py_del', {value: __del__, enumerable: false});
        __setProperty__ (instance, 'py_clear', {value: __clear__, enumerable: false});
        __setProperty__ (instance, 'py_get', {value: __getdefault__, enumerable: false});
        __setProperty__ (instance, 'py_setdefault', {value: __setdefault__, enumerable: false});
        __setProperty__ (instance, 'py_pop', {value: __pop__, enumerable: false});
        __setProperty__ (instance, 'py_popitem', {value: __popitem__, enumerable: false});
        __setProperty__ (instance, 'py_update', {value: __update__, enumerable: false});
        __setProperty__ (instance, 'py_values', {value: __values__, enumerable: false});
        __setProperty__ (instance, '__getitem__', {value: __dgetitem__, enumerable: false});    // Needed since compound keys necessarily
        __setProperty__ (instance, '__setitem__', {value: __dsetitem__, enumerable: false});    // trigger overloading to deal with slices
        return instance;
    }

    __all__.dict = dict;
    dict.__name__ = 'dict';
    
    // Docstring setter

    function __setdoc__ (docString) {
        this.__doc__ = docString;
        return this;
    }

    // Python classes, methods and functions are all translated to JavaScript functions
    __setProperty__ (Function.prototype, '__setdoc__', {value: __setdoc__, enumerable: false});

    // General operator overloading, only the ones that make most sense in matrix and complex operations

    var __neg__ = function (a) {
        if (typeof a == 'object' && '__neg__' in a) {
            return a.__neg__ ();
        }
        else {
            return -a;
        }
    };
    __all__.__neg__ = __neg__;

    var __matmul__ = function (a, b) {
        return a.__matmul__ (b);
    };
    __all__.__matmul__ = __matmul__;

    var __pow__ = function (a, b) {
        if (typeof a == 'object' && '__pow__' in a) {
            return a.__pow__ (b);
        }
        else if (typeof b == 'object' && '__rpow__' in b) {
            return b.__rpow__ (a);
        }
        else {
            return Math.pow (a, b);
        }
    };
    __all__.pow = __pow__;

    var __jsmod__ = function (a, b) {
        if (typeof a == 'object' && '__mod__' in a) {
            return a.__mod__ (b);
        }
        else if (typeof b == 'object' && '__rpow__' in b) {
            return b.__rmod__ (a);
        }
        else {
            return a % b;
        }
    };
    __all__.__jsmod__ = __jsmod__;
    
    var __mod__ = function (a, b) {
        if (typeof a == 'object' && '__mod__' in a) {
            return a.__mod__ (b);
        }
        else if (typeof b == 'object' && '__rpow__' in b) {
            return b.__rmod__ (a);
        }
        else {
            return ((a % b) + b) % b;
        }
    };
    __all__.mod = __mod__;

    // Overloaded binary arithmetic
    
    var __mul__ = function (a, b) {
        if (typeof a == 'object' && '__mul__' in a) {
            return a.__mul__ (b);
        }
        else if (typeof b == 'object' && '__rmul__' in b) {
            return b.__rmul__ (a);
        }
        else if (typeof a == 'string') {
            return a.__mul__ (b);
        }
        else if (typeof b == 'string') {
            return b.__rmul__ (a);
        }
        else {
            return a * b;
        }
    };
    __all__.__mul__ = __mul__;

    var __truediv__ = function (a, b) {
        if (typeof a == 'object' && '__truediv__' in a) {
            return a.__truediv__ (b);
        }
        else if (typeof b == 'object' && '__rtruediv__' in b) {
            return b.__rtruediv__ (a);
        }
        else if (typeof a == 'object' && '__div__' in a) {
            return a.__div__ (b);
        }
        else if (typeof b == 'object' && '__rdiv__' in b) {
            return b.__rdiv__ (a);
        }
        else {
            return a / b;
        }
    };
    __all__.__truediv__ = __truediv__;

    var __floordiv__ = function (a, b) {
        if (typeof a == 'object' && '__floordiv__' in a) {
            return a.__floordiv__ (b);
        }
        else if (typeof b == 'object' && '__rfloordiv__' in b) {
            return b.__rfloordiv__ (a);
        }
        else if (typeof a == 'object' && '__div__' in a) {
            return a.__div__ (b);
        }
        else if (typeof b == 'object' && '__rdiv__' in b) {
            return b.__rdiv__ (a);
        }
        else {
            return Math.floor (a / b);
        }
    };
    __all__.__floordiv__ = __floordiv__;

    var __add__ = function (a, b) {
        if (typeof a == 'object' && '__add__' in a) {
            return a.__add__ (b);
        }
        else if (typeof b == 'object' && '__radd__' in b) {
            return b.__radd__ (a);
        }
        else {
            return a + b;
        }
    };
    __all__.__add__ = __add__;

    var __sub__ = function (a, b) {
        if (typeof a == 'object' && '__sub__' in a) {
            return a.__sub__ (b);
        }
        else if (typeof b == 'object' && '__rsub__' in b) {
            return b.__rsub__ (a);
        }
        else {
            return a - b;
        }
    };
    __all__.__sub__ = __sub__;

    // Overloaded binary bitwise
    
    var __lshift__ = function (a, b) {
        if (typeof a == 'object' && '__lshift__' in a) {
            return a.__lshift__ (b);
        }
        else if (typeof b == 'object' && '__rlshift__' in b) {
            return b.__rlshift__ (a);
        }
        else {
            return a << b;
        }
    };
    __all__.__lshift__ = __lshift__;

    var __rshift__ = function (a, b) {
        if (typeof a == 'object' && '__rshift__' in a) {
            return a.__rshift__ (b);
        }
        else if (typeof b == 'object' && '__rrshift__' in b) {
            return b.__rrshift__ (a);
        }
        else {
            return a >> b;
        }
    };
    __all__.__rshift__ = __rshift__;

    var __or__ = function (a, b) {
        if (typeof a == 'object' && '__or__' in a) {
            return a.__or__ (b);
        }
        else if (typeof b == 'object' && '__ror__' in b) {
            return b.__ror__ (a);
        }
        else {
            return a | b;
        }
    };
    __all__.__or__ = __or__;

    var __xor__ = function (a, b) {
        if (typeof a == 'object' && '__xor__' in a) {
            return a.__xor__ (b);
        }
        else if (typeof b == 'object' && '__rxor__' in b) {
            return b.__rxor__ (a);
        }
        else {
            return a ^ b;
        }
    };
    __all__.__xor__ = __xor__;

    var __and__ = function (a, b) {
        if (typeof a == 'object' && '__and__' in a) {
            return a.__and__ (b);
        }
        else if (typeof b == 'object' && '__rand__' in b) {
            return b.__rand__ (a);
        }
        else {
            return a & b;
        }
    };
    __all__.__and__ = __and__;

    // Overloaded binary compare
    
    var __eq__ = function (a, b) {
        if (typeof a == 'object' && '__eq__' in a) {
            return a.__eq__ (b);
        }
        else {
            return a == b;
        }
    };
    __all__.__eq__ = __eq__;

    var __ne__ = function (a, b) {
        if (typeof a == 'object' && '__ne__' in a) {
            return a.__ne__ (b);
        }
        else {
            return a != b
        }
    };
    __all__.__ne__ = __ne__;

    var __lt__ = function (a, b) {
        if (typeof a == 'object' && '__lt__' in a) {
            return a.__lt__ (b);
        }
        else {
            return a < b;
        }
    };
    __all__.__lt__ = __lt__;

    var __le__ = function (a, b) {
        if (typeof a == 'object' && '__le__' in a) {
            return a.__le__ (b);
        }
        else {
            return a <= b;
        }
    };
    __all__.__le__ = __le__;

    var __gt__ = function (a, b) {
        if (typeof a == 'object' && '__gt__' in a) {
            return a.__gt__ (b);
        }
        else {
            return a > b;
        }
    };
    __all__.__gt__ = __gt__;

    var __ge__ = function (a, b) {
        if (typeof a == 'object' && '__ge__' in a) {
            return a.__ge__ (b);
        }
        else {
            return a >= b;
        }
    };
    __all__.__ge__ = __ge__;
    
    // Overloaded augmented general
    
    var __imatmul__ = function (a, b) {
        if ('__imatmul__' in a) {
            return a.__imatmul__ (b);
        }
        else {
            return a.__matmul__ (b);
        }
    };
    __all__.__imatmul__ = __imatmul__;

    var __ipow__ = function (a, b) {
        if (typeof a == 'object' && '__pow__' in a) {
            return a.__ipow__ (b);
        }
        else if (typeof a == 'object' && '__ipow__' in a) {
            return a.__pow__ (b);
        }
        else if (typeof b == 'object' && '__rpow__' in b) {
            return b.__rpow__ (a);
        }
        else {
            return Math.pow (a, b);
        }
    };
    __all__.ipow = __ipow__;

    var __ijsmod__ = function (a, b) {
        if (typeof a == 'object' && '__imod__' in a) {
            return a.__ismod__ (b);
        }
        else if (typeof a == 'object' && '__mod__' in a) {
            return a.__mod__ (b);
        }
        else if (typeof b == 'object' && '__rpow__' in b) {
            return b.__rmod__ (a);
        }
        else {
            return a % b;
        }
    };
    __all__.ijsmod__ = __ijsmod__;
    
    var __imod__ = function (a, b) {
        if (typeof a == 'object' && '__imod__' in a) {
            return a.__imod__ (b);
        }
        else if (typeof a == 'object' && '__mod__' in a) {
            return a.__mod__ (b);
        }
        else if (typeof b == 'object' && '__rpow__' in b) {
            return b.__rmod__ (a);
        }
        else {
            return ((a % b) + b) % b;
        }
    };
    __all__.imod = __imod__;
    
    // Overloaded augmented arithmetic
    
    var __imul__ = function (a, b) {
        if (typeof a == 'object' && '__imul__' in a) {
            return a.__imul__ (b);
        }
        else if (typeof a == 'object' && '__mul__' in a) {
            return a = a.__mul__ (b);
        }
        else if (typeof b == 'object' && '__rmul__' in b) {
            return a = b.__rmul__ (a);
        }
        else if (typeof a == 'string') {
            return a = a.__mul__ (b);
        }
        else if (typeof b == 'string') {
            return a = b.__rmul__ (a);
        }
        else {
            return a *= b;
        }
    };
    __all__.__imul__ = __imul__;

    var __idiv__ = function (a, b) {
        if (typeof a == 'object' && '__idiv__' in a) {
            return a.__idiv__ (b);
        }
        else if (typeof a == 'object' && '__div__' in a) {
            return a = a.__div__ (b);
        }
        else if (typeof b == 'object' && '__rdiv__' in b) {
            return a = b.__rdiv__ (a);
        }
        else {
            return a /= b;
        }
    };
    __all__.__idiv__ = __idiv__;

    var __iadd__ = function (a, b) {
        if (typeof a == 'object' && '__iadd__' in a) {
            return a.__iadd__ (b);
        }
        else if (typeof a == 'object' && '__add__' in a) {
            return a = a.__add__ (b);
        }
        else if (typeof b == 'object' && '__radd__' in b) {
            return a = b.__radd__ (a);
        }
        else {
            return a += b;
        }
    };
    __all__.__iadd__ = __iadd__;

    var __isub__ = function (a, b) {
        if (typeof a == 'object' && '__isub__' in a) {
            return a.__isub__ (b);
        }
        else if (typeof a == 'object' && '__sub__' in a) {
            return a = a.__sub__ (b);
        }
        else if (typeof b == 'object' && '__rsub__' in b) {
            return a = b.__rsub__ (a);
        }
        else {
            return a -= b;
        }
    };
    __all__.__isub__ = __isub__;

    // Overloaded augmented bitwise
    
    var __ilshift__ = function (a, b) {
        if (typeof a == 'object' && '__ilshift__' in a) {
            return a.__ilshift__ (b);
        }
        else if (typeof a == 'object' && '__lshift__' in a) {
            return a = a.__lshift__ (b);
        }
        else if (typeof b == 'object' && '__rlshift__' in b) {
            return a = b.__rlshift__ (a);
        }
        else {
            return a <<= b;
        }
    };
    __all__.__ilshift__ = __ilshift__;

    var __irshift__ = function (a, b) {
        if (typeof a == 'object' && '__irshift__' in a) {
            return a.__irshift__ (b);
        }
        else if (typeof a == 'object' && '__rshift__' in a) {
            return a = a.__rshift__ (b);
        }
        else if (typeof b == 'object' && '__rrshift__' in b) {
            return a = b.__rrshift__ (a);
        }
        else {
            return a >>= b;
        }
    };
    __all__.__irshift__ = __irshift__;

    var __ior__ = function (a, b) {
        if (typeof a == 'object' && '__ior__' in a) {
            return a.__ior__ (b);
        }
        else if (typeof a == 'object' && '__or__' in a) {
            return a = a.__or__ (b);
        }
        else if (typeof b == 'object' && '__ror__' in b) {
            return a = b.__ror__ (a);
        }
        else {
            return a |= b;
        }
    };
    __all__.__ior__ = __ior__;

    var __ixor__ = function (a, b) {
        if (typeof a == 'object' && '__ixor__' in a) {
            return a.__ixor__ (b);
        }
        else if (typeof a == 'object' && '__xor__' in a) {
            return a = a.__xor__ (b);
        }
        else if (typeof b == 'object' && '__rxor__' in b) {
            return a = b.__rxor__ (a);
        }
        else {
            return a ^= b;
        }
    };
    __all__.__ixor__ = __ixor__;

    var __iand__ = function (a, b) {
        if (typeof a == 'object' && '__iand__' in a) {
            return a.__iand__ (b);
        }
        else if (typeof a == 'object' && '__and__' in a) {
            return a = a.__and__ (b);
        }
        else if (typeof b == 'object' && '__rand__' in b) {
            return a = b.__rand__ (a);
        }
        else {
            return a &= b;
        }
    };
    __all__.__iand__ = __iand__;
    
    // Indices and slices

    var __getitem__ = function (container, key) {                           // Slice c.q. index, direct generated call to runtime switch
        if (typeof container == 'object' && '__getitem__' in container) {
            return container.__getitem__ (key);                             // Overloaded on container
        }
        else {
            return container [key];                                         // Container must support bare JavaScript brackets
        }
    };
    __all__.__getitem__ = __getitem__;

    var __setitem__ = function (container, key, value) {                    // Slice c.q. index, direct generated call to runtime switch
        if (typeof container == 'object' && '__setitem__' in container) {
            container.__setitem__ (key, value);                             // Overloaded on container
        }
        else {
            container [key] = value;                                        // Container must support bare JavaScript brackets
        }
    };
    __all__.__setitem__ = __setitem__;

    var __getslice__ = function (container, lower, upper, step) {           // Slice only, no index, direct generated call to runtime switch
        if (typeof container == 'object' && '__getitem__' in container) {
            return container.__getitem__ ([lower, upper, step]);            // Container supports overloaded slicing c.q. indexing
        }
        else {
            return container.__getslice__ (lower, upper, step);             // Container only supports slicing injected natively in prototype
        }
    };
    __all__.__getslice__ = __getslice__;

    var __setslice__ = function (container, lower, upper, step, value) {    // Slice, no index, direct generated call to runtime switch
        if (typeof container == 'object' && '__setitem__' in container) {
            container.__setitem__ ([lower, upper, step], value);            // Container supports overloaded slicing c.q. indexing
        }
        else {
            container.__setslice__ (lower, upper, step, value);             // Container only supports slicing injected natively in prototype
        }
    };
    __all__.__setslice__ = __setslice__;
	__nest__ (
		__all__,
		'Acordion', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Acordion';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Acordion = __class__ ('Acordion', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Logo';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<div class='content'>\n\t\t</div>\n\t\t<div  class='btns'>\n\t\t<span class='reordenar'>{}</span>\n\t\t<button class='add'>{}</button>\n\t\t</div>\n\t\t<span class='borrar'>{}</span>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = dict ({});
							self.open = false;
							self.height = 0;
							self.children = list ([]);
							self.backgroundContents = '#999';
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.content');
							});
							self.span = 'Reordenar';
							self.btn = 'Añadir items';
							self.borrar = 'Borrar';
						});},
						get add () {return __get__ (this, function (self, titulo, content, descripcion) {
							if (typeof descripcion == 'undefined' || (descripcion != null && descripcion .hasOwnProperty ("__kwargtrans__"))) {;
								var descripcion = '';
							};
							var w = TabAcordion (titulo, descripcion);
							w.hermanos = self.children;
							w.activador = self.cerrarHermanos;
							w.py_update ();
							self.children.append (w);
							$ (self.target).find ('>.content').append (w.target);
							w.target.find ('>.content').css (dict ({'background-color': self.backgroundContents}));
							var __iterable0__ = content;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								w.add (elem);
							}
						});},
						get addTab () {return __get__ (this, function (self, tab) {
							tab.py_update ();
							self.children.append (tab);
							if (self._update) {
								$ (self.content (self)).append (tab.target);
							}
						});},
						get cerrarHermanos () {return __get__ (this, function (self, target) {
							var __iterable0__ = target.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem != target) {
									elem.cerrar ();
								}
							}
						});},
						get appendToTab () {return __get__ (this, function (self, tab, target) {
							target.py_update ();
							self.children [tab].add (target);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.span, self.btn, self.borrar]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'TabAcordion' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.TabAcordion = TabAcordion;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'AddItem', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'AddItem';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var AddItem = __class__ ('AddItem', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span class='icon'></span>\n\t\t<div>\n\t\t<b>{}</b>\n\t\t<p>{}</p>\n\t\t<div>\n\t\t";
							self.icon = config.base_url + 'static/imgs/iconos/document-2.png';
							self.descripcion = '';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.descripcion]);
							self.__update__ ();
							self.target.find ('>.icon').css (dict ({'background-image': "url('{}')".format (self.icon)}));
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.AddItem = AddItem;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'BandaTema', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BandaTema';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var BandaTema = __class__ ('BandaTema', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<div>\n\t\t<div class="text">\n\t\t{}\n\t\t</div>\n\t\t<button>{}</button>\n\t\t</div>\n\t\t';
							self.text = 'Tema activo:<br>' + settings.app;
							self.btn_titulo = 'Cambiar';
							self._html = self._html.format (self.text, self.btn_titulo);
							$ (self.target).html (self._html);
						});},
						get py_update () {return __get__ (this, function (self) {
							// pass;
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BandaTema = BandaTema;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'BasicSlider', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BasicSlider';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicSlider = __class__ ('BasicSlider', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, tabs) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							if (typeof tabs == 'undefined' || (tabs != null && tabs .hasOwnProperty ("__kwargtrans__"))) {;
								var tabs = 3;
							};
							Widget.__init__ (self, titulo);
							self._html = '';
							self.target.html ('<div></div>');
							self.tabs = function () {
								var __accu0__ = [];
								for (var i = 0; i < tabs; i++) {
									__accu0__.append ($ ("<div class='tab'></div>"));
								}
								return __accu0__;
							} ();
							var __iterable0__ = enumerate (self.tabs);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								if (k != 0) {
									elem.css (dict ({'opacity': '0'}));
								}
								$ (self.target).find ('>div').append (elem);
							}
							self.tabWidth = 300;
							self.width = self.tabWidth * tabs;
							self.tabCurrent = 0;
							self.content = (function __lambda__ (self, k) {
								return self.tabs [k];
							});
						});},
						get showTab () {return __get__ (this, function (self, n) {
							var __iterable0__ = enumerate (self.tabs);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								if (k == n) {
									self.tabs [k].css (dict ({'opacity': '1'}));
								}
								else {
									self.tabs [k].css (dict ({'opacity': '0'}));
								}
							}
							$ ($ (self.target).find ('>div').find ('>.tab') [0]).animate (dict ({'margin-left': -(self.tabWidth) * n}));
						});},
						get addToTab () {return __get__ (this, function (self, n, target) {
							target.py_update ();
							$ ($ (self.target).find ('>div').find ('>.tab') [n]).html (target.target);
						});},
						get getTab () {return __get__ (this, function (self, n) {
							return $ ($ (self.target).find ('>div').find ('>.tab') [n].children [0]);
						});},
						get appendToTab () {return __get__ (this, function (self, n, target) {
							target.py_update ();
							self.tabs [n].append (target.target);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.width = self.tabWidth * len (self.tabs);
							$ (self.target).find ('>div').css (dict ({'width': str (self.width) + 'px'}));
							self.__update__ ();
							$ (self.target).find ('>div').find ('>.tab').css (dict ({'width': str (self.tabWidth) + 'px'}));
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicSlider = BasicSlider;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'BasicTabs', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BasicTabs';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __class__ ('BasicTabs', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, tabs, tabdefault) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							if (typeof tabs == 'undefined' || (tabs != null && tabs .hasOwnProperty ("__kwargtrans__"))) {;
								var tabs = 3;
							};
							if (typeof tabdefault == 'undefined' || (tabdefault != null && tabdefault .hasOwnProperty ("__kwargtrans__"))) {;
								var tabdefault = 0;
							};
							Widget.__init__ (self, titulo);
							$ (self.target).html ('<div></div>');
							self.tabs = function () {
								var __accu0__ = [];
								var __iterable0__ = enumerate (range (tabs));
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var i = __left0__ [1];
									__accu0__.append ((k == tabdefault ? $ ("<div class='tab'></div>") : $ ("<div class='tab hidden'></div>")));
								}
								return __accu0__;
							} ();
							self.children = function () {
								var __accu0__ = [];
								for (var elem = 0; elem < tabs; elem++) {
									__accu0__.append (list ([]));
								}
								return __accu0__;
							} ();
							var __iterable0__ = self.tabs;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ (self.target).find ('>div').append (elem);
							}
							self.tabWidth = 300;
							self.tabCurrent = 0;
							self.tabdefault = tabdefault;
							self.width = self.tabWidth * tabs;
							self.content = (function __lambda__ (self, k) {
								return self.tabs [k];
							});
						});},
						get showTab () {return __get__ (this, function (self, n) {
							$ (self.target).find ('>div').find ('>.tab').addClass ('hidden');
							$ ($ (self.target).find ('>div').find ('>.tab') [n]).removeClass ('hidden');
						});},
						get addToTab () {return __get__ (this, function (self, n, target) {
							target.py_update ();
							self.children [n].append (target);
							$ ($ (self.target).find ('>div').find ('>.tab') [n]).html (target.target);
						});},
						get getTab () {return __get__ (this, function (self, n) {
							return $ ($ (self.target).find ('>div').find ('>.tab') [n]);
						});},
						get appendToTab () {return __get__ (this, function (self, n, target) {
							target.py_update ();
							self.children [n].append (target);
							self.tabs [n].append (target.target);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							$ (self.target).find ('>div').find ('>.tab').css (dict ({'width': self.tabWidth}));
							$ (self.target).find ('>div').css (dict ({'width': self.width}));
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Biblioteca', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Biblioteca';
					var Widget = __init__ (__world__.Widget).Widget;
					var DetalleImagen = __init__ (__world__.DetalleImagen).DetalleImagen;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var Biblioteca = __class__ ('Biblioteca', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, Media) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Subir archivo';
							};
							if (typeof Media == 'undefined' || (Media != null && Media .hasOwnProperty ("__kwargtrans__"))) {;
								var Media = null;
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div class='archivos'>\n\t\t<div><span>{}</span> <input type='search' placeholder='{}'></div>\n\t\t<div class='list'>\n\t\t</div>\n\t\t</div>\n\t\t<div class='detalles'>\n\t\t<b class='titulo'></b>\n\t\t<img class='hidden' src=''>\n\t\t<div class='info'></div>\n\t\t<hr>\n\t\t<table>\n\t\t<tr>\n\t\t<td> URL </td>\n\t\t<td><input name='url'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td>Titulo</td>\n\t\t<td><input name='titulo'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td>Leyenda</td>\n\t\t<td><textarea name='leyenda'></textarea></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td> Texto alternativo </td>\n\t\t<td><input name='alternativo'></td>\n\t\t</tr>\n\t\t<tr>\n\t\t<td> Descripción </td>\n\t\t<td><textarea name='decripcion'></textarea></td>\n\t\t</tr>\n\t\t\n\t\t</table>\n\n\t\t</div>\n\t\t";
							self.Media = Media;
							self._titulo = self.titulo;
							self.sugerencias = 'Dimensiones de imagen sugeridas: 150 por 150 píxeles.';
							self.placeholder = 'Buscar elementos multimedia...';
							self.archivos = list ([]);
							self.currents = list ([]);
							self.base_url = ((config.base_url + config.apps_folder) + settings.app) + '/admin/static/archivos/Imagenes/';
						});},
						get open () {return __get__ (this, function (self) {
							self.Media.updateTitulo (self._titulo);
							self.Media.open ();
						});},
						get search () {return __get__ (this, function (self, evt) {
							var __iterable0__ = self.archivos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (!__in__ ($ (evt.target).val ().lower (), elem.titulo.lower ())) {
									$ (elem.target).addClass ('hidden');
								}
								else {
									$ (elem.target).removeClass ('hidden');
								}
							}
						});},
						get getFiles () {return __get__ (this, function (self) {
							var success = function (data) {
								var archivos = nuclear.normalizar (data);
								var __iterable0__ = archivos;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									var i = DetalleImagen ();
									i.titulo = elem [0];
									i.url = (((config.base_url + config.apps_folder) + settings.app) + '/admin/static/archivos/Imagenes/') + nuclear.thumbail (i.titulo);
									self.archivos.append (i);
								}
							};
							var error = function (objRequest) {
								// pass;
							};
							
							          $.ajax({url:self.url,
							                  async:false,
							                  success: success,
							                  error : error
							                  })
							          
						});},
						get nueva () {return __get__ (this, function (self, file, src) {
							var i = DetalleImagen ();
							var cargar = function () {
								i.refresh ();
								clearInterval (invervalo);
							};
							var invervalo = setInterval (cargar, 3000);
							self.Media.tabsManger.showTab (1);
							i.url = (src != null ? src : self.base_url + nuclear.thumbail (file.name
							));
							i.titulo = file.name
							i.ultimaModificacion = file.lastModified
							i.fechaUltimaModificacion = file.lastModifiedDate
							i.size = file.size
							i.tipo = file.type
							self.archivos.append (i);
							i.actualizarHermanos (self.archivos);
							i.Media = self.Media;
							i.py_update ();
							i.indice = len (self.archivos) - 1;
							$ (self.target).find ('.archivos').find ('.list').prepend (i.target);
						});},
						get clearDetalles () {return __get__ (this, function (self) {
							self.target.find ('.detalles').find ("[name='titulo']").val ('');
							self.target.find ('.detalles').find ('.titulo').html ('');
							self.target.find ('.detalles').find ('.info').html ('');
							self.target.find ('.detalles').find ("[name='url']").val ('');
							self.target.find ('.detalles').find ("[name='descripcion']").val ('');
							self.target.find ('.detalles').find ('img').attr ('src', '');
							self.target.find ('.detalles').find ('img').addClass ('hidden');
							self.currents.append (self.url);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.getFiles ();
							$ (self.target).html (self._html.format (self.sugerencias, self.placeholder));
							var __iterable0__ = enumerate (self.archivos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var i = __left0__ [1];
								i.Media = self.Media;
								i.actualizarHermanos (self.archivos);
								i.deseleccionar (self.archivos);
								i.py_update ();
								i.indice = k;
								$ (self.target).find ('.archivos').find ('.list').append (i.target);
							}
							$ (self.target).find ('.archivos').find ("input[type='search']").bind ('keyup', self.search);
							$ (self.target).find ('button').bind ('click', self.open);
						});}
					});
					__pragma__ ('<use>' +
						'DetalleImagen' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Biblioteca = Biblioteca;
						__all__.DetalleImagen = DetalleImagen;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'BoxScroll', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'BoxScroll';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var BoxScroll = __class__ ('BoxScroll', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BoxScroll = BoxScroll;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Button', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Button';
					var Component = nuclear.Component;
					var Widget = __init__ (__world__.Widget).Widget;
					var Button = __class__ ('Button', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = '<button>{}</button>';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Button = Button;
						__all__.Component = Component;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'ButtonAddItem', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ButtonAddItem';
					var Component = nuclear.Component;
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonAddItem = __class__ ('ButtonAddItem', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<button>\n\t\t<span class='left'>\n\t\t<span class='icon'></span>\n\t\t<b class='titulo'>{}</b>\n\t\t</span>\n\t\t<span class='right'>{}</span>\n\t\t</button>\n\t\t";
							self.descripcion = '';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.formato = list ([self.titulo, self.descripcion]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonAddItem = ButtonAddItem;
						__all__.Component = Component;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'ButtonInput', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ButtonInput';
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonInput = __class__ ('ButtonInput', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<button>{}</button>\n\t\t<div class='content'>\n\t\t<input name='{}' placeholder='{}'>\n\t\t<button>{}</button>\n\t\t</div>\n\t\t";
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.placeholder = '';
							self.open = false;
							self.submit = null;
							self.height = 0;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>.content').animate (dict ({'height': '0px', 'padding': '0px'}), 1000, (function __lambda__ () {
								return $ (self.target).find ('>.content').css (dict ({'height': '0px', 'padding': '0px'}));
							}));
							self.open = false;
						});},
						get abrir () {return __get__ (this, function (self) {
							var abrir = function () {
								$ (self.target).find ('>.content').css (dict ({'height': 'auto', 'padding': '5px'}));
							};
							$ (self.target).find ('>.content').animate (dict ({'height': str (self.height) + 'px', 'padding': '5px'}), 1000, abrir);
							self.open = true;
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (submit != null) {
								self.submit (self);
							}
							self.cerrar ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								self.submit (self);
								self.cerrar ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.py_name, self.placeholder, self.btn));
							var recargar = function () {
								self.height = $ (self.target).find ('>.content').outerHeight ();
								$ (self.target).find ('>.content').css (dict ({'height': '0px'}));
							};
							setTimeout (recargar, 1e-05);
							$ (self.target).find ('>button').bind ('click', self.click);
							$ (self.target).find ('>.content').find ('>button').bind ('click', self.send);
							$ (self.target).find ('>.content').find ('>button').bind ('keyup', self.enter);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonInput = ButtonInput;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'ButtonSettings', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ButtonSettings';
					var Widget = __init__ (__world__.Widget).Widget;
					var ButtonSettings = __class__ ('ButtonSettings', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, siguiente, _screen) {
							if (typeof siguiente == 'undefined' || (siguiente != null && siguiente .hasOwnProperty ("__kwargtrans__"))) {;
								var siguiente = 1;
							};
							if (typeof _screen == 'undefined' || (_screen != null && _screen .hasOwnProperty ("__kwargtrans__"))) {;
								var _screen = 0;
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span>\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t</span>";
							self.slider = null;
							self.screen = null;
							self.descripcion = '';
							self._siguiente = siguiente;
							self._screen = _screen;
						});},
						get siguiente () {return __get__ (this, function (self, evt) {
							self.screen.showTab (self._screen);
							self.slider.showTab (self._siguiente);
						});},
						get py_update () {return __get__ (this, function (self) {
							self._update = true;
							self._html = self._html.format (self.titulo, self.descripcion);
							self.target.bind ('click', self.siguiente);
							$ (self.target).html (self._html);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ButtonSettings = ButtonSettings;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'CheckBox', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'CheckBox';
					var Widget = __init__ (__world__.Widget).Widget;
					var CheckBox = __class__ ('CheckBox', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "<input type='checkbox' name='{}'><span>{}</span>";
							self.py_name = '';
							self.hermanos = list ([]);
							self.activador = null;
							self.desactivador = null;
							self.value = false;
						});},
						get desactivarHermanos () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem != self) {
									elem.desactivar ();
								}
							}
						});},
						get click () {return __get__ (this, function (self) {
							if ($ (self.target).find ("input[type='checkbox']").prop ('checked')) {
								self.activar ();
							}
							else {
								self.desactivar ();
							}
						});},
						get desactivar () {return __get__ (this, function (self, desactivador) {
							if (typeof desactivador == 'undefined' || (desactivador != null && desactivador .hasOwnProperty ("__kwargtrans__"))) {;
								var desactivador = null;
							};
							$ (self.target).find ("input[type='checkbox']").prop ('checked', false);
							if (desactivador != null) {
								self.desactivador = desactivador;
								desactivador ();
							}
							else if (self.desactivador != null) {
								self.desactivador ();
							}
						});},
						get activar () {return __get__ (this, function (self, activador) {
							if (typeof activador == 'undefined' || (activador != null && activador .hasOwnProperty ("__kwargtrans__"))) {;
								var activador = null;
							};
							$ (self.target).find ("input[type='checkbox']").prop ('checked', true);
							if (activador != null) {
								self.activador = activador;
								activador ();
							}
							else if (self.activador != null) {
								self.activador ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.py_name, self.titulo]);
							self.__update__ ();
							$ (self.target).find ("input[type='checkbox']").prop ('checked', self.value);
							$ (self.target).find ("input[type='checkbox']").bind ('click', self.click);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'CheckBoxList', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'CheckBoxList';
					var Widget = __init__ (__world__.Widget).Widget;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var CheckBoxList = __class__ ('CheckBoxList', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<h5>{}</h5>\n\t\t<div class='list'></div>\n\t\t";
							self.value = list ([]);
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.list');
							});
						});},
						get add () {return __get__ (this, function (self, target) {
							if (self._update) {
								target.py_update ();
								self.content (self).append (target.target);
							}
							else {
								self.children.append (target);
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo]);
							self.__update__ ();
							if (len (self.value) != 0 && len (self.children) == 0) {
								if (py_typeof (self.value) == list) {
									var __iterable0__ = self.value;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										var opcion = elem [0] + (len (elem) == 3 ? ('<span>' + elem [2]) + '</span>' : '');
										var w = CheckBox (opcion);
										w.value = elem [1];
										w.py_update ();
										self.content (self).append (w.target);
									}
								}
								else if (py_typeof (self.value) == dict) {
									var __iterable0__ = self.value;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										var w = CheckBox (elem);
										w.value = self.value [elem];
										w.py_update ();
										self.content (self).append (w.target);
									}
								}
							}
						});}
					});
					__pragma__ ('<use>' +
						'CheckBox' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.CheckBoxList = CheckBoxList;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'DetalleImagen', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'DetalleImagen';
					var Widget = __init__ (__world__.Widget).Widget;
					var DetalleImagen = __class__ ('DetalleImagen', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, Media) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Subir archivo';
							};
							if (typeof Media == 'undefined' || (Media != null && Media .hasOwnProperty ("__kwargtrans__"))) {;
								var Media = null;
							};
							Widget.__init__ (self, titulo);
							self._html = "<img src='{}' titulo='{}' leyenda='{}' _alt='{}' ><span class='select'></span>";
							self.Media = Media;
							self._titulo = self.titulo;
							self.url = '';
							self.leyenda = '';
							self._alt = '';
							self.marcado = null;
							self.hermanos = list ([]);
							self.tipo = '';
							self.ultimaModificacion = '';
							self.size = '';
							self.fechaUltimaModificacion = '';
							self.indice = 0;
						});},
						get click () {return __get__ (this, function (self, evt) {
							if (evt.shiftKey) {
								self.marcarHastaActual ();
							}
							else if (evt.ctrlKey) {
								if (self.marcado == null) {
									self.seleccionarMarcados ();
									self.marcar ();
								}
								else {
									self.desmarcar ();
								}
							}
							else if (self.marcado == false || self.marcado == null) {
								self.marcarSolo ();
							}
							else {
								self.desmarcarTodo ();
							}
							self.hayMarcas ();
						});},
						get marcar () {return __get__ (this, function (self) {
							var marcador = $ (self.target).find ('.select');
							self.Media.biblioteca.target.find ('.detalles').find ("[name='titulo']").val (self.titulo);
							self.Media.biblioteca.target.find ('.detalles').find ('.titulo').html ('DETALLES DE ADJUNTOS');
							self.Media.biblioteca.target.find ('.detalles').find ('.info').html ('<br>'.join (list ([self.titulo, self.fechaUltimaModificacion, self.size, self.tipo])));
							self.Media.biblioteca.target.find ('.detalles').find ("[name='url']").val (self.url);
							self.Media.biblioteca.target.find ('.detalles').find ("[name='descripcion']").val (self._alt);
							self.Media.biblioteca.target.find ('.detalles').find ('img').attr ('src', self.url);
							self.Media.biblioteca.target.find ('.detalles').find ('img').removeClass ('hidden');
							self.Media.biblioteca.currents.append (self.url);
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'blue'}));
							marcador.css (dict ({'border': 'solid', 'border-color': 'blue'}));
							self.marcado = true;
						});},
						get marcarSolo () {return __get__ (this, function (self) {
							self.desmarcarHermanos ();
							var marcador = $ (self.target).find ('.select');
							self.Media.biblioteca.target.find ('.detalles').find ("[name='titulo']").val (self.titulo);
							self.Media.biblioteca.target.find ('.detalles').find ('.titulo').html ('DETALLES DE ADJUNTOS');
							self.Media.biblioteca.target.find ('.detalles').find ('.info').html ('<br>'.join (list ([self.titulo, self.fechaUltimaModificacion, self.size, self.tipo])));
							self.Media.biblioteca.target.find ('.detalles').find ("[name='url']").val (self.url);
							self.Media.biblioteca.target.find ('.detalles').find ("[name='descripcion']").val (self._alt);
							self.Media.biblioteca.target.find ('.detalles').find ('img').attr ('src', self.url);
							self.Media.biblioteca.target.find ('.detalles').find ('img').removeClass ('hidden');
							self.Media.biblioteca.current = self.url;
							marcador.css (dict ({'border-color': 'blue'}));
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'blue'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'blue'}));
							self.marcado = true;
						});},
						get actualizarHermanos () {return __get__ (this, function (self, widgets) {
							self.hermanos = widgets;
						});},
						get deseleccionar () {return __get__ (this, function (self) {
							self.marcado = false;
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'transparent', 'box-shadow': '5px rgb(100,100,200)'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'gray'}));
						});},
						get desmarcar () {return __get__ (this, function (self) {
							self.marcado = null;
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'transparent', 'box-shadow': 'none'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'transparent'}));
						});},
						get desmarcarHermanos () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem.target != self.target) {
									elem.desmarcar ();
								}
							}
							self.marcado = null;
							self.hayMarcas ();
						});},
						get desmarcarTodo () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.desmarcar ();
							}
							self.hayMarcas ();
						});},
						get hayMarcas () {return __get__ (this, function (self) {
							var seleccionados = list ([]);
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem.marcado != null) {
									seleccionados.append (elem);
								}
							}
							if (len (seleccionados) == 0) {
								self.Media.noSeleccionados ();
							}
							else {
								self.Media.seleccionados (seleccionados);
							}
						});},
						get refresh () {return __get__ (this, function (self, src) {
							if (typeof src == 'undefined' || (src != null && src .hasOwnProperty ("__kwargtrans__"))) {;
								var src = null;
							};
							if (src == null) {
								var src = $ (self.target).find ('img').attr ('src');
							}
							$ (self.target).find ('img').attr ('src', src);
						});},
						get seleccionar () {return __get__ (this, function (self) {
							$ (self.target).css (dict ({'border': 'solid', 'border-color': 'gray', 'box-shadow': 'none'}));
							$ (self.target).find ('.select').css (dict ({'border': 'solid', 'border-color': 'gray'}));
							self.marcado = false;
						});},
						get seleccionarMarcados () {return __get__ (this, function (self) {
							var __iterable0__ = self.hermanos;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (elem.marcado == true) {
									elem.seleccionar ();
								}
							}
						});},
						get marcarHastaActual () {return __get__ (this, function (self) {
							var desde = null;
							var __iterable0__ = enumerate (self.hermanos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								if (elem.marcado == true && desde == null) {
									var desde = k;
								}
							}
							var hasta = self.hermanos.index (self);
							if (desde < hasta) {
								var __iterable0__ = self.hermanos.__getslice__ (desde, hasta, 1);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									elem.seleccionar ();
								}
							}
							else {
								var __iterable0__ = self.hermanos.__getslice__ (hasta, desde + 1, 1);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									elem.seleccionar ();
								}
							}
							self.marcar ();
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.url, self.titulo, self.leyenda.py_replace ('"', '&#34;').py_replace ("'", '&#39;'), self._alt.py_replace ('"', '&#34;').py_replace ("'", '&#39;')));
							$ (self.target).find ('.select').addClass ('hidden');
							$ (self.target).bind ('click', self.click);
							$ (self.target).find ('img').bind ('click', (function __lambda__ (evt) {
								return $ (evt.target).trigger ('marcar', list ([self.target]));
							}));
							$ (self.target).find ('button').bind ('click', self.open);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.DetalleImagen = DetalleImagen;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'EnlaceButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'EnlaceButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var EnlaceButton = __class__ ('EnlaceButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<button>{}</button>\n\t\t';
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.open = false;
							self.submit = null;
							self.color = 'blue';
						});},
						get click () {return __get__ (this, function (self) {
							if (self.activador != null) {
								self.activador (self);
							}
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (self.submit != null) {
								self.submit (self);
							}
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								if (self.submit != null) {
									self.submit (self);
								}
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							self.target.find ('>button').css ('color', self.color);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButton = EnlaceButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'EnlaceButtonInput', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'EnlaceButtonInput';
					var Widget = __init__ (__world__.Widget).Widget;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var EnlaceButtonInput = __class__ ('EnlaceButtonInput', [EnlaceButton], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							EnlaceButton.__init__ (self, titulo);
							self._html += "\n\t\t<div class='content'>\n\t\t<input name='{}' placeholder='{}'><button>{}</button>\n\t\t</div>\n\t\t";
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.value = null;
							self.open = false;
							self.activador = null;
							self.submit = null;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
							if (self.activador != null) {
								self.activador (self);
							}
						});},
						get abrir () {return __get__ (this, function (self) {
							$ (self.target).find ('>button').css (dict ({'display': 'none'}));
							$ (self.target).find ('>.content').css (dict ({'display': 'block'}));
							self.open = true;
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>button').css (dict ({'display': 'block'}));
							$ (self.target).find ('>.content').css (dict ({'display': 'none'}));
							self.open = false;
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (self.submit != null) {
								self.submit (self);
							}
							self.cerrar ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								if (self.submit != null) {
									self.submit (self);
								}
								self.cerrar ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.py_name, self.placeholder, self.btn));
							$ (self.target).find ('>button').bind ('click', self.click);
							if (!(self.open)) {
								$ (self.target).find ('>.content').css (dict ({'display': 'none'}));
							}
							$ (self.target).find ('>.content').find ('>button').bind ('click', self.send);
						});}
					});
					__pragma__ ('<use>' +
						'EnlaceButton' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButton = EnlaceButton;
						__all__.EnlaceButtonInput = EnlaceButtonInput;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'FileUpload', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'FileUpload';
					var Widget = __init__ (__world__.Widget).Widget;
					var FileUpload = __class__ ('FileUpload', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Arrastra archivos a cualquier lugar para subirlos';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t<form method='post' enctype='multipart/form-data' action='{}'>\n\t\t<h3>{}</h3>\n\t\t<div>o</div> \n\t\t<input type='file' name='archivo'>\n\t\t{}\n\t\t</form>\n\t\t<iframe name='fileupload' class='hidden'></iframe>\n\t\t</div>\n\t\t";
							self.restricciones = '\n\t\t<p>Tamaño máximo de archivo: 128 MB.</p>\n\t\t<p>Dimensiones de imagen sugeridas: 150 por 150 píxeles.</p>\n\t\t';
							self.avanzado = false;
							self.activador = true;
							self.automatico = false;
							self.action = '';
							self.categorias = list ([]);
							self.tipos = list ([]);
							self.iframe = '';
						});},
						get enlazar () {return __get__ (this, function (self, funcion) {
							self.activador = funcion;
						});},
						get subidaAutomatica () {return __get__ (this, function (self, evt) {
							var __iterable0__ = $ (evt.target) [0].files;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var _file = __iterable0__ [__index0__];
								if (self.activador != null) {
									$ (self.target).find ('form').submit ();
									self.activador (_file, null);
								}
							}
						});},
						get subir () {return __get__ (this, function (self, evt) {
							var files = $ (evt.target) [0].files;
							var reader = new FileReader ();
							var __iterable0__ = files;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var file = __iterable0__ [__index0__];
								if (!(self.automatico)) {
									var ver = function (evt, file) {
										if (typeof file == 'undefined' || (file != null && file .hasOwnProperty ("__kwargtrans__"))) {;
											var file = file;
										};
										if (self.activador != null) {
											self.activador (file, evt.target.result);
										}
									};
									reader.onload = ver;
									var f = reader.readAsDataURL (file);
								}
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.action, self.titulo, self.restricciones));
							if (self.avanzado == false) {
								var avanzado = " class='hidden'";
							}
							else {
								var avanzado = '';
							}
							var _html = ('<div ' + avanzado) + ">Renombrar: <input name='renombre' > </div>";
							_html += ('<div ' + avanzado) + ">Categorias: <select name='opcion'>";
							var __iterable0__ = enumerate (self.categorias);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								_html += ((((("<option value='" + str (k)) + "' ") + (k == 0 ? 'selected' : '')) + '>') + elem) + '</option>';
							}
							_html += '</select></div>';
							_html += ('<div ' + avanzado) + ">Tipo: <select name='tipo'>";
							var __iterable0__ = enumerate (self.tipos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								_html += ((((("<option value='" + str (k)) + "' ") + (k == 0 ? 'selected' : '')) + '>') + elem) + '</option>';
							}
							_html += '</select></div>';
							_html += ('<div ' + avanzado) + "> Sobrescribir: <input type='checkbox' name='sobrescribir'></div>";
							$ (self.target).find ('form').append (_html);
							$ (self.target).find ('form').attr ('target', 'fileupload');
							var archivo = $ (self.target).find ("input[type='file']");
							if (self.automatico) {
								archivo.bind ('change', self.subidaAutomatica);
							}
							else {
								archivo.bind ('change', self.subir);
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.FileUpload = FileUpload;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'FooterCustomize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'FooterCustomize';
					var Widget = __init__ (__world__.Widget).Widget;
					var FooterCustomize = __class__ ('FooterCustomize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t<span class='ocultar'> \n\t\t<span class='icon'></span>\n\t\t<span class='text'>{}</span>\n\t\t</span>\n\t\t<div class='responsize'>\n\t\t<span class='desktop'></span>\n\t\t<span class='tablet'></span>\n\t\t<span class='phone'></span>\n\t\t</div>\n\t\t";
							self._atras = atras;
							self.status = 'desktop';
						});},
						get atras () {return __get__ (this, function (self, evt) {
							self.slider.showTab (self._atras);
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							$ (self.target).find ('.atras').bind ('click', self.atras);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.FooterCustomize = FooterCustomize;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'HeaderCustomize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'HeaderCustomize';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __class__ ('HeaderCustomize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t\t<span class='atras'></span>\n\t\t\t<div class='text'>\n\t\t\t\t<p>{}</p>\n\t\t\t\t<h3>{}</h3>\n\t\t\t</div>\n\t\t</div>\n\t\t<p>{}</p>\n\t\t";
							self.pretitulo = 'Estas personalizando: ';
							self.descripcion = '';
							self._atras = atras;
						});},
						get atras () {return __get__ (this, function (self, evt) {
							self.slider.showTab (self._atras);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.pretitulo, self.titulo, self.descripcion]);
							self.__update__ ();
							$ (self.target).find ('.atras').bind ('click', self.atras);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'HeaderCustomizeMain', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'HeaderCustomizeMain';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __class__ ('HeaderCustomizeMain', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div>\n\t\t<div class='text'>\n\t\t<span class='help'>?</span>\n\n\t\t<p>Estas personalizando</p>\n\t\t<h3>{}</h3>\n\t\t<div class='pro'>\n\t\t</div>\n\t\t</div>\n\t\t<div class='info' >\n\t\t<p>{}</p>\n\t\t</div>\n\t\t</div>\n\t\t";
							self._help = '\n\t\tEl personalizador te permite tener una \n\t\tvista previa de los cambios de tu sitio \n\t\tantes de publicarlos. Puedes navegar a \n\t\ttraves de las distintas páginas de tu \n\t\tsitio sin salir de la vista previa. Se \n\t\tmuestran enlaces de editar a algunos \n\t\telementos que lo apliquen.';
							self.proButton = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self._help));
							$ (self.target).find ('.info').addClass ('hidden');
							$ (self.target).find ('.help').bind ('click', (function __lambda__ (evt) {
								return ($(evt.target.parentNode).next().hasClass('hidden')
								 ? $(evt.target.parentNode).next().removeClass('hidden')
								 : $(evt.target.parentNode).next().addClass('hidden')
								);
							}));
							if (self.proButton != null) {
								$ (self.target).find ('.pro').html (self.proButton);
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Iframe', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Iframe';
					var Widget = __init__ (__world__.Widget).Widget;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var Iframe = __class__ ('Iframe', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "<iframe src='{}' name='{}'></iframe>";
							self.icon = config.base_url + 'static/imgs/iconos/document-2.png';
							self.py_name = self.titulo;
							self.source = '';
							self.primitivo = (function __lambda__ (self) {
								return self.target.find ('iframe');
							});
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.source, self.py_name]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Iframe = Iframe;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'ImagenRandom', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'ImagenRandom';
					var Widget = __init__ (__world__.Widget).Widget;
					var ImagenRandom = __class__ ('ImagenRandom', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Sugerido';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='visor'>\n\t\t<p>{}</p>\n\t\t<img src='{}' class='hidden'>\n\t\t</div>\n\t\t<div class='btns'>\n\t\t<button class='btn'><span></span>{}</button>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.btn = 'Imagen sugeriada al azar';
							self.btn2 = 'Cambiar image';
							self.btn1 = 'Eliminar imagen';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = null;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).append (target.target);
						});},
						get updateValue () {return __get__ (this, function (self, valor) {
							self.value = valor;
							if (py_typeof (self.value) == list) {
								self.value = self.value [0];
							}
							$ (self.target).find ('>.visor').find ('img').attr ('src', self.value.url);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});},
						get change () {return __get__ (this, function (self) {
							self.Media.open (self.updateValue);
						});},
						get delete () {return __get__ (this, function (self) {
							self.value = null;
							$ (self.target).find ('>.visor').find ('p').removeClass ('hidden');
							$ (self.target).find ('>.visor').find ('img').attr ('src', '');
							$ (self.target).find ('>.visor').find ('img').addClass ('hidden');
							$ (self.target).find ('>.btns').find ('button').remove ('.btn1');
						});},
						get py_update () {return __get__ (this, function (self) {
							if (self.value != null) {
								self.img = self.value;
							}
							$ (self.target).html (self._html.format (self.titulo, self.descripcion, self.placeholder, self.img, self.btn));
							$ (self.target).find ('.btns').find ('.btn2').bind ('click', self.change);
							if (self.value != null && len ($ (self.target).find ('>.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ImagenRandom = ImagenRandom;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Imagen_de_cabecera', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Imagen_de_cabecera';
					var Widget = __init__ (__world__.Widget).Widget;
					var ImagenRandom = __init__ (__world__.ImagenRandom).ImagenRandom;
					var SubidoAnteriormente = __init__ (__world__.SubidoAnteriormente).SubidoAnteriormente;
					var Imagen_de_cabecera = __class__ ('Imagen_de_cabecera', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Imagen de cabecera';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t<b class='subtitulo'>{}</b>\n\t\t<div class='visor'>\n\t\t<p>{}</p>\n\t\t<img src='{}' class='hidden'>\n\t\t</div>\n\t\t<div class='btns'>\n\t\t<button class='btn2'>{}</button>\n\t\t\n\t\t</div>\n\t\t<div class='actual'>\n\t\t</div>\n\t\t<div class='sugerido'>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.subtitulo = 'Cabecera actual';
							self.btn = 'Añadir nueva imagen';
							self.btn2 = 'Cambiar image';
							self.btn1 = 'Eliminar imagen';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = null;
							self.Wanterior = SubidoAnteriormente ('Subido anteriormente');
							self.Wsugerido = ImagenRandom ('Sugerido');
							var quitar = function () {
								$ (self.target).find ('>.btns').find ('.btn1').remove ();
								$ (self.target).find ('>.visor').find ('img').addClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('img').attr ('src', '');
								self.Wanterior.hidden ();
							};
							self.Wanterior.activador = quitar;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).append (target.target);
						});},
						get updateValue () {return __get__ (this, function (self, valor) {
							self.value = valor;
							if (py_typeof (self.value) == list) {
								self.value = self.value [0];
							}
							$ (self.target).find ('>.visor').find ('img').attr ('src', self.value.url);
							self.Wanterior.show ();
							self.Wanterior.subida (self.value.url);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});},
						get change () {return __get__ (this, function (self) {
							self.Media.open (self.updateValue);
						});},
						get delete () {return __get__ (this, function (self) {
							self.value = null;
							$ (self.target).find ('>.visor').find ('p').removeClass ('hidden');
							$ (self.target).find ('>.visor').find ('img').attr ('src', '');
							$ (self.target).find ('>.visor').find ('img').addClass ('hidden');
							$ (self.target).find ('.btns').find ('button').remove ('.btn1');
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion, self.subtitulo, self.placeholder, self.img, self.btn));
							self.Wanterior.py_update ();
							self.Wanterior.hidden ();
							$ (self.target).find ('.actual').html (self.Wanterior.target);
							self.Wsugerido.value = 'http://localhost:8000/PTC/apps/woodridge/admin/static/archivos/Imagenes/Fondo Tampa otras opciones_540x540.png';
							self.Wsugerido.py_update ();
							$ (self.target).find ('.sugerido').html (self.Wsugerido.target);
							$ (self.target).find ('.btns').find ('.btn2').bind ('click', self.change);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('>.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('>.btns').find ('>.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('>img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('>p').addClass ('hidden');
							}
						});}
					});
					__pragma__ ('<use>' +
						'ImagenRandom' +
						'SubidoAnteriormente' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.ImagenRandom = ImagenRandom;
						__all__.Imagen_de_cabecera = Imagen_de_cabecera;
						__all__.SubidoAnteriormente = SubidoAnteriormente;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Input', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Input';
					var Widget = __init__ (__world__.Widget).Widget;
					var Input = __class__ ('Input', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self.descripcion = '';
							self._html = '<b>{}</b><p>{}</p><input>';
							$ (self.target).css (dict ({'display': 'inline-block'}));
							self.value = null;
							self.content = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.descripcion]);
							self.__update__ ();
							if (self.value != null) {
								$ (self.target).find ('>input').val (str (self.value));
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Input = Input;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'InputAndButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'InputAndButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var InputAndButton = __class__ ('InputAndButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<input name='{}' placeholder='{}'>\n\t\t<button>{}</button>\n\t\t";
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.placeholder = '';
							self.open = false;
							self.submit = null;
							self.height = 0;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>.content').animate (dict ({'height': '0px', 'padding': '0px'}), 1000, (function __lambda__ () {
								return $ (self.target).find ('>.content').css (dict ({'height': '0px', 'padding': '0px'}));
							}));
							self.open = false;
						});},
						get abrir () {return __get__ (this, function (self) {
							var abrir = function () {
								$ (self.target).find ('>.content').css (dict ({'height': 'auto', 'padding': '5px'}));
							};
							$ (self.target).find ('>.content').animate (dict ({'height': str (self.height) + 'px', 'padding': '5px'}), 1000, abrir);
							self.open = true;
						});},
						get send () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							if (submit != null) {
								self.submit (self);
							}
							self.cerrar ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								self.submit (self);
								self.cerrar ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.formato = list ([self.py_name, self.placeholder, self.titulo]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.InputAndButton = InputAndButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'InputSearch', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'InputSearch';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var InputSearch = __class__ ('InputSearch', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "<div><span class='search'></span><input type='search' value='{}' name='{}' placeholder='{}'></div>";
							self.icon = config.base_url + 'static/imgs/iconos/lupa.png';
							self.placeholder = 'Buscar...';
							self.value = '';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.value, self.py_name, self.placeholder]);
							self.__update__ ();
							self.target.find ('>div').find ('>.search').css (dict ({'background-image': "url('{}')".format (self.icon)}));
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.InputSearch = InputSearch;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'LayoutHorizontal', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'LayoutHorizontal';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var settings = nuclear.Settings ();
					var config = Config.Config ();
					var LayoutHorizontal = __class__ ('LayoutHorizontal', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							var widgets = tuple ([].slice.apply (arguments).slice (1));
							Widget.__init__ (self, '');
							self.target.html ('<div></div>');
							var __iterable0__ = widgets;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.add (elem);
							}
							self._html = '';
							self.icon = config.base_url + 'static/imgs/iconos/document-2.png';
							self.content = (function __lambda__ (self, k) {
								return self.target.find ('>div').find ('>div') [k];
							});
						});},
						get add () {return __get__ (this, function (self, widget) {
							self.format = list ([self.titulo]);
							var w = $ ('<div>');
							widget.py_update ();
							self.children.append (widget);
							self.target.find ('>div').append (w);
							widget._update = true;
						});},
						get hiddenTab () {return __get__ (this, function (self, n) {
							$ (self.target.find ('>div').find ('>div') [n]).hide ();
						});},
						get showTab () {return __get__ (this, function (self, n) {
							$ (self.target.find ('>div').find ('>div') [n]).show ();
						});},
						get sliderTab () {return __get__ (this, function (self, n) {
							var width = $ (self.find ('>div').target.find ('>div') [n]).outerWidth ();
							$ (self.target.find ('>div').find ('>div') [n]).css (dict ({'width': '0px'}));
							self.hiddenTab (n);
							$ (self.target.find ('>div').find ('>div') [n]).animate (dict ({'width': str (width) + 'px'}), 1000);
							$ (self.target.find ('>div').find ('>div') [n]).css (dict ({'width': str (width) + 'px'}));
						});},
						get reloadSizes () {return __get__ (this, function (self) {
							var width = 0;
							var __iterable0__ = enumerate (self.children);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								if (k + 1 == len (self.children)) {
									$ (self.target.find ('>div').find ('>div') [k]).css ('width', ('calc( 100% - ' + str (width)) + 'px)');
								}
								width += elem.target.outerWidth ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([]);
							self.__update__ ();
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomizeMain' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.LayoutHorizontal = LayoutHorizontal;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Media', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Media';
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var Biblioteca = __init__ (__world__.Biblioteca).Biblioteca;
					var config = Config.Config ();
					var settings = nuclear.Settings ();
					var Media = __class__ ('Media', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Gestor de Archivos';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<div><b class='titulo'>{}</b><span class='close'>x</span></div>\n\t\t<div class='botonera'>\n\t\t<span class='btn'>{}</span>\n\t\t<span class='btn'>{}</span>\n\t\t</div>\n\t\t<div class='content'>\n\t\t</div>\n\t\t<div>\n\t\t<button class='elegir'>{}</button>\n\t\t</div>\n\t\t";
							self.tabsManger = BasicTabs ();
							self.btn1 = 'Subir archivos';
							self.btn2 = 'Biblioteca Multimedia';
							self.btn3 = 'Elegir';
							self.css_selected = dict ({'color': 'gray', 'border': 'solid', 'border-width': '1px', 'border-radius': '12px 12px 0px 0px'});
							self.css_deselected = dict ({'color': 'blue', 'border': 'none'});
							self.url = (config.base_url + settings.app) + '/admin/Archivos/action=ver';
							self.archivos = list ([]);
							self.biblioteca = Biblioteca ();
							self.biblioteca.Media = self;
							self.biblioteca.url = self.url;
							self.activador = null;
							self.value = list ([]);
						});},
						get subir () {return __get__ (this, function (self, evt) {
							// pass;
						});},
						get open () {return __get__ (this, function (self, activador) {
							self.activador = activador;
							$ (self.target).removeClass ('hidden');
						});},
						get close () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							$ (self.target).addClass ('hidden');
						});},
						get updateTitulo () {return __get__ (this, function (self, titulo) {
							$ (self.target).find ('.titulo').text (titulo);
						});},
						get clickTab () {return __get__ (this, function (self, evt) {
							$ (self.target).find ('.botonera').find ('.btn').css (self.css_deselected);
							$ (evt.target).css (self.css_selected);
							var indice = $ (self.target).find ('.botonera').find ('.btn').index (evt.target);
							self.tabsManger.showTab (indice);
						});},
						get selectTab () {return __get__ (this, function (self, tab) {
							for (var elem = 0; elem < 2; elem++) {
								if (elem == tab) {
									$ ($ (self.target).find ('.botonera').find ('.btn') [tab]).css (self.css_selected);
								}
								else {
									$ ($ (self.target).find ('.botonera').find ('.btn') [tab]).css (self.css_deselected);
								}
							}
						});},
						get noSeleccionados () {return __get__ (this, function (self) {
							self.biblioteca.currents = list ([]);
							self.biblioteca.clearDetalles ();
							$ (self.target).find ('.elegir').css (dict ({'color': 'gray', 'background-color': 'gray'}));
						});},
						get seleccionados () {return __get__ (this, function (self, seleccion) {
							self.biblioteca.currents = seleccion;
							self.currents = seleccion;
							$ (self.target).find ('.elegir').css (dict ({'color': 'white', 'background-color': 'blue'}));
						});},
						get elegir () {return __get__ (this, function (self) {
							self.value = list ([]);
							if (self.currents != list ([])) {
								var __iterable0__ = self.currents;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									self.value.append (elem.indice);
								}
								self.close ();
								self.activador (self.currents);
								return self.currents;
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							var upload = FileUpload ();
							upload.automatico = true;
							upload.action = (config.base_url + settings.app) + '/admin/Archivo/None/action=save';
							upload.categorias = nuclear.VAR ('categorias');
							upload.tipos = nuclear.VAR ('tipos');
							upload.enlazar (self.biblioteca.nueva);
							self.tabsManger.appendToTab (0, upload);
							self.tabsManger.appendToTab (1, self.biblioteca);
							$ (self.target).html (self._html.format (self.titulo, self.btn1, self.btn2, self.btn3));
							$ (self.target).addClass ('hidden');
							$ (self.target).find ('.close').bind ('click', self.close);
							$ ($ (self.target).find ('.botonera').find ('.btn') [1]).css (self.css_selected);
							$ (self.target).find ('.botonera').find ('.btn').bind ('click', self.clickTab);
							if (self.tabsManger != null) {
								self.tabsManger.bind ('subir', self.subir);
								$ (self.target).find ('.content').html (self.tabsManger.target);
							}
							$ (self.target).find ('.elegir').bind ('click', self.elegir);
						});}
					});
					__pragma__ ('<use>' +
						'BasicTabs' +
						'Biblioteca' +
						'FileUpload' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BasicTabs = BasicTabs;
						__all__.Biblioteca = Biblioteca;
						__all__.FileUpload = FileUpload;
						__all__.Media = Media;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'MediaButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'MediaButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var MediaButton = __class__ ('MediaButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, Media) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Subir archivo';
							};
							if (typeof Media == 'undefined' || (Media != null && Media .hasOwnProperty ("__kwargtrans__"))) {;
								var Media = null;
							};
							Widget.__init__ (self, titulo);
							self._html = '<button>{}</button>';
							self.Media = Media;
							self._titulo = self.titulo;
						});},
						get open () {return __get__ (this, function (self) {
							self.Media.updateTitulo (self._titulo);
							self.Media.open ();
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							$ (self.target).find ('button').bind ('click', self.open);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.MediaButton = MediaButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'MediaManager', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'MediaManager';
					var Widget = __init__ (__world__.Widget).Widget;
					var MediaManager = __class__ ('MediaManager', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Logo';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='visor'>\n\t\t<p>{}</p>\n\t\t<img src='{}' class='hidden'>\n\t\t</div>\n\t\t<div class='btns'>\n\t\t<button class='btn2'>{}</button>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.btn = 'Elegir imagen';
							self.btn2 = 'Cambiar image';
							self.btn1 = 'Eliminar imagen';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = null;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).append (target.target);
						});},
						get updateValue () {return __get__ (this, function (self, valor) {
							self.value = valor;
							if (py_typeof (self.value) == list) {
								self.value = self.value [0];
							}
							$ (self.target).find ('.visor').find ('img').attr ('src', self.value.url);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('.visor').find ('p').addClass ('hidden');
							}
						});},
						get change () {return __get__ (this, function (self) {
							self.Media.open (self.updateValue);
						});},
						get delete () {return __get__ (this, function (self) {
							self.value = null;
							$ (self.target).find ('.visor').find ('p').removeClass ('hidden');
							$ (self.target).find ('.visor').find ('img').attr ('src', '');
							$ (self.target).find ('.visor').find ('img').addClass ('hidden');
							$ (self.target).find ('.btns').find ('button').remove ('.btn1');
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion, self.placeholder, self.img, self.btn));
							$ (self.target).find ('.btns').find ('.btn2').bind ('click', self.change);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('.visor').find ('p').addClass ('hidden');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.MediaManager = MediaManager;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'RadioButton', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'RadioButton';
					var Widget = __init__ (__world__.Widget).Widget;
					var RadioButton = __class__ ('RadioButton', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "<input type='radio'><span>{}</span>";
							self.hermanos = list ([]);
						});},
						get activar () {return __get__ (this, function (self) {
							$ (self.target).find ('>input').prop ('checked', true);
							var __iterable0__ = enumerate (self.hermanos);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.desactivar ();
							}
						});},
						get desactivar () {return __get__ (this, function (self) {
							$ (self.target).find ('>input').prop ('checked', false);
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.RadioButton = RadioButton;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'RadioButtonList', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'RadioButtonList';
					var Widget = __init__ (__world__.Widget).Widget;
					var RadioButton = __init__ (__world__.RadioButton).RadioButton;
					var RadioButtonList = __class__ ('RadioButtonList', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='content'>\n\t\t</div>\n\t\t";
							self.descripcion = '';
						});},
						get addOptions () {return __get__ (this, function (self, lista, seleccionado) {
							if (typeof seleccionado == 'undefined' || (seleccionado != null && seleccionado .hasOwnProperty ("__kwargtrans__"))) {;
								var seleccionado = 0;
							};
							var __iterable0__ = enumerate (lista);
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var __left0__ = __iterable0__ [__index0__];
								var k = __left0__ [0];
								var elem = __left0__ [1];
								var w = RadioButton (elem);
								if (k == seleccionado) {
									w.activar ();
								}
								self.children.append (w);
								self.add (w);
							}
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).find ('>.content').append (target.target);
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion));
						});}
					});
					__pragma__ ('<use>' +
						'RadioButton' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.RadioButton = RadioButton;
						__all__.RadioButtonList = RadioButtonList;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Select', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Select';
					var Widget = __init__ (__world__.Widget).Widget;
					var Select = __class__ ('Select', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, atras) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<b>{}</b>\n\t\t<select></select>\n\t\t';
							self.py_name = '';
							self.placeholder = 'Nuevo nombre';
							self.btn = 'Añadir';
							self._atras = atras;
							self.activador = null;
							self.value = null;
							self.open = false;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								$ (self.target).find ('>.content').animate (dict ({'height': '0px'}), 1000);
								self.open = false;
							}
							else {
								$ (self.target).find ('>.content').animate (dict ({'height': 'auto'}), 1000);
								self.open = true;
							}
						});},
						get submit () {return __get__ (this, function (self, evt) {
							if (typeof evt == 'undefined' || (evt != null && evt .hasOwnProperty ("__kwargtrans__"))) {;
								var evt = null;
							};
							self.value = $ (self.target).find ('>.content').find ('>input').val ();
							self.activador ();
						});},
						get enter () {return __get__ (this, function (self, evt) {
							if (evt.keyEnter == true) {
								self.submit ();
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo));
							var __iterable0__ = self.opciones;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ (self.target).find ('>select').append (('<option>' + elem) + '</option>');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Select = Select;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'SelectColor', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SelectColor';
					var Widget = __init__ (__world__.Widget).Widget;
					var SelectColor = __class__ ('SelectColor', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<label>{}</label>\n\t\t<input type='color' name='{}'>\n\t\t";
							self.py_name = '';
							self.value = null;
						});},
						get change () {return __get__ (this, function (self) {
							self.value = $ (self.target).find ("input[type='color']").val ();
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.py_name));
							$ (self.target).find ("input[type='color']").bind ('change', self.change);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.SelectColor = SelectColor;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'SidebarAddItems', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SidebarAddItems';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var BandaTema = __init__ (__world__.BandaTema).BandaTema;
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicSlider = __init__ (__world__.BasicSlider).BasicSlider;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var MediaButton = __init__ (__world__.MediaButton).MediaButton;
					var Identidad_del_sitio = __init__ (__world__._SidebarCustomize.Identidad_del_sitio).Identidad_del_sitio;
					var CabeceraMultimedia = __init__ (__world__._SidebarCustomize.CabeceraMultimedia).CabeceraMultimedia;
					var Menus = __init__ (__world__._SidebarCustomize.Menus).Menus;
					var Colores = __init__ (__world__._SidebarCustomize.Colores).Colores;
					var Widgets = __init__ (__world__._SidebarCustomize.Widgets).Widgets;
					var Imagen_de_fondo = __init__ (__world__._SidebarCustomize.Imagen_de_fondo).Imagen_de_fondo;
					var PortadaEstatica = __init__ (__world__._SidebarCustomize.PortadaEstatica).PortadaEstatica;
					var ThemesOptions = __init__ (__world__._SidebarCustomize.ThemesOptions).ThemesOptions;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var Select = __init__ (__world__.Select).Select;
					var ButtonInput = __init__ (__world__.ButtonInput).ButtonInput;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var InputSearch = __init__ (__world__.InputSearch).InputSearch;
					var Input = __init__ (__world__.Input).Input;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var FooterCustomize = __init__ (__world__.FooterCustomize).FooterCustomize;
					var BoxScroll = __init__ (__world__.BoxScroll).BoxScroll;
					var AddItem = __init__ (__world__.AddItem).AddItem;
					var Button = __init__ (__world__.Button).Button;
					var ButtonAddItem = __init__ (__world__.ButtonAddItem).ButtonAddItem;
					var InputAndButton = __init__ (__world__.InputAndButton).InputAndButton;
					var settings = nuclear.Settings ();
					var SidebarAddItems = __class__ ('SidebarAddItems', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = InputSearch ();
							self.add (w);
							w.target.css ('height', '8vh');
							var b = BoxScroll ();
							var a = Acordion ();
							var t = TabAcordion ('Enlaces personalizados');
							var w = Input ('URL');
							w.value = 'http://';
							t.add (w);
							var w = Input ('Texto del enlace');
							t.add (w);
							var w = Button ('Añadir al menu');
							t.add (w);
							a.addTab (t);
							var t = TabAcordion ('Páginas');
							var _b = BoxScroll ();
							var _w = ButtonAddItem ('Inicio');
							_w.descripcion = 'Enlace personalizado';
							_b.add (_w);
							var _w = ButtonAddItem ('Inicio');
							_w.descripcion = 'Página';
							_b.add (_w);
							t.add (_b);
							var _w = InputAndButton ('Añadir');
							_w.placeholder = 'Añadir nueva pagina';
							t.add (_w);
							a.addTab (t);
							var t = TabAcordion ('Entradas');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							var t = TabAcordion ('Categorias');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							var t = TabAcordion ('Etiquetas');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							var t = TabAcordion ('Formato');
							var _b = BoxScroll ();
							t.add (_b);
							a.addTab (t);
							b.add (a);
							self.add (b);
							b.target.css ('height', '92vh');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'AddItem' +
						'BandaTema' +
						'BasicSlider' +
						'BasicTabs' +
						'BoxScroll' +
						'Button' +
						'ButtonAddItem' +
						'ButtonInput' +
						'ButtonSettings' +
						'EnlaceButton' +
						'FileUpload' +
						'FooterCustomize' +
						'HeaderCustomize' +
						'HeaderCustomizeMain' +
						'Input' +
						'InputAndButton' +
						'InputSearch' +
						'MediaButton' +
						'Select' +
						'TabAcordion' +
						'Textarea' +
						'Widget' +
						'_SidebarCustomize.CabeceraMultimedia' +
						'_SidebarCustomize.Colores' +
						'_SidebarCustomize.Identidad_del_sitio' +
						'_SidebarCustomize.Imagen_de_fondo' +
						'_SidebarCustomize.Menus' +
						'_SidebarCustomize.PortadaEstatica' +
						'_SidebarCustomize.ThemesOptions' +
						'_SidebarCustomize.Widgets' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.AddItem = AddItem;
						__all__.BandaTema = BandaTema;
						__all__.BasicSlider = BasicSlider;
						__all__.BasicTabs = BasicTabs;
						__all__.BoxScroll = BoxScroll;
						__all__.Button = Button;
						__all__.ButtonAddItem = ButtonAddItem;
						__all__.ButtonInput = ButtonInput;
						__all__.ButtonSettings = ButtonSettings;
						__all__.CabeceraMultimedia = CabeceraMultimedia;
						__all__.Colores = Colores;
						__all__.EnlaceButton = EnlaceButton;
						__all__.FileUpload = FileUpload;
						__all__.FooterCustomize = FooterCustomize;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Identidad_del_sitio = Identidad_del_sitio;
						__all__.Imagen_de_fondo = Imagen_de_fondo;
						__all__.Input = Input;
						__all__.InputAndButton = InputAndButton;
						__all__.InputSearch = InputSearch;
						__all__.MediaButton = MediaButton;
						__all__.Menus = Menus;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.Select = Select;
						__all__.SidebarAddItems = SidebarAddItems;
						__all__.TabAcordion = TabAcordion;
						__all__.Textarea = Textarea;
						__all__.ThemesOptions = ThemesOptions;
						__all__.Widget = Widget;
						__all__.Widgets = Widgets;
						__all__.__name__ = __name__;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'SidebarAddWidgets', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SidebarAddWidgets';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var BandaTema = __init__ (__world__.BandaTema).BandaTema;
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicSlider = __init__ (__world__.BasicSlider).BasicSlider;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var MediaButton = __init__ (__world__.MediaButton).MediaButton;
					var Identidad_del_sitio = __init__ (__world__._SidebarCustomize.Identidad_del_sitio).Identidad_del_sitio;
					var CabeceraMultimedia = __init__ (__world__._SidebarCustomize.CabeceraMultimedia).CabeceraMultimedia;
					var Menus = __init__ (__world__._SidebarCustomize.Menus).Menus;
					var Colores = __init__ (__world__._SidebarCustomize.Colores).Colores;
					var Widgets = __init__ (__world__._SidebarCustomize.Widgets).Widgets;
					var Imagen_de_fondo = __init__ (__world__._SidebarCustomize.Imagen_de_fondo).Imagen_de_fondo;
					var PortadaEstatica = __init__ (__world__._SidebarCustomize.PortadaEstatica).PortadaEstatica;
					var ThemesOptions = __init__ (__world__._SidebarCustomize.ThemesOptions).ThemesOptions;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var Select = __init__ (__world__.Select).Select;
					var ButtonInput = __init__ (__world__.ButtonInput).ButtonInput;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var InputSearch = __init__ (__world__.InputSearch).InputSearch;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var FooterCustomize = __init__ (__world__.FooterCustomize).FooterCustomize;
					var BoxScroll = __init__ (__world__.BoxScroll).BoxScroll;
					var AddItem = __init__ (__world__.AddItem).AddItem;
					var settings = nuclear.Settings ();
					var SidebarAddWidgets = __class__ ('SidebarAddWidgets', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = InputSearch ();
							self.add (w);
							w.target.css ('height', '8vh');
							var b = BoxScroll ();
							var w = AddItem ('Archivos');
							w.descripcion = 'Un listado mensual de las entradas de tu sitio';
							b.add (w);
							var w = AddItem ('Archivos');
							w.descripcion = 'Un listado mensual de las entradas de tu sitio';
							b.add (w);
							var w = AddItem ('Archivos');
							w.descripcion = 'Un listado mensual de las entradas de tu sitio';
							b.add (w);
							var w = AddItem ('Archivos');
							w.descripcion = 'Un listado mensual de las entradas de tu sitio';
							b.add (w);
							var w = AddItem ('Archivos');
							w.descripcion = 'Un listado mensual de las entradas de tu sitio';
							b.add (w);
							var w = AddItem ('Archivos');
							w.descripcion = 'Un listado mensual de las entradas de tu sitio';
							b.add (w);
							self.add (b);
							b.target.css ('height', '92vh');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'AddItem' +
						'BandaTema' +
						'BasicSlider' +
						'BasicTabs' +
						'BoxScroll' +
						'ButtonInput' +
						'ButtonSettings' +
						'EnlaceButton' +
						'FileUpload' +
						'FooterCustomize' +
						'HeaderCustomize' +
						'HeaderCustomizeMain' +
						'InputSearch' +
						'MediaButton' +
						'Select' +
						'TabAcordion' +
						'Textarea' +
						'Widget' +
						'_SidebarCustomize.CabeceraMultimedia' +
						'_SidebarCustomize.Colores' +
						'_SidebarCustomize.Identidad_del_sitio' +
						'_SidebarCustomize.Imagen_de_fondo' +
						'_SidebarCustomize.Menus' +
						'_SidebarCustomize.PortadaEstatica' +
						'_SidebarCustomize.ThemesOptions' +
						'_SidebarCustomize.Widgets' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.AddItem = AddItem;
						__all__.BandaTema = BandaTema;
						__all__.BasicSlider = BasicSlider;
						__all__.BasicTabs = BasicTabs;
						__all__.BoxScroll = BoxScroll;
						__all__.ButtonInput = ButtonInput;
						__all__.ButtonSettings = ButtonSettings;
						__all__.CabeceraMultimedia = CabeceraMultimedia;
						__all__.Colores = Colores;
						__all__.EnlaceButton = EnlaceButton;
						__all__.FileUpload = FileUpload;
						__all__.FooterCustomize = FooterCustomize;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Identidad_del_sitio = Identidad_del_sitio;
						__all__.Imagen_de_fondo = Imagen_de_fondo;
						__all__.InputSearch = InputSearch;
						__all__.MediaButton = MediaButton;
						__all__.Menus = Menus;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.Select = Select;
						__all__.SidebarAddWidgets = SidebarAddWidgets;
						__all__.TabAcordion = TabAcordion;
						__all__.Textarea = Textarea;
						__all__.ThemesOptions = ThemesOptions;
						__all__.Widget = Widget;
						__all__.Widgets = Widgets;
						__all__.__name__ = __name__;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'SidebarCustomize', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SidebarCustomize';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomizeMain = __init__ (__world__.HeaderCustomizeMain).HeaderCustomizeMain;
					var BandaTema = __init__ (__world__.BandaTema).BandaTema;
					var Widget = __init__ (__world__.Widget).Widget;
					var BasicSlider = __init__ (__world__.BasicSlider).BasicSlider;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var BasicTabs = __init__ (__world__.BasicTabs).BasicTabs;
					var FileUpload = __init__ (__world__.FileUpload).FileUpload;
					var MediaButton = __init__ (__world__.MediaButton).MediaButton;
					var Identidad_del_sitio = __init__ (__world__._SidebarCustomize.Identidad_del_sitio).Identidad_del_sitio;
					var CabeceraMultimedia = __init__ (__world__._SidebarCustomize.CabeceraMultimedia).CabeceraMultimedia;
					var Menus = __init__ (__world__._SidebarCustomize.Menus).Menus;
					var Colores = __init__ (__world__._SidebarCustomize.Colores).Colores;
					var Widgets = __init__ (__world__._SidebarCustomize.Widgets).Widgets;
					var Imagen_de_fondo = __init__ (__world__._SidebarCustomize.Imagen_de_fondo).Imagen_de_fondo;
					var PortadaEstatica = __init__ (__world__._SidebarCustomize.PortadaEstatica).PortadaEstatica;
					var ThemesOptions = __init__ (__world__._SidebarCustomize.ThemesOptions).ThemesOptions;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var Select = __init__ (__world__.Select).Select;
					var ButtonInput = __init__ (__world__.ButtonInput).ButtonInput;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var Input = __init__ (__world__.Input).Input;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var FooterCustomize = __init__ (__world__.FooterCustomize).FooterCustomize;
					var settings = nuclear.Settings ();
					var SidebarCustomize = __class__ ('SidebarCustomize', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t\t<div class='header-top'>\n\t\t\t\t<span class='close'> X </span><button name='save'>{}</button>\n\t\t\t</div>\n\t\t\t<div class='content'>\n\t\t\t</div>\n\t\t\t<div class='footer-bottom'>\n\t\t\t\t\n\t\t\t\t<span class='ocultar'> \n\t\t\t\t\t<span class='icon'></span>\n\t\t\t\t\t<span class='text'>{}</span>\n\t\t\t\t</span>\n\t\t\t\t<div class='responsive'>\n\t\t\t\t\t<span class='desktop'></span>\n\t\t\t\t\t<span class='tablet'></span>\n\t\t\t\t\t<span class='phone'></span>\n\t\t\t\t</div>\n\t\t\t\t\n\t\t\t</div>\n\t\t";
							self.content = (function __lambda__ (self) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								return self.target.find ('>.content');
							});
							self.btn_save = 'Guardar';
							self.btn_desing = 'Ocultar';
							self.btn_desktop = config.base_url + 'static/imgs/iconos/desktop.png';
							self.btn_tablet = config.base_url + 'static/imgs/iconos/tablet.png';
							self.btn_phone = config.base_url + 'static/imgs/iconos/smartphone.png';
						});},
						get py_update () {return __get__ (this, function (self) {
							self._update = true;
							self.format = list ([self.btn_save, self.btn_desing]);
							self.__update__ ();
							self.target.find ('>.footer-bottom').find ('>.responsive').find ('>.desktop').css ('background-image', "url('{}')".format (self.btn_desktop));
							self.target.find ('>.footer-bottom').find ('>.responsive').find ('>.tablet').css ('background-image', "url('{}')".format (self.btn_tablet));
							self.target.find ('>.footer-bottom').find ('>.responsive').find ('>.phone').css ('background-image', "url('{}')".format (self.btn_phone));
							var screens1 = BasicTabs ('', 10);
							screens1.tabWidth = 280;
							var screens2 = BasicTabs ('', 10);
							screens2.tabWidth = 280;
							var slider = BasicSlider ();
							slider.tabWidth = 280;
							self.add (slider);
							slider.appendToTab (1, screens1);
							slider.appendToTab (2, screens2);
							var w = HeaderCustomizeMain (settings.app);
							slider.appendToTab (0, w);
							var w = BandaTema ();
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Identidad del sitio');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 0;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Colores');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 1;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Cabecera multimedia');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 2;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Menús');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 3;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Widgets');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 4;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Portada estatica');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 5;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('Themes Options');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 6;
							slider.appendToTab (0, w);
							var w = ButtonSettings ('CSS adicional');
							w.slider = slider;
							w.screen = screens1;
							w._screen = 7;
							slider.appendToTab (0, w);
							var w = Identidad_del_sitio ('Identidad del sitio');
							w.Media = self.Media;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (0, w);
							var w = Colores ('Colores');
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (1, w);
							var w = CabeceraMultimedia ('Cabecera multimedia');
							w.Media = self.Media;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (2, w);
							var w = Menus ('Menús');
							w.screen = screens2;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (3, w);
							var w = Widgets ('Widgets');
							w.screen = screens2;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (4, w);
							var w = PortadaEstatica ('Portada estática');
							w.Media = self.Media;
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (5, w);
							var w = ThemesOptions ('Themes Options');
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (6, w);
							var w = HeaderCustomize ('CSS Adicional');
							w.slider = slider;
							w._atras = 0;
							w._screen = 0;
							screens1.appendToTab (7, w);
							var w = Textarea ();
							w.value = '\n\t\t/*\n\t\tPuedes añadir tu propio CSS aquí.\n\t\t\n\t\tHaz clic en el icono de ayuda de arriba para averiguar más.\n\t\t*/\n\t\t';
							screens1.appendToTab (7, w);
							w.target.find ('textarea').css ('height', '90vh');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'BandaTema' +
						'BasicSlider' +
						'BasicTabs' +
						'ButtonInput' +
						'ButtonSettings' +
						'EnlaceButton' +
						'FileUpload' +
						'FooterCustomize' +
						'HeaderCustomize' +
						'HeaderCustomizeMain' +
						'Input' +
						'MediaButton' +
						'Select' +
						'TabAcordion' +
						'Textarea' +
						'Widget' +
						'_SidebarCustomize.CabeceraMultimedia' +
						'_SidebarCustomize.Colores' +
						'_SidebarCustomize.Identidad_del_sitio' +
						'_SidebarCustomize.Imagen_de_fondo' +
						'_SidebarCustomize.Menus' +
						'_SidebarCustomize.PortadaEstatica' +
						'_SidebarCustomize.ThemesOptions' +
						'_SidebarCustomize.Widgets' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.BandaTema = BandaTema;
						__all__.BasicSlider = BasicSlider;
						__all__.BasicTabs = BasicTabs;
						__all__.ButtonInput = ButtonInput;
						__all__.ButtonSettings = ButtonSettings;
						__all__.CabeceraMultimedia = CabeceraMultimedia;
						__all__.Colores = Colores;
						__all__.EnlaceButton = EnlaceButton;
						__all__.FileUpload = FileUpload;
						__all__.FooterCustomize = FooterCustomize;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.HeaderCustomizeMain = HeaderCustomizeMain;
						__all__.Identidad_del_sitio = Identidad_del_sitio;
						__all__.Imagen_de_fondo = Imagen_de_fondo;
						__all__.Input = Input;
						__all__.MediaButton = MediaButton;
						__all__.Menus = Menus;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.Select = Select;
						__all__.SidebarCustomize = SidebarCustomize;
						__all__.TabAcordion = TabAcordion;
						__all__.Textarea = Textarea;
						__all__.ThemesOptions = ThemesOptions;
						__all__.Widget = Widget;
						__all__.Widgets = Widgets;
						__all__.__name__ = __name__;
						__all__.settings = settings;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'SubidoAnteriormente', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'SubidoAnteriormente';
					var Widget = __init__ (__world__.Widget).Widget;
					var SubidoAnteriormente = __class__ ('SubidoAnteriormente', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Sugerido';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='visor'>\n\t\t</div>\n\t\t<div class='btns'>\n\t\t<button class='btn'><span></span>{}</button>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = '';
							self.btn = 'Imagen sugeriada al azar';
							self.btn2 = 'Cambiar image';
							self.btn1 = 'Eliminar imagen';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = list ([]);
							self.activador = null;
						});},
						get subida () {return __get__ (this, function (self, url) {
							self.value.insert (0, url);
							var target = $ ("<div><img src='{}'><span class='close'> x </span></div>".format (url));
							$ (self.target).find ('>.visor').prepend (target);
							$ (target).find ('.close').bind ('click', self.close);
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).append (target.target);
						});},
						get close () {return __get__ (this, function (self, evt) {
							var indice = self.value.index ($(evt.target).prev()[0].src
							);
							self.value.splice(indice,1)
							evt.target.parentNode.parentNode.removeChild (evt.target.parentNode);
							self.estaVacio ();
						});},
						get estaVacio () {return __get__ (this, function (self) {
							if (len (self.value) == 0) {
								self.activador ();
							}
						});},
						get updateValue () {return __get__ (this, function (self, valor) {
							self.value = valor;
							if (py_typeof (self.value) == list) {
								self.value = self.value [0];
							}
							$ (self.target).find ('>.visor').find ('img').attr ('src', self.value.url);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});},
						get delete () {return __get__ (this, function (self) {
							self.value = null;
							$ (self.target).find ('>.visor').find ('p').removeClass ('hidden');
							$ (self.target).find ('>.visor').find ('img').attr ('src', '');
							$ (self.target).find ('>.visor').find ('img').addClass ('hidden');
							$ (self.target).find ('>.btns').find ('button').remove ('.btn1');
						});},
						get py_update () {return __get__ (this, function (self) {
							if (self.value != null) {
								self.img = self.value;
							}
							$ (self.target).html (self._html.format (self.titulo, self.descripcion, self.btn));
							$ (self.target).find ('.btns').find ('.btn2').bind ('click', self.change);
							if (self.value != null && len ($ (self.target).find ('>.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('>.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('>.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('>.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('>.visor').find ('p').addClass ('hidden');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.SubidoAnteriormente = SubidoAnteriormente;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'TabAcordion', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'TabAcordion';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var TabAcordion = __class__ ('TabAcordion', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo, descripcion) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'tab';
							};
							if (typeof descripcion == 'undefined' || (descripcion != null && descripcion .hasOwnProperty ("__kwargtrans__"))) {;
								var descripcion = '';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<span>\n\t\t<b class='titulo'>{}</b>\n\t\t<span>\n\t\t<span class='descripcion'>{}</span>\n\t\t<span class='switch'>\n\t\t</span>\n\t\t</span>\n\t\t\n\t\t</span>\n\t\t<div class='content'>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = descripcion;
							self.btn = config.base_url + 'static/imgs/iconos/arrow-4.png';
							self._btn = config.base_url + 'static/imgs/iconos/arrow-3.png';
							self.placeholder = 'No se ha elegido una imagen';
							self.value = dict ({});
							self.open = false;
							self.height = 0;
							self.activador = null;
							self.content = (function __lambda__ (self) {
								return self.target.find ('>.content');
							});
						});},
						get updateTitulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('>span').find ('>.titulo').text (titulo);
							self.titulo = titulo;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							self.children.append (target);
							if (self._update) {
								$ (self.target).find ('>.content').append (target.target);
								var recargar = function () {
									self.height = 0;
									var __iterable0__ = $ (self.target).find ('>.content').children ();
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem = __iterable0__ [__index0__];
										self.height += $ (elem).outerHeight ();
									}
								};
								setTimeout (recargar, 1e-06);
							}
						});},
						get addList () {return __get__ (this, function (self, lista) {
							var __iterable0__ = lista;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.add (elem);
							}
						});},
						get cerrar () {return __get__ (this, function (self) {
							$ (self.target).find ('>.content').animate (dict ({'height': '0px'}), 1000, (function __lambda__ () {
								return $ (self.target).find ('>.content').css (dict ({'height': '0px', 'padding': '0px'}));
							}));
							$ (self.target).find ('.switch').css ('background-image', ("url('" + self.btn) + "')");
							self.open = false;
						});},
						get abrir () {return __get__ (this, function (self) {
							var abrir = function () {
								$ (self.target).find ('>.content').css (dict ({'height': 'auto', 'padding': '5px'}));
							};
							$ (self.target).find ('>.content').animate (dict ({'height': str (self.height) + 'px'}), 1000, abrir);
							$ (self.target).find ('.switch').css ('background-image', ("url('" + self._btn) + "')");
							self.open = true;
						});},
						get click () {return __get__ (this, function (self) {
							if (self.open) {
								self.cerrar ();
							}
							else {
								self.abrir ();
							}
							if (self.activador != null) {
								self.activador (self);
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.descripcion]);
							self.__update__ ();
							if (self.open) {
								$ (self.target).find ('>.content').css ('height', 'auto');
								$ (self.target).find ('.switch').css ('background-image', ("url('" + self._btn) + "')");
							}
							else {
								$ (self.target).find ('>.content').css ('height', '0px');
								$ (self.target).find ('.switch').css ('background-image', ("url('" + self.btn) + "')");
							}
							$ (self.target).find ('>span').bind ('click', self.click);
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TabAcordion = TabAcordion;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Textarea', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Textarea';
					var Widget = __init__ (__world__.Widget).Widget;
					var Textarea = __class__ ('Textarea', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							Widget.__init__ (self, titulo);
							self.descripcion = '';
							self._html = "<b class='titulo'>{}</b><p class='descripcion'>{}</p><textarea></textarea><p class='postdescripcion'></p>";
							self.postdescripcion;
							$ (self.target).css (dict ({'display': 'inline-block'}));
							self.value = null;
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion));
							if (self.value != null) {
								$ (self.target).find ('>textarea').val (str (self.value));
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Textarea = Textarea;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'TyniMCE', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'TyniMCE';
					var Widget = __init__ (__world__.Widget).Widget;
					var config = Config.Config ();
					var TyniMCE = __class__ ('TyniMCE', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self._html = '\n\t\t<h5>{}</h5>\n\t\t<textarea>{}</textarea>\n\t\t';
							self.editor = null;
							self.value = '';
							self.source = config.base_url + 'static/js/tinymce/js/tinymce/tinymce.min.js';
							self.sources = list ([config.base_url + 'static/js/tinymce/js/tinymce/jquery.tinymce.min.js']);
							self.styles = list ([]);
							self.content_css = config.base_url + 'static/js/tinymce/js/tinymce/skins/lightgray/content.min.css';
							self.lang = 'es';
							self.theme = 'modern';
							self.fontsize_formats = '9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 18pt 20pt 22pt 24pt';
							self.content = (function __lambda__ (self) {
								return self.target.find ('>textarea');
							});
							self.code_langs = list ([dict ({'text': 'HTML/XML', 'value': 'markup'}), dict ({'text': 'JavaScript', 'value': 'javascript'}), dict ({'text': 'CSS', 'value': 'css'}), dict ({'text': 'PHP', 'value': 'php'}), dict ({'text': 'Ruby', 'value': 'ruby'}), dict ({'text': 'Python', 'value': 'python'}), dict ({'text': 'Java', 'value': 'java'}), dict ({'text': 'C', 'value': 'c'}), dict ({'text': 'C#', 'value': 'csharp'}), dict ({'text': 'C++', 'value': 'cpp'})]);
							self.plugins = list (['advlist autolink link image lists charmap print preview hr anchor pagebreak table', 'searchreplace wordcount visualblocks visualchars fullscreen insertdatetime media nonbreaking emoticons textcolor', 'save table contextmenu directionality emoticons template paste textcolor', 'code codesample']);
							self.toolbar = 'insertfile undo redo preview | fontselect | fontsizeselect | forecolor backcolor emoticons | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | media fullpage code codesample';
							self.font_formats = tuple ([((((((((((((((('Andale Mono=andale mono,times;' + 'Arial=arial,helvetica,sans-serif;') + 'Arial Black=arial black,avant garde;') + 'Book Antiqua=book antiqua,palatino;') + 'Comic Sans MS=comic sans ms,sans-serif;') + 'Courier New=courier new,courier;') + 'Georgia=georgia,palatino;') + 'Helvetica=helvetica;') + 'Impact=impact,chicago;') + 'Symbol=symbol;') + 'Tahoma=tahoma,arial,helvetica,sans-serif;') + 'Terminal=terminal,monaco;') + 'Times New Roman=times new roman,times;') + 'Trebuchet MS=trebuchet ms,geneva;') + 'Verdana=verdana,geneva;') + 'Webdings=webdings;') + 'Wingdings=wingdings,zapf dingbats']);
						});},
						get add () {return __get__ (this, function (self, target) {
							if (self._update) {
								target.py_update ();
								self.content (self).append (target.target);
							}
							else {
								self.children.append (target);
							}
						});},
						get reconectar () {return __get__ (this, function (self) {
							self.editor = self.target.find ('>textarea').tinymce (dict ({'language': self.lang, 'theme': self.theme, 'plugins': self.plugins, 'codesample_languages': self.code_langs, 'content_css': self.content_css, 'fontsize_formats': self.fontsize_formats, 'font_formats': self.font_formats}));
						});},
						get forceSources () {return __get__ (this, function (self) {
							var __iterable0__ = self.sources;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ ('footer').append ("<script src='{}'></script>".format (elem));
							}
						});},
						get forceStyles () {return __get__ (this, function (self) {
							var __iterable0__ = self.styles;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								$ ('footer').append ("<link rel='stylesheet' href='{}'>".format (elem));
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo, self.value]);
							self.__update__ ();
							if (!__in__ ('tinymce', dir (window))) {
								$ ('footer').append ("<script src='{}'></script>".format (self.source));
								self.forceSources ();
								var cargar = function () {
									self.reconectar ();
								};
								setTimeout (cargar, 2000);
							}
							else {
								self.reconectar ();
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.TyniMCE = TyniMCE;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'VideoManager', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'VideoManager';
					var Widget = __init__ (__world__.Widget).Widget;
					var VideoManager = __class__ ('VideoManager', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Video';
							};
							Widget.__init__ (self, titulo);
							self._html = "\n\t\t<b class='titulo'>{}</b>\n\t\t<p>{}</p>\n\t\t<div class='visor'>\n\t\t<p>{}</p>\n\t\t<img src='{}' class='hidden'>\n\t\t</div>\n\t\t<div class='btns'>\n\t\t<button class='btn2'>{}</button>\n\t\t</div>\n\t\t";
							self.img = '';
							self.descripcion = '\n\t\tSube tu vídeo en formato .mp4 y minimiza \n\t\tsu tamaño de archivo para obtener mejores \n\t\tresultados. Tu tema recomienda unas \n\t\tdimensiones de 2000 × 1200 pixeles.\n\t\t';
							self.btn = 'Seleccione vídeo';
							self.btn2 = 'Cambiar vídeo';
							self.btn1 = 'Eliminar vídeo';
							self.placeholder = 'No has seleccionado ningún vídeo';
							self.value = null;
						});},
						get add () {return __get__ (this, function (self, target) {
							target.py_update ();
							$ (self.target).append (target.target);
						});},
						get updateValue () {return __get__ (this, function (self, valor) {
							self.value = valor;
							if (py_typeof (self.value) == list) {
								self.value = self.value [0];
							}
							$ (self.target).find ('.visor').find ('img').attr ('src', self.value.url);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('.visor').find ('p').addClass ('hidden');
							}
						});},
						get change () {return __get__ (this, function (self) {
							self.Media.open (self.updateValue);
						});},
						get delete () {return __get__ (this, function (self) {
							self.value = null;
							$ (self.target).find ('.visor').find ('p').removeClass ('hidden');
							$ (self.target).find ('.visor').find ('img').attr ('src', '');
							$ (self.target).find ('.visor').find ('img').addClass ('hidden');
							$ (self.target).find ('.btns').find ('button').remove ('.btn1');
						});},
						get py_update () {return __get__ (this, function (self) {
							$ (self.target).html (self._html.format (self.titulo, self.descripcion, self.placeholder, self.img, self.btn));
							$ (self.target).find ('.btns').find ('.btn2').bind ('click', self.change);
							if (self.value != null && len ($ (self.target).find ('.btns').find ('.btn1')) == 0) {
								$ (self.target).find ('.btns').find ('.btn2').before ("<button class='btn1'>{}</button>".format (self.btn1));
								$ (self.target).find ('.btns').find ('.btn1').bind ('click', self.delete);
								$ (self.target).find ('.visor').find ('img').removeClass ('hidden');
								$ (self.target).find ('.visor').find ('p').addClass ('hidden');
							}
						});}
					});
					__pragma__ ('<use>' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.VideoManager = VideoManager;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'Widget', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Widget';
					var Widget = __class__ ('Widget', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = '';
							};
							self.titulo = titulo;
							self.target = $ (("<div class='" + self.__class__.__name__) + "'></div>");
							self.content = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self._html = '';
							self.media = null;
							self.children = list ([]);
							self.hermanos = list ([]);
							self.value = null;
							self.py_name = '';
							self._update = false;
							self.format = list ([self.titulo]);
							self.primitivo = (function __lambda__ (self, k) {
								if (typeof self == 'undefined' || (self != null && self .hasOwnProperty ("__kwargtrans__"))) {;
									var self = self;
								};
								if (typeof k == 'undefined' || (k != null && k .hasOwnProperty ("__kwargtrans__"))) {;
									var k = null;
								};
								return self.target;
							});
							self.css_styles = list ([]);
							self.descripcion = '';
						});},
						get css () {return __get__ (this, function (self, estilo1, estilo2, py_selector) {
							if (typeof estilo2 == 'undefined' || (estilo2 != null && estilo2 .hasOwnProperty ("__kwargtrans__"))) {;
								var estilo2 = null;
							};
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = null;
							};
							if (self._update) {
								if (py_typeof (estilo1) == str && py_typeof (estilo2) == str && py_selector == str) {
									return self.target.find (py_selector).css (estilo1, estilo2);
								}
								else if ((py_typeof (estilo1) == str || py_typeof (estilo1) == dict) && estilo2 == null && py_selector != null) {
									return self.target.find (py_selector).css (estilo1);
								}
								else if (py_typeof (estilo1) == dict && estilo2 == null && py_selector == null) {
									return self.target.find (py_selector).css (estilo1);
								}
							}
							else {
								self.css_styles.append (list ([estilo1, estilo2, py_selector]));
							}
						});},
						get bind () {return __get__ (this, function (self, evento, funcion, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = null;
							};
							if (py_selector == null) {
								self.target.bind (evento, funcion);
							}
							else {
								$ (self.target).find (py_selector).bind (evento, funcion);
							}
						});},
						get addSeparador () {return __get__ (this, function (self, hr) {
							if (typeof hr == 'undefined' || (hr != null && hr .hasOwnProperty ("__kwargtrans__"))) {;
								var hr = false;
							};
							if (hr) {
								$ (self.target).append ('<hr>');
							}
							else {
								$ (self.target).append ('<br>');
							}
						});},
						get add () {return __get__ (this, function (self, target) {
							self.format = list ([self.titulo]);
							if (self._update) {
								target.py_update ();
								self.children.append (target);
								target._update = true;
								$ (self.content (self)).append (target.target);
							}
							else {
								target.py_update ();
								self.children.append (target);
							}
						});},
						get show () {return __get__ (this, function (self) {
							$ (self.target).removeClass ('hidden');
						});},
						get hidden () {return __get__ (this, function (self) {
							$ (self.target).addClass ('hidden');
						});},
						get updateTitulo () {return __get__ (this, function (self, titulo) {
							self.target.find ('.titulo').text (titulo);
							self.titulo = titulo;
						});},
						get val () {return __get__ (this, function (self) {
							var value = dict ([[self.py_name, list ([])]]);
							if (self.children != list ([])) {
								var __iterable0__ = self.children;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									value [self.py_name] = elem.val ();
								}
								return value;
							}
							else {
								return self.value;
							}
						});},
						get clone () {return __get__ (this, function (self, target) {
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
							var clon = copy (self);
							var clonarChildren = function (widget) {
								var l = list ([]);
								var __iterable0__ = enumerate (widget.children);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									widget.children [k] = copy (widget.children [k]);
									widget.children [k].target = $ (elem.target [0].outerHTML);
									l.append (clonarChildren (widget.children [k]));
								}
								widget.children = l;
								return widget;
							};
							clonarChildren (clon);
							clon.target = $ (clon.target [0].outerHTML);
							clon.reload ();
							return clon;
						});},
						get __update__ () {return __get__ (this, function (self) {
							self._update = true;
							if (self._html != '') {
								self.target.html (self._html.format.apply (null, self.format));
							}
							if (self.children != list ([])) {
								var __iterable0__ = enumerate (self.children);
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var __left0__ = __iterable0__ [__index0__];
									var k = __left0__ [0];
									var elem = __left0__ [1];
									if (py_typeof (elem) == list) {
										var __iterable1__ = enumerate (elem);
										for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
											var __left0__ = __iterable1__ [__index1__];
											var k2 = __left0__ [0];
											var elem2 = __left0__ [1];
											if (self.content != null) {
												$ (self.content (self, k, k2)).append (elem.target);
											}
										}
									}
									else if (self.content != null) {
										$ (self.content (self, k)).append (elem.target);
									}
								}
							}
							if (self.css_styles != list ([])) {
								var __iterable0__ = self.css_styles;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									self.css (elem [0], elem [1], elem [2]);
								}
							}
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
						});},
						get reload () {return __get__ (this, function (self) {
							var __iterable0__ = self.children;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								elem.py_update ();
							}
						});},
						get run () {return __get__ (this, function (self, py_selector) {
							if (typeof py_selector == 'undefined' || (py_selector != null && py_selector .hasOwnProperty ("__kwargtrans__"))) {;
								var py_selector = '.widget';
							};
							self.py_update ();
							$ (py_selector).append (self.target);
						});}
					});
					__pragma__ ('<all>')
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.CabeceraMultimedia', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.CabeceraMultimedia';
					var Widget = __init__ (__world__.Widget).Widget;
					var VideoManager = __init__ (__world__.VideoManager).VideoManager;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var Input = __init__ (__world__.Input).Input;
					var Imagen_de_cabecera = __init__ (__world__.Imagen_de_cabecera).Imagen_de_cabecera;
					var CabeceraMultimedia = __class__ ('CabeceraMultimedia', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = 'Si añades un video, la imagen se utilizara como alternativa\n\t\tmientras que el video carga.\n\t\t';
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.descripcion = self.descripcion;
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = VideoManager ('Video de cabecera');
							self.add (w);
							var w = Input ();
							w.descripcion = 'O escribe una URL de YouTube:';
							self.add (w);
							var w = Imagen_de_cabecera ('Imagen de cabecera');
							w.Media = self.Media;
							self.add (w);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomize' +
						'Imagen_de_cabecera' +
						'Input' +
						'VideoManager' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CabeceraMultimedia = CabeceraMultimedia;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Imagen_de_cabecera = Imagen_de_cabecera;
						__all__.Input = Input;
						__all__.VideoManager = VideoManager;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.Colores', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Colores';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var CheckBoxList = __init__ (__world__.CheckBoxList).CheckBoxList;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var SelectColor = __init__ (__world__.SelectColor).SelectColor;
					var Colores = __class__ ('Colores', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = CheckBoxList ('Color Scheme');
							var _w = CheckBox ('Light');
							w.add (_w);
							var _w = CheckBox ('Negro');
							w.add (_w);
							var _w = CheckBox ('Custom');
							w.add (_w);
							var color = SelectColor ();
							self.add (w);
							var mostrar = function () {
								color.show ();
							};
							var ocultar = function () {
								color.hidden ();
							};
							_w.activador = mostrar;
							_w.desactivador = ocultar;
							color.hidden ();
							self.add (color);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'CheckBox' +
						'CheckBoxList' +
						'HeaderCustomize' +
						'SelectColor' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.CheckBoxList = CheckBoxList;
						__all__.Colores = Colores;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.SelectColor = SelectColor;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.Identidad_del_sitio', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Identidad_del_sitio';
					var Widget = __init__ (__world__.Widget).Widget;
					var Input = __init__ (__world__.Input).Input;
					var MediaManager = __init__ (__world__.MediaManager).MediaManager;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var Identidad_del_sitio = __class__ ('Identidad_del_sitio', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = MediaManager ('Logo');
							w.btn2 = 'Elegir logo';
							w.btn1 = 'Eliminar logo';
							w.Media = self.Media;
							w.placeholder = 'No se a elegido un logo';
							self.add (w);
							var w = Input ('Titulo del sitio');
							self.add (w);
							var w = Input ('Descripción corta');
							self.add (w);
							var w = CheckBox ('Muestra el título y descripción del sitio');
							self.add (w);
							var w = MediaManager ('Icono del sitio');
							w.descripcion = '\n\t\tEl icono del sitio lo usa el navegador \n\t\tcomo icono de la aplicación para tu sitio. \n\t\tLos iconos deben ser cuadrados y al menos de 512 píxeles de ancho y alto.\n\t\t';
							w.placeholder = 'No se a elegido un logo';
							w.Media = self.Media;
							self.add (w);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'CheckBox' +
						'HeaderCustomize' +
						'Input' +
						'MediaManager' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.CheckBox = CheckBox;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Identidad_del_sitio = Identidad_del_sitio;
						__all__.Input = Input;
						__all__.MediaManager = MediaManager;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.Imagen_de_fondo', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Imagen_de_fondo';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var Imagen_de_fondo = __class__ ('Imagen_de_fondo', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = self.__doc__;
						});}
					});
					__pragma__ ('<use>' +
						'HeaderCustomize' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Imagen_de_fondo = Imagen_de_fondo;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.Menus', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Menus';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var ButtonInput = __init__ (__world__.ButtonInput).ButtonInput;
					var Select = __init__ (__world__.Select).Select;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var Input = __init__ (__world__.Input).Input;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var CheckBox = __init__ (__world__.CheckBox).CheckBox;
					var CheckBoxList = __init__ (__world__.CheckBoxList).CheckBoxList;
					var Textarea = __init__ (__world__.Textarea).Textarea;
					var Menus = __class__ ('Menus', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = ButtonSettings ('Ubicaciones de menús');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 0;
							w._siguiente = 2;
							self.add (w);
							self.addSeparador ();
							var w = ButtonSettings ('Menús de enlaces de Redes Sociales');
							w.descripcion = '(Actualmente fijado en: Menú de enlaces de Redes Sociales)';
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 1;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonSettings ('Top Menú');
							w.descripcion = '(Actualmente fijado en: Top Menú)';
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 2;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonInput ('Añadir al menu');
							self.add (w);
							var w = HeaderCustomize ('Ubicaciones de menús');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 3;
							self.descripcion = '\n\t\tTu tema soporta 2 menús. Elige qué menú debería aparecer en cada lugar.\n\n\t\tTambién puedes poner menús en los widgets con el widget “Menú personalizado”\n\t\t';
							self.screen.appendToTab (0, w);
							var w = Select ('Top Menu');
							w.opciones = list (['--Eligir--', 'Menu de enlaces a redes sociales', 'Top menu']);
							self.screen.appendToTab (0, w);
							var e = EnlaceButton ('Editar menu');
							self.screen.appendToTab (0, e);
							var w = Select ('Top Menu');
							w.opciones = list (['--Eligir--', 'Menu de enlaces a redes sociales', 'Top menu']);
							self.screen.appendToTab (0, w);
							var e = EnlaceButton ('Editar menu');
							self.screen.appendToTab (0, e);
							self.screen.tabs [0].find ('>div:nth-child(n+2)').css (dict ({'padding-left': '20px', 'padding-right': '20px'}));
							var w = HeaderCustomize ('Menús de enlaces de Redes Sociales');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 3;
							self.screen.appendToTab (1, w);
							var w = Input ();
							w.value = 'Menús de enlaces de Redes Sociales';
							self.screen.appendToTab (1, w);
							var a = Acordion ('');
							var t = TabAcordion ('Yelp');
							var w = Input ('URL');
							w.value = 'https://www.yelp.com';
							t.add (w);
							var w = Input ('Etiqueta de navegación');
							w.value = 'Yelp';
							t.add (w);
							var w = CheckBox ('Abrir enlace en una nueva pestaña');
							t.add (w);
							var w = Input ('Atributos del titulo');
							t.add (w);
							var w = Input ('Relacion con el enlace (XFN)');
							t.add (w);
							var w = Textarea ('Descripción');
							w.postdescripcion = 'La descripción se mostrará en los menús si el tema actual lo soporta.';
							t.add (w);
							var w = EnlaceButton ('Eliminar');
							t.add (w);
							w.color = 'red';
							a.addTab (t);
							var t2 = t.clone ();
							t2.titulo = 'Facebook';
							t2.children [0].value = 'https://facebook.com';
							t2.reload ();
							a.addTab (t2);
							var t3 = t.clone ();
							t3.titulo = 'Twitter';
							t3.children [0].value = 'https://Twitter.com';
							t3.reload ();
							a.addTab (t3);
							var t4 = t.clone ();
							t4.titulo = 'Instagram';
							t4.children [0].value = 'https://Instagram.com';
							a.addTab (t4);
							var t5 = t.clone ();
							t5.titulo = 'Correo electronico';
							t3.children [0].value = 'jzerpa.occoa@gmail.com';
							a.addTab (t5);
							self.screen.appendToTab (1, a);
							var check = CheckBoxList ('Mostrar ubicación');
							check.value = list ([list (['Top Menu', false, '(Actual: Top Menu)']), list (['Menu de enlaces de Redes Sociales', false, '(Actual: Menu de enlaces de Redes Sociales)'])]);
							self.screen.appendToTab (1, check);
							var check2 = CheckBoxList ('Opciones de menú');
							check2.value = list ([list (['Agregar automaticamente nuevas paginas de nivel superior a este menu', false])]);
							self.screen.appendToTab (1, check2);
							self.screen.tabs [1].find ('>div:nth-child(n+2)').css (dict ({'padding-left': '20px', 'padding-right': '20px'}));
							var w = HeaderCustomize ('Top Menú');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 3;
							self.screen.appendToTab (2, w);
							var w = Input ();
							w.value = 'Top Menu';
							self.screen.appendToTab (2, w);
							var a = Acordion ();
							var t = t.clone ();
							t.titulo = 'Inicio';
							a.addTab (t);
							var t = t.clone ();
							t.titulo = 'Acerca de';
							t.descripcion = 'Pagina';
							a.addTab (t);
							var t = t.clone ();
							t.titulo = 'Blog';
							t.descripcion = 'Pagina';
							a.addTab (t);
							var t = t.clone ();
							t.titulo = 'Contacto';
							t.descripcion = 'Pagina';
							a.addTab (t);
							self.screen.appendToTab (2, a);
							var check = check.clone ();
							self.screen.appendToTab (2, check);
							var check2 = check2.clone ();
							self.screen.appendToTab (2, check2.clone ());
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'ButtonInput' +
						'ButtonSettings' +
						'CheckBox' +
						'CheckBoxList' +
						'EnlaceButton' +
						'HeaderCustomize' +
						'Input' +
						'Select' +
						'TabAcordion' +
						'Textarea' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.ButtonInput = ButtonInput;
						__all__.ButtonSettings = ButtonSettings;
						__all__.CheckBox = CheckBox;
						__all__.CheckBoxList = CheckBoxList;
						__all__.EnlaceButton = EnlaceButton;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Input = Input;
						__all__.Menus = Menus;
						__all__.Select = Select;
						__all__.TabAcordion = TabAcordion;
						__all__.Textarea = Textarea;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.PortadaEstatica', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.PortadaEstatica';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var RadioButtonList = __init__ (__world__.RadioButtonList).RadioButtonList;
					var Select = __init__ (__world__.Select).Select;
					var EnlaceButton = __init__ (__world__.EnlaceButton).EnlaceButton;
					var PortadaEstatica = __class__ ('PortadaEstatica', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = self.__doc__;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							w.descripcion = '\n\t\tTu tema permite una página estatica como\n\t\tportada\n\t\t';
							self.add (w);
							var w = RadioButtonList ('Pagina frontal muestra');
							self.add (w);
							w.addOptions (list (['Tus ultimas entradas', 'Una pagina estatica']), 1);
							var w = Select ('Portada');
							w.opciones = list (['Pagina de ejemplo', 'Inicio', 'Acerca de', 'Contacto', 'Blog']);
							self.add (w);
							var w = EnlaceButton ('+Añadir nueva pagina');
							self.add (w);
							var w = Select ('Página de entradaa');
							w.opciones = list (['Pagina de ejemplo', 'Inicio', 'Acerca de', 'Contacto', 'Blog']);
							self.add (w);
							var w = EnlaceButton ('+Añadir nueva pagina');
							self.add (w);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'EnlaceButton' +
						'HeaderCustomize' +
						'RadioButtonList' +
						'Select' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButton = EnlaceButton;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.PortadaEstatica = PortadaEstatica;
						__all__.RadioButtonList = RadioButtonList;
						__all__.Select = Select;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.ThemesOptions', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.ThemesOptions';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var RadioButtonList = __init__ (__world__.RadioButtonList).RadioButtonList;
					var RadioButton = __init__ (__world__.RadioButton).RadioButton;
					var Select = __init__ (__world__.Select).Select;
					var EnlaceButtonInput = __init__ (__world__.EnlaceButtonInput).EnlaceButtonInput;
					var ThemesOptions = __class__ ('ThemesOptions', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize ('Themes Options');
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var r = RadioButtonList ('Page Layout');
							r.descripcion = '\n\t\tWhen the two-column layout is assigned, \n\t\tthe page title is in one column and \n\t\tcontent is in the other.\n\t\t';
							self.add (r);
							var w = RadioButton ('One Column');
							r.add (w);
							var w = RadioButton ('Two Column');
							r.add (w);
							var w = Select ('From Page Section 1 Content');
							w.descripcion = '\n\t\tSelect pages to feature in each area \n\t\tfrom the dropdowns. Add an image to a \n\t\tsection by setting a featured image in \n\t\tthe page editor. Empty sections will not \n\t\tbe displayed.\n\t\t';
							w.opciones = list (['--Elegir--', 'Pagina de ejemplo', 'Inicio', 'Acerca de', 'Contacto', 'Blog']);
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
							var w = Select ('From Page Section 2 Content');
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
							var w = Select ('From Page Section 3 Content');
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
							var w = Select ('From Page Section 4 Content');
							self.add (w);
							var w = EnlaceButtonInput ('+Añadir nueva página');
							self.add (w);
						});}
					});
					__pragma__ ('<use>' +
						'EnlaceButtonInput' +
						'HeaderCustomize' +
						'RadioButton' +
						'RadioButtonList' +
						'Select' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.EnlaceButtonInput = EnlaceButtonInput;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.RadioButton = RadioButton;
						__all__.RadioButtonList = RadioButtonList;
						__all__.Select = Select;
						__all__.ThemesOptions = ThemesOptions;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	__nest__ (
		__all__,
		'_SidebarCustomize.Widgets', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = '_SidebarCustomize.Widgets';
					var Widget = __init__ (__world__.Widget).Widget;
					var HeaderCustomize = __init__ (__world__.HeaderCustomize).HeaderCustomize;
					var ButtonSettings = __init__ (__world__.ButtonSettings).ButtonSettings;
					var Acordion = __init__ (__world__.Acordion).Acordion;
					var TabAcordion = __init__ (__world__.TabAcordion).TabAcordion;
					var Input = __init__ (__world__.Input).Input;
					var TyniMCE = __init__ (__world__.TyniMCE).TyniMCE;
					var Widgets = __class__ ('Widgets', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							Widget.__init__ (self, titulo);
							self.descripcion = self.__doc__;
						});},
						get py_update () {return __get__ (this, function (self) {
							self.__update__ ();
							var w = HeaderCustomize (self.titulo);
							w.slider = self.slider;
							w._atras = self._atras;
							w._screen = self._screen;
							self.add (w);
							var w = ButtonSettings ('Blog Sidebar');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 3;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonSettings ('Footer 1');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 4;
							w._siguiente = 2;
							self.add (w);
							var w = ButtonSettings ('Footer 2');
							w.slider = self.slider;
							w.screen = self.screen;
							w._screen = 5;
							w._siguiente = 2;
							self.add (w);
							var w = HeaderCustomize ('Blog Sidebar');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 6;
							w.descripcion = '\n\t\tAdd widgets here to appear in your sidebar on\n\t\tblog posts and archive pages.\n\t\t';
							self.screen.appendToTab (3, w);
							var a = Acordion ();
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Encuentranos';
							var w = Input ('Titulo');
							w.value = 'Encuentranos';
							var w = TyniMCE ();
							t.add (w);
							a.addTab (t);
							var t = TabAcordion ('Buscar:');
							t.descripcion = 'Busqueda';
							var w = Input ('Titulo');
							w.value = 'Busqueda';
							a.addTab (w);
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Acerca del sitio';
							var w = Input ('Titulo');
							w.value = 'Acerca del sitio';
							var w = TyniMCE ();
							w.value = '\n\t\tEste puede ser un buen lugar para presentarte y presentar tu sitio o incluir algunos créditos.\n\t\t';
							self.screen.appendToTab (3, a);
							var w = HeaderCustomize ('Footer 1');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 7;
							self.screen.appendToTab (4, w);
							var a = Acordion ();
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Encuentranos';
							var w = Input ('Titulo');
							w.value = 'Encuentranos';
							t.add (w);
							var w = TyniMCE ();
							t.add (w);
							a.addTab (t);
							self.screen.appendToTab (4, a);
							var w = HeaderCustomize ('Footer 2');
							w.slider = self.slider;
							w._atras = 1;
							w._screen = 8;
							self.screen.appendToTab (5, w);
							var a = Acordion ();
							var t = TabAcordion ('HTML:');
							t.descripcion = 'Acerca del sitio';
							var w = Input ('Titulo');
							w.value = 'Acerca del sitio';
							t.add (w);
							var w = TyniMCE ();
							w.value = '\n\t\tEste puede ser un buen lugar para presentarte y presentar tu sitio o incluir algunos créditos.\n\t\t';
							t.add (w);
							a.addTab (t);
							var t = TabAcordion ('Buscar:');
							t.descripcion = 'Busqueda';
							var w = Input ('Titulo');
							w.value = 'Busqueda';
							t.add (w);
							a.addTab (t);
							self.screen.appendToTab (5, a);
							self.css (dict ({'padding-left': '20px', 'padding-right': '20px'}), null, '>div:nth-child(n+2)');
						});}
					});
					__pragma__ ('<use>' +
						'Acordion' +
						'ButtonSettings' +
						'HeaderCustomize' +
						'Input' +
						'TabAcordion' +
						'TyniMCE' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.Acordion = Acordion;
						__all__.ButtonSettings = ButtonSettings;
						__all__.HeaderCustomize = HeaderCustomize;
						__all__.Input = Input;
						__all__.TabAcordion = TabAcordion;
						__all__.TyniMCE = TyniMCE;
						__all__.Widget = Widget;
						__all__.Widgets = Widgets;
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
	(function () {
		var __name__ = '__main__';
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
		var LayoutHorizontal = __init__ (__world__.LayoutHorizontal).LayoutHorizontal;
		var SidebarCustomize = __init__ (__world__.SidebarCustomize).SidebarCustomize;
		var SidebarAddItems = __init__ (__world__.SidebarAddItems).SidebarAddItems;
		var SidebarAddWidgets = __init__ (__world__.SidebarAddWidgets).SidebarAddWidgets;
		var Iframe = __init__ (__world__.Iframe).Iframe;
		var Media = __init__ (__world__.Media).Media;
		var l = LayoutHorizontal ();
		var i = Iframe ();
		i.css (dict ({'width': '100%', 'height': 'calc( 100vh - 5px )', 'background-color': 'gray'}), null, '>iframe');
		var media = Media ();
		var sidebar = SidebarCustomize ();
		sidebar.Media = media;
		var sidebar2 = SidebarAddItems ();
		var sidebar3 = SidebarAddWidgets ();
		l.add (sidebar);
		l.add (sidebar2);
		l.add (sidebar3);
		l.add (i);
		media.run ($ ('footer'));
		l.run ($ ('section'));
		l.reloadSizes ();
		__pragma__ ('<use>' +
			'Iframe' +
			'LayoutHorizontal' +
			'Media' +
			'SidebarAddItems' +
			'SidebarAddWidgets' +
			'SidebarCustomize' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Iframe = Iframe;
			__all__.LayoutHorizontal = LayoutHorizontal;
			__all__.Media = Media;
			__all__.SidebarAddItems = SidebarAddItems;
			__all__.SidebarAddWidgets = SidebarAddWidgets;
			__all__.SidebarCustomize = SidebarCustomize;
			__all__.__name__ = __name__;
			__all__.copy = copy;
			__all__.i = i;
			__all__.l = l;
			__all__.media = media;
			__all__.sidebar = sidebar;
			__all__.sidebar2 = sidebar2;
			__all__.sidebar3 = sidebar3;
		__pragma__ ('</all>')
	}) ();
   return __all__;
}
window ['personalizador'] = personalizador ();
