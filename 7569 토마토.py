from collections import deque
import sys
input = sys.stdin.readline

m, n, h= map(int, input().split())
graph = []
visited = []
for _ in range(h):
    stage = []
    visit = []
    for __ in range(n):
        stage.append(list(map(int, input().split())))
        visit.append([False] * m)
    graph.append(stage)
    visited.append(visit)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dz = [-1, 1]

isAllRiped = True
lastDay = 0

q = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                # x 좌표, y좌표, 날짜
                q.append((z, x, y, 1))
                graph[z][x][y] = 1
                visited[z][x][y] = True
            elif graph[z][x][y] == 0:
                isAllRiped = False

while q:
    z, x, y, d = q.popleft()

    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]

        if 0 <= nextX < n and 0 <= nextY < m and not visited[z][nextX][nextY] and graph[z][nextX][nextY] == 0:
            graph[z][nextX][nextY] = 1
            visited[z][nextX][nextY] = True
            q.append((z, nextX, nextY, d + 1))
    
    for i in range(2):
        nextZ = z + dz[i]
        if 0 <= nextZ < h and not visited[nextZ][x][y] and graph[nextZ][x][y] == 0:
            graph[nextZ][x][y] = 1
            visited[nextZ][x][y] = True
            q.append((nextZ, x, y, d + 1))

    if len(q) == 0:
        lastDay = d - 1

if isAllRiped:
    print(0)
else:

    isNotPossible = False
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    isNotPossible = True
                    break
    
    if isNotPossible:
        print(-1)
    else:
        print(lastDay)