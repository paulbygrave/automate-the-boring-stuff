#!/usr/bin/python3
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me for a steamy phone session on 444-444-4444 or 333-333-3333.')
print(mo.group())
