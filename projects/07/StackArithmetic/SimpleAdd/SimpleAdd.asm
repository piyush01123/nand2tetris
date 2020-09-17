// L0: push constant 7
@7
D=A
@0
A=M
M=D
@0
M=M+1
// L1: push constant 8
@8
D=A
@0
A=M
M=D
@0
M=M+1
// L2: add
@0
A=M-1
A=A-1
D=M
@0
A=M-1
D=D+M
@0
A=M-1
A=A-1
M=D
@0
M=M-1
