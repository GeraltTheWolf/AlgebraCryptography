import sys

sys.path.append("..")
from Helper import *
from Hashing import *

main_menu_choice = -1;
sub_main_menu_choice = -1;

STRING = 0
FILE = 1
FOLDER = 2
RECURSIVE = 0
NON_RECURSIVE = 1
MAIN_MENU_STRINGS = [["hash a string", "hash a file", "hash a content of the folder"], [STRING, FILE, FOLDER]]
SUB_MENU_RECURSIVE_STRINGS = [["recursive", "non-recursive"], [RECURSIVE, NON_RECURSIVE]]


def hash_string(algorithm):
    input_string = input("Enter some string to hash: ")
    print(helper_binary_to_hex(helper_string_to_bin(hash_data(input_string, algorithm))))


def hash_file(algorithm, file_path):
    file = helper_read_file(file_path)
    print(os.path.basename(file_path) + " - " + helper_binary_to_hex(helper_string_to_bin(hash_data(file, algorithm))))


def hash_folder(algorithm, folder_path):
    result = helper_get_file_names_in_directory(folder_path)
    print("\r\n------------- FOLDER " + os.path.basename(result[1]) + "-------------")
    for file in result[0]:
        try:
            hash_file(algorithm, file)
        except:
            print("Failed to read file" + file)
    print("--------------------- " + result[1] + " --------------------------")


def hash_folder_recursive(algorithm, folder_path):
    hash_folder(algorithm, folder_path)
    for folder in listdir(folder_path):
        if isdir(folder_path + '/' + folder):
            hash_folder_recursive(algorithm, folder_path + '/' + folder);


helper_display_menu_(MAIN_MENU_STRINGS[0])
main_menu_choice = helper_get_menu_selection(len(MAIN_MENU_STRINGS[0]), MENU_MAIN)

if main_menu_choice == FOLDER:
    helper_display_menu_(SUB_MENU_RECURSIVE_STRINGS[0])
    sub_main_menu_choice = helper_get_menu_selection(len(SUB_MENU_RECURSIVE_STRINGS[0]))

helper_display_menu_(ALGORITHM_NAMES)
algorithm_choice = helper_get_menu_selection(len(ALGORITHM_NAMES))

if main_menu_choice == STRING:
    hash_string(ALGORITHM_NAMES[algorithm_choice])
else:
    if main_menu_choice == FILE:
        file_path = input("Enter FILE path:   ")
        if not isfile(file_path):
            file_path = DUMMY_FILE_PATH
        hash_file(ALGORITHM_NAMES[algorithm_choice], file_path)
    else:
        folder_path = input("Enter FOLDER path:   ")
        if not isdir(folder_path):
            folder_path = DUMMY_FOLDER_PATH
        if main_menu_choice == FOLDER and sub_main_menu_choice == NON_RECURSIVE:
            hash_folder(ALGORITHM_NAMES[algorithm_choice], folder_path)
        elif main_menu_choice == FOLDER and sub_main_menu_choice == RECURSIVE:
            hash_folder_recursive(ALGORITHM_NAMES[algorithm_choice], folder_path)
