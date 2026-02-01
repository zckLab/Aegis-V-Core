.global secure_transform
secure_transform:
    push r18
    push r19
    mov r18, r24
    ldi r19, 4
round_loop:
    eor r18, r22
    swap r18
    rol r18
    subi r18, 0xAC
    dec r19
    brne round_loop
    mov r24, r18
    pop r19
    pop r18
    ret