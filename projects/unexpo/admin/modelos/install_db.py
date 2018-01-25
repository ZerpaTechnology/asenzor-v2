db('apps').insertar('unexpo', 
	[
	 [{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, 
	  {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, 
	  {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, 
	  {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 
	  																 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 
	  																 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}
	  																 }
	  }, 
	  {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, 
	  {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 
	  												  'occoa brothers solutions': 'https://occoasolutions.com'}
	  }
	 ], 
	 [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, 
	  {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, 
	  {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, 
	  {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, 
	  {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, 
	  {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}, 
	  {'Publicaciones': 'text', 'name': 'modelo10', 'value': 'publicaciones'}
	 ], 
	 [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, 
	  {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, 
	  {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, 
	  {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, 
	  {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}
	 ]
	], 
	{'app': i}, 
	zu.DateTime(), 
	['Activa'])