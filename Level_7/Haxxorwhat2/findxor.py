#!/usr/bin/python

import binascii

f1 = open('haxxorwhat2', 'br')
data = f1.read()
f1.close()

result = bytearray(len(data))
pwd = 'xorlatan'

for i in range(len(data)):
    result[i] = data[i] ^ ord(pwd[i % len(pwd)])

f2 = open('haxxorwhat2-xorlatan.zip', 'bw')
f2.write(result)
f2.close()