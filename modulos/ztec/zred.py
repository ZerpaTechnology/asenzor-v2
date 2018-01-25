#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
import SocketServer
import threading
import time
import copy

#creo mi TCP Handler
class MiTcpHandler(SocketServer.BaseRequestHandler):
    
    #sobrescribo la funcion handle
    def handle(self):
        
        while self.data[0] != ".salir":
            #intento recibir informacion
            try:
                self.data.append(self.request.recv(1024))
                self.request.send("listo")
                del self.data[0]
                time.sleep(0.1) #espero 0.1 segundos antes de leer neuvamente
            #si hubo un error lo digo y termino el handle
            except:
                print "El cliente D/C o hubo un error"
                self.data[0]=".salir"

class MiTcpHandler2(SocketServer.BaseRequestHandler):#para uso en bases de datos
    
    #sobrescribo la funcion handle
    def handle(self):
        
        while self.data[0] != self.salir:
            
            #intento recibir informacion
            try:
                self.data[0]=self.request.recv(1024)                
                self.request.send(self.data[1])
                

                
            #si hubo un error lo digo y termino el handle
            except Exception, e:
                print "El cliente D/C o hubo un error"
                print e
                


#no se assusten Creo una clase llamada ThreadServer
class ThreadServer (SocketServer.ThreadingMixIn, SocketServer.ForkingTCPServer):
    pass

def serverSock(host,port,welcome="Server corriendo..",data=["",""]):
    #host & port
    #creo el server
    MiTcpHandler.data=data

    server = ThreadServer((host,port),MiTcpHandler)

    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()
    
    print welcome


def serverSock2(host,port,welcome="Server corriendo..",data=[" "," "],salir=".salir"):
    #host & port
    #creo el server
    MiTcpHandler2.data=data
    MiTcpHandler2.salir=salir
    
    server = ThreadServer((host,port),MiTcpHandler2)
    

    #creo un thread del server
    server_thread = threading.Thread(target=server.serve_forever)
    #empiezo el thread
    server_thread.start()

    
    print welcome
    return server
    

def setCookie(cookie):
    print "<script type='text/javascript'>"
    print "document.cookie+=`"+cookie+"`;"
    print "</script>"

   
def clienteSock(host,port,msj="",welcome="Ingrese un mensaje o salir para terminar"):
		import socket
		#creo un socket y me conecto
		sock= socket.socket()
		sock.connect((host,port))
		enviar=True
		print welcome
		while enviar==True:
		    #intento mandar msj
		    try:  
			     sock.send(msj)
			     time.sleep(0.1)
			     print sock.recv(1024)
			     break
			     enviar=False
		    # si no se puede entonces salgo
		    except Exception, e: 
		            print "no se mando el mensaje"
		            print e
		            enviar=False

		sock.close() #recuerden cerrar el socket
def clienteSock2(host,port,funcion,data=[" "," "],welcome="Ingrese un mensaje o salir para terminar",salir=".salir"):
        #usar espacio " " para enviar data asi se sabe que hay conexion
        import socket
        #creo un socket y me conecto
        sock= socket.socket()
        sock.connect((host,port))
        enviar=True
        print welcome
        sock.send("None")



        while data[0]!=salir:
            try:  
                data[0]=sock.recv(1024)               
                sock.send(data[1])
                funcion(data)
                
                
                
                
            # si no se puede entonces salgo
            except Exception, e: 
                    print "no se mando el mensaje"
                    print e
                    data[0]=salir

        sock.close() #recuerden cerrar el socket


	
#Esta funcion solo es posible ejecutarla en una maquina y no desde el serividor con cgi(XAMPP)
#La solicion seria ejecutarla atravez de un socketServer, ya que con python directo funciona
def sendEmail(rem,dest,password,mensaje,asunto="", remAlias="",destAlias="",debug=False,host="localhost",port=25,server=None,user=None):
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
     
    # Enviar correo Gmail con Python
    # www.pythondiario.com
    try:
        import smtplib

        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # me == my email address
        # you == recipient's email address

        # Create message container - the correct MIME type is multipart/alternative.
    
        msg = MIMEMultipart() 
        msg['To'] = dest
        msg['From'] = rem
        msg['Subject'] = asunto
        #cuerpo del mensaje en HTML y si fuera solo text puede colocar en el 2da parametro 'plain'
        msg.attach(MIMEText(mensaje,'html'))

     
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
      
        # Send the message via local SMTP server.
        if server=="gmail":
            mail = smtplib.SMTP('smtp.gmail.com', 587)
        elif server==None:
            mail = smtplib.SMTP(host, port)

        mail.ehlo()

        mail.starttls()

        if user!=None:
            mail.login(user,password)
        else:
            mail.login(rem,password)

        mail.sendmail(rem, dest,msg.as_string())
        mail.quit()
        print "enviado"

    except Exception as e:
        print "<?php mail('"+dest+"','"+asunto+"','"+"','"+mensaje+"','"+rem+")?>"
        if debug==True:
            print e," esto puede ser culpa del servidor"
            print "Se intento hacer el envio por PHP"
