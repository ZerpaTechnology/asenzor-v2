doc+='''<sidebar class="col-md-2 col-sm-2 pad-1  z-index10 font-ubuntu" id="menu" style="height:90%;position: fixed;top: 40px; left:0;background-color:#3f3f3f">\n<style type="text/css">\n  #main-menu span[name='menu']{\n  background-color:rgb(50,55,60);\n  color:white;\n  border-color: rgb(30,30,30);\n  cursor: pointer;\n  }\n  #main-menu span[name='menu']:hover{\n    background-color:rgb(60,65,70);\n  }\n</style>\n<div style="height:90%" class="scrollbar">\n  \n  <div class="text-center bg-gray">\n  <div class="b-s2 pad-1 b-r5">\n    <form action="'''
try: doc+=str(config.base_url+settings.app+'/'+data['control'])
except Exception as e: doc+=str(e)
doc+='''/Salir" method="post" class="d-inline-block"> \n     <input type="submit" value="Salir" class="btn bg-blue white">\n    </form>   \n     <div class="height-8 b-s1 b-r5 d-inline-block">\n     \n      <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Avatares/'''
try: doc+=str(data['opciones']['archivos'][1][1][data['user']['avatar']])
except Exception as e: doc+=str(e)
doc+='''" class="height-8" >\n     </div>\n    \n    <h4>'''
try: doc+=str(data['user']["usuario"])
except Exception as e: doc+=str(e)
doc+='''</h4>\n    '''
try: doc+=str(data['user']["email"])
except Exception as e: doc+=str(e)
doc+='''  \n  </div>\n  \n  <div id="main-menu">\n    \n    '''
try:
 for menu in data["adminMenu"]:
  doc+='''\n      '''
  titulo=menu[0]
  doc+='''\n\n      <div>\n      <span style="display: block; padding: 10px 5px;" class="b-s1 text-justify" name="menu">\n      <img src="'''
  try: doc+=str(config.base_url)
  except Exception as e:   doc+=str(e)
  doc+='''static/imgs/iconos/'''
  try: doc+=str(menu[3])
  except Exception as e:   doc+=str(e)
  doc+='''" class="height-2"> \n      '''
  try: doc+=str(titulo)
  except Exception as e:   doc+=str(e)
  doc+='''</span>\n      <ul name="submenu" class="hidden">\n      '''
  try:
   for sub in menu[2]:
    doc+='''\n        \n        \n        '''
    try:
     if sub[1][0]!=None:
      doc+='''\n\n          '''
      try:
       if type(normalizar(decode(str(sub[1][1]['valor']))))==str:
        doc+='''\n            '''
        url=urlBuilder(config,settings.app,"admin","",decode(str(sub[1][1]['valor'])),action=sub[1][0])
        doc+='''\n            \n          '''
       elif type(normalizar(decode(str(sub[1][1]['valor']))))==dict:
        doc+='''\n          \n            '''
        url=urlBuilder(config,settings.app,"admin","",action=sub[1][0],kwargs=decode(str(sub[1][1]['valor'])))
        doc+='''\n          \n          '''
       elif type(normalizar(decode(str(sub[1][1]['valor']))))==list:
        doc+='''\n          \n            '''
        url=urlBuilder(config,settings.app,"admin","",args=normalizar(decode(str(sub[1][1]['valor']))),action=sub[1][0])
        doc+='''\n          '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n      \n        '''
     else:
      doc+='''\n            '''
      url=urlBuilder(config,settings.app,'admin','')
      doc+='''\n            '''
      try:
       if type(sub[1][1]['valor'])==dict:
        doc+='''\n              '''
        data["actionNew"][sub[1][1]['valor'].keys()[0]]=config.base_url+data['actionbase']+'&action='+sub[1][0]+'&args='+decode(str(sub[1][1]['valor']) ) if sub[1][1]['valor'][sub[1][1]['valor'].keys()[0]]==None else None
        doc+='''\n        \n            '''
       elif type(sub[1][1]['valor'])==list:
        doc+='''\n              '''
        url=urlBuilder(config,settings.app,'admin','',args=normalizar(decode(str(sub[1][1]['valor']) ) ))
        doc+='''\n\n          '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n        '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n      \n        <li class="pad-05"><a href="'''
    try: doc+=str(url)
    except Exception as e:     doc+=str(e)
    doc+='''">'''
    try: doc+=str(sub[0])
    except Exception as e:     doc+=str(e)
    doc+='''</a>\n        </li>\n      \n      \n      '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n      \n      </ul>\n      </div>\n    \n    '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n    \n  </div>\n  </div>\n  </div>\n  \n  \n\n </sidebar>\n\n'''