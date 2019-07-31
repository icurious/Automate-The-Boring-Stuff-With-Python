import pyperclip
import re

# Phone nmber will be 3 digit are code optional with separator followed by 3 digits then separator then last four digits
# e.g 123-456-789, (123)-456-789, 456-789, 123.456.789, 123 456 789 etc.
# Area code Optional 3 digit. can be 123 or (123) or might not be present.
# Phone number separator can be space(" ") or hyphen(-) or period(.)

# The username part of the email address u is one or more characters
# that can be any of the following: lowercase and uppercase letters, numbers,
# a dot, an underscore, a percent sign, a plus sign, or a hyphen
# The domain name has a slightly less permissive character class with only letters, numbers, periods, and hyphens
# And last will be the “dot-com” part (technically known as the top-level domain), which can  really be dot-anything. This is between two and four characters


phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              #Area Code
(\s|-|\.)?                      #Separator may or may not be present
(\d{3})                         #First three digits
(\s|-|\.)                       #Separator. this time not optional
(\d{4})                         #last four digits    
)'''  ,re.VERBOSE)

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+               #Username
@                               #@ symbol
[a-zA-Z0-9.-]+                  #domain name
(\.[a-zA-Z]{2,4})               #dot-something
)''' , re.VERBOSE)

text = str(pyperclip.paste())

phone_no_list = phone_regex.findall(text)
emai_list = email_regex.findall(text)

phone_numbers = ''
emails = ''

if phone_no_list is not []:
    phone_numbers = 'Phone Numbers: \n'
    for t in phone_no_list:
        phone_numbers = phone_numbers + t[0]+ '\n'

if emai_list is not []:
    emails = 'Emails: \n'
    for t in emai_list:
        emails = emails + t[0]+ '\n'

if phone_no_list == [] and emai_list == []:
    pyperclip.copy("Phone numbers or email not found.")

else:
    new_text = phone_numbers + emails
    pyperclip.copy(new_text)



