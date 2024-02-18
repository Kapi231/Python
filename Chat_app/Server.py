import socket
import sys
#from multiprocessing import Process

server_ip = "127.0.0.1"
server_port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((server_ip, server_port))
print(f"[*] server on {server_ip}:{server_port}")

def message_maintainer():
    # receive packets from users
    data, addr = server.recvfrom(4096)
    print(f"[*] packet from {addr} :: {data.decode()}")

    # send text back
    server.connect(addr)
    server.send(data)

while 1:

    message_maintainer()
    #p1 = Process(target=message_maintainer())

    #p1.start()
    #p1.join()
