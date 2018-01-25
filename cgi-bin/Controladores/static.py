from modulos.ztec.zred import Headers
from modulos.ztec.zu import redict
from config import config
from modulos.ztec.intervalor.control import convertir2
import os
class static(object):
	"""docstring for static"""
	def __init__(self, data):
		self.data=data
		self.HEADERS=Headers()
		self.HEADERS.set_headers({"Content-type":"text/plain\n"})
		if data["control"]!=None and data["control"] in dir(self):
			exec("self."+data["control"]+"()")

	def plugin(self):
			for elem in rest["model"]["global"].obtenerFilas('Gestor-plugins'):
   
				 if len(rest["args"])>1 and elem[0]==self.data["args"][0] and self.data["args"][1]=="screen":

					print "Content-type: image/png"+"\n"
					print file(config.base_root+config.projects_folder+self.data["vista"]+"/screenshot.png", "rb").read()	
	def screen(self):
		print "Content-type: image/png"+"\n"
		print file(config.base_root+config.projects_folder+self.data["app"]+"/screenshot.png", "rb").read()	
	def script(self):
		if self.data["file"].endswith(".js"):
			self.HEADERS.show()
			if os.path.isfile(config.base_root+config.static_folder+"js/python/__javascript__/"+self.data["file"]):

				f=open(config.base_root+config.static_folder+"js/python/__javascript__/"+self.data["file"],"r")
				script=convertir2(f.read().replace("\\n","\\\\n").replace("\\'","\\\\'").replace('\\"','\\\\"'),["<%","%>"])
				doc=""
				try:

					exec(script)
					print "var True=true;var False=false;var None=null;\n"+doc
				except Exception,e:
					print e
				f.close()

		else:
			pass