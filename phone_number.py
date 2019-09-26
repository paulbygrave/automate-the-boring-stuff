#!/usr/bin/python3
def isPhoneNumber(text):
    if len(text) !=12:
        return False # Not phone number length
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # No area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # No first 3 digits
    if text[7] != '-':
        return False # missing dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # No last 4 digits
    return True

message = 'Call me for a steamy phone session on 444-444-444 or 333-333-333'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Couldn\'t find any phone numbers.')
