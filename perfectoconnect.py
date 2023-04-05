import os
import sys
import perfecto_token_provider

if len(sys.argv) < 2:
    print("No cloud name provided. Exiting")
    sys.exit(0)

domain = ".perfectomobile.com"
if sys.argv[1].endswith(domain):
    cloud = sys.argv[1].replace(domain, "")
    hostname = sys.argv[1]
else:
    hostname = sys.argv[1] + domain
    cloud = sys.argv[1]

pConnectDownloadUrl = "https://downloads.connect.perfectomobile.com/clients/Perfecto-Connect-windows64.zip"
pConnectDownloadUrlMac = "https://downloads.connect.perfectomobile.com/clients/Perfecto-Connect-mac.tar"

executable_name = "perfectoconnect"
if sys.platform.startswith("Windows"):
    executable_name = "perfectoconnect64.exe"

perfecto_connect_bin = os.environ.get("PERFECTOCONNECT_BIN")
if perfecto_connect_bin is None:
    perfecto_connect_bin = executable_name

hostname = cloud if cloud.endswith(".perfectomobile.com") else cloud + ".perfectomobile.com"
token = perfecto_token_provider.perfecto_token_provider.get_token_for_cloud(cloud)
if token is None:
    print("Found token for %s" % cloud)
    sys.exit(0)

command = "%s start -c %s -s %s -v" % (executable_name, hostname, token)
if len(sys.argv) == 3 and sys.argv[2] == 'doctor':
    command = "%s doctor -c %s -s %s -v" % (executable_name, hostname, token)

print("Executing %s " % command)

os.system(command)
