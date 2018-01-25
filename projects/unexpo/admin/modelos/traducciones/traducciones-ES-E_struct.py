db=DB()
#El sufijo _E indica que los datos almacenados en esta base de datos inician por la letra E
#Esto para facilitar la navegacion y carga de datos de traducciones
db('Palabras').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Palabras').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Palabras').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Palabras').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Palabras').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db("Palabras").insertar("escritorio",
				 [
				 {"Titulo":"titulo","name":"titulo","value":"escritorio"},
				 {"Ingles":"text","name":"en","value":"descktop"},#ingles
				 {"Frances":"text","name":"fr","value":"bureau"},#frances
				 {"Aleman":"text","name":"ge","value":"Schreibtisch"},#aleman
				 {"Portugues":"text","name":"po","value":"escrivaninha"},#portugues
				 {"Italiano":"text","name":"it","value":"scrivania"},#italiano
				 ],
				 {"Palabra":0},
				 zu.DateTime(),
				 []
				 )
db('Frases').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Frases').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Frases').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Frases').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Frases').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db("Frases").insertar("escritorio de vidrio",
				 [
				 {"escritorio de vidrio":"text","name":"es","value":"escritorio de vidrio"},#ingles
				 {"escritorio de vidrio":"text","name":"en","value":"descktop"},#ingles
				 {"escritorio de vidrio":"text","name":"fr","value":"bureau"},#frances
				 {"escritorio de vidrio":"text","name":"ge","value":"Schreibtisch"},#aleman
				 {"escritorio de vidrio":"text","name":"po","value":"escrivaninha"},#portugues
				 {"escritorio de vidrio":"text","name":"it","value":"scrivania"},#italiano
				 ],
				 {"Frase":0},
				 zu.DateTime(),
				 []
				 )