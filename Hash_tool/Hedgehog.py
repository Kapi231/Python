
import hashlib

h = hashlib.sha256(b'Hello').hexdigest()

print(h)
