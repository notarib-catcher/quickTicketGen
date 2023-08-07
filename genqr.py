import json
import pyqrcode



passphrase_file = open("./config.json")
pass_json = json.load(passphrase_file)
passphrase = pass_json["preshared_passphrase"]
host = pass_json["host_ip_or_domain_with_optional_port"]
background = "black" if pass_json["invertBG"] else "white"
foreground = "white" if pass_json["invertFG"] else "black"

if(passphrase == "" or host == ""):
   print("Passphrase/host cannot be empty! Exiting.")
   passphrase_file.close()
   exit()

http_str = ""
if(pass_json["use_https"]):
    http_str = "https"
else:
    http_str = "http"



#get the qr code data here
slugdata = "returnedbyapi"

slugstring = f"{http_str}://{host}/book/{slugdata}"

qr = pyqrcode.create(slugstring)
if((not pass_json["invertFG"]) and (not pass_json["invertBG"])):
    print(qr.terminal())
else:
    print(qr.terminal(module_color=foreground, background=background))
