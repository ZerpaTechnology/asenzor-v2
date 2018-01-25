__pragma__("alias","s","$")
__pragma__("xpath",["","../../../Components"])
def copy(objeto):
			if "__class__" in dir(objeto):
				if objeto.prototype!=None: 
					
					o=__new__(objeto.prototype.constructor)
					for elem in dir(o):
						if __pragma__("js","{}"," typeof getattr(o,elem)!='function'"):
							setattr(o,elem,copy(getattr(objeto,elem)))
					
				else:
					if __pragma__("js","{}","objeto.__proto__.constructor==Array"):
						l=[]
						for elem in objeto:
							l.append(copy(elem))
						o=Object.assign([],l)
					elif objeto==None:
						o=objeto
					elif __pragma__("js","{}","objeto.__proto__.constructor==String") or __pragma__("js","{}","objeto.__proto__.constructor==Number") or __pragma__("js","{}","objeto.__proto__.constructor==Boolean"):
						o=objeto
					elif __pragma__("js","{}","objeto.__proto__.constructor==Function") :
						o=objeto.prototype.constructor
					else:
						
						d={}
						for elem in objeto:
							
							d[elem]=copy(objeto[elem])				
						o=Object.assign({},d)


			else:
				if type(objeto)==str or type(objeto)==int or type(objeto)==float or type(objeto)==bool:
					
					o=objeto.valueOf()
				elif type(objeto)!=str and type(objeto)!=int and type(objeto)!=float and type(objeto)!=bool and type(objeto)!=None:
					
					o=objeto
				
				else:
					
					o=objeto

			return o

from LayoutHorizontal import LayoutHorizontal
from SidebarCustomize import SidebarCustomize
from SidebarAddItems import SidebarAddItems
from SidebarAddWidgets import SidebarAddWidgets
from Iframe import Iframe
from Media import Media

l=LayoutHorizontal()
i=Iframe()
i.css({"width":"100%",
	   "height":"calc( 100vh - 5px )",
	   "background-color":"gray"},
	   None,
	   ">iframe")


media=Media()


sidebar=SidebarCustomize()
sidebar.Media=media
sidebar2=SidebarAddItems()
sidebar3=SidebarAddWidgets()


l.add(sidebar)
l.add(sidebar2)
l.add(sidebar3)
l.add(i)

media.run(s("footer"))
"""
sidebar.run(s("#menu"))
sidebar2.run(s("#submenu"))
"""
l.run(s("section"))
l.reloadSizes()


