'''
***********************
Python exercise number 1
Author: Robert Petrunic
Date: September 2018.
***********************

This code is mistyped!!!! There are errors in it and you have to fix it
1. Read the following learning outcomes and try to fix the code
2. When you are done - try to write this code in a cleaner way (if possible)
3. When you are done with fixing the code - change it so that the program automatically starts again asking for input until! the result is 2 - then the program should stop
4. Create functions

 In this exercise you will learn the following:
1. assigning values to variables
    It's done by using single equal sign (=)
2. convert into different types (string to integer)
    It's done by using keywords, like str(), int(), float()
3. using while and try/except blocks
    you have to end the line with colon (:)
4. difference between on equal sign and 2 equal signs
   = - assigning the value
   == - comparing the values
5. python is using idents - if you screw up idents - you will have an error
    every loop will have its own ident
6. using single line and multiple line comments
    single line comment is a hash sign
    multiple lines comment ate three single quotes to start and three single quotes to finish the commented block
7. python is case sensitive language!!!
    isNull = true and isNull = True are not the same - it has to be True
    isNull = True and isnull = True are not the same - variable name is also case sensitive
8. Using single and double quotes
    U can use either single or double quotes, as long as you start and finish with the same ;-)
'''

# Enter first number
# Let's deal with variable assignment, compare the variables, while loop,
# try/except block, input and output and single line comments

isNumber = False
while not isNumber:
    a = input('Input the first number (product of the two numbers should be 2):')  # single quotes
    print('a = ' + str(a))
    try:
        int(a)
        isNumber = True
    except:
        isNumber = False
        print("Please input a NUMBER - not a string")  # double quotes - you can use either

# let's deal with type conversion

# This is conversion from string to float (.0) - input is being red as a string
print(float(a))

# This is conversion from string to string (unnecessary in this case)
print(str(a))

# This is conversion from string to integer and then to chr
# If the number is to big it will fail!
# Fix it
try:
    print(chr(int(a)))
except:
    print('Conversion to char failed, converted to string instead')
    print(str(int(a)))

# This is conversion into ord - it only works with string of length 1!!!
# anything else will produce an error
# !!! fix this for inputs that have more than 1 character!!!
try:
    if len(str(a)) != 1:
        print('More than one character, printing each one separately')
        for c in str(a):
            print(ord(c))
    else:
        print(ord(a))
except:
    print('Cannot do that')

# Just printing a string user typed into a shell
print(a)

# Enter second number+
isNumber = False
while not isNumber:
    b = input('Input the second number (product of the two numbers should be 2):')
    print('b = ' + str(b))
    try:
        int(b)
        isNumber = True
    except:
        isNumber = False
        print('Please input a NUMBER - not a string')

c = 0

# multiply two entered numbers
c = int(a) * int(b)
print('c = ' + str(c))

# if the product equals 2 - print "OK", if not print "NoNo"
if c == 2:
    print('OK')
else:
    print('NoNo')
