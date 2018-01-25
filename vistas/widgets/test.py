doc+='''<div>\n'''
try:
 for elem in ["hola","mundo"]:
  doc+='''\n<span>'''
  try: doc+=str(elem)
  except Exception as e:   doc+=str(e)
  doc+='''</span>\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n</div>'''