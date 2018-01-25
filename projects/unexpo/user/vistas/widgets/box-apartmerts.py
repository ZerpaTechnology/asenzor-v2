#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''
<div class="col-md-'''
try: doc+=str(data['widget']['cols'])
except Exception, e: doc+=str(e)
doc+=''' '''
try: doc+=str('col-md-offset-'+str(data['widget']['md-offset']) if 'md-offset' in data['widget'] else '')
except Exception, e: doc+=str(e)
doc+=''' sin-pad">
       <div class=" text-center " >
       <div class="height-6 height-8-sm height-10-xs width-100p tex-center pad-t2 pad-2x-sm z-index10 font-roboto font-s20" style="background-color: rgba(200,0,0,0.8);border:solid;border-color: rgb(71,0,0);color:#d1dddd;" >
         '''
try: doc+=str(data["widget"]["titulo"])
except Exception, e: doc+=str(e)
doc+="""
         
         

        </div>
         <div style="position:relative;height:400px;">
        <a href="#floorapartments"  onclick="popup('"""
try: doc+=str(data['widget']['click'])
except Exception, e: doc+=str(e)
doc+='''')"  style=""> 
          <img id="'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''" src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/'''
try: doc+=str(data['widget']['img1'])
except Exception, e: doc+=str(e)
doc+='''" alt="floridian" style="min-width:100%;min-height:100%;max-height:100%;position: absolute;left: 0;" class="hidden-xs hidden-sm">
        <img id="'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''_1" src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/'''
try: doc+=str(data['widget']['img2'])
except Exception, e: doc+=str(e)
doc+='''" alt="floridian" style="min-width:100%;min-height:100%;max-height:100%;position: absolute;left: 0;" class=" hidden-md hidden-lg">
        </a>
         </div>
         <div class="height-6 height-8-sm height-10-xs width-100p tex-center pad-t2 pad-2x-sm white z-index10 font-roboto font-s20" style="background-color: rgba(200,0,0,0.8);border:solid;border-color: rgb(71,0,0);position:relative" >
         
        </div>
            <div id="hidden" class="height-1">
 
</div>

        
       <div id="'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+="""-info"  class="text-center hidden white width-100p fast-info" style="position: absolute;top:150px">
 <a href="#floorapartments" onclick="popup('"""
try: doc+=str(data['widget']['click'])
except Exception, e: doc+=str(e)
doc+="""')"   class="decoration-none white ">
  <div class="text width-75p" style="background-color:rgba(71,0,0,0.4);margin: 0 auto">
  """
try: doc+=str(do_shortcode(data["widget"]["flash-info"]))
except Exception, e: doc+=str(e)
doc+='''
  
  </div>
 </a>
 </div>
       </div>
       </div>
       <script type="text/javascript">
         
 $("#'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''").mouseover(function(){
 $("'''
try: doc+=str('#'+',#'.join(data['widget']['ids']) )
except Exception, e: doc+=str(e)
doc+='''").addClass("hidden");
   $("#'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''-info").removeClass("hidden");
   
   $("#'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''-info").addClass("animated zoomIn");
   $(".text").addClass("animated zoomInUp");


  
   

  });
 
 $("#'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''1_1").mouseover(function(){
  $("'''
try: doc+=str('#'+',#'.join(data['widget']['ids']) )
except Exception, e: doc+=str(e)
doc+='''").addClass("hidden");
   $("#'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''-info").removeClass("hidden");
   
   $("#'''
try: doc+=str(data['widget']['id'])
except Exception, e: doc+=str(e)
doc+='''-info").addClass("animated zoomIn");
   
   $(".text").addClass("animated zoomInUp");


  
   

  });
       </script>'''