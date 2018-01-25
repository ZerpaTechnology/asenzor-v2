__pragma__("xpath",["","../../../Components"])
__pragma__("alias","s","$")
from Widget import Widget
config=Config.Config()
class CodeMirror(Widget):
	"""docstring for RadioButtonList"""
	def __init__(self, titulo):
		Widget.__init__(self,titulo)
		self._html="""
		<h5>{}</h5>
		<textarea>{}</textarea>
		"""
		self.value=""
		self.data=__new__(FormData)
		self.editor=None
		self.ext="py"
		self.source=config.base_url+"static/js/codemirror-5.27.4/lib/codemirror.js"
		self.styles=[
					config.base_url+"static/js/codemirror-5.27.4/doc/docs.css",
					config.base_url+"static/js/codemirror-5.27.4/lib/codemirror.css",
					config.base_url+"static/js/codemirror-5.27.4/addon/fold/foldgutter.css",
					config.base_url+"static/js/codemirror-5.27.4/addon/dialog/dialog.css",
					config.base_url+"static/js/codemirror-5.27.4/theme/monokai.css",
					]
		self.sources=[
				config.base_url+"static/js/codemirror-5.27.4/addon/display/autorefresh.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/search/searchcursor.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/search/search.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/dialog/dialog.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/edit/matchbrackets.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/edit/closebrackets.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/comment/comment.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/wrap/hardwrap.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/fold/foldcode.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/fold/brace-fold.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/javascript/javascript.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/python/python.js",
				config.base_url+"static/js/codemirror-5.27.4/keymap/sublime.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/selection/selection-pointer.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/xml/xml.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/javascript/javascript.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/css/css.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/vbscript/vbscript.js",
				config.base_url+"static/js/codemirror-5.27.4/mode/htmlmixed/htmlmixed.js",
				config.base_url+"static/js/codemirror-5.27.4/addon/emmet/dist/emmet.js"]

		
	def add(self,target):
		if self._update:
			target.update()
			self.content(self).append(target.target)
		else:
			self.children.append(target)
	def success(self):
		window.alert(self.value)
	def send(self):
		for k,elem in enumerate(s(".tab")):
          if not s(elem).hasClass("hidden"):
           break
	   
	   self.data.append("manager",rest["manager"])
	   self.data.append("app",rest["app"])
	   self.data.append("metodo","write")
	   self.data.append("control","admin")
	   self.data.append("path",s(".path")[k].innerText)
	   self.data.append("file",str(window.editores[k].getDoc().getValue()))
	   
	   s.ajax({
	    "url":config.base_url,
	    "data":data,
	    "cache":False,
	    "contentType":False,
	    "processData":False,
	    "type":"POST",
	    "method":"POST",
	    "success":self.success
	    }) 
	   for k,tab in enumerate(s(".tab")):
	    if not s(tab).hasClass("hidden"):
	      break
	   if s("#borrar")==[]:
	        s("#btns-action")[0].innerHTML+="<button id='borrar'>Borrar</button>"
	   
	   update()

	def reconectar(self):
		
		
			
			if (self.ext=="py"):
				mixedMode = {
		        	"name": "python",
		        	"scriptTypes": [{"matches": "/\/x-handlebars-template|\/x-mustache/i",
		                       "mode": None},
		                      {"matches": "/(text|application)\/(x-)?vb(a|script)/i",
		                       "mode": "vbscript"}]
		      		}
			
			else:
		 		mixedMode = {
			        "name": "htmlmixed",
			        "scriptTypes": [{"matches": "/\/x-handlebars-template|\/x-mustache/i",
			                       "mode": None},
			                      {"matches":"/(text|application)\/(x-)?vb(a|script)/i",
			                       "mode": "vbscript"}]
			      }
		
	  		self.editor=CodeMirror.fromTextArea(self.target.find(">textarea"), {
	  			"lineNumbers": True,
	  			"mode": mixedMode ,
	  			"keyMap": "sublime",
	  			"autoCloseBrackets": True,
	  			"matchBrackets": True,
	  			"showCursorWhenSelecting": True,
	  			"theme": "monokai",
	  			"tabSize": 4,
	  			"selectionPointer": True
	  			})
  
			  emmetCodeMirror(editor);
  			
  		shortcut.add("Ctrl+s",self.send)
  		
  	def forceSources(self):
  		for elem in self.sources:
				s("footer").append("<script src='{}'></script>".format(elem))

	def forceStyles(self):
		for elem in self.styles:
				s("footer").append("<link rel='stylesheet' href='{}'>".format(elem))



	def update(self):
		self.format=[self.titulo,self.value]
		self.__update__()
		if "CodeMirror" not in dir(window):

			self.forceStyles()
			self.forceSources()

			def cargar():
				self.reconectar()

			setInterval(cargar,1000)
		else:
			self.reconectar()

		

			





