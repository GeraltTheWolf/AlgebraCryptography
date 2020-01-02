import sys

sys.path.append("..")
from Helper import *
from Hashing import *

# data_text = helper_read_file(b"C:/Users/irezek/Desktop/Images/text.txt")
# data_binary = helper_read_file("C:/Users/irezek/Desktop/Images/maveric.jpg")


result = helper_get_file_names_in_directory("C:/Users/irezek/Desktop/Images")

res = helper_read_file(result[0][0])

print(result)

print (res)



# data_text_hash = hash_data(data_text, ALGORITHM_NAMES[2])
# data_binary_hash = hash_data(data_binary, ALGORITHM_NAMES[2])
#
# print("\r\nAfter Hashing")
# print(data_text_hash)
# print(data_binary_hash)
#
# binary_str_txt_file = helper_string_to_bin(data_text_hash)
# binary_str_bin_file = helper_string_to_bin(data_binary_hash)
#
#
# print("\r\nAfter Converting to binary string")
# print(binary_str_txt_file)
# print(binary_str_bin_file)
#
# print("\r\nAfter Converting to hex string")
# hex_str_txt_file = helper_binary_to_hex(binary_str_txt_file)
# hex_str_bin_file = helper_binary_to_hex(binary_str_bin_file)
#
# print(hex_str_txt_file)
# print(hex_str_bin_file)



#print (binascii.hexlify(bytes(int(data_binary_hash[i: i + 8], 2) for i in range(0, len(data_binary_hash), 8))))
#print (binascii.hexlify(data_binary_hash))

#print (binascii.hexlify(bin(int(helper_string_to_bin(data_text_hash),2))))
#print (binascii.hexlify(bin(int(helper_string_to_bin(data_binary_hash),2))))