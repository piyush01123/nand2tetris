

import argparse

def get_dest_bits(dest):
    dest_bits = ['0','0','0']
    if 'A' in dest:
        dest_bits[0] = '1'
    if 'D' in dest:
        dest_bits[1] = '1'
    if 'M' in dest:
        dest_bits[2] = '1'
    return ''.join(dest_bits)

def get_comp_bits(comp):
    comp_dict = {
    '0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', '!D':'0001101', '-D':'0001111', 'D+1':'0011111', 'D-1':'0001110',
    'A':'0110000', '!A':'0110001', '-A':'0110011', 'A+1':'0110111', 'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101',
    'M':'1110000', '!M':'1110001', '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010', 'D-M':'1010011', 'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101',
    }
    return comp_dict[comp]

def get_jump_bits(jump):
    if jump=='JMP':
        return '111';
    if jump=='JNE':
        return '101';
    jump_bits = ['0','0','0']
    if 'L' in jump:
        jump_bits[0] = '1'
    if 'E' in jump:
        jump_bits[1] = '1'
    if 'G' in jump:
        jump_bits[2] = '1'
    return ''.join(jump_bits)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--asm_filepath", required=True)
    parser.add_argument("--mac_filepath", required=True)
    args = parser.parse_args()
    asm_file = open(args.asm_filepath, 'r')
    mac_file = open(args.mac_filepath, 'w')

    symbol_table = {
        "R0":0, "R1":1, "R2":2, "R3":3, "R4":4, "R5":5, "R6":6, "R7":7, "R8":8,
        "R9":9, "R10":10, "R11":11, "R12":12, "R13":13, "R14":14, "R15":15,
        "SP":0, "LCL":1, "ARG":2, "THIS":3, "THAT":4,"SCREEN":16384,"KBD":24576
    }

    line_number = 0
    for line in asm_file.readlines():
        line = line.strip()
        if line.startswith("//") or len(line)==0:
            continue
        if "//" in line:
            line = line[:line.index('/')]
        line = line.replace(' ', '')
        # print(line_number,line)

        if line.startswith('(') and line.endswith(')'):
            label = line[1:-1]
            symbol_table[label] = line_number
        else:
            line_number += 1

    # print(symbol_table)
    asm_file = open(args.asm_filepath, 'r')

    n = 16
    for line in asm_file.readlines():
        line = line.strip()
        if line.startswith("//") or len(line)==0:
            continue
        if "//" in line:
            line = line[:line.index('/')]
        line = line.replace(' ', '')
        if line.startswith('(') and line.endswith(')'):
            continue
        if line.startswith('@'):
            # print("A-instruction", line)
            # A-instruction
            value = line[1:]
            try:
                addrs = int(value)
            except:
                if value in symbol_table.keys():
                    pass
                else:
                    symbol_table[value] = n
                    n = n+1
                    # print(symbol_table)
                addrs = symbol_table[value]
            addrs_bin = bin(addrs)
            addrs_bin = '0'*(16-len(addrs_bin[2:])) + addrs_bin[2:]
            # print(addrs_bin, len(addrs_bin))
            mac_file.write(addrs_bin)
            mac_file.write('\n')
        else:
            # print("C-instruction", line)
            # C-instruction
            if '=' not in line:
                dest_bits = '000'
            else:
                dest, _ = line.split('=')
                dest_bits = get_dest_bits(dest)
                # print(line, "Dest", dest, dest_bits)
                line = line[line.index('=')+1:]
            if ';' not in line:
                jump_bits = '000'
            else:
                _, jump = line.split(';')
                jump_bits = get_jump_bits(jump)
                # print(line, "Jump", jump, jump_bits)
                line = line[:line.index(';')]
            comp_bits = get_comp_bits(line)
            # print("comp_bits", comp_bits, "dest_bits", dest_bits, "jump_bits", jump_bits)
            mac_file.write("111"+comp_bits+dest_bits+jump_bits)
            mac_file.write('\n')
    asm_file.close()
    mac_file.close()

if __name__ == "__main__":
    main()
