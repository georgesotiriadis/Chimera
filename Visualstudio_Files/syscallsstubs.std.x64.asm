.code

EXTERN SW3_GetSyscallNumber: PROC

NtProtectVirtualMemory PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 00F99051Bh        ; Load function hash into ECX.
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

NtWriteVirtualMemory PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 0DB942197h        ; Load function hash into ECX.
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
NtWriteVirtualMemory ENDP

NtAllocateVirtualMemory PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 00595031Bh        ; Load function hash into ECX.
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

NtQueueApcThread PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 09A20419Fh        ; Load function hash into ECX.
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

NtResumeThread PROC
	mov [rsp +8], rcx          ; Save registers.
	mov [rsp+16], rdx
	mov [rsp+24], r8
	mov [rsp+32], r9
	sub rsp, 28h
	mov ecx, 074CE3A67h        ; Load function hash into ECX.
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

end