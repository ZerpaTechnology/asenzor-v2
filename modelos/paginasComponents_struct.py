db=DB()ss
db('Paginas').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Paginas').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Paginas').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Paginas').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Paginas').campo('Status',db.list,False,True,False,False,0,-1,None,None)

db('Paginas').insertar('Inicio', [
	#FILA1 
	[
	 ["Column",{"size":12,
	 			"html":"<div class='col-md-12'> </div>",
	 			"children":[ ["ModuloHTML",{"value":"<textarea></textarea>"}],
	 						 ["Modulo",{}]
	 					  ],
	           }],
	 ["Column",{"size":12,

	           }]
	],
	#FILA2
	[],
	#FILA3 
	[],
	#FILA4 
	[],
	#FILA5 
	[],

	]
	, 
	{'Pagina': 0}, 
	'8/8/2017 19:45:34', 
	[])