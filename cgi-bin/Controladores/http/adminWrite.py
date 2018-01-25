if  p["app"]==settings.app and "action" in p:
 
 if p["login"]==True :
  
  if p["action"]=="write":
    if p["user"]["permisologia"]==0:
       HEADERS.show()
       f=open(decode(p["kwargs"]["path"]),"w")
       f.write(p["file"])
       f.close()
       print "Archivo guardado"
    else:
      HEADERS.show()
      print "No tiene permisos para hacer esto"
   
   
  elif p["action"]=="delete":
    if p["user"]["permisologia"]==0:
      import os
      HEADERS.show()
      os.remove(p["args"]["path"])

      print "El archivo a sido eliminado"
    else:
      HEADERS.show()
      print "No tiene permisos para hacer esto"

  
 elif p["action"]=="write" or p["action"]=="delete":
    HEADERS.show()
    print "Tiempo de sesion agotado, vuelve a loguearte para poder continuar"
      
   

