<div class="col-md-12">
<div class="b-s1 b-r5 b-gray pad-05">
<span>Selecciona un menu para editar </span>
 
<select class="bg-white" style="width: 200px" name="seleccionar-menu">

	'''
for elem in data["Menus"]:
  doc+='''
	<option>'''
  try: doc+=str(elem[0])
  except Exception, e:   doc+=str(e)
  doc+='''</option>
	'''
  pass
doc+='''
</select>
<button name="aplicar-menu">seleccionar</button>
o <a href="">crea un nuevo menu</a>
</div>
</div>