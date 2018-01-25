__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class DetalleImagen(Widget):
	def __init__(self,titulo="Subir archivo",Media=None):
		Widget.__init__(self,titulo)
		self._html="<img src='{}' titulo='{}' leyenda='{}' _alt='{}' ><span class='select'></span>"
		self.Media=Media
		self._titulo=self.titulo
		self.url=""
		self.leyenda=""
		self._alt=""
		self.marcado=None # True (actual) | False (marcado) | None (desmarcado)
		self.hermanos=[]
		self.tipo=""
		self.ultimaModificacion=""
		self.size=""
		self.fechaUltimaModificacion=""
		self.indice=0
	def click(self,evt):
		if evt.shiftKey:
			self.marcarHastaActual()

		elif evt.ctrlKey:
			if self.marcado==None:
				self.seleccionarMarcados()
				self.marcar()
			else:
				self.desmarcar()

		else:
			if self.marcado==False or self.marcado==None:
				
				self.marcarSolo()
			else:
				self.desmarcarTodo()

		self.hayMarcas()




	def marcar(self):
		
		marcador=s(self.target).find(".select")
		self.Media.biblioteca.target.find(".detalles").find("[name='titulo']").val(self.titulo)
		self.Media.biblioteca.target.find(".detalles").find(".titulo").html("DETALLES DE ADJUNTOS")
		self.Media.biblioteca.target.find(".detalles").find(".info").html("<br>".join([self.titulo,self.fechaUltimaModificacion,self.size,self.tipo]))
		self.Media.biblioteca.target.find(".detalles").find("[name='url']").val(self.url)
		self.Media.biblioteca.target.find(".detalles").find("[name='descripcion']").val(self._alt)

		self.Media.biblioteca.target.find(".detalles").find("img").attr("src",self.url)
		self.Media.biblioteca.target.find(".detalles").find("img").removeClass("hidden")
		self.Media.biblioteca.currents.append(self.url)
		s(self.target).css({"border":"solid","border-color":"blue"})
		marcador.css({"border":"solid","border-color":"blue"})
		self.marcado=True
			


	def marcarSolo(self):

			self.desmarcarHermanos()
			marcador=s(self.target).find(".select")
			self.Media.biblioteca.target.find(".detalles").find("[name='titulo']").val(self.titulo)
			self.Media.biblioteca.target.find(".detalles").find(".titulo").html("DETALLES DE ADJUNTOS")
			self.Media.biblioteca.target.find(".detalles").find(".info").html("<br>".join([self.titulo,self.fechaUltimaModificacion,self.size,self.tipo]))
			self.Media.biblioteca.target.find(".detalles").find("[name='url']").val(self.url)
			self.Media.biblioteca.target.find(".detalles").find("[name='descripcion']").val(self._alt)

			self.Media.biblioteca.target.find(".detalles").find("img").attr("src",self.url)
			self.Media.biblioteca.target.find(".detalles").find("img").removeClass("hidden")
			self.Media.biblioteca.current=self.url
			marcador.css({"border-color":"blue"})
			s(self.target).css({"border":"solid","border-color":"blue"})
			s(self.target).find(".select").css({"border":"solid","border-color":"blue"})
			self.marcado=True	
			
			
	



			
	def actualizarHermanos(self,widgets):
		self.hermanos=widgets
		

	def deseleccionar(self):
		self.marcado=False
		s(self.target).css({"border":"solid","border-color":"transparent","box-shadow":"5px rgb(100,100,200)"})
		s(self.target).find(".select").css({"border":"solid","border-color":"gray"})

	def desmarcar(self):
		self.marcado=None
		s(self.target).css({"border":"solid","border-color":"transparent","box-shadow":"none"})
		s(self.target).find(".select").css({"border":"solid","border-color":"transparent"})

	def desmarcarHermanos(self):
		
		for elem in self.hermanos:
			if elem.target !=self.target:
				elem.desmarcar()
		self.marcado=None
		self.hayMarcas()
		

	def desmarcarTodo(self):
		for elem in self.hermanos:
			elem.desmarcar()
		self.hayMarcas()
			
			

	def hayMarcas(self):
		
		seleccionados=[]
		for elem in self.hermanos:
			if elem.marcado!=None:
				seleccionados.append(elem)

		if len(seleccionados)==0:
			self.Media.noSeleccionados()
		else:
			self.Media.seleccionados(seleccionados)
	def refresh(self,src=None):
		if src==None:
			src=s(self.target).find("img").attr("src")			
		s(self.target).find("img").attr("src",src)



	def seleccionar(self):
		
		s(self.target).css({"border":"solid","border-color":"gray","box-shadow":"none"})
		s(self.target).find(".select").css({"border":"solid","border-color":"gray"})
		self.marcado=False
	def seleccionarMarcados(self):
		for elem in self.hermanos:
			if elem.marcado==True:
				elem.seleccionar()

	def marcarHastaActual(self):
		desde=None
		for k,elem in enumerate(self.hermanos):
			if elem.marcado==True and desde==None:
				desde=k
		hasta=self.hermanos.index(self)
		
		if desde<hasta:
			for elem in self.hermanos[desde:hasta]:
				elem.seleccionar()
		else:
			for elem in self.hermanos[hasta:desde+1]:
				elem.seleccionar()
		self.marcar()










	def update(self):
		
		s(self.target).html(self._html.format(self.url,self.titulo,self.leyenda.replace('"',"&#34;").replace("'","&#39;"),self._alt.replace('"',"&#34;").replace("'","&#39;")))
		s(self.target).find(".select").addClass("hidden")
		
		s(self.target).bind("click",self.click)
		s(self.target).find("img").bind("click",lambda evt: s(evt.target).trigger("marcar",[self.target]))
		
		
		s(self.target).find("button").bind("click",self.open)

