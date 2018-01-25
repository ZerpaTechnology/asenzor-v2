db=DB()
db('ES-palabras').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('ES-palabras').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('ES-palabras').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('ES-palabras').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('ES-palabras').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db("ES-palabras").insertar("escritorio",
				 [
				 {"escritorio":"text","name":"en","value":"descktop"},#ingles
				 {"escritorio":"text","name":"fr","value":"bureau"},#frances
				 {"escritorio":"text","name":"ge","value":"Schreibtisch"},#aleman
				 {"escritorio":"text","name":"po","value":"escrivaninha"},#portugues
				 {"escritorio":"text","name":"it","value":"scrivania"},#italiano
				 ],
				 {"es-palabra":0},
				 zu.DateTime(),
				 []
				 )
db('ES-oraciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('ES-oraciones').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('ES-oraciones').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('ES-oraciones').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('ES-oraciones').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db("ES-oraciones").insertar("escritorio de vidrio",
				 [
				 {"escritorio de vidrio":"text","name":"es","value":"escritorio de vidrio"},#ingles
				 {"escritorio de vidrio":"text","name":"en","value":"descktop"},#ingles
				 {"escritorio de vidrio":"text","name":"fr","value":"bureau"},#frances
				 {"escritorio de vidrio":"text","name":"ge","value":"Schreibtisch"},#aleman
				 {"escritorio de vidrio":"text","name":"po","value":"escrivaninha"},#portugues
				 {"escritorio de vidrio":"text","name":"it","value":"scrivania"},#italiano
				 ],
				 {"es-oracion":0},
				 zu.DateTime(),
				 []
				 )