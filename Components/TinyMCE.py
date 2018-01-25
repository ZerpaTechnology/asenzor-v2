__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
class TinyMCE(Widget):
	"""docstring for RadioButtonList"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""
		<h5>{}</h5>
		<textarea>{}</textarea>
		"""
		self.editor=None

		self.value=""
		
		self._load_js=[config.base_url+"static/js/tinymce/js/tinymce/tinymce.min.js",config.base_url+"static/js/tinymce/js/tinymce/jquery.tinymce.min.js"]
		self.styles=[]
		self.content_css=config.base_url+"static/js/tinymce/js/tinymce/skins/lightgray/content.min.css"
		self.lang="es"
		self.theme="modern"
		self.fontsize_formats="9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 18pt 20pt 22pt 24pt"
		self.content=lambda self:self.target.find(">textarea")
		self.code_langs=[
		        {"text": 'HTML/XML', "value": 'markup'},
		        {"text": 'JavaScript', "value": 'javascript'},
		        {"text": 'CSS', "value": 'css'},
		        {"text": 'PHP', "value": 'php'},
		        {"text": 'Ruby', "value": 'ruby'},
		        {"text": 'Python', "value": 'python'},
		        {"text": 'Java', "value": 'java'},
		        {"text": 'C', "value": 'c'},
		        {"text": 'C#', "value": 'csharp'},
		        {"text": 'C++', "value": 'cpp'}
		    ]
		self.plugins=[
		         "advlist autolink link image lists charmap print preview hr anchor pagebreak table",
		         "searchreplace wordcount visualblocks visualchars fullscreen insertdatetime media nonbreaking emoticons textcolor",
		         "save table contextmenu directionality emoticons template paste textcolor",
		         "code codesample"
		   ]
		self.toolbar="insertfile undo redo preview | fontselect | fontsizeselect | forecolor backcolor emoticons | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | media fullpage code codesample"
		self.font_formats="Andale Mono=andale mono,times;"+\
		        "Arial=arial,helvetica,sans-serif;"+\
		        "Arial Black=arial black,avant garde;"+\
		        "Book Antiqua=book antiqua,palatino;"+\
		        "Comic Sans MS=comic sans ms,sans-serif;"+\
		        "Courier New=courier new,courier;"+\
		        "Georgia=georgia,palatino;"+\
		        "Helvetica=helvetica;"+\
		        "Impact=impact,chicago;"+\
		        "Symbol=symbol;"+\
		        "Tahoma=tahoma,arial,helvetica,sans-serif;"+\
		        "Terminal=terminal,monaco;"+\
		        "Times New Roman=times new roman,times;"+\
		        "Trebuchet MS=trebuchet ms,geneva;"+\
		        "Verdana=verdana,geneva;"+\
		        "Webdings=webdings;"+\
		        "Wingdings=wingdings,zapf dingbats",
		Widget.load_sources(self)
		
	def add(self,target):
		if self._update:
			target.update()
			self.content(self).append(target.target)
		else:
			self.children.append(target)

	def reconectar(self,timout=0):
			def cargar():
				nonlocal self
				self.target.find(">textarea").tinymce({"language" : self.lang,
			   "theme": self.theme,
			   "plugins": self.plugins,
			   "codesample_languages": self.code_langs,
			   "content_css": self.content_css,
			   #"toolbar": self.toolbar, 
			   "fontsize_formats": self.fontsize_formats,
			   "font_formats": self.font_formats})
			setTimeout(cargar,timout)
			



			

	def forceSources(self):
  		for elem in self.sources:
  			s("footer").append("<script src='{}'></script>".format(elem))

	def forceStyles(self):
		for elem in self.styles:
			s("footer").append("<link rel='stylesheet' href='{}'>".format(elem))
	def valueCacher(self):
		
		self.value=self.target.find(">textarea").val()
		print(self.value)
		
		self.data["value"]=self.value
		

	
	def done(self):
		self.target.find(">textarea").on("keyup",self.valueCacher)


	def update(self):
		
		self.format=[self._titulo,self.value]
		self.__update__()
		
		

		
		
		
		


			





