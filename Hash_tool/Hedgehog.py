
import hashlib

i = input()

with open("passToHash", "r") as file:
    for line in file.readlines():
        h = hashlib.sha256(line.encode('utf-8')).hexdigest()
        if h == i:
            print(f"the right password: {line}")
            break
        else:
            print("0")

# So i finnaly know what the problem is :))))
# when function reads text files instead of passing it one by one, it mashes everything together
#
# I want this:
# "kapi"
# "ja"
# "ty"
#
# But it do this instead:
# "kapijaty"