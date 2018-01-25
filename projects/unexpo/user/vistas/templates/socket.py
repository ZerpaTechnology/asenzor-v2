#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html>    <html>  <head>    '''
incluir(data,"head")
print '''      </head >  <body onload="brython(1)">    <div style="overflow:scroll" >      <button id="openbtn" >Abrir</button>            <button id="sendbtn" disable>Enviar</button>      <button id="closebtn" disable>Cerrar</button>          </div>    <script type="text/python3" src="static/brython/websocket.by"></script>              </body></html>'''