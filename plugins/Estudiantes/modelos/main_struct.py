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
db("Estudiantes").campo("Nombre",db.str)
db("Estudiantes").campo("Contenido",db.list)
db("Estudiantes").campo("args",db.dict)
db("Estudiantes").campo("Fecha",db.str)
db("Estudiantes").campo("Status",db.list)
#--------------------------------------------
db("Plantillas").insertar("",[[
	{"Nombre":"titulo","name":"titulo","value":""},
	{"Nombres":"titulo","name":"titulo","value":""},
	{"Apellidos":"titulo","name":"titulo","value":""},
	{"Correo Electrónico":"email","name":"email","value":""},
	{"Número de teléfono":"tel","name":"telefono","value":""},
	{"Expediente":"number","name":"expediente","value":0},
	{"Cedula":"number","name":"cedula","value":0},
	{"Número":"number","name":"numero","value":0},
	{"Índice ácademico":"number","name":"indice academico","value":0},
	{"Índice de Repitiente":"number","name":"indice repitiente","value":0},
	{"Beca":"select","name":"beca","value":0,"opcion":0},
	{"Creditos Aprobados":"number","name":"creditos aprobados","value":0},
	],
	[{"SNI":"number","name":"sni","value":0},
	{"Semestres cursados":"list","name":"semestres cursados","value":["2015-1","2015-2","2016-1","2016-2"]},
	]
	],
	{"Plantilla":0},
	zu.DateTime(),
	[]
	)
#--------------------------------------------
db("Plantillas").insertar("",[
	#Requisitos
	[{"Nombre":"titulo","name":"titulo","value":""},
	 {"Requisitos":"list","name":"requisitos","value":["Constancia de inscripción","Constancia de estudio","Record Académico","Cuenta Bancaria"]},
	 {"Pago":"number","name":"pago","value":250000},
	],
	],
	{"Beca":0},
	zu.DateTime(),
	[])
#--------------------------------------------
db("Estudiantes").insertar("Jesus Zerpa",[[
	{"Nombre":"titulo","name":"titulo","value":"Jesus Zerpa"},
	{"Nombres":"titulo","name":"titulo","value":"Jesus Abraham"},
	{"Apellidos":"titulo","name":"titulo","value":"Zerpa Maldonado"},
	{"Correo Electrónico":"email","name":"email","value":"jesus26abraham1996@gmail.com"},
	{"Número de teléfono":"tel","name":"telefono","value":"04261415102"},
	{"Expediente":"number","name":"expediente","value":2015147042},
	{"Cedula":"number","name":"cedula","value":25466590},
	{"Número":"number","name":"numero","value":644},
	{"Índice ácademico":"number","name":"indice academico","value":4.8},
	{"Índice de Repitiente":"number","name":"indice repitiente","value":1.00},
	{"Beca":"select","name":"beca","value":0,"opcion":0},
	{"Creditos Aprobados":"number","name":"creditos aprobados","value":35},
	],
	[{"SNI":"number","name":"sni","value":123456789},
	{"Semestres cursados":"list","name":"semestres cursados","value":["2015-1","2015-2","2016-1","2016-2"]},
	]
	],
	{"Estudiante":0},
	zu.DateTime(),
	[]
	)
db("Becas").campo("Nombre",db.str)
db("Becas").campo("Contenido",db.list)
db("Becas").campo("args",db.dict)
db("Becas").campo("Fecha",db.str)
db("Becas").campo("Status",db.list)
db("Becas").insertar("Empresarial",[
	#Requisitos
	[{"Nombre":"titulo","name":"titulo","value":"Empresarial"},
	 {"Requisitos":"list","name":"requisitos","value":["Constancia de inscripción","Constancia de estudio","Record Académico","Cuenta Bancaria"]},
	 {"Pago":"number","name":"pago","value":250000},
	],
	],
	{"Beca":0},
	zu.DateTime(),
	[])
