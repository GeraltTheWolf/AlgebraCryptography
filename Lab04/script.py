'''
***********************
Python exercise number 2
Author: Robert Petrunic
Date: September 2018.
***********************

Let's work with strings in python.
In python string is an array and you can access it in the same manner. For instance:
"Hello class" string can be accessed by using an array like notation:
string1 = "Hello class"
string2 = "let's start"
stringecho = string1 + " " + string2
print (string1)		# it will print "Hello class"
print (string2)		# it will print "let's start"
print (stringecho) 	# it will print "Hello class let's start"
print (string[0:4])	# it will print "Hell"
print (string[0:4]*3) # it will print "HellHellHell"

# Write a program (or programs) that will take a string as an input and do the following with the string
1. Reverse it: Hell -> lleH
2. create 2 strings from the input string by taking letters at the even position in the string into first and odd letters into second string:
	EXAMPLE:
string = "This is my string"
	string1 = "hsi ysrn"
	string2 = "Ti sm tig"
3. Take an input string and reverse it. Then repeat the string x times (x is the parameter application expect together with a string
example command line:
py "this is my string" 10 (repeat reversed string 10 times)
4. Go to www.spammimic.com website. Click on encode link. Choose option "Encode as space". In the "Enter a short secret message" type "Hello" without quotations, and click on the encode button (do not enter anything in the "Paste in some innocent looking text:" option). Double click in the results box and you will have few lines of spaces.
Copy and paste this into a notepad or notepad++. Try to reverse engineer this and write a python script that will decode the message encoded with this option. If you do not finish this in the classroom, try to finish it at home!
'''

import sys

try:
    inputString = sys.argv[1]
    repeatCount = int(sys.argv[2])
except:
    print('Pass first parameter string and second integer!!!!')
    exit(1)

# Task 1

print("Task 1:")
string1Reversed = inputString[::-1]
print("Reversed:  " + string1Reversed)
print()



# Task 2

stringEven = inputString[1::2]
stringOdd = inputString[::2]
print("Task 2:")
print("Odd:  " + stringOdd)
print("Even:  " + stringEven)
print()



# Task 3

repeatedString = string1Reversed * repeatCount
print("Task 3:")
print("Repeated string:  " + repeatedString)
print()



# Task 4
try:
    fileRead = open("whitespace.txt", "r").read()
    print("Task 4:")
except:
    print("No file named whitespace.txt found in root")
    exit(1)

binaryStr = ''

for c in str(fileRead):
    # print(ord(c))
    if ord(c) == 32:
        binaryStr += "0"
    elif ord(c) == 9:
        binaryStr += "1"

# Remove first zeros
binaryStr = binaryStr[8:]
print("This is binary representation:  " + binaryStr)
print("This is message:  " + bytes(int(binaryStr[i: i + 8], 2) for i in range(0, len(binaryStr), 8)).decode('utf-8'))
