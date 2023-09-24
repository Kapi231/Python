
import hashlib

targetHash = "1234"
hashReady = bytes(targetHash.encode('utf-8'))
h = hashlib.sha256(hashReady).hexdigest()

file = open("passToHash.txt", "r")

for line in file.readlines():
    h2 = hashlib.sha256(b"1234").hexdigest()
    if h == h2:
        print("yay")
    else:
        pass