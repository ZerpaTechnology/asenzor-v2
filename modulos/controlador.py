from config import config
import os


from modulos.ztec.intervalor.control import generar2,convertir3

from modulos.ztec.zred import normalizar,decode,urlBuilder,Headers

import ztec
def thumbails(raiz,ruta,archivo,sufijo="_540x540"):
	from settings import config as settings
	from settings import routes
	if raiz=="admin":
		base=config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+ruta
		base2=config.base_url+config.apps_folder+settings.app+"/admin/"+routes.static_folder+ruta

	elif raiz=="user":
		base=config.base_root+config.apps_folder+settings.app+"/user/"+routes.static_folder+ruta
		base2=config.base_url+config.apps_folder+settings.app+"/user/"+routes.static_folder+ruta
	elif raiz=="global":
		base=config.base_root+config.static+ruta
		base2=config.base_url+config.static+ruta
	if os.path.exists(base+archivo[:archivo.rfind(".")]+sufijo+archivo[archivo.rfind("."):]):
		return base2+archivo[:archivo.rfind(".")]+sufijo+archivo[archivo.rfind("."):]
	else:
		return base2+archivo

def xs(img):
  return img[:img.find(".")]+"_540x540"+img[img.find("."):]

def brython_load(modulos,espacio="global",python=""):
	by=""
	js=""
	if type(modulos)==str:
		modulos=[modulos]
	if espacio=="global":
		for elem in modulos:
			if os.path.exists(config.base_root+config.static_folder+"brython/"+elem[:elem.rfind(".")]+".js"):
				f=open(config.base_root+config.static_folder+"brython/"+elem[:elem.rfind(".")]+".js")
				js+="\n"+f.read()+"\n"
				f.close()
				
			elif os.path.exists(config.base_root+config.static_folder+"brython/"+elem):

				f=open(config.base_root+config.static_folder+"brython/"+elem)
				by+="#"+elem+"\n"+f.read()
				f.close()			
			else:
				by+="<!-- Brython no encontro el script "+modulo+"-->\n"
		
	elif espacio=="admin":
		for elem in modulos:
			from settings import config as settings
			from settings import routes
			if os.path.exists(config.base_root+config.apps_folder+settins.app+"/admin/"+routes.static_folder+"brython/"+elem[:elem.rfind(".")]+".js"):
				f=open(config.base_root+config.apps_folder+settins.app+"/admin/"+routes.static_folder+"brython/"+elem[:elem.rfind(".")]+".js")
				js+="\n"+f.read()+"\n"
				f.close()
			elif os.path.exists(config.base_root+config.apps_folder+settins.app+"/admin/"+routes.static_folder+"brython/"+elem):
				f=open(config.base_root+config.apps_folder+settins.app+"/admin/"+routes.static_folder+"brython/"+elem)
				by+="\n"+f.read()+"\n"
				f.close()
			else:
				by+="<!-- Brython no encontro el script "+elem+"-->\n"
	elif espacio=="user":
		from settings import config as settings
		from settings import routes
		for elem in modulos:
			if os.path.exists(config.base_root+config.apps_folder+settins.app+"/user/"+routes.static_folder+"brython/"+elem[:elem.rfind(".")]+".js"):
				f=open(config.base_root+config.apps_folder+settins.app+"/user/"+routes.static_folder+"brython/"+elem)
				js+="\n"+f.read()+"\n"
				f.close()
			elif os.path.exists(config.base_root+config.apps_folder+settins.app+"/user/"+routes.static_folder+"brython/"+elem):
				f=open(config.base_root+config.apps_folder+settins.app+"/user/"+routes.static_folder+"brython/"+elem)
				by+="\n"+f.read()+"\n"
				f.close()		
			else:
				by+="<!-- Brython no encontro el script "+elem+"-->\n"
	
	return "<script>"+js+"</script>"+"<script type='text/python"+python+"'>"+by+"</script>"








