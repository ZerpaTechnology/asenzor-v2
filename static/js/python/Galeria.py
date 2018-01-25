#!/usr/bin/python
# -*- coding: utf-8 -*-
__pragma__("alias","s","$")
decode=Codificador.Codificador.decode
config=Config.Config()

class Galeria:
  def __init__(self,selector,preview="#out",pos_default=0):
    self.posiciones=[pos_default for i in s(selector)]
    self.iterables=[]
    self.selector=selector
    self.current=0
    self.widget=preview
    self.preview=s(preview+" .preview")[0]

    for k,i in enumerate(self.posiciones):
      l=[]

      for tab in s(selector)[k].children:
          for span in tab.children:
              if window.innerHeight>585 and window.innerWidth>386:

                l.append(span.getAttribute("href"))
              else:
                l.append(span.children[0].src)
      self.iterables.append(l)

    
    

    


    def abspath(cadena):

     l=cadena.split("/")
     
     for i in range(cadena.count("../")):
      f=l.index("..")
      del l[f-1]
      del l[f-1]
     return "/".join(l)


    def img_link(evt):
     evt.preventDefault()
     """
     s(".f-left")[0].style.marginTop=str(window.innerHeight/2-s(".f-left")[0].clientHeight/2)+"px"
     s(".f-left")[0].style.top="0px"
     s(".f-right")[0].style.marginTop=str(window.innerHeight/2-s(".f-right")[0].clientHeight/2)+"px"
     s(".f-right")[0].style.top="0px"                    
     """
     s(preview).removeClass("hidden")
     for k,elem in enumerate(s(self.selector)):

      if elem==evt.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode:
        
        self.posiciones[k]=self.iterables[k].index(evt.target.parentNode.getAttribute("href"))
        
        s(self.preview).css("background-image","url('"+self.iterables[k][self.posiciones[k]]+"')")
        self.current=k

     
    
    s(self.selector).bind("click",img_link)

    def f_left(evt):

      self.posiciones[self.current]=self.posiciones[self.current]-1 if self.posiciones[self.current]>0 else len(self.iterables[self.current])-1
      s(self.preview).css("background-image","url('"+self.iterables[self.current][self.posiciones[self.current]]+"')")
      
    s(".f-left").bind("click",f_left)

    def f_right(evt):

      self.posiciones[self.current]=self.posiciones[self.current]+1 if self.posiciones[self.current]<len(self.iterables[self.current])-1 else 0
      alert(self.iterables[self.current][self.posiciones[self.current]])
      s(self.preview).css("background-image","url('"+self.iterables[self.current][self.posiciones[self.current]]+"')")
      
      

 
      


    s(".f-right").bind("click",f_right)

    def _exit(evt):
      s(evt.target.parentNode.parentNode).addClass("hidden")
      
    s(".exit").bind("click",_exit)
   

  def update(self): 

     #s(self.preview)[0].style.marginTop=str(window.innerHeight/2-s(self.preview)[0].parent.parent.clientHeight/2)+"px"
     self.preview=s(self.widget+" .preview")[0]
     


     #s(self.preview.parentNode).css({"padding-top":str(((self.preview.parentNode.height)/2)-(self.preview.height/2))+"px"})

  
class Slider:
  """docstring for Galeria_min"""
  def __init__(self,selector,pos_default=0):
    self.selector=selector
    
    self.iterables=s(self.selector)
    self.posiciones=[pos_default for i in self.iterables]


    
    
    for k2,selec in enumerate(s(self.selector)):
      content=s(selec).find(".content")[0]
      if len(content.children)>0:
        for k,elem in enumerate(content.children):
          s(elem).css({"max-width":"100%","max-height":"100%","text-align":"center"})
          s(content).css({"padding-top":(elem.height/2)-(elem.height/2)})
          if k!=pos_default:
            s(elem).addClass("hidden")






    
    
    def f_right(evt):
      for k,elem in enumerate(self.iterables):

        if elem.children[2]==evt.target.parentNode:
          content=elem.children[0]
          s(content.children[self.posiciones[k]]).addClass("hidden")
          self.posiciones[k]=self.posiciones[k]+1 if self.posiciones[k]<len(content.children)-1 else 0
          s(content.children[self.posiciones[k]]).removeClass("hidden")
          s(content).css({"padding-top":(s(content)[0].height/2)-(content.children[self.posiciones[k]].height/2)})
      
      
      
      
    def f_left(evt):

       for k,elem in enumerate(self.iterables):
        if elem.children[1]==evt.target.parentNode:
          content=elem.children[0]
          s(content.children[self.posiciones[k]]).addClass("hidden")
          self.posiciones[k]=self.posiciones[k]-1 if self.posiciones[k]>0 else len(content.children)-1
          s(content.children[self.posiciones[k]]).removeClass("hidden")
          s(content).css({"padding-top":(s(content)[0].height/2)-(content.children[self.posiciones[k]].height/2)})
      
           
    s(self.selector+" .f-left").bind("click",f_left)
    s(self.selector+" .f-right").bind("click",f_right)
    


