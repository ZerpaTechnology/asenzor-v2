import zipfile
import shutil
import os
import urllib2
import sys
from os.path import exists
sys.path+=["../"]
import config.config as config
sys.path+=["../"+config.apps_folder+"JDYM/admin/"]
import settings.routes as routes
import settings.config as settings

def descargarVersion( version="update",dom="http://zerpatechonolgy.com.ve/"):
	doc_url=+"update/"+version+".zip"
	u = urllib2.urlopen(doc_url)
	localFile = open( version+".zip" , 'w')
	localFile.write(u.read())
	localFile.close()
def backup(archivo,path):
	archivos=[]
	archivo=archivo.replace("/","")
	for elem in os.listdir(path):
		
		if (archivo[:archivo.rfind(".")]== elem[:elem.rfind(".")] or archivo[:archivo.rfind(".")]+"_backup" in elem[:elem.rfind(".")]) and elem[elem.rfind("."):]==archivo[archivo.rfind("."):]:
			archivos+=[elem]

	
	if archivo in archivos:
		archivos.remove(archivo)
		
	return archivo[:archivo.rfind(".")]+"_backup"+str(len(archivos))+archivo[archivo.rfind("."):]
	
def lastbackup(archivo,path):
	archivos=[]
	archivo=archivo.replace("/","")
	for elem in os.listdir(path):
		
		if "." in archivo:
			if (archivo[:archivo.rfind(".")]== elem[:elem.rfind(".")] or archivo[:archivo.rfind(".")]+"_backup" in elem[:elem.rfind(".")]) and elem[elem.rfind("."):]==archivo[archivo.rfind("."):]:
				archivos+=[elem]
		else:
			if archivo==elem or archivo+":backup" in elem:
				archivos+=[elem]	

	
	if len(archivos)>1:
		
		
		return archivo[:archivo.rfind(".")]+"_backup"+str(len(archivos)-2)+archivo[archivo.rfind("."):]
	else:
		return None

def actualizar(config,settings,version="update"):
	zf=zipfile.ZipFile(version+".zip", "r")
	carpetas=[]
	for i in zf.namelist():
		zf.extract(i, path="/root/workspace/htdocs/zerpatec_backup/update/")
		if i.split("/")[0] not in carpetas:
			carpetas.append(i.split("/")[0])
	for elem in carpetas:
		if elem =="apps":
			
			if elem!=config.apps_dir:
				os.rename("apps",config.apps_dir)
				carpetas[carpetas.index("apps")]=config.apps_dir
			if os.listdir(config.apps_folder)[0]!=config.apps_folder+settings.app:
				os.rename(config.apps_folder+os.listdir(config.apps_folder)[0],config.apps_folder+settings.app)

			for folder, subfolders, files in os.walk(elem):
				for file in files:
					archivo=os.path.join(folder,file)
					if exists("../"+archivo):
						mibackup=backup(archivo[archivo.rfind("/"):],"../"+archivo[:archivo.rfind("/")])

						if archivo.endswith(".py") or archivo.endswith(".php") or archivo.endswith(".rb") or archivo.endswith(".perl"):
							os.rename("../"+archivo,"../"+archivo[:archivo.rfind("/")]+"/"+mibackup)
						else:

							ultbackup=lastbackup(archivo[archivo.rfind("/"):],"../"+archivo[:archivo.rfind("/")])							
							if ultbackup:
								if exists("../"+archivo[:archivo.rfind("/")]+"/"+ultbackup):
									os.remove("../"+archivo[:archivo.rfind("/")]+"/"+ultbackup)
								mibackup=backup(archivo[archivo.rfind("/"):],"../"+archivo[:archivo.rfind("/")])
								os.rename("../"+archivo,"../"+archivo[:archivo.rfind("/")]+"/"+mibackup)
								
							else:


								os.rename("../"+archivo,"../"+archivo[:archivo.rfind("/")]+"/"+mibackup)

						shutil.move(archivo,"../"+archivo[:archivo.rfind("/")])
					else:
						shutil.move(archivo,"../"+archivo[:archivo.rfind("/")])

def crearVersion(config,settings,routes,nombre="update"):
	f=zipfile.ZipFile(nombre+".zip","w")
	for filename in ["../"+config.apps_folder+settings.app+"/user/"+config.controller_folder+routes.http_dir,
					 "../"+config.apps_folder+settings.app+"/user/"+config.controller_folder+routes.websocket_dir,
					 "../"+config.apps_folder+settings.app+"/admin/"+routes.models_dir,
					 "../"+config.apps_folder+settings.app+"/admin/"+routes.vistas_dir,
					 "../"+config.apps_folder+settings.app+"/admin/"+routes.static_dir,
					 "../"+config.static_dir,
		]:
		for folder, subfolders, files in os.walk(filename):
		    for file in files:
		            f.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),os.getcwd()).replace("../",""), compress_type = zipfile.ZIP_DEFLATED)
		 
	f.close()
#crearVersion(config,settings,routes,"update2")
actualizar(config,settings,"update")
#crearVersion(config,settings,routes,"update")