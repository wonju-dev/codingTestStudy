def getNearestNode():
    global distance
    global visited

    index = 0
    minValue = INF
    
    for i in range(2, 6):
        if distance[i] <= minValue and not visited[i]:
            minValue = distance[i]
            index = i

    return index


graph = [
    [(1,2), (3,1), (2,5)],
    [(2,3), (3, 2)],
    [(1,3)],
    [(2,3), (4, 1)],
    [(2,1), (5,2)],
    []
]

# 0번 node에서 다른 node들 까지의 거리
INF = int(1e9)
distance = [0] + [INF] * 5
# node 방문 여부 확인
visited = [True] + [False] * 5
# 0번 노드(시작점) 처리
for connection in graph[0]:
    node, dis = connection
    distance[node] = dis

# 1 ~ 6번 노드에 대해 검증
for i in range(1, 6):
    nearestNode = getNearestNode()
    visited[nearestNode] = True
    for connection in graph[nearestNode]:
        node, dis = connection
        if distance[node] > distance[nearestNode] + dis:
            distance[node] = distance[nearestNode] + dis

print(distance)