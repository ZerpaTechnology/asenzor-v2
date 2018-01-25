#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<div id="chatContactList" class="'''+str('hidden' if  'hidden' in data and 'chatContactList' in data['hidden'] else '' )+'''">  <style>    #chatContactList{      width:200px;    }    #buscar{      background-color:white;      color:black;      width:100%;    }    #chatContactList .mensajes{      height:250px;    }    #chatContactList .contact-link    {      cursor:pointer;    }        '''
if "css" in data and "chatContactList" in  data["css"]:
  print '''      '''+str(data["css"]["chatContactList"])  +'''    '''
elif "style" in data and "chatContactList" in  data["style"]:
  print '''      '''
  for selector in data["style"]["chatContactList"]:
    print '''        '''+str(selector)    +''' {        '''
    for estilos in data["style"]["chatContactList"][selector]:
      print '''          '''+str(estilos)      +''' : '''+str(data["style"]["chatContactList"][selector][estilos])      +''' ;        '''
      pass
    print '''                      '''
    pass
  print '''            '''
  pass
print '''  </style>  <div class="bg-ubuntu_blue pad-05 text-center">    <span>'''+str( "Contactos")+'''</span>      </div>  <div style="overflow-y:scroll" class="bg-white mensajes">    <ul>      '''
if "contactos" in data:
  print '''      '''
  for elem in data["contactos"]:
    print '''      <li><a class="contact-link"><img src="'''+str(data['base_url'])    +'''..static/archivos/Avatares/'''+str(opciones[1][elem['avatar']] )    +'''"> <span>'''+str(elem["nombre"])    +'''</span></a></li>      '''
    pass
  print '''      '''
  pass
print '''    </ul>  </div>  <input type="search" placeholder="Buscar... " id="buscar"></div>'''