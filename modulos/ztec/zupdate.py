#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile
import shutil
import os
import urllib2
import sys
from zred import decode
from os.path import exists
#https://drive.google.com/uc?export=download&confirm=no_antivirus&id=XXXXXXXXX
#https://drive.google.com/file/d/0ByJYMxvQwmxFNkpRa19hU3RZWWc/view?usp=sharing
def status(count, data_size, total_data):
    """Llamado por cada bloque de datos recibido"""
    print count, data_size, total_data


def descargarVersion2(config,version="0ByJYMxvQwmxFNkpRa19hU3RZWWc",dom="http://zerpatechnology.com.ve/"):
	from urllib import urlretrieve, urlcleanup
	url = ("https://drive.google.com/uc?export=download&confirm=no_antivirus&id="+version)
	# Nombre del archivo a partir del URL
	filename = url[url.rfind("/") + 1:]
	while not filename:
	   filename = raw_input("No se ha podido obtener el nombre del "
	                             "archivo.\nEspecifique uno: ")
	    
	print "Descargando %s..." % filename
	    
	urlretrieve(url, filename, status)  # Descargar archivo
	urlcleanup()  #  Limpiar cache
	    
	print "%s descargado correctamente." % filename

def checkSize(version="0ByJYMxvQwmxFNkpRa19hU3RZWWc",dom="https://drive.google.com/"):

	import urllib
	site=urllib.urlopen(dom+"uc?export=download&confirm=bKUz&id="+version)
	meta=site.info()
	return meta.getheaders("Content-Length")[0]

def descargarVersion(config,version="0ByJYMxvQwmxFNkpRa19hU3RZWWc",dom="https://drive.google.com/"):
	try:
		#doc_url=dom+"update/"+version+".zip"
		doc_url=dom+"uc?export=download&confirm=bKUz&id="+version



		u = urllib2.urlopen(doc_url)
		#print u.headers

		


		localFile = open( "../"+config.update_folder+version+".zip" , 'w')
		
		localFile.write(u.read())
		localFile.close()
		return doc_url
	except Exception,e:
		print e
		return None

def backup(archivo,path):
	archivos=[]
	archivo=archivo.replace("/","")
	for elem in os.listdir(path):
	
		if (archivo[:archivo.rfind(".")]== elem[:elem.rfind(".")] or archivo[:archivo.rfind(".")]+"_backup" in elem[:elem.rfind(".")]) and elem[elem.rfind("."):]==archivo[archivo.rfind("."):]:
			archivos+=[elem]

	
	if archivo in archivos:
		archivos.remove(archivo)
	if "." in archivo:
		return archivo[:archivo.rfind(".")]+"_backup"+str(len(archivos))+archivo[archivo.rfind("."):]
	else:
		return archivo+"_backup"+str(len(archivos))
	
def lastbackup(archivo,path):
	archivos=[]
	archivo=archivo.replace("/","")

	for elem in os.listdir(path):
		
		if "." in archivo:
			if (archivo[:archivo.rfind(".")]== elem[:elem.rfind(".")] or archivo[:archivo.rfind(".")]+"_backup" in elem[:elem.rfind(".")]) and elem[elem.rfind("."):]==archivo[archivo.rfind("."):]:
				archivos+=[elem]
		else:
			if archivo==elem or archivo+"_backup" in elem:
				archivos+=[elem]	

		
	if len(archivos)>1:
		
		
		return archivo[:archivo.rfind(".")]+"_backup"+str(len(archivos)-2)+archivo[archivo.rfind("."):]


	else:
		return None
		

def actualizar(config,settings,version="update"):
	
	zf=zipfile.ZipFile("../"+config.update_folder+version+".zip", "r")
	
	carpetas=[]
	import chardet
	
	#zipfile.ZipInfo._decodeFilename = lambda self: self.filename
	#zf.extractall("../"+config.update_folder)
	for m in zf.infolist():

	    data = zf.read(m) # extract zipped data into memory

	    # convert unicode file path to utf8
	    disk_file_name = m.filename.encode('utf8')

	    dir_name = os.path.dirname("../"+config.update_folder+disk_file_name)
	    
	    try:
	    	if dir_name[len("../"+config.update_folder):].split("/")[0] not in carpetas:
	    		carpetas.append(dir_name[len("../"+config.update_folder):].split("/")[0])
	        os.makedirs(dir_name)
	    except OSError as e:
	    	
	        if e.errno == os.errno.EEXIST:
	            pass
	        else:
	            raise
	    except Exception as e:
	        pass

	    try:
		    with open("../"+config.update_folder+disk_file_name, 'wb') as fd:
		        fd.write(data)
	    except Exception as e:
	    	pass
	zf.close()
	
	for elem in carpetas:
		if elem =="apps":
			
			if elem!=config.apps_dir:
				os.rename("../"+config.update_folder+"apps",config.apps_dir)
				carpetas[carpetas.index("apps")]=config.apps_dir
			if os.listdir("../"+config.update_folder+config.apps_folder)[0]!=config.apps_folder+settings.app:
				os.rename("../"+config.update_folder+config.apps_folder+os.listdir("../"+config.update_folder+config.apps_folder)[0],"../"+config.update_folder+config.apps_folder+settings.app)


			for folder, subfolders, files in os.walk("../"+config.update_folder+elem):
				
				for file in files:
					archivo=os.path.join(folder,file)
					if exists(archivo):
						
						mibackup=backup(archivo[archivo.rfind("/"):],archivo[:archivo.rfind("/")])



						if archivo.endswith(".py") or archivo.endswith(".php") or archivo.endswith(".rb") or archivo.endswith(".perl"):

							os.rename("../"+archivo[len("../update/"):],"../"+archivo[len("../update/"):archivo.rfind("/")]+"/"+mibackup)
						else:
							
							ultbackup=lastbackup(archivo[archivo.rfind("/"):],"../"+archivo[len("../update/"):archivo.rfind("/")])							
							
							if ultbackup:
								
								if exists(archivo[:archivo.rfind("/")]+"/"+ultbackup):
									
									os.remove(archivo[:archivo.rfind("/")]+"/"+ultbackup)
								
								
								mibackup=backup(archivo[archivo.rfind("/"):],"../"+archivo[len("../update/"):archivo.rfind("/")])
								

								os.rename("../"+archivo[len("../update/"):],"../"+archivo[len("../update/"):archivo.rfind("/")]+"/"+mibackup)
								
							else:
								
								
								os.rename("../"+archivo[len("../update/"):],"../"+archivo[len("../update/"):archivo.rfind("/")]+"/"+mibackup)
						
						shutil.move(archivo,"../"+archivo[len("../update/"):archivo.rfind("/")])
						
					else:


						shutil.move(archivo,"../"+archivo[len("update/"):archivo.rfind("/")])
	
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
