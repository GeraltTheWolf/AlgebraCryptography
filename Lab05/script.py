import sys
from caesarcipher import CaesarCipher
import math

textMessage = sys.argv[1]
choice = int(sys.argv[2])

try:
    cesarSecretNumber = int(sys.argv[3])
except:
    cesarSecretNumber = 3


def reverse_string():
    print("Reverse string")
    print(textMessage[::-1])


def reverse_string_by(reverse_by):
    print("Reverse string by " + str(reverse_by))
    new_string = textMessage
    new_string_final = ""
    while len(new_string) % reverse_by > 0:
        new_string += "x"
        print(new_string)
    for chunk in [new_string[i:i + reverse_by] for i in range(0, len(new_string), reverse_by)]:
        new_string_final += chunk[::-1]
    print(new_string_final)


def cesar_cipher():
    print("cesar_cipher")
    new_string_final = CaesarCipher(textMessage, cesarSecretNumber)
    print(new_string_final.encoded)


def cesar_box():
    print("cesar_box")
    new_string = textMessage
    width = cesarSecretNumber
    if width == 0:
        width = int(round(math.sqrt(len(new_string))))
    new_string += '$' * (width - len(new_string) % width)  # Making the string to fit box size
    new_string_final = ''
    for x in range(0, width):
        for i in range(x, len(new_string), width):
            new_string_final += new_string[i]
    print(new_string_final)


if choice == 1:
    reverse_string()
elif choice == 2:
    reverse_string_by(2)
elif choice == 3:
    reverse_string_by(3)
elif choice == 4:
    cesar_cipher()
elif choice == 5:
    cesar_box()



