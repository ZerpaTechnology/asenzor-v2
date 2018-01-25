#!usr/bin/env python
__pragma__("alias","s","$")


config=Config.Config()


def scroll(evt,clase=".text-parallax",grosor=45,posIni=70):
 activar=False
 
 
 #document.body.scrollTop
 for k,elem in enumerate(s(clase)):
  #grosor de las letras
  """
  if elem.parent.getBoundingClientRect().top+elem.parent.height/2-grosor<posIni and elem.parent.getBoundingClientRect().top+posIni>posIni:
  """
  #-webkit-transform: translate3d(0, -8px, 5px);
  elem.style.transform="translate3d(0px,"+str((elem.parentNode.getBoundingClientRect().top*1.5)-posIni)+"px,-100px)"
  elem.style.webkitTransform="translate3d(0px,"+str((elem.parentNode.getBoundingClientRect().top*1.5)-posIni)+"px,-100px)"
  elem.style.MozTransform="translate3d(0px,"+str((elem.parentNode.getBoundingClientRect().top*1.5)-posIni)+"px,-100px)"
  elem.style.OTransform="translate3d(0px,"+str((elem.parentNode.getBoundingClientRect().top*1.5)-posIni)+"px,-100px)"
  elem.style.msTransform="translate3d(0px,"+str((elem.parentNode.getBoundingClientRect().top*1.5)-posIni)+"px,-100px)"

  """
   #lo paso
   #if elem.parent.getBoundingClientRect().top>posIni:
   #elem.style.top=grosor*grosor/(window.screen.height-posIni)


   if "hidden"  in elem.class_name:
    elem.class_name=elem.class_name.replace(" hidden","")
  else:  
  """
  if s(elem.children[0]).hasClass("hidden"):
    s(elem.children[0]).removeClass("hidden")
    
  
def render(evt=None,clase=".text-parallax"):
 for k,elem in enumerate(s(clase)):

  elem.children[0].style.left=str(window.screen.width/2-elem.clientWidth/2)+"px"
  elem.style.width="100%"

 
render()
window.addEventListener("scroll",scroll,True)
window.addEventListener("orientationchange",render,True)
