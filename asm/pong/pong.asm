;    org 100h

section .text
    global _start
_start:

    mov eax, 0x13               ; 320x200x8
    int 0x10
    ; init
    mov dword [ballx], 1
    mov dword [bally], 1

;    push word 0x0a000
;    pop es

gameloop:

    call clear
    call drawball
    call flip

    call wait4vtrace

    mov ah, 0x1
    int 0x16
    jz gameloop

    mov eax, 0x3                ; 80x25
    int 0x10

    int 0x20                    ; exit


wait4vtrace:
    vsync_active:
        mov dx, 0x03da          ; input port for vtrace
        in al, dx
        test al, 0x8            ; bit 3 on signifies activity
        jnz vsync_active
    vsync_retrace:
        in al, dx
        test al, 0x8            ; bit 3 off signifies retrace
        jz vsync_retrace
    ret

drawball:
    mov eax, [bally]
    mov ebx, eax
    shl eax, 8
    shl ebx, 6
    add eax, ebx
    add eax, [ballx]
    mov dl, 7
    mov [buffer+eax], dl
    ret

flip:
    mov edi, vga
    mov esi, buffer
    mov ecx, 320*200/4
    cld
    rep movsd
    ret

clear:
    mov edi, buffer            ; buffer
    xor eax, eax
    mov ecx, 320*200/4
    cld                         ; clear direction
    rep stosd                   ; store eax at ES:EDI
    ret

section .bss
    ballx resd 1
    bally resd 1
    buffer resd 320*200
    vga resd 320*200
