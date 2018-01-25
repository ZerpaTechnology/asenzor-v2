if  p["app"]==settings.app:
 
 if p["login"]==True:
  from ztec.zred import decode
  if p["action"]=="write":
   
   f=open(decode(p["kwargs"]["path"]),"w")
   f.write(p["file"])
   f.close()
   print "Archivo guardado"
  elif p["action"]=="delete":
      import os
      os.remove(p["args"]["path"])
      print "El archivo a sido eliminado"
      
      
   

