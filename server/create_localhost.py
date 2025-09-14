import socket
import threading

HOST = "127.0.0.1"
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []


def broadcast(msg, client_sender):
    for client in clients:
        if clients != client_sender:
            client.send(msg)
    
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def initialize():
    print(f"[SERVER] Listening on {HOST}:{PORT}")
    print("Write /exit to close server")
    while True:
        client, addr = server.accept()
        print("[SERVER] New connection: {addr} connected")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

initialize()