doc+='''\n'''
data["style"]={"widget-chat":{"#widget-chat":{"position":"fixed","right":"0px","bottom":"50px"} } }  
doc+='''\n'''
#=incluir(data,"widget-chat")
doc+='''\n\n<footer class="text-center bg-ubuntu_jet white pad-t1 pad-b1" style="position: fixed;bottom: 0px;left: 0px;width: 100%;z-index:12;">\n<div id="notifications" style="position: fixed;top: 10px; right: 10px">\n	\n</div>\n '''
try: doc+=str(data["app"])
except Exception as e: doc+=str(e)
doc+='''2017@zerpatechnology\n <div class="right pad-r1">\n '''
try:
 if "actionbase" in data:
  doc+='''\n  <a href="'''
  try: doc+=str(data['actionbase'])
  except Exception as e:   doc+=str(e)
  doc+='''&action=licencias" class="bluelight">Licencias</a>  \n '''
  pass
except Exception as e: doc+=str(e)
doc+='''\n </div>\n\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/menu.js"></script>\n\n\n<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/notifications.by"></script>-->\n\n\n<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/websocket.by"></script>-->\n<!-- <script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/chat.by"></script> -->\n<script>\n    (function($){\n        $(window).on("load",function(){\n            $(".scrollbar").mCustomScrollbar();\n            theme:"dark";\n        });\n    })(jQuery);\n    \n</script>\n<style type="text/css">\n	#login{\n		position: fixed;\n		top: 0;\n		left: 0;\n		width: 100%;\n		height: 100%;\n		background-color:rgba(0,0,0,0.5);\n	}\n</style>\n<div id="login" class="'''
try: doc+=str('hidden' if data['login']==True else 'hidden' if data['control']=='admin' and data['metodo']==None else '')
except Exception as e: doc+=str(e)
doc+='''">\n\n\n	'''
try: doc+=str(incluir(data,"login"))
except Exception as e: doc+=str(e)
doc+='''\n</div>\n\n\n\n</footer>\n \n\n\n\n\n\n\n\n\n\n'''