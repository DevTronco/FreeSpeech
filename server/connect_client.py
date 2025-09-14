import socket
import threading

HOST = '127.0.0.1'
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

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

#thread start
recv_thread = threading.Thread(target=receive)
recv_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()