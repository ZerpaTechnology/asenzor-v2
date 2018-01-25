#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html><html>'''
try: doc+=str(incluir(data,"head",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''<body >'''
try: doc+=str(incluir(data,"login",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''  '''
try: doc+=str(incluir(data,"footer",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''  </body></html>'''