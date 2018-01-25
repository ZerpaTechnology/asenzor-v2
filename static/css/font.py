c=0
cd=""
while c<100:
	cd+="""
	@media (max-width: 360px){
	  .pad-t"""+str(c)+"""-xs {
	    padding-top: """+str(c)+"""0px !important; } }
	
	@media (max-width: 360px){
	  .pad-r"""+str(c)+"""-xs {
	    padding-right: """+str(c)+"""0px !important; } }
	@media (max-width: 360px){
	  .pad-b"""+str(c)+"""-xs {
	    padding-bottom: """+str(c)+"""0px !important; } }
	@media (max-width: 360px){
	  .pad-"""+str(c)+"""-xs {
	    padding: """+str(c)+"""0px !important; } }
	"""
	c+=1
f=open("f","w")
f.write(cd)
f.close()