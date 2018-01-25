db=DB()
db("Contactos").campo("Titulo",db.str)
db("Contactos").campo("Contenido",db.list)
db("Contactos").campo("args",db.dict)
db("Contactos").campo("Fecha",db.str)
db("Contactos").campo("Status",db.list)
#===========================================
db("Conversaciones").campo("Titulo",db.str)
db("Conversaciones").campo("Contenido",db.list)
db("Conversaciones").campo("args",db.dict)
db("Conversaciones").campo("Fecha",db.str)
db("Conversaciones").campo("Status",db.list)
#===========================================
db("Contactos").insertar("Jesus Zerpa",
  [            
    {"Nombre":"text","value":"Jesus Zerpa","name":"nombre"},
     {"Email":"email","value":"jesus26abraham1996@gmail.com","name":"email"},
     {"Avatar":"select-image-admin","value":0,"opcion":1,"name":"avatar"},
     {"Telefono":"phone","value":"04261415102","name":"phone"},
    {"Activo":"bool","opcion":3,"name":"activo","value":0},
    {"Tipo":"select-admin","opcion":6,"name":"tipo","value":0}, #local,global    
    {"Sitio web":"url","value":"zerpatechnology.com.ve","name":"web"}, #en caso de ser global se conectara al dominio
    {"Contraseña":"password","value":"123456","name":"password"},#si es global
    {"Puerto":"number","value":8000,"name":"puerto"},#de ser global se conectara por el puerto 80 por defecto
  ],
  {"Contacto":0},
  zu.DateTime(),
  []
  )
db("Conversaciones").insertar("Usuario1 - Usuario2",
  [
    [{"Conversación":"titulo","value":"Mes - fecha - hora"},
     {"Mensaje":"msj","value":"hola como estas?"},
     {"Mensaje":"msj","value":"bien y tu?"},
    ]
  ],
  {"Conversacion":0},
  zu.DateTime(),
  []
  )



