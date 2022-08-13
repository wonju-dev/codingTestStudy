INF = int(1e9)

# index X에서 다른 node로 갈 때 드는 비용
# INF = 간선 없음
graph = [
    [0, 4, INF, 6],
    [3, 0, 7, INF],
    [5, INF, 0, 4],
    [INF, INF, 2, 0]
]

for node in range(4):
    for f in range(4):
        for t in range(4):
            graph[f][t] = min((graph[f][t], graph[f][node] + graph[node][t]))

print(graph)