def decode(cadena):
    if type(cadena)==str or type(cadena)==unicode:
        cadena=cadena.replace("\xc2\xa1","¡")
        cadena=cadena.replace("\xc2\xa2","¢")
        cadena=cadena.replace("\xc2\xa3","£")
        cadena=cadena.replace("\xc2\xa4","¤")
        cadena=cadena.replace("\xc2\xa5","¥")
        cadena=cadena.replace("\xc2\xa6","¦")
        cadena=cadena.replace("\xc2\xa7","§")
        cadena=cadena.replace("\xc2\xa8","¨")
        cadena=cadena.replace("\xc2\xa9","©")
        cadena=cadena.replace("\xc2\xaa","ª")
        cadena=cadena.replace("\xc2\xab","«")
        cadena=cadena.replace("\xc2\xac","¬")
        cadena=cadena.replace("\xc2\xae","®")
        cadena=cadena.replace("\xc2\xaf","¯")
        cadena=cadena.replace("\xc2\xb0","°")
        cadena=cadena.replace("\xc2\xb1","±")
        cadena=cadena.replace("\xc2\xb2","²")
        cadena=cadena.replace("\xc2\xb3","³")
        cadena=cadena.replace("\xc2\xb4","´")
        cadena=cadena.replace("\xc2\xb5","µ")
        cadena=cadena.replace("\xc2\xb6","¶")
        cadena=cadena.replace("\xc2\xb7","·")
        cadena=cadena.replace("\xc2\xb8","¸")
        cadena=cadena.replace("\xc2\xb9","¹")
        cadena=cadena.replace("\xc2\xba","º")
        cadena=cadena.replace("\xc2\xbb","»")
        cadena=cadena.replace("\xc2\xbc","¼")
        cadena=cadena.replace("\xc2\xbd","½")
        cadena=cadena.replace("\xc2\xbe","¾")
        cadena=cadena.replace("\xc2\xbf","¿")
        cadena=cadena.replace("\xc3\x80","À")
        cadena=cadena.replace("\xc3\x81","Á")
        cadena=cadena.replace("\xc3\x82","Â")
        cadena=cadena.replace("\xc3\x83","Ã")
        cadena=cadena.replace("\xc3\x84","Ä")
        cadena=cadena.replace("\xc3\x85","Å")
        cadena=cadena.replace("\xc3\x86","Æ")
        cadena=cadena.replace("\xc3\x87","Ç")
        cadena=cadena.replace("\xc3\x88","È")
        cadena=cadena.replace("\xc3\x89","É")
        cadena=cadena.replace("\xc3\x8a","Ê")
        cadena=cadena.replace("\xc3\x8b","Ë")
        cadena=cadena.replace("\xc3\x8c","Ì")
        cadena=cadena.replace("\xc3\x8d","Í")
        cadena=cadena.replace("\xc3\x8e","Î")
        cadena=cadena.replace("\xc3\x8f","Ï")
        cadena=cadena.replace("\xc3\x90","Ð")
        cadena=cadena.replace("\xc3\x91","Ñ")
        cadena=cadena.replace("\xc3\x92","Ò")
        cadena=cadena.replace("\xc3\x93","Ó")
        cadena=cadena.replace("\xc3\x94","Ô")
        cadena=cadena.replace("\xc3\x95","Õ")
        cadena=cadena.replace("\xc3\x96","Ö")
        cadena=cadena.replace("\xc3\x97","×")
        cadena=cadena.replace("\xc3\x98","Ø")
        cadena=cadena.replace("\xc3\x99","Ù")
        cadena=cadena.replace("\xc3\x9a","Ú")
        cadena=cadena.replace("\xc3\x9b","Û")
        cadena=cadena.replace("\xc3\x9c","Ü")
        cadena=cadena.replace("\xc3\x9d","Ý")
        cadena=cadena.replace("\xc3\x9e","Þ")
        cadena=cadena.replace("\xc3\x9f","ß")
        cadena=cadena.replace("\xc3\xa0","à")
        cadena=cadena.replace("\xc3\xa1","á")
        cadena=cadena.replace("\xc3\xa2","â")
        cadena=cadena.replace("\xc3\xa3","ã")
        cadena=cadena.replace("\xc3\xa4","ä")
        cadena=cadena.replace("\xc3\xa5","å")
        cadena=cadena.replace("\xc3\xa6","æ")
        cadena=cadena.replace("\xc3\xa7","ç")
        cadena=cadena.replace("\xc3\xa8","è")
        cadena=cadena.replace("\xc3\xa9","é")
        cadena=cadena.replace("\xc3\xaa","ê")
        cadena=cadena.replace("\xc3\xab","ë")
        cadena=cadena.replace("\xc3\xac","ì")
        cadena=cadena.replace("\xc3\xad","í")
        cadena=cadena.replace("\xc3\xae","î")
        cadena=cadena.replace("\xc3\xaf","ï")
        cadena=cadena.replace("\xc3\xb0","ð")
        cadena=cadena.replace("\xc3\xb1","ñ")
        cadena=cadena.replace("\xc3\xb2","ò")
        cadena=cadena.replace("\xc3\xb3","ó")
        cadena=cadena.replace("\xc3\xb4","ô")
        cadena=cadena.replace("\xc3\xb5","õ")
        cadena=cadena.replace("\xc3\xb6","ö")
        cadena=cadena.replace("\xc3\xb7","÷")
        cadena=cadena.replace("\xc3\xb8","ø")
        cadena=cadena.replace("\xc3\xb9","ù")
        cadena=cadena.replace("\xc3\xba","ú")
        cadena=cadena.replace("\xc3\xbb","û")
        cadena=cadena.replace("\xc3\xbc","ü")
        cadena=cadena.replace("\xc3\xbd","ý")
        cadena=cadena.replace("\xc3\xbe","þ")
        cadena=cadena.replace("\xc3\xbf","ÿ")
        cadena=cadena.replace("\xe2\x80\x91","‑") 
        cadena=cadena.replace("\xe2\x80\x92","‒") 
        cadena=cadena.replace("\xe2\x80\x93","–") 
        cadena=cadena.replace("\xe2\x80\x94","—") 
        cadena=cadena.replace("\xe2\x80\x95","―") 
        cadena=cadena.replace("\xe2\x80\x96","‖") 
        cadena=cadena.replace("\xe2\x80\x97","‗") 
        cadena=cadena.replace("\xe2\x80\x98","‘") 
        cadena=cadena.replace("\xe2\x80\x99","’") 
        cadena=cadena.replace("\xe2\x80\x9a","‚") 
        cadena=cadena.replace("\xe2\x80\x9b","‛") 
        cadena=cadena.replace("\xe2\x80\x9c","“") 
        cadena=cadena.replace("\xe2\x80\x9d","”") 
        cadena=cadena.replace("\xe2\x80\x9e","„") 
        cadena=cadena.replace("\xe2\x80\x9f","‟") 
        cadena=cadena.replace("\xe2\x80\xa0","†") 
        cadena=cadena.replace("\xe2\x80\xa1","‡") 
        cadena=cadena.replace("\xe2\x80\xa2","•") 
        cadena=cadena.replace("\xe2\x80\xa3","‣") 
        cadena=cadena.replace("\xe2\x80\xa4","․") 
        cadena=cadena.replace("\xe2\x80\xa5","‥") 
        cadena=cadena.replace("\xe2\x80\xa6","…") 
        cadena=cadena.replace("\xe2\x80\xa7","‧") 
        cadena=cadena.replace("\xe2\x80\xb0","‰") 
        cadena=cadena.replace("\xe2\x80\xb1","‱") 
        cadena=cadena.replace("\xe2\x80\xb2","′") 
        cadena=cadena.replace("\xe2\x80\xb3","″") 
        cadena=cadena.replace("\xe2\x80\xb4","‴") 
        cadena=cadena.replace("\xe2\x80\xb5","‵") 
        cadena=cadena.replace("\xe2\x80\xb6","‶") 
        cadena=cadena.replace("\xe2\x80\xb7","‷") 
        cadena=cadena.replace("\xe2\x80\xb8","‸") 
        cadena=cadena.replace("\xe2\x80\xb9","‹") 
        cadena=cadena.replace("\xe2\x80\xba","›") 
        cadena=cadena.replace("\xe2\x80\xbb","※") 
        cadena=cadena.replace("\xe2\x80\xbc","‼") 
        cadena=cadena.replace("\xe2\x80\xbd","‽") 
        cadena=cadena.replace("\xe2\x80\xbe","‾") 
        cadena=cadena.replace("\xe2\x80\xbf","‿") 
        cadena=cadena.replace("\xe2\x81\x80","⁀") 
        cadena=cadena.replace("\xe2\x81\x81","⁁") 
        cadena=cadena.replace("\xe2\x81\x82","⁂") 
        cadena=cadena.replace("\xe2\x81\x83","⁃") 
        cadena=cadena.replace("\xe2\x81\x84","⁄") 
        cadena=cadena.replace("\xe2\x81\x85","⁅") 
        cadena=cadena.replace("\xe2\x81\x86","⁆") 
        cadena=cadena.replace("\xe2\x81\x87","⁇") 
        cadena=cadena.replace("\xe2\x81\x88","⁈") 
        cadena=cadena.replace("\xe2\x81\x89","⁉") 
        cadena=cadena.replace("\xe2\x81\x8a","⁊") 
        cadena=cadena.replace("\xe2\x81\x8b","⁋") 
        cadena=cadena.replace("\xe2\x81\x8c","⁌") 
        cadena=cadena.replace("\xe2\x81\x8d","⁍") 
        cadena=cadena.replace("\xe2\x81\x8e","⁎") 
        cadena=cadena.replace("\xe2\x81\x8f","⁏") 
        cadena=cadena.replace("\xe2\x81\x90","⁐") 
        cadena=cadena.replace("\xe2\x81\x91","⁑") 
        cadena=cadena.replace("\xe2\x81\x92","⁒") 
        cadena=cadena.replace("\xe2\x81\x93","⁓") 
        cadena=cadena.replace("\xe2\x81\x94","⁔") 
        cadena=cadena.replace("\xe2\x81\x95","⁕") 
        cadena=cadena.replace("\xe2\x81\x96","⁖") 
        cadena=cadena.replace("\xe2\x81\x97","⁗") 
        cadena=cadena.replace("\xe2\x81\x98","⁘") 
        cadena=cadena.replace("\xe2\x81\x99","⁙") 
        cadena=cadena.replace("\xe2\x81\x9a","⁚") 
        cadena=cadena.replace("\xe2\x81\x9b","⁛") 
        cadena=cadena.replace("\xe2\x81\x9c","⁜") 
        cadena=cadena.replace("\xe2\x81\x9d","⁝") 
        cadena=cadena.replace("\xe2\x81\x9e","⁞") 
        cadena=cadena.replace("\xe2\x81\xb0","⁰") 
        cadena=cadena.replace("\xe2\x81\xb1","ⁱ") 
        cadena=cadena.replace("\xe2\x81\xb4","⁴") 
        cadena=cadena.replace("\xe2\x81\xb5","⁵") 
        cadena=cadena.replace("\xe2\x81\xb6","⁶") 
        cadena=cadena.replace("\xe2\x81\xb7","⁷") 
        cadena=cadena.replace("\xe2\x81\xb8","⁸") 
        cadena=cadena.replace("\xe2\x81\xb9","⁹") 
        cadena=cadena.replace("\xe2\x81\xba","⁺") 
        cadena=cadena.replace("\xe2\x81\xbb","⁻") 
        cadena=cadena.replace("\xe2\x81\xbc","⁼") 
        cadena=cadena.replace("\xe2\x81\xbd","⁽") 
        cadena=cadena.replace("\xe2\x81\xbe","⁾") 
        cadena=cadena.replace("\xe2\x81\xbf","ⁿ") 
        cadena=cadena.replace("\xe2\x81\xbf","ⁿ") 
        #----------------------------------------
        #doble slashes
        cadena=cadena.replace("\\xc2\\xa1","¡")
        cadena=cadena.replace("\\xc2\\xa2","¢")
        cadena=cadena.replace("\\xc2\\xa3","£")
        cadena=cadena.replace("\\xc2\\xa4","¤")
        cadena=cadena.replace("\\xc2\\xa5","¥")
        cadena=cadena.replace("\\xc2\\xa6","¦")
        cadena=cadena.replace("\\xc2\\xa7","§")
        cadena=cadena.replace("\\xc2\\xa8","¨")
        cadena=cadena.replace("\\xc2\\xa9","©")
        cadena=cadena.replace("\\xc2\\xaa","ª")
        cadena=cadena.replace("\\xc2\\xab","«")
        cadena=cadena.replace("\\xc2\\xac","¬")
        cadena=cadena.replace("\\xc2\\xae","®")
        cadena=cadena.replace("\\xc2\\xaf","¯")
        cadena=cadena.replace("\\xc2\\xb0","°")
        cadena=cadena.replace("\\xc2\\xb1","±")
        cadena=cadena.replace("\\xc2\\xb2","²")
        cadena=cadena.replace("\\xc2\\xb3","³")
        cadena=cadena.replace("\\xc2\\xb4","´")
        cadena=cadena.replace("\\xc2\\xb5","µ")
        cadena=cadena.replace("\\xc2\\xb6","¶")
        cadena=cadena.replace("\\xc2\\xb7","·")
        cadena=cadena.replace("\\xc2\\xb8","¸")
        cadena=cadena.replace("\\xc2\\xb9","¹")
        cadena=cadena.replace("\\xc2\\xba","º")
        cadena=cadena.replace("\\xc2\\xbb","»")
        cadena=cadena.replace("\\xc2\\xbc","¼")
        cadena=cadena.replace("\\xc2\\xbd","½")
        cadena=cadena.replace("\\xc2\\xbe","¾")
        cadena=cadena.replace("\\xc2\\xbf","¿")
        cadena=cadena.replace("\\xc3\\x80","À")
        cadena=cadena.replace("\\xc3\\x81","Á")
        cadena=cadena.replace("\\xc3\\x82","Â")
        cadena=cadena.replace("\\xc3\\x83","Ã")
        cadena=cadena.replace("\\xc3\\x84","Ä")
        cadena=cadena.replace("\\xc3\\x85","Å")
        cadena=cadena.replace("\\xc3\\x86","Æ")
        cadena=cadena.replace("\\xc3\\x87","Ç")
        cadena=cadena.replace("\\xc3\\x88","È")
        cadena=cadena.replace("\\xc3\\x89","É")
        cadena=cadena.replace("\\xc3\\x8a","Ê")
        cadena=cadena.replace("\\xc3\\x8b","Ë")
        cadena=cadena.replace("\\xc3\\x8c","Ì")
        cadena=cadena.replace("\\xc3\\x8d","Í")
        cadena=cadena.replace("\\xc3\\x8e","Î")
        cadena=cadena.replace("\\xc3\\x8f","Ï")
        cadena=cadena.replace("\\xc3\\x90","Ð")
        cadena=cadena.replace("\\xc3\\x91","Ñ")
        cadena=cadena.replace("\\xc3\\x92","Ò")
        cadena=cadena.replace("\\xc3\\x93","Ó")
        cadena=cadena.replace("\\xc3\\x94","Ô")
        cadena=cadena.replace("\\xc3\\x95","Õ")
        cadena=cadena.replace("\\xc3\\x96","Ö")
        cadena=cadena.replace("\\xc3\\x97","×")
        cadena=cadena.replace("\\xc3\\x98","Ø")
        cadena=cadena.replace("\\xc3\\x99","Ù")
        cadena=cadena.replace("\\xc3\\x9a","Ú")
        cadena=cadena.replace("\\xc3\\x9b","Û")
        cadena=cadena.replace("\\xc3\\x9c","Ü")
        cadena=cadena.replace("\\xc3\\x9d","Ý")
        cadena=cadena.replace("\\xc3\\x9e","Þ")
        cadena=cadena.replace("\\xc3\\x9f","ß")
        cadena=cadena.replace("\\xc3\\xa0","à")
        cadena=cadena.replace("\\xc3\\xa1","á")
        cadena=cadena.replace("\\xc3\\xa2","â")
        cadena=cadena.replace("\\xc3\\xa3","ã")
        cadena=cadena.replace("\\xc3\\xa4","ä")
        cadena=cadena.replace("\\xc3\\xa5","å")
        cadena=cadena.replace("\\xc3\\xa6","æ")
        cadena=cadena.replace("\\xc3\\xa7","ç")
        cadena=cadena.replace("\\xc3\\xa8","è")
        cadena=cadena.replace("\\xc3\\xa9","é")
        cadena=cadena.replace("\\xc3\\xaa","ê")
        cadena=cadena.replace("\\xc3\\xab","ë")
        cadena=cadena.replace("\\xc3\\xac","ì")
        cadena=cadena.replace("\\xc3\\xad","í")
        cadena=cadena.replace("\\xc3\\xae","î")
        cadena=cadena.replace("\\xc3\\xaf","ï")
        cadena=cadena.replace("\\xc3\\xb0","ð")
        cadena=cadena.replace("\\xc3\\xb1","ñ")
        cadena=cadena.replace("\\xc3\\xb2","ò")
        cadena=cadena.replace("\\xc3\\xb3","ó")
        cadena=cadena.replace("\\xc3\\xb4","ô")
        cadena=cadena.replace("\\xc3\\xb5","õ")
        cadena=cadena.replace("\\xc3\\xb6","ö")
        cadena=cadena.replace("\\xc3\\xb7","÷")
        cadena=cadena.replace("\\xc3\\xb8","ø")
        cadena=cadena.replace("\\xc3\\xb9","ù")
        cadena=cadena.replace("\\xc3\\xba","ú")
        cadena=cadena.replace("\\xc3\\xbb","û")
        cadena=cadena.replace("\\xc3\\xbc","ü")
        cadena=cadena.replace("\\xc3\\xbd","ý")
        cadena=cadena.replace("\\xc3\\xbe","þ")
        cadena=cadena.replace("\\xc3\\xbf","ÿ")
        cadena=cadena.replace("\\xe2\\x80\\x91","‑") 
        cadena=cadena.replace("\\xe2\\x80\\x92","‒") 
        cadena=cadena.replace("\\xe2\\x80\\x93","–") 
        cadena=cadena.replace("\\xe2\\x80\\x94","—") 
        cadena=cadena.replace("\\xe2\\x80\\x95","―") 
        cadena=cadena.replace("\\xe2\\x80\\x96","‖") 
        cadena=cadena.replace("\\xe2\\x80\\x97","‗") 
        cadena=cadena.replace("\\xe2\\x80\\x98","‘") 
        cadena=cadena.replace("\\xe2\\x80\\x99","’") 
        cadena=cadena.replace("\\xe2\\x80\\x9a","‚") 
        cadena=cadena.replace("\\xe2\\x80\\x9b","‛") 
        cadena=cadena.replace("\\xe2\\x80\\x9c","“") 
        cadena=cadena.replace("\\xe2\\x80\\x9d","”") 
        cadena=cadena.replace("\\xe2\\x80\\x9e","„") 
        cadena=cadena.replace("\\xe2\\x80\\x9f","‟") 
        cadena=cadena.replace("\\xe2\\x80\\xa0","†") 
        cadena=cadena.replace("\\xe2\\x80\\xa1","‡") 
        cadena=cadena.replace("\\xe2\\x80\\xa2","•") 
        cadena=cadena.replace("\\xe2\\x80\\xa3","‣") 
        cadena=cadena.replace("\\xe2\\x80\\xa4","․") 
        cadena=cadena.replace("\\xe2\\x80\\xa5","‥") 
        cadena=cadena.replace("\\xe2\\x80\\xa6","…") 
        cadena=cadena.replace("\\xe2\\x80\\xa7","‧") 
        cadena=cadena.replace("\\xe2\\x80\\xb0","‰") 
        cadena=cadena.replace("\\xe2\\x80\\xb1","‱") 
        cadena=cadena.replace("\\xe2\\x80\\xb2","′") 
        cadena=cadena.replace("\\xe2\\x80\\xb3","″") 
        cadena=cadena.replace("\\xe2\\x80\\xb4","‴") 
        cadena=cadena.replace("\\xe2\\x80\\xb5","‵") 
        cadena=cadena.replace("\\xe2\\x80\\xb6","‶") 
        cadena=cadena.replace("\\xe2\\x80\\xb7","‷") 
        cadena=cadena.replace("\\xe2\\x80\\xb8","‸") 
        cadena=cadena.replace("\\xe2\\x80\\xb9","‹") 
        cadena=cadena.replace("\\xe2\\x80\\xba","›") 
        cadena=cadena.replace("\\xe2\\x80\\xbb","※") 
        cadena=cadena.replace("\\xe2\\x80\\xbc","‼") 
        cadena=cadena.replace("\\xe2\\x80\\xbd","‽") 
        cadena=cadena.replace("\\xe2\\x80\\xbe","‾") 
        cadena=cadena.replace("\\xe2\\x80\\xbf","‿") 
        cadena=cadena.replace("\\xe2\\x81\\x80","⁀") 
        cadena=cadena.replace("\\xe2\\x81\\x81","⁁") 
        cadena=cadena.replace("\\xe2\\x81\\x82","⁂") 
        cadena=cadena.replace("\\xe2\\x81\\x83","⁃") 
        cadena=cadena.replace("\\xe2\\x81\\x84","⁄") 
        cadena=cadena.replace("\\xe2\\x81\\x85","⁅") 
        cadena=cadena.replace("\\xe2\\x81\\x86","⁆") 
        cadena=cadena.replace("\\xe2\\x81\\x87","⁇") 
        cadena=cadena.replace("\\xe2\\x81\\x88","⁈") 
        cadena=cadena.replace("\\xe2\\x81\\x89","⁉") 
        cadena=cadena.replace("\\xe2\\x81\\x8a","⁊") 
        cadena=cadena.replace("\\xe2\\x81\\x8b","⁋") 
        cadena=cadena.replace("\\xe2\\x81\\x8c","⁌") 
        cadena=cadena.replace("\\xe2\\x81\\x8d","⁍") 
        cadena=cadena.replace("\\xe2\\x81\\x8e","⁎") 
        cadena=cadena.replace("\\xe2\\x81\\x8f","⁏") 
        cadena=cadena.replace("\\xe2\\x81\\x90","⁐") 
        cadena=cadena.replace("\\xe2\\x81\\x91","⁑") 
        cadena=cadena.replace("\\xe2\\x81\\x92","⁒") 
        cadena=cadena.replace("\\xe2\\x81\\x93","⁓") 
        cadena=cadena.replace("\\xe2\\x81\\x94","⁔") 
        cadena=cadena.replace("\\xe2\\x81\\x95","⁕") 
        cadena=cadena.replace("\\xe2\\x81\\x96","⁖") 
        cadena=cadena.replace("\\xe2\\x81\\x97","⁗") 
        cadena=cadena.replace("\\xe2\\x81\\x98","⁘") 
        cadena=cadena.replace("\\xe2\\x81\\x99","⁙") 
        cadena=cadena.replace("\\xe2\\x81\\x9a","⁚") 
        cadena=cadena.replace("\\xe2\\x81\\x9b","⁛") 
        cadena=cadena.replace("\\xe2\\x81\\x9c","⁜") 
        cadena=cadena.replace("\\xe2\\x81\\x9d","⁝") 
        cadena=cadena.replace("\\xe2\\x81\\x9e","⁞") 
        cadena=cadena.replace("\\xe2\\x81\\xb0","⁰") 
        cadena=cadena.replace("\\xe2\\x81\\xb1","ⁱ") 
        cadena=cadena.replace("\\xe2\\x81\\xb4","⁴") 
        cadena=cadena.replace("\\xe2\\x81\\xb5","⁵") 
        cadena=cadena.replace("\\xe2\\x81\\xb6","⁶") 
        cadena=cadena.replace("\\xe2\\x81\\xb7","⁷") 
        cadena=cadena.replace("\\xe2\\x81\\xb8","⁸") 
        cadena=cadena.replace("\\xe2\\x81\\xb9","⁹") 
        cadena=cadena.replace("\\xe2\\x81\\xba","⁺") 
        cadena=cadena.replace("\\xe2\\x81\\xbb","⁻") 
        cadena=cadena.replace("\\xe2\\x81\\xbc","⁼") 
        cadena=cadena.replace("\\xe2\\x81\\xbd","⁽") 
        cadena=cadena.replace("\\xe2\\x81\\xbe","⁾") 
        cadena=cadena.replace("\\xe2\\x81\\xbf","ⁿ") 
        cadena=cadena.replace("\\xe2\\x81\\xbf","ⁿ") 
        #----------------------------------------
        #slash alreves
        cadena=cadena.replace("/xc2/xa1","¡")
        cadena=cadena.replace("/xc2/xa2","¢")
        cadena=cadena.replace("/xc2/xa3","£")
        cadena=cadena.replace("/xc2/xa4","¤")
        cadena=cadena.replace("/xc2/xa5","¥")
        cadena=cadena.replace("/xc2/xa6","¦")
        cadena=cadena.replace("/xc2/xa7","§")
        cadena=cadena.replace("/xc2/xa8","¨")
        cadena=cadena.replace("/xc2/xa9","©")
        cadena=cadena.replace("/xc2/xaa","ª")
        cadena=cadena.replace("/xc2/xab","«")
        cadena=cadena.replace("/xc2/xac","¬")
        cadena=cadena.replace("/xc2/xae","®")
        cadena=cadena.replace("/xc2/xaf","¯")
        cadena=cadena.replace("/xc2/xb0","°")
        cadena=cadena.replace("/xc2/xb1","±")
        cadena=cadena.replace("/xc2/xb2","²")
        cadena=cadena.replace("/xc2/xb3","³")
        cadena=cadena.replace("/xc2/xb4","´")
        cadena=cadena.replace("/xc2/xb5","µ")
        cadena=cadena.replace("/xc2/xb6","¶")
        cadena=cadena.replace("/xc2/xb7","·")
        cadena=cadena.replace("/xc2/xb8","¸")
        cadena=cadena.replace("/xc2/xb9","¹")
        cadena=cadena.replace("/xc2/xba","º")
        cadena=cadena.replace("/xc2/xbb","»")
        cadena=cadena.replace("/xc2/xbc","¼")
        cadena=cadena.replace("/xc2/xbd","½")
        cadena=cadena.replace("/xc2/xbe","¾")
        cadena=cadena.replace("/xc2/xbf","¿")
        cadena=cadena.replace("/xc3/x80","À")
        cadena=cadena.replace("/xc3/x81","Á")
        cadena=cadena.replace("/xc3/x82","Â")
        cadena=cadena.replace("/xc3/x83","Ã")
        cadena=cadena.replace("/xc3/x84","Ä")
        cadena=cadena.replace("/xc3/x85","Å")
        cadena=cadena.replace("/xc3/x86","Æ")
        cadena=cadena.replace("/xc3/x87","Ç")
        cadena=cadena.replace("/xc3/x88","È")
        cadena=cadena.replace("/xc3/x89","É")
        cadena=cadena.replace("/xc3/x8a","Ê")
        cadena=cadena.replace("/xc3/x8b","Ë")
        cadena=cadena.replace("/xc3/x8c","Ì")
        cadena=cadena.replace("/xc3/x8d","Í")
        cadena=cadena.replace("/xc3/x8e","Î")
        cadena=cadena.replace("/xc3/x8f","Ï")
        cadena=cadena.replace("/xc3/x90","Ð")
        cadena=cadena.replace("/xc3/x91","Ñ")
        cadena=cadena.replace("/xc3/x92","Ò")
        cadena=cadena.replace("/xc3/x93","Ó")
        cadena=cadena.replace("/xc3/x94","Ô")
        cadena=cadena.replace("/xc3/x95","Õ")
        cadena=cadena.replace("/xc3/x96","Ö")
        cadena=cadena.replace("/xc3/x97","×")
        cadena=cadena.replace("/xc3/x98","Ø")
        cadena=cadena.replace("/xc3/x99","Ù")
        cadena=cadena.replace("/xc3/x9a","Ú")
        cadena=cadena.replace("/xc3/x9b","Û")
        cadena=cadena.replace("/xc3/x9c","Ü")
        cadena=cadena.replace("/xc3/x9d","Ý")
        cadena=cadena.replace("/xc3/x9e","Þ")
        cadena=cadena.replace("/xc3/x9f","ß")
        cadena=cadena.replace("/xc3/xa0","à")
        cadena=cadena.replace("/xc3/xa1","á")
        cadena=cadena.replace("/xc3/xa2","â")
        cadena=cadena.replace("/xc3/xa3","ã")
        cadena=cadena.replace("/xc3/xa4","ä")
        cadena=cadena.replace("/xc3/xa5","å")
        cadena=cadena.replace("/xc3/xa6","æ")
        cadena=cadena.replace("/xc3/xa7","ç")
        cadena=cadena.replace("/xc3/xa8","è")
        cadena=cadena.replace("/xc3/xa9","é")
        cadena=cadena.replace("/xc3/xaa","ê")
        cadena=cadena.replace("/xc3/xab","ë")
        cadena=cadena.replace("/xc3/xac","ì")
        cadena=cadena.replace("/xc3/xad","í")
        cadena=cadena.replace("/xc3/xae","î")
        cadena=cadena.replace("/xc3/xaf","ï")
        cadena=cadena.replace("/xc3/xb0","ð")
        cadena=cadena.replace("/xc3/xb1","ñ")
        cadena=cadena.replace("/xc3/xb2","ò")
        cadena=cadena.replace("/xc3/xb3","ó")
        cadena=cadena.replace("/xc3/xb4","ô")
        cadena=cadena.replace("/xc3/xb5","õ")
        cadena=cadena.replace("/xc3/xb6","ö")
        cadena=cadena.replace("/xc3/xb7","÷")
        cadena=cadena.replace("/xc3/xb8","ø")
        cadena=cadena.replace("/xc3/xb9","ù")
        cadena=cadena.replace("/xc3/xba","ú")
        cadena=cadena.replace("/xc3/xbb","û")
        cadena=cadena.replace("/xc3/xbc","ü")
        cadena=cadena.replace("/xc3/xbd","ý")
        cadena=cadena.replace("/xc3/xbe","þ")
        cadena=cadena.replace("/xc3/xbf","ÿ")
        cadena=cadena.replace("/xe2/x80/x91","‑") 
        cadena=cadena.replace("/xe2/x80/x92","‒") 
        cadena=cadena.replace("/xe2/x80/x93","–") 
        cadena=cadena.replace("/xe2/x80/x94","—") 
        cadena=cadena.replace("/xe2/x80/x95","―") 
        cadena=cadena.replace("/xe2/x80/x96","‖") 
        cadena=cadena.replace("/xe2/x80/x97","‗") 
        cadena=cadena.replace("/xe2/x80/x98","‘") 
        cadena=cadena.replace("/xe2/x80/x99","’") 
        cadena=cadena.replace("/xe2/x80/x9a","‚") 
        cadena=cadena.replace("/xe2/x80/x9b","‛") 
        cadena=cadena.replace("/xe2/x80/x9c","“") 
        cadena=cadena.replace("/xe2/x80/x9d","”") 
        cadena=cadena.replace("/xe2/x80/x9e","„") 
        cadena=cadena.replace("/xe2/x80/x9f","‟") 
        cadena=cadena.replace("/xe2/x80/xa0","†") 
        cadena=cadena.replace("/xe2/x80/xa1","‡") 
        cadena=cadena.replace("/xe2/x80/xa2","•") 
        cadena=cadena.replace("/xe2/x80/xa3","‣") 
        cadena=cadena.replace("/xe2/x80/xa4","․") 
        cadena=cadena.replace("/xe2/x80/xa5","‥") 
        cadena=cadena.replace("/xe2/x80/xa6","…") 
        cadena=cadena.replace("/xe2/x80/xa7","‧") 
        cadena=cadena.replace("/xe2/x80/xb0","‰") 
        cadena=cadena.replace("/xe2/x80/xb1","‱") 
        cadena=cadena.replace("/xe2/x80/xb2","′") 
        cadena=cadena.replace("/xe2/x80/xb3","″") 
        cadena=cadena.replace("/xe2/x80/xb4","‴") 
        cadena=cadena.replace("/xe2/x80/xb5","‵") 
        cadena=cadena.replace("/xe2/x80/xb6","‶") 
        cadena=cadena.replace("/xe2/x80/xb7","‷") 
        cadena=cadena.replace("/xe2/x80/xb8","‸") 
        cadena=cadena.replace("/xe2/x80/xb9","‹") 
        cadena=cadena.replace("/xe2/x80/xba","›") 
        cadena=cadena.replace("/xe2/x80/xbb","※") 
        cadena=cadena.replace("/xe2/x80/xbc","‼") 
        cadena=cadena.replace("/xe2/x80/xbd","‽") 
        cadena=cadena.replace("/xe2/x80/xbe","‾") 
        cadena=cadena.replace("/xe2/x80/xbf","‿") 
        cadena=cadena.replace("/xe2/x81/x80","⁀") 
        cadena=cadena.replace("/xe2/x81/x81","⁁") 
        cadena=cadena.replace("/xe2/x81/x82","⁂") 
        cadena=cadena.replace("/xe2/x81/x83","⁃") 
        cadena=cadena.replace("/xe2/x81/x84","⁄") 
        cadena=cadena.replace("/xe2/x81/x85","⁅") 
        cadena=cadena.replace("/xe2/x81/x86","⁆") 
        cadena=cadena.replace("/xe2/x81/x87","⁇") 
        cadena=cadena.replace("/xe2/x81/x88","⁈") 
        cadena=cadena.replace("/xe2/x81/x89","⁉") 
        cadena=cadena.replace("/xe2/x81/x8a","⁊") 
        cadena=cadena.replace("/xe2/x81/x8b","⁋") 
        cadena=cadena.replace("/xe2/x81/x8c","⁌") 
        cadena=cadena.replace("/xe2/x81/x8d","⁍") 
        cadena=cadena.replace("/xe2/x81/x8e","⁎") 
        cadena=cadena.replace("/xe2/x81/x8f","⁏") 
        cadena=cadena.replace("/xe2/x81/x90","⁐") 
        cadena=cadena.replace("/xe2/x81/x91","⁑") 
        cadena=cadena.replace("/xe2/x81/x92","⁒") 
        cadena=cadena.replace("/xe2/x81/x93","⁓") 
        cadena=cadena.replace("/xe2/x81/x94","⁔") 
        cadena=cadena.replace("/xe2/x81/x95","⁕") 
        cadena=cadena.replace("/xe2/x81/x96","⁖") 
        cadena=cadena.replace("/xe2/x81/x97","⁗") 
        cadena=cadena.replace("/xe2/x81/x98","⁘") 
        cadena=cadena.replace("/xe2/x81/x99","⁙") 
        cadena=cadena.replace("/xe2/x81/x9a","⁚") 
        cadena=cadena.replace("/xe2/x81/x9b","⁛") 
        cadena=cadena.replace("/xe2/x81/x9c","⁜") 
        cadena=cadena.replace("/xe2/x81/x9d","⁝") 
        cadena=cadena.replace("/xe2/x81/x9e","⁞") 
        cadena=cadena.replace("/xe2/x81/xb0","⁰") 
        cadena=cadena.replace("/xe2/x81/xb1","ⁱ") 
        cadena=cadena.replace("/xe2/x81/xb4","⁴") 
        cadena=cadena.replace("/xe2/x81/xb5","⁵") 
        cadena=cadena.replace("/xe2/x81/xb6","⁶") 
        cadena=cadena.replace("/xe2/x81/xb7","⁷") 
        cadena=cadena.replace("/xe2/x81/xb8","⁸") 
        cadena=cadena.replace("/xe2/x81/xb9","⁹") 
        cadena=cadena.replace("/xe2/x81/xba","⁺") 
        cadena=cadena.replace("/xe2/x81/xbb","⁻") 
        cadena=cadena.replace("/xe2/x81/xbc","⁼") 
        cadena=cadena.replace("/xe2/x81/xbd","⁽") 
        cadena=cadena.replace("/xe2/x81/xbe","⁾") 
        cadena=cadena.replace("/xe2/x81/xbf","ⁿ") 
        #url
        #---------------------------------------
        cadena=cadena.replace("/xc2/xa1","¡")
        cadena=cadena.replace("/xc2/xa2","¢")
        cadena=cadena.replace("/xc2/xa3","£")
        cadena=cadena.replace("/xc2/xa4","¤")
        cadena=cadena.replace("/xc2/xa5","¥")
        cadena=cadena.replace("/xc2/xa6","¦")
        cadena=cadena.replace("/xc2/xa7","§")
        cadena=cadena.replace("/xc2/xa8","¨")
        cadena=cadena.replace("/xc2/xa9","©")
        cadena=cadena.replace("/xc2/xaa","ª")
        cadena=cadena.replace("/xc2/xab","«")
        cadena=cadena.replace("/xc2/xac","¬")
        cadena=cadena.replace("/xc2/xae","®")
        cadena=cadena.replace("/xc2/xaf","¯")
        cadena=cadena.replace("/xc2/xb0","°")
        cadena=cadena.replace("/xc2/xb1","±")
        cadena=cadena.replace("/xc2/xb2","²")
        cadena=cadena.replace("/xc2/xb3","³")
        cadena=cadena.replace("/xc2/xb4","´")
        cadena=cadena.replace("/xc2/xb5","µ")
        cadena=cadena.replace("/xc2/xb6","¶")
        cadena=cadena.replace("/xc2/xb7","·")
        cadena=cadena.replace("/xc2/xb8","¸")
        cadena=cadena.replace("/xc2/xb9","¹")
        cadena=cadena.replace("/xc2/xba","º")
        cadena=cadena.replace("/xc2/xbb","»")
        cadena=cadena.replace("/xc2/xbc","¼")
        cadena=cadena.replace("/xc2/xbd","½")
        cadena=cadena.replace("/xc2/xbe","¾")
        cadena=cadena.replace("/xc2/xbf","¿")
        cadena=cadena.replace("/xc3/x80","À")
        cadena=cadena.replace("/xc3/x81","Á")
        cadena=cadena.replace("/xc3/x82","Â")
        cadena=cadena.replace("/xc3/x83","Ã")
        cadena=cadena.replace("/xc3/x84","Ä")
        cadena=cadena.replace("/xc3/x85","Å")
        cadena=cadena.replace("/xc3/x86","Æ")
        cadena=cadena.replace("/xc3/x87","Ç")
        cadena=cadena.replace("/xc3/x88","È")
        cadena=cadena.replace("/xc3/x89","É")
        cadena=cadena.replace("/xc3/x8a","Ê")
        cadena=cadena.replace("/xc3/x8b","Ë")
        cadena=cadena.replace("/xc3/x8c","Ì")
        cadena=cadena.replace("/xc3/x8d","Í")
        cadena=cadena.replace("/xc3/x8e","Î")
        cadena=cadena.replace("/xc3/x8f","Ï")
        cadena=cadena.replace("/xc3/x90","Ð")
        cadena=cadena.replace("/xc3/x91","Ñ")
        cadena=cadena.replace("/xc3/x92","Ò")
        cadena=cadena.replace("/xc3/x93","Ó")
        cadena=cadena.replace("/xc3/x94","Ô")
        cadena=cadena.replace("/xc3/x95","Õ")
        cadena=cadena.replace("/xc3/x96","Ö")
        cadena=cadena.replace("/xc3/x97","×")
        cadena=cadena.replace("/xc3/x98","Ø")
        cadena=cadena.replace("/xc3/x99","Ù")
        cadena=cadena.replace("/xc3/x9a","Ú")
        cadena=cadena.replace("/xc3/x9b","Û")
        cadena=cadena.replace("/xc3/x9c","Ü")
        cadena=cadena.replace("/xc3/x9d","Ý")
        cadena=cadena.replace("/xc3/x9e","Þ")
        cadena=cadena.replace("/xc3/x9f","ß")
        cadena=cadena.replace("/xc3/xa0","à")
        cadena=cadena.replace("/xc3/xa1","á")
        cadena=cadena.replace("/xc3/xa2","â")
        cadena=cadena.replace("/xc3/xa3","ã")
        cadena=cadena.replace("/xc3/xa4","ä")
        cadena=cadena.replace("/xc3/xa5","å")
        cadena=cadena.replace("/xc3/xa6","æ")
        cadena=cadena.replace("/xc3/xa7","ç")
        cadena=cadena.replace("/xc3/xa8","è")
        cadena=cadena.replace("/xc3/xa9","é")
        cadena=cadena.replace("/xc3/xaa","ê")
        cadena=cadena.replace("/xc3/xab","ë")
        cadena=cadena.replace("/xc3/xac","ì")
        cadena=cadena.replace("/xc3/xad","í")
        cadena=cadena.replace("/xc3/xae","î")
        cadena=cadena.replace("/xc3/xaf","ï")
        cadena=cadena.replace("/xc3/xb0","ð")
        cadena=cadena.replace("/xc3/xb1","ñ")
        cadena=cadena.replace("/xc3/xb2","ò")
        cadena=cadena.replace("/xc3/xb3","ó")
        cadena=cadena.replace("/xc3/xb4","ô")
        cadena=cadena.replace("/xc3/xb5","õ")
        cadena=cadena.replace("/xc3/xb6","ö")
        cadena=cadena.replace("/xc3/xb7","÷")
        cadena=cadena.replace("/xc3/xb8","ø")
        cadena=cadena.replace("/xc3/xb9","ù")
        cadena=cadena.replace("/xc3/xba","ú")
        cadena=cadena.replace("/xc3/xbb","û")
        cadena=cadena.replace("/xc3/xbc","ü")
        cadena=cadena.replace("/xc3/xbd","ý")
        cadena=cadena.replace("/xc3/xbe","þ")
        cadena=cadena.replace("/xc3/xbf","ÿ")
        cadena=cadena.replace("/xe2/x80/x91","‑") 
        cadena=cadena.replace("/xe2/x80/x92","‒") 
        cadena=cadena.replace("/xe2/x80/x93","–") 
        cadena=cadena.replace("/xe2/x80/x94","—") 
        cadena=cadena.replace("/xe2/x80/x95","―") 
        cadena=cadena.replace("/xe2/x80/x96","‖") 
        cadena=cadena.replace("/xe2/x80/x97","‗") 
        cadena=cadena.replace("/xe2/x80/x98","‘") 
        cadena=cadena.replace("/xe2/x80/x99","’") 
        cadena=cadena.replace("/xe2/x80/x9a","‚") 
        cadena=cadena.replace("/xe2/x80/x9b","‛") 
        cadena=cadena.replace("/xe2/x80/x9c","“") 
        cadena=cadena.replace("/xe2/x80/x9d","”") 
        cadena=cadena.replace("/xe2/x80/x9e","„") 
        cadena=cadena.replace("/xe2/x80/x9f","‟") 
        cadena=cadena.replace("/xe2/x80/xa0","†") 
        cadena=cadena.replace("/xe2/x80/xa1","‡") 
        cadena=cadena.replace("/xe2/x80/xa2","•") 
        cadena=cadena.replace("/xe2/x80/xa3","‣") 
        cadena=cadena.replace("/xe2/x80/xa4","․") 
        cadena=cadena.replace("/xe2/x80/xa5","‥") 
        cadena=cadena.replace("/xe2/x80/xa6","…") 
        cadena=cadena.replace("/xe2/x80/xa7","‧") 
        cadena=cadena.replace("/xe2/x80/xb0","‰") 
        cadena=cadena.replace("/xe2/x80/xb1","‱") 
        cadena=cadena.replace("/xe2/x80/xb2","′") 
        cadena=cadena.replace("/xe2/x80/xb3","″") 
        cadena=cadena.replace("/xe2/x80/xb4","‴") 
        cadena=cadena.replace("/xe2/x80/xb5","‵") 
        cadena=cadena.replace("/xe2/x80/xb6","‶") 
        cadena=cadena.replace("/xe2/x80/xb7","‷") 
        cadena=cadena.replace("/xe2/x80/xb8","‸") 
        cadena=cadena.replace("/xe2/x80/xb9","‹") 
        cadena=cadena.replace("/xe2/x80/xba","›") 
        cadena=cadena.replace("/xe2/x80/xbb","※") 
        cadena=cadena.replace("/xe2/x80/xbc","‼") 
        cadena=cadena.replace("/xe2/x80/xbd","‽") 
        cadena=cadena.replace("/xe2/x80/xbe","‾") 
        cadena=cadena.replace("/xe2/x80/xbf","‿") 
        cadena=cadena.replace("/xe2/x81/x80","⁀") 
        cadena=cadena.replace("/xe2/x81/x81","⁁") 
        cadena=cadena.replace("/xe2/x81/x82","⁂") 
        cadena=cadena.replace("/xe2/x81/x83","⁃") 
        cadena=cadena.replace("/xe2/x81/x84","⁄") 
        cadena=cadena.replace("/xe2/x81/x85","⁅") 
        cadena=cadena.replace("/xe2/x81/x86","⁆") 
        cadena=cadena.replace("/xe2/x81/x87","⁇") 
        cadena=cadena.replace("/xe2/x81/x88","⁈") 
        cadena=cadena.replace("/xe2/x81/x89","⁉") 
        cadena=cadena.replace("/xe2/x81/x8a","⁊") 
        cadena=cadena.replace("/xe2/x81/x8b","⁋") 
        cadena=cadena.replace("/xe2/x81/x8c","⁌") 
        cadena=cadena.replace("/xe2/x81/x8d","⁍") 
        cadena=cadena.replace("/xe2/x81/x8e","⁎") 
        cadena=cadena.replace("/xe2/x81/x8f","⁏") 
        cadena=cadena.replace("/xe2/x81/x90","⁐") 
        cadena=cadena.replace("/xe2/x81/x91","⁑") 
        cadena=cadena.replace("/xe2/x81/x92","⁒") 
        cadena=cadena.replace("/xe2/x81/x93","⁓") 
        cadena=cadena.replace("/xe2/x81/x94","⁔") 
        cadena=cadena.replace("/xe2/x81/x95","⁕") 
        cadena=cadena.replace("/xe2/x81/x96","⁖") 
        cadena=cadena.replace("/xe2/x81/x97","⁗") 
        cadena=cadena.replace("/xe2/x81/x98","⁘") 
        cadena=cadena.replace("/xe2/x81/x99","⁙") 
        cadena=cadena.replace("/xe2/x81/x9a","⁚") 
        cadena=cadena.replace("/xe2/x81/x9b","⁛") 
        cadena=cadena.replace("/xe2/x81/x9c","⁜") 
        cadena=cadena.replace("/xe2/x81/x9d","⁝") 
        cadena=cadena.replace("/xe2/x81/x9e","⁞") 
        cadena=cadena.replace("/xe2/x81/xb0","⁰") 
        cadena=cadena.replace("/xe2/x81/xb1","ⁱ") 
        cadena=cadena.replace("/xe2/x81/xb4","⁴") 
        cadena=cadena.replace("/xe2/x81/xb5","⁵") 
        cadena=cadena.replace("/xe2/x81/xb6","⁶") 
        cadena=cadena.replace("/xe2/x81/xb7","⁷") 
        cadena=cadena.replace("/xe2/x81/xb8","⁸") 
        cadena=cadena.replace("/xe2/x81/xb9","⁹") 
        cadena=cadena.replace("/xe2/x81/xba","⁺") 
        cadena=cadena.replace("/xe2/x81/xbb","⁻") 
        cadena=cadena.replace("/xe2/x81/xbc","⁼") 
        cadena=cadena.replace("/xe2/x81/xbd","⁽") 
        cadena=cadena.replace("/xe2/x81/xbe","⁾") 
        cadena=cadena.replace("/xe2/x81/xbf","ⁿ") 
        cadena=cadena.replace("\\054",",")
        #---------------------------------------
        cadena=cadena.replace("%20",' ') 
        cadena=cadena.replace("%7B","{") 
        cadena=cadena.replace("%7D","}")
        cadena=cadena.replace("%C3%91","Ñ")
        cadena=cadena.replace("%C3%B1","ñ")
        cadena=cadena.replace("%3A",":")
        cadena=cadena.replace("%2C",",") 
        cadena=cadena.replace("%5B","[") 
        cadena=cadena.replace("%5D","]") 
        cadena=cadena.replace("%2F","/")
        cadena=cadena.replace("%3C","<") 
        cadena=cadena.replace("%3E",">") 
        cadena=cadena.replace("%0A","\n") 
        cadena=cadena.replace("%3D","=") 
        cadena=cadena.replace("%22",'"') 
        cadena=cadena.replace("%09",' ') 
        cadena=cadena.replace("%C2%A1","¡")
        cadena=cadena.replace("%C2%A2","¢")
        cadena=cadena.replace("%C2%A3","£")
        cadena=cadena.replace("%C2%A4","¤")
        cadena=cadena.replace("%C2%A5","¥")
        cadena=cadena.replace("%C2%A6","¦")
        cadena=cadena.replace("%C2%A7","§")
        cadena=cadena.replace("%C2%A8","¨")
        cadena=cadena.replace("%C2%A9","©")
        cadena=cadena.replace("%C2%AA","ª")
        cadena=cadena.replace("%C2%AB","«")
        cadena=cadena.replace("%C2%AC","¬")
        cadena=cadena.replace("%C2%AE","®")
        cadena=cadena.replace("%C2%AF","¯")
        cadena=cadena.replace("%C2%B0","°")
        cadena=cadena.replace("%C2%B1","±")
        cadena=cadena.replace("%C2%B2","²")
        cadena=cadena.replace("%C2%B3","³")
        cadena=cadena.replace("%C2%B4","´")
        cadena=cadena.replace("%C2%B5","µ")
        cadena=cadena.replace("%C2%B6","¶")
        cadena=cadena.replace("%C2%B7","·")
        cadena=cadena.replace("%C2%B8","¸")
        cadena=cadena.replace("%C2%B9","¹")
        cadena=cadena.replace("%C2%BA","º")
        cadena=cadena.replace("%C2%BB","»")
        cadena=cadena.replace("%C2%BC","¼")
        cadena=cadena.replace("%C2%BD","½")
        cadena=cadena.replace("%C2%BE","¾")
        cadena=cadena.replace("%C2%BF","¿")
        cadena=cadena.replace("%C3%80","À")
        cadena=cadena.replace("%C3%81","Á")
        cadena=cadena.replace("%C3%82","Â")
        cadena=cadena.replace("%C3%83","Ã")
        cadena=cadena.replace("%C3%84","Ä")
        cadena=cadena.replace("%C3%85","Å")
        cadena=cadena.replace("%C3%86","Æ")
        cadena=cadena.replace("%C3%87","Ç")
        cadena=cadena.replace("%C3%88","È")
        cadena=cadena.replace("%C3%89","É")
        cadena=cadena.replace("%C3%8A","Ê")
        cadena=cadena.replace("%C3%8B","Ë")
        cadena=cadena.replace("%C3%8C","Ì")
        cadena=cadena.replace("%C3%8D","Í")
        cadena=cadena.replace("%C3%8E","Î")
        cadena=cadena.replace("%C3%8F","Ï")
        cadena=cadena.replace("%C3%90","Ð")
        cadena=cadena.replace("%C3%91","Ñ")
        cadena=cadena.replace("%C3%92","Ò")
        cadena=cadena.replace("%C3%93","Ó")
        cadena=cadena.replace("%C3%94","Ô")
        cadena=cadena.replace("%C3%95","Õ")
        cadena=cadena.replace("%C3%96","Ö")
        cadena=cadena.replace("%C3%97","×")
        cadena=cadena.replace("%C3%98","Ø")
        cadena=cadena.replace("%C3%99","Ù")
        cadena=cadena.replace("%C3%9A","Ú")
        cadena=cadena.replace("%C3%9B","Û")
        cadena=cadena.replace("%C3%9C","Ü")
        cadena=cadena.replace("%C3%9D","Ý")
        cadena=cadena.replace("%C3%9E","Þ")
        cadena=cadena.replace("%C3%9F","ß")
        cadena=cadena.replace("%C3%A0","à")
        cadena=cadena.replace("%C3%A1","á")
        cadena=cadena.replace("%C3%A2","â")
        cadena=cadena.replace("%C3%A3","ã")
        cadena=cadena.replace("%C3%A4","ä")
        cadena=cadena.replace("%C3%A5","å")
        cadena=cadena.replace("%C3%A6","æ")
        cadena=cadena.replace("%C3%A7","ç")
        cadena=cadena.replace("%C3%A8","è")
        cadena=cadena.replace("%C3%A9","é")
        cadena=cadena.replace("%C3%AA","ê")
        cadena=cadena.replace("%C3%AB","ë")
        cadena=cadena.replace("%C3%AC","ì")
        cadena=cadena.replace("%C3%AD","í")
        cadena=cadena.replace("%C3%AE","î")
        cadena=cadena.replace("%C3%AF","ï")
        cadena=cadena.replace("%C3%B0","ð")
        cadena=cadena.replace("%C3%B1","ñ")
        cadena=cadena.replace("%C3%B2","ò")
        cadena=cadena.replace("%C3%B3","ó")
        cadena=cadena.replace("%C3%B4","ô")
        cadena=cadena.replace("%C3%B5","õ")
        cadena=cadena.replace("%C3%B6","ö")
        cadena=cadena.replace("%C3%B7","÷")
        cadena=cadena.replace("%C3%B8","ø")
        cadena=cadena.replace("%C3%B9","ù")
        cadena=cadena.replace("%C3%BA",'ú') 
        cadena=cadena.replace("%C3%B3",'ó') 
        cadena=cadena.replace("%C3%99","Ù")
        cadena=cadena.replace("%C3%9A","Ú")
        cadena=cadena.replace("%C3%9B","Û")
        cadena=cadena.replace("%C3%9C","Ü")
        cadena=cadena.replace("%C3%9D","Ý")
        cadena=cadena.replace("%C3%9E","Þ")
        cadena=cadena.replace("%C3%9F","ß")
        cadena=cadena.replace("%C3%A0","à")
        cadena=cadena.replace("%C3%A1","á")
        cadena=cadena.replace("%C3%A2","â")
        cadena=cadena.replace("%C3%A3","ã")
        cadena=cadena.replace("%C3%A4","ä")
        cadena=cadena.replace("%C3%A5","å")
        cadena=cadena.replace("%C3%A6","æ")
        cadena=cadena.replace("%C3%A7","ç")
        cadena=cadena.replace("%C3%A8","è")
        cadena=cadena.replace("%C3%A9","é")
        cadena=cadena.replace("%C3%AA","ê")
        cadena=cadena.replace("%C3%AB","ë")
        cadena=cadena.replace("%C3%AC","ì")
        cadena=cadena.replace("%C3%AD","í")
        cadena=cadena.replace("%C3%AE","î")
        cadena=cadena.replace("%C3%AF","ï")
        cadena=cadena.replace("%C3%B0","ð")
        cadena=cadena.replace("%C3%B1","ñ")
        cadena=cadena.replace("%C3%B2","ò")
        cadena=cadena.replace("%C3%B3","ó")
        cadena=cadena.replace("%C3%B4","ô")
        cadena=cadena.replace("%C3%B5","õ")
        cadena=cadena.replace("%C3%B6","ö")
        cadena=cadena.replace("%C3%B7","÷")
        cadena=cadena.replace("%C3%B8","ø")
        cadena=cadena.replace("%C3%B9","ù")
        cadena=cadena.replace("%C3%BA","ú")
        cadena=cadena.replace("%C3%BB","û")
        cadena=cadena.replace("%C3%BV","ü")
        cadena=cadena.replace("%C3%BD","ý")
        cadena=cadena.replace("%C3%BE","þ")
        cadena=cadena.replace("%C3%BF","ÿ")
        cadena=cadena.replace("%3F","?")
        cadena=cadena.replace("%E2%80%91","‑") 
        cadena=cadena.replace("%E2%80%92","‒") 
        cadena=cadena.replace("%E2%80%93","–") 
        cadena=cadena.replace("%E2%80%94","—") 
        cadena=cadena.replace("%E2%80%95","―") 
        cadena=cadena.replace("%E2%80%96","‖") 
        cadena=cadena.replace("%E2%80%97","‗") 
        cadena=cadena.replace("%E2%80%98","‘") 
        cadena=cadena.replace("%E2%80%99","’") 
        cadena=cadena.replace("%E2%80%9A","‚") 
        cadena=cadena.replace("%E2%80%9B","‛") 
        cadena=cadena.replace("%E2%80%9C","“") 
        cadena=cadena.replace("%E2%80%9D","”") 
        cadena=cadena.replace("%E2%80%9E","„") 
        cadena=cadena.replace("%E2%80%9F","‟") 
        cadena=cadena.replace("%E2%80%A0","†") 
        cadena=cadena.replace("%E2%80%A1","‡") 
        cadena=cadena.replace("%E2%80%A2","•") 
        cadena=cadena.replace("%E2%80%A3","‣") 
        cadena=cadena.replace("%E2%80%A4","․") 
        cadena=cadena.replace("%E2%80%A5","‥") 
        cadena=cadena.replace("%E2%80%A6","…") 
        cadena=cadena.replace("%E2%80%A7","‧") 
        cadena=cadena.replace("%E2%80%B0","‰") 
        cadena=cadena.replace("%E2%80%B1","‱") 
        cadena=cadena.replace("%E2%80%B2","′") 
        cadena=cadena.replace("%E2%80%B3","″") 
        cadena=cadena.replace("%E2%80%B4","‴") 
        cadena=cadena.replace("%E2%80%B5","‵") 
        cadena=cadena.replace("%E2%80%B6","‶") 
        cadena=cadena.replace("%E2%80%B7","‷") 
        cadena=cadena.replace("%E2%80%B8","‸") 
        cadena=cadena.replace("%E2%80%B9","‹") 
        cadena=cadena.replace("%E2%80%BA","›") 
        cadena=cadena.replace("%E2%80%BB","※") 
        cadena=cadena.replace("%E2%80%BC","‼") 
        cadena=cadena.replace("%E2%80%BD","‽") 
        cadena=cadena.replace("%E2%80%BE","‾") 
        cadena=cadena.replace("%E2%80%BF","‿") 
        cadena=cadena.replace("%E2%81%80","⁀") 
        cadena=cadena.replace("%E2%81%81","⁁") 
        cadena=cadena.replace("%E2%81%82","⁂") 
        cadena=cadena.replace("%E2%81%83","⁃") 
        cadena=cadena.replace("%E2%81%84","⁄") 
        cadena=cadena.replace("%E2%81%85","⁅") 
        cadena=cadena.replace("%E2%81%86","⁆") 
        cadena=cadena.replace("%E2%81%87","⁇") 
        cadena=cadena.replace("%E2%81%88","⁈") 
        cadena=cadena.replace("%E2%81%89","⁉") 
        cadena=cadena.replace("%E2%81%8A","⁊") 
        cadena=cadena.replace("%E2%81%8B","⁋") 
        cadena=cadena.replace("%E2%81%8C","⁌") 
        cadena=cadena.replace("%E2%81%8D","⁍") 
        cadena=cadena.replace("%E2%81%8E","⁎") 
        cadena=cadena.replace("%E2%81%8F","⁏") 
        cadena=cadena.replace("%E2%81%90","⁐") 
        cadena=cadena.replace("%E2%81%91","⁑") 
        cadena=cadena.replace("%E2%81%92","⁒") 
        cadena=cadena.replace("%E2%81%93","⁓") 
        cadena=cadena.replace("%E2%81%94","⁔") 
        cadena=cadena.replace("%E2%81%95","⁕") 
        cadena=cadena.replace("%E2%81%96","⁖") 
        cadena=cadena.replace("%E2%81%97","⁗") 
        cadena=cadena.replace("%E2%81%98","⁘") 
        cadena=cadena.replace("%E2%81%99","⁙") 
        cadena=cadena.replace("%E2%81%9A","⁚") 
        cadena=cadena.replace("%E2%81%9B","⁛") 
        cadena=cadena.replace("%E2%81%9C","⁜") 
        cadena=cadena.replace("%E2%81%9D","⁝") 
        cadena=cadena.replace("%E2%81%9E","⁞") 
        cadena=cadena.replace("%E2%81%B0","⁰") 
        cadena=cadena.replace("%E2%81%B1","ⁱ") 
        cadena=cadena.replace("%E2%81%B4","⁴") 
        cadena=cadena.replace("%E2%81%B5","⁵") 
        cadena=cadena.replace("%E2%81%B6","⁶") 
        cadena=cadena.replace("%E2%81%B7","⁷") 
        cadena=cadena.replace("%E2%81%B8","⁸") 
        cadena=cadena.replace("%E2%81%B9","⁹") 
        cadena=cadena.replace("%E2%81%Ba","⁺") 
        cadena=cadena.replace("%E2%81%BB","⁻") 
        cadena=cadena.replace("%E2%81%BC","⁼") 
        cadena=cadena.replace("%E2%81%BD","⁽") 
        cadena=cadena.replace("%E2%81%BE","⁾") 
        cadena=cadena.replace("%E2%81%BF","ⁿ") 
        cadena=cadena.replace("%40","@")
        cadena=cadena.replace("%3B",";") 
        cadena=cadena.replace("%25","%")
        cadena=cadena.replace("%23","#") 
        cadena=cadena.replace("%24","$")
        cadena=cadena.replace("%2B","+")
        cadena=cadena.replace("%7C","|") 
        cadena=cadena.replace("%5C","\\")
        cadena=cadena.replace("%26","&") 
    return cadena

