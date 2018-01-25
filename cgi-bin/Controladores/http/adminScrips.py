if "action" in p and p["action"]=="write": #and "args" in p:
	if "admin" in p and p["admin"]==True and "login" in p and p["login"]==True:
		if p["method"]=="ajax":	
			print data