class Controlador(object):
	"""docstring for Vistas"""
	def __init__(self,data):      
	  
	  self.data=data
	  

	  self.request=data["request"] 
	  self.isglobal=False
	  self.admin=False

	  self.servida=False
	  self.plugins=data["plugins"]

	  self.vista=None

	  self.tabla="Paginas"
	  self.embebed=None

	  self.model_name="paginas"
	  self.vistas=[]
	  self.ruta_html=""
	  self.ruta_python=""
	  self.HEADERS=Headers()
	  
	  

	  

	  self.zt=None
	  if self.data["app"]!=None:

	  	import settings.config as settings
	  	
	  	
	  	import settings.routes as routes


	  	self.ruta_widget=config.base_root+config.apps_folder+settings.app+"/user/"+routes.vistas_folder
	  	self.ruta_python=self.ruta_html+routes.templates_folder
	  	from ztec.zt import ZT
	  	self.zt=ZT(config.base_root+(config.apps_folder if data["manager"]==False else config.projects_folder)+settings.app+"/admin/"+routes.models_folder+routes.traducciones_folder+"traducciones-"+settings.lang.upper(),"request/",data["token"] if "token" in data else "user",ext=".py")
	  self.data_temp={}


	  


	  for elem in data:
	    if type(elem)==int:
	      self.data_temp[elem]=data[elem]
	    elif type(elem)==str:
	      self.data_temp[elem]=data[elem]
	    elif type(elem)==bool:
	      self.data_temp[elem]=data[elem]
	    elif type(elem)==float:
	      self.data_temp[elem]=data[elem]
	    elif type(elem)==dict:
	      self.data_temp[elem]=data[elem]
	    elif type(elem)==list:
	      self.data_temp[elem]=data[elem]
	    elif type(elem)==tuple:
	      self.data_temp[elem]=data[elem]


	def add_vista(self,vista):
		if vista not in self.vistas:
			self.vistas.append(vista)
			self.vista=vista
	def hacer_constructor(self,ul_class="navbar-nav mr-auto",li_class="nav-item",a_class="nav-link",a_atts="",li_atts="",ul_atts="",funcion=None,constructor=None,marcadores=None):

		def construir_menu(menu,ul_class=ul_class,li_class=li_class,a_class=a_class, a_atts=a_atts,li_atts=li_atts,ul_atts=ul_atts, funcion=funcion,constructor=constructor,marcadores=marcadores):
			if constructor==None:
				constructor=self.construir_menu

			html="<ul class='"+ul_class+"' "+ul_atts+">"
			
			for k,tag in enumerate(menu):
				if type(tag["url"])==list:
					#if marcadores!=None and k in list(marcadores):

					html+=(("<li "+li_atts+" class='"+li_class+"'><a tabindex='-1'  class='"+a_class+"' "+a_atts+" href='"+config.base_url+tag["url"][3]+"/"+tag["url"][4]+"'>"+tag["name"]+constructor(tag["children"])+"</a></li>") if funcion==None else funcion(tag,constructor))
				elif type(tag["url"])==str:
					
					html+=("<li "+li_atts+" class='"+li_class+"'><a tabindex='-1'  class='"+a_class+"' "+a_atts+" href='"+tag["url"]+"'>"+tag["name"]+constructor(tag["children"])+"</a></li>") if funcion==None else funcion(tag,constructor)
					pass

			html+="</ul>"
			return html
		return construir_menu

	def construir_menu(self,menu,ul_class="nav navbar-nav",li_class="nav-item",a_class="nav-link",a_atts="",li_atts="",ul_atts="",funcion=None,constructor=None):

		if constructor==None:
			constructor=self.construir_menu


		
		html="<ul class='"+ul_class+"'>"
		
		for tag in menu:
			

			if type(tag["url"])==list:

				html+="<li class='"+li_class+"' "+li_atts+"  >"+("<a tabindex='-1'  class='"+a_class+"' "+a_atts+"  href='"+config.base_url+tag["url"][3]+"/"+tag["url"][4]+"'>"+tag["name"]+"</a>"+constructor(tag["children"])+"</li>"  if funcion==None else funcion(tag,constructor) )
			else:
				
				html+=("<li class='"+li_class+"' "+li_atts+" >"+("<a  tabindex='-1' class='"+a_class+"' "+a_atts+"  href='"+tag["url"]+"'>"+tag["name"]+"</a>"+constructor(tag["children"])+"</li>")) if funcion==None else funcion(tag,constructor)
				pass

		html+="</ul>"
		return html

	def main_menu(self,ul_class="navbar-nav mr-auto",li_class="nav-item",a_class="nav-link",funcion=None,constructor=None):
		
		return self.construir_menu(self.data["model"]["menus"].obtenerMenu("main")[1][0],ul_class=ul_class,li_class=li_class,a_class=a_class,funcion=funcion,constructor=constructor)

	def foot_menu(self,_class="",_id="foot_menu"):

		return self.construir_menu(self.data["model"]["menus"].obtenerMenu("footer")[1][0],_class)

	def top_bar_menu(self,_class="",_id="top_bar_menu"):

		return self.construir_menu(self.data["model"]["menus"].obtenerMenu("top")[1][0],_class)
		
	def my_acount_menu(self,_class="",_id="main_menu"):

		return self.construir_menu(self.data["model"]["menus"].obtenerMenu("my_acount")[1][0],_class)

	def metodo_desconocido(self):
		
		from modulos.ztec.zred import gringolizar
		if self.data["app"]!=None:
		  	import settings.config as settings
		  	import settings.routes as routes
		
		#self.vista="error404"
		
		
		for elem in self.data["model"][self.model_name].obtenerFilas(self.tabla):

			if self.data["metodo"]==None:
				
				if gringolizar(elem[0],"-")==self.data["control"]:
					metadatos=self.data["model"][self.model_name].formatearMetadatos(elem[4])
					self.data["post"]=elem[1]
					self.vista=metadatos["layout"]
			else:

				if gringolizar(elem[0],"-")==self.data["metodo"]:

					metadatos=self.data["model"][self.model_name].formatearMetadatos(elem[4])
					self.data["post"]=elem[1]

					self.vista=metadatos["layout"]

		self.servir()



	def generar(self,ruta_html,ruta_python,cabeceras):

	  generar2(ruta_html,ruta_python,cabeceras) 

	def incluir(self,data,widgets,isglobal=False,admin=False,embebido=False):

	  widget=""
	  import urllib,urllib2 
	  from modulos.ztec.zu import filtrar_datos_planos
	  from modulos.ztec.zu import rstr
	  incluir=self.incluir

	  do_shortcode=self.do_shortcode
	  main_menu=self.main_menu
	  foot_menu=self.foot_menu
	  top_bar_menu=self.top_bar_menu
	  my_acount=self.my_acount_menu
	  hacer_constructor=self.hacer_constructor

	  import imp
	  if self.data["global_control"]!=None:
	  	plugin=imp.load_source("",config.base_root+config.plugins_folder+self.data["control"]+"/plugin.py")
	  if self.data["app"]!=None:
	  	import settings.config as settings
	  	import settings.routes as routes
	  	routes.base_url=config.base_url+settings.app+"/"
	  	


	  def wapper(target,constructor):
	  	global len
	  	global False
	  	global True
	  	if len(target["children"])>0:
	  		sub=False
	  		for elem in target["children"]:
	  			if len(elem["children"])>0:
	  				sub=True
	  				break

	  		return '<li class="'+("dropdown" if sub==False else "dropdown-submenu")+'"><a tabindex="-1"  class="dropdown-toggle nav-link" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="true"><b>'+target["name"]+'</b> <span class="caret"></span>'+constructor(target["children"])+'</li>'
	  	else:
	  		return "<li><a class='nav-link'   tabindex='-1'  href='"+target["url"]+"'>"+target["name"]+"</a>""</li>"
	  
	  if type(widgets)==list or type(widgets)==tuple:
	    if embebido=="php":
	      for w in widgets:
	        pass
	    elif embebido=="rb":
	      for w in widgets:
	        generar2(self.ruta_widget+(routes.widgets_folder if self.data["app"]!=None else "")+w+".html.erb",self.ruta_widget+w+".rb","")
	    else:

	      for w in widgets:
	      	if len(w)==1:
	      		self.generar(self.ruta_widget+(routes.widgets_folder if self.data["app"]!=None else "")+w+".html",self.ruta_widget+w+".py","")
		        f=open(self.ruta_widget+(routes.widgets_folder if self.data["app"]!=None else "")+w+".py","r")
		        widget+=f.read()+"\n"
		        f.close()
	      	elif len(w)==2:
		      	for w2 in w[1]:
		      		if w[0]==data["action"]:


				        self.generar((self.ruta_widget if self.isglobal==False else config.base_root+config.vistas_folder)+(routes.widgets_folder if self.data["app"]!=None else "")+w2+".html",(self.ruta_widget if self.isglobal==False else config.base_root+config.vistas_folder)+(routes.widgets_folder if self.data["app"]!=None else "")+w2+".py","")
				        f=open((self.ruta_widget if self.isglobal==False else config.base_root+config.vistas_folder)+(routes.widgets_folder if self.data["app"]!=None else "")+w2+".py","r")
				        widget+=f.read()+"\n"
				        f.close()
	      doc=""


	      exec(widget)
	      return doc
	  elif type(widgets)==str:

	    if embebido=="php":
	      params = urllib.urlencode({"data":filtrar_datos_planos(self.data)})
	      
	      f=urllib2.urlopen(config.base_url+rstr(self.ruta_widget.replace("/admin/","/user/"),"/",5)+widgets+".php",params)
	      return f.read()
	    elif embebido=="rb":
	      self.generar(self.ruta_widget+(routes.widgets_folder if self.data["app"]!=None else "")+widgets+".html.rb",self.ruta_widget+widgets+".rb","")
	      params = urllib.urlencode({"data":filtrar_datos_planos(self.data)})
	      f=urllib2.urlopen(config.base_url+rstr(self.ruta_widget.replace("/admin/","/user/"),"/",5)+widgets+".rb",params)
	      return f.read()
	    else:
	    	self.HEADERS.show()
	    	
	    	
	    	if isglobal:

	    		routes.widget_root=config.base_root+config.vistas_folder+config.widgets_folder
	    		routes.widget_base_url=config.base_url+routes.widget_root[len(config.base_root):]


	    	elif data["control"]=="admin":
	    		routes.widget_root=self.ruta_widget.replace("/user/","/admin/")
	    		routes.widget_base_url=config.base_url.replace("/user/","/admin/")+routes.widget_root[len(config.base_root):]
	    	else:
	    		routes.widget_root=self.ruta_widget
	    		routes.widget_base_url=config.base_url+routes.widget_root[len(config.base_root):]
	    	
	    	
	    	if os.path.exists(routes.widget_root+widgets+".html"):
		    	self.generar(routes.widget_root+widgets+".html",routes.widget_root+widgets+".py","")
		    	
		    	f=open(routes.widget_root+widgets+".py","r")


		    	widget+=f.read()+"\n"


		    	f.close()
		    	doc=""

		    	try:

		    		exec(widget)
		    	except Exception as e:
		    		return e
		    	
		    	return doc	    		
	    	elif os.path.exists(routes.widget_root+widgets+"/"+widgets+".html"):

	    		routes.widget_root+=widgets+"/"
	    		routes.widget_base_url+=widgets+"/"
	    		

		    	self.generar(routes.widget_root+widgets+".html",routes.widget_root+widgets+".py","")
		    	f=open(routes.widget_root+widgets+".py","r")


		    	widget+=f.read()+"\n"

		    	f.close()
		    	doc=""


		    	try:
		    		exec(widget)
		    	except Exception as e:
		    		return e
		    	

		    	return doc


	def do_shortcode(self,string):
	
		try:

		  import imp
		  

		  __plugins__={}
		  __etiquetas__=[]
		  __etiquetas2__=[]

		  for plugin in self.plugins:

		    for short in self.plugins[plugin].shortcodes:
		      
		      __etiquetas__.append(["["+self.plugins[plugin].plugin.name+"-"+short,"]"])


		      if self.plugins[plugin].shortcodes[short].contenedor==True:
		        __etiquetas2__.append("[/"+self.plugins[plugin].plugin.name+"-"+short+"]")
		      else:
		        __etiquetas2__.append(None)
		      

		      
		      __plugins__[self.plugins[plugin].plugin.name+"-"+short]=self.plugins[plugin].shortcodes[short].run

		  return convertir3(string,__etiquetas__,__etiquetas2__,__plugins__)        
		  
		except Exception,e:
		  print "#",e
		
		pass
	def error404(self):

		from settings import config as settings
		self.vista=settings.error404
		self.servir()
	def servir(self):
	  if self.servida==False:

		  import urllib,urllib2 
		  from modulos.ztec.zu import filtrar_datos_planos	  
		  if self.data["app"]!=None:
		  	import settings.config as settings
		  	import settings.routes as routes
		  	routes.base_url=config.base_url+settings.app+"/"
		  self.servida=True
		  notFound=None

		  

		  
		 
		  do_shortcode=self.do_shortcode
		  main_menu=self.main_menu
		  foot_menu=self.foot_menu
		  top_bar_menu=self.top_bar_menu
		  my_acount_menu=self.my_acount_menu

		  
		  from ztec.zu import rstr
		  from ztec.zred import HEAD,TITLE,BASE,LINK,META,STYLE,SCRIPT,NOSCRIPT,BODY,SECTION,NAV,ARTICLE,ASIDE,H1,H2,H3,H4,H5,H6,HEADER,FOOTER,ADDRESS,MAIN,P,HR,PRE,BLOCKQUOTE,OL,UL,LI,DL,DT,DD,FIGURE,FIGCAPTION,DIV,A,EM,STRONG,SMALL,S,CITE,Q,DFN,ABBR,DATA,TIME,CODE,VAR,SAMP,KBD,SUB,SUP,I,B,U,MARK,RUBY,RT,RP,BDI,BDO,SPAN,BR,WBR,INS,DEL,IMG,IFRAME,EMBED,OBJECT,PARAM,VIDEO,AUDIO,MAP,AREA,MATH,TABLE,CAPTION,COLGROUP,COL,TR,TD,FORM,FIELDSET,LEGEND,LABEL,INPUT,BUTTON,SELECT,DATALIST,OPTION,TEXTAREA,KEYGEN,OUTPUT,PROGRESS,METER,DETALIST,COMMAND,MENU,SUMMARY
		  if self.data["control"]=="admin":
		  	
		  	routes.layout_base_root=(config.base_root+config.vistas_folder if self.isglobal==True else self.ruta_widget.replace("/user/","/admin/"))
		  	routes.layout_url=(config.base_url+config.vistas_folder if self.isglobal==True else self.ruta_widget.replace("/user/","/admin/"))+self.vista

		  	routes.template_root=(config.base_root+config.vistas_folder if self.isglobal==True else self.ruta_widget.replace("/user/","/admin/"))+routes.templates_folder+self.vista+".py"

		  	routes.layout_base_url=(config.base_url+config.vistas_folder if self.isglobal==True else config.base_url+self.ruta_widget[len(config.base_root):].replace("/user/","/admin/"))
		  else:
		  	routes.layout_base_root=("../"+config.vistas_folder if self.isglobal==True else self.ruta_widget.replace("/admin/","/user/"))
		  	routes.template_root=("../"+config.vistas_folder if self.isglobal==True else self.ruta_widget.replace("/admin/","/user/"))+routes.templates_folder+self.vista+".py"
		  	routes.layout_base_url=(config.base_url+config.vistas_folder if self.isglobal==True else config.base_url+self.ruta_widget[len(config.base_root):].replace("/admin/","/user/"))

		  if os.path.exists(routes.layout_base_root+self.vista+".html") and self.embebed==None:  
		    	routes.layout_root=routes.layout_base_root+self.vista+".html"
		    	routes.layout_url=routes.layout_base_url+self.vista+".html"

		    	
		    	generar2(routes.layout_root,routes.template_root,"#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
		    	f=open(routes.template_root,"r")
		    	html=f.read() 	
		    	f.close()

		  elif os.path.exists(routes.layout_base_root+self.vista) and self.embebed==None:
	  
		    	routes.layout_root=routes.layout_base_root+self.vista+"/"+self.vista+".html"
		    	routes.layout_url=routes.layout_base_url+self.vista+"/"+self.vista+".html"
		    	generar2(routes.layout_root,routes.template_root,"#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
		    	f=open(routes.template_root,"r")	   
		    	html=f.read() 	
		    	f.close()

		  elif  self.embebed!=None and os.path.exists(routes.layout_base_root+self.vista+".html."+self.embebed):
		    	routes.layout_root=routes.layout_base_root+self.vista+"/"+self.vista+".html."+self.embebed
		    	routes.layout_url=routes.layout_base_url+self.vista+"/"+self.vista+".html."+self.embebed
		    	routes.template_url=routes.layout_base_url+routes.template_folder+self.vista+"."+self.embebed

		    	generar2(routes.layout_root,routes.template_root,"#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
		    	f=open(routes.template_root,"r")	
		    	params = urllib.urlencode({"data":filtrar_datos_planos(self.data)})
		    	f=urllib2.urlopen(routes.template_url+self.vista+self.embebed,params)
		    	html=f.read()         
		    	f.close()

		  elif  self.embebed!=None and os.path.exists(routes.layout_base_root+self.vista+"/"+self.vista+".html."+self.embebed):
		    	routes.layout_root=routes.layout_base_root+self.vista+"/"+self.vista+".html."+self.embebed
		    	routes.layout_url=routes.layout_base_url+self.vista+"/"+self.vista+".html."+self.embebed
		    	routes.template_url=routes.layout_base_url+"../"+routes.template_folder+self.vista+"."+self.embebed

		    	generar2(routes.layout_root,routes.template_root,"#!/usr/bin/python\n# -*- coding: utf-8 -*-\n")
		    	f=open(routes.template_root,"r")	
		    	params = urllib.urlencode({"data":filtrar_datos_planos(self.data)})
		    	f=urllib2.urlopen(routes.template_url+self.vista+self.embebed,params)   
		    	notFound=True
		    	html=f.read()         	
		    	f.close()


		  elif os.path.exists(routes.layout_base_root+self.vista+"."+self.embebed if self.embebed!=None else "php"):
		    	if self.embebed==None:
		    		self.embebed="php"
		    	routes.layout_url=routes.layout_base_url
		    	params = urllib.urlencode({"data":filtrar_datos_planos(self.data)})
		    	f=urllib2.urlopen(routes.layout_url+self.vista+self.embebed,params)        
		    	notFound=True
		    	html=f.read()
		    	f.close()
	

		  if notFound==True or self.embebed!=None:
			print html
			return html
		  else:
			  try:

			  
			    self.HEADERS.show()
			    doc=""
			    data=self.data
			    incluir=self.incluir
			    self.ruta_widget=routes.layout_base_root+routes.widgets_folder
			    
			    ruta_widget=self.ruta_widget



			    exec(html)


			    print doc
			    return doc
			    
			  except Exception as e:
			    import traceback

			    

			    try:
			      exc_type,exc_obj,exc_tb=sys.exc_info()
			      fname = exc_tb.tb_frame.f_code.co_filename
			      print "".join(traceback.format_exception(exc_type,fname,exc_tb)).replace("\n","<br>")
			    except:
			      print e
			    
			    
			    if len(e.args)==2:

			      print e,"<br>"
			      print e.args[1][3]


			    else:
			      print e
