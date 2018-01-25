doc+='''<div id="out" class="width-100p hidden section-parallax" style="position: fixed;background-color:rgba(255,255,255,0.5); z-index: 400;top:0;height: 800px">\n<div class="width-90p text-center preview" style="position: relative; margin-right: auto;margin-left: auto;height:100vh;background-color: rgba(0,0,0,0.5);background-size: 60% auto;background-repeat:no-repeat; background-position: center; ">\n<span class="f-left"><img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f1.png"  class="height-5"></span>\n<span class="f-right"><img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''../admin/static/archivos/Imagenes/f2.png" class="height-5"> </span>\n<span class="exit"> x </span>\n</div>\n</div>\n'''