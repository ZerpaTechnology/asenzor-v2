doc+='''<style type="text/css">\n	#media-field{\n		border: solid;\n		border-width: 1px;\n		margin: 10px;\n	}\n	#media-field .btn-cerrar{\n		border: solid;\n		border-width: 1px;\n		display: inline-block;\n		position: absolute;\n		height: 30px;\n		width: 30px;\n		cursor: pointer;\n		right:10px;\n		top:0px;\n		padding: 5px;\n		text-align: center;\n	}\n	#media-field .item{\n		background-color: black;\n		height: 200px;\n		width:200px;\n		display: inline-block;\n		margin: 2px;\n\n		cursor: pointer;\n\n		/*border-color:rgb(100,150,200);*/\n		position: relative;\n		background-size: cover;\n	}\n	#media-field .marcar{\n		/*background-color: rgb(200,200,200);*/\n		/*background-color:rgb(100,150,200);*/\n		/*border: solid;*/\n		/*border-color:white;*/\n		height: 20px;\n		width:20px;\n		display: inline-block;\n		position: absolute;\n		top:-10px;\n		right:-10px;\n		\n		border-width: 1px;\n	}\n	#media-field .item.activo{\n		border:solid;\n		border-color:rgb(100,150,200);\n\n	}\n	#media-field .item.activo .marcar{\n		\n		background-color:rgb(100,150,200);\n		border: solid;\n		border-width: 1px;\n		border-color:white;\n	}\n	#media-field .item.marcado{\n		border:solid;\n		border-width: 5px;\n		border-color:rgb(200,200,200);\n	}\n	#media-field .item.marcado .marcar{\n		background-color: rgb(200,200,200);\n		/*background-color:rgb(100,150,200);*/\n		border: solid;\n		border-width: 1px;\n		border-color:white;\n	}\n</style>\n<div id="media-field">\n	<div>\n		<h1>Insertar medios</h1>\n		<span class="btn-cerrar">x</span>\n		<div>\n			<span href="#tab-1" class="btn btn-info">Subir archivo</span>\n			<span href="#tab-2" class="btn btn-info">Biblioteca de medios</span>\n		</div>\n	</div>\n	<div class="content">\n		<div id="tab-1" class="bg-white hidden" >\n\n			\n		</div>\n		<div id="tab-2">\n			<div class="container-fluid">\n				<div class="row">\n				<div class="col-md-8 bg-white" style="max-height: 400px;overflow-y: scroll;padding: 10px">\n					'''
try:
 for elem in data["model"]["archivos"].obtenerFilas("Archivos"):
  doc+='''\n					'''
  content=data["model"]["archivos"].contener(elem[1])
  doc+='''\n					'''
  try:
   if "enlace" in content[0]:
    doc+="""\n					<span class="item" style="background-image: url('"""
    try: doc+=str(content[0]['enlace']['value'])
    except Exception as e:     doc+=str(e)
    doc+='''');" \n					    size="" \n					    enlace="'''
    try: doc+=str(content[0]['enlace']['value'])
    except Exception as e:     doc+=str(e)
    doc+='''"\n					    name="'''
    try: doc+=str(content[0]['renombre']['value'])
    except Exception as e:     doc+=str(e)
    doc+='''"\n					    >\n						<span class="marcar"></span>\n					</span>\n					'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n					'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n					\n				</div>\n				<div class="col-md-4" style="max-height: 400px;overflow-y: scroll;">\n				<div>\n				<img src="" class="media-preview" >\n				<p>Nombre de archivo: 2017-09-19-PHOTO-00000389.jpg</p>\n				<p>Tipo de archivo: image/jpeg</p>\n				<p>Subido el: 20 Septiembre, 2017</p>\n				<p>Tamaño de archivo: 129 KB</p>\n				<p>Dimensiones: 956 × 1280</p>\n				</div>\n				<table>\n					<tr>\n						<td><label>Url</label></td>\n						<td><input type="" name="url"></td>\n					</tr>\n					<tr>\n						<td><label>Titulo</label></td>\n						<td><input type="" name="nombre"></td>\n					</tr>\n					<tr>\n						<td><label>Tamaño</label></td>\n						<td><input type="" name="size"></td>\n					</tr>\n					<tr>\n						<td><label>Leyenda</label></td>\n						<td><textarea class="width-100p"></textarea></td>\n					</tr>\n					<tr>\n						<td><label>Texto alternativo</label></td>\n						<td><input type="" name="alternativo"></td>\n					</tr>\n					<tr>\n						<td><label>Descripción</label></td>\n						<td><input type="" name="descripcion"></td>\n					</tr>\n					<tr>\n						<td><label>Subido por</label></td>\n						<td><label>admin</label></td>\n					</tr>\n				</table>\n				\n					\n\n				</div>\n					\n				</div>\n				\n			</div>\n\n		</div>\n	</div>\n	<div class="container-fluid">\n		<div class="row">\n		<div class="col-md-11">\n			\n		</div>\n		<div class="col-md-1 text-right">\n		<button class="btn white bg-blue" name="insertar">Insertar</button>	\n		</div>\n			\n		</div>\n		\n	</div> \n</div>\n<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/script/file=config.by&manager=True"></script>\n<script type="text/python" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/decode.by"></script>\n<script type="text/python" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/nuclear.by"></script>\n<script type="text/python" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/media-field.by"></script>\n<script type="text/python">\nfrom browser import window\nwindow.Media("#media-field")\n</script>'''