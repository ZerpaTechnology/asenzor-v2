doc+='''<header class="bg-ubuntu_jet height-4" style="position: fixed;top: 0px;left: 0px;width: 100%;z-index: 10;">\n <a href="#" id="btn-menu">\n <div class="d-inline-block pad-l1 pad-t05 pad-b05">\n  <span class="blue font-s20">'''
try: doc+=str(data["app"])
except Exception as e: doc+=str(e)
doc+='''</span><span class="font-s12 white">DASHBOARD</span>\n\n </div> \n \n </a>\n <a href="'''
try: doc+=str(data['actionbase'])
except Exception as e: doc+=str(e)
doc+='''&action=licencias" class="pad-l3 bluelight">Licencias</a>\n <nav class="d-inline-block white pad-1 pad-r2 right hidden">\n  <span class="ubuntu_green">400 bs.F</span> / <span class="ubuntu_red">0 bs.F</span>\n  <a href=""><img src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/iconos/noun_138581_cc.png" class="height-2"></a> \n  <a href=""><img src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/iconos/003-contact.png" class="height-2"></a> \n  <a href=""><img src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/iconos/007-alarm.png" class="height-2"></a> \n \n </nav>  \n</header>'''