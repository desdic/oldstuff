#!/usr/bin/env python2
"""
Use pwntools to interact with a process
"""

from pwn import *

context(os = 'linux', arch = 'amd64')

if 'HOST' in args:
    r = remote(args['HOST'], int(args['PORT']))
else:
    r = process('guess.py')

start = 1
while True:
    print("Sending %d" % start)
    r.sendline(str(start))
    a = r.recvline()
    if "Nope" not in a:
        break
    start += 1

print("Lucky number was: %d[%s]" % (start, a))
r.clean()
