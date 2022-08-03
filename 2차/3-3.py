INF = int(1e9)


def getNearestNodeIndex(distance, visited):

    value = INF
    index = 0

    for i in range(1, len(distance)):
        if distance[i] < value and not visited[i]:
            value = distance[i]
            index = i
    
    return index

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    visited[destination] = True
    distance[destination] = 0

    for road in roads:
        a, b = road
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    for connectedNode in graph[destination]:
        nodeNumber, dis = connectedNode
        distance[nodeNumber] = dis

    for _ in range(n - 1):
        nearestNodeIndex = getNearestNodeIndex(distance, visited)
        visited[nearestNodeIndex] = True
        for connectedNode in graph[nearestNodeIndex]:
            nodeNumber, dis = connectedNode
            if distance[nearestNodeIndex] + dis < distance[nodeNumber]:
                distance[nodeNumber] = distance[nearestNodeIndex] + dis

    answer = []

    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])

    return answer
