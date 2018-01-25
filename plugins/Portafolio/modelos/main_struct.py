db=DB()
#============================================
#TABLA de opciones
db("Opciones").campo("Nombre",db.str)
db("Opciones").campo("Valores",db.list)
db("Opciones").insertar("Becas",["Empresarial","Política","Preparaduria","Trabajo"])
#=============================================
db("Plantillas").campo("Nombre",db.str)
db("Plantillas").campo("Contenido",db.list)
db("Plantillas").campo("args",db.dict)
db("Plantillas").campo("Fecha",db.str)
db("Plantillas").campo("Status",db.list)
#============================================
db("Proyectos").campo("Nombre",db.str)
db("Proyectos").campo("Contenido",db.list)
db("Proyectos").campo("args",db.dict)
db("Proyectos").campo("Fecha",db.str)
db("Proyectos").campo("Status",db.list)

#--------------------------------------------
db("Plantillas").insertar("Proyectos",[
	[{"Nombre":"titulo","name":"titulo","value":""}],
	[
	{"Enlace":"text","value":"","name":"enlace"}
	{"Descripción":"textarea","value":"","name":"descripcion"},
	{"Interactividad":"number","value":0,"opcion":0,"max":100,"min":0},
	{"Diseño":"number","value":0,"opcion":0,"max":100,"min":0},
	{"Informacion":"number","value":0,"opcion":0,"max":100,"min":0},
	{"Recursos multimedia":"number","value":0,"opcion":0,"max":100,"min":0},
	{"Estado del proyecto":"number","value":0,"opcion":0,"max":100,"min":0},
	{"Modulos":"list","name":"modulos","value":[]},
	]
	],
	{"Plantilla":0},
	zu.DateTime(),
	[]
	)


