doc+='''<div class="campoForm">\n\n'''

"""
"depende" hace referencia al valor de otro campo

"subtabla" actualiza su valor en referencia a una tabla fon el formato de la tabla opciones 
generalmente se aplica a esta, valor es el indice de valores de esta subtabla, los campos con este
atributo deben ser actualizados al producir un evento change

Opciones [tabla,subtabla,[valor...] ]
"""

doc+='''\n\n<div style="background-color:rgb(200,200,200);padding: 10px;margin: 5px">\n<input type="checkbox" name="seleccion" style="margin-top:10px ">\n<div class="d-inline-block">\n<label> Tipo</label>\n  <select name="tipo">\n  	<option>text</option><!-- input de text -->\n  	<option>text-admin</option><!-- input de text que cambia a span en el user -->\n  	<option>text-email</option><!-- input de email-->\n  	<option>text-phone</option><!-- input de telefono-->\n  	<option>text-titulo</option><!-- input de text que cambia el nombre de la seccion en el admin y es texto en el span o h en el user-->\n  	<option>textarea</option> <!-- textarea tyminice  en admin -->\n  	<option>textarea-admin</option><!-- textarea tyminice  en admin cambia a contenido en el user-->\n  	<option>select</option><!-- simple campo de select -->\n  	<option>select-img</option><!-- simple campo de select -->\n  	<option>media</option><!-- despliega el popup de la biblioteca multimedia -->\n  	<option>img</option><!-- es una etiquete img -->\n  	<option>img-admin</option><!--muestra una image en el dashboard al ser seleccionada por un select \n    -->\n    <option>number</option>\n  	<option>fixed</option><!-- texto fijo tanto para el user como el admin-->\n  	<option>file</option><!-- campo que permite subir un archivo-->\n    <option>file-img</option><!-- campo que permite subir una imagen y previsualizarla-->\n  	<!--<option>list</option>-->\n  </select>\n</div>\n<div class="d-inline-block">\n <label> Nombre</label>\n <input type="text" name="name">\n </div>\n <div class="d-inline-block">\n <label> Titulo</label>\n <input type="text" name="titulo">\n <label> Valor</label>\n </div>\n   <div class="d-inline-block">\n   <input type="text" name="value">\n   <label> Opcion</label>\n   </div>\n   <div class="d-inline-block">\n   <select name="opcion">\n   	<option></option>\n    '''
try:
 for k,elem in enumerate(data["opciones"]):
  doc+='''\n   	<option>'''
  try: doc+=str(k)
  except Exception as e:   doc+=str(e)
  doc+='''</option>\n    '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n   </select>\n   </div>\n <div class="d-inline-block">\n <label>Opciones</label>\n <select name="opciones">\n <option></option>\n \n    '''
try:
 for elem in data["opciones"]:
  doc+='''\n    <option>'''
  try: doc+=str(elem)
  except Exception as e:   doc+=str(e)
  doc+='''</option>\n    '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n \n </select>\n </div>\n   \n <div class="d-inline-block">\n <label>Tabla</label>\n <select name="tabla">\n <option></option>\n '''
try:
 if "tablas" in data:
  doc+='''\n    '''
  try:
   for tabla in data["tablas"]:
    doc+='''\n   	<option>'''
    try: doc+=str(tabla)
    except Exception as e:     doc+=str(e)
    doc+='''</option>\n    '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n </select>\n </div>\n <div class="d-inline-block">\n <label>Depende</label>\n <input name="depende">\n 	<option></option>\n  '''
try:
 if "campos" in data:
  doc+='''\n    '''
  try:
   for campo in data["campos"]:
    doc+='''\n   	<option>'''
    try: doc+=str(campo)
    except Exception as e:     doc+=str(e)
    doc+='''</option>\n    '''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n  '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n </select>\n </div>\n <div class="d-inline-block">\n <label>min</label>\n <input type="number" name="min" step="0.00000001">\n </div>\n <div class="d-inline-block">\n <label>max</label>\n <input type="number" name="max" step="0.00000001">\n </div>\n <div class="d-inline-block">\n <label>step</label>\n <input type="number" name="step" step="0.00000001">\n</div>\n </div>\n</div>\n'''