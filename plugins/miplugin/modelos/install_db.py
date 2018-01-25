db('Plugins').insertar('miplugin', [
	[{'Titulo': 'text', 'name': 'titulo', 'value': 'pageCreator'}, 
	 {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, 
	 {'value': 'GNU', 'name': 'licencia', 'Licencia': 'text'}, 
	 {'Serial': 'text', 'name': 'serial', 'value': '123456'}, 
	 {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, 
	 {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, 
	 {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, 
	 {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'},
	], 
	[{'Hook del edit': 'text', 'name': 'hook-editar', 'value': '[pageCreator-widget]'},
	]
	], 
	{'Plugin': i}, 
	zu.DateTime(), 
	['Instalado'])