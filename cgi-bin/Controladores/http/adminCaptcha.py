if p["app"]=settings.app:
	if p["multipart-from/data"]==True:
		import os

		password="6LeR_jMUAAAAALp5FTznsBBLC2549pGHSl2rXIjz"
		req=rullib.open("https://www.google.com/recaptcha/api/siteverify?secret="+password+"&response="+data["g-recaptcha-response"].value+"&remoteip="+os.environ["REMOTE_ADDR"])
		