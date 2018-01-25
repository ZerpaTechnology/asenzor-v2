#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html><head>	<title></title></head><body><ul>'''
for licencia in data["licencias"]:
  print '''	<li><a href="'''  +str(config.base_url+"static/licencias/"+licencia)  +'''">'''  +str(licencia)  +'''<a></li>'''
  pass
print '''	</ul></body></html>'''