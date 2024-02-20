import socket
import sys
from multiprocessing import Process

def main():
    # receive packets from users
    data, (addr, port) = server.recvfrom(4096)
    print(f"[*] packet from {addr}:{port} :: {data.decode()}")
    
    #checks if command is send from privilaged user, not good security...
    if data.decode() == f"{server_admin}: ?shutdown" and addr == server_ip:
        server.sendto(b'[*] Closing server\n[*] Disconnecting...', (addr, port))
        server.close()
        sys.exit()
 
    else:
        # send text back
        server.sendto(data, (addr, port))

if __name__ == '__main__':

    print("<==========CHAT APP SEVER==========>\n")

    server_ip = "127.0.0.1"
    server_port = 9998
    server_admin = "admin" # username privilaged to close server (line 21)

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((server_ip, server_port))
    print(f"[*] server on {server_ip}:{server_port}")    

    while 1:
        main()
