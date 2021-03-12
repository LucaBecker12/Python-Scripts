# This is an implementation of the caser cipher in Python
# Caser cipher is a symmetric encyrption Algorithm which encode every letter in the Alphabet to one digit between 0 an 25

import string

def encrypt(word, key):
    encrypted = ""
    for c in word:
        encrypted += chr(ord(c) + key)
    return encrypted

def decrypt(word, key):
    decrypted = ""
    for c in word:
        decrypted += chr(ord(c) - key)
    return decrypted
