import control
#retorna los intervalos en numeros
prueba="""
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation [plugin1 id=1 ] esto va dentro [/plugin1] ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur.[plugin2 id=2] Excepteur sint[/plugin2] occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
#conjunto es donde se encutentra lo interno

def plugin(args=None,content=None,exterior=None):
	
	if args!=None:
		print "args :",args
	"""
	if content!=None:
		print "contenido :",content
	if exterior!=None:
		print "exterior :",exterior
	"""
control.convertir3(prueba,[["[plugin1","]"],["[plugin2","]"]],[["[/plugin1","]"],["[/plugin2","]"]],funcion=plugin)
