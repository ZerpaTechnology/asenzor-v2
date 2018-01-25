doc+='''<head>\n <title>Administrador</title>\n <meta charset="utf-8">\n   <meta http-equiv="pragma" content="no-cache">\n <link rel="icon" type="image/png" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/logos/logoZtec.png" />\n <link rel="shortcut icon" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/logos/logoZtec.png" />\n <script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-3.1.0.js"></script>\n <link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/jquery.mCustomScrollbar.css" />\n <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.mCustomScrollbar.js"></script>\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/estilos.css">\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/bootstrap.css">\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/flexboxgrid.css">\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/ff.css">\n \n \n <link href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/perfect-scrollbar.min.css" rel="stylesheet">\n '''
try:
 if "action" in data and data["action"]=="menus":
  doc+='''\n<script type="text/javascript" src="'''
  try: doc+=str(config.base_url)
  except Exception as e:   doc+=str(e)
  doc+='''static/js/jquery-ui-1.12.1.custom/jquery-ui.js"></script>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n  <script type="text/javascript" src="'''
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
doc+='''static/js/python/__javascript__/nuclear.js"></script>\n  '''
try:
 if data["login"]:
  doc+='''\n  \n  <!--<script type="text/javascript" src="'''
  try: doc+=str(config.base_url)
  except Exception as e:   doc+=str(e)
  doc+='''static/js/python/__javascript__/login.js"></script>-->\n  '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n \n    <style type="text/css">\n      @media(max-width:380px){\n        .sin-pad-xs{\n          padding:0px !important;\n        }\n      }\n      input,select,button{\n        font-size:13px;\n      }\n      \n.mCSB_container{\n margin-right:15px !important ;\n} \n\n </style>\n\n\n <script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/tinymce/js/tinymce/tinymce.min.js"></script>\n <script type="text/javascript">\n        tinymce.init({\n   language : 'es',\n   selector: "textarea.editor",\n    theme: "modern",\n    plugins: [\n         "advlist autolink link image lists charmap print preview hr anchor pagebreak table",\n         "searchreplace wordcount visualblocks visualchars fullscreen insertdatetime media nonbreaking emoticons textcolor",\n         "save table contextmenu directionality emoticons template paste textcolor",\n         "code codesample"\n   ],\n   codesample_languages: [\n        {text: 'HTML/XML', value: 'markup'},\n        {text: 'JavaScript', value: 'javascript'},\n        {text: 'CSS', value: 'css'},\n        {text: 'PHP', value: 'php'},\n        {text: 'Ruby', value: 'ruby'},\n        {text: 'Python', value: 'python'},\n        {text: 'Java', value: 'java'},\n        {text: 'C', value: 'c'},\n        {text: 'C#', value: 'csharp'},\n        {text: 'C++', value: 'cpp'}\n    ],\n   content_css: "'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/tinymce/js/tinymce/skins/lightgray/content.min.css",\n   toolbar: "insertfile undo redo preview | fontselect | fontsizeselect | forecolor backcolor emoticons | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | media fullpage code codesample", \n    fontsize_formats: "9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 18pt 20pt 22pt 24pt",\n    \n\n font_formats: "Andale Mono=andale mono,times;"+\n        "Arial=arial,helvetica,sans-serif;"+\n        "Arial Black=arial black,avant garde;"+\n        "Book Antiqua=book antiqua,palatino;"+\n        "Comic Sans MS=comic sans ms,sans-serif;"+\n        "Courier New=courier new,courier;"+\n        "Georgia=georgia,palatino;"+\n        "Helvetica=helvetica;"+\n        "Impact=impact,chicago;"+\n        "Symbol=symbol;"+\n        "Tahoma=tahoma,arial,helvetica,sans-serif;"+\n        "Terminal=terminal,monaco;"+\n        "Times New Roman=times new roman,times;"+\n        "Trebuchet MS=trebuchet ms,geneva;"+\n        "Verdana=verdana,geneva;"+\n        "Webdings=webdings;"+\n        "Wingdings=wingdings,zapf dingbats",\n });   \n</script>\n\n\n \n'''
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
doc+='''\n</head>\n\n\n\n\n\n'''