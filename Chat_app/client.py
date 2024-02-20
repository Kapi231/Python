import socket, sys

print("<==========CHAT APP==========>\n")
help = " ? - admin command\n / - user command\n ?shutdown - close server\n /exit - exit app"
print(help)

server_addr = ("127.0.0.1", 9998)

username = input("\n[*] how other users should call you? \n   --> ")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if username != "" and len(username) >= 4:
    print(f"[*] Hi {username}")
    pass

else:
    print("[*] invalid username!")
    sys.exit()

def switch(command):

    if command == "/help":
        print(help)

    elif command == "/exit":
        print("[*] Closing app")
        sys.exit()

    else:
        pass

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
