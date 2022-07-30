from collections import deque


n, m = map(int, input().split())
frame = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 1
for _ in range(n):
    frame.append(list(map(int, list(input()))))

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m or frame[nx][ny] == 0:
            continue
    
        if frame[nx][ny] == 1:
            frame[nx][ny] = frame[x][y] + 1
            q.append((nx, ny))

print(frame[n-1][m-1])