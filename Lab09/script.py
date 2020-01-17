import sys
import random

sys.path.append("..")
from HelperCrypto import *
from Cryptodome.Cipher import AES

key = generate_key_pair()
iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

aes = AES.new(key, AES.MODE_CBC, iv)
data = 'hello world 1234' # <- 16 bytes
encd = aes.encrypt(data)



aes = AES.new(key.publickey(), AES.MODE_CBC, iv)
decd = aes.decrypt(encd)
print(decd)