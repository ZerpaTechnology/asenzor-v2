doc+='''<head>\n	 <title>Personalizador</title>\n <meta charset="utf-8">\n   <meta http-equiv="pragma" content="no-cache">\n	\n	<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-3.1.0.js"></script>\n	\n  <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/bootstrap.css">\n  \n	<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/jquery.mCustomScrollbar.css" />\n <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.mCustomScrollbar.js"></script>\n <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-ui-1.12.1.custom/jquery-ui.js"></script>\n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/script/file=Config.js&manager=True"></script>\n  \n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/Codificador.js"></script>\n  \n  <!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/nuclear.by"></script>-->\n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/py_datos.js"></script>\n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/nuclear.js"></script>\n   <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">\n<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''/Components/css/Components.css">\n<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/flexboxgrid.css">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n  <!-- Link Swiper's CSS -->\n'''
try:
 if "vars" in data:
  doc+='''\n\n'''
  try:
   for elem in data["vars"]:
    doc+="""\n<var name='"""
    try: doc+=str(elem)
    except Exception as e:     doc+=str(e)
    doc+="""' style="display: none">"""
    try: doc+=str(decode(str(data["vars"][elem])))
    except Exception as e:     doc+=str(e)
    doc+='''</var>\n'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</head>'''