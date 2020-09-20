// L0: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// L1: pop local 0         
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
// L2: label LOOP_START
(LOOP_START)
// L3: push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L4: push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L5: add
@SP
A=M-1
A=A-1
D=M
@SP
A=M-1
D=D+M
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
// L6: pop local 0	        
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
// L7: push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L8: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// L9: sub
@SP
A=M-1
A=A-1
D=M
@SP
A=M-1
D=D-M
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
// L10: pop argument 0      
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// L11: push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L12: if-goto LOOP_START  
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JNE
// L13: push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
