#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<html>  <head>    '''
incluir(data,"head")
print '''  </head>  <body>    <section class="container-fluid">      <div class="row">        <div class="col-md-4">        '''
incluir(data,"chatBox")
print '''                </div>        <div class="col-md-4">                 '''
incluir(data,"chatContactList")
print '''                </div>        <div class="col-md-4">        '''
incluir(data,"offlineBox")
print '''                </div>      </div>        </section>          </body></html>'''