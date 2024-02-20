import socket, sys

server_addr = ("127.0.0.1", 9998)

username = input("[*] how other users should call you? \n   --> ")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if username != "" and len(username) >= 4:
    print(f"[*] Hi {username}")
    pass

else:
    print("[*] invalid username!")
    sys.exit()

def sending_and_reciving():
    # send message to server
    text = input(">>> ")

    if text == "/exit":
        sys.exit()

    try:
        client.sendto(f"{username}: {text}".encode(), server_addr)
        mess, addr = client.recvfrom(4096)
        print(mess.decode())
    
    except:
        print("[*] Can't send/recive package, server is down")
        sys.exit()

while 1:
    sending_and_reciving()
