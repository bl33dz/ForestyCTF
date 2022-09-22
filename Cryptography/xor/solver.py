#!/usr/bin/python3

a = open("flag.txt.encrypted", "rb").read()
b = [a[len(a)-i-1] ^ (len(a)-i-1 + 0x37) for i in range(len(a))]

print(bytes(b))