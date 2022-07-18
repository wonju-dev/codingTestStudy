import sys

n = int(sys.stdin.readline())

mySet = "0" * 21
for _ in range(n):
    rows = list(sys.stdin.readline().split())
    op = op = rows[0]

    num = 1
    if len(rows) == 2 :
        num = int(rows[1])

    if op == 'add':
        mySet = mySet[:num] + "1" + mySet[num+1 :]
    elif op == 'check':
        print(1 if mySet[num] == "1" else 0)
    elif op == 'remove':
        mySet = mySet[:num] + "0" + mySet[num+1 :]
    elif op == 'toggle':
        if mySet[num] == "1":
            mySet = mySet[:num] + "0" + mySet[num+1 :]
        else :
            mySet = mySet[:num] + "1" + mySet[num+1 :]
    elif op == 'all':
        mySet = "1" * 21
    elif op == 'empty':
        mySet = "0" * 21