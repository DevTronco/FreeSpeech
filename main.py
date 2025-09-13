import os 
import sys
import platform

setup_path = os.path.join(os.path.dirname(__file__), "setup")
sys.path.append(setup_path)

from setup import setup_app

def cls_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear") 


setup_app.setup.pip_checker()
setup_app.setup.modules_installer()
cls_console()

print("Welcome to FreeSpeech!")
print("Made with love by Tronco. https://github.com/DevTronco")
print("Digit 'help' to see commands")

while True:
    user_cmd = input("CMD>> ").strip().lower()

    if user_cmd.lower() == "help":
        print("""
        -help: you just did it
        -version: shows FreeSpeech current version
        -join <invite_link>: joins server from invite link  
        -leave: leaves the server
        -cls: clears the console
        -create: goes to server creation menu
        -close: closes own server
        -exit: closes FreeSpeech 
        """)
        continue
    elif user_cmd.lower() == "cls":
        cls_console()
        continue
    elif user_cmd.lower() == "exit":
        sys.exit()
        break
    elif user_cmd.lower() == "version":
        print("FreeSpeech version: beta 0.0.1.")
    else:
        print("Command not found.")
        continue
 
