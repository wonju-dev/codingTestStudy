import heapq

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
    distance = [INF] * (n + 1)

    for road in roads:
        a, b = road
        # (도착, 비용)
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    # 시작점에 대한 초기화
    q = []
    distance[destination] = 0
    # (도착지로 가는 비용 = 가장 가까운 노드, 도착지) 우선순위 큐 삽입
    heapq.heappush(q, (0, destination))
    
    # 시작점에 대한 초기화
    for connectedNode in graph[destination]:
        nodeNumber, dis = connectedNode
        distance[nodeNumber] = dis

    while q:
        dist, node = heapq.heappop(q)

        # 원래 가려는 비용이 더 싸면 그냥 무시
        if distance[node] < dist:
            continue
    
        # 현재 노드와 연결된 노드들에 대해
        for connectedNode in graph[node]:
            # 다음 노드로 가기 위한 비용
            costToGoNext = dist + connectedNode[1]
            # 현재노드에서 다음 노드를 거쳐가는 비용 vs destination에서 바로 가는 비용
            if costToGoNext <= distance[connectedNode[0]]:
                distance[connectedNode[0]] = costToGoNext
                heapq.heappush(q, (costToGoNext, connectedNode[0]))

    answer = []
    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])

    return answer

print(solution(3, [[1,2], [2, 3]], [2,3], 1))
print(solution(5, [[1,2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))