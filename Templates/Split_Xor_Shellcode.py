import sys
sys.path.append('./Encryption')
from Encryption.Xor import DoXor
from Read_Shellcode import key,plaintext



ciphertext = DoXor(plaintext, key)


# Split the ciphertext into chunks of 50 hex values
chunks = [ciphertext[i:i+50] for i in range(0, len(ciphertext), 50)]

# Convert each chunk to a string of comma-separated hex values
chunk_strings = [', '.join(['0x' + hex(ord(x))[2:].zfill(2) for x in chunk]) for chunk in chunks]

# Combine the chunk strings and format them into a shellcode string
ciphertext_split = '{\n\t' + ',\n\t'.join(chunk_strings) + '\n};'


