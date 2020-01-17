import sys

sys.path.append("..")
from HelperCrypto import *

# Steps:
# 1. Generate Public-Private Key Pair
# 2. Save Keys to a File (simulate sharing of public key)
# 3. Read file
# 4. Create signature
# 5. Validate signature
# https://pycryptodome.readthedocs.io/en/latest/src/public_key/dsa.html


SINGLE_FILE = 0
ALL_FILES = 1
ALL_FILES_RECURSIVE = 2
AUTOMATE = False

MENU_OPTIONS = [
    ["Single file supplied in the command-line", "All the files in the folder", "All the files in all the subfolders"],
    [SINGLE_FILE, ALL_FILES, ALL_FILES_RECURSIVE]]


def sign_single_file(file_path_to_sign):
    private_key = import_private_key(PRIVATE_KEY_FILE_NAME)
    file_to_sign = helper_read_file(file_path_to_sign, True)
    signature = generate_signature(file_to_sign, private_key)
    print("\r\nSignature for: " + os.path.basename(file_path_to_sign))
    print(signature)
    if not AUTOMATE:
        input("\r\nIf you want to mod the file now is the time! Press enter when done.\r\n")
    verify_signature(file_path_to_sign, signature)
    return signature


def sign_all_files(folder_path_to_sign):
    result = helper_get_file_names_in_directory(folder_path_to_sign)
    print("\r\n------------- FOLDER " + os.path.basename(result[1]) + "-------------")
    for file in result[0]:
        try:
            sign_single_file(file)
        except:
            print("Failed to read file" + file)
    print("\r\n--------------------- " + result[1] + " --------------------------")


def sign_all_files_recursively(folder_path_to_sign):
    sign_all_files(folder_path_to_sign)
    for folder in listdir(folder_path_to_sign):
        if isdir(folder_path_to_sign + '/' + folder):
            sign_all_files_recursively(folder_path_to_sign + '/' + folder)


print("Generating key pair....\r\n")
if os.path.isfile(PUBLIC_KEY_FILE_NAME) and os.path.isfile(PRIVATE_KEY_FILE_NAME):
    print("Generating key pair.... Skipped!")
    print("Key pair already exist!\r\n")
else:
    key_pair = generate_key_pair()
    print("Generating key pair.... Done!\r\n")

print("Select option to create digital signature:\r\n")

helper_display_menu_(MENU_OPTIONS[0])
menu_choice = helper_get_menu_selection(len(MENU_OPTIONS[0]), MENU_MAIN)

if menu_choice == SINGLE_FILE:
    file_path = input("Enter FILE path:   ")
    if not isfile(file_path):
        file_path = DUMMY_FILE_PATH
    sign_single_file(file_path)
else:
    folder_path = input("Enter FOLDER path:   ")
    if not isdir(folder_path):
        folder_path = DUMMY_FOLDER_PATH
    if menu_choice == ALL_FILES:
        sign_all_files(folder_path)
    elif menu_choice == ALL_FILES_RECURSIVE:
        sign_all_files_recursively(folder_path)
