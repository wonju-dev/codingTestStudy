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
    
    q = deque()
    q.append((a, ""))

    visited = [False] * 10000
    
    while q:
        curr, hist = q.popleft()

        if curr == b:
            print(hist)
            break

        for nextPair in ((D(curr), hist + 'D'), (S(curr), hist + 'S'), (L(curr), hist + 'L'), (R(curr), hist + 'R')):
            if not visited[nextPair[0]]:
                visited[nextPair[0]] = True
                q.append(nextPair)