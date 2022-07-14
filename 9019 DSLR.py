from collections import deque

def trimZero(num):
    return num.lstrip("0")

def D(num):
    return str((int(trimZero(num)) * 2) % 10000)

def S(num):
    return str(int(trimZero(num)) - 1) if int(trimZero(num)) -1 != 0 else '9999'

def L(num):
    if len(num) != 4:
        num = "0" * (4 - len(num)) + num
    return num[1:4] + num[0]

def R(num):
    if len(num) != 4:
        num = "0" * (4 - len(num)) + num
    return num[3] + num[0:3]


case = int(input())
for _ in range(case):
    a, b = input().split()
    queue = deque()
    queue.append((a, []))
    
    loop = 0

    while trimZero(queue[0][0]) != b:
        curr, hist = queue.popleft()
        queue.append((D(curr), hist + ['D']))
        queue.append((S(curr), hist + ['S']))
        queue.append((L(curr), hist + ['L']))
        queue.append((R(curr), hist + ['R']))
        
    print("".join(queue[0][1]))