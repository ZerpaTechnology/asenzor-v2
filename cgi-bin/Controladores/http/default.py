
from Controladores.http.Blog import Blog
from Controladores.http.Login import Login
from settings import config as settings
from config import config
class default(Blog,Login):
	def __init__(self,data):
		Login.__init__(self,data)
		Blog.__init__(self,data)
		self.vista="index"
		self.data["base_url"]=config.base_url+config.apps_folder+settings.app+"/user/"
		
		self.modelo=data["model"]["paginas"]
		self.data["page"]=self.data["model"]["paginas"].obtenerFilas("Paginas")[0][1]
		self.vistas=[]
	


	

		
		