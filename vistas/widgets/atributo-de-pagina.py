doc+='''<div class="bg-white">
  <a href="" style="text-decoration: none;color:black">
  <div class="b-s1 pad-05">
   <span><b>Atributo de pagina</b></span>
  </div>
  </a>
  <div>
  
  <div class="pad-1 font-s12">
  
   <div>
     <label>Superior</label> 
     </div>
     <div>
     
     <select name="atributo-control" class="bg-white" width="200px" >
      '''
for elem in settings.http:
  doc+='''
        <option '''
  try: doc+=str("selected" if data['meta-control']==elem else "")
  except Exception, e:   doc+=str(e)
  doc+='''>'''
  try: doc+=str(elem)
  except Exception, e:   doc+=str(e)
  doc+='''</option>
      '''
  pass
doc+='''
     </select> 
  </div>
   <div>
     <label>Plantilla</label> 
     </div>
     <div>
     
     <select name="atributo-layout" class="bg-white" id="plantilla" width="200px" >
      <option>Ninguno</option>
      '''
for elem in settings.layouts:
  doc+='''
      <option '''
  try: doc+=str("selected" if data['meta-layout']==elem else "")
  except Exception, e:   doc+=str(e)
  doc+='''>'''
  try: doc+=str(elem)
  except Exception, e:   doc+=str(e)
  doc+='''</option>
      '''
  pass
doc+='''
     </select> 
   </div>
   <div>
     <label>Orden</label> 
     </div>
     <div>
     <select class="bg-white" width="200px">
      <option>0</option>
     </select> 
   </div>
   <div class="marg-t1" style="color:rgb(50,50,50)"><b>¿Necesitas ayuda? usa la pestaña de ayuda en la parte superior del título de la plantilla.</b></div>
   </div>
  </div>
  
 </div>'''