def encode(cadena):
    if type(cadena)==str or type(cadena)==unicode:
        cadena=cadena.replace(' ',"%20") 
        cadena=cadena.replace("{","%7B") 
        cadena=cadena.replace("}","%7D")
        cadena=cadena.replace("Ñ","%C3%91")
        cadena=cadena.replace("ñ","%C3%B1")
        cadena=cadena.replace(":","%3A")
        cadena=cadena.replace(",","%2C") 
        cadena=cadena.replace("[","%5B") 
        cadena=cadena.replace("]","%5D") 
        cadena=cadena.replace("/","%2F")
        cadena=cadena.replace("<","%3C") 
        cadena=cadena.replace(">","%3E") 
        cadena=cadena.replace("\n","%0A") 
        cadena=cadena.replace("=","%3D") 
        cadena=cadena.replace('"',"%22") 
        cadena=cadena.replace(' ',"%09") 
        cadena=cadena.replace("¡","%C2%A1")
        cadena=cadena.replace("¢","%C2%A2")
        cadena=cadena.replace("£","%C2%A3")
        cadena=cadena.replace("¤","%C2%A4")
        cadena=cadena.replace("¥","%C2%A5")
        cadena=cadena.replace("¦","%C2%A6")
        cadena=cadena.replace("§","%C2%A7")
        cadena=cadena.replace("¨","%C2%A8")
        cadena=cadena.replace("©","%C2%A9")
        cadena=cadena.replace("ª","%C2%AA")
        cadena=cadena.replace("«","%C2%AB")
        cadena=cadena.replace("¬","%C2%AC")
        cadena=cadena.replace("®","%C2%AE")
        cadena=cadena.replace("¯","%C2%AF")
        cadena=cadena.replace("°","%C2%B0")
        cadena=cadena.replace("±","%C2%B1")
        cadena=cadena.replace("²","%C2%B2")
        cadena=cadena.replace("³","%C2%B3")
        cadena=cadena.replace("´","%C2%B4")
        cadena=cadena.replace("µ","%C2%B5")
        cadena=cadena.replace("¶","%C2%B6")
        cadena=cadena.replace("·","%C2%B7")
        cadena=cadena.replace("¸","%C2%B8")
        cadena=cadena.replace("¹","%C2%B9")
        cadena=cadena.replace("º","%C2%BA")
        cadena=cadena.replace("»","%C2%BB")
        cadena=cadena.replace("¼","%C2%BC")
        cadena=cadena.replace("½","%C2%BD")
        cadena=cadena.replace("¾","%C2%BE")
        cadena=cadena.replace("¿","%C2%BF")
        cadena=cadena.replace("À","%C3%80")
        cadena=cadena.replace("Á","%C3%81")
        cadena=cadena.replace("Â","%C3%82")
        cadena=cadena.replace("Ã","%C3%83")
        cadena=cadena.replace("Ä","%C3%84")
        cadena=cadena.replace("Å","%C3%85")
        cadena=cadena.replace("Æ","%C3%86")
        cadena=cadena.replace("Ç","%C3%87")
        cadena=cadena.replace("È","%C3%88")
        cadena=cadena.replace("É","%C3%89")
        cadena=cadena.replace("Ê","%C3%8A")
        cadena=cadena.replace("Ë","%C3%8B")
        cadena=cadena.replace("Ì","%C3%8C")
        cadena=cadena.replace("Í","%C3%8D")
        cadena=cadena.replace("Î","%C3%8E")
        cadena=cadena.replace("Ï","%C3%8F")
        cadena=cadena.replace("Ð","%C3%90")
        cadena=cadena.replace("Ñ","%C3%91")
        cadena=cadena.replace("Ò","%C3%92")
        cadena=cadena.replace("Ó","%C3%93")
        cadena=cadena.replace("Ô","%C3%94")
        cadena=cadena.replace("Õ","%C3%95")
        cadena=cadena.replace("Ö","%C3%96")
        cadena=cadena.replace("×","%C3%97")
        cadena=cadena.replace("Ø","%C3%98")
        cadena=cadena.replace("Ù","%C3%99")
        cadena=cadena.replace("Ú","%C3%9A")
        cadena=cadena.replace("Û","%C3%9B")
        cadena=cadena.replace("Ü","%C3%9C")
        cadena=cadena.replace("Ý","%C3%9D")
        cadena=cadena.replace("Þ","%C3%9E")
        cadena=cadena.replace("ß","%C3%9F")
        cadena=cadena.replace("à","%C3%A0")
        cadena=cadena.replace("á","%C3%A1")
        cadena=cadena.replace("â","%C3%A2")
        cadena=cadena.replace("ã","%C3%A3")
        cadena=cadena.replace("ä","%C3%A4")
        cadena=cadena.replace("å","%C3%A5")
        cadena=cadena.replace("æ","%C3%A6")
        cadena=cadena.replace("ç","%C3%A7")
        cadena=cadena.replace("è","%C3%A8")
        cadena=cadena.replace("é","%C3%A9")
        cadena=cadena.replace("ê","%C3%AA")
        cadena=cadena.replace("ë","%C3%AB")
        cadena=cadena.replace("ì","%C3%AC")
        cadena=cadena.replace("í","%C3%AD")
        cadena=cadena.replace("î","%C3%AE")
        cadena=cadena.replace("ï","%C3%AF")
        cadena=cadena.replace("ð","%C3%B0")
        cadena=cadena.replace("ñ","%C3%B1")
        cadena=cadena.replace("ò","%C3%B2")
        cadena=cadena.replace("ó","%C3%B3")
        cadena=cadena.replace("ô","%C3%B4")
        cadena=cadena.replace("õ","%C3%B5")
        cadena=cadena.replace("ö","%C3%B6")
        cadena=cadena.replace("÷","%C3%B7")
        cadena=cadena.replace("ø","%C3%B8")
        cadena=cadena.replace("ù","%C3%B9")
        cadena=cadena.replace('ú',"%C3%BA") 
        cadena=cadena.replace('ó',"%C3%B3") 
        cadena=cadena.replace("Ù","%C3%99")
        cadena=cadena.replace("Ú","%C3%9A")
        cadena=cadena.replace("Û","%C3%9B")
        cadena=cadena.replace("Ü","%C3%9C")
        cadena=cadena.replace("Ý","%C3%9D")
        cadena=cadena.replace("Þ","%C3%9E")
        cadena=cadena.replace("ß","%C3%9F")
        cadena=cadena.replace("à","%C3%A0")
        cadena=cadena.replace("á","%C3%A1")
        cadena=cadena.replace("â","%C3%A2")
        cadena=cadena.replace("ã","%C3%A3")
        cadena=cadena.replace("ä","%C3%A4")
        cadena=cadena.replace("å","%C3%A5")
        cadena=cadena.replace("æ","%C3%A6")
        cadena=cadena.replace("ç","%C3%A7")
        cadena=cadena.replace("è","%C3%A8")
        cadena=cadena.replace("é","%C3%A9")
        cadena=cadena.replace("ê","%C3%AA")
        cadena=cadena.replace("ë","%C3%AB")
        cadena=cadena.replace("ì","%C3%AC")
        cadena=cadena.replace("í","%C3%AD")
        cadena=cadena.replace("î","%C3%AE")
        cadena=cadena.replace("ï","%C3%AF")
        cadena=cadena.replace("ð","%C3%B0")
        cadena=cadena.replace("ñ","%C3%B1")
        cadena=cadena.replace("ò","%C3%B2")
        cadena=cadena.replace("ó","%C3%B3")
        cadena=cadena.replace("ô","%C3%B4")
        cadena=cadena.replace("õ","%C3%B5")
        cadena=cadena.replace("ö","%C3%B6")
        cadena=cadena.replace("÷","%C3%B7")
        cadena=cadena.replace("ø","%C3%B8")
        cadena=cadena.replace("ù","%C3%B9")
        cadena=cadena.replace("ú","%C3%BA")
        cadena=cadena.replace("û","%C3%BB")
        cadena=cadena.replace("ü","%C3%BV")
        cadena=cadena.replace("ý","%C3%BD")
        cadena=cadena.replace("þ","%C3%BE")
        cadena=cadena.replace("ÿ","%C3%BF")
        cadena=cadena.replace("?","%3F")
        cadena=cadena.replace("‑","%E2%80%91") 
        cadena=cadena.replace("‒","%E2%80%92") 
        cadena=cadena.replace("–","%E2%80%93") 
        cadena=cadena.replace("—","%E2%80%94") 
        cadena=cadena.replace("―","%E2%80%95") 
        cadena=cadena.replace("‖","%E2%80%96") 
        cadena=cadena.replace("‗","%E2%80%97") 
        cadena=cadena.replace("‘","%E2%80%98") 
        cadena=cadena.replace("’","%E2%80%99") 
        cadena=cadena.replace("‚","%E2%80%9A") 
        cadena=cadena.replace("‛","%E2%80%9B") 
        cadena=cadena.replace("“","%E2%80%9C") 
        cadena=cadena.replace("”","%E2%80%9D") 
        cadena=cadena.replace("„","%E2%80%9E") 
        cadena=cadena.replace("‟","%E2%80%9F") 
        cadena=cadena.replace("†","%E2%80%A0") 
        cadena=cadena.replace("‡","%E2%80%A1") 
        cadena=cadena.replace("•","%E2%80%A2") 
        cadena=cadena.replace("‣","%E2%80%A3") 
        cadena=cadena.replace("․","%E2%80%A4") 
        cadena=cadena.replace("‥","%E2%80%A5") 
        cadena=cadena.replace("…","%E2%80%A6") 
        cadena=cadena.replace("‧","%E2%80%A7") 
        cadena=cadena.replace("‰","%E2%80%B0") 
        cadena=cadena.replace("‱","%E2%80%B1") 
        cadena=cadena.replace("′","%E2%80%B2") 
        cadena=cadena.replace("″","%E2%80%B3") 
        cadena=cadena.replace("‴","%E2%80%B4") 
        cadena=cadena.replace("‵","%E2%80%B5") 
        cadena=cadena.replace("‶","%E2%80%B6") 
        cadena=cadena.replace("‷","%E2%80%B7") 
        cadena=cadena.replace("‸","%E2%80%B8") 
        cadena=cadena.replace("‹","%E2%80%B9") 
        cadena=cadena.replace("›","%E2%80%BA") 
        cadena=cadena.replace("※","%E2%80%BB") 
        cadena=cadena.replace("‼","%E2%80%BC") 
        cadena=cadena.replace("‽","%E2%80%BD") 
        cadena=cadena.replace("‾","%E2%80%BE") 
        cadena=cadena.replace("‿","%E2%80%BF") 
        cadena=cadena.replace("⁀","%E2%81%80") 
        cadena=cadena.replace("⁁","%E2%81%81") 
        cadena=cadena.replace("⁂","%E2%81%82") 
        cadena=cadena.replace("⁃","%E2%81%83") 
        cadena=cadena.replace("⁄","%E2%81%84") 
        cadena=cadena.replace("⁅","%E2%81%85") 
        cadena=cadena.replace("⁆","%E2%81%86") 
        cadena=cadena.replace("⁇","%E2%81%87") 
        cadena=cadena.replace("⁈","%E2%81%88") 
        cadena=cadena.replace("⁉","%E2%81%89") 
        cadena=cadena.replace("⁊","%E2%81%8A") 
        cadena=cadena.replace("⁋","%E2%81%8B") 
        cadena=cadena.replace("⁌","%E2%81%8C") 
        cadena=cadena.replace("⁍","%E2%81%8D") 
        cadena=cadena.replace("⁎","%E2%81%8E") 
        cadena=cadena.replace("⁏","%E2%81%8F") 
        cadena=cadena.replace("⁐","%E2%81%90") 
        cadena=cadena.replace("⁑","%E2%81%91") 
        cadena=cadena.replace("⁒","%E2%81%92") 
        cadena=cadena.replace("⁓","%E2%81%93") 
        cadena=cadena.replace("⁔","%E2%81%94") 
        cadena=cadena.replace("⁕","%E2%81%95") 
        cadena=cadena.replace("%E2%81%96","⁖") 
        cadena=cadena.replace("%E2%81%97","⁗") 
        cadena=cadena.replace("%E2%81%98","⁘") 
        cadena=cadena.replace("%E2%81%99","⁙") 
        cadena=cadena.replace("%E2%81%9A","⁚") 
        cadena=cadena.replace("%E2%81%9B","⁛") 
        cadena=cadena.replace("%E2%81%9C","⁜") 
        cadena=cadena.replace("%E2%81%9D","⁝") 
        cadena=cadena.replace("%E2%81%9E","⁞") 
        cadena=cadena.replace("%E2%81%B0","⁰") 
        cadena=cadena.replace("%E2%81%B1","ⁱ") 
        cadena=cadena.replace("%E2%81%B4","⁴") 
        cadena=cadena.replace("%E2%81%B5","⁵") 
        cadena=cadena.replace("%E2%81%B6","⁶") 
        cadena=cadena.replace("%E2%81%B7","⁷") 
        cadena=cadena.replace("%E2%81%B8","⁸") 
        cadena=cadena.replace("%E2%81%B9","⁹") 
        cadena=cadena.replace("%E2%81%Ba","⁺") 
        cadena=cadena.replace("%E2%81%BB","⁻") 
        cadena=cadena.replace("%E2%81%BC","⁼") 
        cadena=cadena.replace("%E2%81%BD","⁽") 
        cadena=cadena.replace("%E2%81%BE","⁾") 
        cadena=cadena.replace("%E2%81%BF","ⁿ") 
        cadena=cadena.replace("@","%40")
        cadena=cadena.replace(";","%3B") 
        cadena=cadena.replace("%","%25")
        cadena=cadena.replace("#","%23") 
        cadena=cadena.replace("$","%24")
        cadena=cadena.replace("+","%2B")
        cadena=cadena.replace("|","%7C") 
        cadena=cadena.replace("\\","%5C")
        cadena=cadena.replace("&","%26") 
    return cadena
