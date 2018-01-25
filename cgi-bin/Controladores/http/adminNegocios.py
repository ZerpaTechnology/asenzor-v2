#METODO POST

if data["action"].value=="Registrar":
 if  p["app"]==settings.app:
  try:
   horarios={"value":data["horarios"].value if "horario" in data else ""}
   horarios["lunes"]=data["lunes"].value
   horarios["martes"]=data["martes"].value
   horarios["miercoles"]=data["miercoles"].value
   horarios["jueves"]=data["jueves"].value
   horarios["viernes"]=data["viernes"].value
   horarios["sabado"]=data["sabado"].value
   horarios["domingo"]=data["domingo"].value
  except:
   horarios={}
  
  try:
   nombre=data["nombre"].value
  except:
   nombre=""
  try:
   email=data["email"].value
  except:
   email=""
  try:
   direccion=data["direccion"].value
  except:
   direccion=""
  try:
   categoria=int(data["categoria"].value)
  except:
   categoria=0
  try:
   subcategoria=int(data["subcategoria"].value)
  except:
   subcategoria=0
  try:
   especialidad=int(data["especialidad"].value)
  except:
   especialidad=0
  try:
   imagen=int(data["imagen"].value)
  except:
   imagen=0
  try:
   latitud=float(data["latitud"].value)
  except:
   latitud=0
  try:
   longitud=float(data["longitud"].value)
  except:
   lonfitud=0
  try:
   estrellas=int(data["estrellas"].value)
  except:
   estrellas=0
  try:
   telefono=data["telefono"].value
  except:
   telefono=""
  
  try:
   pago=data["pago"].value
  except:
   pago=""
  try:
   efectivo=int(data["efectivo"].value)
  except:
   efectivo=0
  try:
   visa=int(data["visa"].value)
  except:
   visa=0
  try:
   mastercard=int(data["mastercard"].value)
  except:
   mastercard=0
  try:
   web=data["web"].value
  except:
   web=""
  try:
   notas=data["notas"].value
  except:
   notas=""

  p["model"]["negocios"].registrarNegocio(nombre,email,direccion,categoria,subcategoria,especialidad,imagen,"Holanda",latitud,longitud,estrellas,horarios,telefono,pago,efectivo,visa,mastercard,web,notas)


elif data["action"].value=="Guardar":
 if  p["app"]=="ATET":
  try:
   horarios={}
   horarios["lunes"]=data["lunes"].value
   horarios["martes"]=data["martes"].value
   horarios["miercoles"]=data["miercoles"].value
   horarios["jueves"]=data["jueves"].value
   horarios["viernes"]=data["viernes"].value
   horarios["sabado"]=data["sabado"].value
   horarios["domingo"]=data["domingo"].value
  except:
   horarios={}
  

  p["model"]["negocios"].modificarNegocio(p["args"][1],data["nombre"].value, nombre,email,direccion,categoria,subcategoria,especialidad,imagen,"Holanda",latitud,longitud,estrellas,horarios,telefono,web,notas)

