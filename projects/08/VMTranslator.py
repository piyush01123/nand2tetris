
import argparse
import sys
import random
import os

def commandType(line):
    arithmetic_commands = "add","sub","neg","eq","gt","lt","and","or","not"
    if any(line.startswith(cmd) for cmd in arithmetic_commands):
        return "C_ARITHMETIC"
    if line.startswith("push"):
        return "C_PUSH"
    if line.startswith("pop"):
        return "C_POP"
    if line.startswith("label"):
        return "C_LABEL"
    if line.startswith("goto"):
        return "C_GOTO"
    if line.startswith("if-goto"):
        return "C_IFGOTO"
    if line.startswith("function"):
        return "C_FUNCTION"
    if line.startswith("call"):
        return "C_CALL"
    if line.startswith("return"):
        return "C_RETURN"

def arg1(line):
    return line.split(' ')[1]

def arg2(line):
    return int(line.split(' ')[2].strip('//').strip('\t'))

def segmentPointer(segment):
    if segment=="local":
        return "LCL"
    if segment=="argument":
        return "ARG"
    if segment=="this":
        return "THIS"
    if segment=="that":
        return "THAT"

def push_LCL_ARG_THIS_THAT(segment, i):
    # segment can be one of LCL, ARG, THIS, THAT
    # i is an integer
    seg_ptr = segmentPointer(segment)
    return '\n'.join([
        "@{}".format(seg_ptr),
        "A=M"]+
        ["A=A+1"]*i+[
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

def pop_LCL_ARG_THIS_THAT(segment, i):
    seg_ptr = segmentPointer(segment)
    return '\n'.join([
        "@SP",
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
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

def push_static(i, vm_filename):
    return '\n'.join([
        "@{}.{}".format(vm_filename, i),
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

def pop_static(i, vm_filename):
    return '\n'.join([
        "@SP",
        "M=M-1",
        "A=M",
        "D=M",
        "@{}.{}".format(vm_filename, i),
        "M=D",
    ])

def push_temp(i):
    return '\n'.join([
        "@5"]+
        ["A=A+1"]*i+[
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

def pop_temp(i):
    return '\n'.join([
        "@SP",
        "M=M-1",
        "A=M",
        "D=M",
        "@5"]+
        ["A=A+1"]*i+[
        "M=D",
    ])

def push_pointer(i):
    return '\n'.join([
        "@{}".format("THIS" if i==0 else "THAT"),
        "D=M",
        "@SP",
        "A=M",
        "M=D",
        "@SP",
        "M=M+1"
    ])

def pop_pointer(i):
    return '\n'.join([
        "@SP",
        "M=M-1",
        "A=M",
        "D=M",
        "@{}".format("THIS" if i==0 else "THAT"),
        "M=D",
    ])


def write_push_pop(asm_file, command_type, segment, i, vm_file):
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
            asm_file.write(push_static(i, vm_file.name.split('/')[-1].split('.vm')[0]))
        if command_type=='C_POP':
            asm_file.write(pop_static(i, vm_file.name.split('/')[-1].split('.vm')[0]))
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
            "@SP",
            "A=M-1",
            "D=M",
            "D={}D".format(signs[command]),
            "@SP",
            "A=M-1",
            "M=D",
        ])
    signs = {"add":'+', "sub":'-', "and":'&', "or":'|'}
    if command in signs.keys():
        return '\n'.join([
            "@SP",
            "A=M-1",
            "A=A-1",
            "D=M",
            "@SP",
            "A=M-1",
            "D=D{}M".format(signs[command]),
            "@SP",
            "A=M-1",
            "A=A-1",
            "M=D",
            "@SP",
            "M=M-1"
        ])
    signs = {"gt":"JGT", "lt":"JLT", "eq":"JEQ"}
    rnd = random.randint(0,1000)
    if command in signs.keys():
        return '\n'.join([
            "@SP",
            "A=M-1",
            "A=A-1",
            "D=M",
            "@SP",
            "A=M-1",
            "D=D-M",
            "@SP",
            "A=M-1",
            "A=A-1",
            "M=-1",
            "@DONE{}".format(rnd),
            "D;{}".format(signs[command]),
            "@SP",
            "A=M-1",
            "A=A-1",
            "M=0",
            "(DONE{})".format(rnd),
            "@SP",
            "M=M-1"
        ])

def write_arithmetic(asm_file, command):
    asm_file.write(get_arithmetic_asm(command))
    asm_file.write('\n')
    return

def write_label(asm_file, label):
    asm_file.write("({})\n".format(label))

def write_goto(asm_file, label):
    asm_file.write('\n'.join([
        "@{}".format(label),
        "0;JMP"
    ]))
    asm_file.write('\n')

def write_ifgoto(asm_file, label):
    asm_file.write('\n'.join([
        "@SP",
        "M=M-1",
        "A=M",
        "D=M",
        "@{}".format(label),
        "D;JNE"
    ]))
    asm_file.write('\n')

def write_call(asm_file, function_name, nArgs):
    asm_file.flush()
    num_lines = 0
    for line in open(asm_file.name, 'r'):
        if line.startswith('(') or line.startswith('//'):
            continue
        else:
            num_lines+=1
    print("NUM_LINES:", num_lines)

    def push_address(address):
        return '\n'.join([
            "@{}".format(address),
            "D=M",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ])

    asm_file.write('\n'.join([
        push_constant(num_lines + 7*5 + 10 + nArgs + 5),
        push_address("LCL"),
        push_address("ARG"),
        push_address("THIS"),
        push_address("THAT"),
        "@SP",
        "D=M"] + ["D=D-1"]*5 + ["D=D-1"]*nArgs + [
        "@ARG",
        "M=D", # ARG=SP-5-nArgs

        "@SP",
        "D=M",
        "@LCL",
        "M=D", #LCL=SP

        "@{}".format(function_name),
        "0;JMP"
    ]))
    asm_file.write('\n')


def write_function(asm_file, function_name, nVars):
    asm_file.write('\n'.join([
        "({})".format(function_name)]+
        [push_constant(0)]*nVars
    ))
    asm_file.write('\n')

def write_return(asm_file):
    asm_file.write('\n'.join([
        "@LCL",
        "D=M",
        "@R13",
        "M=D", # RAM[13] = LCL (endFrame)

        "@LCL",
        "D=M",] + ["D=D-1"]*5 +[
        "A=D",
        "D=M",
        "@R14",
        "M=D", # RAM[14] = returnAddress (endFrame)

        "@SP",
        "M=M-1",
        "A=M",
        "D=M",
        "@ARG",
        "A=M",
        "M=D", # *ARG=pop() (returnValue)

        "@ARG",
        "D=M",
        "@SP",
        "M=D+1", # SP=ARG+1

        "@R13",
        "M=M-1",
        "A=M",
        "D=M",
        "@THAT",
        "M=D",

        "@R13",
        "M=M-1",
        "A=M",
        "D=M",
        "@THIS",
        "M=D",

        "@R13",
        "M=M-1",
        "A=M",
        "D=M",
        "@ARG",
        "M=D",

        "@R13",
        "M=M-1",
        "A=M",
        "D=M",
        "@LCL",
        "M=D",

        "@R14",
        "A=M",
        "0;JMP" # control goes to the line after function call

    ]))
    asm_file.write('\n')

def write_assembly(vm_file, asm_file):
    line_number = 0
    for line in vm_file.readlines():
        line = line.strip()
        if line.startswith("//") or len(line)==0:
            continue
        if '//' in line:
            line = line[:line.index('//')]

        asm_file.write('// ')
        asm_file.write("L{}: ".format(line_number))
        asm_file.write(line)
        asm_file.write('\n')

        if commandType(line) in ["C_PUSH", "C_POP", "C_FUNCTION", "C_CALL"]:
            print(line_number, "CT:", commandType(line), "ARG1:", arg1(line), "ARG2:", arg2(line))
            if commandType(line) in ["C_PUSH", "C_POP"]:
                write_push_pop(asm_file, commandType(line), arg1(line), arg2(line), vm_file)
            if commandType(line) == "C_FUNCTION":
                write_function(asm_file, arg1(line), arg2(line))
            if commandType(line) == "C_CALL":
                write_call(asm_file, arg1(line), arg2(line))
        else:
            print(line_number, "CT:", commandType(line))
            if commandType(line) == "C_ARITHMETIC":
                write_arithmetic(asm_file, line.strip())
            if commandType(line) == "C_LABEL":
                write_label(asm_file, arg1(line))
            if commandType(line) == "C_GOTO":
                write_goto(asm_file, arg1(line))
            if commandType(line) == "C_IFGOTO":
                write_ifgoto(asm_file, arg1(line))
            if commandType(line) == "C_RETURN":
                write_return(asm_file)
        line_number += 1


def main():
    if len(sys.argv) != 2:
        raise ValueError("Less arguments")

    if os.path.isfile(sys.argv[1]):
        vm_filename = sys.argv[1]
        asm_filename = vm_filename.replace('.vm', '.asm')
        vm_file = open(vm_filename, 'r')
        asm_file = open(asm_filename, 'w')
        write_assembly(vm_file, asm_file)
        vm_file.close()
        asm_file.close()

    if os.path.isdir(sys.argv[1]):
        vm_dirname = sys.argv[1]
        dir = vm_dirname.split('/')[-1]
        if dir == "":
            dir = vm_dirname.split('/')[-2]
        asm_filename = os.path.join(vm_dirname, "{}.asm".format(dir))

        vm_filenames = [f for f in os.listdir(vm_dirname) if f.endswith('.vm')]
        i = vm_filenames.index("Sys.vm")
        vm_filenames = ["Sys.vm"] + vm_filenames[:i] + vm_filenames[i+1:]

        asm_file = open(asm_filename, 'w')
        # asm_file.write('\n'.join([
        #     "@SP",
        #     "D=M",
        #     "@SETSP",
        #     "D;JEQ",
        #     "@DONTSET",
        #     "0;JMP",
        #     "(SETSP)",
        #     "@SP",
        #     "M=0"]+["M=M+1"]*261+[
        #     "(DONTSET)"
        # ]))
        asm_file.write('\n'.join([
            "@SP",
            "M=0"]+["M=M+1"]*261
        ))
        asm_file.write('\n')
        for vm_filename in vm_filenames:
            if vm_filename.endswith('.vm'):
                vm_file = open(os.path.join(vm_dirname, vm_filename), 'r')
                write_assembly(vm_file, asm_file)
                vm_file.close()
        asm_file.close()


if __name__=="__main__":
    main()
