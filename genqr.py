import json
import os
from getpass import getpass
from colorama import Fore, Back, Style
import pyqrcode



try:
    passphrase_file = open("./config.json")
except FileNotFoundError:
    print(Fore.RED + "Error: No config.json file found." + Style.RESET_ALL + "\nPlease make a config.json file in this directory.\n"+Style.RESET_ALL+"Check github for an example.")
    exit()
pass_json = json.load(passphrase_file)
passphrase = pass_json["preshared_passphrase"]
host = pass_json["host_ip_or_domain_with_optional_port"]
background = "black" if pass_json["invertBG"] else "white"
foreground = "white" if pass_json["invertFG"] else "black"

if(passphrase == "" or host == ""):
   print("ServerPassphrase/host cannot be empty! Exiting.")
   passphrase_file.close()
   exit()

http_str = ""
if(pass_json["use_https"]):
    http_str = "https"
else:
    http_str = "http"

print(Fore.RED + Style.BRIGHT + '\n\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.' + Style.RESET_ALL)

print(Fore.CYAN + Style.BRIGHT + "\n\n   _____ _____ __  __ _____  _      ______ _______ _  _________") 
print("  / ____|_   _|  \/  |  __ \| |    |  ____|__   __| |/ /__   __|")
print(" | (___   | | | \  / | |__) | |    | |__     | |  | ' /   | |   ")
print("  \___ \  | | | |\/| |  ___/| |    |  __|    | |  |  <    | |   ")
print("  ____) |_| |_| |  | | |    | |____| |____   | |  | . \   | |   ")
print(" |_____/|_____|_|  |_|_|    |______|______|  |_|  |_|\_\  |_|   \n\n" + Style.RESET_ALL)

print("By" + Fore.BLUE + " Aaryan D. MITB (2021-25)" + Style.RESET_ALL)
print("Support - " + Fore.BLUE + "Discord:" + Fore.CYAN +  " @ribcatcher" + Style.RESET_ALL)
print("For help type '?'\n")
def clean():
    # For Windows
    if os.name == 'nt':
        os.system('cls')


    # For macOS and Linux
    else:
        os.system('clear')

                                                                
def getToken():
    cpass = getpass("Enter the passphrase: ")
    if(cpass != CLILock):
        print(Fore.RED + "Invalid passphrase!" + Style.RESET_ALL)
        return
    clean()
    slugdata = "returnedbyapi"

    slugstring = f"{http_str}://{host}/book/{slugdata}"

    qr = pyqrcode.create(slugstring)
    if((not pass_json["invertFG"]) and (not pass_json["invertBG"])):
        print(qr.terminal())
    else:
        print(qr.terminal(module_color=foreground, background=background))
    print(Style.BRIGHT + Fore.BLUE + f"Link: {slugstring}" + Style.RESET_ALL)

CLILock = ""
while(CLILock == ""):
    CLILock = getpass("Enter a passphrase to secure gqr: ")
    print(Style.RESET_ALL + " ")
    if(CLILock == ""):
        print(Fore.RED + "Phrase cannot be empty" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Set successfully" + Style.RESET_ALL)
    


while(True):
    print("\n"+ Fore.GREEN +"[COMMAND]: " + Style.RESET_ALL, end="")
    cmd = input()
    if(cmd == "gqr"):
        getToken()
    elif(cmd == "clear"):
        clean()
    elif(cmd == "exit"):
        clean()
        passphrase_file.close()
        exit()
    elif(cmd == "help" or cmd == "?"):
        print("\nCOMMANDS:\n1. gqr - generates a QR to claim a ticket\n2. clear - clear the screen\n3. exit - closes and exits\n3. help - displays this message")
    else:
        print(Fore.RED + "Invalid command! Type 'help' or '?' for a command list" + Style.RESET_ALL)




