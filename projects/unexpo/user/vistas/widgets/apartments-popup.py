#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''
<div id="'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''" class="bg-ubuntu_porcelain width-90p height-60  text-center hidden section-parallax" style="position: fixed; left: -45%; margin-left:50%; padding: 10px;top:50px;z-index:500;">

<div class="pad-1 text-center height-50 height-35-xs" style="overflow-y:scroll;">
 <h2>'''
try: doc+=str(data["widget"]["titulo"])
except Exception, e: doc+=str(e)
doc+='''</h2>
 <hr class="height-4">
  <div class="d-inline-block">
  

  <div class="width-40 width-30-xs">

<!--
  <div class="swiper-container">
        <div class="swiper-wrapper">
            <div class="swiper-slide"><img src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/'''
try: doc+=str(data['opciones']['archivos'][0][1][data['page'][2][5]['value']])
except Exception, e: doc+=str(e)
doc+='''" class="width-40 width-20-xs"></div>
            <div class="swiper-slide"><img src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/'''
try: doc+=str(data['opciones']['archivos'][0][1][data['page'][2][6]['value']])
except Exception, e: doc+=str(e)
doc+='''" class="width-40 width-20-xs"></div>
            
        </div>
        
        <div class="swiper-pagination"></div>
        
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
    </div>

  
-->
</div>
<div class="Slider" style="position: relative;">

<div class="content width-40  width-30-xs">
'''
for elem in data["widget"]["slider"]:
  doc+='''
<img src="'''
  try: doc+=str(data['base_url'])
  except Exception, e:   doc+=str(e)
  doc+='''../admin/static/archivos/Imagenes/'''
  try: doc+=str(elem)
  except Exception, e:   doc+=str(e)
  doc+='''">
'''
  pass
doc+='''
</div>
  <div class="f-left"><img src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f1.png"  class="height-5"></div>
  <div class="f-right"><img src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f2.png"  class="height-5"></div>
</div>

  </div>
    
      
  
 
  
  
 <div class="d-inline-block width-60 width-40-xs alg-top ">
    <div class="bg-white pad-1 ">
    <div class="text-left">

  '''
try: doc+=str(do_shortcode(data['widget']['content']))
except Exception, e: doc+=str(e)
doc+='''

  


    </div>
</div>
  </div>

</div>

<a id="'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''-cerrar" class="b-r20 bg-ubuntu_ash white pad-05 b-s1 b-white " style="position: absolute;right:-20px;top:-20px;cursor:pointer">Close</a>

</div>
'''