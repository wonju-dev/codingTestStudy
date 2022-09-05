n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a][b] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            graph[b][c] = min((graph[b][c], graph[b][a] + graph[a][c]))

count = 0 
for node in range(1, n + 1):
    visited = [True] + [False] * n
    visited[node] = True
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if row == node or col == node:
                if graph[row][col] != INF:
                    if row == node:
                        visited[col] = True
                    else:
                        visited[row] = True
    if False not in visited:
        count += 1

print(count)