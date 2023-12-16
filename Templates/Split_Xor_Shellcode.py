import sys


def split_xor_shellcode(ciphertext):
    # Splits encrypted shellcode into manageable chunks
    # Formats them for use in the application

    # Split the ciphertext into chunks of 50 hex values
    chunks = [ciphertext[i:i+50] for i in range(0, len(ciphertext), 50)]
    # Convert each chunk to a string of comma-separated hex values
    chunk_strings = [', '.join(['0x' + hex(ord(x))[2:].zfill(2) for x in chunk]) for chunk in chunks]
    # Combine the chunk strings and format them into a shellcode string
    ciphertext_split = '{\n\t' + ',\n\t'.join(chunk_strings) + '\n};'
    return ciphertext_split


def split_aes_shellcode(ciphertext):
    ciphertext_split = ''
    
    lines = [ciphertext[i:i+60] for i in range(0, len(ciphertext), 60)]

    # Join the lines with newline characters to create the final result
    ciphertext_split = '\n'.join(lines)


    return ciphertext_split
