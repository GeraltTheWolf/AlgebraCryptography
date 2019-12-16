'''
***********************
Practical 6
Author: Robert Petrunic
Date: October 2018.
***********************

As a developer you will have to fix someone else's code and you will have to work with legacy code also. This is a
simulation of both issues that you will have in real life from time to time.

This application is poorly written, and it does NOT work correctly in python3! You have two options: Write your own
application or fix this one. The application main functions are the following:
-	Take string input
-	Convert string to byte
-	Reverse original string
-	Convert reversed string to byte
-	XOR original string with reversed string
o	This is encryption / decryption function

If you decide to fix the existing application, do the following:
1. modify all the functions to remove unnecessary loops if they exist
2. modify all function calls to remove all unnecessary repetitions
3. optimize the code to make it faster (if you didn't do it in the first two steps)
4. Explain why is this encryption scheme flawed even though it is using "OTP"?
5. Explain why is this OTP not the real OTP?
6. Application has to be called like this:
  python fakeOTP.py "text to be encrypted/decrypted"
and it has to have an option to encrypt the contents of the file also
  python fakeOTP.py "path_to_a_file_to_be_encrypted"
Your application has to recognize weather the text is to be encrypted/decrypted directly from the parameter string
or from file on the file system.

If you decide to create an application from scratch you have to implement the following:
1. Implement the same encryption/decryption technique as in the code below
2. Explain why is this encryption scheme flawed even though it is using "OTP"?
3. Explain why is this OTP not the real OTP?
4. Application has to be called like this:
  python fakeOTP.py "text to be encrypted/decrypted"
and it has to have an option to encrypt the contents of the file also
  python fakeOTP.py "path_to_a_file_to_be_encrypted"
Your application has to recognize weather the text is to be encrypted/decrypted directly from the parameter string
or from file on the file system.

This encryption scheme was supposed to be OTP (One-Time pad), which is so called unbreakable encryption, where the key
length is the same as the length of the text to be encrypted and the key is not supposed to be reused NEVER EVER EVER
EVER!. Unfortunately, implementation is flawed and this is not real OTP - even though it looks like it at the first
sight.

Explain what is OTP and why is this type o encryption (OTP) unusable in real world?

!!! After you fix and optimize the code below (or create the new application with all the functionality requested in the task, make this encryption scheme a little bit more difficult to crack and safer by doing the following (which is not the OTP either!!!)

1. Create a NEW program (you can use previous one as a template of create completely new one):
  - you have to use XOR-ing though
2. Use the text file provided with the exercise and read the key from the text file:
  - Key has to be the same size as the message to be encrypted and it is not allowed for the key to be partially or
  fully repeated during a single encryption attempt - it has to be used only once
  - Download the text file from the following link (unzip it before usage):
  https://1drv.ms/f/s!Ajm-3AdyO3sSht4Ll6HOUMTuyTtdoA
  - You have to use random number to choose the starting point in the text file as a starting point for a key
  - Code has to do the wrapping around this dictionary file if during the key generation EOF is reached
  - starting point has to be written down to a file together with the encrypted message like this:
   startingPoint:encryptedMessage (ex. 1324:AF12324412CBD124255756) where 1324 is character at the location number 1234
   in the file used to generate the key. The message has to be written into a file in HEX-a notation(not on the screen)!
   If the key starts at position that will reach the end of the text before the key is fully generated you have to wrap
   the key (continue from the beginning of the file until the key size is at the length it has to be).
3. Answer the following questions:
  - If the key is not supposed to be repeated partially nor fully, what is the maximum size of the message you can
  encrypt with this method as defined in the task?

IMPORTANT: all the exercises you are working on, including this one is for learning purposes only - DO NOT TRY TO CREATE
 YOUR OWN ENCRYPTION SCHEME AND USE IT IN YOUR APPLICAITON BECAUSE IT WILL NOT BE AS SECURE AS THE ONES ALREADY ON THE
 MARKET, like AES for instance!

1. Explain why is the above claim correct!

'''
import sys


# this is the encryption / decryption function
def encrypt_xor(message, key):
    result = []
    i = len(message) - 1
    while i >= 0:
        result = [(message[i] ^ key[i])] + result
        i -= 1
    return result


def s_to_bit_list(s):
    ordinals = (ord(c) for c in s)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    return [(o >> shift) & 1 for o in ordinals for shift in shifts]


def bit_list_to_chars(bl):
    bi = iter(bl)
    bytes = zip(*(bi,) * 8)
    shifts = (7, 6, 5, 4, 3, 2, 1, 0)
    for byte in bytes:
        yield chr(sum(bit << s for bit, s in zip(byte, shifts)))


def bit_list_to_s(bl):
    return ''.join(bit_list_to_chars(bl))


# this code will call a convert_to_bits function and prepare input string for XOR encryption
inputString = sys.argv[1]
inputStringLength = len(inputString) - 1

inputStringBitArray = s_to_bit_list(inputString)

print("\nThis is the string that will be encrypted\n")
print(inputStringBitArray)

# this code will call reverse_String function
inputStringReversed = inputString[::-1]
print("\nReversed\n" + inputStringReversed)

# this code will call a convert_to_bits function and prepare key for XOR encryption
inputString = inputStringReversed

otp = s_to_bit_list(inputStringReversed)
print("\nThis is the !OTP (One-Time pad)\n")
print(otp)

# this code will call the Encrypt_XOR function and return encrypted message
encrypted = encrypt_xor(inputStringBitArray, otp)
print("\nThis is encrypted\n")
print(encrypted)

# this code will call the Encrypt_XOR function and return decrypted message
decrypted = encrypt_xor(encrypted, otp)
print("\nThis is decrypted\n")
print(decrypted)

# this code will call the Encrypt_XOR function and return OTP (key)
otp2 = encrypt_xor(encrypted, decrypted)
print("\nThis is the key after XOR-ing the encrypted and decrypted message \n")
print(otp2)

print("\nThis is decrypted text \n" + bit_list_to_s(decrypted))
print()

print("Explain why is this encryption scheme flawed even though it is using OTP?")
print("Ovaj OTP je jednostavno prokužiti je cijelo vrijeme koristi istu metodu. Stalno koristi isti key.")
print()
print("5. Explain why is this OTP not the real OTP?")
print("OTP bi svaki puta trebao koristi drugi password")
print()
print("Explain what is OTP and why is this type o encryption (OTP) unusable in real world?")
print("Zbog toga što key treba biti iste veličine kao i poruka (poruka može biti 9 gb pa i key, a i treba omogućiti prijenos keya")



