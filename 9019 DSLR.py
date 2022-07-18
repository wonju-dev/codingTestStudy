from collections import deque
import sys
input = sys.stdin.readline

def D(num):
    return (2*num)%10000

def S(num):
    return (num-1)%10000

def L(num):
    return (10*num+(num//1000))%10000

def R(num):
    return (num//10+(num%10)*1000)%10000


case = int(input())
for _ in range(case):
    a, b = map(int, input().split())
    
    queue = deque()
    queue.append((a, ""))

    visited = [False] * 10000
    
    while queue[0][0] != b:
        curr, hist = queue.popleft()
        visited[int(curr)] = True

        for nextNum in ((D(curr), hist + 'D'), (S(curr), hist + 'S'), (L(curr), hist + 'L'), (R(curr), hist + 'R')):
            if not visited[nextNum[0]]:
                queue.append((nextNum[0], nextNum[1]))
    print(queue[0][1])