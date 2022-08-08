def solution(n, roads, sources, destination):
    INF = int(1e9)
    graph = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for pair in roads:
        a, b = pair
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 1

    for a in range(n):
        for b in range(n):
            for c in range(n):
                graph[b][c] = min((graph[b][c], graph[b][a] + graph[a][c]))

    answer = []
    for source in sources:
        answer.append(graph[source - 1][destination - 1])

    return answer

print(solution(3, [[1,2], [2,3]], [2,3], 1))