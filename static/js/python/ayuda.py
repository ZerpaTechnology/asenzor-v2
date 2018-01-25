#!/usr/bin/python
# -*- coding: utf-8 -*-
__pragma__("alias","s","$")

def flash_help(evt):
 if s("#flash-help").hasClass("hidden"):
  s("#flash-help").removeClass("hidden")
 else:
  s("#flash-help").addClass("hidden")

s("#ayuda").bind("click",flash_help)

def flash_info(evt):
	
	for k,elem in enumerate(s(".info")):
		if elem.text==s(".btn-flash-info")[k].text:
			if s(elem).hasClass("hidden"):
				s(s(".info")[k]).removeClass("hidden")
			else:
				s(s(".info")[k]).addClass("hidden")


		"""

		if evt.target.text==s(".btn-flash-info")[k].text:

			if "hidden" in elem.class_name:
				s(s(".info")[k]).removeClass("hidden")
			
		else:
			if "hidden" not in elem.class_name:
				s(s(".info")[k]).addClass("hidden")
		"""
			
s(".btn-flash-info").bind("click",flash_info)