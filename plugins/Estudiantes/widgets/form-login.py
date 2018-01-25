#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div class="ff pad-t2 pad-b2 b-s1">\n\n<form  action="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''/Plugin/'''
try: doc+=str(plugin.name)
except Exception as e: doc+=str(e)
doc+='''/Entrar/manager=True&app='''
try: doc+=str(data['app'])
except Exception as e: doc+=str(e)
doc+='''" method="post">\n		<span class="blue font-s30"><b>UNEXPO</b></span> | <span class="font-s25">WebLogin</span>\n	\n	<div class="bg-gray b-r5 pad-3 text-center-sm">\n	<div>\n	<label class="font-s20">Expediente:</label>\n		<input type="number" name="expediente">\n	</div>\n	<div>\n	<label class="font-s20">Contraseña:</label>\n		<input type="password" name="password">\n	</div>\n	</div>\n\n	<div class="text-center-sm">\n	<input type="checkbox" name="" class="width-2 sin-marg">\n	<span class="alg-top">Yo uso esta maquina regularmente</span>\n	<div>\n	<input type="submit" name="" value="Entrar" class="btn white b-r5 bg-bluelight" >	\n	<a id="registrarse" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''/Plugin/'''
try: doc+=str(plugin.name)
except Exception as e: doc+=str(e)
doc+='''/Registrar/manager=True&app='''
try: doc+=str(data['app'])
except Exception as e: doc+=str(e)
doc+='''" class="btn b-r5 white bg-blue">Registrarse</a>\n	</div>\n	\n	</div>\n	\n</form>\n\n</div>'''