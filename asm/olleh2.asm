section .text
    global _start
_start:

    mov edi, msg    ; point to start of string
    mov esi, edi    ; point to end of string
    add esi, len
    dec esi

    mov ecx, len
    shr ecx, 1      ; len(msg)/2

reverse:            ; swap bytes

    mov al, BYTE [edi]
    mov bl, BYTE [esi]
    mov BYTE [esi], al
    mov BYTE [edi], bl

    inc edi
    dec esi

    loop reverse

    mov edx,len     ;message length
    mov ecx,msg     ;message to write
    mov ebx,1       ;file descriptor (stdout)
    mov eax,4       ;system call number (sys_write)
    int 0x80        ;call kernel

    mov eax,1 ; exit 0
    xor ebx,ebx
    int 0x80

section .data
    msg db 'Hello, world!', 0xa
    len equ $ - msg     ;length of the string

