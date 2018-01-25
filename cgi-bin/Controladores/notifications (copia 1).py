if rest["app"]=="asenzor" and rest["method"]=="ajax":
	if rest["control"]=="notifications":
		print "Content-type: text/plain\n"
		versiones={}
		for elem in config.versiones_disponibles:
			for elem2 in rest["model"]["global"].obtenerFilas("Asenzor"):
				if elem2[0]==elem:
					versiones[elem]=elem2[1][4]["value"]
		print versiones