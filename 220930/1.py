# 후위 표기법

case = int(input())

while case > 0:

    chunks = input().split()
    length = int(input())
    numbers = []
    operators = []

    for chunk in chunks:
        if chunk in ["+", "-", "*", "(", ")"]:
            operators.append(chunk)
        else:
            numbers.append(int(chunk))

    case -=1

"""
2 + 2 * 2
( 2 + 2 ) * 2
( ( 2 + 3 ) * 2 ) * 2
2 - 3
"""