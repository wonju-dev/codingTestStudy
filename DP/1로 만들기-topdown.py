# 하다보니 재귀가 아니고 BFS로 구현했다
from collections import deque


n = int(input())
q = deque()
q.append((n, 0))

while q:
    num, count = q.popleft()

    if num == 1:
        print(count)
        break

    if num % 5 == 0:
        q.append((num // 5, count + 1))
    if num % 3 == 0:
        q.append((num // 3, count + 1))
    if num % 2 == 0:
        q.append((num // 2, count + 1))
    q.append((num - 1, count + 1))
