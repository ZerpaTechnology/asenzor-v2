from modulos.ztec.zmodel import Model
from modulos.ztec import zu
import sys
try:
	from config import config
except:
	import config
from modulos.ztec.zdb import DB
from modulos.ztec import zu
class model(Model):
	
	def activarPlugin(self,plugin):#activa/desactiva
		if self.request():
			for k,elem in enumerate(self.obtenerFilas("Plugins")):
				if elem[0]==plugin:
					return self.models["main"].activarPlugin(plugin)

	
	def instalarPlugin(self,plugin):
		if self.request():
			
			f=open(config.base_root+config.plugins_folder+plugin+"/install_db.py","r")
			source=f.read()
			f.close()
			db=self.db
			insertar=True
			for k,elem in enumerate(self.obtenerFilas("Plugins")):
				if elem[0]==plugin:
					insertar=False
					break
			dbfile=self.models["main"].dbfile
			
			i=len(self.obtenerFilas("Plugins"))
			exec(source)
			
			if insertar:
				
				self.db.registro=db.registro
				self.grabar()

				for elem in self.obtenerFilas("apps"):
					temp=dbfile.split("/")
					pos=temp.index(config.apps_dir)
					temp[pos+1]=elem[0]
					temp="/".join(temp)
					
					if self.models["main"].request(temp):
						self.models["main"].db("Plugins").insertar(plugin,False)						
						self.models["main"].grabar()
						
			else:
				self.db("Plugins").modificarCampo(k,"Contenido",db("Plugins").obtenerFilasValores("Contenido")[-1])
				self.grabar()
			

			return True


