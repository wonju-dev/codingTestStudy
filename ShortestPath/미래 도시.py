INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(n):
    graph[i][i] = 0

x, k = map(int, input().split())

for a in range(n):
    for b in range(n):
        for c in range(n):
            graph[b][c] = min([graph[b][c], graph[b][a] + graph[a][c]])

distance = graph[0][x] + graph[x][k]

if distance >= INF:
    print(-1)
else:
    print(distance)