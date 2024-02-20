import getpass, os, socket, sys, time
from threading import Thread

def log_request():
    #requesting chat log to have live chat
    while 1:
        try:
            time.sleep(3)
            client.sendto("<data_request>".encode(), server_addr)
            log, addr = client.recvfrom(4096)
            os.system("cls")
            print(log.decode())

        except:
            print("[*] Lost connection with server")
            break

def switch(command):

    if command == "/exit":
        print("[*] Closing app")
        sys.exit()

    else:
        pass  

def main():
    # send message to server
    text = getpass.getpass("")
    if text == "/exit":
        sys.exit()

    os.system("cls")

    try:
        client.sendto(f"{username}: {text}".encode(), server_addr)
        mess, addr = client.recvfrom(4096)
        print(mess.decode())
        
    except:
        print("[*] Can't send/recive package, server is down")
        sys.exit()

if __name__ == '__main__':

    print("<==========CHAT APP==========>\n")
    print(" ? - admin command\n / - user command\n ?shutdown - close server\n /exit - exit app")
    getpass.getpass("\n[*] Press any key to continue")

    server_addr = ("127.0.0.1", 9998)

    username = input("\n[*] how other users should call you? \n   --> ")
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if username != "" and len(username) >= 4:
        print(f"[*] Hi {username}")
        pass

    else:
        print("[*] invalid username!")
        sys.exit()

    log_thread = Thread(target=log_request)
    log_thread.daemon = True
    log_thread.start()

    while 1:
        main()
