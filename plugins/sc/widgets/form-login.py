#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div class="pad-t2 pad-b2 b-s1">

<form  action="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''/Plugin/'''
try: doc+=str(plugin.name)
except Exception, e: doc+=str(e)
doc+='''/Entrar/manager=True&app='''
try: doc+=str(data['app'])
except Exception, e: doc+=str(e)
doc+='''" method="post">
		<span class="blue font-s30"><b>UNEXPO</b></span> | <span class="font-s25">WebLogin</span>
	
	<div class="bg-gray b-r5 pad-3 text-center-sm">
	<div>
	<label class="font-s20">Expediente:</label>
		<input type="number" name="expediente">
	</div>
	<div>
	<label class="font-s20">Contraseña:</label>
		<input type="password" name="password">
	</div>
	</div>

	<div class="text-center-sm">
	<input type="checkbox" name="" class="width-2 sin-marg">
	<span class="alg-top">Yo uso esta maquina regularmente</span>
	<div>
	<input type="submit" name="" value="Entrar" >	
	</div>
	
	</div>
	
</form>

</div>'''