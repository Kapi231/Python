import socket

target_ip = "0.0.0.0"
target_port = 9998

TCP_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCP_client.connect((target_ip, target_port))

TCP_client.send(b"Hello World")

response = TCP_client.recv(4096)
print(response.decode('UTF-8'))

TCP_client.close()
