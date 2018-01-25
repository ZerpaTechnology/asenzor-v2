__pragma__("alias","s","$")
from Widget import Widget
from Popup import Popup
from SwiperSlider import SwiperSlider
from BoxText import BoxText
class PopupExplication(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Popup.__init__(self,titulo)
		self._html="""
		<div class='container'>
		<div class='row'>
		<div class='col-md-6 col-xs-12 left'>
		</div>
		<div class='col-md-6 col-xs-12 right'>
		</div>
		</div>

		</div>
		"""
		self.target.find(">.content").html(self._html)
		self.slider=SwiperSlider()
		self.BoxText=BoxText()


		
		
	def titulo(self,titulo):
		self.target.find(".titulo").text(titulo)
		self._titulo=titulo

	def update(self):
		self.format=[self._titulo]
		self.__update__()
		self.__titulo=self.target.find(">.titulo")
		self.titulo(self._titulo)
		self.slider.update()
		self.BoxText.update()
		s(self.target.find(".>content").find(">.container").find(">.row").find(">.col-md-6")[0]).html(self.slider.target)
		s(self.target.find(".>content").find(">.container").find(">.row").find(">.col-md-6")[1]).html(self.BoxText.target)
		
	
	
		


		