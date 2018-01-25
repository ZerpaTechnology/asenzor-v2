rest=window.rest
config=Config.Config()
Component=nuclear.Component
__pragma__("alias","s","$")
Components={"builder-box":Component("builder-box",{},True,True,True)}
if rest["action"]=="personalizar":
	s("[builder]").append("<span class='builder'></span>")
	s("[builder]").append(Components["builder-box"].run())

	s(".builder").css({"background-image":"url('"+config.base_url+"static/imgs/iconos/pencil_blue.png')",
					   "height":"30px",
					   "width":"30px",
					   "position":"absolute",
					   "top":"0px",
					   "left":"0px",
					   "background-size":"cover",
					   "cursor":"pointer"})

	s(".builder-box").css({"width":"300px",
									"height":"300px",
									"position":"relative",
									"top":"0px",
									"left":"0px",
									"border":"solid",
									"border-width":"1px"})
	def consultarConfiguracion(evt):
		pass
	s(".builder").bind("click",consultarConfiguracion)