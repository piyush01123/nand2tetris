
import argparse
import sys
import random

def commandType(line):
    arithmetic_commands = "add","sub","neg","eq","gt","lt","and","or","not"
    if any(line.startswith(cmd) for cmd in arithmetic_commands):
        return "C_ARITHMETIC"
    if line.startswith("push"):
        return "C_PUSH"
    if line.startswith("pop"):
        return "C_POP"

def arg1(line):
    if commandType(line)=="C_ARITHMETIC":
        return line
    else:
        return line.split(' ')[1]

def arg2(line):
    return int(line.split(' ')[-1])

def segmentPointer(segment):
    if segment=="local":
        return 1
    if segment=="argument":
        return 2
    if segment=="this":
        return 3
    if segment=="that":
        return 4

def push_LCL_ARG_THIS_THAT(segment, i):
    # segment can be one of LCL, ARG, THIS, THAT
    # i is an integer
    seg_ptr = segmentPointer(segment)
    return '\n'.join([
        "@{}".format(seg_ptr),
        "A=M"]+
        ["A=A+1"]*i+[
        "D=M",
        "@0",
        "A=M",
        "M=D",
        "@0",
        "M=M+1"
    ])

def pop_LCL_ARG_THIS_THAT(segment, i):
    seg_ptr = segmentPointer(segment)
    return '\n'.join([
        "@0",
        "M=M-1",
        "A=M",
        "D=M",
        "@{}".format(seg_ptr),
        "A=M"]+
        ["A=A+1"]*i+[
        "M=D",
    ])

def push_constant(i):
    return '\n'.join([
        "@{}".format(i),
        "D=A",
        "@0",
        "A=M",
        "M=D",
        "@0",
        "M=M+1"
    ])

def push_static(i):
    return '\n'.join([
        "@16"]+
        ["A=A+1"]*i+[
        "D=M",
        "@0",
        "A=M",
        "M=D",
        "@0",
        "M=M+1"
    ])

def pop_static(i):
    return '\n'.join([
        "@0",
        "M=M-1",
        "A=M",
        "D=M",
        "@16"]+
        ["A=A+1"]*i+[
        "M=D",
    ])

def push_temp(i):
    return '\n'.join([
        "@5"]+
        ["A=A+1"]*i+[
        "D=M",
        "@0",
        "A=M",
        "M=D",
        "@0",
        "M=M+1"
    ])

def pop_temp(i):
    return '\n'.join([
        "@0",
        "M=M-1",
        "A=M",
        "D=M",
        "@5"]+
        ["A=A+1"]*i+[
        "M=D",
    ])

def push_pointer(i):
    return '\n'.join([
        "@{}".format(3 if i==0 else 4),
        "D=M",
        "@0",
        "A=M",
        "M=D",
        "@0",
        "M=M+1"
    ])

def pop_pointer(i):
    return '\n'.join([
        "@0",
        "M=M-1",
        "A=M",
        "D=M",
        "@{}".format(3 if i==0 else 4),
        "M=D",
    ])


def write_push_pop(asm_file, command_type, segment, i):
    if segment in ["local","argument","this","that"]:
        if command_type=='C_PUSH':
            asm_file.write(push_LCL_ARG_THIS_THAT(segment, i))
        if command_type=='C_POP':
            asm_file.write(pop_LCL_ARG_THIS_THAT(segment, i))
    if segment=='constant':
        assert command_type=='C_PUSH'
        asm_file.write(push_constant(i))
    if segment == "static":
        if command_type=='C_PUSH':
            asm_file.write(push_static(i))
        if command_type=='C_POP':
            asm_file.write(pop_static(i))
    if segment == "temp":
        if command_type=='C_PUSH':
            asm_file.write(push_temp(i))
        if command_type=='C_POP':
            asm_file.write(pop_temp(i))
    if segment == "pointer":
        if command_type=='C_PUSH':
            asm_file.write(push_pointer(i))
        if command_type=='C_POP':
            asm_file.write(pop_pointer(i))
    asm_file.write('\n')
    return


def get_arithmetic_asm(command):
    signs = {"neg":'-', "not":'!'}
    if command in signs.keys():
        return '\n'.join([
            "@0",
            "A=M-1",
            "D=M",
            "D={}D".format(signs[command]),
            "@0",
            "A=M-1",
            "M=D",
        ])
    signs = {"add":'+', "sub":'-', "and":'&', "or":'|'}
    if command in signs.keys():
        return '\n'.join([
            "@0",
            "A=M-1",
            "A=A-1",
            "D=M",
            "@0",
            "A=M-1",
            "D=D{}M".format(signs[command]),
            "@0",
            "A=M-1",
            "A=A-1",
            "M=D",
            "@0",
            "M=M-1"
        ])
    signs = {"gt":"JGT", "lt":"JLT", "eq":"JEQ"}
    rnd = random.randint(0,1000)
    if command in signs.keys():
        return '\n'.join([
            "@0",
            "A=M-1",
            "A=A-1",
            "D=M",
            "@0",
            "A=M-1",
            "D=D-M",
            "@0",
            "A=M-1",
            "A=A-1",
            "M=-1",
            "@DONE{}".format(rnd),
            "D;{}".format(signs[command]),
            "@0",
            "A=M-1",
            "A=A-1",
            "M=0",
            "(DONE{})".format(rnd),
            "@0",
            "M=M-1"
        ])

def write_arithmetic(asm_file, command):
    asm_file.write(get_arithmetic_asm(command))
    asm_file.write('\n')
    return

def main():
    # parser = argparse.ArgumentParser()
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--vm_filepath", required=True)
    # parser.add_argument("--asm_filepath", required=True)
    # args = parser.parse_args()
    # print(args)
    # vm_file = open(args.vm_filepath, 'r')
    # asm_file = open(args.asm_filepath, 'w')

    print(sys.argv)
    vm_file = open(sys.argv[1], 'r')
    asm_file = open(sys.argv[1].replace('.vm', '.asm'), 'w')

    line_number = 0
    for line in vm_file.readlines():
        line = line.strip()
        if line.startswith("//") or len(line)==0:
            continue
        if "//" in line:
            line = line[:line.index('/')]
        asm_file.write('// ')
        asm_file.write("L{}: ".format(line_number))
        asm_file.write(line)
        asm_file.write('\n')
        if commandType(line) in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            print(line_number,line, commandType(line), arg1(line), arg2(line))
            if commandType(line) in ["C_PUSH", "C_POP"]:
                write_push_pop(asm_file, commandType(line), arg1(line), arg2(line))
        else:
            print(line_number,line, commandType(line), arg1(line))
            if commandType(line) == "C_ARITHMETIC":
                write_arithmetic(asm_file, arg1(line))
        line_number += 1

    vm_file.close()
    asm_file.close()


if __name__=="__main__":
    main()
