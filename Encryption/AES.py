#pip install crypto, pycryptodome
import sys
#For Linux
from Cryptodome.Cipher import AES 
#For Windows
#from Crypto.Cipher import AES
from secrets import token_bytes
from binascii import unhexlify
import random
import hashlib
import binascii

keyAES = token_bytes(16)

def returnKey(keyAES):
    hex_values = [f'0x{byte:02x}' for byte in keyAES]
    keyAES = '{' + ', '.join(hex_values) + '}'
    
    return keyAES

def encryptAES(plaintext, keyAES):
    
    def pad(s):
        padding_length = AES.block_size - len(s) % AES.block_size
        padding = bytes([padding_length] * padding_length)
        
        return s + padding

    def aesenc(plaintext, keyAES):
        k = hashlib.sha256(keyAES).digest()
        iv = bytes(16)
        cipher = AES.new(k, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext))
        hex_values = [f'0x{byte:02x}' for byte in ciphertext]
        ciphertext = '{' + ', '.join(hex_values) + '};'
        
        return ciphertext

    ciphertext = aesenc(plaintext, keyAES)
    
    return str(ciphertext)
