.code

EXTERN SW3_GetSyscallNumber: PROC

NtAllocateVirtualMemory PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 00D952B3Bh        ; Load function hash into ECX.
	call SW3_GetSyscallNumber              ; Resolve function hash into syscall number.
	add rsp, 28h
	mov rcx, [rsp+8]                      ; Restore registers.
	mov rdx, [rsp+16]
	mov r8, [rsp+24]
	mov r9, [rsp+32]
	mov r15,rcx
    mov r14,r15
    mov r13,r14
    mov r10,r13
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
	syscall                    ; Invoke system call.
	ret
NtAllocateVirtualMemory ENDP

NtWriteVirtualMemory PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 007951913h        ; Load function hash into ECX.
	call SW3_GetSyscallNumber              ; Resolve function hash into syscall number.
	add rsp, 28h
	mov rcx, [rsp+8]                      ; Restore registers.
	mov rdx, [rsp+16]
	mov r8, [rsp+24]
	mov r9, [rsp+32]
	mov r10, rcx
	syscall                    ; Invoke system call.
	ret
NtWriteVirtualMemory ENDP

NtQueueApcThread PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 076AD3601h        ; Load function hash into ECX.
	call SW3_GetSyscallNumber              ; Resolve function hash into syscall number.
	add rsp, 28h
	mov rcx, [rsp+8]                      ; Restore registers.
	mov rdx, [rsp+16]
	mov r8, [rsp+24]
	mov r9, [rsp+32]
	mov r15,rcx
    mov r14,r15
    mov r13,r14
    mov r10,r13
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
	syscall                    ; Invoke system call.
	ret
NtQueueApcThread ENDP

NtProtectVirtualMemory PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 082139AB2h        ; Load function hash into ECX.
	call SW3_GetSyscallNumber              ; Resolve function hash into syscall number.
	add rsp, 28h
	mov rcx, [rsp+8]                      ; Restore registers.
	mov rdx, [rsp+16]
	mov r8, [rsp+24]
	mov r9, [rsp+32]
	mov r15,rcx
    mov r14,r15
    mov r13,r14
    mov r10,r13
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
	syscall                    ; Invoke system call.
	ret
NtProtectVirtualMemory ENDP

NtResumeThread PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 0D17213DCh        ; Load function hash into ECX.
	call SW3_GetSyscallNumber              ; Resolve function hash into syscall number.
	add rsp, 28h
	mov rcx, [rsp+8]                      ; Restore registers.
	mov rdx, [rsp+16]
	mov r8, [rsp+24]
	mov r9, [rsp+32]
	mov r15,rcx
    mov r14,r15
    mov r13,r14
    mov r10,r13
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
	syscall                    ; Invoke system call.
	ret
NtResumeThread ENDP

NtClose PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 0FDB111E1h        ; Load function hash into ECX.
	call SW3_GetSyscallNumber              ; Resolve function hash into syscall number.
	add rsp, 28h
	mov rcx, [rsp+8]                      ; Restore registers.
	mov rdx, [rsp+16]
	mov r8, [rsp+24]
	mov r9, [rsp+32]
	mov r15,rcx
    mov r14,r15
    mov r13,r14
    mov r10,r13
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
	syscall                    ; Invoke system call.
	ret
NtClose ENDP

end