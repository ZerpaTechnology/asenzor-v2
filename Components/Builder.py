__pragma__("xpath",["_Builder/",
					])
__pragma__("alias","s","$")
from Widget import Widget
from _Builder.Row import Row
from _Builder.Column import  Column
from _Builder.Modulo import Modulo
from _Builder.Window import Window

class Builder(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo="Builder-Z")
		self._html="""
		<div class='header'>
			<div>
			<b class='titulo'></b>
			<div>
				<span class='minimizar'></span>
			</div>

			</div>
			
			<div class='btns'>
				<div class='btns-left'>
					<span class='save'>Guardar libreria</span>
					<span class='load'>Cargar libreria</span>
					<span class='clear'>Limpiar layout</span>
				</div>
				<div class='btns-right'>
					<span class='deshacer'></span>
					<span class='rehacer'></span>
					<span class='historial'></span>
				</div>
			</div>
		</div>
		<div class='content'>
		<span class='add'> Añadir </span>
		</div>		
		<div class='window'></div>
		"""

		
		
		
		self._rows=[]
		self.window=Window()
		self.window.Builder=self


		
		
		

	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def appendRow(self):
		row=Row()
		

		self._rows.append(row)
		row.i=self._rows.index(row)
		row.window=self.window
		row.update()
		s.when(self.target.find(">.content").find(">.add").before(row.target)).then(row.done)
		

	def moveRow(self,acutal,destino):
		pass
	def changeRow(self,acutal,destino):
		pass

	def addCols(self,row,lista=None):
		print(lista)
		if lista==None:
			self._rows[row].InsertColumns.open()
		else:
		
			for elem in lista:
				if type(elem)!=str:
					clase=""
					col=Column()
					


					for elem2 in elem:
						if "md-" in elem2:
							
							col.size=int(elem2.replace("md-",""))
							col._titulo=str(col.size)
							col.window=self.window
							
						clase=clase+" col-"+elem2
					
					
					self._rows[row].add(col)
					

				else:
				
					col=Column()
					
					col.size=int(elem.replace("md-",""))
					col._titulo=str(col.size)
					col.window=self.window
					
					self._rows[row].add(col)
			
					

	def addToCol(self,row,col,widget):
		widget.update()
		s.when(s(s(self.target.find(">.row")[row]).find(">div")[col]).html(widget.target)).then(widget.done)
		return s(s(self.target.find(">.row")[row]).find(">div")[col])




	def addModulo(self,row,col,modulo=None):
		if modulo=="default":
			m=Modulo(modulo)
			self._rows[row].children[col].add(m)
	def done(self):
		pass


	def update(self):


		self.format=[self._titulo]
		self.window.update()
		
		self.__update__()
		self.__button=self.target.find(">button")
		self.__add=self.target.find(">.content").find(">.add")
		self.__add.on("click",self.appendRow)
		self.titulo(self._titulo)
		
		
		s.when(self.target.find(">.window").html(self.window.target)).then(self.window.done)
		
		
		"""
		self.InsertColumns.update()
		self.InsertModulo.update()
		self.target.append(self.InsertColumns.target)
		self.target.append(self.InsertModulo.target)
		"""
		self.window.hidden()

		self.__titulo=self.target.find(">.titulo")
		
	
	
		


		