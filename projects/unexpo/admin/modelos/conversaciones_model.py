#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from ztec.zmodel import Model
import sys
import os
import datetime
import ztec.zu as zu
sys.path.append("../")
import settings
try:
 import config.config as config
except:
 import config

try:
 class model(Model):
    """Modelo para manejar las conversaciones en el sistema de chat"""
    
    def iniciarConversacion(self,usuarioInicial,*usuarios,**kwargs):
      """Este metodo nos permite buscar si ya existe esta conversacion o crear una nueva"""
      if self.request():
        if "tema" in kwargs:
          pass
        else:
          hay=False
          conversaciones=self.obtenerFilas("Conversaciones")
          for k, elem in enumerate(conversaciones):
            if usuarioInicial+" - ".join(usuarios) == elem[0]:
              hay=True
              break

          if k==len(conversaciones)-1 and hay==True:

            self.db("Conversaciones").modificarCampo(k,"Contenido"
              [conversaciones[k][1]]+[[{"Conversación":"titulo","value":zu.DateTime()}]],
            )
            self.db("Conversaciones").modificarCampo(k,"Fecha",
              zu.DateTime())
          elif k==len(conversaciones)-1 and hay!=True:
            self.db("Conversaciones").insertar(usuarioInicial+" - ".join(usuarios),
              [
                [{"Conversación":"titulo","value":zu.DateTime()},
                ],
              ],
              {"Conversacion":k+1},
              zu.DateTime(),
              []
            )
          else:            

            self.db("Conversaciones").modificarCampo(k,"Contenido",
              [
                [conversaciones[k][1]]+[[{"Conversación":"titulo","value":zu.DateTime()}]],
              ],
              )
            self.db("Conversaciones").modificarCampo(k,"Fecha",
              zu.DateTime())
          self.grabar()
          return k+1

    def conversar(self,conversacion,usuario,mensaje,p):  
      if self.request():
        
        contenido=self.obtenerFilas("Conversaciones")[conversacion][1]
        current_user=p["main"]["model"].obtenerUsuario(token)
        if usuario==current_user["token"]:
          contenido[-1].append({current_user["email"]:"msj","value":mensaje})
        else:
          contenido[-1].append({usuario:"msj","value":mensaje})
        self.db("Conversaciones").modificarCampo(conversacion,"Contenido",contenido)
        self.grabar()
    def obtenerContacto(self,email):
      if self.update():
        d={}
        for contacto in  self.obtenerFilas("Contactos")[1]:
          if contacto[1]["value"]==email:
            for elem in contacto:
             d[elem["name"]]=elem["value"]
          
          
        return d
    def obtenerContactos(self):
      if self.update():
        l=[]
        for contacto in  self.obtenerFilas("Contactos")[1]:
          d={}
          for elem in contacto:
           d[elem["name"]]=elem["value"]
          l.append(d)
        return d
        
    def obtenerContenido(self,indice,tabla):
        t={}
        for elem in self.obtenerTabla(tabla)[indice][1]:
          t[elem["name"]]=elem["value"]
        return t


    
except Exception,e:
  pass
