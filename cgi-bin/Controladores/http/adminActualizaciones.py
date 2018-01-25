
if p["action"]=="update":
  import requests
  req=requests.get("zerpatechnology.com.ve/update/notifications")
  if req.text!=config.version:
    zred.download("zerpatechnology.com.ve/update/download/"+req.text,"../update")

  