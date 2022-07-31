from collections import deque

l = int(input())

for _ in range(l):
    op = input()
    n = int(input())
    data = list(map(str, input().lstrip("[").rstrip("]").split(",")))
    q = deque(data)

    direction = 1
    good = True

    for i in range(len(op)):
        if op[i] == "R":
            direction = -1 if direction == 1 else 1
        else:
            if len(q) == 0 or q[0] == "":
                print('error')
                good = False
                break
            elif direction == 1:
                q.popleft()
            else:
                q.pop()
    
    if good:
        print("[", end="")
        if direction == 1:
            print(",".join(q), end="")
        else:
            ans = []
            while q:
                ans.append(q.pop())
            print(",".join(ans), end="")
        print("]")