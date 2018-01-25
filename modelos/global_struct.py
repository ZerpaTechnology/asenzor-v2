db=DB(debug=True)
#=========================
#REGISTRO DE ERRORES
db("Log").campo("Nombre",db.str)
db("Log").campo("Contenido",db.list)
db("Log").campo("args",db.dict)
db("Log").campo("Fecha",db.str,formato="%d/%m/%Y %H:%M:%S")
db("Log").campo("Status",db.list)
#=========================
#Plugins instalados
db("Plugins").campo("Nombre",db.str)
db("Plugins").campo("Contenido",db.list)
db("Plugins").campo("args",db.dict)
db("Plugins").campo("Fecha",db.str,formato="%d/%m/%Y %H:%M:%S")
db("Plugins").campo("Status",db.list)
#=========================
#REGISTRO DE LAS BASES DE DATOS DE LAS APPS
db("apps").campo("Nombre",db.str)
db("apps").campo("Contenido",db.list)
db("apps").campo("args",db.dict)
db("apps").campo("Fecha",db.str,formato="%d/%m/%Y %H:%M:%S")
db("apps").campo("Status",db.list)
#=========================
#REGISTRO DE LOS CONTACTOS DEL ADMINISTRADOS DEL FMK
db("Contactos").campo("Nombre",db.str)
db("Contactos").campo("Contenido",db.list)
db("Contactos").campo("args",db.dict)
db("Contactos").campo("Fecha",db.str,formato="%d/%m/%Y %H:%M:%S")
db("Contactos").campo("Status",db.list)

db('Gestor-apps').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Gestor-apps').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Gestor-apps').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Gestor-apps').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Gestor-apps').campo('Status',db.list,False,True,False,False,0,-1,None,None)

db('Gestor-plugins').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Gestor-plugins').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Gestor-plugins').campo('Status',db.list,False,True,False,False,0,-1,None,None)

