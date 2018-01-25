#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''\n<iframe src="'''
try: doc+=str(config.base_url+'Plugin/'+plugin.name+'/sc/'+data['sc']+'/manager=True&app='+data['app'])
except Exception as e: doc+=str(e)
doc+='''" style="width:100%;min-height: 300px;border:none">\n</iframe>'''