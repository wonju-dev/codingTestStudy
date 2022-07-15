from collections import deque

def trimZero(num):
    result = str(num).lstrip("0")
    return result if result != "" else "0"

def D(num):
    return str((int(num) * 2) % 10000)

def S(num):
    result = str(int(num) - 1)
    return result if int(result) > 0 else '9999'

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
    numberAndWord = [False for _ in range(10001)]
    queue = deque()
    queue.append((a, ""))
    
    while trimZero(queue[0][0]) != b:
        curr, hist = queue.popleft()
        numberAndWord[int(curr)] = True

        for nextNum in ((D(curr), hist + 'D'), (S(curr), hist + 'S'), (L(curr), hist + 'L'), (R(curr), hist + 'R')):
            if 0 <= int(nextNum[0]) <= 9999 and not numberAndWord[int(nextNum[0])]:
                queue.append((trimZero(nextNum[0]), nextNum[1]))
        
    print("".join(queue[0][1]))