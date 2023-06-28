# Define the usage message so that the user will now how the script works
# Documentation
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Example: [raw payload file] [output path] [process name] [dll_exports]\n")
    # All the possible arguments
    parser.add_argument("--raw", "-r", help="Path to file containing shellcode",
    type=str,nargs=1,metavar='',required=True)
    parser.add_argument("--path", "-p", help="Path to output the C template file",
    type=str,nargs=1,metavar='',required=True)
    parser.add_argument("--pname", "-n", help="Name of process to inject shellcode into",
    type=str,nargs=1,metavar='',required=True)
    parser.add_argument("--dexports", "-d", help="Specify which DLL Exports you want to use either teams or onedrive",
    type=str,nargs=1,metavar='',required=True)
    parser.add_argument("--enc", "-e", help="Specify which encryption you prefer (XOR / AES)",
    type=str,nargs=1,metavar='',required=True)
    parser.add_argument("--inj", "-i", help="Specify which injection technique you prefer (EB / MS)",
    type=str,nargs=1,metavar='',choices=['EB', 'MS'],required=True)
    parser.add_argument("--rshell", "-s", help="[Optional] Replace shellcode variable name with a unique name",
    type=str,nargs=1,metavar='',required=False, default="encoded_kwdikas")
    parser.add_argument("--rxor", "-x", help="[Optional] Replace xor encryption name with a unique name",
    type=str,nargs=1,metavar='', required=False, default="do_xor")
    parser.add_argument("--rkey", "-k", help="[Optional] Replace key variable name with a unique name",
    type=str,nargs=1,metavar='',required=False, default="key")
    parser.add_argument("--rsleep", "-z", help="[Optional] Replace sleep time your own sleep time",
    type=int,nargs=1,metavar='',required=False,default=4000)

    args = parser.parse_args()
    if (len(sys.argv)) < 1:
            parser.print_help()
            sys.exit(1)
    return args