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
