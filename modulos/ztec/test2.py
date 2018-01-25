import zdb
db=zdb.DB("test.py")
print db("Usuarios").obtenerCampo("Contenido")