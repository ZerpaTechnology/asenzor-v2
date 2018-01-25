__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class FileUpload(Widget):
	"""docstring for HeaderCustomize"""
	def __init__(self, titulo="Arrastra archivos a cualquier lugar para subirlos"):
		Widget.__init__(self,titulo)		
		self._html="""
		<div>
		<form method='post' enctype='multipart/form-data' action='{}'>
		<h3>{}</h3>
		<div>o</div> 
		<input type='file' name='archivo'>
		{}
		</form>
		<iframe name='fileupload' class='hidden'></iframe>
		</div>
		"""
		self.restricciones="""
		<p>Tamaño máximo de archivo: 128 MB.</p>
		<p>Dimensiones de imagen sugeridas: 150 por 150 píxeles.</p>
		"""
		self.avanzado=False
		self.activador=True
		self.automatico=False
		self.action=""
		self.categorias=[]
		self.tipos=[]
		self.iframe=""


	def enlazar(self,funcion):
		self.activador=funcion
	def subidaAutomatica(self,evt):
		
		for _file in s(evt.target)[0].files:
			if self.activador!=None:
				s(self.target).find("form").submit()
				self.activador(_file,None)

	def subir(self,evt):
		 files = s(evt.target)[0].files
		 reader =__new__(FileReader)()
		 for file in files:
			 if not self.automatico:
			 	def ver(evt,file=file):
			 		if self.activador!=None:
			 			self.activador(file,evt.target.result)
			 	reader.onload=ver
			 	f = reader.readAsDataURL(file)
			 


   
	def update(self):
		s(self.target).html(self._html.format(self.action,self.titulo,self.restricciones))
		if self.avanzado==False:
			avanzado= " class='hidden'"
		else:
			avanzado=""
		
		

		_html="<div "+avanzado+">Renombrar: <input name='renombre' > </div>"
		
		_html+="<div "+avanzado+">Categorias: <select name='opcion'>"
		for k,elem in enumerate(self.categorias):
			_html+="<option value='"+str(k)+"' " +('selected' if k==0 else '')+">"+elem+"</option>"
		_html+="</select></div>"
	
		_html+="<div "+avanzado+">Tipo: <select name='tipo'>"
		for k,elem in enumerate(self.tipos):
			_html+="<option value='"+str(k)+"' " +('selected' if k==0 else '')+">"+elem+"</option>"
		_html+="</select></div>"
		_html+="<div "+avanzado+"> Sobrescribir: <input type='checkbox' name='sobrescribir'></div>"
		s(self.target).find("form").append(_html)
		s(self.target).find("form").attr("target","fileupload")


		

		archivo=s(self.target).find("input[type='file']")
		if self.automatico:
			archivo.bind('change',self.subidaAutomatica)
		else:
			archivo.bind("change",self.subir)

		

		
		

	
		