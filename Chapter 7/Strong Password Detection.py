# Write a function that uses regular expressions to make sure the password
# string it is passed is strong. A strong password is defined as one that is at
# least eight characters long, contains both uppercase and lowercase characters,
# and has at least one digit. You may need to test the string against multiple regex
# patterns to validate its strength

import re

password_regex_8_char = re.compile(r'(.{8,})', re.VERBOSE)   #At least 8 characters
password_regex_1_digit = re.compile(r'(\d+)', re.VERBOSE)    #At least 8 characters
password_regex_uppercase = re.compile(r'[A-Z]+', re.VERBOSE) #At least 1 uppercase char
password_regex_lowercase = re.compile(r'[a-z]+', re.VERBOSE) #At least 1 lowercase char

while True:
    password = input("Enter a Password: ")

    found1 = password_regex_8_char.findall(password)
    found2 = password_regex_1_digit.findall(password)
    found3 = password_regex_uppercase.findall(password)
    found4 = password_regex_lowercase.findall(password)

    if len(found1) == 0:
        print(" * Password must be at least 8 Characters long!")
    if len(found2) == 0:
        print(" * Password must contain at least 1 digit!")
    if len(found3) == 0:
        print(" * Password must have UpperCase Letters!")
    if len(found4) == 0:
        print(" * Password must have LowerCase Letters!")

    if found1!=[] and found2!=[] and found3!=[] and found4!=[]:
        print("Its a strong Password")
        break




