contenedor=True
modelos=["main","galerias","shortcodes"]
shortcodes=["base_url","base_url_full","galeria","base_route","slider"]
widgets=["galeria","slider"]
name="sc"
widgets_folder="widgets/"
shortcodes_folder="shortcodes/"
navegacion=[['ShortCodes', 
			'listar',  
			[['Todos los shortcodes', ['listar', {'titulo': 'Estudiantes', 'valor': ["Plugin",name,'Shortcodes']}, None]], 
			 ['crear shortcode', ['editar', {'titulo': 'Nuevo Shortcode', 'valor': ["Plugin",name,'Shortcode', None]}, None]],
			 ['Galerias', ['listar', {'titulo': 'Nuevo Shortcode', 'valor': ["Plugin",name,'Galerias']}, None]], 
			 ['crear galeria', ['editar', {'titulo': 'Nuevo Shortcode', 'valor': ["Plugin",name,'Galeria', None]}, None]], 
			 ['Sliders', ['listar', {'titulo': 'Nuevo Shortcode', 'valor': ["Plugin",name,'Sliders']}, None]], 
			 ['crear slider', ['editar', {'titulo': 'Nuevo Shortcode', 'valor': ["Plugin",name,'Slider', None]}, None]], 
			 ], 
			 '001-symbol.png',
			]]

__path__=__file__[:__file__.rfind("/")+1]