def normalizar(v):
    

    if (type(v)==str or type(v)==unicode) and v not in list(globals()):
        if ";" not in v:
            try:
                v=decode(v.strip())
                if v not in globals():
                    exec("a="+v)
                    return a
                else:
                    return v
            except Exception,e:
                return v
        else:
            return v
    else:
        
        return v
def getCookie():
    import os
    cookies={}
    if "HTTP_COOKIE" in os.environ:
        
        
        for elem in os.environ["HTTP_COOKIE"].split(";"):

            if "=" in elem:                
                k,v=elem.split("=")
                cookies[k.strip()]=normalizar(v)

    return cookies
def zAPI(linea,vars):
        for elem in vars:
            exec(elem+"=vars['"+elem+"']")
        if len(linea)<=200:     
            c=0
            mark=0
            mark2=0#para los bucles y condicionales
            codigo=""
            nivel=0
            condicion=[]
            funciones=0
            enlace=False
            lineas=0
            __r=None

            while c<len(linea):
                #si hay condiciones
                if len(condicion)>1:
                    if condicion[-1]=="==" or condicion[-1]=="!=" or condicion[-1]==">=" or condicion[-1]=="<=" or condicion[-1]=="<" or condicion[-1]==">" or condicion[-1]=="in" or condicion[-1]=="for " or condicion[-1]=="while ":

                        if c>0 and c<=3:
                            if  linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                                if  linea[c-2]=="=" and linea[c-1]=="=":
                                    #if len()
                                    pass
                                elif linea[c-2]=="!" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]!="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]!="=":
                                    pass
                                #es una asignacion
                                elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                    pass
                                pass
                            pass

                        #------------------------------
                        if c>=3 and c<=5:
                            if  linea[c-1]!=" " and linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                                if  linea[c-2]=="=" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="!" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]=="=":
                                    pass
                                elif linea[c-2]=="<" and linea[c-1]!="=":
                                    pass
                                elif linea[c-2]==">" and linea[c-1]!="=":
                                    pass
                                #es una asignacion
                                elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                    pass
                                pass


                            elif linea[c-1]==" " and linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                                if  linea[c-3]=="=" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]=="!" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]==">" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]=="<" and linea[c-2]=="=":
                                    pass
                                elif linea[c-3]=="<" and linea[c-2]!="=":
                                    pass
                                elif linea[c-3]==">" and linea[c-2]!="=":
                                    pass
                                pass

                        #para lo anterior y bucle while
                        if c>=5 and c<=9:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                pass
                            pass
                        #para bucle for
                        elif c>=9:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                pass
                            pass
                            
                        #para bucle while y for
                        elif c>=11 and c<13:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                        
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                if "for " in linea[:c-3]:
                                    pass
                                else:
                                    pass
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                if "while " in linea[:c-3]:
                                    pass
                                else:
                                    pass
                            
                        #para el bucle while con in
                        elif c>=13:
                            if linea[c-1]=="=" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="!" and linea[c]=="=":
                                pass
                            elif linea[c-1]==">" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]=="=":
                                pass
                            elif linea[c-1]=="<" and linea[c]!="=":
                                pass
                            elif linea[c-1]==">" and linea[c]!="=":
                                pass
                            #usa in
                            elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                                
                                if "for " in linea[:c-3]:
                                    pass
                                else:
                                    pass
                                pass
                            #es una asignacion
                            elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                                
                                if "while " in linea[:c-3]:
                                    pass

                                else:
                                    pass
                            else:

                                if linea[c]==";":
                                    if nivel==0:
                                        codigo.append(linea[mark:c])
                                        mark=c
                                        lineas+=1
                                    else:
                                        tab=" "*condicion
                                        codigo.append(tab+linea[mark:c])
                                        lineas+=1



                                elif linea[c]=="]":
                                    pass
                                elif linea[c]=="}":
                                    pass
                                elif linea[c]=="]]":
                                    pass
                                elif linea[c]=="}}":
                                    pass

                        else:
                            if linea[c]==";":
                                pass
                            elif linea[c]=="]":
                                pass
                            elif linea[c]=="}":
                                pass
                            elif linea[c]=="]]":
                                pass
                            elif linea[c]=="}}":
                                pass


                else:
                    #para una pregunta boolean
                    if c>0 and c<=3:
                        if  linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":

                            if  linea[c-2]=="=" and linea[c-1]=="=":
                                        
                                    if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])


                            elif linea[c-2]=="!" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]!="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]!="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            #es una asignacion
                            elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                if len(linea)<=4:
                                        exec("__r="+linea[mark:c+1])
                            pass
                        pass

                    #------------------------------
                    if c>=3 and c<=7:
                        if  linea[c-1]!=" " and linea[c]!="=" and linea[c]!="!" and linea[c]!="<" and linea[c]!=">" and linea[c]!=" ":
                            if  linea[c-2]=="=" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="!" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]=="<" and linea[c-1]!="=":
                                exec("__r="+linea[mark:c+1])
                            elif linea[c-2]==">" and linea[c-1]!="=":
                                exec("__r="+linea[mark:c+1])
                            #es una asignacion
                            elif linea[c-4]!=">" and linea[c-3]!="!" and linea[c-2]!="<" and linea[c-1]=="=":
                                exec("__r="+linea[mark:c+1])
                            pass


                    #para lo anterior y bucle while
                    if c>7 and c<=10:

                        if linea[c-1]=="=" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="!" and linea[c]=="=":
                            pass
                        elif linea[c-1]==">" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]!="=":
                            pass
                        elif linea[c-1]==">" and linea[c]!="=":
                            pass
                        #usa in
                        elif " in " in linea[mark:c-2] and linea[c-2]==" " and linea[c]!=" ":
                            nivel+=1
                            
                            if condicion==[]:
                                codigo+="if "+linea[mark:c-2]+":\n"
                                mark=c
                            else:
                                if condicion[-1]=="if":
                                    pass
                                elif condicion[-1]=="elif":
                                    pass

                            mark=c
                            condicion.append("for")


                        #es una asignacion
                        elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                            pass
                        else:
                            if nivel>0:
                                tab=" "*nivel
                                if linea[c]==":":
                                    
                                    codigo+=tab+linea[mark-1:c]+"("
                                    c+=1
                                    mark=c

                                    funciones+=1
                                if linea[c]==";":
                                    if funciones>0:
                                        codigo+=tab+linea[mark:c]+")"
                                    else:
                                        codigo+="\n"
                                else:
                                    pass
                        
                    #para bucle for
                    elif c>10 and c<=13:
                        if linea[c-1]=="=" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="!" and linea[c]=="=":
                            pass
                        elif linea[c-1]==">" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]!="=":
                            pass
                        elif linea[c-1]==">" and linea[c]!="=":
                            pass
                        #usa in
                        elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                            pass
                        #es una asignacion
                        elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                            pass
                        else:
                            if nivel>0:
                                pass
                            
                        
                    #para bucle while y for
                    elif c>13:
                        if linea[c-1]=="=" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="!" and linea[c]=="=":
                            pass
                        elif linea[c-1]==">" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]=="=":
                            pass
                        elif linea[c-1]=="<" and linea[c]!="=":
                            pass
                        elif linea[c-1]==">" and linea[c]!="=":
                            pass
                    
                        #usa in
                        elif linea[c-3]==" " and linea[c-2]=="i" and linea[c-1]=="n" and linea[c]==" ":
                            if "for " in linea[:c-3]:
                                pass
                            else:
                                pass
                            pass
                        #es una asignacion
                        elif linea[c-1]!=">" and linea[c-1]!="!" and linea[c-1]!="<" and linea[c]=="=":
                            if "while " in linea[:c-3]:
                                pass
                            else:
                                pass
                        else:
                            if nivel>0:
                                pass

                        
                    #para el bucle while con in
                    
                c+=1
            if funciones>0:
                codigo+=linea[mark:c]+")"
        try:
            print "-----------"
            print codigo
            print "-----------"
            exec(codigo)
            return __r
        except Exception,e:
            print e

