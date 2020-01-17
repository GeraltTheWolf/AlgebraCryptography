import sys

sys.path.append("..")
from Helper import *
from Cryptodome.PublicKey import DSA
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA256

PUBLIC_KEY_FILE_NAME = "public_key.pem"
PRIVATE_KEY_FILE_NAME = "private_key.pem"
PASSPHRASE = "vegetables"


def generate_key_pair():
    dsa_key_pair = DSA.generate(2048)
    f = open(PUBLIC_KEY_FILE_NAME, "wb")
    f.write(dsa_key_pair.publickey().export_key())
    f.close()
    f2 = open(PRIVATE_KEY_FILE_NAME, "wb")
    f2.write(dsa_key_pair.export_key(format="PEM", pkcs8=True, passphrase=PASSPHRASE))
    f2.close()
    return dsa_key_pair


def import_public_key(public_key_file_path):
    f = open(public_key_file_path, "r")
    return DSA.import_key(f.read())


def import_private_key(private_key_file_path):
    f = open(private_key_file_path, "r")
    return DSA.import_key(f.read(), passphrase=PASSPHRASE)


def generate_signature(file_to_sign, key):
    hash_obj = SHA256.new(file_to_sign)
    signer = DSS.new(key, 'fips-186-3')
    return signer.sign(hash_obj)


def verify_signature(file_path_to_verify, signature):
    public_key = import_public_key(PUBLIC_KEY_FILE_NAME)
    file_to_verify = helper_read_file(file_path_to_verify, True)
    hash_obj = SHA256.new(file_to_verify)
    verifier = DSS.new(public_key, 'fips-186-3')
    # Verify the authenticity of the message
    try:
        verifier.verify(hash_obj, signature)
        print("The file is authentic.")
    except ValueError:
        print("The file is not authentic.")