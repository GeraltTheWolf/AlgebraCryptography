'''
***********************
Practical 7
Author: https://www.pythoncentral.io/hashing-strings-with-python/
Date: December 2018.
***********************
By using the sample code provided below, create a program in python:
1. hash an input string with one of the following hashing algorithms:
	MD5
	SHA (SHA1)
	SHA2 (SHA224, SHA256, SHA384, SHA512)
	SHA3 (SHA3_256, SHA3_224, SHA3_384, SHA3_512)
	blake (blake2b, blake2s)
	shake (shake_128, shake_256)
	adler32
	crc32

2. hash a file with the above mentioned hashing algorithms

3. hash all the files in the specific folder (non-recursive and recursive)

!! The program should have a menu driven options, meaning that user should start the program and choose the options
Example:
first menu should look like this:
	Choose:
		1 - hash a string
		2 - hash a file
		3 - hash a content of the folder
the second menu should look like this:
	Choose:
		1 - MD5
		2 - SHA1 (SHA160)
		3 - SHA224
		4 - SHA256
		5 - SHA384
		6 - SHA512
		...
		x - SHA3_512
		...
		y - blake2b
		...
Please, use the hashlib.algorithms_guaranteed function to programatically generate this menu!

the third menu is based on the options from the first menu - if the user has chosen the option number 3 (hash a content of the folder) menu 3 should appear asking for user input regarding a recursive (hash all the files in the current and all the files in subfolders) or non-recursive option (hash only the files in the current folder ignoring the subfolders)
third menu should look like this
	Choose:
		1 - recursive
		2 - non-recursive

!!! the program should return the result in hex representation on screen (for example: D12ADFFBC342EFAACCE3AAACCCEEEFFF). Lower case or uppercase - it doesn't matter.
If the option "hash a file" was chosen it should return the hash and the name of the file (if this is a single file!).

Example:
	hash	filename
If the option was to hash the files in the folder, then the result is a file with all the hashes and files. The resulting file should look like this:
	hash	file name
	hash2	filename2
	hash3	filename3
	...

If the option was to hash the files in the folder recursively, then the result is a file with all the hashes and files. The resulting file should look like this:
	Folder1
		hash	file name
		hash2	filename2
		hash3	filename3
	Folder2
		hash	file name
		hash2	filename2
		hash3	filename3
	...
		...

'''
# hashing functions
import hashlib

# CRC functions (adler32, crc32)
# import zlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)

# This works only in python 2 - string
# hash_object = hashlib.md5("Hello world")
# print (hash_object.hexdigest())

# This works only in python 3 - bytes!!! (letter b infront of the string!! it is not a typo!
# Example 1 - MD5:
hash_object = hashlib.md5(b"Hello world")
print(hash_object.hexdigest())

# Example 2 - blake2s:
hash_object = hashlib.blake2s(b"Hello world")
print(hash_object.hexdigest())

# Example 3 - SHA3_512:
hash_object = hashlib.sha3_512(b"Hello world")
print(hash_object.hexdigest())
