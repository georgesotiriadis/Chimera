import random
from Templates.Split_Xor_Shellcode import split_xor_shellcode
# generate random  4 byte key
key = ''.join([chr(random.randint(0, 255)) for i in range(4)])
key_hex = ''.join(['\\x' + hex(ord(x))[2:].zfill(2) for x in key])

#xor oeperation function 
def DoXor(data, key):
    l = len(key)
    output_str = ""

    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        output_str += chr((current) ^ ord(current_key))

        
    return output_str

