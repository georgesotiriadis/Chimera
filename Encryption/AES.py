#pip install crypto, pycryptodome
import sys
from Cryptodome.Cipher import AES 
from secrets import token_bytes
from binascii import unhexlify
import hashlib
import random

#keyAES = token_bytes(16)
key = ''.join([chr(random.randint(0, 255)) for i in range(16)])
keyAES = ''.join(['\\x' + hex(ord(x))[2:].zfill(2) for x in key])

def encryptAES(plaintext,keyAES):
    
    def pad(s):
        padding_length = AES.block_size - len(s) % AES.block_size
        padding = bytes([padding_length] * padding_length)
        return s + padding

    def aesenc(plaintext, keyAES):
        k = hashlib.sha256(keyAES.encode()).digest()
        iv = bytes(16)
        cipher = AES.new(k, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext))
        return ciphertext

    ciphertext = aesenc(plaintext, keyAES)
    
    return str(ciphertext)

    