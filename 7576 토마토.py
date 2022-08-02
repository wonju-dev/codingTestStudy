from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
visited = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    visited.append([False] * m)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

isAllRiped = True
lastDay = 0

q = deque()

for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            # x 좌표, y좌표, 날짜
            q.append((x, y, 1))
            graph[x][y] = 1
            visited[x][y] = True
        elif graph[x][y] == 0:
            isAllRiped = False

while q:
    x, y, d = q.popleft()

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        if 0 <= nextX < n and 0 <= nextY < m and not visited[nextX][nextY] and graph[nextX][nextY] == 0:
            graph[nextX][nextY] = 1
            visited[nextX][nextY] = True
            q.append((nextX, nextY, d + 1))

    if len(q) == 0:
        lastDay = d - 1

if isAllRiped:
    print(0)
else:

    isNotPossible = False
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                isNotPossible = True
                break
    
    if isNotPossible:
        print(-1)
    else:
        print(lastDay)