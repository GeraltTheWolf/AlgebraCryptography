import os
import hashlib
import time





















clear = lambda: os.system('cls')
hash_object = hashlib.md5(b"Hello world")

main_menu_choice = -1

def print_main_menu():
    print("Chose:\r\n")
    print("1 - hash a string\r\n2 - hash a file\r\n3 - hash a content of the folder\r\n0 - Exit\r\n")


def save_to_file(message):
    open("cypto1_" + time.strftime("%Y%m%d-%H%M%S") + ".txt", 'w+').write(message)

def print_algorithms_menu():
    clear()
    index_of_algorithm = 1
    algNames = list(hashlib.algorithms_guaranteed)
    for a in algNames:
        print(str(index_of_algorithm) + " - " + a)
        index_of_algorithm += 1
    print("0 - Back")

    algorithms_menu_choice = int(input())

    if 0 < algorithms_menu_choice < len(algNames):
        m = hashlib.new(algNames[algorithms_menu_choice-1])
        m.update(hash_object)
        try:
            hash = m.hexdigest()
        except:
            hash = m.hexdigest(len(hash_object))
        save_to_file(hash)


while main_menu_choice != 0:
    clear()
    print_main_menu()
    main_menu_choice = int(input())
    if main_menu_choice != 0:
        print_algorithms_menu()


def print_hash_and_file_name(hash,file_name):
    print()
