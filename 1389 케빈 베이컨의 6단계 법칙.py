INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    graph[i][i] = 0
    
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min([graph[a][b], graph[a][i] + graph[i][b]])

index = 1
for i in range(2, n + 1):
    if sum(graph[i]) < sum(graph[index]):
        index = i
print(index)