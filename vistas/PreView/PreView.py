from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.Window import alert

class PreView(SimplePanel):
	"""docstring for PreView"""
	def __init__(self):
		SimplePanel.__init__(self)
		f=open("texto.txt","r")
		script=f.read()
		f.close()
		alert(script)


if __name__=="__main__":
	RootPanel().add(PreView())

		