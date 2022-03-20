#!/usr/bin/python3

import hashlib

numbers = b'11865457 Vanilla Cafe', b'42640575 Cherry Cola', b'80427209 Beef Jerky'

for i in range(len(numbers)):
    m = hashlib.sha256()
    m.update(numbers[i])
    print(m.hexdigest())