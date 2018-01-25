#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html><head> <title>Formulario</title> <link rel="stylesheet" href="'''+str(data['base_url'])+'''static/css/_bootstrap.css"> <link rel="stylesheet" href="'''+str(data['base_url'])+'''static/css/ff.css"> <script type="text/javascript" src="'''+str(data['base_url'])+'''static/js/brython/brython.js"></script> <script type="text/javascript" src="'''+str(data['base_url'])+'''static/js/brython/brython_stdlib.js"></script> <meta name="viewport" content="width=device-width, initial-scale=1"> <link rel="icon" type="image/png" href="'''+str(data['base_url'])+'''../admin/static/archivos/Imagenes/logo_min.png" /></head><body><section class="bg-gray"><form method="post" action="'''+str(config.base_url+config.controller_folder)+'''post.py" enctype='multipart/form-data'>  '''
for k,box in enumerate(data["boxes"]):
  print '''  <div class="b-s1 pad-1 b-r5">  <div>      '''
  if box!=None:
    print '''  '''
    for k2,elem in enumerate(box):
      print '''      '''
      if type(elem)==dict:
        print '''    '''
        tmp=list(elem)
        print '''    '''
        tmp.remove("name") if "name" in tmp else tmp
        print '''    '''
        tmp.remove("value") if "value" in tmp else tmp
        print '''    '''
        tmp.remove("step") if "step" in tmp else tmp
        print '''    '''
        tmp.remove("opcion") if "opcion" in tmp else tmp
        print '''    '''
        tmp.remove("requerido") if "requerido" in tmp else tmp
        print '''    '''
        tmp.remove("tabla") if "tabla" in tmp else tmp
        print '''    '''
        tmp.remove("depende") if "depende" in tmp else tmp
        print '''    '''
        tmp.remove("categoria") if "categoria" in tmp else tmp
        print '''    '''
        tmp.remove("descripcion") if "descripcion" in tmp else tmp
        print '''    '''
        tmp.remove("padre") if "padre" in tmp else tmp
        print '''    '''
        tmp.remove("placeholder") if "placeholder" in tmp else tmp
        print '''    '''
        tmp.remove("opciones") if "opciones" in tmp else tmp
        print '''    '''
        tmp=tmp[0]
        print '''                    '''
        if elem[tmp]=="fixed":
          print '''          <div class=" pad-05  marg-05">     <label>'''          +str(decode(tmp))          +'''</label>      <select name="'''          +str(elem['name'])          +'''" value="0">      <option>'''          +str(decode(elem['value']))          +'''</option>     </select>          </div>     '''
        elif elem[tmp]=="img-admin":
          print '''        <div class="text-center width-100p">     <img src="'''          +str(data['base_url'])          +'''../admin/static/archivos/Imagenes/'''          +str(data['opciones']['archivos'][0][1][data['page'][0][2]['value']])          +'''" class="height-10-xs" style="max-width:100%">    </div>                '''
        elif elem[tmp]=="text":
          print '''          <div class=" pad-05  b-s1 marg-05">            <label>'''          +str(tmp)          +'''<span></span></label>      <input type="'''          +str(elem[tmp])          +'''" name="'''          +str(elem['name'])          +'''" value="'''          +str(elem['value'])          +'''" '''          +str("required" if "requerido" in elem and elem['requerido']==True else '')          +''' '''          +str("placeholder='"+elem["placeholder"]+"'" if "placeholder" in elem else "")          +'''>       '''
          if "descripcion" in elem:
            print '''       <p>'''            +str(decode(elem["descripcion"]))            +'''</p>       '''
            pass
          print '''     </div>    '''
        elif elem[tmp]=="text-titulo":
          print '''          <div class=" pad-05  b-s1 marg-05">            <label>'''          +str(tmp)          +'''<span>['''          +str(k2)          +''']</span></label>      <input type="'''          +str(elem[tmp])          +'''" name="'''          +str(elem['name'])          +'''" value="'''          +str(elem['value'])          +'''" '''          +str("required" if "requerido" in elem and elem['requerido']==True else '')          +'''>      <script type="text/javascript">      $("#titulo'''          +str(k)          +'''").html("'''          +str(elem['value'])          +'''");      $("input[name='''          +str(elem['name'])          +''']").on("text",function(){       $("#titulo'''          +str(k)          +'''").html($("input[name='''          +str(elem['name'])          +''']").;      })                   </script>     </div>    '''
        elif elem[tmp]=="text-phone":
          print '''              <div class="pad-05 marg-05">                <label>'''          +str(tmp)          +'''<span></span></label>        <br>        <input type="phone" name="'''          +str(elem['name'])          +'''" value="'''          +str(elem['value'])          +'''" '''          +str("required" if "requerido" in elem and elem['requerido']==True else '')          +'''  class="width-100p height-3">         </div>    '''
        elif elem[tmp]=="text-email":
          print '''              <div class=" pad-05 marg-05">                <label>'''          +str(tmp)          +'''<span></span></label>        <br>        <input type="email" name="'''          +str(elem['name'])          +'''" value="'''          +str(elem['value'])          +'''" '''          +str("required" if "requerido" in elem and elem['requerido']==True else '')          +'''  class="width-100p height-3">       </div>    '''
        elif elem[tmp]=="text-admin":
          print '''          '''
          if data["login"]==True:
            print '''            <div class=" pad-05  marg-05">            <label>'''            +str(decode(tmp))            +'''<span>['''            +str(k2)            +''']</span></label>      <input type="text" name="'''            +str(elem['name'])            +'''" value="'''            +str(decode(elem['value']))            +'''">      </div>      '''
            pass
          print '''         '''
        elif elem[tmp]=="textarea":
          print '''     <div class="marg-05">     <label>'''          +str(decode(tmp))          +'''<span>['''          +str(k2)          +''']</span></label>     <textarea class="width-100p editor" name="'''          +str(elem['name'])          +'''">'''          +str(decode(elem['value']))          +'''</textarea>     </div>    '''
        elif elem[tmp]=="textarea-admin" and data["login"]==True:
          print '''     <div class="marg-05">     <label>'''          +str(decode(tmp))          +'''<span>['''          +str(k2)          +''']</span></label>     <textarea class="width-100p editor" name="'''          +str(elem['name'])          +'''">'''          +str(decode(elem['value']))          +'''</textarea>     </div>    '''
        elif elem[tmp]=="file":
          print '''     <div class=" pad-05  marg-05">     <label>'''          +str(tmp)          +'''<span>['''          +str(k2)          +''']</span></label>     <input type="'''          +str(elem[tmp])          +'''" name="'''          +str(elem['name'])          +'''" >     </div>    '''
        elif elem[tmp]=="select":
          print '''               <div class=" pad-05  marg-05">     <label>'''          +str(decode(tmp))          +'''<span>['''          +str(k2)          +''']</span></label>     <select name="'''          +str(elem['name'])          +'''"  '''          +str("depende='"+elem['depende']+"'" if "depende" in elem else "")          +'''  '''          +str('categoria=\"'+elem['categoria']+'\"' if 'categoria' in elem else '')          +''' '''          +str('tabla="'+elem['tabla']+'"' if 'tabla' in elem else '')          +''' class="width-19">            '''
          if "opcion" in elem and "tabla" not in elem:
            print '''                '''
            for _k, opcion in enumerate(data["opciones"][elem['opciones']][elem['opcion']][1]):
              print '''        <option '''              +str("selected" if elem['value']==_k else '')              +''' >'''              +str(decode(opcion))              +'''</option>        '''
              pass
            print '''      '''
          elif "opcion" in elem and "tabla" in elem and elem["tabla"]=="Imagenes":
            print '''              '''
            for _k, opcion in enumerate(data["imagenes"][elem["opcion"]][1]):
              print '''        <option '''              +str("selected" if elem['value']==_k else '')              +''' >'''              +str(decode(opcion))              +'''</option>        '''
              pass
            print '''             '''
          elif "tabla" in elem and "depende" not in elem:
            print '''                  '''
            for opcion in data["tablas"][elem['tabla']]:
              print '''         <option >'''              +str(decode(opcion))              +'''</option>         '''
              pass
            print '''      '''
          elif "tabla" in elem and "depende" in elem:
            print '''                  '''
            for opcion in list(data["categorias"][data["tablas"][elem['tabla']][0]]):
              print '''         <option >'''              +str(decode(opcion))              +'''</option>         '''
              pass
            print '''            '''
            pass
          print '''             </select>     </div>    '''
        elif elem[tmp]=="select-admin":
          print '''     '''
          if data["login"]==True:
            print '''      <div class=" pad-05  marg-05">      <label>'''            +str(decode(tmp))            +'''<span>['''            +str(k2)            +''']</span></label>      <select name="'''            +str(elem['name'])            +'''" >       '''
            for _k, opcion in enumerate(data["opciones"][elem['opciones']][elem['opcion']][1]):
              print '''        <option value="'''              +str(_k)              +'''" '''              +str("selected" if elem['value']==_k else '')              +''' >'''              +str(decode(opcion))              +'''</option>        '''
              pass
            print '''      </select>      </div>      '''
            pass
          print '''    '''
        elif elem[tmp]=="number":
          print '''     <div class=" pad-05  marg-05">     <label>'''          +str(tmp)          +'''<span>['''          +str(k2)          +''']</span></label>     <input type="'''          +str(elem[tmp])          +'''" name="'''          +str(elem['name'])          +'''" value="'''          +str(elem['value'])          +'''" '''          +str("step='"+elem['step']+"'" if "step" in elem else "")          +'''>     </div>         '''
        elif type(elem)==list:
          print '''     <div class="b-s1 pad-1 marg-1 b-r5 marg-05">     </div>      '''
          pass
        print '''       '''
      elif elem!=None:
        print '''    <div class="b-s1 b-r5 marg-05 pad-1">    <h2 id="titulo'''        +str(k2)        +'''"></h2>           '''
        for sub in elem:
          print '''              '''
          if type(sub)==str:
            print '''      <h3>'''            +str(sub)            +'''</h3>     '''
          elif type(sub)==dict:
            print '''            '''
            tmp=list(sub)
            print '''      '''
            tmp.remove("name") if "name" in tmp else tmp
            print '''      '''
            tmp.remove("value") if "value" in tmp else tmp
            print '''      '''
            tmp.remove("step") if "step" in tmp else tmp
            print '''      '''
            tmp.remove("opcion") if "opcion" in tmp else tmp
            print '''      '''
            tmp.remove("requerido") if "requerido" in tmp else tmp
            print '''      '''
            tmp.remove("tabla") if "tabla" in tmp else tmp
            print '''      '''
            tmp.remove("depende") if "depende" in tmp else tmp
            print '''      '''
            tmp.remove("categoria") if "categoria" in tmp else tmp
            print '''      '''
            tmp.remove("descripcion") if "descripcion" in tmp else tmp
            print '''      '''
            tmp.remove("padre") if "padre" in tmp else tmp
            print '''      '''
            tmp.remove("placeholder") if "placeholder" in tmp else tmp
            print '''      '''
            tmp.remove("opciones") if "opciones" in tmp else tmp
            print '''            '''
            tmp=tmp[0]
            print '''            '''
            if sub[tmp]=="text":
              print '''             <div class=" pad-05  marg-05">       <label>'''              +str(decode(tmp))              +'''</label>       <br>       <input type="'''              +str(sub[tmp])              +'''" name="'''              +str(sub['name'])              +'''" value="'''              +str(decode(sub['value']))              +'''" '''              +str("required" if "requerido" in sub and sub['requerido']==True else '')              +''' class="width-100p height-3" '''              +str("placeholder='"+sub["placeholder"]+"'" if "placeholder" in sub else "")              +'''>         '''
              if "descripcion" in sub:
                print '''       <p>'''                +str(decode(sub["descripcion"]))                +'''</p>       '''
                pass
              print '''       </div>      '''
            elif sub[tmp]=="img-admin":
              print '''       <div class="text-center width-100p">               <img src="'''              +str(data['base_url'])              +'''../admin/static/archivos/Imagenes/'''              +str(data['opciones']['archivos'][0][1][data['page'][0][2]['value']])              +'''" class="height-20 height-10-xs" style="max-width:100%">       </div>                   '''
            elif sub[tmp]=="text-email":
              print '''              <div class=" pad-05 marg-05">                <label>'''              +str(tmp)              +'''<span></span></label>        <br>        <input type="email" name="'''              +str(sub['name'])              +'''" value="'''              +str(sub['value'])              +'''" '''              +str("required" if "requerido" in sub and sub['requerido']==True else '')              +'''  class="width-100p height-3">       </div>      '''
            elif sub[tmp]=="text-phone":
              print '''              <div class="pad-05 marg-05">                <label>'''              +str(tmp)              +'''<span></span></label>        <br>        <input type="phone" name="'''              +str(sub['name'])              +'''" value="'''              +str(sub['value'])              +'''" '''              +str("required" if "requerido" in sub and sub['requerido']==True else '')              +'''  class="width-100p height-3">         </div>      '''
            elif sub[tmp]=="text-admin":
              print '''              <h1 class="text-center">'''              +str(sub["value"])              +'''</h1>       <div class="text-center">       <div class="d-inline-block text-justify">             '''
            elif sub[tmp]=="text-titulo":
              print '''              <div class=" pad-05  marg-05">       <label>'''              +str(decode(tmp))              +'''</label>              <input type="'''              +str(sub[tmp])              +'''" name="'''              +str(sub['name'])              +'''" value="'''              +str(decode(sub['value']))              +'''" '''              +str("required" if "requerido" in sub and sub['requerido']==True else '')              +'''>       </div>       <script>       $("#titulo'''              +str(k2)              +'''").html("'''              +str(sub['value'])              +'''");       $("input[name='''              +str(sub['name'])              +''']").on("keyup",function(){        $("#titulo'''              +str(k2)              +'''").html(this.value);       })       </script>      '''
            elif sub[tmp]=="textarea":
              print '''       <div class="marg-05">       <label>'''              +str(decode(tmp))              +'''</label>       <textarea class="width-100p editor" name="'''              +str(sub['name'])              +'''">'''              +str(decode(sub['value']))              +'''</textarea>       </div>      '''
            elif sub[tmp]=="textarea-admin" and data["login"]==True:
              print '''       <div class="marg-05">       <label>'''              +str(decode(tmp))              +'''</label>       <textarea class="width-100p editor" name="'''              +str(sub['name'])              +'''">'''              +str(decode(sub['value']))              +'''</textarea>       </div>      '''
            elif sub[tmp]=="select":
              print '''              <div class=" pad-05  marg-05">       <label>'''              +str(decode(tmp))              +'''</label>       <br>       <select name="'''              +str(sub['name'])              +'''"  value="'''              +str(sub['value'])              +'''" '''              +str("depende='"+opcion+"'" if "depende" in sub else "")              +''' '''              +str('tabla="'+sub['tabla']+'"' if 'tabla' in sub else '')              +''' '''              +str('categoria=\"'+sub['categoria']+'\"' if 'categoria' in sub else '')              +''' class="width-100p height-3">                '''
              if "opcion" in sub:
                print '''                  '''
                for _k, opcion in enumerate(data["opciones"][sub['opciones']][sub['opcion']][1]):
                  print '''          <option value="'''                  +str(_k)                  +'''" '''                  +str("selected" if sub['value']==_k else '')                  +''' >'''                  +str(decode(opcion))                  +'''</option>          '''
                  pass
                print '''        '''
              elif "tabla" in sub:
                print '''                  '''
                for _k,opcion in enumerate(data["tablas"][sub['tabla']]):
                  print '''         <option >'''                  +str(decode(opcion))                  +'''</option>         '''
                  pass
                print '''        '''
              elif "subtabla" in sub:
                print '''         <!--subtabla es el nombre de la tabla -->         '''
                for _fila in data["model"]["main"].obtenerFilas(sub['subtabla']):
                  print '''         <option >'''                  +str(decode(fila[0]))                  +'''</option>         '''
                  pass
                print '''        '''
                pass
              print '''       </select>       </div>      '''
            elif sub[tmp]=="select-admin":
              print '''       '''
              if data["login"]==True:
                print '''        <div class=" pad-05  marg-05">        <label>'''                +str(tmp)                +'''</label>        <select name="'''                +str(elem['name'])                +'''"  value="'''                +str(elem['value'])                +'''">         '''
                for opcion in data["opciones"][elem['opciones']][elem['opcion']][1]:
                  print '''         <option>'''                  +str(decode(opcion))                  +'''</option>         '''
                  pass
                print '''        </select>        </div>        '''
                pass
              print '''      '''
            elif sub[tmp]=="file":
              print '''       <div class=" pad-05  marg-05">       <label>'''              +str(tmp)              +'''</label>       <input type="'''              +str(sub[tmp])              +'''" name="'''              +str(sub['name'])              +'''" value="'''              +str(sub['value'])              +'''">       </div>      '''
            elif sub[tmp]=="number":
              print '''       <div class=" pad-05  marg-05">       <label>'''              +str(decode(tmp))              +'''</label>       <br>       <input type="'''              +str(sub[tmp])              +'''" name="'''              +str(sub['name'])              +'''" value="'''              +str(decode(sub['value']))              +'''" '''              +str("step='"+sub['step']+"'" if "step" in sub else "")              +''' class="width-100p height-3">       </div>                     '''
              pass
            print '''             '''
            pass
          print '''     '''
          pass
        print '''    </div>    '''
        if sub[tmp]=="text-admin":
          print '''        </div>        </div>        '''
          pass
        print '''    '''
        pass
      print '''       '''
      pass
    print '''  </div>  </div>   '''
    pass
  print ''' '''
  pass
