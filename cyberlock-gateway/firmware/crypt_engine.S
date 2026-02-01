.global fast_verify
fast_verify:
    eor r24, r22   ; XOR entre entrada e chave
    com r24        ; Inverte os bits (NOT)
    ret            ; Retorna para o C++