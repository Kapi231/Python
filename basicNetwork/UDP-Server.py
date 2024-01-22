import socket

server_ip = "0.0.0.0"
bind_port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((server_ip, bind_port))
print(f"[*] server run on {server_ip}:{bind_port}")

while 1:
    
    #message sending
    data, addr = server.recvfrom(1024)
    print(f"[*] user: {data.decode()}")
    