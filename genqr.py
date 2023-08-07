import json
from colorama import Fore, Back, Style
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
print("****************************************************************\n\n")
print("   _____ _____ __  __ _____  _      ______ _______ _  _________") 
print("  / ____|_   _|  \/  |  __ \| |    |  ____|__   __| |/ /__   __|")
print(" | (___   | | | \  / | |__) | |    | |__     | |  | ' /   | |   ")
print("  \___ \  | | | |\/| |  ___/| |    |  __|    | |  |  <    | |   ")
print("  ____) |_| |_| |  | | |    | |____| |____   | |  | . \   | |   ")
print(" |_____/|_____|_|  |_|_|    |______|______|  |_|  |_|\_\  |_|   \n\n")
print("****************************************************************\n\n")
print("By Aaryan D. MITB (2021-25)")
print("Help and support - Discord: @ribcatcher\n")
                                                                
def getToken():
    slugdata = "returnedbyapi"

    slugstring = f"{http_str}://{host}/book/{slugdata}"

    qr = pyqrcode.create(slugstring)
    if((not pass_json["invertFG"]) and (not pass_json["invertBG"])):
        print(qr.terminal())
    else:
        print(qr.terminal(module_color=foreground, background=background))
    print(Style.BRIGHT + Fore.BLUE + f"Link: {slugstring}" + Style.RESET_ALL)

while(True):
    print("\n"+ Fore.GREEN +"[COMMAND]: " + Style.RESET_ALL, end="")
    cmd = input()
    if(cmd == "gqr"):
        getToken()
    elif(cmd == "exit"):
        passphrase_file.close()
        exit()
    elif(cmd == "help" or cmd == "?"):
        print("\nCOMMANDS:\n1. gqr - generates a QR to claim a ticket\n2. exit - closes and exits\n3. help - displays this message")
    else:
        print(Fore.RED + "Invalid command! Type 'help' or '?' for a command list" + Style.RESET_ALL)




