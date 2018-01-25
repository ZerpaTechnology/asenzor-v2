#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div >
<form>
<h2>Plugins</h2>
<input type="file" name="webapp" value="subir app" id="subir-app">
<div class="ff hidden" id="detalles">
	<p></p>
	<button class="btn bg-blue white b-r5" name="btn-instalar">Instalar</button>
</div>
</form>
<div class="bg-gray font-ubuntu pad-l05 font-s14">
	<style type="text/css">
	.btn-webapps:hover{
	color:#00a0d2;
	cursor: pointer;
	}
		
	</style>

	<span style="border: solid; border-color: transparent;" class="btn-webapps">Instaladas</span>
	<div class="d-inline-block bg-ubuntu_ash pad-05">
	<b class="" style="color:rgb(155,0,0);">Nuevo: </b>
	<div class="d-inline-block bg-gray pad-1">
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Destacadas</span>	
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Populares</span>	
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Recientes</span>	
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Favoritos</span>		
	</div>
	
	</div>
	<input type="search" name="" placeholder="Buscar webapps" style="height:30px">
	
	
</div>
<div class="tab">
'''
for plugin in data["plugins-list"]:
  doc+="""
<span class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-100p" style="background-image: url('"""
  try: doc+=str(config.base_url+config.plugins_folder+plugin)
  except Exception, e:   doc+=str(e)
  doc+='''/screenshot.png');background-size: cover; background-position: center;">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class=""> '''
  try: doc+=str(plugin)
  except Exception, e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1">Activar/Desactivar</button>
		<button>Actualizar</button>
	</div>
</span>
'''
  pass
doc+='''

</div>
<div class="tab">
</div>
<div class="tab">
</div>
<div class="tab">
</div>
<div class="tab">
</div>
<div class="tab">
</div>
</div>
<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/plugins.by"></script>'''