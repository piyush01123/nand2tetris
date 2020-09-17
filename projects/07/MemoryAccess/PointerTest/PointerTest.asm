// L0: push constant 3030
@3030
D=A
@0
A=M
M=D
@0
M=M+1
// L1: pop pointer 0
@0
M=M-1
A=M
D=M
@THIS
M=D
// L2: push constant 3040
@3040
D=A
@0
A=M
M=D
@0
M=M+1
// L3: pop pointer 1
@0
M=M-1
A=M
D=M
@THAT
M=D
// L4: push constant 32
@32
D=A
@0
A=M
M=D
@0
M=M+1
// L5: pop this 2
@0
M=M-1
A=M
D=M
@3
A=M
A=A+1
A=A+1
M=D
// L6: push constant 46
@46
D=A
@0
A=M
M=D
@0
M=M+1
// L7: pop that 6
@0
M=M-1
A=M
D=M
@4
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
// L8: push pointer 0
@THIS
D=M
@0
A=M
M=D
@0
M=M+1
// L9: push pointer 1
@THAT
D=M
@0
A=M
M=D
@0
M=M+1
// L10: add
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
// L11: push this 2
@3
A=M
A=A+1
A=A+1
D=M
@0
A=M
M=D
@0
M=M+1
// L12: sub
@0
A=M-1
A=A-1
D=M
@0
A=M-1
D=D-M
@0
A=M-1
A=A-1
M=D
@0
M=M-1
// L13: push that 6
@4
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
D=M
@0
A=M
M=D
@0
M=M+1
// L14: add
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
