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
