from collections import deque


n = int(input())
graph = [[] for _ in range(n)]
canGo = [[0] * n for _ in range(n)]

for i in range(n):
    value = list(map(int, input().split()))
    for j in range(len(value)):
        if value[j] == 1:
            graph[i].append(j)

for presentNode in range(n):
    q = deque()
    visited = [False for _ in range(n)]

    for node in graph[presentNode]:
        q.append(node)

    while q:
        nextNode = q.popleft()
        if not visited[nextNode]:
            visited[nextNode] = True
            canGo[presentNode][nextNode] = 1
            for node in graph[nextNode]:
                q.append(node)

for row in canGo:
    for i in range(len(row)):
        if i != len(row) - 1:
            print(row[i], end=" ")
        else:
            print(row[i])