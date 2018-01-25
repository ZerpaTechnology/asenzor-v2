contenedor=True
modelos=["main"]
shortcodes=["estilo1"]
widgets=["estilo1"]
name="Portafolio"
widgets_folder="widgets/"
shortcodes_folder="shortcodes/"

navegacion=[['Portafolio', 
			'listar',  
			[['Todas las paginas', ['listar', {'titulo': 'Paginas', 'valor': ["Plugin",name,'Shortcodes']}, None]], 
			 ['crear pagina', ['editar', {'titulo': 'Nueva pagina', 'valor': ["Plugin",name,'Shortcode', None]}, None]],
			 ], 
			 '001-symbol.png',
			]]

__path__=__file__[:__file__.rfind("/")+1]

