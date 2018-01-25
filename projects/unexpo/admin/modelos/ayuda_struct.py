db=DB()
db('Ayuda').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Ayuda').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Ayuda').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db("Entradas-de-ayuda").campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db("Entradas-de-ayuda").campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db("Entradas-de-ayuda").campo('args',db.dict,False,True,False,False,0,-1,None,None)
db("Entradas-de-ayuda").campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db("Entradas-de-ayuda").campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Ayuda').insertar('Primeros pasos',
					[
						[ {'Nombre': 'text', 'name': 'titulo', 'value': ''},
						  {'Email': 'email', 'name': 'email', 'value': ''},
						  {'Contenido': 'textarea', 'name': 'contenido', 'value': ''},
						]
					], 
					{'Ayuda': 0}, 
					'19/7/2017 16:24:50', 
					[])
db("Entradas-de-ayuda").insertar('Primeros pasos - Resumen', 
					[
						[{'value': 0, 'name': 'id', 'Ayuda': 'hidden-id'},
						 {'Nombre': 'text', 'name': 'titulo', 'value': 'Primeros pasos - Resumen'},
						  {'Contenido': 'textarea', 'name': 'contenido', 'value': ''},
						]
					], 
					{'Entrada-de-ayuda': 0}, 
					'19/7/2017 16:24:50', 
					[])

