#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div id="alert" class="pad-1 hidden">
<style type="text/css">
	#alert{
		width: 80%;
		height:500px;
		position: fixed;
		top:20px;
		left:10%;
		z-index: 100;
		background-color:white;

	}
  #alert-close{
  position: absolute;
  right: -10px;
  top:-10px;
  background-color: gray;
  color:white;
  border: solid;
  border-width: 1px;
  border-radius: 15px;
  padding: 5px;
  cursor: pointer;

  }
</style>
<span id="alert-close">x</span>
  '''
if "widget" in data:
  doc+='''
    '''
  incluir(data,data["widget"])
  doc+='''
  '''
elif "content" in data:
  doc+='''
    '''
  if type(data["content"])==list:
    doc+='''
      '''
    for elem in data["content"]:
      doc+='''
         <div>'''
      try: doc+=str(elem)
      except Exception, e:       doc+=str(e)
      doc+='''<div>
      '''
      pass
    doc+='''
      '''
    pass
  doc+='''
  '''
  pass
doc+='''
  '''
if type(data["content"])==str:
  doc+='''
     '''
  try: doc+=str(data["content"])
  except Exception, e:   doc+=str(e)
  doc+='''
  '''
  pass
doc+='''
    
  
  <script type="text/javascript">
  	$("#alert-close").bind("click",function(){
  		$("#alert").addClass("hidden")
  	});
  </script>
</div>'''