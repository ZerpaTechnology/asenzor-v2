#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html>\n'''
try: doc+=str(incluir(data,"head2"))
except Exception as e: doc+=str(e)
doc+='''\n<body>\n<!--\n'''
#=incluir(data,"sidebar-customize")
doc+='''\n<iframe src="'''
#=routes.base_url+'action=personalizar'
doc+='''" style="height: 100vh;padding: 0px;background-color:gray;display: inline-block;width:calc(100% - 284px );border: none;">\n</iframe>\n-->\n<section class='Components'>\n	\n</section>\n<footer class="Components">\n</footer>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''Components/__javascript__/Components.js"></script>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/personalizador.js"></script>\n</body>\n</html>'''