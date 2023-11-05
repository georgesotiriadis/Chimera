def ChosenEncryption(encryption_type,xor_func):

    aes = f"""
     int AESDec(char* size, unsigned int size_len, char* encryptionKey, size_t keySize) {{
	HCRYPTPROV hHash;
	HCRYPTHASH hHaHash;
	HCRYPTKEY hencryptionKey;

	if (!CryptAcquireContextW(&hHash, NULL, NULL, PROV_RSA_AES, CRYPT_VERIFYCONTEXT)) {{
		return -1;
	}}
	if (!CryptCreateHash(hHash, CALG_SHA_256, 0, 0, &hHaHash)) {{
		return -1;
	}}
	if (!CryptHashData(hHaHash, (BYTE*)encryptionKey, (DWORD)keySize, 0)) {{
		return -1;
	}}
	if (!CryptDeriveKey(hHash, CALG_AES_256, hHaHash, 0, &hencryptionKey)) {{
		return -1;
	}}

	if (!CryptDecrypt(hencryptionKey, (HCRYPTHASH)NULL, 0, 0, (BYTE*)size, (DWORD*)&size_len)) {{
		return -1;
	}}

	CryptReleaseContext(hHash, 0);
	CryptDestroyHash(hHaHash);
	CryptDestroyKey(hencryptionKey);

	return 0;
    }}
    
    """

    xor=f"""
    void {xor_func}(unsigned char* data, size_t data_len, char* key, size_t key_len)
    {{
        int j;
        j = 0;
        for (int i = 0; i < data_len; i++)
        {{
            if (j == key_len - 1) j = 0;
            data[i] = data[i] ^ key[j];
            j++;
        }}
    }};
    """
    
    if encryption_type == "AES": 
        return aes
    else:
        return xor