"use strict";
// Transcrypt'ed from Python, 2018-01-22 21:48:23
function nuclear () {
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
		'math', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'math';
					__pragma__ ('<all>')
						__all__.__name__ = __name__;
					__pragma__ ('</all>')
				}
			}
		}
	);
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
	__nest__ (
		__all__,
		'zu', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var math = {};
					var __name__ = 'zu';
					__nest__ (math, '', __init__ (__world__.math));
					var invertString = function (cad) {
						var c = '';
						var __iterable0__ = cad;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							var c = elem + c;
						}
						return c;
					};
					var randomString = function (lon, alp, noalp, num) {
						if (typeof lon == 'undefined' || (lon != null && lon .hasOwnProperty ("__kwargtrans__"))) {;
							var lon = 8;
						};
						if (typeof alp == 'undefined' || (alp != null && alp .hasOwnProperty ("__kwargtrans__"))) {;
							var alp = true;
						};
						if (typeof noalp == 'undefined' || (noalp != null && noalp .hasOwnProperty ("__kwargtrans__"))) {;
							var noalp = true;
						};
						if (typeof num == 'undefined' || (num != null && num .hasOwnProperty ("__kwargtrans__"))) {;
							var num = true;
						};
						var v_num = '0123456789';
						var v_alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
						var v_noalp = '.-!$()|@{[]}~>';
						if (alp == true && noalp == true && num == true) {
							var v = (v_num + v_alp) + v_noalp;
						}
						else if (alp == true && noalp == false && num == true) {
							var v = v_num + v_alp;
						}
						else if (alp == false && noalp == true && num == true) {
							var v = v_num + v_noalp;
						}
						else if (alp == true && noalp == true && num == false) {
							var v = v_alp + v_noalp;
						}
						else if (alp == false && noalp == false && num == true) {
							var v = v_num;
						}
						else if (alp == true && noalp == false && num == false) {
							var v = v_alp;
						}
						else if (alp == false && noalp == true && num == false) {
							var v = v_noalp;
						}
						else {
							return null;
						}
						var c = 0;
						var token = '';
						while (c < lon) {
							token += v [random.randrange (0, len (v))];
							c++;
						}
						return token;
					};
					var cmpString = function (cad1, cad2, orden, mayor) {
						if (typeof orden == 'undefined' || (orden != null && orden .hasOwnProperty ("__kwargtrans__"))) {;
							var orden = '1a.';
						};
						if (typeof mayor == 'undefined' || (mayor != null && mayor .hasOwnProperty ("__kwargtrans__"))) {;
							var mayor = true;
						};
						var c = (mayor == true ? 'aáàäbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzçḉ' : invertString ('aáàäbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzçḉ'));
						var c1 = c + c.upper ();
						var c2 = (mayor == true ? '0123456789' : invertString ('0123456789'));
						var c3 = (mayor == true ? ",;.·:_+-*/^%=&~@#|()[]{}¡!¿?<>«»ºª¬'‘´`¨“”€ł¶ŧ←↓→øþæßðđŋħł¢µΩŁ¢®Ŧ¥↑ıØÞÆ§ÐªŊĦŁ©" : invertString (",;.·:_+-*/^%=&~@#|()[]{}¡!¿?<>«»ºª¬'‘´`¨“”€ł¶ŧ←↓→øþæßðđŋħł¢µΩŁ¢®Ŧ¥↑ıØÞÆ§ÐªŊĦŁ©"));
						var rango = (len (cad1) <= len (cad2) ? len (cad1) : len (cad2));
						if (orden == '1a.') {
							var cadena = (c2 + c1) + c3;
						}
						else if (orden == '.a1') {
							var cadena = (c3 + c1) + c2;
						}
						else if (orden == '1.a') {
							var cadena = (c2 + c3) + c1;
						}
						else if (orden == 'a.1') {
							var cadena = (c1 + c3) + c2;
						}
						else if (orden == 'a1.') {
							var cadena = (c1 + c2) + c3;
						}
						else if (orden == '.1a') {
							var cadena = (c3 + c2) + c1;
						}
						for (var x = 0; x < rango; x++) {
							if (cadena.find (cad1 [x]) > cadena.find (cad2 [x])) {
								return true;
							}
							else if (cadena.find (cad1 [x]) < cadena.find (cad2 [x])) {
								return false;
							}
						}
						return null;
					};
					var ordenLargString = function (l, mayor, largo, orden) {
						if (typeof mayor == 'undefined' || (mayor != null && mayor .hasOwnProperty ("__kwargtrans__"))) {;
							var mayor = true;
						};
						if (typeof largo == 'undefined' || (largo != null && largo .hasOwnProperty ("__kwargtrans__"))) {;
							var largo = true;
						};
						if (typeof orden == 'undefined' || (orden != null && orden .hasOwnProperty ("__kwargtrans__"))) {;
							var orden = '1a.';
						};
						var nl = list ([]);
						var c = 0;
						var pos = 0;
						while (c < len (l)) {
							var cad = l [c];
							var c2 = 0;
							var pos = 0;
							while (c2 <= len (nl) - 1) {
								if (largo == true) {
									if (len (nl [c2]) > len (cad)) {
										pos++;
									}
									else if (len (nl [c2]) == len (cad)) {
										if (!(cmpString (nl [c2], cad, __kwargtrans__ ({mayor: mayor, orden: orden})))) {
											pos++;
										}
										else {
											// pass;
										}
									}
								}
								else if (len (nl [c2]) < len (cad)) {
									pos++;
								}
								else if (len (nl [c2]) == len (cad)) {
									if (cmpString (nl [c2], cad, __kwargtrans__ ({mayor: mayor, orden: orden}))) {
										// pass;
									}
									else {
										pos++;
									}
								}
								c2++;
							}
							nl.insert (pos, cad);
							c++;
						}
						return nl;
					};
					var getTab = function (linea) {
						var c = 0;
						var cadena = '';
						while (c < len (linea)) {
							if (linea [c] == '\t' || linea [c] == '\r' || linea [c] == ' ') {
								cadena += linea [c];
							}
							else {
								return cadena;
							}
							c++;
						}
						return cadena;
					};
					var siguienteNivel = function (codigo, funcion) {
						if (typeof funcion == 'undefined' || (funcion != null && funcion .hasOwnProperty ("__kwargtrans__"))) {;
							var funcion = null;
						};
						var cadena = '';
						var cadena2 = '';
						var c = 0;
						var tab = len (getTab (codigo [c]));
						while (c < len (codigo)) {
							if (len (getTab (codigo [c])) > tab) {
								cadena += codigo [c] + '\n';
							}
							else if (len (getTab (codigo [c])) == tab) {
								cadena2 += codigo [c] + '\n';
							}
							c++;
						}
						if (funcion != null) {
							return funcion (cadena.__getslice__ (0, -(1), 1).py_split ('\n')) + cadena2;
						}
						else {
							return cadena.__getslice__ (0, -(1), 1) + cadena2;
						}
					};
					var finIndex = function (cadena, busca) {
						return (cadena.index (busca) + len (busca)) - 1;
					};
					var compilarLambda = function (codigo) {
						var c = 0;
						var abierto = false;
						var tabulacion = 0;
						var cadena = '';
						var cadena2 = '';
						var punteros = list ([]);
						while (c < len (codigo) - 1) {
							if (__in__ ('lambda ', codigo [c]) && __in__ ('=', codigo [c]) && __in__ (':', codigo [c]) && abierto == false) {
								var abierto = true;
								var cadena = siguienteNivel (codigo.__getslice__ (c + 1, null, 1), compilarLambda);
								var f = finIndex (codigo [c], 'lambda') + 1;
								var parametros = codigo [c].__getslice__ (f, codigo [c].index (':'), 1);
								var cparametros = '';
								var __iterable0__ = parametros.py_split (',');
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									cparametros += ((elem + '=') + elem) + ',';
								}
								cadena2 += ((((codigo [c] + 'zlambda(') + cparametros.__getslice__ (0, -(1), 1)) + ",__codigo__='''") + cadena.__getslice__ (0, -(1), 1)) + "''')\n";
								c += len (cadena.py_split ('\n')) - 1;
							}
							else {
								cadena2 += codigo [c] + '\n';
							}
							c++;
						}
						return cadena2;
					};
					var remplazarFueraString = function (cadena, viejo, nuevo) {
						var inicio = 0;
						var fin = 0;
						var abierto = false;
						var abridor = null;
						while (fin < len (cadena) - 1) {
							if (cadena [fin] == "'" || cadena [fin] == '"') {
								if (abierto == false) {
									var abierto = true;
									var abridor = cadena [fin];
									var cadena = (cadena.__getslice__ (0, inicio, 1) + cadena.__getslice__ (inicio, fin, 1).py_replace (viejo, nuevo)) + cadena.__getslice__ (fin, null, 1);
								}
								else if (abridor == cadena [fin]) {
									var abierto = false;
									var abridor = null;
									var inicio = fin;
								}
							}
							fin++;
						}
						return cadena;
					};
					var ordLargString = function (lista, creciente) {
						if (typeof creciente == 'undefined' || (creciente != null && creciente .hasOwnProperty ("__kwargtrans__"))) {;
							var creciente = true;
						};
						var _lista = lista;
						var lista2 = list ([]);
						var valor = '';
						var valor2 = '';
						var __iterable0__ = _lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (lista2 == list ([])) {
								lista2.append (elem);
							}
							else {
								var __iterable1__ = lista2;
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var elem2 = __iterable1__ [__index1__];
									if (len (elem) > len (elem2)) {
										var valor = elem2;
									}
								}
								lista2.insert (lista2.index (elem), valor);
							}
						}
						return lista2;
					};
					var dimensionar = function (lista) {
						var c = '';
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							c += ('[' + str (elem)) + ']';
						}
						return c;
					};
					var add = function (lista, numero) {
						var l = len (lista);
						var c = 0;
						while (c < l) {
							lista [c] = lista [c] + numero;
							c++;
						}
					};
					var add2 = function (lista, lista2) {
						var l = len (lista);
						var c = 0;
						while (c < l) {
							lista [c] = list ([lista [c] [0] + lista2 [0], lista [c] [1] + lista2 [1]]);
							c++;
						}
					};
					var restar = function (lista, numero) {
						var l = len (lista);
						var c = 0;
						while (c < l) {
							lista [c] = lista [c] - numero;
							c++;
						}
					};
					var mayor = function (lista) {
						var i = 0;
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (py_typeof (elem) == int) {
								if (elem > i) {
									var i = elem;
								}
							}
						}
						return i;
					};
					var ciento = function (valor1, valor2) {
						return (valor1 * valor2) / 100;
					};
					var ciento2 = function (valor1, valor2) {
						return (valor1 * 100) / valor2;
					};
					var diferenciar = function (v1, v2) {
						var l = list ([]);
						var __iterable0__ = v1;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							var __iterable1__ = v2;
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var elem2 = __iterable1__ [__index1__];
								if (elem != elem2) {
									l.append (elem2);
								}
							}
						}
						return l;
					};
					var por = function (v1, v2, f) {
						if (typeof f == 'undefined' || (f != null && f .hasOwnProperty ("__kwargtrans__"))) {;
							var f = 1;
						};
						if (f == 1) {
							var c = 0;
							var d = dict ({});
							var __iterable0__ = v1;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								d [str (elem)] = v2 [c];
								c++;
							}
							return d;
						}
						if (f == 2) {
							var cadena = '';
							var __iterable0__ = v1;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								cadena += str (elem) + ',';
							}
							var cadena = cadena.__getslice__ (0, -(1), 1);
							return cadena;
						}
					};
					var mayor_f = function (lista, f) {
						if (typeof f == 'undefined' || (f != null && f .hasOwnProperty ("__kwargtrans__"))) {;
							var f = 1;
						};
						var lista2 = list ([]);
						var a = 0;
						var m = 0;
						var d = 0;
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							lista2.append (elem.py_split ('/'));
							print (elem.py_split ('/'));
						}
						var __iterable0__ = lista2;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (elem [0] > d) {
								var d = elem [0];
							}
							if (el6em [1] > m) {
								var m = elem [1];
							}
							if (elem [2] > a) {
								var a = elem [2];
							}
						}
						if (f == 1) {
							return list ([d, m, a]);
						}
						if (f == 2) {
							return (((str (d) + '/') + str (m)) + '/') + str (a);
						}
					};
					var u = function (valor, f) {
						if (typeof f == 'undefined' || (f != null && f .hasOwnProperty ("__kwargtrans__"))) {;
							var f = 1;
						};
						if (f == 1) {
							var c = 0;
							var __iterable0__ = valor;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								valor [c] = elem.decode ('utf-8');
								c++;
							}
							return valor;
						}
						if (f == 2) {
							var c = 0;
							var __iterable0__ = valor;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								valor [c] [0] = elem [0].decode ('utf-8');
								c++;
							}
							return valor;
						}
					};
					var u2 = function (valor) {
						return str (valor).py_replace ('\\xc3\\xb3', 'ó').py_replace ('\\xc3\\xba', 'ú').py_replace ('\\xc3\\xad', 'í').py_replace ('\\xc2\\xa1', '!').py_replace ('\\xc3\\xb1', 'ñ');
					};
					var nu2 = function (valor) {
						return str (valor).py_replace ('ó', 'o').py_replace ('ú', 'u').py_replace ('í', 'i').py_replace ('á', 'a').py_replace ('é', 'e');
					};
					var tipo_v = function (tipo) {
						if (tipo == str) {
							return '';
						}
						if (tipo == int) {
							return 0;
						}
						if (tipo == bool) {
							return false;
						}
						if (tipo == null) {
							return null;
						}
						if (tipo == float) {
							return 0.0;
						}
						if (tipo == list) {
							return list ([]);
						}
						if (tipo == tuple) {
							return tuple ([]);
						}
						if (tipo == dict) {
							return dict ({});
						}
					};
					var tipo = function (cadena) {
						var cadena = cadena.py_replace ("<type 'str'>", 'str');
						var cadena = cadena.py_replace ("<type 'int'>", 'int');
						var cadena = cadena.py_replace ("<type 'float'>", 'float');
						var cadena = cadena.py_replace ("<type 'list'>", 'list');
						var cadena = cadena.py_replace ("<type 'tuple'>", 'tuple');
						var cadena = cadena.py_replace ("<type 'None'>", 'None');
						var cadena = cadena.py_replace ("<type 'dict'>", 'dict');
						return cadena;
					};
					var concatenar = function (lista, separador) {
						if (typeof separador == 'undefined' || (separador != null && separador .hasOwnProperty ("__kwargtrans__"))) {;
							var separador = null;
						};
						var i = '';
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (separador != null) {
								i += str (elem) + separador;
							}
							else {
								i += str (elem);
							}
						}
						if (separador != null) {
							return i.__getslice__ (0, -(1), 1);
						}
						else {
							return i;
						}
					};
					var concatenar2 = function (lista) {
						var i = '';
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							i += str (elem) + '\n';
						}
						return i;
					};
					var posicionar = function (pantalla, t_posicion, posicion) {
						// pass;
					};
					var poligono = function (size, pos, radios) {
						print (radios);
						if (len (radios) == 4) {
							var top = arco (radios [0], 'top');
							add2 (top, list ([pos [0], pos [1]]));
							return top.__getslice__ (0, 50, 1);
						}
						else {
							print ('no hay los radios necesarios');
						}
					};
					var rect_radius = function (pos, size, radios, borde, inverso) {
						if (typeof borde == 'undefined' || (borde != null && borde .hasOwnProperty ("__kwargtrans__"))) {;
							var borde = false;
						};
						if (typeof inverso == 'undefined' || (inverso != null && inverso .hasOwnProperty ("__kwargtrans__"))) {;
							var inverso = false;
						};
						var angulo = 0;
						var rect = list ([]);
						var right = list ([]);
						var bottom = list ([]);
						var left = list ([]);
						var top = list ([]);
						while (angulo < 6.4) {
							var sen = math.sin (angulo);
							var cos = math.cos (angulo);
							if (angulo < 1.6) {
								var y = ((sen * radios [2] + pos [1]) + size [1]) - radios [2];
								var x = ((cos * radios [2] + pos [0]) + size [0]) - radios [2];
								bottom.append (tuple ([x, y]));
							}
							if (angulo > 1.6 && angulo < 3.2) {
								var y = ((sen * radios [3] + pos [1]) + size [1]) - radios [3];
								var x = (cos * radios [3] + pos [0]) + radios [3];
								left.append (tuple ([x, y]));
							}
							if (angulo > 3.2 && angulo < 4.8) {
								var y = (sen * radios [0] + pos [1]) + radios [0];
								var x = (cos * radios [0] + pos [0]) + radios [0];
								top.append (tuple ([x, y]));
							}
							if (angulo > 4.8 && angulo < 6.4) {
								var y = (sen * radios [1] + pos [1]) + radios [1];
								var x = ((cos * radios [1] + pos [0]) + size [0]) - radios [1];
								right.append (tuple ([x, y]));
							}
							angulo += 0.01;
						}
						if (borde == false) {
							var rect = ((top + right) + bottom) + left;
						}
						else {
							var rect = list ([top, right, bottom, left]);
						}
						if (inverso == true) {
							top.insert (0, tuple ([0, 0]));
							right.insert (0, tuple ([pos [0] + size [0], pos [1]]));
							bottom.insert (0, tuple ([pos [0] + size [0], pos [1] + size [1]]));
							left.insert (0, tuple ([pos [0], pos [1] + size [1]]));
							var rect = list ([top, right, bottom, left]);
						}
						return rect;
					};
					var css_convert = function (atributo, css) {
						if (__in__ (atributo, css)) {
							if (atributo == 'background' || atributo == 'background-color') {
								return 2;
							}
						}
						else {
							print ('este atributo no existe');
						}
					};
					var rect_radius2 = function (pos, size, radios, borde, inverso) {
						if (typeof borde == 'undefined' || (borde != null && borde .hasOwnProperty ("__kwargtrans__"))) {;
							var borde = false;
						};
						if (typeof inverso == 'undefined' || (inverso != null && inverso .hasOwnProperty ("__kwargtrans__"))) {;
							var inverso = false;
						};
						var angulo = 0;
						var rect = list ([]);
						var right = list ([]);
						var bottom = list ([]);
						var left = list ([]);
						var top = list ([]);
						while (angulo < 6.2) {
							var sen = math.sin (angulo);
							var cos = math.cos (angulo);
							if (angulo < 1.6) {
								var y = ((int (sen * radios [2] [1]) + pos [1]) + size [1]) - radios [2] [1];
								var x = ((int (cos * radios [2] [0]) + pos [0]) + size [0]) - radios [2] [0];
								bottom.append (tuple ([x, y]));
							}
							if (angulo > 1.6 && angulo < 3.2) {
								var y = ((int (sen * radios [3] [1]) + pos [1]) + size [1]) - radios [3] [1];
								var x = ((int (cos * radios [3] [0]) + pos [0]) + radios [3] [0]) - 1;
								left.append (tuple ([x, y]));
							}
							if (angulo > 3.2 && angulo < 4.8) {
								var y = (sen * radios [0] [1] + pos [1]) + radios [0] [1];
								var x = (cos * radios [0] [0] + pos [0]) + radios [0] [0];
								top.append (tuple ([x, y]));
							}
							if (angulo > 4.8 && angulo < 6.2) {
								var y = (sen * radios [1] [1] + pos [1]) + radios [1] [1];
								var x = (((cos * radios [1] [0] + pos [0]) + size [0]) - radios [1] [0]) + 1;
								right.append (tuple ([x, y]));
							}
							angulo += 0.002;
						}
						if (borde == false) {
							var rect = ((top + right) + bottom) + left;
						}
						else {
							var rect = list ([top, right, bottom, left]);
						}
						if (inverso == true) {
							top.insert (0, tuple ([0, 0]));
							right.insert (0, tuple ([pos [0] + size [0], pos [1]]));
							bottom.insert (0, tuple ([pos [0] + size [0], pos [1] + size [1]]));
							left.insert (0, tuple ([pos [0], pos [1] + size [1]]));
							var rect = list ([top, right, bottom, left]);
						}
						return rect;
					};
					var separar = function (cadena) {
						var c = 0;
						var start = 0;
						var l = list ([]);
						while (c < len (cadena)) {
							if (cadena [c] == 'x' || cadena [c] == '%' || cadena.__getslice__ (start, c + 1, 1) == 'bottom' || cadena.__getslice__ (start, c + 1, 1) == 'right' || cadena.__getslice__ (start, c + 1, 1) == 'left' || cadena.__getslice__ (start, c + 1, 1) == 'center' || cadena.__getslice__ (start, c + 1, 1) == 'top' || cadena.__getslice__ (start, c + 1, 1) == 'auto') {
								if (c < len (cadena)) {
									var a = 1;
								}
								else {
									var a = 0;
								}
								l.append (cadena.__getslice__ (start, c + a, 1));
								var start = c + a;
							}
							c++;
						}
						return l;
					};
					var css_posicionamiento = function (objetos) {
						var x = 0;
						var y = 0;
						var __iterable0__ = objetos;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (elem.css.get_style ('position') == 'static') {
								if (elem.css.get_style ('display') == 'inline') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'block') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'inline-block') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'run-in') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'inline-table') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-footer-group') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-column') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'none') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-row-group') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-row') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-cell') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'inherit') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'list-item') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-header-group') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-column') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-caption') {
									// pass;
								}
								if (elem.css.get_style ('display') == 'table-footer-group') {
									// pass;
								}
							}
							if (elem.css.get_style ('position') == 'relative') {
								// pass;
							}
							if (elem.css.get_style ('position') == 'absolute') {
								// pass;
							}
							if (elem.css.get_style ('position') == 'fixed') {
								// pass;
							}
							if (elem.css.get_style ('position') == 'inherit') {
								// pass;
							}
						}
					};
					var listar_d = function (dic, clave) {
						var l = list ([]);
						var elem = dic [clave];
						if (elem != dict ({})) {
							var __iterable0__ = elem;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var i = __iterable0__ [__index0__];
								if (elem [i] != dict ({})) {
									var elemento = elem [i];
									while (elemento != dict ({})) {
										elemento;
									}
								}
							}
						}
					};
					var dicc = __class__ ('dicc', [object], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self) {
							self.l_claves = list ([]);
							self.d = dict ({});
						});},
						get niveles () {return __get__ (this, function (self, clave, orden) {
							var contador = 0;
							if (self.py_get (clave) != null) {
								var ciclo = self.py_get (clave);
								while (ciclo.keys_all () != list ([])) {
									if (len (ciclo.keys_p) >= orden) {
										try {
											var ciclo = ciclo.py_get (ciclo.keys_p [orden]);
											contador++;
										}
										catch (__except0__) {
											break;
										}
									}
								}
							}
							return contador;
						});},
						get mapear () {return __get__ (this, function (self, niveles) {
							if (typeof niveles == 'undefined' || (niveles != null && niveles .hasOwnProperty ("__kwargtrans__"))) {;
								var niveles = 1;
							};
							var dic = self.d;
							if (niveles > 20) {
								var niveles = 20;
							}
							var l = list ([]);
							var base = 'for elem0 in dic:\n try:\n  if dic[elem0].d.keys()!=[]:\n   l.append([elem0])\n   pass\n  else:\n   l.append([elem0])\n except:\n  l.append([elem0])';
							var base2 = base;
							var codigo = base;
							var lista = 'l.append([elem0])';
							for (var elem = 0; elem < niveles; elem++) {
								if (elem != 0) {
									var base2 = base2.py_replace ('dic[elem0].d', 'dic' + diccionar_elem ('elem', elem + 1, '.d'));
									var base2 = base2.py_replace ('dic:', ('dic' + diccionar_elem ('elem', elem, '.d')) + ':');
									var base2 = base2.py_replace ('for elem0', 'for elem' + str (elem));
									var base2 = base2.py_replace (lista, lista.py_replace ('[elem0]', listar_elem ('elem', elem + 1)));
									var base2 = tabular (base2, get_tab2 (codigo, 'pass'));
									var l_codigo = codigo.py_split ('\n');
									var __iterable0__ = l_codigo;
									for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
										var elem2 = __iterable0__ [__index0__];
										if (__in__ ('pass', elem2)) {
											l_codigo [l_codigo.index (elem2)] = base2;
										}
									}
									var codigo = concatenar2 (l_codigo);
									var base2 = base;
								}
							}
							var f = open ('/home/abraham/prueba.txt', 'w');
							f.write (codigo);
							f.close ();
							exec (codigo);
							return l;
						});},
						get get_keys () {return __get__ (this, function (self, valor) {
							var __iterable0__ = self.keys_p ();
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (self.d [elem] == valor) {
									return self.py_keys (elem);
								}
								else {
									print ('ese valor no se encuentra en el diccionario Z');
									return null;
								}
							}
						});},
						get py_get () {return __get__ (this, function (self, clave) {
							var indice = 0;
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (clave, elem)) {
									var indice = self.l_claves.index (elem);
									return self.d [self.l_claves [indice] [0]];
								}
							}
							if (!(__in__ (clave, elem))) {
								print ('la clave no existe');
								return null;
							}
						});},
						get set () {return __get__ (this, function (self, valor) {
							var claves = tuple ([].slice.apply (arguments).slice (2));
							var claves = list (claves);
							var __iterable0__ = claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (elem, self.keys_all ())) {
									claves.remove (elem);
								}
							}
							if (claves != list ([])) {
								self.l_claves.append (claves);
								self.d [claves [0]] = valor;
							}
							else {
								print ('las claves ya estaban agragadas anteriormente');
							}
						});},
						get set2 () {return __get__ (this, function (self, valor, claves) {
							var claves2 = list (claves);
							var __iterable0__ = claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (elem, self.keys_all ())) {
									claves2.remove (elem);
								}
							}
							if (claves != list ([])) {
								self.l_claves.append (claves2);
								self.d [claves2 [0]] = valor;
							}
							else {
								print ('las claves ya estaban agragadas anteriormente');
							}
						});},
						get key2 () {return __get__ (this, function (self, clave, lista) {
							var claves = self.py_keys (clave);
							var indice = self.l_claves.index (claves);
							var __iterable0__ = lista;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (!(__in__ (elem, self.l_claves [indice])) && !(__in__ (elem, self.keys_all ()))) {
									self.l_claves [indice].append (elem);
								}
							}
						});},
						get key () {return __get__ (this, function (self, clave1, clave2) {
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var indice = self.l_claves.index (elem);
								self.l_claves [indice] = list (self.l_claves [indice]);
								if (__in__ (clave1, self.l_claves [indice]) && !(__in__ (clave2, self.keys_all ()))) {
									self.l_claves [indice].append (clave2);
								}
							}
						});},
						get py_keys () {return __get__ (this, function (self, clave) {
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (clave, elem)) {
									var indice = self.l_claves.index (elem);
								}
							}
							return self.l_claves [indice];
						});},
						get keys_p () {return __get__ (this, function (self) {
							return self.d.py_keys ();
						});},
						get keys_p2 () {return __get__ (this, function (self, clave) {
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								if (__in__ (clave, elem)) {
									return elem [0];
								}
							}
						});},
						get keys_all () {return __get__ (this, function (self) {
							var l = list ([]);
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								var __iterable1__ = elem;
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var elem2 = __iterable1__ [__index1__];
									l.append (elem2);
								}
							}
							return l;
						});},
						get fusionar () {return __get__ (this, function (self, dic, sobrescribir) {
							if (typeof sobrescribir == 'undefined' || (sobrescribir != null && sobrescribir .hasOwnProperty ("__kwargtrans__"))) {;
								var sobrescribir = false;
							};
							var __iterable0__ = dic.keys_p ();
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								self.set2 (dic.py_get (elem), dic.py_keys (elem));
							}
						});},
						get show () {return __get__ (this, function (self) {
							print ('<');
							var __iterable0__ = self.l_claves;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								print (elem, ':', self.d [elem [0]]);
							}
							print ('>');
						});}
					});
					var get_tab = function (cadena, palabra) {
						var l = cadena.py_split ('\n');
						var columna = '';
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (palabra, elem)) {
								var columna = elem;
							}
						}
						var x1 = 0;
						var x2 = 1;
						while (columna.__getslice__ (x1, x2, 1) == ' ' || columna.__getslice__ (x1, x2, 1) == '\t') {
							x1++;
							x2++;
						}
						return x1;
					};
					var get_tab2 = function (cadena, palabra) {
						var l = cadena.py_split ('\n');
						var columna = '';
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (palabra, elem)) {
								var columna = elem;
							}
						}
						var x1 = 0;
						var x2 = 1;
						while (columna.__getslice__ (x1, x2, 1) == ' ' || columna.__getslice__ (x1, x2, 1) == '\t') {
							x1++;
							x2++;
						}
						return columna.__getslice__ (0, x1, 1);
					};
					var tabular = function (cadena, tabs) {
						var l = cadena.py_split ('\n');
						if (py_typeof (tabs) == str) {
							var __iterable0__ = l;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								l [l.index (elem)] = tabs + elem;
							}
						}
						if (py_typeof (tabs) == int) {
							var __iterable0__ = l;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								l [l.index (elem)] = ' ' * tabs + elem;
							}
						}
						var cadena = '';
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							cadena += elem + '\n';
						}
						return cadena;
					};
					var listar_elem = function (palabra, numero) {
						var l = list ([]);
						for (var elem = 0; elem < numero; elem++) {
							l.append (palabra + str (elem));
						}
						return str (l).py_replace ("'", '');
					};
					var diccionar_elem = function (palabra, numero, medio, retorno) {
						if (typeof medio == 'undefined' || (medio != null && medio .hasOwnProperty ("__kwargtrans__"))) {;
							var medio = '';
						};
						if (typeof retorno == 'undefined' || (retorno != null && retorno .hasOwnProperty ("__kwargtrans__"))) {;
							var retorno = 0;
						};
						var l = list ([]);
						var cadena = '';
						for (var elem = 0; elem < numero; elem++) {
							l.append (palabra + str (elem));
						}
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							cadena += (('[' + elem) + ']') + medio;
						}
						if (retorno > 0) {
							return cadena.__getslice__ (0, -(retorno), 1);
						}
						else if (retorno < 0) {
							return cadena.__getslice__ (0, retorno, 1);
						}
						else if (retorno == 0) {
							return cadena;
						}
					};
					var mapear = function (dic, niveles, mapeo) {
						if (typeof niveles == 'undefined' || (niveles != null && niveles .hasOwnProperty ("__kwargtrans__"))) {;
							var niveles = 1;
						};
						if (typeof mapeo == 'undefined' || (mapeo != null && mapeo .hasOwnProperty ("__kwargtrans__"))) {;
							var mapeo = 'claves';
						};
						if (niveles > 20) {
							var niveles = 20;
						}
						var l = list ([]);
						var base = 'for elem0 in dic:\n if type(dic[elem0])==dict:\n  if dic[elem0].keys()!=[]:\n   l.append([elem0])\n   pass\n  else:\n   l.append([elem0])\n else:\n  l.append([elemento])';
						var base2 = base;
						var codigo = base;
						var lista = 'l.append([elem0])';
						for (var elem = 0; elem < niveles; elem++) {
							if (elem != 0) {
								var base2 = base2.py_replace ('dic[elem0]', 'dic' + diccionar_elem ('elem', elem + 1));
								var base2 = base2.py_replace ('dic:', ('dic' + diccionar_elem ('elem', elem)) + ':');
								var base2 = base2.py_replace ('for elem0', 'for elem' + str (elem));
								var base2 = base2.py_replace (lista, lista.py_replace ('[elem0]', listar_elem ('elem', elem + 1)));
								if (mapeo == 'claves') {
									var base2 = base2.py_replace ('([elemento])', ('([' + listar_elem ('elem', elem + 1)) + '])');
								}
								if (mapeo == 'valores') {
									var base2 = base2.py_replace ('([elemento])', ((('(' + listar_elem ('elem', elem + 1).__getslice__ (0, -(1), 1)) + ',dic') + diccionar_elem ('elem', elem + 1)) + '])');
								}
								var base2 = tabular (base2, get_tab2 (codigo, 'pass'));
								var l_codigo = codigo.py_split ('\n');
								var __iterable0__ = l_codigo;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem2 = __iterable0__ [__index0__];
									if (__in__ ('pass', elem2)) {
										l_codigo [l_codigo.index (elem2)] = base2;
									}
								}
								var codigo = concatenar2 (l_codigo);
								var base2 = base;
							}
						}
						exec (codigo);
						return l;
					};
					var buscar_ruta = function (dic, palabra, niveles, todo, mapeo) {
						if (typeof niveles == 'undefined' || (niveles != null && niveles .hasOwnProperty ("__kwargtrans__"))) {;
							var niveles = 1;
						};
						if (typeof todo == 'undefined' || (todo != null && todo .hasOwnProperty ("__kwargtrans__"))) {;
							var todo = 'todo';
						};
						if (typeof mapeo == 'undefined' || (mapeo != null && mapeo .hasOwnProperty ("__kwargtrans__"))) {;
							var mapeo = 'claves';
						};
						var l = mapear (dic, niveles, mapeo);
						var l_temp = list ([]);
						var l_remover = list ([]);
						var __iterable0__ = l;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (elem.count (palabra) >= 1) {
								l_temp.append (elem);
							}
						}
						if (mapeo == 'calves') {
							if (todo == 'solo') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 1] != palabra) {
										l_remover.append (elem);
									}
								}
								var __iterable0__ = l_remover;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									l_temp.remove (elem);
								}
							}
							if (todo == 'claves ruta') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 2] != palabra) {
										l_remover.append (elem);
									}
								}
								var __iterable0__ = l_remover;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									l_temp.remove (elem);
								}
							}
							if (todo == 'claves') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 1] != palabra && elem [len (elem) - 2] == palabra) {
										l_remover.append (elem [len (elem) - 1]);
									}
								}
								var l_temp = l_remover;
							}
							if (todo == 'padre') {
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									var l_temp = list ([]);
									if (__in__ (palabra, elem)) {
										var indice = elem.index (palabra);
										if (indice > 0) {
											l_temp.append (elem [indice - 1]);
										}
									}
								}
							}
						}
						if (mapeo == 'valores') {
							if (todo == 'solo') {
								var l2 = list ([]);
								var __iterable0__ = l_temp;
								for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
									var elem = __iterable0__ [__index0__];
									if (elem [len (elem) - 1] == palabra) {
										l2.append (elem);
									}
								}
								var l_temp = l2;
							}
						}
						return l_temp;
					};
					var unir_key_map = function (lista) {
						var l = list ([]);
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (len (elem) > 0) {
								l.append (elem [1]);
							}
							else {
								l.append (elem [0]);
							}
						}
						return l;
					};
					var estaEn = function (lista, cadena) {
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (elem, lista)) {
								return true;
							}
						}
						return false;
					};
					var movPosList = function (l, posActual, nuevaPos) {
						var lista = l;
						var elem = lista [posActual];
						delete lista [posActual];
						lista.insert (nuevaPos, elem);
						return lista;
					};
					var movPosStr = function (cadena, posActual, nuevaPos) {
						var espacio = '';
						var palabra = '';
						var espacios = list ([]);
						var palabras = list ([]);
						var c = 0;
						var primero = null;
						while (c < len (cadena)) {
							if (cadena [c] == ' ' || cadena [c] == '\n' || cadena [c] == '\t') {
								espacio += cadena [c];
								if (primero == null) {
									var primero = true;
								}
							}
							else if (espacio != '') {
								espacios.append (espacio);
								var espacio = '';
							}
							if (cadena [c] != ' ' && cadena [c] != '\n' && cadena [c] != '\t') {
								palabra += cadena [c];
								if (primero == null) {
									var primero = false;
								}
							}
							else {
								palabras.append (palabra);
								var palabra = '';
							}
							print ('cadena: ', list ([cadena [c]]));
							print (palabra);
							print (espacio);
							c++;
						}
						if (palabra != '') {
							palabras.append (palabra);
						}
						if (espacio != '') {
							espacios.append (espacio);
						}
						var palabras = movPosList (palabras, posActual, nuevaPos);
						print (palabras);
						var cadena = '';
						if (primero == true) {
							var c = 0;
							while (c < len (espacios)) {
								cadena += espacios [c];
								if (c < len (palabra)) {
									cadena += palabras [c];
								}
								c++;
							}
						}
						else if (primero == false) {
							var c = 0;
							while (c < len (palabras)) {
								cadena += palabras [c];
								if (c < len (espacios)) {
									cadena += espacios [c];
								}
								c++;
							}
						}
						return cadena;
					};
					var haveFolder = function (path) {
						var __iterable0__ = os.listdir (path);
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (os.isdir ((path + '/') + elem)) {
								return true;
							}
						}
						return false;
					};
					var rstr = function (cadena, sub, vez) {
						var cadena2 = '';
						var c = len (cadena) - 1;
						while (c >= 0) {
							var cadena2 = cadena [c] + cadena2;
							if (cadena2.count ('/') == vez) {
								return cadena2;
							}
							c--;
						}
					};
					var reKeyIn = function (patron, lista) {
						if (!__in__ ('*', patron)) {
							if (__in__ ('[', patron)) {
								// pass;
							}
						}
					};
					var getPattern = function (lista) {
						var exp1 = list ([]);
						var similitudes = list ([]);
						var previo = null;
						var iguallong = true;
						var temp = null;
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (temp == null) {
								var temp = len (elem);
							}
							else if (len (elem) != temp) {
								var iguallong = false;
							}
						}
						var __iterable0__ = lista;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (previo != null) {
								var __iterable1__ = enumerate (previo);
								for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
									var __left0__ = __iterable1__ [__index1__];
									var k = __left0__ [0];
									var ch = __left0__ [1];
									if (ch == elem [k]) {
										if (similitudes == list ([])) {
											similitudes.append (elem [k]);
										}
										else {
											similitudes [-(1)] += elem [k];
										}
									}
									else if (k + 2 < len (previo)) {
										var temp = '';
										var __iterable2__ = enumerate (previo);
										for (var __index2__ = 0; __index2__ < len (__iterable2__); __index2__++) {
											var __left0__ = __iterable2__ [__index2__];
											var k2 = __left0__ [0];
											var ch2 = __left0__ [1];
											if (ch2 != elem [k2]) {
												temp += elem [k2];
											}
											else {
												if (!__in__ (elem.__getslice__ (k, null, 1), exp1)) {
													exp1.append (temp);
												}
												break;
											}
										}
									}
									else {
										if (!__in__ (elem.__getslice__ (k, null, 1), exp1)) {
											exp1.append (elem.__getslice__ (k, null, 1));
										}
										break;
									}
								}
							}
							else {
								var previo = elem;
							}
						}
					};
					var iterRelacionado = function () {
					};
					var filtrar_datos_planos = function (data) {
						if (py_typeof (data) == dict) {
							var d = dict ({});
							var __iterable0__ = data;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								d [elem] = filtrar_datos_planos (data [elem]);
							}
							return d;
						}
						else if (py_typeof (data) == list || py_typeof (data) == tuple) {
							var l = list ([]);
							var __iterable0__ = data;
							for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
								var elem = __iterable0__ [__index0__];
								l.append (filtrar_datos_planos (elem));
							}
							return l;
						}
						else if (py_typeof (data) == int || py_typeof (data) == float || py_typeof (data) == str || py_typeof (data) == bool) {
							return data;
						}
					};
					var filtrar_del_dict = function (diccionario, py_keys) {
						var d = dict ({});
						var __iterable0__ = py_keys;
						for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
							var elem = __iterable0__ [__index0__];
							if (__in__ (elem, diccionario)) {
								d [elem] = diccionario [elem];
							}
						}
						return d;
					};
					__pragma__ ('<use>' +
						'math' +
					'</use>')
					__pragma__ ('<all>')
						__all__.__name__ = __name__;
						__all__.add = add;
						__all__.add2 = add2;
						__all__.buscar_ruta = buscar_ruta;
						__all__.ciento = ciento;
						__all__.ciento2 = ciento2;
						__all__.cmpString = cmpString;
						__all__.compilarLambda = compilarLambda;
						__all__.concatenar = concatenar;
						__all__.concatenar2 = concatenar2;
						__all__.css_convert = css_convert;
						__all__.css_posicionamiento = css_posicionamiento;
						__all__.dicc = dicc;
						__all__.diccionar_elem = diccionar_elem;
						__all__.diferenciar = diferenciar;
						__all__.dimensionar = dimensionar;
						__all__.estaEn = estaEn;
						__all__.filtrar_datos_planos = filtrar_datos_planos;
						__all__.filtrar_del_dict = filtrar_del_dict;
						__all__.finIndex = finIndex;
						__all__.getPattern = getPattern;
						__all__.getTab = getTab;
						__all__.get_tab = get_tab;
						__all__.get_tab2 = get_tab2;
						__all__.haveFolder = haveFolder;
						__all__.invertString = invertString;
						__all__.iterRelacionado = iterRelacionado;
						__all__.listar_d = listar_d;
						__all__.listar_elem = listar_elem;
						__all__.mapear = mapear;
						__all__.mayor = mayor;
						__all__.mayor_f = mayor_f;
						__all__.movPosList = movPosList;
						__all__.movPosStr = movPosStr;
						__all__.nu2 = nu2;
						__all__.ordLargString = ordLargString;
						__all__.ordenLargString = ordenLargString;
						__all__.poligono = poligono;
						__all__.por = por;
						__all__.posicionar = posicionar;
						__all__.randomString = randomString;
						__all__.reKeyIn = reKeyIn;
						__all__.rect_radius = rect_radius;
						__all__.rect_radius2 = rect_radius2;
						__all__.remplazarFueraString = remplazarFueraString;
						__all__.restar = restar;
						__all__.rstr = rstr;
						__all__.separar = separar;
						__all__.siguienteNivel = siguienteNivel;
						__all__.tabular = tabular;
						__all__.tipo = tipo;
						__all__.tipo_v = tipo_v;
						__all__.u = u;
						__all__.u2 = u2;
						__all__.unir_key_map = unir_key_map;
					__pragma__ ('</all>')
				}
			}
		}
	);
	(function () {
		var re = {};
		var __name__ = '__main__';
		__nest__ (re, '', __init__ (__world__.re));
		var list = py_datos.list;
		var py_metatype = py_datos.py_metatype;
		var thumbail = function (img, sufijo) {
			if (typeof sufijo == 'undefined' || (sufijo != null && sufijo .hasOwnProperty ("__kwargtrans__"))) {;
				var sufijo = '_540x540';
			};
			return (img.__getslice__ (0, img.rfind ('.'), 1) + sufijo) + img.__getslice__ (img.rfind ('.'), null, 1);
		};
		var defaultValues = function () {
			return list ([list ([null]), list ([])]);
		};
		var defaultEvents = function () {
			var eventos = list ([list ([list (['click', list ([])]), list (['mouseenter', list ([])]), list (['mouseleave', list ([])]), list (['mouseover', list ([])]), list (['mouseout', list ([])]), list (['mousemove', list ([])]), list (['mousedown', list ([])]), list (['mouseup', list ([])]), list (['dblclick', list ([])]), list (['keypress', list ([])]), list (['keydonw', list ([])]), list (['keyup', list ([])]), list (['input', list ([])]), list (['blur', list ([])]), list (['focus', list ([])]), list (['drag', list ([])]), list (['dragend', list ([])]), list (['dragenter', list ([])]), list (['dragleave', list ([])]), list (['dragover', list ([])]), list (['dragstart', list ([])]), list (['drop', list ([])])]), list ([])]);
			return eventos;
		};
		var getEvents = function (elemento) {
			var hijos = list ([]);
			var lista = list ([]);
			var eventos = list (['click', 'mouseenter', 'mouseleave', 'mouseover', 'mouseout', 'mousemove', 'mousedown', 'mouseup', 'dblclick', 'keypress', 'keydonw', 'keyup', 'input', 'blur', 'focus', 'drag', 'dragend', 'dragenter', 'dragleave', 'dragover', 'dragstart', 'drop']);
			if (len (elemento.children) > 0) {
				var __iterable0__ = elemento.children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					hijos += list ([getEvents (elem)]);
				}
			}
			var __iterable0__ = eventos;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				lista += list ([list ([elem, elemento.events (elem)])]);
			}
			return list ([lista, hijos]);
		};
		var getValues = function (elemento) {
			if (__in__ ('value', dir (elemento))) {
				var lista = list ([elemento.value]);
			}
			else {
				var lista = list ([null]);
			}
			var hijos = list ([]);
			if (len (elemento.children) > 0) {
				var __iterable0__ = elemento.children;
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var elem = __iterable0__ [__index0__];
					hijos += list ([getValues (elem)]);
				}
			}
			return list ([lista, hijos]);
		};
		var updateEvent = function (listaEvent, padre) {
			if (py_typeof (listaEvent [0] [0]) == str) {
				var eventos = listaEvent [0] [0];
				var __iterable0__ = enumerate (eventos);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var eventolist = __left0__ [1];
					if (len (eventolist) > 0) {
						if (eventolist != null && py_typeof (eventolist) == list && py_typeof (eventolist [0]) == str) {
							var __iterable1__ = eventolist [1];
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var funcion = __iterable1__ [__index1__];
								padre.bind (eventolist [0], funcion);
							}
						}
					}
				}
			}
			else {
				var eventos = listaEvent [0];
				var __iterable0__ = enumerate (eventos);
				for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
					var __left0__ = __iterable0__ [__index0__];
					var k = __left0__ [0];
					var eventolist = __left0__ [1];
					if (len (eventolist) > 0) {
						if (eventolist != null && py_typeof (eventolist) == list) {
							var __iterable1__ = eventolist [1];
							for (var __index1__ = 0; __index1__ < len (__iterable1__); __index1__++) {
								var funcion = __iterable1__ [__index1__];
								padre.bind (eventolist [0], funcion);
							}
						}
					}
				}
			}
			var hijos = listaEvent [1];
			var c = 0;
			var __iterable0__ = enumerate (hijos);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var hijo = __left0__ [1];
				if (hijo != null && len (padre.children) > 0) {
					updateEvent (hijo, padre.children [k]);
				}
			}
		};
		var updateValues = function (listaValues, padre) {
			var py_values = listaValues [0];
			var hijos = listaValues [1];
			var __iterable0__ = enumerate (py_values);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var valor = __left0__ [1];
				if (valor != null) {
					padre.value = valor;
				}
			}
			var __iterable0__ = enumerate (hijos);
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var __left0__ = __iterable0__ [__index0__];
				var k = __left0__ [0];
				var hijo = __left0__ [1];
				if (hijo != null) {
					updateValues (hijo, padre.children [k]);
				}
			}
		};
		var zjoin = function (lista, sep) {
			var c = '';
			var __iterable0__ = lista;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				c += str (elem) + sep;
			}
			return c.__getslice__ (0, -(1), 1);
		};
		var normalizar = function (v) {
			var decode = Codificador.Codificador.decode;
			var dicccionar = function (json) {
				var l = list ([]);
				if (json != null) {
					var __iterable0__ = enumerate (Object.keys(json)
					);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						l.append (list ([elem, (py_typeof (json [elem]) != dict && py_typeof (json [elem]) != object ? json [elem] : dicccionar (json [elem]))]));
					}
				}
				return dict (l);
			};
			if (py_typeof (v) == str && !__in__ (v, list (__globals__ (__all__)))) {
				if (!__in__ (';', v)) {
					try {
						var v = decode (v.strip ());
						if (!__in__ (v, __globals__ (__all__))) {
							window.eval ('False=false;True=true;None=null;a=' + v);
							if (typeof (a) == 'object' && !(v.strip ().startswith ('[')) && !(v.strip ().endswith (']'))) {
								return dicccionar (a);
							}
							else {
								return a;
							}
						}
						else {
							return v;
						}
					}
					catch (__except0__) {
						return v;
					}
				}
				else {
					return v;
				}
			}
			else {
				return v;
			}
		};
		var getCookie = function () {
			var cookies = dict ({});
			var __iterable0__ = document.cookie.py_split (';');
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				if (__in__ ('=', elem)) {
					var __left0__ = elem.py_split ('=');
					var k = __left0__ [0];
					var v = __left0__ [1];
					cookies [k.strip ()] = normalizar (v);
				}
			}
			return cookies;
		};
		var getRest = function () {
			var config = Config.Config ();
			var decode = Codificador.Codificador.decode;
			var url = decode (window.location.href).__getslice__ (len (config.base_url), null, 1).py_split ('#');
			var gato = null;
			if (len (url) == 2) {
				var gato = url [1];
			}
			var url = url [0].py_split ('/');
			if (__in__ ('', url)) {
				url.remove ('');
			}
			var pos = list (['app', 'control', 'metodo', 'args', 'kwargs']);
			var rest = dict ({'app': null, 'control': null, 'metodo': null, 'args': list ([]), 'kwargs': dict ({}), 'action': null, 'manager': false, 'request': dict ({}), '#': null});
			var identificar = function (elem, rest, pos) {
				if (!__in__ ('=', elem) && !__in__ ('{', elem) && !__in__ ('}', elem)) {
					if (len (pos) > 0) {
						if (pos [0] == 'app') {
							if (__in__ (elem, config.apps)) {
								rest ['app'] = normalizar (elem);
							}
							pos.remove ('app');
						}
						else if (pos [0] == 'control') {
							rest ['control'] = normalizar (elem);
							pos.remove ('control');
						}
						else if (pos [0] == 'metodo') {
							rest ['metodo'] = normalizar (elem);
							pos.remove ('metodo');
						}
						else if (pos [0] == 'args') {
							rest ['args'].append (normalizar (elem));
						}
						else if (pos [0] == 'kwargs') {
							pos.remove ('kwargs');
						}
					}
				}
				else if (__in__ ('=', elem)) {
					if (len (pos) > 0) {
						if (pos [0] == 'app') {
							pos.remove ('app');
						}
						else if (pos [0] == 'control') {
							pos.remove ('control');
						}
						else if (pos [0] == 'metodo') {
							pos.remove ('metodo');
						}
						else if (pos [0] == 'args') {
							pos.remove ('args');
						}
						else if (pos [0] == 'kwargs') {
							pos.remove ('kwargs');
						}
					}
					var __iterable0__ = elem.py_split ('&');
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var item = __iterable0__ [__index0__];
						var __left0__ = item.py_split ('=');
						var k = __left0__ [0];
						var v = __left0__ [1];
						rest [k] = normalizar (v);
					}
				}
				else if (__in__ ('{', elem) && __in__ ('}', elem)) {
					if (len (pos) > 0) {
						if (pos [0] == 'app') {
							pos.remove ('app');
						}
						else if (pos [0] == 'control') {
							pos.remove ('control');
						}
						else if (pos [0] == 'metodo') {
							pos.remove ('metodo');
						}
						else if (pos [0] == 'args') {
							pos.remove ('args');
						}
						else if (pos [0] == 'kwargs') {
							pos.remove ('kwargs');
						}
						rest ['kwargs'] = normalizar (elem);
					}
				}
			};
			var __iterable0__ = url;
			for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
				var elem = __iterable0__ [__index0__];
				identificar (elem, rest, pos);
			}
			if (gato != null) {
				rest ['#'] = gato;
			}
			if (rest ['app'] == null) {
				rest ['app'] = config.default_app;
			}
			return rest;
		};
		var Component = __class__ ('Component', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self, url, data, admin, isglobal, offline) {
				if (typeof data == 'undefined' || (data != null && data .hasOwnProperty ("__kwargtrans__"))) {;
					var data = dict ({});
				};
				if (typeof admin == 'undefined' || (admin != null && admin .hasOwnProperty ("__kwargtrans__"))) {;
					var admin = true;
				};
				if (typeof isglobal == 'undefined' || (isglobal != null && isglobal .hasOwnProperty ("__kwargtrans__"))) {;
					var isglobal = true;
				};
				if (typeof offline == 'undefined' || (offline != null && offline .hasOwnProperty ("__kwargtrans__"))) {;
					var offline = false;
				};
				var widget = '';
				var data = str (data);
				self.admin = admin;
				self.isglobal = isglobal;
				if (offline == false) {
					self.py_update (data);
				}
				else {
					if (isglobal) {
						
						          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/global/widgets/'+url+'.html/action=componer/',
						                  
						                  async:false,
						                  
						                  success:  function(respuesta){
						                            widget=respuesta;
						                        },
						                  error : function(objXMLHttpRequest) {
						                    console.log("error1",objXMLHttpRequest);
						                    }
						                  })
						          
					}
					else if (admin) {
						
						          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/admin/widgets/'+url+'.html/action=componer/',
						             
						                  async:false,
						                  
						
						                  success:  function(respuesta){
						                            widget=respuesta;
						                        },
						                  error : function(objXMLHttpRequest) {
						                    console.log("error2",objXMLHttpRequest);
						                    }
						                  })
						          
					}
					else {
						
						          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/user/widgets/'+url+'.html/action=componer/',
						                  
						                  async:false,
						                  
						                  success:  function(respuesta){
						                            widget=respuesta;
						                        },
						                error : function(objXMLHttpRequest) {
						                console.log("error3",objXMLHttpRequest);
						                }
						
						                  })
						                
						          
					}
					var lineas = widget.py_split ('\n');
					var getTab = __init__ (__world__.zu).getTab;
					var AnteriorIdentacion = '';
					var abierta = false;
					var __iterable0__ = enumerate (lineas);
					for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
						var __left0__ = __iterable0__ [__index0__];
						var k = __left0__ [0];
						var elem = __left0__ [1];
						var identacion = getTab (elem);
						if (__in__ ('#', elem)) {
							if (__in__ ('=', elem) && (elem [elem.find ('=') - 1] != '=' && elem [elem.find ('=') - 1] != '<' && elem [elem.find ('=') - 1] != '>' && elem [elem.find ('=') - 1] != '!')) {
								var c = elem.find ('=');
								while (c > 0) {
									if (elem [c] == '\t' || elem [c] == ' ') {
										break;
									}
									c--;
								}
								lineas [k] = (elem.__getslice__ (0, c, 1) + 'var ') + elem.__getslice__ (c, null, 1);
							}
							lineas [k] = lineas [k].py_replace ('#', ';//');
							var elem = lineas [k];
						}
						if (__in__ ('except Exception as e:', elem)) {
							lineas [k] = elem.py_replace ('except Exception as e:', '}catch(e){');
							if (lineas [k].strip ().endswith ('}catch(e){')) {
								var abierta = true;
							}
							else {
								lineas [k] += ';}';
								var elem = lineas [k];
								var abierta = false;
							}
						}
						else if (__in__ ('try:', elem)) {
							lineas [k] = elem.py_replace ('try:', 'try{');
							var elem = lineas [k] + (lineas [k].endswith ('try{') ? '' : ';');
							var abierta = true;
						}
						else if (__in__ ("'''", elem)) {
							lineas [k] = elem.py_replace ("'''", '`');
							var elem = lineas [k] + ';';
						}
						else if (__in__ ('"""', elem)) {
							lineas [k] = elem.py_replace ('"""', '`');
							var elem = lineas [k] + ';';
						}
						else if (__in__ ('elif ', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('elif ', '}else if(').py_replace (':', '){');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('if ', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('if ', 'if(').py_replace (':', '){');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('else', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('else', '}else').py_replace (':', '{');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('=', elem) && (elem [elem.find ('=') - 1] != '+' && elem [elem.find ('=') - 1] != '=' && elem [elem.find ('=') - 1] != '<' && elem [elem.find ('=') - 1] != '>' && elem [elem.find ('=') - 1] != '!' && !__in__ ('//', elem)) && elem [elem.find ('=') + 1] != '=') {
							var c = elem.find ('=') - 1;
							while (c > 0) {
								if (elem [c] == '\t' || elem [c] == ' ') {
									lineas [k] = ((elem.__getslice__ (0, c + 1, 1) + 'var ') + elem.__getslice__ (c + 1, null, 1)) + ';';
									break;
								}
								c--;
							}
						}
						else if (__in__ ('while ', elem) && __in__ (':', elem)) {
							lineas [k] = elem.py_replace ('while ', 'while(').py_replace (':', '){');
							var elem = lineas [k];
						}
						else if (__in__ ('for ', elem) && __in__ (':', elem)) {
							var des = '(\\w+)\\s*(?:,(\\s*\\w+))?';
							var _iter = '((?:\\w+)?(?:\\(?\\[[A-Za-z0-9_,\\-\'"]+?\\]\\)?)?)';
							var patron1 = re.compile (((('for\\s+' + des) + '\\s*in\\s+') + _iter) + ':');
							var descompresion = patron1.findall (lineas [k]) [0];
							var cond2 = '}else{';
							var i = lineas [k].find ('for ');
							print (descompresion);
							if (len (descompresion) > 2 && descompresion [1] != '' && descompresion [1] != null) {
								var f = lineas [k].find (':', lineas [k].find (descompresion [2]));
								var cond1 = ((('if (str(' + descompresion [2]) + ").strip()[0]=='[' && str(") + descompresion [2]) + ").strip().slice(-1)==']'){";
								var iterable = ((((('var ' + descompresion [1]) + '=') + descompresion [2]) + '[') + descompresion [0]) + '][1];';
								var iterable2 = ((((('var ' + descompresion [1]) + '= Object.keys(') + descompresion [2]) + ')[') + descompresion [0]) + '];';
								var bucle = ((((((('for (var ' + descompresion [0]) + ' = 0; ') + descompresion [0]) + ' < Object.keys(') + descompresion [2]) + ').length; ') + descompresion [0]) + '++) {';
								lineas [k] = ((((((lineas [k].__getslice__ (0, i, 1) + bucle) + cond1) + iterable) + cond2) + iterable2) + '}') + lineas [k].__getslice__ (f + 1, null, 1);
							}
							else {
								var f = lineas [k].find (':', lineas [k].find (descompresion [2]));
								var cond1 = ((('if (str(' + descompresion [2]) + ").strip()[0]=='[' && str(") + descompresion [2]) + ").strip().slice(-1)==']'){";
								var bucle = ('for (var _k = 0; _k < Object.keys(' + descompresion [2]) + ').length; _k++){/**/';
								var iterable = ((('var ' + descompresion [0]) + '=') + descompresion [2]) + '[_k];';
								var iterable2 = ((('var ' + descompresion [0]) + '= Object.keys(') + descompresion [2]) + ')[_k];';
								lineas [k] = ((((((lineas [k].__getslice__ (0, i, 1) + bucle) + cond1) + iterable) + cond2) + iterable2) + '}') + lineas [k].__getslice__ (f + 1, null, 1);
							}
						}
						else if (__in__ ('try:', elem)) {
							lineas [k] = elem.py_replace ('try:', 'try{');
							var elem = lineas [k];
							var abierta = true;
						}
						else if (__in__ ('pass', elem)) {
							lineas [k] = elem.py_replace ('pass', '}//pass');
							var elem = lineas [k];
							var abierta = false;
						}
						else if (lineas [k].strip () != '') {
							lineas [k] += ';';
						}
						else if (len (AnteriorIdentacion) > len (identacion) && abierta == true) {
							if (!__in__ ('}', lineas [k])) {
								lineas [k] += '}';
							}
						}
						if (!(lineas [k].strip ().endswith ('{')) && !(lineas [k].strip ().endswith ('}')) && !(lineas [k].strip ().endswith (';')) && lineas [k].strip () != '') {
							lineas [k] += ';';
							var elem = lineas [k];
						}
						if (__in__ (' if ', elem) && __in__ (' else ', elem)) {
							if (elem.find ('=') > elem.find (' if ')) {
								var codigo = elem.__getslice__ (len ('str('), -(1), 1);
								var valor1 = codigo.__getslice__ (0, codigo.find (' if ') - len (' if '), 1);
								var condicion = codigo.__getslice__ (codigo.find (' if '), codigo.find (' else ') - len (' else '), 1);
								var valor2 = codigo.__getslice__ (codigo.find (' else '), null, 1);
								lineas [k] = ((((((variable + 'str(') + condicion) + '?') + valor1) + ':') + valor2) + ');';
							}
							else {
								var variable = elem.__getslice__ (0, elem.find ('str('), 1);
								var codigo = elem.__getslice__ (elem.find ('str(') + len ('str('), null, 1);
								var i = elem.rfind ('(', elem.find (' if '));
								var f = elem.find (')', elem.find (' else '));
								var bloque = elem.__getslice__ (i + 1, f, 1);
								var valor1 = bloque.__getslice__ (0, bloque.find (' if '), 1);
								var condicion = bloque.__getslice__ (bloque.find (' if ') + len (' if '), bloque.find (' else '), 1);
								var valor2 = bloque.__getslice__ (bloque.find (' else ') + len (' else '), null, 1);
								lineas [k] = ((((((variable + 'str((') + condicion) + ')?') + valor1) + ':') + valor2) + ');';
							}
						}
					}
					var widget = '\n'.join (lineas);
					self.widget = widget;
				}
				return widget;
			});},
			get run () {return __get__ (this, function (self, data) {
				if (typeof data == 'undefined' || (data != null && data .hasOwnProperty ("__kwargtrans__"))) {;
					var data = dict ({});
				};
				var doc = '';
				var decode = Codificador.Codificador.decode;
				try {
					eval (self.widget);
				}
				catch (__except0__) {
					print (__except0__);
				}
				return doc;
			});},
			get py_update () {return __get__ (this, function (self, data) {
				if (typeof data == 'undefined' || (data != null && data .hasOwnProperty ("__kwargtrans__"))) {;
					var data = dict ({});
				};
				if (self.isglobal) {
					
					          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/global/widgets/'+self.url+'.html/action=compuesto/'+data,
					                  async:false,
					                  success:  function(respuesta){
					                            self.widget=respuesta;
					                        },
					                  error : function(objXMLHttpRequest) {
					                    console.log("error1",objXMLHttpRequest);
					                    }
					                  })
					          
				}
				else if (self.admin) {
					
					          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/admin/widgets/'+self.url+'.html/action=compuesto/'+data,
					                  async:false,
					                  success:  function(respuesta){
					                            self.widget=respuesta;
					                        },
					                  error : function(objXMLHttpRequest) {
					                    console.log("error2",objXMLHttpRequest);
					                    }
					                  })
					          
				}
				else {
					
					          $.ajax({url:config.base_url+settings.app+'/admin/Show/layout/user/widgets/'+self.url+'.html/action=compuesto/'+data,
					                  async:false,
					                  success:  function(respuesta){
					                            self.widget=respuesta;
					                        },
					                error : function(objXMLHttpRequest) {
					                console.log("error3",objXMLHttpRequest);
					                }
					
					                  })
					          
				}
				return self.widget;
			});}
		});
		var VAR = function (nombre) {
			try {
				return normalizar ($ (("var[name='" + nombre) + "']") [0].innerText);
			}
			catch (__except0__) {
				print ('No se pudo encontrar la varible html: ' + nombre);
				print (__except0__);
			}
		};
		var Settings = __class__ ('Settings', [object], {
			__module__: __name__,
			get __init__ () {return __get__ (this, function (self) {
				var rest = getRest ();
				self.app = rest ['app'];
			});}
		});
		window.settings = Settings ();
		window.rest = getRest ();
		__pragma__ ('<use>' +
			're' +
			'zu' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Component = Component;
			__all__.Settings = Settings;
			__all__.VAR = VAR;
			__all__.__name__ = __name__;
			__all__.defaultEvents = defaultEvents;
			__all__.defaultValues = defaultValues;
			__all__.getCookie = getCookie;
			__all__.getEvents = getEvents;
			__all__.getRest = getRest;
			__all__.getValues = getValues;
			__all__.list = list;
			__all__.normalizar = normalizar;
			__all__.thumbail = thumbail;
			__all__.py_metatype = py_metatype;
			__all__.updateEvent = updateEvent;
			__all__.updateValues = updateValues;
			__all__.zjoin = zjoin;
		__pragma__ ('</all>')
	}) ();
   return __all__;
}
window ['nuclear'] = nuclear ();
