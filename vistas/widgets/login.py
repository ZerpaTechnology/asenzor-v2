doc+='''<div class="container-fluid sin-pad">\n\n<div class="row">\n <div class="col-md-12 col-sm-12" style="margin:20px auto;">\n <!--  HOME -->\n \n \n <div class="width-32 b-s1 bg-white text-center pad-1 width-30-xs" style="margin: 0 auto; border-color:gray;   box-shadow: 2px 2px 2px #888888;">\n  <div class="font-ubuntu">\n  <img src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/logos/logoZtec.png" class="height-10"><h3 class="bluelight">Bienvenido al Panel de control de '''
try: doc+=str(data["app"])
except Exception as e: doc+=str(e)
doc+='''</h3>\n\n  <form method="post" action="'''
try: doc+=str(config.base_url+settings.app)
except Exception as e: doc+=str(e)
doc+='''/admin/Entrar"  '''
try: doc+=str('' if data['login']==False else 'target="login"')
except Exception as e: doc+=str(e)
doc+='''>\n  <div class="text-left">\n   <p>Nombre de usuario o dirección de correo electrónico</p>\n  </div>\n  <div>\n   <input type="text" name="email" style="background:#fbfbfb;box-shadow: inset 0 1px 2px rgba(0,0,0,.07);color:black" class="height-3 marg-1 width-28 width-22-xs">\n  </div>\n  <div>\n  <div class="text-left">\n   <p>Contraseña</p>\n  </div>\n   \n   <input type="password" name="password" style="background:#fbfbfb;box-shadow: inset 0 1px 2px rgba(0,0,0,.07);color: black" class="height-3 marg-1 width-28 width-22-xs">\n  </div>\n   \n   <p>Por favor logueate para continuar</p>\n   <button type="submit" name="action" value="Login" class="btn bg-blue white pad-05 b-r5">Entrar</button>\n   \n  </form> \n  </div>\n  \n  \n </div>\n <div class="marg-b3 text-center pad-t1">\n <p class="hidden"><a href="">¿Has perdido tu contraseña?</a></p>\n <p class="hidden"><a href=""> <- Volver al mode user</a></p>\n  \n </div>\n \n\n </div>\n</div>\n<iframe name="login" src="" style="display: none">\n</iframe>\n\n</div>'''