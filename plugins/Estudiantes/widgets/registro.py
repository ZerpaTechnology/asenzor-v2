#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div>\n'''
try: doc+=str(incluir(data,"head","global"))
except Exception as e: doc+=str(e)
doc+='''\n'''
data["boxes"]=[data["plugins"]["Estudiantes"].model["main"].obtenerFilas("Estudiantes")[0][1]]
doc+='''\n'''
try: doc+=str(incluir(data,"edit-box","global"))
except Exception as e: doc+=str(e)
doc+='''\n\n\n</div>'''