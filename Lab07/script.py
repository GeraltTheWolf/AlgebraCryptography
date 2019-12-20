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
    print(hex(int(helper_string_to_bin(hash_data(input_string, algorithm)), 2)))


def hash_file(algorithm):
    result = helper_read_file(input("Enter FILE path:   "))
    print(result[1] + " - " + hex(int(helper_string_to_bin(hash_data(result[0], algorithm)), 2)))


def hash_folder(algorithm, folder_path):
    result = helper_read_file_names_in_directory(folder_path)
    print("\r\nFOLDER" + os.path.basename(result[1]))
    for r in result[0]:
        try:
            read_file = helper_read_file(result[1] + "/" + r)
            print(read_file[1] + " - " + hex(int(helper_string_to_bin(hash_data(read_file[0], algorithm)), 2)))
        except:
            print("Failed to read file" + r)


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
elif main_menu_choice == FILE:
    hash_file(ALGORITHM_NAMES[algorithm_choice])
elif main_menu_choice == FOLDER and sub_main_menu_choice == NON_RECURSIVE:
    hash_folder(ALGORITHM_NAMES[algorithm_choice], input("Enter DIR path:   "))
elif main_menu_choice == FOLDER and sub_main_menu_choice == RECURSIVE:
    hash_folder_recursive(ALGORITHM_NAMES[algorithm_choice], input("Enter DIR path:   "))
