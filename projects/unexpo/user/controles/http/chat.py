if "action" in p and p["action"]=="chat": #and "args" in p:
 if "admin" in p and p["admin"]==True and "login" in p and p["login"]==True:
 	p["model"]["contactos"].obtenerChatDisponible()
 	p["model"]["contactos"].iniciarChat(p["contato"])
 	p["model"]["contactos"].enviarMensaje(p["contato"])
 	p["model"]["contactos"].escucharChat(p["contato"])
 	pass
 else:
 	p["model"]["contactos"].obtenerChatDisponible()
 	p["model"]["contactos"].iniciarChat(p["contato"])
 	p["model"]["contactos"].enviarMensaje(p["contato"])
 	p["model"]["contactos"].escucharChat(p["contato"])

 	pass

