db=DB()
#============================================
#TABLA de opciones
db("Opciones").campo("Nombre",db.str)
db("Opciones").campo("Valores",db.list)
db("Opciones").insertar("Becas",["Empresarial","Política","Preparaduria","Trabajo"])
#=============================================
db("Plantillas").campo("Nombre",db.str)
db("Plantillas").campo("Contenido",db.list)
db("Plantillas").campo("args",db.dict)
db("Plantillas").campo("Fecha",db.str)
db("Plantillas").campo("Status",db.list)
#============================================
db("Shortcodes").campo("Nombre",db.str)
db("Shortcodes").campo("Contenido",db.list)
db("Shortcodes").campo("args",db.dict)
db("Shortcodes").campo("Fecha",db.str)
db("Shortcodes").campo("Status",db.list)
#--------------------------------------------
db('Plantillas').insertar('Shortcodes', [[{'Nombre': 'titulo', 'name': 'titulo', 'value': 'sc-'}, {'ext': 'py', 'Controlador': 'textarea-code', 'name': 'controlador', 'value': """
from modulos.Plugin import Shortcode

from config import config

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		

		
	def run(self,atts,content):
		return 'hola soy tu Shortcode'

	"""}, {'ext': 'html', 'Dise\xc3\xb1o': 'textarea-code', 'name': 'layout', 'value': '<div></div>'}]], {'Plantilla': 0}, '1/12/2017 10:6:39', [])

#--------------------------------------------
db("Shortcodes").insertar("sc-galeria",[
	[{"Nombre":"titulo","name":"titulo","value":"sc-galeria"},
	 {"Controlador":"textarea-code","name":"controlador","value":"""
from modulos.Plugin import Shortcode

from config import config
from settings import config as settings

class shortcode(Shortcode):
	def __init__(self,plugin,contendor=False):
		Shortcode.__init__(self,plugin,contendor)
		self.widget="galeria"
        #mi comentario
		

		
	def run(self,atts,content):
		self.plugin.data["galeria"]=self.plugin.model["galerias"].obtenerFilas("Galerias")[atts["id"]]

		return self.incluir(self.plugin.data)
	 ""","ext":"py"},
	 {"Diseño":"textarea-code","name":"layout","value":"""
<style type="text/css">
.zslider{
	position: relative;
	background: black;
}
.f-left{
  position: absolute;
  
  font-size: 50px;
  color: blue;
  top:45%;
  left: 0;
  cursor: pointer;

  

  z-index: 200;
 }
  .exit{
  
  font-size: 30px;
  color: white;
  position: absolute;
  right: 0px;
  top: 0px;
  cursor: pointer;


 }
.f-right{
  
  position: absolute;
  
  font-size: 50px;
  color: blue;
  
  right: 5%;top: 45%;
  right: 0;
  z-index: 200;
  cursor: pointer;
   }
</style>

<div>
<script type="text/python3" src="{{=config.base_url}}static/brython/decode.by"></script>
<script type="text/python3" src="{{=config.base_url}}static/script/file=config.by&manager=True"></script>
<script type="text/python3" src="{{=config.base_url}}static/brython/nuclear.by"></script>
<script type="text/python3" src="{{=config.base_url}}static/brython/galeria.by"></script>

<div class="zslider" style="position: relative;width:400px;height: 400px">

	<div class="content " style="height: 400px;overflow: hidden;">
	{{for k, elem in enumerate(data["galeria"][1][1]):}}
		{{img=data['opciones'][elem['opciones']][0][1][elem['value']]}}
		<img src="{{=config.base_url+config.apps_folder+settings.app+'/admin/'+routes.static_folder}}archivos/Imagenes/{{=img}}"
		style="max-height:100%;max-width: 100%;vertical-align: center" >

	{{pass}}
</div>
  <div class="f-left"><img src="{{=data['base_url']}}../admin/static/archivos/Imagenes/f1.png"  class="height-5"></div>
  <div class="f-right"><img src="{{=data['base_url']}}../admin/static/archivos/Imagenes/f2.png"  class="height-5"></div>
</div>


<script type="text/python3">
from browser import window
window.Slider(".zslider")	
</script>

</div>
	 ""","ext":"html"},
	],
	
	],
	{"Shortcode":0},
	zu.DateTime(),
	[]
	)
db('Shortcodes').insertar('sc-base_route', [[{'Nombre': 'titulo', 'name': 'titulo', 'value': 'sc-base_route'}, {'ext': 'py', 'Controlador': 'textarea-code', 'name': 'controlador', 'value': 'from modulos.Plugin import Shortcode\r\n\r\nfrom config import config\r\nfrom settings import config as settings\r\n\r\nclass shortcode(Shortcode):\r\n\tdef __init__(self,plugin,contendor=False):\r\n\t\tShortcode.__init__(self,plugin,contendor)\r\n\t\t\r\n\r\n\t\t\r\n\tdef run(self,atts,content):\r\n\t\treturn config.base_url+config.apps_foler+settings.app+"/"'}, {'ext': 'html', 'Dise\xc3\xb1o': 'textarea-code', 'name': 'layout', 'value': '<div></div>'}]], {'Shortcode': 2}, '1/12/2017 20:59:7', [{'name': 'control', 'value': 'Inicio'}, {'name': 'layout', 'value': 'Ninguno'}])