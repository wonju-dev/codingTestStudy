n = int(input())

for q in range(n):
    ps = input()
    stack = []
    openCount = 0
    closeCount = 0
    wrong = False
    for i in range(len(ps)):
        if ps[i] == "(":
            stack.append(ps[i])
            openCount += 1
        elif ps[i] == ")" and len(stack) != 0:
            stack.pop()
            closeCount += 1
        else:
            wrong = True
            break
    if openCount != closeCount or len(stack) != 0 or wrong:
        print("NO")
    else:
        print("YES")
