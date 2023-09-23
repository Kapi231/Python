
import hashlib

h = hashlib.sha256(b'Hello').hexdigest()

print(h)

if h == 'Hello':
    print('Yes')
else:
    print('No')
