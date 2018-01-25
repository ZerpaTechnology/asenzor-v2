#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html>\n'''

menu={"HOME":data["base_url"]+"vista=index",
   "ABOUT":data["base_url"]+"vista=about",
   "PORTAFOLIO":data["base_url"]+"vista=portafolio",
   "BLOG":data["base_url"]+"vista=blog",
   "CONTACTO":data["base_url"]+"vista=contacto",
  }


doc+='''\n'''
data["actionNew"]={} 
doc+='''\n'''
try:
 if data["action"]!="personalizar":
  doc+='''\n'''
  try: doc+=str(incluir(data,"head",isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+='''\n'''
 else:
  doc+='''\n'''
  try: doc+=str(incluir(data,"head2",isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n<body >\n<noscript>\n  <p>La página que estás viendo requiere para su funcionamiento el uso de JavaScript. \nSi lo has deshabilitado intencionadamente, por favor vuelve a activarlo.</p>\n</noscript>\n'''
try:
 if data["action"]!="personalizar":
  doc+='''\n'''
  try: doc+=str(incluir(data,"header"))
  except Exception as e:   doc+=str(e)
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n<div class="container-fluid text-center-xs sin-pad-xs" >\n<div class="row">\n'''
try:
 if data["action"]!="personalizar":
  doc+='''\n  '''
  try: doc+=str(incluir(data,"left-sidebar",isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+='''\n'''
 else:
  doc+='''\n  '''
  try: doc+=str(incluir(data,"sidebar-customize",isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n <div class="col-xs-12 '''
try: doc+=str('col-sm-offset-2  pad-1 pad-t5 pad-b5' if data['action']!='personalizar' else  '')
except Exception as e: doc+=str(e)
doc+=''' col-md-10 col-sm-10" id="content" style="background-color: rgb(240,240,240) !important;height: 90vh">\n <!--  HOME -->\n \n '''
try:
 if "hook1" in data and "action" in data and data["action"]!=None:
  doc+='''\n \n '''
  try: doc+=str(incluir(data,data["hook1"],isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+='''\n \n '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n\n '''
try:
 if "action" not in data or data["action"]==None:
  doc+='''\n <h2>Escritorio</h2>\n \n     <div>\n      <div class="d-inline-block b-s2" style="border-color:gray">\n      <div class="d-inline-block alg-top pad-1">\n      <div><p>Aplicación web:<b class="font-s30"> '''
  try: doc+=str(settings.app)
  except Exception as e:   doc+=str(e)
  doc+='''</b></p></div>\n      <img src="'''
  try: doc+=str(data['base_url'])
  except Exception as e:   doc+=str(e)
  doc+='''../screenshot.png" class="height-20">  \n      </div>\n\n      <div style="display: inline-block;">\n      <div class="d-inline-block pad-1 bg-gray">\n      '''
  try:
   if data["creditos"]!=[]:
    doc+='''\n          <p><b>Creditos</b></p>\n          '''
    logos=data["creditos"][0]['colaboraciones-imgs']["value"]
    doc+='''\n          \n          '''
    try:
     for elem in logos:
      doc+='''\n            <img src="'''
      try: doc+=str(data['base_url']+'../admin/static/archivos/Imagenes/'+elem)
      except Exception as e:       doc+=str(e)
      doc+='''" class="height-15">\n          '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n          <p>Aplicación web creada en\n          '''
    mades=data["creditos"][0]['hecho']["value"]
    doc+='''\n            '''
    try:
     for k,elem in enumerate(mades):
      doc+='''\n            <a href="'''
      try: doc+=str(mades[elem])
      except Exception as e:       doc+=str(e)
      doc+='''">'''
      try: doc+=str(elem)
      except Exception as e:       doc+=str(e)
      doc+='''</a>'''
      try: doc+=str("," if k<len(mades)-2  else " y " if k!=len(mades)-1 else "")
      except Exception as e:       doc+=str(e)
      doc+='''\n          '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n           </p>\n      \n          '''
    colaboraciones=data["creditos"][0]['colaboraciones']["value"]
    doc+='''\n          \n              '''
    try:
     for elem in colaboraciones:
      doc+='''\n              <p><b>'''
      try: doc+=str(elem)
      except Exception as e:       doc+=str(e)
      doc+='''</b>:\n                  '''
      try:
       for k,nombre in enumerate(colaboraciones[elem]):
        doc+='''\n                  <a href="mailto:'''
        try: doc+=str(colaboraciones[elem][nombre])
        except Exception as e:         doc+=str(e)
        doc+='''">'''
        try: doc+=str(nombre)
        except Exception as e:         doc+=str(e)
        doc+='''</a> '''
        try: doc+=str("," if k<len(colaboraciones[elem])-1 else "" )
        except Exception as e:         doc+=str(e)
        doc+='''\n                  '''
        pass
      except Exception as e: doc+=str(e)
      doc+='''\n              </p>\n              '''
      pass
    except Exception as e: doc+=str(e)
    doc+='''\n          <p>Para el framework <b>Azensor</b> un producto de <a href="https://zerpatechnology.com.ve">zerpatechnology</a></p>\n          <p>Este software se distribuye bajo la <a href="LICENSE">GNU LESSER GENERAL PUBLIC LICENSE</a></p>\n\n         </div>\n         </div>\n         '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n\n     '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n\n     \n         '''
try:
 if "action" in data and data["action"]=="licencias":
  doc+='''\n\n              <div class="bg-ubuntu_porcelain pad-1">\n                  <h2>Licencias</h2>\n                  <hr class="bg-ubuntu_red height-1">\n                  <p>Este software se distribuye bajo la <a href="LICENSE">GNU LESSER GENERAL PUBLIC LICENSE</a></p>\n                  <p>\n                   Varios de los contenidos multimedia usado en este framework son sacado de distintos sitios web's aquí compartimos las licencias que se nos han proporcionado para el uso de este continido.\n                  </p> \n                 <ul class="no-list-style pad-l2">\n\n                      '''
  try:
   for licencia in data["licencias"]:
    doc+='''\n                       <li><a href="'''
    try: doc+=str(config.base_url+"static/licencias/"+licencia)
    except Exception as e:     doc+=str(e)
    doc+='''">'''
    try: doc+=str(licencia)
    except Exception as e:     doc+=str(e)
    doc+='''</a></li>\n                      '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n                  </ul> \n        \n                \n               \n              </div>\n         '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n <div class="pad-1">\n\n Gracias por crear con <a href="http://zerpatechnology.com.ve/AsenZor">Asenzor</a>  \n </div>\n </div>\n</div>\n</div>\n'''
try:
 if data["action"]!="personalizar":
  doc+='''\n'''
  try: doc+=str(incluir(data,"footer",isglobal=True))
  except Exception as e:   doc+=str(e)
  doc+=''' \n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</body>\n</html>\n\n\n\n'''