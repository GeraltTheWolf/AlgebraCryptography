import sys
import random
import os
import time

inputString = sys.argv[1]


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


def generate_key(input_length, file_name, skip=None):
    file = open(file_name, "r", encoding='latin-1')
    file_size = os.path.getsize("collection.txt")
    if skip is None:
        skip = random.randint(1, file_size)
    words = ""

    try:
        file.seek(skip, 0)
        for line in file:
            if not line.startswith("#"):
                if len(words) < input_length:
                    words += line.replace("\n", "")
                else:
                    while len(words) > input_length:
                        words = words[:-1]
                    break
    except EOFError:
        pass
    except StopIteration:
        print("EOF")
        file.close()
        file = open("collection.txt", "r", encoding='latin-1')
        while len(words) < input_length:
            for line in file:
                if not line.startswith("#"):
                    if len(words) < input_length:
                        words += line.replace("\n", "")
                    else:
                        while len(words) > input_length:
                            words = words[:-1]
                        break
    file.close()
    return words, skip


def save_to_file(starting_point, message):
    result = [str(x) for x in message]
    result = ''.join(result)
    bits = "{0:0>4X}".format(int(result, 2))
    open("cypto_" + time.strftime("%Y%m%d-%H%M%S") + ".txt", 'w+').write(str(starting_point) + ":" + bits)


generatedKey = generate_key(len(inputString), "Collection.txt")
print("Fist generated key with radnom seek: " + generatedKey[0])

generatedKey2 = generate_key(len(inputString), "Collection.txt", generatedKey[1])
print("Second generated key with seek " + str(generatedKey[1]) + ": " + generatedKey2[0])

inputStringLength = len(inputString) - 1

inputStringBitArray = s_to_bit_list(inputString)

# this code will call reverse_String function
inputStringReversed = inputString[::-1]

# this code will call a convert_to_bits function and prepare key for XOR encryption
inputString = inputStringReversed

otp = s_to_bit_list(generatedKey[0])

# this code will call the Encrypt_XOR function and return encrypted message
encrypted = encrypt_xor(inputStringBitArray, otp)

# this code will call the Encrypt_XOR function and return decrypted message
decrypted = encrypt_xor(encrypted, otp)

# this code will call the Encrypt_XOR function and return OTP (key)
otp2 = encrypt_xor(encrypted, decrypted)

print("\nThis is decrypted text: " + bit_list_to_s(decrypted))

save_to_file(generatedKey[1], encrypted)