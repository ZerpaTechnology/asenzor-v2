#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:

	
	keys=[]
	for elem in data:
		keys.append(elem)

	if data["action"].value=="publicarNoticia":

		l=[]
		l2=["email","password","name","lastname","rank","avatar","department_id","position_id"]
		for elem in l2:
			if elem not in keys:
				print "No llenastes el campo ",elem
				l.append(elem)
			
	
		if l==[]:
			
			#img=p["base_url"]+"../../static/imgs/icono_perfil.jpg"
			#main_model.registrarUsuario(p["nombres"],p["apellidos"],p["correo"],p["password"],img,img)
			
			#zred.sendEmail("zerpatechnolgy@gmail.com",p["correo"],"pendiente","Gracias por registrarte en AsenZor porfavor introduce el siguiente codigo para confirmar tu registro: "+codConfirmacion)
			#---------------------------------------------
			
			codConfirmacion=zu.randomString(4,noalp=False)

		
		
			
			
			p["model"]["noticias"].publicarNoticia(data[""].value,data["password"].value,data["email"].value,data["name"].value,data["lastname"].value,int(data["rank"].value),data["avatar"].value,int(data["department_id"].value),int(data["position_id"].value))
			#zred.clienteSock("localhost",9999,'python zred.sendEmail(jesus26abraham1996@gmail.com,'+p["correo"]+',password,<p>Gracias por registrarte en AsenZor por favor introduce el siguiente código para confirmar tu registro: '+codConfirmacion+'</p> , Asenzor - Codigo de confirmacion)')
			#zred.clienteSock("localhost",9999,'')

			#---------------------------------------------

			if "log" in p and p["log"]=="show":
				print "Se ha enviado un mensaje de confirmación al correo ",p["correo"],"<br>"
				for elem in modelo.db.log:
					print elem.replace("\n","<br>").replace("\x1b[1;31m","<span class='blue'>").replace("\x1b[0m","</span>")
				

				if settings.consola==True:
					try:
						for elem in modelo.db.log:
							clienteSock(settings.host,settings.consola_port,elem,"")
					except Exception as e:
						print e
			
			
		else:
			print "No llenastes los campos: ",l
	
except Exception, e:
	if config.mod_debug==False:
		print "error en session<br>"
		print es