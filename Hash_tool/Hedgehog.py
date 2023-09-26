
import hashlib

i = input("Hash: ")

# Main function is working but i need to give it a way to chose what type of hash it is.
with open("passwordList.txt", "r") as file:
    for line in file.readlines():
        word = line.split()
        h = hashlib.sha256(word[0].encode('utf-8')).hexdigest()
        print(h)
        if h == i:
            print(f"Password: {line}")
            break
        else:
            pass
