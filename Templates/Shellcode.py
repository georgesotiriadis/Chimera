from Encryption.Choose_Encryption import ChosenEncryption

def EncryptedShellcode(shellcode_var,ciphertext_split):
    # Generates a string representing encrypted shellcode
    # Integrates with the chosen encryption method

    shellcode = f"""
    #pragma once
    unsigned char {shellcode_var}[] = {ciphertext_split}
    """
    return shellcode
