case = int(input())

while case > 0:

    length = int(input())
    chunks = input().split()

    opStack = []
    outStack = []

    for chunk in chunks:
        if chunk in ["*", "("]:
            opStack.append(chunk)
        elif chunk in ["+", "-"]:
            if len(opStack) == 0:
                opStack.append(chunk)
            else:
                while opStack[-1] == "*":
                    outStack.append(opStack.pop())
                opStack.append(chunk)
        elif chunk == ")":
            while opStack[-1] != "(":
                outStack.append(opStack.pop())
            opStack.pop()
        else:
            outStack.append(chunk)

        # print(opStack, outStack)

    while len(opStack) != 0:
        outStack.append(opStack.pop())

    temp = []
    for chunk in outStack:
        if chunk.isdecimal():
            # print(chunk, type(chunk))

            temp.append(chunk)
        else:
            op2 = int(temp.pop())
            op1 = int(temp.pop())

            if chunk == "+":
                temp.append(op1 + op2)
            elif chunk == "-":
                temp.append(op1 - op2)
            elif chunk == "*":
                temp.append(op1 * op2)
    
    print(temp[0])
    
    case -=1

"""
2 + 2 * 2
( 2 + 2 ) * 2
( ( 2 + 3 ) * 2 ) * 2
2 - 3
"""