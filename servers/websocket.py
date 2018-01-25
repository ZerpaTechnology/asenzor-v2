#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import sys
import os
import time
from config import config
#(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
mtime= None
app=None
develop=None
clients=[]
routes=None
settings=None
script=""
beforeScript=None
escribir=False
operacion=""
cliente=None
datos=None
def loop():
	global mtime
	global config
	global routes
	global app
	global datos
	global script
	global beforeScript
	global operacion
	global escribir
	global cliente
	global develop
	


	while True:

		(mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2)=os.stat(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py")
		
		if mtime!=mtime2 and escribir==False:
			
			f=open(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py","r")
			script=f.read()
			f.close()
			if cliente.address[1]==develop and script!=beforeScript:
				cliente.sendMessage(unicode(script))
				escribir=True
			beforeScript=script
			(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py")
			
			
		


			
		
			

			

class SimpleEcho(WebSocket):
    def handleConnected(self):
	   global clients
	   clients.append(self)

    def handleClose(self):
	   global clients
	   clients.remove(self)
    def handleMessage(self):
        # echo message back to client
        try:
	        request=""
	        global mtime
	        global develop
	        global clients
	        global escribir
	        global cliente
	        global datos
	        global script
	        global beforeScript
	        cliente=self
	        print "$$",self.data
	        datos=self.data

	        if type(self.data)==unicode:
		        	if self.data[0]=="{" and self.data[-1]=="}":
		        		try:
			            		exec("data="+self.data)
			            		if "app" not in data:
			            			data["app"]=config.default_app        			
		                		sys.path.append(config.apps_folder+data["app"]+"/admin/")
		                		import settings
		                		from settings import routes as routes
		                		from settings import config as settings
		                		from modulos.ztec.zred import normalizar
		                		global routes
		                		global settings
		                		global app
		                		app=data["app"]
		                		
		                 		for elem in settings.websocket_controllers:		
			            			f=open(config.apps_folder+data["app"]+"/user/"+config.controller_folder+routes.websocket_folder+elem+".py","r")
			            			try:
		           	    			    exec(f.read())
		                 			    if request!="":
					                        self.sendMessage(unicode(request))
			            			except Exception, e:
			            				import traceback
			            				exc_type,exc_obj,exc_tb=sys.exc_info()
			            				fname = exc_tb.tb_frame.f_code.co_filename
			            				print "".join(traceback.format_exception(exc_type,fname,exc_tb))
		        				f.close()

		        			if data["action"]=="develop":
		        						
		        				if normalizar(data["args"])==[True]:

											develop=self.address[1]
											
											(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat(config.apps_folder+data["app"]+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py")
											self.sendMessage(unicode(True))
		        				elif normalizar(data["args"])!=[False]:
											develop=None
											self.sendMessage(unicode(False))

		        			for elem in settings.custom_websocket_controllers:
			            			f=open(config.apps_folder+data["app"]+"/user/"+config.controller_folder+routes.custom_websocket_folder+elem+".py","r")
			            			try:
		           	    			    exec(f.read())
		                 			    if request!="":
					                        self.sendMessage(unicode(request))
			            			except Exception, e:
			            				import traceback
			            				exc_type,exc_obj,exc_tb=sys.exc_info()
			            				fname = exc_tb.tb_frame.f_code.co_filename
			            				print "".join(traceback.format_exception(exc_type,fname,exc_tb))
		        				f.close()
			            	except Exception, e:
								import traceback
								exc_type,exc_obj,exc_tb=sys.exc_info()
								fname = exc_tb.tb_frame.f_code.co_filename
								print "".join(traceback.format_exception(exc_type,fname,exc_tb))
				elif develop!=None:
					
					
					t=threading.Thread(target=loop,args=())
					t.start()
					if self.address[1]==develop:
						

						if escribir==True:
							if "#CORRECTO:" in self.data.split("\n")[0]:
								f=open(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"log.py","a")
								f.write("\n#======================================================\n"+script)
								f.close()
								(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py")
							elif "#ERROR:" in self.data.split("\n")[0]:
								(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py")
							
								
						escribir=False
						globals()["escribir"]=False
					
					"""
					if mtime!=mtime2:
					  print "xxxxxxxxxx"

					  meta=os.stat(config.apps_folder+app+"/user/"+config.controller_folder+routes.websocket_folder+"develop.py")
					  
					  f=open(config.apps_folder+app+"/user/"+config.controller_folder+roots.websocket_folder+"develop.py","r")
		        		  script=f.read()
		        		  f.close()
		        		for elem in clients:
		        			if elem==develop:
		        				self.sendMessage(script)
		        				print self.data
						
					else:
				        	pass
				       
				        	  f=open(config.apps_folder+app+"/user/"+config.controller_folder+roots.websocket_folder+"log.py","a")
				        	  f.write(script)
				        	  f.close()
				       

		        	"""
	        		
	        		
				else:
					self.sendMessage(self.data)
        except Exception,e:
        	print e
    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', 8000, SimpleEcho)
server.serveforever()
