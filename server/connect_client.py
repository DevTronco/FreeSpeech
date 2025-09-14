import socket
import threading
import random
import create_localhost

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print("\n" + message)
        except:
            print("Connessione chiusa.")
            client.close()
            break

def send():
    while True:
        message = input()
        client.send(message.encode('utf-8'))

def connect_through_link(link):
    PORT = random.randint(50000, 65535)

    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((link, create_localhost.PORT))

    recv_thread = threading.Thread(target=receive)
    recv_thread.start()

    send_thread = threading.Thread(target=send)
    send_thread.start()

connect_through_link(create_localhost.HOST)