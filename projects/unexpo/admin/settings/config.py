#!/usr/bin/python
# -*- coding: utf-8 -*-
libs_python=["ztec","functions"]
libs_php=[]
#aqui va el nombre de las bases de datos
dbs=["main","usuarios","formularios","paginas","archivos","conversaciones","ayuda","publicaciones","informaciones","anuncios"]
#variable para paso de parametros
serial="00001"
vistas=["index","noticias","galeria","layout1","layout2","logs","formulario","parallax","chat","socket"]
vistas_admin=["index","login","licencias"]
vista_default="index"
app="unexpo"
plugins=["pageCreator"]
consola=True
host="localhost"
consola_port=9999
mod_debug=True
ajax_file="ajax.json"
socket_default_controller="chat"
get_controllers=[]
get_custom_controllers=[]
websocket_controllers=[socket_default_controller]
custom_websocket_controllers=[]

post_controllers=[]

global_get_controllers=["documentation","configuracion","adminActions","adminShow","static","update","vistas2",]
global_get_controllers.append("vistas")
global_post_controllers=["adminUsuarios","documentation","adminDB","adminPage","adminForms","adminMenus","adminWrite",
      "adminArchivos","adminActions","adminShow","adminGaleria","static"]
post_custom_controllers=[]
get_php_controllers=[]
post_php_controllers=[]
admin_models_embebed={}
models_embebed={"usuarios":["login","closeSession"],"global":["isUser","login"]}
seo_url=True
static_dir="static"
lang="es"