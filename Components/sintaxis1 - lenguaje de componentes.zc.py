PATH:"../../../Components"
from SliderCustomize import SliderCustomize
from BasicSlider import BasicSlider

.SidebarCustomize[#self]
	"""
	Estos son los comentarios multilinea tradicionales de python
	"""
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

