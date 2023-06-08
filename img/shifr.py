import hashlib

# Шифрование строк
h1 = hashlib.md5(b'I love Python')
print(h1.hexdigest())


h2 = input()
print(hashlib.md5(h2.encode()).hexdigest())

р3 =