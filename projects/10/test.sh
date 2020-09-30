
rm */*.xml

# python3 JackAnalyzer.py ExpressionLessSquare
# python3 JackAnalyzer.py Square
# python3 JackAnalyzer.py ArrayTest
#
# ../../tools/TextComparer.sh ExpressionLessSquare/SquareT.xml ExpressionLessSquare/cmp/SquareT.xml
# ../../tools/TextComparer.sh ExpressionLessSquare/SquareGameT.xml ExpressionLessSquare/cmp/SquareGameT.xml
# ../../tools/TextComparer.sh ExpressionLessSquare/MainT.xml ExpressionLessSquare/cmp/MainT.xml
# ../../tools/TextComparer.sh Square/SquareT.xml Square/cmp/SquareT.xml
# ../../tools/TextComparer.sh Square/SquareGameT.xml Square/cmp/SquareGameT.xml
# ../../tools/TextComparer.sh Square/MainT.xml Square/cmp/MainT.xml
# ../../tools/TextComparer.sh ArrayTest/MainT.xml ArrayTest/cmp/MainT.xml


python3 JackAnalyzer.py ExpressionLessSquare/Square.jack
# python3 JackAnalyzer.py ExpressionLessSquare/SquareGame.jack
# python3 JackAnalyzer.py ExpressionLessSquare/Main.jack
#
# python3 JackAnalyzer.py Square/Square.jack
# python3 JackAnalyzer.py Square/SquareGame.jack
# python3 JackAnalyzer.py Square/Main.jack
#
# python3 JackAnalyzer.py ArrayTest/Main.jack
#
../../tools/TextComparer.sh ExpressionLessSquare/Square.xml ExpressionLessSquare/cmp/Square.xml
# ../../tools/TextComparer.sh ExpressionLessSquare/SquareGame.xml ExpressionLessSquare/cmp/SquareGame.xml
# ../../tools/TextComparer.sh ExpressionLessSquare/Main.xml ExpressionLessSquare/cmp/Main.xml
#
# ../../tools/TextComparer.sh Square/Square.xml Square/cmp/Square.xml
# ../../tools/TextComparer.sh Square/SquareGame.xml Square/cmp/SquareGame.xml
# ../../tools/TextComparer.sh Square/Main.xml Square/cmp/Main.xml
#
# ../../tools/TextComparer.sh ArrayTest/Main.xml ArrayTest/cmp/Main.xml
