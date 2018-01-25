__pragma__("alias","s","$")
from Widget import Widget
from BasicTabs import BasicTabs
from TinyMCE import TinyMCE
from Button import Button
from Input import Input
class ModuloHTML(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Insertar Modulo"):
		Widget.__init__(self,titulo)
		self._html="""
		<button>
		<span class='icon'></span>
		<b class='titulo'></b>
		</button>
		""" #HTML para la ventana de insertar modulo
		self._html2=self._html #HTML para la columna
		self._html3=""#HTML para la ventana de configuraciones
		self.BasicTabs=BasicTabs()
		self.window=None
		self.column=None
		self._contenido=""
		self.dataChildren=[{},{},{}]


		

	def titulo(self,titulo):
		self.__titulo.text(titulo)
		self._titulo=titulo

	def insertar(self,evt):

		self.column.add(self,2)
		self.window.close()
		

	def open(self,evt):
		
		self.window.Modulo=self

		self.window._nav=[["General Settings","settings",lambda self2:lambda evt: self.BasicTabs.showTab(0)],
					["Custom CSS","load",lambda self2:lambda evt: self.BasicTabs.showTab(1)],
					]
		self.window._footerNav=[["Guardar","save",lambda self2:lambda evt: None],
					
					]
		self.window.open("Modulo")

	def done(self):

		self.BasicTabs.width="100%"
		self.BasicTabs.tabWidth="100%"
		self.BasicTabs.update()
		i=Input("Titulo:")
		t=TinyMCE("Contenido:")
		t.data=self.dataChildren[1]


		if "value" in self.dataChildren[1]:
			t.value=self.dataChildren[1]["value"]

		



		s.when(self.target3.html(self.BasicTabs.target)).then(self.BasicTabs.done)
		self.BasicTabs.appendToTab(0,i)
		self.BasicTabs.appendToTab(0,t)
		

		
		
		
		self.target.find(">button").on("click",self.insertar)
		self.target2.find(">button").find(">.titulo").text("prueba")
		self.target2.find(">button").on("click",self.open)
		
		
		self.__titulo=self.target.find(">button").find(">.titulo")
		self.titulo(self._titulo)

		t.reconectar()
		

		
	
	def update(self):
		self.format=[self._titulo]
		self.__update__()
		
		
		#=========================================	
		