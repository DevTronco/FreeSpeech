import os 
import sys
import platform

server_path = os.path.join(os.path.dirname(__file__), "server")
sys.path.append(server_path)


from server import create_localhost, connect_client

def cls_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear") 

print("Welcome to FreeSpeech!")
print("Made with love by Tronco. https://github.com/DevTronco")
print("Digit 'help' to see commands")

while True:
    user_cmd = input("CMD>> ").strip().lower()

    if user_cmd.lower() == "help":
        print("""
        -help: you just did it
        -version: shows FreeSpeech current version
        -join: joins server from invite link  
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
    elif user_cmd.lower() == "create":
        cls_console()
        create_localhost.initialize()
    elif user_cmd.lower() == "join":
        link = str(input("enter here the invite link (example: freespeech/server/very_good_server): "))
        connect_client(link)

    else:
        print("Command not found.")
        continue