print ''' <div class="text-center"><button type="submit" name="action" value="'''+str('Post-de-Formulario:0')+'''" class="btn bg-blue white pad-05 pad-l5 pad-r5 b-r5">SEND</button>   </div> '''
if "new" in data and data["new"]==True:
  print ''' <div class="pad-t1"> <a class="pad-05 b-r5 marg-t1 btn bg-bluelight font-ubuntu white" style="text-decoration: none" href="#add" id="add">  Añadir Campo </a>  </div>   '''
  pass
print '''<script type="text/javascript">        tinymce.init({   language : 'es',   selector: "textarea.editor",    theme: "modern",    plugins: [         "advlist autolink link image lists charmap print preview hr anchor pagebreak table",         "searchreplace wordcount visualblocks visualchars fullscreen insertdatetime media nonbreaking emoticons textcolor",         "save table contextmenu directionality emoticons template paste textcolor",         "code codesample"   ],   codesample_languages: [        {text: 'HTML/XML', value: 'markup'},        {text: 'JavaScript', value: 'javascript'},        {text: 'CSS', value: 'css'},        {text: 'PHP', value: 'php'},        {text: 'Ruby', value: 'ruby'},        {text: 'Python', value: 'python'},        {text: 'Java', value: 'java'},        {text: 'C', value: 'c'},        {text: 'C#', value: 'csharp'},        {text: 'C++', value: 'cpp'}    ],   content_css: "'''+str(config.base_url)+'''static/js/tinymce/js/tinymce/skins/lightgray/content.min.css",   toolbar: "insertfile undo redo preview | fontselect | fontsizeselect | forecolor backcolor emoticons | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | media fullpage code codesample",     fontsize_formats: "9pt 10pt 11pt 12pt 13pt 14pt 15pt 16pt 18pt 20pt 22pt 24pt",     font_formats: "Andale Mono=andale mono,times;"+        "Arial=arial,helvetica,sans-serif;"+        "Arial Black=arial black,avant garde;"+        "Book Antiqua=book antiqua,palatino;"+        "Comic Sans MS=comic sans ms,sans-serif;"+        "Courier New=courier new,courier;"+        "Georgia=georgia,palatino;"+        "Helvetica=helvetica;"+        "Impact=impact,chicago;"+        "Symbol=symbol;"+        "Tahoma=tahoma,arial,helvetica,sans-serif;"+        "Terminal=terminal,monaco;"+        "Times New Roman=times new roman,times;"+        "Trebuchet MS=trebuchet ms,geneva;"+        "Verdana=verdana,geneva;"+        "Webdings=webdings;"+        "Wingdings=wingdings,zapf dingbats", });   </script></form></section></body></html>'''