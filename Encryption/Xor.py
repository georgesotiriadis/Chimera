import random

def DoXor(data, key):
    l = len(key)
    output_str = ""

    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        output_str += chr((current) ^ ord(current_key))

    return output_str



