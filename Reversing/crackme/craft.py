#!/usr/bin/python3

from pwn import xor

flag = b"just_trace_or_debug_in_order_to_know_how_the_program_works"
secret = b"7827197"

print([x for x in xor(flag, secret)])
print(xor(flag, secret).decode())

