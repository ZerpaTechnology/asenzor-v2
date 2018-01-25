#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from ztec.zmodel import Model
import sys
import os
import datetime
import ztec.zu as zu
sys.path.append("../")
import settings
try:
	import config.config as config
except:
	import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		

except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e