doc+='''\n   '''
try:
 if "campo" in data:

  elem=data["campo"]
  doc+='''  \n   '''
  k2=data["indice"]
  doc+='''\n   '''
  try:
   if type(elem)==dict:
    doc+='''\n      '''
    tmp=list(elem)
    doc+='''\n      '''
    tmp.remove("name") if "name" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("value") if "value" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("step") if "step" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("opcion") if "opcion" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("requerido") if "requerido" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("tabla") if "tabla" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("depende") if "depende" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("categoria") if "categoria" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("descripcion") if "descripcion" in tmp else tmp
    doc+='''\n      '''
    tmp.remove("padre") if "padre" in tmp else tmp
    doc+='''\n      '''
    tmp=tmp[0]
    doc+='''\n    '''
    try:
     if elem[tmp]=="fixed":
      doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <label>'''
      try: doc+=str(decode(tmp))
      except Exception as e:       doc+=str(e)
      doc+='''</label> \n     <select name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="0" width="200px">\n      <option>'''
      try: doc+=str(decode(elem['value']))
      except Exception as e:       doc+=str(e)
      doc+='''</option>\n     </select>\n     \n     </div> \n    '''
     elif elem[tmp]=="text":
      doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n      <input type="'''
      try: doc+=str(elem[tmp])
      except Exception as e:       doc+=str(e)
      doc+='''" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="'''
      try: doc+=str(elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
      except Exception as e:       doc+=str(e)
      doc+='''>\n     </div>\n    '''
     elif elem[tmp]=="text-admin":
      doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n      <input type="'''
      try: doc+=str(elem[tmp])
      except Exception as e:       doc+=str(e)
      doc+='''" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="'''
      try: doc+=str(elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
      except Exception as e:       doc+=str(e)
      doc+='''>\n     </div>\n    '''
     elif elem[tmp]=="text-email":
      doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n      <input type="email" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="'''
      try: doc+=str(elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
      except Exception as e:       doc+=str(e)
      doc+='''>\n     </div>\n    '''
     elif elem[tmp]=="text-phone":
      doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n      <input type="phone" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="'''
      try: doc+=str(elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
      except Exception as e:       doc+=str(e)
      doc+='''>\n     </div>\n    '''
     elif elem[tmp]=="text-titulo":
      doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n      <input style="width:200px" type="'''
      try: doc+=str(elem[tmp])
      except Exception as e:       doc+=str(e)
      doc+='''" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="'''
      try: doc+=str( elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
      except Exception as e:       doc+=str(e)
      doc+='''>\n      \n      \n       \n      </script>\n     </div>\n    '''
     elif elem[tmp]=="text-admin":
      doc+='''\n         '''
      try:
       if data["login"]==True:
        doc+='''\n          \n          <div class="d-inline-block pad-05 width-20 marg-05">\n          \n          <label>'''
        try: doc+=str(decode(tmp))
        except Exception as e:         doc+=str(e)
        doc+='''<span>['''
        try: doc+=str(k2)
        except Exception as e:         doc+=str(e)
        doc+=''']</span></label>\n          <input type="text" name="'''
        try: doc+=str(elem['name'])
        except Exception as e:         doc+=str(e)
        doc+='''" value="'''
        try: doc+=str(decode(elem['value']))
        except Exception as e:         doc+=str(e)
        doc+='''">\n          </div>\n          '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n    '''
     elif elem[tmp]=="textarea":
      doc+='''\n     <div class="marg-05">\n     <label>'''
      try: doc+=str(decode(tmp))
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n     <textarea class="width-100p editor" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''">'''
      try: doc+=str(decode(elem['value']))
      except Exception as e:       doc+=str(e)
      doc+='''</textarea>\n     </div>\n    '''
     elif elem[tmp]=="textarea-admin" and data["login"]==True:
      doc+='''\n     <div class="marg-05">\n     <label>'''
      try: doc+=str(decode(tmp))
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n     <textarea class="width-100p editor" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''">'''
      try: doc+=str(decode(elem['value']))
      except Exception as e:       doc+=str(e)
      doc+='''</textarea>\n     </div>\n    '''
     elif elem[tmp]=="file":
      doc+='''\n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <img src="" class="width-100p hidden">\n     <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n     <input type="'''
      try: doc+=str(elem[tmp])
      except Exception as e:       doc+=str(e)
      doc+='''" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" class="img-file">\n     </div>\n    '''
     elif elem[tmp]=="select":
      doc+='''\n     \n     \n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <label>'''
      try: doc+=str(decode(tmp))
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n     <select style="width:200px" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''"  '''
      try: doc+=str("depende='"+elem['depende']+"'" if "depende" in elem else "")
      except Exception as e:       doc+=str(e)
      doc+='''  '''
      try: doc+=str('categoria=\"'+elem['categoria']+'\"' if 'categoria' in elem else '')
      except Exception as e:       doc+=str(e)
      doc+=''' '''
      try: doc+=str('tabla="'+elem['tabla']+'"' if 'tabla' in elem else '')
      except Exception as e:       doc+=str(e)
      doc+='''> \n     \n      '''
      try:
       if "opcion" in elem and "tabla" not in elem:
        doc+='''\n       \n\n       '''
        try:
         for _k, opcion in enumerate(data["opciones"][elem['opcion']][1]):
          doc+='''\n        <option '''
          try: doc+=str("selected" if elem['value']==_k else '')
          except Exception as e:           doc+=str(e)
          doc+=''' >'''
          try: doc+=str(decode(opcion))
          except Exception as e:           doc+=str(e)
          doc+='''</option>\n        '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n\n      '''
       elif "opcion" in elem and "tabla" in elem and elem["tabla"]=="Imagenes":
        doc+='''\n       \n\n       '''
        try:
         for _k, opcion in enumerate(data["imagenes"][elem["opcion"]][1]):
          doc+='''\n        <option '''
          try: doc+=str("selected" if elem['value']==_k else '')
          except Exception as e:           doc+=str(e)
          doc+=''' >'''
          try: doc+=str(decode(opcion))
          except Exception as e:           doc+=str(e)
          doc+='''</option>\n        '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n       \n\n      '''
       elif "tabla" in elem and "depende" not in elem:
        doc+='''\n         \n         '''
        try:
         for opcion in data["tablas"][elem['tabla']]:
          doc+='''\n         <option >'''
          try: doc+=str(decode(opcion))
          except Exception as e:           doc+=str(e)
          doc+='''</option>\n         '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n      '''
       elif "tabla" in elem and "depende" in elem:
        doc+='''\n         \n         '''
        try:
         for opcion in list(data["categorias"][data["tablas"][elem['tabla']][0]]):
          doc+='''\n         <option >'''
          try: doc+=str(decode(opcion))
          except Exception as e:           doc+=str(e)
          doc+='''</option>\n         '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n      \n      '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n        \n     </select>\n     </div>\n    '''
     elif elem[tmp]=="select-admin":
      doc+='''\n     '''
      try:
       if data["login"]==True:
        doc+='''\n      <div class="d-inline-block pad-05 width-20 marg-05">\n      <label>'''
        try: doc+=str(decode(tmp))
        except Exception as e:         doc+=str(e)
        doc+='''<span>['''
        try: doc+=str(k2)
        except Exception as e:         doc+=str(e)
        doc+=''']</span></label>\n      <select style="width:200px" name="'''
        try: doc+=str(elem['name'])
        except Exception as e:         doc+=str(e)
        doc+='''" >\n       '''
        try:
         for _k, opcion in enumerate(data["opciones"][elem['opcion']][1]):
          doc+='''\n        <option value="'''
          try: doc+=str( _k)
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str( "selected" if elem['value']==_k else '')
          except Exception as e:           doc+=str(e)
          doc+=''' >'''
          try: doc+=str(decode(opcion))
          except Exception as e:           doc+=str(e)
          doc+='''</option>\n        '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n      </select>\n\n      </div>\n      '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n    '''
     elif elem[tmp]=="img":
      doc+='''\n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <img src="'''
      try: doc+=str(data['base_url'])
      except Exception as e:       doc+=str(e)
      doc+='''../admin/static/archivos/Imagenes/'''
      try: doc+=str(data['opciones'][elem['opcion']][1][elem['value']])
      except Exception as e:       doc+=str(e)
      doc+='''" class="width-100p">\n     <B>Imagen</B>\n     <input type="" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" class="hidden">\n     </div>\n    '''
     elif elem[tmp]=="img-admin":
      doc+='''\n   \n     <div class="d-inline-block pad-05 width-20 marg-05">\n       <img src="" class="width-100p hidden" archivos="'''
      try: doc+=str(elem['carpeta'] if 'carpeta' in elem else '')
      except Exception as e:       doc+=str(e)
      doc+='''">\n       <label>'''
      try: doc+=str(decode(tmp))
      except Exception as e:       doc+=str(e)
      doc+='''</label>\n       \n       <select style="width:200px" class="img-admin" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''"  value="'''
      try: doc+=str(elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str("depende='"+opcion+"'" if "depende" in elem else "")
      except Exception as e:       doc+=str(e)
      doc+=''' '''
      try: doc+=str('tabla="'+elem['tabla']+'"' if 'tabla' in elem else '')
      except Exception as e:       doc+=str(e)
      doc+=''' '''
      try: doc+=str('categoria="'+elem['categoria']+'"' if 'categoria' in elem else '')
      except Exception as e:       doc+=str(e)
      doc+=''' '''
      try: doc+=str('opcion="'+str(elem['opcion'])+'"' if 'opcion' in elem else '')
      except Exception as e:       doc+=str(e)
      doc+='''>\n       '''
      try:
       for _k,i in enumerate(data["opciones"][data["campo"]["opciones"]][data["campo"]["opcion"]][1]):
        doc+='''\n        <option value="'''
        try: doc+=str(_k)
        except Exception as e:         doc+=str(e)
        doc+='''">'''
        try: doc+=str(i)
        except Exception as e:         doc+=str(e)
        doc+='''</option>\n        '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n\n       </select>\n\n       </div>\n  '''
     elif elem[tmp]=="number":
      doc+='''\n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <label>'''
      try: doc+=str(tmp)
      except Exception as e:       doc+=str(e)
      doc+='''<span>['''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+=''']</span></label>\n     <input type="'''
      try: doc+=str(elem[tmp])
      except Exception as e:       doc+=str(e)
      doc+='''" name="'''
      try: doc+=str(elem['name'])
      except Exception as e:       doc+=str(e)
      doc+='''" value="'''
      try: doc+=str(elem['value'])
      except Exception as e:       doc+=str(e)
      doc+='''" '''
      try: doc+=str( "step='"+elem['step']+"'" if "step" in elem else "")
      except Exception as e:       doc+=str(e)
      doc+='''>\n     </div>\n  '''
     elif type(elem)==list:
      doc+='''\n     <div class="b-s1 pad-1 marg-1 b-r5 marg-05">\n     </div> \n  '''
     elif elem!=None:
      doc+='''\n      <div class="b-s1 b-r5 marg-05">\n      <h2 id="titulo'''
      try: doc+=str(k2)
      except Exception as e:       doc+=str(e)
      doc+='''"></h2>\n      </div>\n  '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n\n'''