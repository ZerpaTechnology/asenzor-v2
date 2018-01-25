db=DB()
#=============================================
#TABLA NEGOCIOS
db("Negocios").campo("Nombre",db.str)
db("Negocios").campo("Contenido",db.list)
db("Negocios").campo("args",db.dict)
db("Negocios").campo("Fecha",db.str)
#---------------------------------------------
#=============================================
#TABLAS ESPECIALES
#=============================================
#OPCIONES
db("Opciones").campo("Nombre",db.str)
db("Opciones").campo("Valores",db.list)
#---------------------------------------------
#CATEGORIA
db("Categorias").campo("Nombre",db.str)
db("Categorias").campo("Subcategoria",db.str)
db("Categorias").campo("Valores",db.list)
#---------------------------------------------
#IMAGENES
db("Imagenes").campo("Nombre",db.str)
db("Imagenes").campo("Valores",db.list)
#--------------------------------------
#ARCHIVOS
db("Archivos").campo("Nombre",db.str)
db("Archivos").campo("Contenido",db.list) #["imgheader","caja1","logo"]
db("Archivos").campo("args",db.dict)
db("Archivos").campo("Fecha",db.str)
#=============================================
db("Negocios").insertar("ZerpaTechnology",
						[

							{"Nombre":"text","value":"ZerpaTechnology","name":"nombre","requerido":True},
							{"Email":"text","value":"zerpatechnology@gmail.com","name":"email","requerido":True},
							{"País":"fixed","value":"Venezuela","name":"pais"},
							{"Dirección":"text","value":"Venezuela","name":"direccion","requerido":True},
							{"Categoria":"select","value":0,"name":"categoria","requerido":True,"tabla":"Categorias"},
							{"Subcategorias":"select","value":0,"name":"subcategoria","requerido":True,"tabla":"Categorias","depende":"categoria"},
							{"Especialidad":"select","value":0,"name":"especialidad","requerido":True,"categoria":"subcategoria"},
							{"Imagen":"select","value":0,"name":"imagen","requerido":True, "tabla":"Imagenes","opcion":0},
							{"Latitud":"number","value":10.5013437,"name":"latitud","requerido":True,"step":0.0000001 },
							{"Longitud":"number","value":-66.9216024,"name":"longitud","requerido":True,"step":0.0000001},
							{"Estrellas":"number","value":0,"name":"estrellas","requerido":True,"step":0.1},
								[
								{"Horario":"text","value":"Horario","name":"estrellas","requerido":True},
								{"Lunes":"text","value":"9:00am a 4:pm","name":"lunes","requerido":True},
								{"Martes":"text","value":"9:00am a 4:pm","name":"martes","requerido":True},
								{"Miercoles":"text","value":"9:00am a 4:pm","name":"miercoles","requerido":True},
								{"Jueves":"text","value":"9:00am a 4:pm","name":"jueves","requerido":True},
								{"Viernes":"text","value":"9:00am a 4:pm","name":"viernes","requerido":True},
								{"Sabado":"text","value":"9:00am a 4:pm","name":"sabado","requerido":True},
								{"Domingo":"text","value":"9:00am a 4:pm","name":"domingo","requerido":True},
								],
								[							
								{"Opciones de pago":"text","value":"Opciones de pago","name":"pago"},
								{"Efectivo":"select","value":1,"name":"efectivo","opcion":0},
								{"Visa":"select","value":0,"name":"Visa","opcion":0},
								{"MasterCard":"select","value":0,"name":"MasterCard","opcion":0},
								],
							{"Pagina web":"text","value":"https://zerpatechnology.com.ve","name":"web"},
							{"Número de telefono":"text","value":"584261415102","name":"telefono"}
							,
							
						],
						{"Negocio":0},
						zu.DateTime()
						)
#---------------------------------------------
db("Archivos").insertar("logo_zerpatec_fondo.png",
						[
							[
							{"Imagen":"file","name":"archivo","value":""},
							{"Título":"text","name":"renombe","value":"logo_zerpatec_fondo.png"},							
							{"Tipo":"select","name":"tipo","value":0,"tabla":"Imagenes"}
							]
						],
						{"Archivo":0},
						zu.DateTime()
						)
db("Archivos").insertar("restaurante.jpg",
						[
							[
							{"Imagen":"file","name":"archivo","value":""},
							{"Título":"text","name":"renombe","value":"restaurante.jpg"},							
							{"Tipo":"select","name":"tipo","value":1,"tabla":"Imagenes"}
							]
						],
						{"Archivo":1},
						zu.DateTime()
						)
db("Archivos").insertar("tecnologia.jpg",
						[
							[
							{"Imagen":"file","name":"archivo","value":""},
							{"Título":"text","name":"renombe","value":"tecnologia.jpg"},							
							{"Tipo":"select","name":"tipo","value":1,"tabla":"Imagenes"}
							]
						],
						{"Archivo":2},
						zu.DateTime()
						)

db("Imagenes").insertar("Negocios",
	[
	"logo_zerpatec_fondo.png"
	]
	)
db("Imagenes").insertar("Categorias",
	[
	"tecnologia.jpg"
	]
	)

#----------------------------------------

db("Categorias").insertar("Tecnologia","Software",
	[
	"Paginas web",
	"Aplicaciones Mobiles",
	"WebApps",
	"Apicaciones de Escritorio",
	"SEO"
	]
	)
db("Categorias").insertar("Restaurante","Cocina",
	[
	"Americana",
	"Hamburguesa",
	"Caribeña",
	"China",
	"Snackbar",
	"EetCafe",
	"Buena Cena",
	"Francesa",
	"Griega",
	"India",
	"Indonesia",
	]
	)
db("Opciones").insertar("Booleano",
	[
	"Si",
	"No",
	]
	)
#=============================================
db.grabar(self.dbfile+"_db.py")