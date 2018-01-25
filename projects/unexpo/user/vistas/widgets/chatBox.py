#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<div class="chat '''+str('hidden' if 'chat' in data['hidden'] else '' )+'''">  <style>      input,button{    font-size:13px;  }    .chat{    width:200px;    font-size:12px !important;          }  .chat textarea{    width:100%;      }   .chat .mensajes{      height:240px;    }  .conversador1{    text-align:left;  }  .conversador1 p{    background-color:rgb(200,200,250);    border-radius:30px 0px 30px 30px;    padding:8px;        display:inline-block;    margin:0px;  }  .yo{    text-align:right;  }  .yo p{    background-color:rgb(150,200,250);    border-radius:30px 30px 30px 0px;    padding:8px;        display:inline-block;    margin:0px;  }    .btn-closeChat{      cursor:pointer;      padding:5px;    }    .chatbox{      min-height:30px;    }</style>  <div class="bg-ubuntu_blue pad-05">    <span class="titulo">Usuario 1</span>    <div class="right">      <img src="'''+str(config.base_url)+'''static/imgs/iconos/005-add.png" class="height-1_5">      <img src="'''+str(config.base_url)+'''static/imgs/iconos/004-settings.png" class="height-1_5">      <span class="btn-closeChat">x</span></div>  </div>  <div style="overflow-y:scroll" class="bg-white mensajes">    <div>    '''
if "conversacion" in data:
  print '''      '''
  for elem in data["conversacion"]:
    print '''        '''
    if elem[0]=="conversador1":
      print '''        <div class="conversador1"><p>'''+str(elem[1])      +'''</p></div>        '''
    elif elem[0]=="yo":
      print '''        <div class="yo"><p >'''+str(elem[1])      +'''</p></div>                '''
      pass
    print '''      '''
    pass
  print '''    '''
  pass
print '''  </div>  </div>  <textarea class="chatbox">    hola  </textarea></div>'''