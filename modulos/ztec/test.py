#!/usr/bin/python
# -*- coding: utf-8 -*-
import zdb
db=zdb.DB()
db('Log').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Log').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Log').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Log').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Log').campo('Status',db.bool,False,True,False,False,0,-1,None,None)
db('apps').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('apps').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('apps').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('apps').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('apps').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Usuarios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Asenzor').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Asenzor').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Asenzor').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Asenzor').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Asenzor').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Contactos').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Contactos').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Contactos').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Contactos').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Contactos').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').insertar('Permisos', ['Administrador', 'Editor', 'Autor', 'Colaborador', 'Subscriptor'])
db('Asenzor').insertar('0ByJYMxvQwmxFNkpRa19hU3RZWW2c', [{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'web', 'value': ['Yorby Meza', 'Carlos Vegas', 'Jes\xc3\xbas Zerpa']}, {'name': 'licencia', 'value': '0ByJYMxvQwmxFNkpRa19hU3RZWWc', 'licencia': 'text'}, {'Tama\xc3\xb1o': 'text', 'name': 'size', 'value': 4093838}], {'Asenzor': 0}, '28/8/2017 18:51:7', ['Activa'])
db('Asenzor').insertar('0ByJYMxvQwmxFNkpRa19hU3RZWWc', [{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.2'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'web', 'value': {'Yorby Meza': '', 'Carlos Vegas': '', 'Jes\xc3\xbas Zerpa': ''}}, {'name': 'licencia', 'value': '0ByJYMxvQwmxFNkpRa19hU3RZWWc', 'licencia': 'text'}, {'Tama\xc3\xb1o': 'text', 'name': 'size', 'value': 4093838}], {'Asenzor': 1}, '28/8/2017 18:51:7', ['sin descargar'])
db('apps').insertar('hazRealito', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}]], {'app': 0}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('JDYM', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': None}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'name': 'modelo5', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo6', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo7', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo8', 'value': 'informaciones'}, {'Publicaciones': 'text', 'name': 'modelo9', 'value': 'publicaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 1}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('asosa', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}, {'Publicaciones': 'text', 'name': 'modelo10', 'value': 'publicaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 2}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('woodridge', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}, {'Publicaciones': 'text', 'name': 'modelo10', 'value': 'publicaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 3}, '28/8/2017 18:51:7', ['Activa'])
db('Usuarios').insertar('Programador', [[{'name': 'usuario', 'value': 'Administrador', 'Usuario': 'text'}, {'Email': 'text', 'value': 'jzerpa.occoa@gmail.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': 'occoasolutions'}, {'opcion': 1, 'opciones': 'archivos', 'Avatar': 'select', 'value': 0, 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': ']iO@2f>r'}, {'Muere': 'hidden', 'name': 'muere', 'value': '5/10/2017 19:55:59'}, {'Login': 'hidden', 'name': 'login', 'value': False}, {'opcion': 0, 'value': 0, 'name': 'permisologia', 'opciones': 'usuarios', 'Permisologia': 'select'}]], {'globalUser': 0}, '12/7/2017 10:27:11', [])
db('Usuarios').insertar('jesus', [[{'name': 'usuario', 'value': 'jesus', 'Usuario': 'text'}, {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': '1234'}, {'opcion': 1, 'value': 0, 'Avatar': 'select', 'opciones': 'archivos', 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': 'P3ku(b7d'}, {'Muere': 'hidden', 'name': 'muere', 'value': '4/10/2017 15:43:33'}, {'Login': 'hidden', 'name': 'login', 'value': True}, {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': 0, 'Permisologia': 'select'}]], {'Usuario': 1}, '4/10/2017 14:43:33', [])


