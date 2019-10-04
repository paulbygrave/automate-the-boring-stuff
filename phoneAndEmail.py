
import re
import pyperclip

# TODO: Create a regex for phone numbers
# 111-111-1111, 111-1111, (111) 111-1111, 111-1111 ext. 12345, x12345
phoneRegex = re.compile(r'''
( 
((\d\d\d)|(\(\d\d\d\)))?           # area code
(\s|-|\.)                              # first separator
\d\d\d                              # first 3 digits
(-|\.)                                   # separator
\d\d\d\d                            # last 4 digits
(((ext(\.)?\s)|x)                   # extension word-part(optional)
(\d{2,5}))?                         # extension number-part (optional)
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
# something@something.something
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+     # name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the emails/phone numbers from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# TODO: Print the extracted emails/phone numbers
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
print(str(results))
