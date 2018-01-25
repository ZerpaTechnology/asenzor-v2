#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div >
<form target="iframeUpload" method="post" enctype="multipart/form-data" action="'''
try: doc+=str(config.base_url+config.controller_folder)
except Exception, e: doc+=str(e)
doc+='''post.py" id="form-upload">
<h2>Webapps</h2>
<input type="file" name="upload" value="subir app" id="subir-app">
<input type="hidden" name="action" value="upload">
<input type="hidden" name="nombre" value="" >
<div class="ff hidden" id="detalles">
	<p></p>
	
</div>
</form>
<iframe name="iframeUpload" class="hidden" style="height: 50px;border: none;"></iframe>
<button class="btn bg-blue white b-r5 hidden d-block" name="btn-instalar">Instalar</button>

<div class="bg-gray font-ubuntu pad-l05 font-s14" id="gestor">
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
for app in data["webapps"]:
  doc+='''
<div class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception, e:   doc+=str(e)
  doc+=''');">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class=""> '''
  try: doc+=str(app[0])
  except Exception, e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="'''
  try: doc+=str('activar' if 'Desactivada' in app[4] else 'desactivar')
  except Exception, e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str("Activar" if "Desactivada" in app[4] else "Desactivar")
  except Exception, e:   doc+=str(e)
  doc+='''</button>
		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception, e:   doc+=str(e)
  doc+='''
	</div>
</div>
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
doc+='''static/brython/allapps.by"></script>
<script type="text/python3">
from browser import window
window.Gestor("#gestor")
</script>'''