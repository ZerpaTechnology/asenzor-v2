__pragma__("xpath",["../","../../static/js/python/"])
__pragma__("alias","s","$")

from Widget import Widget
from BasicTabs import BasicTabs


config=Config.Config()

class InsertColumns(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Insertar Columnas"):
		Widget.__init__(self,titulo)
		self._html="<div class='content'></div>"
		
		
		
		self._columns={"1":config.base_url+"static/imgs/columna-1.png",
		"1/2-1/4-1/4":config.base_url+"static/imgs/columna-1_2-1_4-1_4.png",
		"1/4-1/4-1/2":config.base_url+"static/imgs/columna-1_4-1_4-1_2.png",
		"1/3":config.base_url+"static/imgs/columna-1_3.png",
		"3/4-1/4":config.base_url+"static/imgs/columna-3_4-1_4-.png",
		"1/4-3/4":config.base_url+"static/imgs/columna-1_4-3_4-.png",
		"1/2":config.base_url+"static/imgs/columna-1_2.png",
		"1/4":config.base_url+"static/imgs/columna-1_4.png",
		}
		self.library={"nombre":[{"1/2":["modulo"]}
								]}
		self.row=0
		self.BasicTabs=BasicTabs(2)
		self.BasicTabs.tabWidth="100%"
		self.BasicTabs.width="100%"
		





	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	
	
	def insertar(self,evt):
		col=["md-12"]
		
		if s(evt.target).attr("name")=="1":
			col=["md-12"]
		elif s(evt.target).attr("name")=="1/2-1/4-1/4":
			col=["md-6","md-3","md-3"]
		elif s(evt.target).attr("name")=="1/4-1/4-1/2":
			col=["md-3","md-3","md-6"]
		elif s(evt.target).attr("name")=="1/3":
			col=["md-4","md-4","md-4"]
		elif s(evt.target).attr("name")=="1/3":
			col=["md-4","md-4","md-4"]
		elif s(evt.target).attr("name")=="3/4-1/4":
			col=["md-8","md-4"]
		elif s(evt.target).attr("name")=="1/4-3/4":
			col=["md-4","md-8"]
		elif s(evt.target).attr("name")=="1/2":
			col=["md-6","md-6"]
		elif s(evt.target).attr("name")=="1/4":
			col=["md-3","md-3","md-3","md-3"]

		self.Builder.addCols(self.row,col)
		self.Builder.window.close()

	def tabNew(self,evt):
		self.BasicTabs.showTab(0)
	def tabLoad(self,evt):
		self.BasicTabs.showTab(1)
	def done(self):
		pass
		
		

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.Builder.window._nav=[["Nueva columna","new",lambda self:lambda evt: None],
					["Cargar de la libreria","load",lambda self:lambda evt: None],
					]

		self.BasicTabs.update()
		
		for elem in self._columns.keys():
			

			img=s("<img>")
			self.BasicTabs.appendToTab(0,img)	
			img.attr("src",self._columns[elem])
			img.attr("name",elem)
			img.css({"width": "300px","margin": "10px","cursor":"pointer"})
			img.bind("click",self.insertar)
		self.target.find(">.content").append(self.BasicTabs.target)
		
		return self.target
		


		
		
		
		
		#self.__new=self.target.find(">.header").find(">.btns").find(">.btns-left").find(">.new")
		#self.__load=self.target.find(">.header").find(">.btns").find(">.btns-left").find(">.load")
		
		#self.__new.on("click",self.tabNew)
		#self.__load.on("click",self.tabLoad)

		
	
	
		


		