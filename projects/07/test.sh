

# python3 VMTranslator.py --vm_filepath MemoryAccess/BasicTest/BasicTest.vm --asm_filepath MemoryAccess/BasicTest/BasicTest.asm
# python3 VMTranslator.py --vm_filepath MemoryAccess/PointerTest/PointerTest.vm --asm_filepath MemoryAccess/PointerTest/PointerTest.asm
# python3 VMTranslator.py --vm_filepath MemoryAccess/StaticTest/StaticTest.vm --asm_filepath MemoryAccess/StaticTest/StaticTest.asm
# python3 VMTranslator.py --vm_filepath StackArithmetic/SimpleAdd/SimpleAdd.vm --asm_filepath StackArithmetic/SimpleAdd/SimpleAdd.asm
# python3 VMTranslator.py --vm_filepath StackArithmetic/StackTest/StackTest.vm --asm_filepath StackArithmetic/StackTest/StackTest.asm
# rm */*/*.asm

python3 VMTranslator.py MemoryAccess/BasicTest/BasicTest.vm
python3 VMTranslator.py MemoryAccess/PointerTest/PointerTest.vm
python3 VMTranslator.py MemoryAccess/StaticTest/StaticTest.vm
python3 VMTranslator.py StackArithmetic/SimpleAdd/SimpleAdd.vm
python3 VMTranslator.py StackArithmetic/StackTest/StackTest.vm
