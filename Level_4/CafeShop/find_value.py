#!/usr/bin/python3

import hashlib

i = 1
found = False

while i < 999999999 and found == False:
    value = f"{int(i):08}" + ' Cola Decaf'

    m = hashlib.sha256()
    m.update(value.encode())
    hash = m.hexdigest()

    if 'c01a' in hash and 'decaf' in hash:
       print(value)
       found = True

    else:
       i += 1
       