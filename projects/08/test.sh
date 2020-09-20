

rm */*/*.asm

python3 VMTranslator.py ProgramFlow/BasicLoop/BasicLoop.vm
python3 VMTranslator.py ProgramFlow/FibonacciSeries/FibonacciSeries.vm

python3 VMTranslator.py FunctionCalls/SimpleFunction/SimpleFunction.vm
python3 VMTranslator.py FunctionCalls/NestedCall
python3 VMTranslator.py FunctionCalls/FibonacciElement/
python3 VMTranslator.py FunctionCalls/StaticsTest
