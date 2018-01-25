#!/usr/bin/env python
# -*- coding: utf-8 -*-

if "action" in p:
	if p["action"]=="crearLibro":
			main_model.crearLibro("AsenZor - Guia del desarrollador",["Jesús Zerpa"])

	if p["action"]=="guardarTema":
			introduccion="""
			 """
			main_model.guardarTema("AsenZor - default","AsenZor - Guia del desarrollador","introducción")
