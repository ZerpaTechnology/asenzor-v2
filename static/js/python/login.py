__pragma__("alias","s","$")


config=window.config


def checkear():	
	cookies=nuclear.getCookie()
	if ("token" in cookies and cookies["token"]=="") and ("token2" in cookies and cookies["token2"]==""):
		s("#login").removeClass("hidden")
	else:
		s("#login").addClass("hidden")
		
window.setInterval(checkear,1000)
