// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// Put your code here.

// if (R0==0 || R1==0) {R2 = 0}
// else {
// R2=0
// for i in 1,2,..,R0
// R2+=R1
// }

// if part
@R2
M=0

@R0
D=M
@END
D;JEQ

@R1
D=M
@END
D;JEQ

// else part

@i
M=1 // i=1

(LOOP)
@i
D=M
@R0
D=D-M
@END
D;JGT  // if i-R0>0 goto (END)
@R1
D=M
@R2
M=D+M // R2+=R1
@i
M=M+1 // i++
@LOOP
0;JMP // goto (LOOP)

(END)
@END
0;JMP
