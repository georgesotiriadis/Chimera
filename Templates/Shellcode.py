from Encryption.Choose_Encryption import ChosenEncryption

def EncryptedShellcode(shellcode_var,ciphertext_split):


    shellcode = f"""
    unsigned char {shellcode_var}[] = {ciphertext_split}
    """
    return shellcode
