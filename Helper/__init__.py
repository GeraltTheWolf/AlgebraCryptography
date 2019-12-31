import os
from os.path import isfile, join, isdir
from pathlib import Path
from os import listdir

clear = lambda: os.system('cls')

MENU_MAIN = 1
MENU_SUBMENU = 2
BACK_OR_EXIT = -1


def helper_get_menu_selection(max_menu_selection, menu_type=MENU_SUBMENU):
    user_input = 0
    while True:
        try:
            user_input = int(input("Enter menu option:  "))
            clear()
            if user_input == BACK_OR_EXIT and menu_type == MENU_MAIN:
                exit(0)
        except ValueError:
            print("Enter number choice from 0 - " + str(max_menu_selection))
            continue
        else:
            if user_input < -1 or user_input > max_menu_selection:
                if user_input == BACK_OR_EXIT and menu_type == MENU_MAIN:
                    exit(0)
                print("Enter choice from 0 - " + str(max_menu_selection))
                continue
            break
    return user_input


def helper_display_menu_(options, menu_type=MENU_MAIN):
    for i in range(len(options)):
        print(str(i) + " - " + options[i])
    if menu_type == MENU_MAIN:
        print("-1 - EXIT")
    else:
        print("-1 - back")


def helper_string_to_bin(string_input):
    return ''.join(format(ord(x), 'b') for x in string_input)


def helper_read_file(file_path):
    if isfile(file_path):
        return [open(file_path, encoding='utf-8').read(), os.path.basename(file_path)]
    else:
        print(file_path + " is not a file. Closing app.")
        exit()


def helper_read_file_names_in_directory(directory_path):
    if isdir(directory_path):
        only_files = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
        return [only_files, directory_path]
    else:
        print(directory_path + " is not a directory. Closing app.")
        exit()

def helper_read_file_test(file_path):
    if isfile(file_path):
        try:
            return open(file_path, encoding='utf-8').read()
        except UnicodeDecodeError:
            return Path(file_path).read_bytes()
    else:
        print(file_path + " is not a file. Closing app.")
        exit()