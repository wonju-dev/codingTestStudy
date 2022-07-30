n, m = map(int, input().split())
frame = []
count = 0
for i in range(n):
    frame.append(list(map(int,input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

def dfs(sx, sy):
    if 0 <= sx <= n - 1 and 0 <= sy <= m - 1 and frame[sx][sy] == 0:
        frame[sx][sy] = 2
        for i in range(4):
            dfs(sx + dx[i], sy + dy[i])


for x in range(n):
    for y in range(m):
        if frame[x][y] == 0:
            dfs(x, y)
            count += 1

print(count)