__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget
from DetalleImagen import DetalleImagen
config=Config.Config()
settings=nuclear.Settings()
class Biblioteca(Widget):
	def __init__(self,titulo="Subir archivo",Media=None):
		Widget.__init__(self,titulo)
		self._html="""
		<div class='archivos'>
		<div><span>{}</span> <input type='search' placeholder='{}'></div>
		<div class='list'>
		</div>
		</div>
		<div class='detalles'>
		<b class='titulo'></b>
		<img class='hidden' src=''>
		<div class='info'></div>
		<hr>
		<table>
		<tr>
		<td> URL </td>
		<td><input name='url'></td>
		</tr>
		<tr>
		<td>Titulo</td>
		<td><input name='titulo'></td>
		</tr>
		<tr>
		<td>Leyenda</td>
		<td><textarea name='leyenda'></textarea></td>
		</tr>
		<tr>
		<td> Texto alternativo </td>
		<td><input name='alternativo'></td>
		</tr>
		<tr>
		<td> Descripción </td>
		<td><textarea name='decripcion'></textarea></td>
		</tr>
		
		</table>

		</div>
		"""
		
		self.Media=Media
		self._titulo=self.titulo
		self.sugerencias="Dimensiones de imagen sugeridas: 150 por 150 píxeles."
		self.placeholder="Buscar elementos multimedia..."

		self.archivos=[]
		self.currents=[]
		self.base_url=config.base_url+config.apps_folder+settings.app+"/admin/static/archivos/Imagenes/"

	
	def open(self):
		self.Media.updateTitulo(self._titulo)
		self.Media.open()
	def search(self,evt):
		for elem in self.archivos:
			if s(evt.target).val().lower() not in elem.titulo.lower():
				s(elem.target).addClass("hidden")
			else:
				s(elem.target).removeClass("hidden")


	def getFiles(self):
		def success(data):
			archivos=nuclear.normalizar(data)
			
			for elem in archivos:
				i=DetalleImagen()
				i.titulo=elem[0]
				i.url=config.base_url+config.apps_folder+settings.app+"/admin/static/archivos/Imagenes/"+nuclear.thumbail(i.titulo)
				self.archivos.append(i)
		def error(objRequest):
			pass
		__pragma__("js","{}","""
          $.ajax({url:self.url,
                  async:false,
                  success: success,
                  error : error
                  })
          """)
	def nueva(self,file,src):
		i=DetalleImagen()
		def cargar():
			nonlocal i
			i.refresh()
			clearInterval(invervalo)
		invervalo=setInterval(cargar,3000)
		self.Media.tabsManger.showTab(1)
		i.url=src if src!=None else self.base_url+nuclear.thumbail(__pragma__("js","{}","file.name"))
		i.titulo=__pragma__("js","{}","file.name")
		i.ultimaModificacion=__pragma__("js","{}","file.lastModified")
		i.fechaUltimaModificacion=__pragma__("js","{}","file.lastModifiedDate")
		i.size=__pragma__("js","{}","file.size")
		i.tipo=__pragma__("js","{}","file.type")
		self.archivos.append(i)
		i.actualizarHermanos(self.archivos)
		i.Media=self.Media
		i.update()
		i.indice=len(self.archivos)-1
		s(self.target).find(".archivos").find(".list").prepend(i.target)
	def clearDetalles(self):
		self.target.find(".detalles").find("[name='titulo']").val("")
		self.target.find(".detalles").find(".titulo").html("")
		self.target.find(".detalles").find(".info").html("")
		self.target.find(".detalles").find("[name='url']").val("")
		self.target.find(".detalles").find("[name='descripcion']").val("")

		self.target.find(".detalles").find("img").attr("src","")
		self.target.find(".detalles").find("img").addClass("hidden")
		self.currents.append(self.url)



		

	def update(self):
		self.getFiles()
		s(self.target).html(self._html.format(self.sugerencias,self.placeholder))
		for k,i in enumerate(self.archivos):
			i.Media=self.Media
			i.actualizarHermanos(self.archivos)
			i.deseleccionar(self.archivos)
			i.update()
			i.indice=k
			s(self.target).find(".archivos").find(".list").append(i.target)
		s(self.target).find(".archivos").find("input[type='search']").bind("keyup",self.search)
		
		s(self.target).find("button").bind("click",self.open)