#=========================
db("apps").insertar("asosa",
	[
		#Detalles de la aplicacion
		[
		{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, 
		{'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, 
		{'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, 
		{'Colaboraciones': 'text', 'name': 'web', 'value': ['occoasolutions.com', 'iokary.com']}
		],
		#modelos de la aplicacion
		[
		{'Principal': 'text', 'name': 'modelo1', 'value': 'main'}, 
		{'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}, 
		{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, 
		{'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, 
		{'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, 
		{'Conversaciones': 'text', 'name': 'modelo6', 'value': 'conversaciones'}, 
		{'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, 
		{'Anuncios': 'text', 'name': 'modelo8', 'value': 'anuncios'}, 
		{'Informaciones': 'text', 'name': 'modelo9', 'value': 'informaciones'}, 
		]
	],
	{"app":0},
	zu.DateTime(),
	["Activa"])
db('apps').insertar('JDYM', 
	[
		[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, 
		 {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, 
		 {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, 
		 {'Colaboraciones': 'text', 'name': 'web', 'value': ['Yorby Meza',"Carlos Vegas", 'Jesús Zerpa']}
		 ], 
		[{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, 
		 {'Usuarios': 'text', 'name': 'modelo2', 'value': 'usuarios'}, 
		 {'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, 
		 {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, 
		 {'Archivos': 'text', 'name': 'modelo5', 'value': 'archivos'}, 
		 {'value': 'conversaciones', 'name': 'modelo6', 'Conversaciones': 'text'}, 
		 {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, 
		 {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, 
		 {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}
		 {'value': 'publicaciones', 'name': 'modelo10', 'Publicaciones': 'text'}
		]
	], 
	{'app': 1}, 
	'28/8/2017 18:51:7', 
	["Activa"])
db('Plugins').insertar('pageCreator', [
	[{'Titulo': 'text', 'name': 'titulo', 'value': 'pageCreator'}, 
	 {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, 
	 {'Licencia': 'text', 'name': 'licencia', 'value': 'GNU'}, 
	 {'Serial': 'text', 'name': 'serial', 'value': '123456'}, 
	 {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, 
	 {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, 
	 {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, 
	 {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'}, 
	 {'opcion': 0, 'Activo': 'select', 'name': 'web', 'value': 0}],
	 [{'Hook del edit': 'text', 'name': 'hook-edit', 'value': '[pageCreator-widget]'}],
	 ], 
	 {'Plugin': 0}, 
	 '12/7/2017 10:27:11', 
	 ["Instalado"])
db('Gestor-apps').insertar('hazRealito', [
	#creditos
	[{'Versi\xc3\xb3n': 'text', 'name': 'version', 'value': '0.0.1'}, 
	 {'Autor': 'text', 'name': 'autor', 'value': 'Jes\xc3\xbas Abraham Zerpa Maldonado'}, 
	 {'Email del Autor': 'text', 'name': 'email', 'value': 'jzerpa.occoa@gmail.com'}, 
	 {'Colaboraciones': 'text', 'name': 'colaboraciones', 'value': {'Maquetaci\xc3\xb3n': {'Yorby Meza': 'yorvymeza@gmail.com', 
	 																					   'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 
	 																'Desarrollo backend': {'Jes\xc3\xbas Zerpa': 'jesus26abraham1996@gmail.com'}, 
	 																'Dise\xc3\xb1o': {'Carlos Vegas': 'carlosvegas@gmail.com'}}
	 																}, 
	 {'Colaboraciones Logos': 'text', 'name': 'colaboraciones-imgs', 'value': ['logoZtec.png']}, 
	 {'Hecho en': 'text', 'name': 'hecho', 'value': {'Zerpatechnology': 'https://www.zerpatechnology.com.ve/'}}
	], 
	#modelos locales
	[{'Formularios': 'text', 'name': 'modelo3', 'value': 'formularios'}, 
	 {'name': 'modelo6', 'value': 'conversaciones', 'Conversaciones': 'text'}, 
	 {'Publicaciones': 'text', 'name': 'modelo7', 'value': 'publicaciones'}, 
	 {'value': 'anuncios', 'name': 'modelo8', 'Anuncios': 'text'}, 
	 {'value': 'informaciones', 'name': 'modelo9', 'Informaciones': 'text'}
	], 
	#modelos globales
	[{'name': 'modelo1', 'value': 'main', 'Principal': 'text'}, 
	 {'Archivos': 'text', 'name': 'modelo2', 'value': 'archivos'}, 
	 {'Usuarios': 'text', 'name': 'modelo3', 'value': 'usuarios'}, 
	 {'Paginas': 'text', 'name': 'modelo4', 'value': 'paginas'}, 
	 {'Menus': 'text', 'name': 'modelo5', 'value': 'menus'}
	],
	#documentacion
	[{"name":"documentacion",'hazRealito':"dict","value":{
	"Titulo1":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.",
	"Titulo2":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.",
	}},
	]
	], 
	{'Gestor-app': 0}, 
	'28/8/2017 18:51:7', 
	['Destacada',"Popular","Reciente","Favorita"])

db('Gestor-plugins').insertar('miplugin', [
	#creditos
	[{'Titulo': 'text', 'name': 'titulo', 'value': 'pageCreator'}, 
	 {'Autor': 'text', 'name': 'autor', 'value': 'Jesus Zerpa'}, 
	 {'value': 'GNU', 'name': 'licencia', 'Licencia': 'text'}, 
	 {'Serial': 'text', 'name': 'serial', 'value': '123456'}, 
	 {'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 37}, 
	 {'Descripci\xc3\xb3n': 'textarea', 'name': 'descripcion', 'value': ''}, 
	 {'Email': 'text', 'value': 'jesus26abraham1996@gmail.com', 'name': 'email'}, 
	 {'Web': 'text', 'name': 'web', 'value': 'https://zerpatechnology.com.ve'},
	], 
	#modelos globales
	[{'Hook del edit': 'text', 'name': 'hook-editar', 'value': '[pageCreator-widget]'},
	],
	#documentacion
	[{"name":"documentacion",'miPlugin':"dict","value":{
	"Titulo1":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.",
	"Titulo2":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat tenetur perspiciatis obcaecati doloribus maiores ex eveniet quod laudantium atque assumenda quae hic culpa, praesentium ipsa vel excepturi veniam amet quidem.",
	}},],

	], 
	{'Gestor-plugin': 0}, 
	zu.DateTime(), 
	['Destacado',"Popular","Reciente","Favorito"])
db.grabar(dbfile+"_db.py")