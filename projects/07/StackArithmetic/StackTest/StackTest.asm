// L0: push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// L1: push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// L2: eq
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
M=-1
@DONE263
D;JEQ
@0
A=M-1
A=A-1
M=0
(DONE263)
@0
M=M-1
// L3: push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// L4: push constant 16
@16
D=A
@0
A=M
M=D
@0
M=M+1
// L5: eq
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
M=-1
@DONE227
D;JEQ
@0
A=M-1
A=A-1
M=0
(DONE227)
@0
M=M-1
// L6: push constant 16
@16
D=A
@0
A=M
M=D
@0
M=M+1
// L7: push constant 17
@17
D=A
@0
A=M
M=D
@0
M=M+1
// L8: eq
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
M=-1
@DONE179
D;JEQ
@0
A=M-1
A=A-1
M=0
(DONE179)
@0
M=M-1
// L9: push constant 892
@892
D=A
@0
A=M
M=D
@0
M=M+1
// L10: push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// L11: lt
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
M=-1
@DONE767
D;JLT
@0
A=M-1
A=A-1
M=0
(DONE767)
@0
M=M-1
// L12: push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// L13: push constant 892
@892
D=A
@0
A=M
M=D
@0
M=M+1
// L14: lt
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
M=-1
@DONE52
D;JLT
@0
A=M-1
A=A-1
M=0
(DONE52)
@0
M=M-1
// L15: push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// L16: push constant 891
@891
D=A
@0
A=M
M=D
@0
M=M+1
// L17: lt
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
M=-1
@DONE625
D;JLT
@0
A=M-1
A=A-1
M=0
(DONE625)
@0
M=M-1
// L18: push constant 32767
@32767
D=A
@0
A=M
M=D
@0
M=M+1
// L19: push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// L20: gt
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
M=-1
@DONE26
D;JGT
@0
A=M-1
A=A-1
M=0
(DONE26)
@0
M=M-1
// L21: push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// L22: push constant 32767
@32767
D=A
@0
A=M
M=D
@0
M=M+1
// L23: gt
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
M=-1
@DONE726
D;JGT
@0
A=M-1
A=A-1
M=0
(DONE726)
@0
M=M-1
// L24: push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// L25: push constant 32766
@32766
D=A
@0
A=M
M=D
@0
M=M+1
// L26: gt
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
M=-1
@DONE364
D;JGT
@0
A=M-1
A=A-1
M=0
(DONE364)
@0
M=M-1
// L27: push constant 57
@57
D=A
@0
A=M
M=D
@0
M=M+1
// L28: push constant 31
@31
D=A
@0
A=M
M=D
@0
M=M+1
// L29: push constant 53
@53
D=A
@0
A=M
M=D
@0
M=M+1
// L30: add
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
// L31: push constant 112
@112
D=A
@0
A=M
M=D
@0
M=M+1
// L32: sub
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
// L33: neg
@0
A=M-1
D=M
D=-D
@0
A=M-1
M=D
// L34: and
@0
A=M-1
A=A-1
D=M
@0
A=M-1
D=D&M
@0
A=M-1
A=A-1
M=D
@0
M=M-1
// L35: push constant 82
@82
D=A
@0
A=M
M=D
@0
M=M+1
// L36: or
@0
A=M-1
A=A-1
D=M
@0
A=M-1
D=D|M
@0
A=M-1
A=A-1
M=D
@0
M=M-1
// L37: not
@0
A=M-1
D=M
D=!D
@0
A=M-1
M=D
