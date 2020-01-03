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




