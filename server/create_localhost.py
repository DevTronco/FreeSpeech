import socket
import threading
import psutil

def get_ip():
    for iface, addrs in psutil.net_if_addrs().items():
        if "zerotier" in iface.lower():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip = addr.address
                    if (ip.startswith("10.") or
                        ip.startswith("192.168.") or
                        (ip.startswith("172.") and 16 <= int(ip.split('.')[1]) <= 31)):
                        return ip
    raise RuntimeError("ZeroTier IP not found.")

HOST = get_ip()
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def generate_link():
    print(f"Link: freespeech://{HOST}:{PORT}")

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