import socket
import sys
from multiprocessing import Process

server_ip = "127.0.0.1"
server_port = 9998
server_admin = "admin" # username privilaged to close server (line 21)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    server.bind((server_ip, server_port))
    print(f"[*] server on {server_ip}:{server_port}")

def message_maintainer():
    # receive packets from users
    data, (addr, port) = server.recvfrom(4096)
    print(f"[*] packet from {addr}:{port} :: {data.decode()}")
    
    #checks if command is send from privilaged user, not good security...
    if data.decode() == f"{server_admin}: ?exit" and addr == server_ip:
        server.sendto(b'[*] Closing server\n[*] Disconnecting...', (addr, port))
        server.close()
        sys.exit()
 
    else:
        # send text back
        server.sendto(data, (addr, port))

def procceses():
    p1 = Process(target=message_maintainer())

    p1.start()

if __name__ == '__main__':
    main() 

    while 1:
        procceses()
