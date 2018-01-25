db=DB()
db("Detalles").campo("Nombre",db.str)
db("Detalles").campo("Portada",db.str)
db("Detalles").campo("Contentindo",db.dict)
db("Detalles").campo("Fecha",db.str)
db("Detalles").insertar("Shortcodes",
	"http://portada.png",
	{
	"tab1":"""
	contendio
	""",
	"tab2":"""
	""",
	"tab3":"""
	"""
	},
	'12/7/2017 10:27:11')