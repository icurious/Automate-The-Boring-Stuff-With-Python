# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second argument to
# the function will be removed from the string.

import re


def regex(*args):
    if len(args)==1:
        return args[0].strip()
    if len(args)==2:
        remove_regex = re.compile(str(args[1]),re.VERBOSE)
        remove = remove_regex.sub('',args[0])
        print(remove)


print(regex("      %%%hello%%%%World    "))         #Will remove spaces
print(regex("      %%%hello%%%World    ","%%%"))    #will remove "%%%"