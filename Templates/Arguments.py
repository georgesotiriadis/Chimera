# Define the usage message so that the user will know how the script works
# Documentation
import argparse
import sys
def parse_arguments():

	
   # Define the usage message so that the user will know how the script works
   # Documentation
    parser = argparse.ArgumentParser(
        description="Example: [raw payload file] [output path] [process name] [dll_exports]\n")
    # All the possible arguments
    parser.add_argument("--raw", "-r", help="Path to file containing shellcode",
    type=str,nargs=1,required=True)
    parser.add_argument("--path", "-p", help="Path to output the C template file",
    type=str,required=True)
    parser.add_argument("--pname", "-n", help="Name of process to inject shellcode into",
    type=str,required=True)
    parser.add_argument("--dexports", "-d", help="Specify which DLL Exports you want to use either teams or onedrive",
    type=str,nargs=1,choices=['teams', 'onedrive'],required=True)
    parser.add_argument("--enc", "-e", help="Specify which encryption you prefer (XOR / AES)",
    type=str,nargs=1,choices=['XOR', 'AES'],required=True)
    parser.add_argument("--inj", "-i", help="Specify which injection technique you prefer (EB / MS)",
    type=str,choices=['EB', 'MS'],required=True)
    parser.add_argument("--rshell", "-s", help="[Optional] Replace shellcode variable name with a unique name",
    type=str,required=False, default="encoded_shell")
    parser.add_argument("--rxor", "-x", help="[Optional] Replace xor encryption name with a unique name",
    type=str,required=False, default="do_xor")
    parser.add_argument("--rkey", "-k", help="[Optional] Replace key variable name with a unique name",
    type=str,required=False, default="key")
    parser.add_argument("--rsleep", "-z", help="[Optional] Give total sleep time to include during execution (seconds)",
    type=int,required=False,default=4000)
    parser.add_argument("--size", "-f", help="[Optional] File size of junk data in KB. Zero (0) is disabled (default), and one (1) is random filesize.", 
    type=int,required=False,default=0)

    args = parser.parse_args()
    if (len(sys.argv)) < 1:
            parser.print_help()
            sys.exit(1)
    return args
