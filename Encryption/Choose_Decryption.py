def Choose_Decryption(encryption_type,xor_func,shellcode_var,key_var):
    xor_dec=f"""
         {xor_func}({shellcode_var}, sizeof({shellcode_var}), {key_var}, sizeof({key_var}));
    """

    aes_dec=f"""
        AESDecrypt((char *) {shellcode_var}, sizeof({shellcode_var}), (char *) {key_var}, sizeof({key_var}));
        """
   
    if encryption_type == "AES": 
        return aes_dec
    else:
        return xor_dec