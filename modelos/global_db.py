# -*- coding: utf-8 -*-
db=DB()
db('Log').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db.load=True
db('Log').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Log').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Log').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Log').campo('Status',db.bool,False,True,False,False,0,-1,None,None)
db('apps').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('apps').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('apps').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('apps').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('apps').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Plugins').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Plugins').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Plugins').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Plugins').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Plugins').campo('Status',db.list,False,True,False,False,0,-1,None,None)
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
db('Gestor-apps').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Gestor-apps').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Gestor-apps').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Gestor-apps').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Gestor-apps').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('static').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('static').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('static').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('static').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('static').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Gestor-plugins').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Proyectos').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Proyectos').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Proyectos').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Proyectos').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Proyectos').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Gestor-apps').insertar('unexpo', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Zerpatechnology': 'https://www.zerpatechnology.com.ve/'}}, {'Portada': 'url', 'name': 'portada', 'value': 'http://localhost/PTC/asenzor/unexpo/static/screen'}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}], [{'unexpo': 'dict', 'name': 'documentacion', 'value': {'Titulo2': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.', 'Titulo1': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.'}}]], {'Gestor-app': 0}, '28/8/2017 18:51:7', ['Destacada', 'Popular', 'Reciente', 'Favorita', 'de Pago'])
db('Opciones').insertar('Permisos', ['Administrador', 'Editor', 'Autor', 'Colaborador', 'Subscriptor'])
db('Asenzor').insertar('0ByJYMxvQwmxFNkpRa19hU3RZWW2c', [{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'web', 'value': ['Yorby Meza', 'Carlos Vegas', 'Jes\xc3\xbas Zerpa']}, {'name': 'licencia', 'value': '0ByJYMxvQwmxFNkpRa19hU3RZWWc', 'licencia': 'text'}, {'Tama\xc3\xb1o': 'text', 'name': 'size', 'value': 4093838}], {'Asenzor': 0}, '28/8/2017 18:51:7', ['Activa'])
db('Asenzor').insertar('0ByJYMxvQwmxFNkpRa19hU3RZWWc', [{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.2'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'web', 'value': {'Yorby Meza': '', 'Carlos Vegas': '', 'Jes\xc3\xbas Zerpa': ''}}, {'name': 'licencia', 'value': '0ByJYMxvQwmxFNkpRa19hU3RZWWc', 'licencia': 'text'}, {'Tama\xc3\xb1o': 'text', 'name': 'size', 'value': 4093838}], {'Asenzor': 1}, '28/8/2017 18:51:7', ['sin descargar'])
db('apps').insertar('hazRealito', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Zerpatechnology': 'https://www.zerpatechnology.com.ve/'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}]], {'app': 0}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('JDYM', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': None}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'name': 'modelo5', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo6', 'value': 'publicaciones'}, {'value': 'informaciones', 'name': 'modelo8', 'Informaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo9', 'value': 'publicaciones'}, {'Galerias': 'text', 'name': 'modelo10', 'value': 'galerias'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 1}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('marquis', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}, {'Formularios': 'text', 'name': 'formularios', 'value': 'formularios'}]], {'app': 2}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('woodridge', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}, {'Formularios': 'text', 'name': 'formularios', 'value': 'formularios'}]], {'app': 3}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('unexpo', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 4}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('royalty', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 5}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('ybor', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 6}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('ridgestone', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 7}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('king-of-pasta', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'name': 'modelo15', 'value': 'menus', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 8}, '4/11/2017 22:33:1', ['Activa'])
db('apps').insertar('occoa', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Zerpatechnology': 'https://www.zerpatechnology.com.ve/'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}]], {'app': 9}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('CBK', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Zerpatechnology': 'https://www.zerpatechnology.com.ve/'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}]], {'app': 10}, '28/8/2017 18:51:7', ['Activa'])
db('apps').insertar('coming-soon', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Zerpatechnology': 'https://www.zerpatechnology.com.ve/'}}], [{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}]], {'app': 11}, '28/8/2017 18:51:7', ['Activa'])
db('Gestor-plugins').insertar('pageCreator', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'pageCreator'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, {'value': 'GNU', 'name': 'licencia', 'Licencia': 'text'}, {'Serial': 'text', 'name': 'serial', 'value': '123456'}, {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'}, {'Portada': 'url', 'name': 'portada', 'value': 'http://localhost/PTC/asenzor/static/plugin/pageCreator/screen'}], [{'Hook del edit': 'text', 'name': 'hook-editar', 'value': '[pageCreator-widget]'}], [{'name': 'documentacion', 'value': {'Titulo2': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.', 'Titulo1': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.'}, 'miPlugin': 'dict'}]], {'Gestor-plugin': 0}, '2/11/2017 22:35:21', ['Destacado', 'Popular', 'Reciente', 'Favorito'])
db('static').insertar('xxxx', [{'Cifrado': 'titulo', 'value': 'xxxx', 'name': 'cifrado'}, {'Nombre': 'text', 'name': 'nombre', 'value': 'archivo'}, {'Descarga': 'url', 'name': 'descarga', 'value': '/root/workspace/htdocs/PTC/projects/unexpo.zip'}], {'static': 0}, '4/10/2017 14:43:33', [])
db('Proyectos').insertar('unexpo', [[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Lider de proyecto': {'Max ochoa': 'occoasolutions@gmail.com'}, 'Producci\xc3\xb3n': {'iokary': 'iokarympc@gmail.com'}, 'Frontend y backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}}}, {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['iokary.jpg', 'logoOccoa.jpg', 'logoZtec.png']}, {'Hecho en': 'text', 'name': 'hecho', 'value': {'Iokary': 'https://www.mpciokary.com/', 'occoa brothers solutions': 'https://occoasolutions.com'}}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, {'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, {'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}, {'Publicaciones': 'text', 'name': 'modelo10', 'value': 'publicaciones'}], [{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, {'Ayuda': 'text', 'name': 'modelo11', 'value': 'ayuda'}, {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}]], {'app': 4}, '4/11/2017 22:33:1', ['Activa'])
db('Plugins').insertar('sc', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'sc'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, {'Licencia': 'text', 'name': 'licencia', 'value': 'GNU'}, {'Serial': 'text', 'name': 'serial', 'value': '123456'}, {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'}], [{'Hook del edit': 'text', 'name': 'otro', 'value': '[miplugin]'}]], {'Plugin': 0}, '26/10/2017 22:52:40', ['Instalado'])
db('Plugins').insertar('Estudiantes', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'Estudiantes'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, {'Licencia': 'text', 'name': 'licencia', 'value': 'GNU'}, {'Serial': 'text', 'name': 'serial', 'value': '123456'}, {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'}], [{'Hook del edit': 'text', 'name': 'otro', 'value': '[miplugin]'}]], {'Plugin': 1}, '26/10/2017 22:52:40', ['Instalado'])
db('Plugins').insertar('Portafolio', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'sc'}, {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, {'Licencia': 'text', 'name': 'licencia', 'value': 'GNU'}, {'Serial': 'text', 'name': 'serial', 'value': '123456'}, {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'}], [{'Hook del edit': 'text', 'name': 'otro', 'value': '[miplugin]'}]], {'Plugin': 2}, '26/10/2017 22:52:40', ['Instalado'])
db('Usuarios').insertar('Administrador', [[{'name': 'usuario', 'value': 'Administrador', 'Usuario': 'text'}, {'Email': 'text', 'value': 'jzerpa.occoa@gmail.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': 'occoasolutions'}, {'opcion': 1, 'opciones': 'archivos', 'Avatar': 'select', 'value': 2, 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': 'tl8XgC>I'}, {'Muere': 'hidden', 'name': 'muere', 'value': '22/1/2018 22:21:39'}, {'Login': 'hidden', 'name': 'login', 'value': True}, {'opcion': 0, 'value': 0, 'name': 'permisologia', 'opciones': 'usuarios', 'Permisologia': 'select'}]], {'Usuario': 0}, '28/11/2017 11:45:7', [])
db('Usuarios').insertar('jesus', [[{'name': 'usuario', 'value': 'jesus', 'Usuario': 'text'}, {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': '1234'}, {'name': 'avatar', 'opciones': 'archivos', 'carpeta': 'Avatares', 'value': 0, 'Avatar': 'img-admin', 'opcion': 1}, {'Token': 'hidden', 'name': 'token', 'value': 'P3ku(b7d'}, {'Muere': 'hidden', 'name': 'muere', 'value': '4/10/2017 15:43:33'}, {'Login': 'hidden', 'name': 'login', 'value': True}, {'opcion': 0, 'opciones': 'usuarios', 'name': 'permisologia', 'value': 0, 'Permisologia': 'select'}, {'Clave': 'text', 'name': 'clave', 'value': ''}]], {'Usuario': 1}, '4/10/2017 14:43:33', [])
db.load=False
