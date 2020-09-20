// L0: push argument 1
@ARG
A=M
A=A+1
D=M
@SP
A=M
M=D
@SP
M=M+1
// L1: pop pointer 1           
@SP
M=M-1
A=M
D=M
@THAT
M=D
// L2: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// L3: pop that 0              
@SP
M=M-1
A=M
D=M
@THAT
A=M
M=D
// L4: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// L5: pop that 1              
@SP
M=M-1
A=M
D=M
@THAT
A=M
A=A+1
M=D
// L6: push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L7: push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// L8: sub
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
// L9: pop argument 0          
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// L10: label MAIN_LOOP_START
(MAIN_LOOP_START)
// L11: push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L12: if-goto COMPUTE_ELEMENT 
@SP
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
// L13: goto END_PROGRAM        
@END_PROGRAM
0;JMP
// L14: label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
// L15: push that 0
@THAT
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L16: push that 1
@THAT
A=M
A=A+1
D=M
@SP
A=M
M=D
@SP
M=M+1
// L17: add
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
// L18: pop that 2              
@SP
M=M-1
A=M
D=M
@THAT
A=M
A=A+1
A=A+1
M=D
// L19: push pointer 1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// L20: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// L21: add
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
// L22: pop pointer 1           
@SP
M=M-1
A=M
D=M
@THAT
M=D
// L23: push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// L24: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// L25: sub
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
// L26: pop argument 0          
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// L27: goto MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
// L28: label END_PROGRAM
(END_PROGRAM)
