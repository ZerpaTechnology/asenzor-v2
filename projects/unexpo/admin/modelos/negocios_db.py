# -*- coding: utf-8 -*-
try:
 from ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Negocios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Negocios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Negocios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Negocios').campo('Fecha',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Categorias').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Categorias').campo('Subcategoria',db.str,False,True,False,False,0,-1,None,None)
db('Categorias').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Imagenes').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Imagenes').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Archivos').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Archivos').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Archivos').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Archivos').campo('Fecha',db.str,False,True,False,False,0,-1,None,None)
db('Negocios').insertar('ZerpaTechnology', [{'Nombre': 'text', 'name': 'nombre', 'value': 'ZerpaTechnology', 'requerido': True}, {'requerido': True, 'Email': 'text', 'value': 'zerpatechnology@gmail.com', 'name': 'email'}, {'Pa\xc3\xads': 'fixed', 'name': 'pais', 'value': 'Venezuela'}, {'Direcci\xc3\xb3n': 'text', 'name': 'direccion', 'value': 'Venezuela', 'requerido': True}, {'Categoria': 'select', 'tabla': 'Categorias', 'name': 'categoria', 'value': 0, 'requerido': True}, {'depende': 'categoria', 'name': 'subcategoria', 'value': 0, 'Subcategorias': 'select', 'requerido': True, 'tabla': 'Categorias'}, {'categoria': 'subcategoria', 'requerido': True, 'value': 0, 'Especialidad': 'select', 'name': 'especialidad'}, {'Imagen': 'select', 'value': 0, 'requerido': True, 'opcion': 0, 'tabla': 'Imagenes', 'name': 'imagen'}, {'Latitud': 'number', 'step': 1e-07, 'name': 'latitud', 'value': 10.5013437, 'requerido': True}, {'step': 1e-07, 'requerido': True, 'value': -66.9216024, 'Longitud': 'number', 'name': 'longitud'}, {'step': 0.1, 'Estrellas': 'number', 'name': 'estrellas', 'value': 0, 'requerido': True}, [{'Horario': 'text', 'name': 'estrellas', 'value': 'Horario', 'requerido': True}, {'Lunes': 'text', 'name': 'lunes', 'value': '9:00am a 4:pm', 'requerido': True}, {'requerido': True, 'value': '9:00am a 4:pm', 'Martes': 'text', 'name': 'martes'}, {'requerido': True, 'value': '9:00am a 4:pm', 'Miercoles': 'text', 'name': 'miercoles'}, {'Jueves': 'text', 'name': 'jueves', 'value': '9:00am a 4:pm', 'requerido': True}, {'requerido': True, 'name': 'viernes', 'value': '9:00am a 4:pm', 'Viernes': 'text'}, {'Sabado': 'text', 'name': 'sabado', 'value': '9:00am a 4:pm', 'requerido': True}, {'Domingo': 'text', 'name': 'domingo', 'value': '9:00am a 4:pm', 'requerido': True}], [{'Opciones de pago': 'text', 'name': 'pago', 'value': 'Opciones de pago'}, {'opcion': 0, 'Efectivo': 'select', 'name': 'efectivo', 'value': 1}, {'opcion': 0, 'Visa': 'select', 'name': 'Visa', 'value': 0}, {'opcion': 0, 'value': 0, 'MasterCard': 'select', 'name': 'MasterCard'}], {'value': 'https://zerpatechnology.com.ve', 'Pagina web': 'text', 'name': 'web'}, {'N\xc3\xbamero de telefono': 'text', 'name': 'telefono', 'value': '584261415102'}], {'Negocio': 0}, '15/4/2017 23:24:56')
db('Archivos').insertar('logo_zerpatec_fondo.png', [[{'Imagen': 'file', 'value': '', 'name': 'archivo'}, {'T\xc3\xadtulo': 'text', 'value': 'logo_zerpatec_fondo.png', 'name': 'renombe'}, {'value': 0, 'name': 'tipo', 'Tipo': 'select', 'tabla': 'Imagenes'}]], {'Archivo': 0}, '15/4/2017 23:24:56')
db('Archivos').insertar('restaurante.jpg', [[{'Imagen': 'file', 'value': '', 'name': 'archivo'}, {'T\xc3\xadtulo': 'text', 'value': 'restaurante.jpg', 'name': 'renombe'}, {'value': 1, 'name': 'tipo', 'Tipo': 'select', 'tabla': 'Imagenes'}]], {'Archivo': 1}, '15/4/2017 23:24:56')
db('Archivos').insertar('tecnologia.jpg', [[{'Imagen': 'file', 'value': '', 'name': 'archivo'}, {'T\xc3\xadtulo': 'text', 'value': 'tecnologia.jpg', 'name': 'renombe'}, {'value': 1, 'name': 'tipo', 'Tipo': 'select', 'tabla': 'Imagenes'}]], {'Archivo': 2}, '15/4/2017 23:24:56')
db('Imagenes').insertar('Negocios', ['logo_zerpatec_fondo.png'])
db('Imagenes').insertar('Categorias', ['tecnologia.jpg'])
db('Categorias').insertar('Tecnologia', 'Software', ['Paginas web', 'Aplicaciones Mobiles', 'WebApps', 'Apicaciones de Escritorio', 'SEO'])
db('Categorias').insertar('Restaurante', 'Cocina', ['Americana', 'Hamburguesa', 'Caribe\xc3\xb1a', 'China', 'Snackbar', 'EetCafe', 'Buena Cena', 'Francesa', 'Griega', 'India', 'Indonesia'])
db('Opciones').insertar('Booleano', ['Si', 'No'])
db.load=False
