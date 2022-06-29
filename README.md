
# From Nand to Tetris

Build a Computer from First Principles. Coursera course by Shimon Schocken, Noam Nisan (HUJ). This is a project based course that teaches computer architecture by building everything hierarchically starting from just a Nand Gate.

### Contents
(Part 1)
1. Boolean logic
2. Boolean arithmetic and ALU
3. Sequential logic and memory
4. Machine language
5. Von Neuman architecture and  CPU
6. Assembler

(Part 2)

7. VM - Memory and Stack
8. VM - Functions and program flow
9. Jack language practice
10. Compiler - Syntax analysis 
11. Compiler - VM code generation
12. OS


### How to run
Ensure that you have a working Java version by typing `java --version` from Terminal. If it is not installed, then install Java from [here](https://java.com/en/download/manual.jsp). You should now be able to run the emulators by running `*.sh` files in `tools` directory.

Projects 1,2,3 and 5 are to be run on a 'HardwareSimulator'. Load the appropriate HDL script and corresponding test file and it will check for correctness. They contain implementations of Or,Xor,And,Mux,DMux,Bit,Register,RAM,Memory,CPU,Computer.

Project 4 is to practice assembly language. It has to be run on a 'CPUEmulator'.

Project 6 requires us to implement an assembbler in a high-level language of choice. I did it in python. Assembler converts assembly language to binary.

Projects 7 and 8 requires us to implement a VM Translator in a high-level language of choice. I did it in python. VM translator converts vmcode to assembly language.

Project 9 is to practice Jack language by building some fun activities. I implemented a version of Flappy Bird.

Project 10 and 11 requires us to impleement compiler for Jack language. Compiler converts high-level Jack code to VM language.

Project 12 requires us to implement OS in Jack language.

<!-- ### Perspectives:
Though I work in machine learning and specifically in computer vision research area, I have a non-CS college degree. I learned programming on my own and I use it daily for my work. However I always wanted to know internal workings of computer. So I took this course as  a hobby. At the end of part 1, I am reasonably happy with my understanding. Here are the things I learnt:
- Building chips from Nand to Computer with several in between, Or,Xor,And,Mux,DMux,Bit,Register,RAM,Memory,CPU,Computer
- Assembly language
- Built an assembler in java to convert assembly to machine language.
Looking forward to part 2 of the course to learn about further layers of abstraction. -->
