#!/usr/bin/env python
#!C:/Python27/python.exe
# -*- coding: utf-8 -*-


#print "Content-type: text/plain\n"


try:
	#===============================
	#LIBRERIAS
	import os
	import sys

	sys.path.append("../")

	from config import config

	
	from modulos.ztec.Asenzor import Asenzor



	from modulos.ztec.zred import Headers
	
	sys.path.append(config.base_root+"modulos/ztec")
	HEADERS=Headers()
	
	#======================================
	
	
	fmk=Asenzor()

	fmk.run()
	#================================
	

	
except Exception ,e:
	HEADERS.show()
	print e

