doc+='''<div class="box text-left">\n<div class="row">\n<div class="col-md-2 col-xs-12">\n\n\n\n<style type="text/css">\n  .CodeMirror {border-top: 1px solid #eee; border-bottom: 1px solid #eee; line-height: 1.3; height: 500px}\n  .CodeMirror-linenumbers { padding: 0 8px; }\n\n  .folderclass:before{\n   content: url("'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/iconos/007-folder.png");\n   cursor: pointer;\n  }\n  .fileclass:before{\n   content: url("'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/iconos/005-file.png");\n   cursor: pointer;\n  }\n  #alert-close{\n    position:absolute;\n    right:-15px;\n    top:-15px;\n    border:solid;\n    border-width:1px;\n    border-color:white;\n    border-radius:20px;\n    padding:5px;\n    background-color:gray;\n    color:white;\n  }\n</style>\n  <button id="titulo">\n    '''
try: doc+=str(data["titulo"] if "titulo" in data else "")
except Exception as e: doc+=str(e)
doc+=''' <button id="nuevo">Crear Nuevo</button>\n  </button>\n\n <div class="height-50 b-s1 width-100p font-s13 text-left" style="overflow-y: scroll;" id="treefiles">\n \n  \n  '''
try: doc+=str(data["renderTree"](data["trees"],folderclass="folderclass",fileclass="fileclass",excluir=data["excluir"]))
except Exception as e: doc+=str(e)
doc+='''\n  \n \n </div>\n\n</div>\n<div class="col-md-10 col-xs-12">\n <div class="height-48 b-s1 width-100p">\n<link rel=stylesheet href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/doc/docs.css">\n\n<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/lib/codemirror.css">\n<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/fold/foldgutter.css">\n<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/dialog/dialog.css">\n<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/theme/monokai.css">\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/lib/codemirror.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/display/autorefresh.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/search/searchcursor.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/search/search.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/dialog/dialog.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/edit/matchbrackets.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/edit/closebrackets.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/comment/comment.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/wrap/hardwrap.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/fold/foldcode.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/fold/brace-fold.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/javascript/javascript.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/python/python.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/keymap/sublime.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/selection/selection-pointer.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/xml/xml.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/javascript/javascript.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/css/css.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/vbscript/vbscript.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/htmlmixed/htmlmixed.js"></script>\n\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/emmet/dist/emmet.js"></script>\n\n\n\n<style type="text/css">\n .CodeMirror{\n  height: 100% !important;\n }\n .tab-btn{\n  background-color: rgb(150,100,150);\n  border: none;\n  color: white;\n }\n .tab{\n  height: 100%;\n }\n\n</style>\n\n<div id="tabs-btn">\n  <span style="padding:2px"><button class="tab-btn">Nuevo Archivo</button><button class="close-btn">x</button></span> \n</div>\n<div id="content2">\n<!-- tab1-->\n<div>\n  <div class="tab" >\n  <div class="path" style="overflow-x:scroll"></div>\n    <textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%">\n    </textarea>  \n</div>\n</div>\n\n<!-- tab2-->\n<div></div>\n<!-- tab3-->\n<div></div>\n<!-- tab4-->\n<div></div>\n<!-- tab5-->\n<div></div>\n<!-- tab6-->\n<div></div>\n<!-- tab7-->\n<div></div>\n<!-- tab8-->\n<div></div>\n<!-- tab9-->\n<div></div>\n<!-- tab10-->\n<div></div>\n<div id="btns-action">\n<button class="bg-blue white" id="guardar">Guardar</button>  \n</div>\n\n<div id="alert" class="hidden" style="position: fixed;z-index:100">\n</div>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/shortcut.js"></script>\n<script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/codeEditor.js">\n</script>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/menu2.js" ></script>\n\n\n<div class="height-10"></div> \n</div> \n</div>\n\n\n\n'''