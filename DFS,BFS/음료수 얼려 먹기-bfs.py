from collections import deque


n, m = map(int, input().split())
frame = []
count = 0
for i in range(n):
    frame.append(list(map(int,input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))

    while len(q) != 0:
        x, y = q.popleft()
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX <= n - 1 and 0 <= nextY <= m - 1 and frame[nextX][nextY] == 0:
                frame[nextX][nextY] = 2
                q.append((nextX, nextY))

for x in range(n):
    for y in range(m):
        if frame[x][y] == 0:
            bfs(x, y)
            count += 1

print(count)