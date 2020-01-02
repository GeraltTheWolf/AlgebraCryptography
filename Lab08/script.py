# from Cryptodome.PublicKey import ECC
# from Cryptodome.Hash import SHA256
# from Cryptodome.Signature import DSS
#
# key = ECC.generate(curve='P-256')
#
# f = open('myprivatekey.pem','wt')
# f.write(key.export_key(format='PEM'))
# f.close()
#
# f = open('myprivatekey.pem','rt')
# key = ECC.import_key(f.read())
#
#
# message = b'I give my permission to order #4355'
# prvkey = ECC.import_key(open('myprivatekey.pem').read())
# h = SHA256.new(message)
# signer = DSS.new(prvkey, 'fips-186-3')
# signature = signer.sign(h)
#
#
# key = ECC.import_key(open('pubkey.der').read())
# h = SHA256.new(message)
# verifier = DSS.new(key, 'fips-186-3')
# try:
#     verifier.verify(h, signature)
#     print("The message is authentic.")
# except ValueError:
#     print("The message is not authentic.")

from Cryptodome.PublicKey import DSA
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256
from Helper import *

# Generate Public-Private Key Pair

# https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html


file = helper_read_file("C:/Users/irezek/Desktop/Images/text.txt")

# Create a new DSA key
key = DSA.generate(2048)

f = open("public_key.pem", "w")
f.write(str(key.publickey().export_key()).encode("utf-8"))
f.close()

# Sign a message
message = file
hash_obj = SHA256.new(message)
signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)

# Load the public key
f = open("public_key.pem", "r")
hash_obj = SHA256.new(message)
pub_key = DSA.import_key(bytes(f.read().encode("utf-8")))
verifier = DSS.new(pub_key, 'fips-186-3')

# Verify the authenticity of the message
try:
    verifier.verify(hash_obj, signature)
    print
    "The message is authentic."
except ValueError:
    print
    "The message is not authentic."
