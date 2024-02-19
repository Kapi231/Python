import socket, sys

ip = "127.0.0.1"
port = 9998

username = input("[*] how other users should call you? \n   --> ")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((ip, port))

if username != "" and len(username) >= 4:
    print(f"[*] Hi {username}")
    pass

else:
    print("[*] invalid username!")
    sys.exit()

while 1:

    # send message to server
    text = input(">>> ")

    if text == "/exit":
        sys.exit()

    # receive messages form server
    client.send(f"{username}: {text}".encode())
    mess, addr = client.recvfrom(4096)
    print(mess.decode())
