#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<div class="pad-2  bg-ubuntu_yellow">	<div class="bg-white pad-1 text-center height-30 height-40-xs font-s18" style="overflow-y: scroll;">		<div><h3><u>Publicaciones recientes:</u></h3></div>				'''
for publicacion in data["publicaciones"][0][1]:
  print '''				<div>			<h4 class="blue">'''  +str(publicacion[0]["value"])  +'''</h4>									<div class="d-inline-block width-70p">								'''  +str(data["parrafer"](publicacion[2]["value"],"text-left"))  +'''							</div>				</div>			</div>		'''
  pass
print '''	</div>'''