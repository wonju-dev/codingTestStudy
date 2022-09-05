n = int(input())
m = int(input())

# 데이터 초기화
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
    graph[i][i] = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            graph[b][c] = min((graph[b][c], graph[b][a] + graph[a][c]))

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if graph[row][col] == INF:
            print(0, end=" ")
        else:
            print(graph[row][col], end=" ")
    print()

