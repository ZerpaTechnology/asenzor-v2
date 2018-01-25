__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")

from Widget import Widget

class SubmitButton(Widget):
	def __init__(self,titulo="Subir archivo",url=None):
		Widget.__init__(self,titulo)
		self._html="<button>{}</button>"
		
		self._titulo=self.titulo
		self.data={}
		self.url=url
		self.status=None
	
	def addData(self,nombre,component):
		self.data[nombre]=component
	def exito(self,data):
		self.status=True
	def fail(self,data):
		self.status=False
	
	def clear(self):
		self.status=None

	def send(self,evt):
		data={}
		for elem in list(self.data):
			data[elem]=self.data[elem].value
		s.post(self.url,data).done(exito).fail(self.fail)



	def update(self):
		
		s(self.target).html(self._html.format(self.titulo))
		s(self.target).find("button").bind("click",self.send)

