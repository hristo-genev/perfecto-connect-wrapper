import os
import sys
import json

if len(sys.argv) < 2:
  print ("No cloud name provided. Exiting")
  sys.exit(0)

cloud = sys.argv[1]
hostname = cloud if cloud.endswith(".perfectomobile.com") else cloud + ".perfectomobile.com"
authFilePath = os.getenv("TOKEN_STORAGE")
if authFilePath is None:
  print ("Missing TOKEN_STORAGE variable pointing to the location of the tokens file")
  sys.exit(0)
  
token = ""
pConnectDownloadUrl = "https://downloads.connect.perfectomobile.com/clients/Perfecto-Connect-windows64.zip"

try:
  token = json.load(open(authFilePath))["tokens"][cloud]       
  print ("Found token for %s" % cloud)
except KeyError as er:
  print ("Token not found for %s" % cloud)
  sys.exit(0)
except Exception:
  print (sys.exc_info())
  sys.exit(0)
  
command = "perfectoconnect64.exe start -c %s -s %s -v" % (hostname, token)
print ("Executting %s " % command)

os.system(command)