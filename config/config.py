#!/usr/bin/python
import os
proyectos=["default","ej"]#lista de proyectos en el framework
proyectos_disp=["unexpo"]#lista de proyectos habilitados
protocolo="http://"

host=protocolo+os.environ["SERVER_NAME"]+((":"+os.environ["SERVER_PORT"]) if  os.environ["SERVER_PORT"]!="80" else "")+"/" if "SERVER_NAME" in os.environ else ""

host_folder="htdocs"#public_html
if  "SERVER_NAME" in os.environ:

	fmk_dir=os.getcwd().replace("\\","/").split("/")[-2] if os.getcwd().replace("\\","/").split("/")[-2]!=os.environ["SERVER_NAME"] and  os.getcwd().replace("\\","/").split("/")[-2]!="public_html" else ""
	
	fmk_url=fmk_dir+"/"

	base_url=host+fmk_url if fmk_url!="/" else host
	logs=base_url+"log.txt"
	host_folder="public_html"

modelos_dir="modelos"
modelos_folder=modelos_dir+"/"

default_project="default"
request_folder=modelos_folder+"request/"

dbs=["main"]#base de datos globales

libs_folder="modulos/"
libs=["ztec"]#librerias cargadas en el framework
mod_debug=False
apps_dir="apps"
controller_folder="cgi-bin/"
settings_folder="settings/"
default_controller="default"
apps_folder=apps_dir+"/"
projects_dir="projects"
projects_folder="projects/"
static_dir="static"
static_folder=static_dir+"/"
vistas_dir="vistas"
vistas_folder=vistas_dir+"/"

lengs=["es","en"]
leng_default=["es"]


base_root=os.path.abspath(__file__[:-len("/config.py")]+"/../").replace("\\","/")+"/"


	

default_app="unexpo"
default_controller="default.py"
controles_dir="controles"
controller_url=controles_dir+"/"+default_controller
lanzador_dir="controles"
lanzador_default="lanzador.py"
lanzador_url=lanzador_dir+"/"+lanzador_default
templates_folder="templates/"
vistas=["default"]#lista de todos la vistas html sin codigo python embebido
templates=[]#lista de todos los templates (vistas con codigo python embebido y widgets)
widgets=[]#lista con todos los widgets(templates minimalistas)
vistas_disp=["default","PamaxAgency"]#lista con las vistas disponibles para mostrar
templates_disp=[]#lista con los templates disponibles para mostrar
widgets_disp=[]#lista con los widgets disponibles para mostrar
custom_url=None
proyecto="default"#proyecto actual
error=False
controller_vista="vista.py"
plugins_dir="plugins"
plugins_folder=plugins_dir+"/"
main_libs_url=base_root+libs_folder
main_libs_url_relative="../"+libs_folder
consola=True
seo_url=True
apps=[]

update_dir="update"

update_folder=update_dir+"/"
global_dir="globals"
global_folder=global_dir+"/"
notifications_controller="notifications"
controladores=[static_dir,apps_dir,notifications_controller,"plugins","Plugin"]
controller_global_dir="globals"
controller_global_folder=controller_global_dir+"/"
versiones_disponibles=["0.0.1","0.0.2"]
notfound=False
asenzor_host=protocolo+"localhost/PTC/"
post=base_url+controller_folder+"post.py"
folder_donwloads="download/"
widgets_folder="widgets/"
version="0.0.1"
admin="admin"#es el nombre del control para el administrador
licencias=[
"license.html",
"license.pdf",
"license2.html",
"license2.pdf",
"license3.html",
"license3.pdf",
"license4.pdf",
"license5.pdf",
"noun_138581_cc.png",
]
for elem in os.listdir(base_root+apps_folder):
	if os.path.isdir("../"+apps_folder+elem):
		apps.append(elem)
