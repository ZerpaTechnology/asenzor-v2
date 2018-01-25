doc+='''\n'''
try:
 for k,box in enumerate(data["boxes"]):
  doc+='''\n\n\n \n  <div class="b-s1 pad-1 b-r5">\n  <div>\n  \n  \n  '''
  try:
   if box!=None:
    doc+='''\n  '''
    try:
     for k2,elem in enumerate(box):
      doc+='''\n   '''
      try:
       if type(elem)==dict:
        doc+='''\n    '''
        tmp=list(elem)
        doc+='''\n\n    '''
        tmp.remove("name") if "name" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("value") if "value" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("step") if "step" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("opcion") if "opcion" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("requerido") if "requerido" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("tabla") if "tabla" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("depende") if "depende" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("categoria") if "categoria" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("descripcion") if "descripcion" in tmp else tmp
        doc+='''\n    '''
        tmp.remove("padre") if "padre" in tmp else tmp
        doc+='''\n    '''
        tmp=tmp[0]
        doc+='''\n    \n    \n    \n    \n    '''
        try:
         if elem[tmp]=="fixed":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <label>'''
          try: doc+=str(decode(tmp))
          except Exception as e:           doc+=str(e)
          doc+='''</label> \n     <select name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="0" width="200px">\n      <option>'''
          try: doc+=str(decode(elem['value']))
          except Exception as e:           doc+=str(e)
          doc+='''</option>\n     </select>\n     \n     </div> \n    '''
         elif elem[tmp]=="text":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n      <input type="'''
          try: doc+=str(elem[tmp])
          except Exception as e:           doc+=str(e)
          doc+='''" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
          except Exception as e:           doc+=str(e)
          doc+='''>\n     </div>\n    '''
         elif elem[tmp]=="text-admin":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n      <input type="'''
          try: doc+=str(elem[tmp])
          except Exception as e:           doc+=str(e)
          doc+='''" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
          except Exception as e:           doc+=str(e)
          doc+='''>\n     </div>\n    '''
         elif elem[tmp]=="text-email":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n      <input type="email" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
          except Exception as e:           doc+=str(e)
          doc+='''>\n     </div>\n    '''
         elif elem[tmp]=="text-phone":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n      <input type="phone" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
          except Exception as e:           doc+=str(e)
          doc+='''>\n     </div>\n    '''
         elif elem[tmp]=="text-titulo":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 b-s1 marg-05">\n      \n      <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n      <input style="width:200px" type="'''
          try: doc+=str(elem[tmp])
          except Exception as e:           doc+=str(e)
          doc+='''" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str("required" if "requerido" in elem and elem['requerido']==True else '')
          except Exception as e:           doc+=str(e)
          doc+='''>\n      <script type="text/javascript">\n      $("#titulo'''
          try: doc+=str(k)
          except Exception as e:           doc+=str(e)
          doc+='''").html("'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''");\n      $("input[name='''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+=''']").on("text",function(){\n       $("#titulo'''
          try: doc+=str(k)
          except Exception as e:           doc+=str(e)
          doc+='''").html($("input[name='''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+=''']").;\n      })\n      \n       \n      </script>\n     </div>\n\n    '''
         elif elem[tmp]=="text-admin":
          doc+='''\n     '''
          try:
           if data["login"]==True:
            doc+='''\n      \n      <div class="d-inline-block pad-05 width-20 marg-05">\n      \n      <label>'''
            try: doc+=str(decode(tmp))
            except Exception as e:             doc+=str(e)
            doc+='''<span>['''
            try: doc+=str(k2)
            except Exception as e:             doc+=str(e)
            doc+=''']</span></label>\n      <input type="text" name="'''
            try: doc+=str(elem['name'])
            except Exception as e:             doc+=str(e)
            doc+='''" value="'''
            try: doc+=str(decode(elem['value']))
            except Exception as e:             doc+=str(e)
            doc+='''">\n      </div>\n      '''
            pass
          except Exception as e: doc+=str(e)
          doc+='''\n    '''
         elif elem[tmp]=="textarea":
          doc+='''\n     <div class="marg-05">\n     <label>'''
          try: doc+=str(decode(tmp))
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n     <textarea class="width-100p editor" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''">'''
          try: doc+=str(decode(elem['value']))
          except Exception as e:           doc+=str(e)
          doc+='''</textarea>\n     </div>\n    '''
         elif elem[tmp]=="textarea-admin" and data["login"]==True:
          doc+='''\n     <div class="marg-05">\n     <label>'''
          try: doc+=str(decode(tmp))
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n     <textarea class="width-100p editor" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''">'''
          try: doc+=str(decode(elem['value']))
          except Exception as e:           doc+=str(e)
          doc+='''</textarea>\n     </div>\n    '''
         elif elem[tmp]=="file":
          doc+='''\n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <img src="" class="width-100p hidden">\n     <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n     <input type="'''
          try: doc+=str(elem[tmp])
          except Exception as e:           doc+=str(e)
          doc+='''" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" class="img-file">\n     </div>\n    '''
         elif elem[tmp]=="select":
          doc+='''\n     \n     \n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <label>'''
          try: doc+=str(decode(tmp))
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n     <select style="width:200px" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''"  '''
          try: doc+=str("depende='"+elem['depende']+"'" if "depende" in elem else "")
          except Exception as e:           doc+=str(e)
          doc+='''  '''
          try: doc+=str('categoria=\"'+elem['categoria']+'\"' if 'categoria' in elem else '')
          except Exception as e:           doc+=str(e)
          doc+=''' '''
          try: doc+=str('tabla="'+elem['tabla']+'"' if 'tabla' in elem else '')
          except Exception as e:           doc+=str(e)
          doc+='''> \n     \n      '''
          try:
           if "opcion" in elem and "tabla" not in elem:
            doc+='''\n       \n\n       '''
            try:
             for _k, opcion in enumerate(data["opciones"][elem['opcion']][1]):
              doc+='''\n        <option '''
              try: doc+=str("selected" if elem['value']==_k else '')
              except Exception as e:               doc+=str(e)
              doc+=''' >'''
              try: doc+=str(decode(opcion))
              except Exception as e:               doc+=str(e)
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
              except Exception as e:               doc+=str(e)
              doc+=''' >'''
              try: doc+=str(decode(opcion))
              except Exception as e:               doc+=str(e)
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
              except Exception as e:               doc+=str(e)
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
              except Exception as e:               doc+=str(e)
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
            except Exception as e:             doc+=str(e)
            doc+='''<span>['''
            try: doc+=str(k2)
            except Exception as e:             doc+=str(e)
            doc+=''']</span></label>\n      <select style="width:200px" name="'''
            try: doc+=str(elem['name'])
            except Exception as e:             doc+=str(e)
            doc+='''" >\n       '''
            try:
             for _k, opcion in enumerate(data["opciones"][elem['opcion']][1]):
              doc+='''\n        <option value="'''
              try: doc+=str(_k)
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("selected" if elem['value']==_k else '')
              except Exception as e:               doc+=str(e)
              doc+=''' >'''
              try: doc+=str(decode(opcion))
              except Exception as e:               doc+=str(e)
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
          except Exception as e:           doc+=str(e)
          doc+='''../admin/static/archivos/Imagenes/'''
          try: doc+=str(data['opciones'][elem['opcion']][1][elem['value']])
          except Exception as e:           doc+=str(e)
          doc+='''" class="width-100p">\n     <B>Imagen</B>\n     <input type="" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" class="hidden">\n     </div>\n    '''
         elif elem[tmp]=="img-admin":
          doc+='''\n     \n     <div class="d-inline-block pad-05 width-20 marg-05">\n       zzzzzzz\n       </div> \n    '''
         elif elem[tmp]=="number":
          doc+='''\n     <div class="d-inline-block pad-05 width-20 marg-05">\n     <label>'''
          try: doc+=str(tmp)
          except Exception as e:           doc+=str(e)
          doc+='''<span>['''
          try: doc+=str(k2)
          except Exception as e:           doc+=str(e)
          doc+=''']</span></label>\n     <input type="'''
          try: doc+=str(elem[tmp])
          except Exception as e:           doc+=str(e)
          doc+='''" name="'''
          try: doc+=str(elem['name'])
          except Exception as e:           doc+=str(e)
          doc+='''" value="'''
          try: doc+=str(elem['value'])
          except Exception as e:           doc+=str(e)
          doc+='''" '''
          try: doc+=str("step='"+elem['step']+"'" if "step" in elem else "")
          except Exception as e:           doc+=str(e)
          doc+='''>\n     </div>\n     \n    '''
         elif type(elem)==list:
          doc+='''\n     <div class="b-s1 pad-1 marg-1 b-r5 marg-05">\n     </div> \n     '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n    \n   '''
       elif elem!=None:
        doc+='''\n    <div class="b-s1 b-r5 marg-05">\n    <h2 id="titulo'''
        try: doc+=str(k2)
        except Exception as e:         doc+=str(e)
        doc+='''"></h2>\n    \n   \n    '''
        try:
         for sub in elem:
          doc+='''\n    \n     \n     '''
          try:
           if type(sub)==str:
            doc+='''\n      <h3>'''
            try: doc+=str(sub)
            except Exception as e:             doc+=str(e)
            doc+='''</h3>\n     '''
           elif type(sub)==dict:
            doc+='''\n      '''
            tmp=list(sub)
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
            tmp.remove("categoria") if "captegoria" in tmp else tmp
            doc+='''\n      '''
            tmp.remove("descripcion") if "descripcion" in tmp else tmp
            doc+='''\n      '''
            tmp.remove("padre") if "padre" in tmp else tmp
            doc+='''\n      \n\n      '''
            tmp=tmp[0]
            doc+='''\n      \n      '''
            try:
             if sub[tmp]=="text":
              doc+='''\n      \n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       \n       <input type="'''
              try: doc+=str(sub[tmp])
              except Exception as e:               doc+=str(e)
              doc+='''" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(decode(sub['value']))
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("required" if "requerido" in sub and sub['requerido']==True else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n       </div>\n      '''
             elif sub[tmp]=="img":
              doc+='''\n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <img src="'''
              try: doc+=str(data['base_url'])
              except Exception as e:               doc+=str(e)
              doc+='''../admin/static/archivos/Imagenes/'''
              try: doc+=str(data['opciones'][sub['opcion']][1][sub['value']])
              except Exception as e:               doc+=str(e)
              doc+='''" class="width-100p">\n       <B>Imagen</B>\n       <input type="" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" class="hidden">\n       </div>\n      '''
             elif sub[tmp]=="text-admin":
              doc+='''\n      \n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       \n       <input type="'''
              try: doc+=str(sub[tmp])
              except Exception as e:               doc+=str(e)
              doc+='''" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(decode(sub['value']))
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("required" if "requerido" in sub and sub['requerido']==True else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n       </div>\n      '''
             elif sub[tmp]=="text-email":
              doc+='''\n       \n       <div class="d-inline-block pad-05 width-20 marg-05">\n        \n        <label>'''
              try: doc+=str(tmp)
              except Exception as e:               doc+=str(e)
              doc+='''<span>['''
              try: doc+=str(k2)
              except Exception as e:               doc+=str(e)
              doc+=''']</span></label>\n        <input type="email" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(sub['value'])
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("required" if "requerido" in sub and sub['requerido']==True else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n       </div>\n      '''
             elif sub[tmp]=="text-phone":
              doc+='''\n       \n       <div class="d-inline-block pad-05 width-20 marg-05">\n        \n        <label>'''
              try: doc+=str(tmp)
              except Exception as e:               doc+=str(e)
              doc+='''<span>['''
              try: doc+=str(k2)
              except Exception as e:               doc+=str(e)
              doc+=''']</span></label>\n        <input type="phone" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(sub['value'])
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("required" if "requerido" in sub and sub['requerido']==True else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n       </div>\n      '''
             elif sub[tmp]=="text-titulo":
              doc+='''\n       \n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       \n       <input style="width:200px" type="'''
              try: doc+=str(sub[tmp])
              except Exception as e:               doc+=str(e)
              doc+='''" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(decode(sub['value']))
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("required" if "requerido" in sub and sub['requerido']==True else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n       </div>\n       <script>\n       $("#titulo'''
              try: doc+=str(k2)
              except Exception as e:               doc+=str(e)
              doc+='''").html("'''
              try: doc+=str(sub['value'])
              except Exception as e:               doc+=str(e)
              doc+='''");\n       $("input[name='''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+=''']").on("keyup",function(){\n        $("#titulo'''
              try: doc+=str(k2)
              except Exception as e:               doc+=str(e)
              doc+='''").html(this.value);\n       })\n       </script>\n      '''
             elif sub[tmp]=="textarea":
              doc+='''\n       <div class="marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       <textarea class="width-100p editor" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''">'''
              try: doc+=str(decode(sub['value']))
              except Exception as e:               doc+=str(e)
              doc+='''</textarea>\n       </div>\n      '''
             elif sub[tmp]=="img-admin":
              doc+='''\n       <div class="d-inline-block pad-05 width-20 marg-05">\n         <img src="" class="width-100p hidden">\n         <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n         <select style="width:200px" class="width-20 img-admin" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''"  value="'''
              try: doc+=str(sub['value'])
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("depende='"+opcion+"'" if "depende" in sub else "")
              except Exception as e:               doc+=str(e)
              doc+=''' '''
              try: doc+=str('tabla="'+sub['tabla']+'"' if 'tabla' in sub else '')
              except Exception as e:               doc+=str(e)
              doc+=''' '''
              try: doc+=str('categoria="'+sub['categoria']+'"' if 'categoria' in sub else '')
              except Exception as e:               doc+=str(e)
              doc+=''' '''
              try: doc+=str('opcion="'+str(sub['opcion'])+'"' if 'opcion' in sub else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n          \n          '''
              try:
               if "opcion" in sub:
                doc+='''\n           \n           '''
                try:
                 for _k, opcion in enumerate(data["opciones"][sub['opcion']][1]):
                  doc+='''\n            <option value="'''
                  try: doc+=str(_k)
                  except Exception as e:                   doc+=str(e)
                  doc+='''" '''
                  try: doc+=str("selected" if sub['value']==_k else '')
                  except Exception as e:                   doc+=str(e)
                  doc+=''' >'''
                  try: doc+=str(decode(opcion))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n            '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n          '''
               elif "tabla" in sub:
                doc+='''\n           \n           '''
                try:
                 for _k,opcion in enumerate(data["tablas"][sub['tabla']]):
                  doc+='''\n           <option >'''
                  try: doc+=str(decode(opcion))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n           '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n          '''
               elif "subtabla" in sub:
                doc+='''\n           <!--subtabla es el nombre de la tabla -->\n\n           '''
                try:
                 for _fila in data["model"]["main"].obtenerFilas(sub['subtabla']):
                  doc+='''\n           <option >'''
                  try: doc+=str(decode(fila[0]))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n           '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n          '''
                pass
              except Exception as e: doc+=str(e)
              doc+='''\n\n         </select>\n\n         </div>\n     \n      '''
             elif sub[tmp]=="textarea-admin" and data["login"]==True:
              doc+='''\n       <div class="marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       <textarea class="width-100p editor" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''">'''
              try: doc+=str(decode(sub['value']))
              except Exception as e:               doc+=str(e)
              doc+='''</textarea>\n       </div>\n      '''
             elif sub[tmp]=="select":
              doc+='''\n       \n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       <select  style="width:200px" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''"  value="'''
              try: doc+=str(sub['value'])
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("depende='"+opcion+"'" if "depende" in sub else "")
              except Exception as e:               doc+=str(e)
              doc+=''' '''
              try: doc+=str('tabla="'+sub['tabla']+'"' if 'tabla' in sub else '')
              except Exception as e:               doc+=str(e)
              doc+=''' '''
              try: doc+=str('categoria="'+sub['categoria']+'"' if 'categoria' in sub else '')
              except Exception as e:               doc+=str(e)
              doc+=''' '''
              try: doc+=str('opcion="'+str(sub['opcion'])+'"' if 'opcion' in sub else '')
              except Exception as e:               doc+=str(e)
              doc+='''>\n        \n        '''
              try:
               if "opcion" in sub:
                doc+='''\n         \n         '''
                try:
                 for _k, opcion in enumerate(data["opciones"][sub['opcion']][1]):
                  doc+='''\n          <option value="'''
                  try: doc+=str(_k)
                  except Exception as e:                   doc+=str(e)
                  doc+='''" '''
                  try: doc+=str("selected" if sub['value']==_k else '')
                  except Exception as e:                   doc+=str(e)
                  doc+=''' >'''
                  try: doc+=str(decode(opcion))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n          '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n        '''
               elif "tabla" in sub:
                doc+='''\n         \n         '''
                try:
                 for _k,opcion in enumerate(data["tablas"][sub['tabla']]):
                  doc+='''\n         <option >'''
                  try: doc+=str(decode(opcion))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n         '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n        '''
               elif "subtabla" in sub:
                doc+='''\n         <!--subtabla es el nombre de la tabla -->\n\n         '''
                try:
                 for _fila in data["model"]["main"].obtenerFilas(sub['subtabla']):
                  doc+='''\n         <option >'''
                  try: doc+=str(decode(fila[0]))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n         '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n        '''
                pass
              except Exception as e: doc+=str(e)
              doc+='''\n\n       </select>\n\n       </div>\n      '''
             elif sub[tmp]=="select-admin":
              doc+='''\n       '''
              try:
               if data["login"]==True:
                doc+='''\n        <div class="d-inline-block pad-05 width-20 marg-05">\n        <label>'''
                try: doc+=str(tmp)
                except Exception as e:                 doc+=str(e)
                doc+='''</label>\n        <select style="width:200px" name="'''
                try: doc+=str(elem['name'])
                except Exception as e:                 doc+=str(e)
                doc+='''"  value="'''
                try: doc+=str(elem['value'])
                except Exception as e:                 doc+=str(e)
                doc+='''">\n         '''
                try:
                 for opcion in data["opciones"][elem['opcion']][1]:
                  doc+='''\n         <option>'''
                  try: doc+=str(decode(opcion))
                  except Exception as e:                   doc+=str(e)
                  doc+='''</option>\n         '''
                  pass
                except Exception as e: doc+=str(e)
                doc+='''\n        </select>\n        </div>\n        '''
                pass
              except Exception as e: doc+=str(e)
              doc+='''\n      '''
             elif sub[tmp]=="file":
              doc+='''\n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <label>'''
              try: doc+=str(tmp)
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       <img src="" class="width-100p hidden">\n       <input type="'''
              try: doc+=str(sub[tmp])
              except Exception as e:               doc+=str(e)
              doc+='''" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(sub['value'])
              except Exception as e:               doc+=str(e)
              doc+='''" class="img-file">\n       </div>\n      '''
             elif sub[tmp]=="number":
              doc+='''\n       <div class="d-inline-block pad-05 width-20 marg-05">\n       <label>'''
              try: doc+=str(decode(tmp))
              except Exception as e:               doc+=str(e)
              doc+='''</label>\n       <input type="'''
              try: doc+=str(sub[tmp])
              except Exception as e:               doc+=str(e)
              doc+='''" name="'''
              try: doc+=str(sub['name'])
              except Exception as e:               doc+=str(e)
              doc+='''" value="'''
              try: doc+=str(decode(sub['value']))
              except Exception as e:               doc+=str(e)
              doc+='''" '''
              try: doc+=str("step='"+sub['step']+"'" if "step" in sub else "")
              except Exception as e:               doc+=str(e)
              doc+='''>\n       </div>\n       \n       \n       '''
              pass
            except Exception as e: doc+=str(e)
            doc+='''\n      '''
            pass
          except Exception as e: doc+=str(e)
          doc+='''\n     '''
          pass
        except Exception as e: doc+=str(e)
        doc+='''\n    </div>\n    '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n    \n   '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n  </div>\n  </div>\n \n\n \n '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n \n<script type="text/javascript">\n        tinymce.init({\n   language : 'es',\n   selector: "textarea.editor",\n    theme: "modern",\n    plugins: [\n         "advlist autolink link image lists charmap =preview hr anchor pagebreak table",\n         "searchreplace wordcount visualblocks visualchars fullscreen insertdatetime media nonbreaking emoticons textcolor",\n         "save table contextmenu directionality emoticons template paste textcolor",\n         "code codesample"\n   ],\n   codesample_languages: [\n        {text: 'HTML/XML', value: 'markup'},\n        {text: 'JavaScript', value: 'javascript'},\n        {text: 'CSS', value: 'css'},\n        {text: 'PHP', value: 'php'},\n        {text: 'Ruby', value: 'ruby'},\n        {text: 'Python', value: 'python'},\n        {text: 'Java', value: 'java'},\n        {text: 'C', value: 'c'},\n        {text: 'C#', value: 'csharp'},\n        {text: 'C++', value: 'cpp'}\n    ],\n   content_css: "'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/tinymce/js/tinymce/skins/lightgray/content.min.css",\n   toolbar: "insertfile undo redo preview | fontselect | fontsizeselect | forecolor backcolor emoticons | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | media fullpage code codesample", \n    fontsize_formats: "9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 18pt 20pt 22pt 24pt",\n    \n\n font_formats: "Andale Mono=andale mono,times;"+\n        "Arial=arial,helvetica,sans-serif;"+\n        "Arial Black=arial black,avant garde;"+\n        "Book Antiqua=book antiqua,palatino;"+\n        "Comic Sans MS=comic sans ms,sans-serif;"+\n        "Courier New=courier new,courier;"+\n        "Georgia=georgia,palatino;"+\n        "Helvetica=helvetica;"+\n        "Impact=impact,chicago;"+\n        "Symbol=symbol;"+\n        "Tahoma=tahoma,arial,helvetica,sans-serif;"+\n        "Terminal=terminal,monaco;"+\n        "Times New Roman=times new roman,times;"+\n        "Trebuchet MS=trebuchet ms,geneva;"+\n        "Verdana=verdana,geneva;"+\n        "Webdings=webdings;"+\n        "Wingdings=wingdings,zapf dingbats",\n });   \n</script>\n\n\n'''