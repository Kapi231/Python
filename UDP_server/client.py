import socket

target_ip = "0.0.0.0"
target_port = 9998

UDP_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
        
    send_message = input(">>> ")

    if send_message == "exit":
        UDP_client.close()
        break

    else:
        UDP_client.sendto(send_message.encode(), (target_ip, target_port))
