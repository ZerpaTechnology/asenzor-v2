PATH:"../../../Components"
#==========Cabeceras y codifo PYTHON========================================
from SliderCustomize import SliderCustomize
from BasicSlider import BasicSlider
__pragma__("alias","s","$") #uso de pragmas

#========CONSTRUCCION DEL FRONTEND================================
.SidebarCustomize[#self]
	"""
	Estos son los comentarios multilinea tradicionales de python
	"""
	__init__(self,titulo):
		Widget.__init__(self,titulo)
		self.html="""
			<div class='header-top'>
				<span class='close'> X </span><button name='save'>{}</button>
			</div>
			<div class='content'>
			</div>
			<div class='footer-bottom'>
				
				<span class='ocultar'> 
					<span class='icon'></span>
					<span class='text'>{}</span>
				</span>
				<div class='responsive'>
					<span class='desktop'></span>
					<span class='tablet'></span>
					<span class='phone'></span>
				</div>
				
			</div>
		"""
		self.content=lambda:self=self:self.target.find(">.content")
		self.btn_save="Guardar"
		self.btn_desing="Ocultar"
		self.btn_desktop=config.base_url+"static/imgs/iconos/desktop.png"
		self.btn_tablet=config.base_url+"static/imgs/iconos/tablet.png"
		self.btn_phone=config.base_url+"static/imgs/iconos/smartphone.png"
	metodo(self):
		alert("hola mundo ")
	#los selectores debe ser los ultimos en colocarse
	"""
	para no usar __update__ basta sobrescribir el metodo por ejemplo:

	__update__(self):
		pass

	"""

	#selectores y eventos se aplican despues del metodo __update__
	$(">.header-top").css:#selector de estilos
		background-color:white
	$(">.footer-bottom").css:
		$(">.responsive"):
			#ejemplo de selectores decendentes
			$(">.desktop"):
			$(">.tablet"):
			$(">.phone"):

	$(">.ocultar>.icon").bind('click',self.metodo):#selector de eventos
	#por defecto la adicion de widgets se hace en el update 
	.BasicSlider("",10) [#slider] #identificador
		&add:self.add #metodo de adicion de widget por defecto no es necesario colocar
		.BasicTabs [#screen1]
			.HeaderCustomizeMain
			.BandaTema
			.ButtonSettings("Identidad del sitio")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=0
			.ButtonSettings("Colores")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=1

			.ButtonSettings("Cabecera multimedia")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=2
			.ButtonSettings("Menus")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=3
			.ButtonSettings("Widgets")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=4
			.ButtonSettings("Portada estatica")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=5
			.ButtonSettings("Themes options")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=6
			.ButtonSettings("CSS adicional")
				self.slider=[#slider]
				self.screen=[#screen1]
				self._screen=7
			


		.BasicTabs("",10) [#screen2]
			&add:self.appendToTab #esto significa el metodo de adicion de widgets a usar
			.Identidad_del_sitio("Identidad del sitio")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0
			.CabeceraMultimedia("Cabecera Multimedia")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0
			.Menus("Menus")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0
			.Widgets("Widgets")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0
			.PortadaEstatica("Portada estatica")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0
			.ThemesOptions("Themes Options")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0
			.PortadaEstatica("Portada estatica")
				self.Media=[#self].Media
				self.slider=[#slider]
				self._atras=0
				self._screen=0

