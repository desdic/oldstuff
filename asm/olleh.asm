section .text
    global _start
_start:

    mov ecx,msg
    add ecx, len-2 ; point to end of msg
    mov [offset], ecx

    mov ecx,len
    dec ecx
loop:
    mov eax, ecx
    push ecx
    mov ecx,[offset]
    mov edx,1 ; 1 char
    mov ebx,1
    mov eax,4
    int 0x80
    dec byte [offset]

    pop ecx
    loop loop

    mov eax,1
    xor ebx,ebx
    int 0x80

section .data
    msg db 'Hello, world!', 0xa
    len equ $ - msg     ;length of the string

section .bss
    offset resw 0
