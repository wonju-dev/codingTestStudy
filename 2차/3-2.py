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
            graph[a][destination - 1] = min((graph[a][destination - 1], graph[a][b] + graph[b][destination - 1]))

    answer = []
    for source in sources:
        distance = graph[source - 1][destination - 1]
        if distance == INF:
            answer.append(-1)
        else:
            answer.append(distance)

    return answer


print(solution(3, [[1,2], [2,3]], [2,3], 1))
print(solution(5, [[1,2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))

