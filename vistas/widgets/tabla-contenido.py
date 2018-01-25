doc+='''\n<div class="content">\n'''
c=0#cuenta indece de todos los elementos
doc+='''\n'''
item=0#cuenta el indice del elemento en la tabla activa
doc+='''\n'''
pag_current=1#cuenta la pagina actual
doc+='''\n'''
try:
 while c< len(data["listar"]):
  doc+='''\n  '''
  elem=data["listar"][c]
  doc+='''\n  \n  '''
  try:
   if item==0:
    doc+='''\n  \n    <div class="'''
    try: doc+=str('' if data['pag']==pag_current else 'hidden')
    except Exception as e:     doc+=str(e)
    doc+='''">\n    <table class="table" >\n    <tr>\n       <th><input type="checkbox" name=""></th>\n       '''
    try:
     for h in data["table-headers"]:
      doc+='''\n      <th>'''
      try: doc+=str(decode(h))
      except Exception as e:       doc+=str(e)
      doc+='''</th>\n      '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n    </tr>\n\n    '''
    item=1
    doc+='''\n  '''
   elif item<=data['n-pag']:
    doc+='''\n    <tr>\n      <td><input type="checkbox" name=""></td>\n      '''
    key=list(elem[2])[0]
    doc+='''\n      <td><a href="'''
    try: doc+=str(config.base_url+data['app']+'/admin/'+('Plugin/'+data['args'][0]+'/' if data['metodo']=='Plugin' else '')+key+'/'+str(elem[2][key])+'/action=editar' )
    except Exception as e:     doc+=str(e)
    doc+='''">'''
    try: doc+=str(decode(elem[0]))
    except Exception as e:     doc+=str(e)
    doc+='''</a></td>\n      <td>'''
    try: doc+=str(elem[3])
    except Exception as e:     doc+=str(e)
    doc+='''</td>\n      <td></td>\n      </tr>\n      \n      '''
    item+=1
    doc+='''\n      '''
    c+=1
    doc+='''\n\n    \n  '''
   else:
    doc+='''\n\n    </table>\n    </div>\n      '''
    item=0
    doc+='''\n      '''
    pag_current+=1
    doc+='''\n  '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n  \n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</table>\n    </div>\n</div>'''