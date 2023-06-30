#pip install crypto, pycryptodome
import sys
from Crypto.Cipher import AES
from secrets import token_bytes
from binascii import unhexlify
import hashlib

keyAES = token_bytes(16)

def encryptAES(plaintext,keyAES):
    
    def pad(s):
        padding_length = AES.block_size - len(s) % AES.block_size
        padding = bytes([padding_length] * padding_length)
        return s + padding

    def aesenc(plaintext, keyAES):
        k = hashlib.sha256(keyAES).digest()
        iv = bytes(16)
        cipher = AES.new(k, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext))
        return ciphertext

    ciphertext = aesenc(plaintext, keyAES)
    
    return str(ciphertext)