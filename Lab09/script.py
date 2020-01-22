import sys;
import os
import fnmatch

sys.path.append("..")
from HelperCrypto import *
from Hashing import get_file_hash
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.Random import get_random_bytes


# Samples that where used to produce this code:
# https://pycryptodome.readthedocs.io/en/latest/src/examples.html
# https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/

SINGLE_FILE = 0
ALL_FILES = 1
ALL_FILES_RECURSIVE = 2
AUTOMATE = False

MENU_OPTIONS = [
    ["Single file supplied in the command-line", "All the files in the folder", "All the files in all the sub-folders"],
    [SINGLE_FILE, ALL_FILES, ALL_FILES_RECURSIVE]]


def encrypt_file(file_path_to_encrypt):
    try:
        # Read original file as bytes
        input_file = helper_read_file(file_path_to_encrypt, as_bytes=True)

        # Generate Session key - Each time session key is different
        session_key = get_random_bytes(16)  # Use a stored / generated random_bytes
        cipher_rsa = PKCS1_OAEP.new(import_public_key_rsa(PUBLIC_KEY_FILE_NAME))

        # *************** BEGIN encryption ***************
        # Encrypt session key with public key
        encrypted_session_key = cipher_rsa.encrypt(session_key)
        output_file = open(file_path_to_encrypt + '.encrypted', 'wb')

        # Create the cipher object and encrypt the data
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        cipher_text, tag = cipher_aes.encrypt_and_digest(input_file)
        [output_file.write(x) for x in (encrypted_session_key, cipher_aes.nonce, tag, cipher_text)]
        # *************** END encryption ***************

        output_file.close()
    except:
        print("Something went wrong during encryption phase")


def decrypt_file(file_path_to_decrypt):

    try:
        # Import private key and build cipher object
        private_key = import_private_key_rsa(PRIVATE_KEY_FILE_NAME)
        cipher_rsa = PKCS1_OAEP.new(private_key)

        # *************** BEGIN Decryption ***************
        # Decrypt the session key with the private RSA key
        input_file = open(file_path_to_decrypt + '.encrypted', "rb")
        enc_session_key, nonce, tag, cipher_text = [input_file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(cipher_text, tag)
        # *************** END Decryption ***************

        # Save decrypted file
        output_file = open(file_path_to_decrypt + '.decrypted', 'wb')
        output_file.write(data)
    except:
        print("Something went wrong during decryption phase")


def encrypt_decrypt_all_files(folder_path_to_sign):
    result = helper_get_file_names_in_directory(folder_path_to_sign)
    print("\r\n------------- FOLDER " + os.path.basename(result[1]) + "-------------")
    for file in result[0]:
        try:
            encrypt_file(file)
            decrypt_file(file)
        except:
            print("Failed to read file" + file)
    print("\r\n--------------------- " + result[1] + " --------------------------")


def encrypt_decrypt_all_files_recursively(folder_path_to_sign):
    encrypt_decrypt_all_files(folder_path_to_sign)
    for folder in listdir(folder_path_to_sign):
        print(folder_path_to_sign + '/' + folder)
        if isdir(folder_path_to_sign + '/' + folder):
            encrypt_decrypt_all_files_recursively(folder_path_to_sign + '/' + folder)


print("Generating key pair....\r\n")
if os.path.isfile(PUBLIC_KEY_FILE_NAME) and os.path.isfile(PRIVATE_KEY_FILE_NAME):
    print("Generating key pair.... Skipped!")
    print("Key pair already exist!\r\n")
else:
    key_pair = generate_key_pair_rsa()
    print("Generating key pair.... Done!\r\n")


helper_display_menu_(MENU_OPTIONS[0])
menu_choice = helper_get_menu_selection(len(MENU_OPTIONS[0]), MENU_MAIN)


if menu_choice == SINGLE_FILE:
    file_path = input("Enter FILE path:   ")
    if not isfile(file_path):
        file_path = DUMMY_FILE_PATH
    encrypt_file(file_path)
    decrypt_file(file_path)
else:
    folder_path = input("Enter FOLDER path:   ")
    if not isdir(folder_path):
        folder_path = DUMMY_FOLDER_PATH
    if menu_choice == ALL_FILES:
        encrypt_decrypt_all_files(folder_path)
    elif menu_choice == ALL_FILES_RECURSIVE:
        encrypt_decrypt_all_files_recursively(folder_path)

# assert get_file_hash("my_file.txt") == get_file_hash("my_file.txt" + '.decrypted'), 'Files are not identical'

input("Press any key to delete files that were created")

# Get a list of all files in directory
for rootDir, subdirs, filenames in os.walk(DUMMY_FOLDER_PATH):
    # Find the files that matches the given patterm
    for filename in fnmatch.filter(filenames, '*.encrypted'):
        try:
            os.remove(os.path.join(rootDir, filename))
        except OSError:
            print("Error while deleting encrypted file")
    for filename in fnmatch.filter(filenames, '*.decrypted'):
        try:
            os.remove(os.path.join(rootDir, filename))
        except OSError:
            print("Error while deleting decrypted file")

