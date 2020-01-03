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
    """

    Args:
        string_input: any string value will do

    Returns:
        binary string (001100111)

    """
    return ''.join(format(ord(x), 'b') for x in string_input)


def helper_binary_to_hex(binary_string):
    """

    Args:
        binary_string: The binary string (01000110)

    Returns:
        hex string (A12CD)

    """
    return hex(int(binary_string, 2))[2:].upper()


def helper_get_file_names_in_directory(absolute_path):
    """

    Args:
        absolute_path: Path to directory

    Returns:
        [[files],directory absolute path]

    """
    if isdir(absolute_path):
        only_files = [os.path.join(absolute_path, f) for f in listdir(absolute_path) if isfile(join(absolute_path, f))]
        return [only_files, absolute_path]
    else:
        print(absolute_path + " is not a directory. Closing app.")
        exit()


def helper_read_file(absolute_path, as_bytes=False):
    """

    Args:
        absolute_path: Path to file
        as_bytes: flag to read file as bytes

    Returns:
        string or binary contents of the pointed-to file as a bytes object

    """
    if isfile(absolute_path):
        try:
            if as_bytes:
                return bytes(open(absolute_path, encoding='utf-8').read(), 'utf-8')
            else:
                return open(absolute_path, encoding='utf-8').read()
        except UnicodeDecodeError:
            return Path(absolute_path).read_bytes()
    else:
        print(absolute_path + " is not a file. Closing app.")
        exit()