def urlParamDecod(param):

    return param.replace("+"," ").replace("%40","@").replace("®","reg")
def redirect(url,tiempo=0):
    
    print "<script>location=`"+url.strip()+"`</script>"
def charset(cha="utf-8"):
    print "<meta charset='"+cha+"'>"

def parrafer(cadena,clase=""):
    parrafo=""
    for elem in cadena.split("\n"):
        parrafo+="<p class='"+clase+"'>"+elem+"</p>\n"
    return parrafo


def zform(db,action,controller="post.py",placeholder="",submit="Enviar",i=None,style="",display="block",_class="ff pad-1",ignorar=[],confirmar=[],valores={},clases={}):
    try:
        form=style+"<form name='_FORM"+action+"' id='_FORM"+action+"' action='"+controller+"'"+(" class='text-center "+_class+"'" if display=="block-center" or display=="inline-block-center" else "")+(" class='text-right "+_class+"'" if display=="block-right" or display=="inline-block-right" else "")+(" class='text-justify "+_class+"'" if display=="block-justify" or display=="inline-block-justify" else "")+" method='post'>"
        c=0
        id_elem=1
        d=""
        d2=""

        script=""

        
        for elem in db.campos[db.seleccion]: 

                value=""

                if i!=None:
                            value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                else:

                        
                        if elem[0] in valores:

                            value="value='"+str(valores[elem[0]])+"'"
                        else:
                            value=""

                        if elem[0] in clases:

                            if elem[0] in ignorar:
                                
                                _class=" class='"+clases[elem[0]]+" hidden'"
                            else:
                                
                                _class=" class='"+clases[elem[0]]+"'"
                        else:
                            if elem[0] in ignorar:
                                
                                _class=" class='hidden'"

                            else:
                                
                                _class=""
                if display=="block" or display=="block-center" or display=="block-rigth" or display=="block-justify":
                    d="<br "+_class+">"
                    d2="<br "+_class+">"
                elif display=="inline-block" or display=="inline-block-center" or display=="inline-block-rigth" or display=="inline-block-justify":
                    d2="<br "+_class+">"

                if elem[1]==db.str:
                    if elem[0] in confirmar:

                  
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" id='_CONF"+action+elem[0]+"'><span id='_CONFSPAN"+action+elem[0]+" class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+" class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+" class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+" class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='Confirmar "+placeholder+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+" class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+" class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                        script+="""
                        $('#_CONF"""+action+elem[0]+"""').keyup(function(){
                        
                        if (document.getElementById('"""+action+elem[0]+"""').value== document.getElementById('_CONF"""+action+elem[0]+"""').value){$('#_CONFSPAN"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN2"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(true) }
                        else{
                        $('#_CONFSPAN2"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(flase) }
                        })
                        """
                    else:
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" name='"+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2

                elif elem[1]==db.password:
                    if elem[0] in confirmar:

                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='password' "+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"' id='"+action+elem[0]+"'></div>"+d2
                                id_elem+=2
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='password' "+value+_class+" id='_CONF"+action+elem[0]+"'><span id='_CONFSPAN"+action+elem[0]+"'' class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+"'' class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+"' class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+"' class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+"> Confirmar "+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='password' placeholder='Confirmar "+placeholder+elem[0]+"'"+value+_class+" id='_CONF"+action+elem[0]+"'></div><span id='_CONFSPAN"+action+elem[0]+"' class='hidden bg-ubuntu_green white' >Datos confirmados</span><span id='_CONFSPAN2"+action+elem[0]+"' class='hidden bg-ubuntu_red white'> La confirmación de "+elem[0]+" no coincide </span>"+d2
                                id_elem+=2
                        script+="""
                        $('#_CONF"""+action+elem[0]+"""').keyup(function(){
                        
                        if (document.getElementById('"""+action+elem[0]+"""').value== document.getElementById('_CONF"""+action+elem[0]+"""').value){$('#_CONFSPAN"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN2"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(true) }
                        else{
                        $('#_CONFSPAN2"""+action+elem[0]+"""').removeClass('hidden');$('#_CONFSPAN"""+action+elem[0]+"""').addClass('hidden');$('#_FORM"""+action+"""').val(false) }
                        })
                        """
                    else:
                        if i!=None:
                                value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                        else:
                                value=""
                        if placeholder!="":
                            form+="<div id='zform"+action+str(id_elem)+"'><input type='text' "+value+_class+" name='"+elem[0]+"'></div>"+d
                            id_elem+=1
                        else:
                            if type(placeholder) ==list or type(placeholder) ==tuple:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder[c]+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2
                            else:
                                form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<div id='zform"+action+str(id_elem+1)+"'><input type='text' placeholder='"+placeholder+elem[0]+"'"+value+_class+" name='"+elem[0]+"'></div>"+d2
                                id_elem+=2

                elif elem[1]==db.doc:
                    if placeholder!="":
                        if i!=None:
                            value=str(db.obtenerCampo(i,elem[0]))
                        else:
                            value=""
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<textarea name='"+elem[0]+"'"+_class+">"+value+"</textarea>"+d2
                        id_elem+=2
                    else:
                        if i!=None:
                            value=str(db.obtenerCampo(i,elem[0]))
                        else:
                            value=""
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<textarea placeholder='"+placeholder[c]+elem[0]+"' name='"+elem[0]+"' id='"+action+elem[0]+"'"+_class+">"+value+"</textarea>"+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+"</label>"+d+"<textarea placeholder='"+placeholder+elem[0]+"' name='"+elem[0]+"' id='"+action+elem[0]+"'"+_class+">"+value+"</textarea>"+d2
                            id_elem+=2
                elif elem[1]==db.email:
                    if elem[7]!=-1:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+action+str(id_elem+1)+'"><input  type="email" '+mini+maxi+step+value+_class+'name="'+elem[0]+'"></div>'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+action+str(id_elem+1)+'"><input  type="email" placeholder="'+placeholder[c]+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'"></div>'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+action+str(id_elem+1)+'"><input type="email" placeholder="'+placeholder+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'"></div>'+d2
                            id_elem+=2
                elif elem[1]==db.int or elem[1]==db.float or elem[1]==db.long:
                    if elem[7]!=-1:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'" type="number" '+mini+maxi+step+value+_class+'name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'" type="number" placeholder="'+placeholder[c]+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'" type="number" placeholder="'+placeholder+'"'+mini+maxi+step+value+_class+'name="'+elem[0]+'">'+d2
                            id_elem+=2

                elif elem[1]==db.datetime:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="datetime" onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true)" '''+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="datetime" onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true)" placeholder="'''+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="datetime" onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true)" placeholder="'''+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2

                elif elem[1]==db.time:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="time" onclick="mostrarCalendar(this,'hh:ii')" '''+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="time" onclick="mostrarCalendar(this,'hh:ii')" placeholder="'''+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="time" onclick="mostrarCalendar(this,'hh:ii')" placeholder="'''+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2

                elif elem[1]==db.date:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="date" class="date" onclick="mostrarCalendar(this,'yyyy/mm/dd')" '''+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="date" class="date" onclick="mostrarCalendar(this,'yyyy/mm/dd')" placeholder="'''+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<input id="'+str(id_elem+1)+'''" type="date" class="date" onclick="mostrarCalendar(this,'yyyy/mm/dd')" placeholder="'''+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'">'+d2
                            id_elem+=2
                elif elem[1]==db.file:
                    if elem[7]!=0:
                            maxi=' max="'+str(elem[7])+'"'
                    else:
                        maxi=""
                    if elem[6]!=0:
                        mini=' min="'+str(elem[6])+'"'
                    else:
                        mini=""
                    if elem[8]!=None:
                        step=' step="'+str(elem[8])+'"'
                    else:
                        step=""

                    if i!=None:
                        value=" value='"+str(db.obtenerCampo(i,elem[0]))+"'"
                    else:
                        value=""
                    if placeholder!="":
                        form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+str(id_elem+1)+'"><input type="file" '+mini+maxi+step+value+_class+'></div>'+d2
                        id_elem+=2
                    else:
                        if type(placeholder) ==list or type(placeholder) ==tuple:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+str(id_elem+1)+'"><input type="file" placeholder="'+placeholder[c]+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'"><div>'+d2
                            id_elem+=2
                        else:
                            form+="<label id='zform"+action+str(id_elem)+"' "+_class+">"+elem[0]+'</label>'+d+'<div id="zform'+str(id_elem+1)+'"><input type="file" placeholder="'+placeholder+'"'+mini+maxi+step+value+_class+' name="'+elem[0]+'"></div>'+d2
                            id_elem+=2
                

                c+=1

        return form+"<input type='text' class='hidden' name='action' value='"+action+"'><input type='submit' id='"+str(id_elem+1)+"' class='btn white b-r5' value='"+submit+"'></form><script>"+script+"</script>"
    except Exception, e:
        print "Error en el zform"
        print e

def INPUT(_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_value=""):
    if _type=="time":
        _onclick="mostrarCalendar(this,'hh:ii');"+_onclick
    elif _type=="date":
        _onclick="mostrarCalendar(this,'yyyy/mm/dd');"+_onclick
    elif _type=="datetime":
        _onclick="mostrarCalendar(this,'yyyy/mm/dd hh:ii',true);"+_onclick
    return "<input "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' value="'''+_value+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"

def DIV(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<div "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</div>"

def FORM(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_action=None,_method="post",_zaction=None):
    
    return "<form "+''' method="'''+_method+'''"'''+''' onclick="'''+_onclick+'''"'''+(''' action="'''+_action+'''"''' if _action!=None else '')+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+(INPUT(_name="action",_class="hidden",_value=_zaction) if _zaction!=None else '')+"</form>"
def P(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<p "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</p>"

def B(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<B "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</B>"
def H1(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h1 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h1>"

def H2(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h2 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h2>"

def H3(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h3 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h3>"

def H4(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h4 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h4>"

def H5(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h5 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h5>"

def H6(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h6 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h6>"
def H7(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<h7 "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</h7>"
def SPAN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<span "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</span>"
def ARTICLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<article "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</article>"
def SECTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<section "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</section>"
def BODY(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<body "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</body>"
def HEAD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<head "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</head>"
def HEADER(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<header "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</header>"
def FOOTER(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<footer "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</footer>"
def ASIDE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<aside "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</aside>"
def STYLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<style "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</style>"
def CANVAS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    
    return "<canvas "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</canvas>"
def AUDIO(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):
    
    return "<audio "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</audio>"
def VIDEO(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):
    
    return "<video "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</video>"
def SCRIPT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):    
    return "<script "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</script>"
def NOSCRIPT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="", _src=""):    
    return "<noscript "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' src="'''+_src+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</noscript>"


def NAV(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<aside "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</nav>"
def TABLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<table "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</table>"
def TR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<tr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</tr>"
def TD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<td "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</td>"
def CAPTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<caption "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</caption>"
def COL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<col "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</col>"
def COLGROUP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<colgroup "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</colgroup>"
def MAIN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<main "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</main>"
def LI(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):  
    return "<li "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</li>"
def UL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):  
    return "<ul "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ul>"
def DL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<dl"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dl>"    
def DT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<dt"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dt>"
def DD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<dd"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dd>"        
def FIGURE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<figure"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</figure>"    
def FIGCAPTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<figcaption"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</figcaption>"    
def STRONG(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<strong"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</strong>"    
def EM(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<em"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</em>"    
def S(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<S"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</S>"    
def CITE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<cite"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</cite>"    
def MENU(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<menu"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</menu>"    
def COMMAND(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<command"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</command>"    
def DETALIST(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<detalist"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</detalist>"    
def METER(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<meter"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</meter>"    
def PROGRESS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<progress"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</progress>"    
def OUTPUT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<output"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</output>"    
def KEYGEN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<keygen"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</keygen>"    
def TEXTAREA(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<textarea"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</textarea>"    
def OPTION(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<option"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</option>"    
def DATALIST(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<datalist"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</datalist>"    
def SELECT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<select"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</select>"    
def BUTTON(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<button"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</button>"    
def LABEL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<label"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</label>"    
def legend(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<legend"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</legend>"    
def FIELDSET(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):    
    return "<fieldset"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</fieldset>"    
def MAP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<map "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</map>"
def AREA(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<area "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</area>"

def A(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_href=""):
    
    return "<a "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' href="'''+_href+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</a>"
def IMG(_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_src=""):
    
    return "<img "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' src="'''+_src+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"
def BR(_type="text",_name="",_id="",_onclick="",_class="",_placeholder="",_src=""):
    
    return "<br"+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' src="'''+_src+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"
def SOURCE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<source "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</source>"
def PARAM(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<param "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</param>"
def EMBED(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<embebed "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</embebed>"
def IFRAME(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<iframe "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</iframe>"
def DEL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<del "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</del>"
def INS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<ins "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ins>"
def WBR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<wbr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</wbr>"
def BDO(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<bdo "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</bdo>"
def BDI(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<bdi "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</bdi>"
def MARK(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<mark "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</mark>"
def U(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<u "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</u>"
def I(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<i "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</i>"
def SUB(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<sub "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</sub>"
def SUP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<sup "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</sup>"
def KBD(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<kbd "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</kbd>"
def SAMP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<samp "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</samp>"
def VAR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<var "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</var>"
def CODE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<code "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</code>"   
def TIME(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<time "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</time>"
def DATA(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<data "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</data>"
def ABBR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<abbr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</abbr>"
def DFN(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<dfn "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</dfn>"
def Q(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<q "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</q>"
def SMALL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<small "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</small>"
def PRE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<pre "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</pre>"
def HR(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<hr "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</hr>"
def OL(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<ol "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ol>"
def BLOCKQUOTE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<blockquote "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</blockquote>"
def ADDRESS(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<address "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</address>"
def LINK(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<link "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</link>"
def BASE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<base "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</base>"
def META(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<meta "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</meta>"
def TITLE(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<title "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</title>"
def TRACK(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<track "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</track>"
def MATH(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<math "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</math>"
def OBJECT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<object "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</object>"
def RP(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<rp "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</rp>"
def RT(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<rt "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</rt>"
def RUBY(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<ruby "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</ruby>"
def SUMMARY(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<summary "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</summary>"
def LEGEND(_content="",_type="text",_name="",_id="",_onclick="",_class="",_placeholder=""):
    return "<legend "+''' onclick="'''+_onclick+'''"'''+''' class="'''+_class+'''"'''+''' id="'''+_id+'''"'''+''' placeholder="'''+_placeholder+'''"'''''' type="'''+_type+'''"'''+">"+_content+"</legend>"

def redirecter(base,_app,control,vista="",*args,**kwargs):

    _kwargs=""
    
    for elem in list(kwargs):
        if elem!="seo_url"  and elem !="kwargs":
            _kwargs+=elem+"="+str(kwargs[elem])+"&"
    _kwargs=_kwargs[:-1]

    if "seo_url" in kwargs:
        seo_url=kwargs["seo_url"]
    else:
        seo_url=False


    def redireccionador(seo_url=seo_url,base=base,vista=vista,app=_app,kwargs=kwargs,_kwargs=_kwargs,args=args,control=control):
        
        if type(base)!=str and "base_url" in dir(base):
                seo_url=base.seo_url
                _base=base.base_url
        else:
            _base=base

        if seo_url==False:

            if "kwargs" not in kwargs:
                __kwargs={}
            else:
                __kwargs=kwargs["kwargs"]
            if vista=="":
                _vista=""
            else:
                _vista="&vista="+vista


            redirect(base+"app="+app+"&control="+control+_vista+"&args="+str(args)+_kwargs+"&kwargs="+str(__kwargs))
        else:

            if args!=[]:

                if vista=="":
                    _vista=""
                else:
                    _vista="/"+vista
                _kwargs=""

                if "kwargs" not in kwargs:
                    __kwargs={}
                else:
                    __kwargs=kwargs["kwargs"]
                for elem in list(kwargs):
                    if elem!="seo_url"  and elem !="kwargs":
                        _kwargs+=elem+"="+str(kwargs[elem])+"&"
                _kwargs=_kwargs[:-1]


                if _kwargs!="":
                    if __kwargs!={}:
                        if type(base)!=str and  base.default_app==app and control!=None:
                            redirect(_base)
                        else:
                            redirect(_base+app+"/"+control+(_vista+"/" if _vista!=None else "")+"/".join(args)+"/"+_kwargs+"/"+str(__kwargs))
                            pass
                            

                    else:

                        if type(base)!=str and  base.default_app==app and control==None:
                            redirect(_base)
                        else:
                            redirect(_base+app+"/"+control+(_vista+"/" if _vista!=None else "")+"/".join(args)+"/"+_kwargs)
                            pass
                else:

                    
                    if type(base)!=str and  base.default_app==app and control==None:
                        redirect(_base)

                        pass
                    else:
                        
                        redirect(_base+app+"/"+control+(_vista+"/" if _vista!=None else "")+"/".join(args))
                        pass
            else:
                
                if type(base)!=str and  base.default_app==app and control==None:
                    redirect(_base)
                    pass
                else:
                    redirect(_base+app+"/"+control+(_vista+"/" if _vista!=None else ""))
                    pass

    return redireccionador

def urlBuilder(base,app,control,vista="",*args,**kwargs):
    
    try:

        if "args" in kwargs:
                args=kwargs["args"]

                del kwargs["args"]
        _kwargs=""

        for elem in list(kwargs):
            if elem!="seo_url"  and elem !="kwargs":
                _kwargs+=elem+"="+str(kwargs[elem])+"&"
        _kwargs=_kwargs[:-1]
        

        if "seo_url" in kwargs:
            seo_url=kwargs["seo_url"]
        else:
            seo_url=False
        

        
        if "base_url" in dir(base):
                seo_url=base.seo_url
                base=base.base_url

        if seo_url==False:

            if "kwargs" not in kwargs:
                __kwargs={}
            else:
                __kwargs=kwargs["kwargs"]
            if vista=="":
                _vista=""
            else:
                _vista="&vista="+vista

            return base+"app="+app+"&control="+control+_vista+"&args="+str(args)+_kwargs+"&kwargs="+str(__kwargs)
        else:
            
            if "kwargs" not in kwargs:
                __kwargs={}
            else:
                __kwargs=kwargs["kwargs"]
            
            _kwargs=""


            for elem in list(kwargs):
                if elem!="seo_url"  and elem !="kwargs":
                    _kwargs+=elem+"="+str(kwargs[elem])+"&"
            _kwargs=_kwargs[:-1]

            if vista=="":
                _vista=""
            else:
                _vista="/"+vista
            if list(args)!=[]:
                if _kwargs!="":
                    if __kwargs!={}:
                        if list(args)!=[]:
                            j=""
                            for elem in args:
                                j+="/"+str(elem)
                            if type(base)!=str and  base.default_app==app and control==None:
                                return base
                            else:
                                return base+app+"/"+control+_vista+j+"/"+_kwargs+"/"+str(__kwargs)
                        else:

                            if type(base)!=str and  base.default_app==app and control==None:
                                return base
                            else:
                                return base+app+"/"+control+_vista+"/"+_kwargs+"/"+str(__kwargs)
                    else:

                        if args!=[]:
                            j=""
                            for elem in args:
                                j+="/"+str(elem)
                            if type(base)!=str and  base.default_app==app and control==None:
                                return base
                            else:
                                return base+app+"/"+control+_vista+j+"/"+str(_kwargs)
                        else:
                            return base+app+"/"+control+_vista+"/"+_kwargs
                else:
                    j=""
                    for elem in args:
                        j+="/"+str(elem)
                    
                    if type(base)!=str and  base.default_app==app and control==None:
                        return  base

                    else:
                        return  base+app+"/"+control+_vista+j
            else:

                if __kwargs!={}:
                    if _kwargs!="":
                        if type(base)!=str and  base.default_app==app and control==None:
                            return base
                        else:
                            return base+app+"/"+control+_vista+"/"+_kwargs+"/"+str(__kwargs)
                    else:
                        if type(base)!=str and  base.default_app==app and control==None:
                            return base
                        else:
                            return base+app+"/"+control+_vista+"/"+str(__kwargs)
                else:
                    if type(base)!=str and  base.default_app==app and control==None:
                        return base
                    else:
                        return base+app+"/"+control+_vista

    except Exception,e:
        print e        

def renderTree(folder,folderclass="",fileclass="",sub=False,excluir=None):
    widget=""

    if type(folder)==list and folder!=[]:
        if sub==False:
            subclass= "main-menu"
            widget+="<ul class='marg-l05 "+subclass+"' style='list-style:none'>"
        else:
            subclass= "sub2"
            widget+="<li class='hidden'><ul class='marg-l05 "+subclass+"' style='list-style:none'>"

        
        for k,elem in enumerate(folder):
            if type(elem)==str:
                if excluir==None:
                    widget+="<li class='"+fileclass+"'>"+elem+"</li>"
                else:
                    exclu=False
                    if type(excluir)==str:
                        if  excluir!=elem[-len(excluir):]:    
                            widget+="<li class='"+fileclass+"'>"+elem+"</li>"

                    elif type(excluir)==list:
                        for ex in excluir:
                            if  ex==elem[-len(ex):]:    
                                exclu=True
                        if  exclu==False:
                                widget+="<li class='"+fileclass+"'>"+elem+"</li>"
            else:

                widget+="<li class='"+folderclass+" menu2'>"+elem.keys()[0]+"</li>"+renderTree(elem[elem.keys()[0]],folderclass,fileclass,sub=True,excluir=excluir)

        if sub==False:
            widget+="</ul>"
        else:
            widget+="</ul></li>"

    return widget
def zipextract(archivo,ruta=None):
    import zipfile
    import os
    zf=zipfile.ZipFile(archivo, "r")
    
    carpetas=[]
    import chardet
    folder=archivo[:-len(archivo.split("/")[-1])]
    #zipfile.ZipInfo._decodeFilename = lambda self: self.filename
    #zf.extractall("../"+config.update_folder)
    for m in zf.infolist():

        data = zf.read(m) # extract zipped data into memory

        # convert unicode file path to utf8
        disk_file_name = m.filename.encode('utf8')


        dir_name = os.path.dirname(disk_file_name)
       
        try:
            
            os.makedirs(folder+dir_name)

        except OSError as e:
            
            if e.errno == os.errno.EEXIST:
                pass
            else:
                raise
        except Exception as e:
            pass

        try:

            
            with open(folder+disk_file_name, 'wb') as fd:
                fd.write(data)
            
        except Exception as e:
            pass
    zf.close()
    
def download(url,path):
      import requests
      path+="/" if path[-1]!="/" else ""
      local_filename = url.split('/')[-1]
      # NOTE the stream=True parameter
      r = requests.get(url, stream=True)
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=1024): 
              if chunk: # filter out keep-alive new chunks
                  f.write(path+chunk)
                  #f.flush() commented by recommendation from J.F.Sebastian
      return local_filename
def download2(url,path):
    from urllib2 import urlopen
    r = urlopen(url)
    f = open(path+url.split("/")[-1], "wb")
    f.write(r.read())
    # Cerrar ambos
    f.close()
    r.close()

def getRest(config): 
    import os
    
    url=decode(config.host[:-1]+os.environ['REQUEST_URI'])[len(config.base_url):].split("#")
    gato=None
    if len(url)==2:
        gato=url[1]
    url=url[0]

    cadena=""
    nurl=[]
    abre=None
    for i in url:

        if i=="/" and abre==None:
            nurl.append(cadena)    
            cadena=""
        elif i=="'" or i=='"' and abre==None:
            abre=i
            cadena+=i
        elif i==abre:
            abre=None
            cadena+=i
        else:
            cadena+=i
    else:
        nurl.append(cadena)
    url=nurl
    


    if "" in url:
        url.remove("")

    pos=["app","control","metodo","args","kwargs"]
    rest={"app":None,"control":None,"metodo":None,"args":[],"action":None,"kwargs":{},"manager":False,"request":{},"global_control":None,"#":None}
    
    def identificar(elem,rest,pos):
        
        if "=" not in elem and "{" not in elem and "}" not in elem:
            if len(pos)>0:
                if pos[0]=="app":

                    if elem in config.apps:
                        rest["app"]=normalizar(elem)
                        pos.remove("app")
                    elif elem==config.admin:
                        rest["app"]=config.default_app

                        rest["control"]="admin"

                        pos.remove("app")
                        pos.remove("control")
                    elif elem in config.controladores:

                        rest["global_control"]=normalizar(elem)

                        pos.remove("app")
                        


                    
                elif pos[0]=="control":
                    rest["control"]=normalizar(elem)
                    pos.remove("control")
                elif pos[0]=="metodo":
                    rest["metodo"]=normalizar(elem)
                    pos.remove("metodo")
                elif pos[0]=="args":
                    rest["args"].append(normalizar(elem))
                    
                elif pos[0]=="kwargs":
                    pos.remove("kwargs")
            
        elif "="  in elem:
            if len(pos)>0:
                if pos[0]=="app":
                    pos.remove("app")
                elif pos[0]=="control":
                    pos.remove("control")
                elif pos[0]=="metodo":
                    pos.remove("metodo")
                elif pos[0]=="args":
                    pos.remove("args")
                elif pos[0]=="kwargs":
                    pos.remove("kwargs")
            d={}
            for item in elem.split("&"):
                k,v=item.split("=")
                if k in list(d):
                    d[k].append(normalizar(v))
                    rest[k]=d[k]

                else:
                    d[k]=[normalizar(v)]
                    rest[k]=normalizar(v)
            
        elif "{" in elem and "}" in elem:

            if len(pos)>0:
                if pos[0]=="app":
                    pos.remove("app")
                elif pos[0]=="control":
                    pos.remove("control")
                elif pos[0]=="metodo":
                    pos.remove("metodo")
                elif pos[0]=="args":
                    pos.remove("args")
                else:    
                    pos.remove("kwargs")
                rest["kwargs"]=normalizar(elem)
    for elem in url:
        identificar(elem,rest,pos)
    if gato!=None:
        rest["#"]=gato
    if rest["manager"]==False and rest["global_control"]==None and rest["app"]==None:
        rest["app"]=rest["global_control"]
    return rest


def modificador(self,data,tabla,indice):
    boxes=[]
    c=0

    for k2,box in enumerate(self.obtenerFilas(tabla)[int(indice)][1]):
        for k,campo in enumerate(box):
                tmp=list(campo)
                tmp.remove("name") if "name" in tmp else tmp
                tmp.remove("value") if "value" in tmp else tmp
                tmp.remove("step") if "step" in tmp else tmp
                tmp.remove("opcion") if "opcion" in tmp else tmp
                tmp.remove("requerido") if "requerido" in tmp else tmp
                tmp.remove("tabla") if "tabla" in tmp else tmp
                tmp.remove("depende") if "depende" in tmp else tmp
                tmp.remove("categoria") if "captegoria" in tmp else tmp
                tmp.remove("descripcion") if "descripcion" in tmp else tmp
                tmp.remove("padre") if "padre" in tmp else tmp
                tmp.remove("opciones") if "opciones" in tmp else tmp
                
                tmp=tmp[0]
                
                if campo[tmp]=="text-titulo":
                    titulo=campo["value"]+" "+str(i+1)
                if campo[tmp]!="text-admin" and campo[tmp]!="img-admin" and campo[tmp]!="select-admin" :
                    indice=campo["name"]

                    
                    if "opcion" in campo:
                        
                        box[k]["value"]=int(data[indice].value)

                    elif campo[tmp]=="number":
                        
                        box[k]["value"]=int(data[indice].value)
                        
                    else:
                        box[k]["value"]=data[indice].value
                c+=1
        boxes.append(box)
    return boxes

def listar(data,config):
    
        
        data["listar"]=[]

        
        if "Modelos" in data:
            for modelo in data["Modelos"]:
                elem=data["model"][modelo].obtenerFilas(data["Tabla"])
                for k, elem2 in enumerate(elem):
                    elem[k][1]=[]
                data["listar"].extend(elem)
            
            if data["listar"]==None:
                data["listar"]=[]

        if "Modelos-plugin" in data:

            for modelo in data["Modelos-plugin"]:

                elem=data["plugins"][data["plugin"]].model[modelo].obtenerFilas(data["Tabla"])
                for k, elem2 in enumerate(elem):
                    elem[k][1]=[]
                data["listar"].extend(elem)
            
            if data["listar"]==None:
                data["listar"]=[]                
        
        data["vars"]["listar"]=data["listar"]
        data["ajax-data"]={"action":"listar","metodo":data["metodo"],"pag-action":None}
        data["vars"]["ajax-data"]=data["ajax-data"]

        data["baseAction"]=urlBuilder(config,data["app"],"admin","index",data["metodo"])
        data["vars"]["baseAction"]=data["baseAction"]

        data["titulo"]=decode(data["metodo"])
        data["vars"]["titulo"]=data["titulo"]

        
        
        data["filtrar"]=["Todas las fechas","Septiembre 2014"]
        data["vars"]["filtrar"]=data["filtrar"]
        data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}
        data["vars"]["acciones"]=data["acciones"]
        data["addNew"]="Añadir nuevo"
        data["vars"]["addNew"]=data["addNew"]
        data["n-pag"]=5
        data["vars"]["n-pag"]=data["n-pag"]
        data['status']=["Publicada"]
        data["vars"]["status"]=data["status"]
        dicstatus={}
        

        for elem in data['status']:
          try:

            if "filtrar" in dir(data["model"][modelos[data["metodo"]] if data["metodo"] in modelos else data["metodo"]]):

                filtrados=data["model"][modelos[data["metodo"]] if data["metodo"] in modelos else data["metodo"]].filtrar([elem],data["metodo"])

                dicstatus[elem]=data["model"][modelos[data["metodo"]] if data["metodo"] in modelos else data["metodo"]].obtenerIdsFiltrados(filtrados)
          except:
            filtrados=[]
            dicstatus={}


        data['filtros']=dicstatus
        data["vars"]["filtros"]=data["filtros"]


        data["keyNew"]=data["titulo"]
        data["vars"]["keyNew"]=data["keyNew"]
        data['campos']=["Nombre","Descripción"]
        data["vars"]["campos"]=data['campos']
        




def listarAjax(data,config):
    
        
        listar=[]
        for k,modelo in enumerate(data["Modelos"]):
            elem=data["model"][modelo].obtenerFilas(data["Tabla"])
            elem[k][1]=[]
            formato=data["model"][modelo].db(data["Tabla"]).obtenerFormato("Fecha")
            listar.append(elem)
        
        if listar==None:
            listar=[]

        
        titulo=data["metodo"]

        print "data={}"
        print 'data["listar"]='+str(listar)
        print 'data["ajax-data"]='+str({"action":"listar","args":data["metodo"],"pag-action":None})
        print 'data["baseAction"]="'+urlBuilder(config,data["app"],"admin","index",args=data["metodo"])+'"'
        print 'data["titulo"]="'+str(data["metodo"])+'"'
        print 'data["filtrar"]='+str(["Todas las fechas","Septiembre 2014"])
        print 'data["addNew"]='+"'Añadir nuevo'"
        print 'data["n-pag"]='+str(5)
        print "data['campos']="+str(["Titulo","Fecha"])
        print "data['app']='"+data["app"]+"'"
        print "data['vista']='"+"index"+"'"
        print 'data["beforeAction"]="'+data["action"]+'"'
        print 'data["action"]="'+data["action"]+'"'
        print 'data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}'
        if titulo=="Paginas":
          pass
        elif titulo=="Entradas":
          pass
        elif titulo=="Menus":
          pass
        elif titulo=="Portafolio":
          pass
        elif titulo=="Usuarios":
          pass
        elif titulo=="Plugins":
          print "data['campos']="+str(["Plugin","Descripción"])
        elif titulo=="Negocios" or titulo=="Archivos":

          status=["Publicada"]
          dicstatus={}

          for elem in status:
            
            filtrados=data["model"]["main"].ordenar(filtros=[elem])

            dicstatus[elem]=data["model"]["main"].obtenerIdsFiltrados(filtrados)

          print "data['filtros']="+str(dicstatus)
        else:
          print "data['campos']="+str(["Titulo","Fecha"])
    


class Headers:
    def __init__(self):
        self._HEADERS_={}
        self._HEADERS_["Content-type"]="text/html"
        self._RETURNHEADERS_=False 
    def set_headers(self,cabeceras):
        self._HEADERS_.update(cabeceras)

    def show(self,cabeceras={}):
        if self._RETURNHEADERS_==False:
            self._RETURNHEADERS_=True
            self._HEADERS_.update(cabeceras)
            l=[]
            for elem in self._HEADERS_:
              if "content-type"!=elem.lower():
                l.insert(0,elem)
              else:
                l.append(elem)
            for elem in l:
              print elem+": "+self._HEADERS_[elem]+"\n"

def formatear_rb(html,codigo):
    if html!=None:
        html=html.replace('"',"'")
    return 'puts """'+(html if html!=None else "")+'"""\n'+(codigo if codigo!=None else "")+"\n"


def formatear_pl(html,codigo):
    if html!=None:
        html=html.replace('"',"'")

    return 'print "'+(html if html!=None else "")+'";\n'+(codigo if codigo!=None else "")+"\n"


def downloader(config,ruta,folder="../download/",get=True):
    import os,zu
    for elem in os.listdir(folder):
        (mode2, ino2, dev2, nlink2, uid2, gid2, size2, atime2, mtime2, ctime2) = os.stat(folder+elem)
        if mtime2>1509822411*24:
            os.remove(folder+elem)
    
    with open(ruta,"r") as doc:
        archivo=doc.read()
    token=zu.randomString()
    while token in os.listdir(folder):
        token=zu.randomString()
    os.mkdir(folder+token,0755)

    with open(folder+token+"/"+ruta.split("/")[-1],"w") as f2:
        f2.write(archivo)
    
    
    if get==True:
        
        print"<html>"
        print "Descarga iniciada"
        print "<iframe src='"+config.asenzor_host+config.folder_donwloads+token+"/"+ruta.split("/")[-1]+"' style='display:none' onload='window.close()'></iframe>"
        
        
        print"</html>"
    else:
        print config.asenzor_host+config.folder_donwloads+token+"/"+ruta.split("/")[-1]
    


def gringolizar(vista,espacio="_"):
    l=["n","a","e","i","o","u","A","E","I","O","U","a","e","i","o","u","A","E","I","O","U"]
    vista=vista.replace(" ",espacio)
    for k,elem in enumerate(["ñ","á","é","í","ó","ú","Á","É","Í","Ó","Í","ä","ë","ï","ö","ü","Ä","Ë","Ï","Ö","Ü"]):
        vista=vista.replace(elem,l[k])
    return vista


def sufijar(archivo,sufijo="_540x540"):
    return archivo[:archivo.rfind(".")]+sufijo+archivo[archivo.rfind("."):]

def js_data(datos):
    '''
    print """function js_data(){

    }
    """
    for elem in datos:
        print 'js_data.prototype.'+elem+"="+str("`{}`".format(datos[elem]) if type(datos[elem])==str else datos[elem])+";"
    print "var js_data=new js_data();"
    '''
    print "var js_data="+str(datos)