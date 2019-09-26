#!/usr/bin/python3
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me for a steamy phone session on 444-444-4444 or 333-333-3333.'))

