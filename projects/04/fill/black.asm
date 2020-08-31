
// Screen is 256x512 pixels
// Each row can be represented by 32 16-bit numbers and there are 256 such rows

// So to create a full-black screen,
// set RAM[16384], RAM[16385], .. RAM[24575] to -1

@16384
D=A
@i
M=D // i=16384

(LOOP)
@i
A=M
M=-1 // RAM[i]=-1
@i
D=M
@24575
D=D-A
@END
D;JGT // if i-24575>0 goto (END)
@i
M=M+1 // i++
@LOOP
0;JMP

(END)
@END
0;JMP
