#!/usr/bin/python3

FLAG = b"ForestyCTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

def encrypt(plaintext):
    ciphertext = []
    for i in range(len(plaintext)):
        print(f"plaintext[{len(plaintext) - i - 1}] ^ {i + 0x37:x}")
        ciphertext.append(plaintext[len(plaintext) - i - 1] ^ (i + 0x37))
    return bytes(ciphertext)

print(encrypt(FLAG))
